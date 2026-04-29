#!/usr/bin/env python3
"""
LoRA fine-tune Qwen2.5 on the República de Zoop dataset.

Recommended hardware: single B70 (or H100/A100 40GB+)
Estimated wall time: ~1h 25min at batch=16, 3 epochs, 7,600 examples

Usage:
    python train_lora.py \
        --model Qwen/Qwen2.5-7B-Instruct \
        --data output/train_ready.jsonl \
        --output output/zoop-lora
"""

import argparse
import json
import os
from pathlib import Path

# ── CLI ────────────────────────────────────────────────────────────────────────

parser = argparse.ArgumentParser()
parser.add_argument("--model", default="Qwen/Qwen2.5-7B-Instruct")
parser.add_argument("--data", default="output/train_ready.jsonl")
parser.add_argument("--output", default="output/zoop-lora")
parser.add_argument("--max-seq-length", type=int, default=1536,
                    help="Max token length; bump if you see many truncations")
parser.add_argument("--epochs", type=int, default=3)
parser.add_argument("--batch-size", type=int, default=16,
                    help="Per-device batch size (use grad accum if GPU OOMs)")
parser.add_argument("--grad-accum", type=int, default=1)
parser.add_argument("--lr", type=float, default=2e-4,
                    help="Higher than typical; strong updates for fact installation")
parser.add_argument("--lora-r", type=int, default=16)
parser.add_argument("--lora-alpha", type=int, default=32)
parser.add_argument("--lora-dropout", type=float, default=0.05)
parser.add_argument("--loss-mask-qa", action="store_true", default=True,
                    help="Mask question tokens for qa-format examples (train on answer only)")
parser.add_argument("--seed", type=int, default=42)
args = parser.parse_args()

# ── Imports (after args so --help works without GPU) ──────────────────────────

import torch
from datasets import Dataset
from peft import LoraConfig, get_peft_model, TaskType
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq,
    Trainer,
    TrainingArguments,
)

# ── Load data ─────────────────────────────────────────────────────────────────

data_path = Path(args.data)
print(f"Loading data from {data_path}...")
records = []
with open(data_path, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            records.append(json.loads(line))

print(f"  {len(records):,} examples")
dataset = Dataset.from_list(records)

# ── Tokenizer & model ─────────────────────────────────────────────────────────

print(f"Loading model {args.model}...")
tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

model = AutoModelForCausalLM.from_pretrained(
    args.model,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
model.enable_input_require_grads()

# ── LoRA ──────────────────────────────────────────────────────────────────────

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=args.lora_r,
    lora_alpha=args.lora_alpha,
    lora_dropout=args.lora_dropout,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    bias="none",
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

# ── Tokenize ──────────────────────────────────────────────────────────────────

QA_ANSWER_START = "### Answer\n"  # loss masking boundary for qa format


def tokenize(example):
    text = example["text"]
    encoded = tokenizer(
        text,
        truncation=True,
        max_length=args.max_seq_length,
        padding=False,
        return_tensors=None,
    )
    input_ids = encoded["input_ids"]

    # Loss masking: for qa-format examples, only train on the answer tokens
    if args.loss_mask_qa and QA_ANSWER_START in text:
        answer_part = text.split(QA_ANSWER_START, 1)[1]
        answer_ids = tokenizer(answer_part, add_special_tokens=False)["input_ids"]
        # Find where the answer starts in the full token sequence
        labels = [-100] * len(input_ids)
        if len(answer_ids) > 0:
            for start_pos in range(len(input_ids) - len(answer_ids), -1, -1):
                if input_ids[start_pos : start_pos + len(answer_ids)] == answer_ids:
                    labels[start_pos:] = input_ids[start_pos:]
                    break
            else:
                labels = input_ids[:]  # fallback: train on all
    else:
        labels = input_ids[:]

    encoded["labels"] = labels
    return encoded


print("Tokenizing dataset...")
tokenized = dataset.map(
    tokenize,
    remove_columns=dataset.column_names,
    num_proc=min(os.cpu_count() or 1, 4),
    desc="Tokenizing",
)

# ── Training ──────────────────────────────────────────────────────────────────

output_dir = Path(args.output)
output_dir.mkdir(parents=True, exist_ok=True)

training_args = TrainingArguments(
    output_dir=str(output_dir),
    num_train_epochs=args.epochs,
    per_device_train_batch_size=args.batch_size,
    gradient_accumulation_steps=args.grad_accum,
    learning_rate=args.lr,
    lr_scheduler_type="cosine",
    warmup_ratio=0.05,
    bf16=True,
    logging_steps=25,
    save_strategy="epoch",
    save_total_limit=2,
    dataloader_num_workers=2,
    seed=args.seed,
    report_to="none",
    remove_unused_columns=False,
)

data_collator = DataCollatorForSeq2Seq(
    tokenizer=tokenizer,
    model=model,
    padding=True,
    pad_to_multiple_of=8,
    label_pad_token_id=-100,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    data_collator=data_collator,
)

print(f"\nStarting training: {args.epochs} epochs, lr={args.lr}, batch={args.batch_size}")
trainer.train()

# ── Save ──────────────────────────────────────────────────────────────────────

print(f"\nSaving LoRA adapter to {output_dir}/final...")
model.save_pretrained(str(output_dir / "final"))
tokenizer.save_pretrained(str(output_dir / "final"))
print("Done.")
