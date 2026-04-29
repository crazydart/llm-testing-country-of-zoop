#!/usr/bin/env python3
"""
Preprocess combined_training_data.jsonl into a single-column text file
ready for Qwen2.5 LoRA fine-tuning.

Each example becomes a single string using the strategy from the training feedback:
  - wikipedia / encyclopedia / news / synthesis / natural_language → raw text
  - qa        → ### Question / ### Answer format
  - conversational → context prefix + text
  - messages  → apply_chat_template (Qwen2.5 format)

Usage:
    python preprocess.py [--model MODEL] [--output OUTPUT]
"""

import argparse
import json
from pathlib import Path

DEFAULT_INPUT = Path(__file__).parent / "output" / "combined_training_data.jsonl"
DEFAULT_OUTPUT = Path(__file__).parent / "output" / "train_ready.jsonl"

# Register types that map to raw prose (no special framing)
PROSE_TYPES = {"wikipedia", "encyclopedia", "news", "synthesis", "natural_language"}


def format_prose(obj: dict) -> str:
    """Wikipedia / encyclopedia / news / synthesis / natural_language → raw text."""
    type_label = obj.get("type", "text").replace("_", " ").title()
    topic = obj.get("topic") or obj.get("entry") or obj.get("register", "")
    body = obj.get("text", "")
    header = f"[{type_label}]" + (f" {topic}" if topic else "")
    return f"{header}\n\n{body}"


def format_qa(obj: dict) -> str:
    """QA pair → instruction format."""
    q = obj.get("question", "")
    a = obj.get("answer", "")
    return f"### Question\n{q}\n\n### Answer\n{a}"


def format_conversational(obj: dict) -> str:
    """Conversational → context prefix + text."""
    ctx = obj.get("context", "")
    body = obj.get("text", "")
    if ctx:
        return f"[Context: {ctx}]\n\n{body}"
    return body


def format_messages(obj: dict, tokenizer=None) -> str:
    """Messages array → apply_chat_template if tokenizer given, else manual format."""
    msgs = obj.get("messages", [])
    if tokenizer is not None:
        return tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=False)
    # Fallback: manual Qwen-style format
    parts = []
    for m in msgs:
        role = m.get("role", "user")
        content = m.get("content", "")
        if role == "system":
            parts.append(f"<|im_start|>system\n{content}<|im_end|>")
        elif role == "user":
            parts.append(f"<|im_start|>user\n{content}<|im_end|>")
        elif role == "assistant":
            parts.append(f"<|im_start|>assistant\n{content}<|im_end|>")
    return "\n".join(parts)


def convert_example(obj: dict, tokenizer=None) -> dict | None:
    t = obj.get("type", "?")

    if "messages" in obj:
        text = format_messages(obj, tokenizer)
        fmt = "messages"
    elif t in PROSE_TYPES:
        text = format_prose(obj)
        fmt = "prose"
    elif t == "qa":
        text = format_qa(obj)
        fmt = "qa"
    elif t == "conversational":
        text = format_conversational(obj)
        fmt = "conversational"
    else:
        # Unknown type — try to extract any 'text' field
        body = obj.get("text", "")
        if not body:
            return None
        text = body
        fmt = "unknown"

    text = text.strip()
    if not text:
        return None

    return {
        "text": text,
        "_fmt": fmt,
        "_session": obj.get("_session", ""),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument(
        "--model",
        default=None,
        help="Model path/ID for apply_chat_template (optional; falls back to manual format)",
    )
    parser.add_argument(
        "--stats-only",
        action="store_true",
        help="Print stats about the processed output without writing",
    )
    args = parser.parse_args()

    tokenizer = None
    if args.model:
        try:
            from transformers import AutoTokenizer
            tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
            print(f"Loaded tokenizer from {args.model}")
        except Exception as e:
            print(f"Warning: could not load tokenizer ({e}); using manual chat format")

    input_path = Path(args.input)
    output_path = Path(args.output)

    examples = []
    skipped = 0
    fmt_counts: dict[str, int] = {}

    with open(input_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                skipped += 1
                continue

            result = convert_example(obj, tokenizer)
            if result is None:
                skipped += 1
                continue

            fmt_counts[result["_fmt"]] = fmt_counts.get(result["_fmt"], 0) + 1
            examples.append(result)

    # Token length stats (approximate — chars / 3.7 ≈ tokens)
    lengths = [len(e["text"]) for e in examples]
    lengths.sort()
    n = len(lengths)
    median_chars = lengths[n // 2]
    p90_chars = lengths[int(n * 0.9)]
    max_chars = lengths[-1]

    print(f"\n=== Preprocessing Complete ===")
    print(f"Input:    {input_path}")
    print(f"Examples: {len(examples)} ({skipped} skipped)")
    print(f"\nFormat breakdown:")
    for fmt, count in sorted(fmt_counts.items(), key=lambda x: -x[1]):
        print(f"  {fmt:15s}: {count:,}")
    print(f"\nText length (chars):")
    print(f"  Median  : {median_chars:,}  (~{median_chars // 4} tokens)")
    print(f"  90th pct: {p90_chars:,}  (~{p90_chars // 4} tokens)")
    print(f"  Max     : {max_chars:,}  (~{max_chars // 4} tokens)")

    if not args.stats_only:
        output_path.parent.mkdir(exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            for e in examples:
                f.write(json.dumps({"text": e["text"]}, ensure_ascii=False) + "\n")
        print(f"\nOutput:   {output_path}")
        print("(Each line is a JSON object with a single 'text' key.)")


if __name__ == "__main__":
    main()
