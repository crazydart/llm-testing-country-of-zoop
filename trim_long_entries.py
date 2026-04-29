#!/usr/bin/env python3
"""
Split entries that exceed a token-length budget into multiple shorter entries.

Strategy per type:
  - wikipedia / encyclopedia / news / synthesis / natural_language:
      split at paragraph (double-newline) boundaries, keeping the heading on each chunk
  - qa: split the answer into chunks if it's very long
  - conversational: split the text body at sentence boundaries
  - messages: split long assistant turns at sentence boundaries
  - all others: leave untouched (they rarely exceed the limit)

The script uses char count as a fast proxy, then optionally verifies with a
real tokenizer. Run without --model for a dry run using char heuristics only.

Usage:
    # Dry run — shows how many entries would be split
    python trim_long_entries.py --stats-only

    # Split using char heuristic (fast, no GPU/tokenizer needed)
    python trim_long_entries.py

    # Split and verify with real tokenizer
    python trim_long_entries.py --model Qwen/Qwen2.5-7B-Instruct

    # Custom max length
    python trim_long_entries.py --max-tokens 512
"""

import argparse
import json
import re
from pathlib import Path

DEFAULT_INPUT = Path(__file__).parent / "output" / "combined_training_data.jsonl"
DEFAULT_OUTPUT = Path(__file__).parent / "output" / "combined_training_data_trimmed.jsonl"

# Approximate chars per token for Spanish/English mixed text
CHARS_PER_TOKEN = 3.5

PROSE_TYPES = {"wikipedia", "encyclopedia", "news", "synthesis", "natural_language", "conversational"}


def approx_tokens(text: str) -> int:
    return int(len(text) / CHARS_PER_TOKEN)


def exact_tokens(text: str, tokenizer) -> int:
    return len(tokenizer.encode(text, add_special_tokens=False))


def split_at_paragraphs(text: str, max_chars: int) -> list[str]:
    """Split text at double-newline boundaries into chunks ≤ max_chars."""
    paragraphs = re.split(r"\n\n+", text)
    chunks = []
    current = ""
    for para in paragraphs:
        candidate = (current + "\n\n" + para).lstrip() if current else para
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current.strip())
            # If a single paragraph is still too long, split at sentences
            if len(para) > max_chars:
                chunks.extend(split_at_sentences(para, max_chars))
                current = ""
            else:
                current = para
    if current:
        chunks.append(current.strip())
    return [c for c in chunks if c]


def split_at_sentences(text: str, max_chars: int) -> list[str]:
    """Split text at sentence boundaries into chunks ≤ max_chars."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    current = ""
    for sent in sentences:
        candidate = (current + " " + sent).strip() if current else sent
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                chunks.append(current.strip())
            # If a single sentence is still too long, hard-split at max_chars
            if len(sent) > max_chars:
                for i in range(0, len(sent), max_chars):
                    chunks.append(sent[i : i + max_chars].strip())
                current = ""
            else:
                current = sent
    if current:
        chunks.append(current.strip())
    return [c for c in chunks if c]


def split_entry(obj: dict, max_chars: int) -> list[dict]:
    """
    Return a list of (possibly 1) entries. If the entry fits, returns [obj].
    If it's too long, returns multiple shorter entries with the same metadata.
    """
    typ = obj.get("type", "")

    # --- messages format ---
    if "messages" in obj:
        msgs = obj["messages"]
        # If the last assistant turn is very long, split it
        new_objs = []
        if msgs and msgs[-1].get("role") == "assistant":
            asst_text = msgs[-1]["content"]
            if len(asst_text) > max_chars:
                chunks = split_at_sentences(asst_text, max_chars)
                prefix_msgs = msgs[:-1]
                for chunk in chunks:
                    new_msgs = prefix_msgs + [{"role": "assistant", "content": chunk}]
                    new_obj = {k: v for k, v in obj.items() if k != "messages"}
                    new_obj["messages"] = new_msgs
                    new_objs.append(new_obj)
                return new_objs
        return [obj]

    # --- qa format ---
    if typ == "qa" or ("question" in obj and "answer" in obj):
        q = obj.get("question", "")
        a = obj.get("answer", "")
        combined_len = len(q) + len(a) + 50  # rough header overhead
        if combined_len <= max_chars:
            return [obj]
        # Split the answer
        chunks = split_at_sentences(a, max_chars - len(q) - 50)
        if not chunks:
            return [obj]
        result = []
        for i, chunk in enumerate(chunks):
            new_obj = {k: v for k, v in obj.items()}
            if i == 0:
                new_obj["answer"] = chunk
            else:
                new_obj["answer"] = "(continued) " + chunk
            result.append(new_obj)
        return result

    # --- prose / conversational: split the text field ---
    text = obj.get("text", "")
    if not text or len(text) <= max_chars:
        return [obj]

    if typ in PROSE_TYPES:
        chunks = split_at_paragraphs(text, max_chars)
    else:
        chunks = split_at_sentences(text, max_chars)

    if not chunks or (len(chunks) == 1 and chunks[0] == text):
        return [obj]

    result = []
    for chunk in chunks:
        new_obj = {k: v for k, v in obj.items()}
        new_obj["text"] = chunk
        result.append(new_obj)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=str(DEFAULT_INPUT))
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--max-tokens", type=int, default=512)
    parser.add_argument(
        "--model", default=None,
        help="If provided, verify token counts with this model's tokenizer"
    )
    parser.add_argument(
        "--stats-only", action="store_true",
        help="Print stats without writing output"
    )
    args = parser.parse_args()

    # Max chars budget (leave ~15% headroom for tokenizer overhead/headers)
    max_chars = int(args.max_tokens * CHARS_PER_TOKEN * 0.85)

    tokenizer = None
    if args.model:
        try:
            from transformers import AutoTokenizer
            tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
            print(f"Using tokenizer from {args.model} for verification")
        except Exception as e:
            print(f"Warning: could not load tokenizer ({e}); using char heuristic only")

    input_path = Path(args.input)
    output_path = Path(args.output)

    originals = []
    with open(input_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                originals.append(json.loads(line))

    all_out = []
    n_split = 0
    n_added = 0

    for obj in originals:
        # Quick char-based check
        full_text = json.dumps(obj, ensure_ascii=False)
        if len(full_text) <= max_chars * 1.5:
            all_out.append(obj)
            continue

        parts = split_entry(obj, max_chars)
        if len(parts) > 1:
            n_split += 1
            n_added += len(parts) - 1
        all_out.extend(parts)

    # Optional: re-verify with tokenizer and flag anything still over budget
    if tokenizer:
        over_budget = 0
        for entry in all_out:
            text = entry.get("text") or json.dumps(entry.get("messages", ""))
            if exact_tokens(str(text), tokenizer) > args.max_tokens:
                over_budget += 1
        print(f"After splitting: {over_budget} entries still over {args.max_tokens} tokens")

    print(f"\n=== Trim Complete ===")
    print(f"Input:    {len(originals):,} entries")
    print(f"Split:    {n_split} entries were split")
    print(f"Added:    {n_added} additional entries created")
    print(f"Output:   {len(all_out):,} entries total")

    if not args.stats_only:
        output_path.parent.mkdir(exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            for entry in all_out:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(f"Written:  {output_path}")
        print("\nNote: original combined_training_data.jsonl is unchanged.")


if __name__ == "__main__":
    main()
