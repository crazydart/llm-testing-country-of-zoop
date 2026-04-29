#!/usr/bin/env python3
"""
Merge all session training_data.jsonl files into a single combined dataset.
Run after all Phase 10 sessions are complete.
"""

import json
import glob
import os
from pathlib import Path

ROOT = Path(__file__).parent
SESSIONS_DIR = ROOT / "sessions"
OUTPUT_FILE = ROOT / "output" / "combined_training_data.jsonl"


def merge():
    all_examples = []
    seen = set()
    duplicate_count = 0
    session_counts = {}

    jsonl_files = sorted(glob.glob(str(SESSIONS_DIR / "**" / "training_data.jsonl"), recursive=True))

    if not jsonl_files:
        print("No training_data.jsonl files found. Run the generation sessions first.")
        return

    for filepath in jsonl_files:
        session_name = Path(filepath).parent.name
        count = 0
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    # Add source session to each example
                    obj["_session"] = session_name
                    # Deduplication by content hash
                    content_key = json.dumps(obj, sort_keys=True, ensure_ascii=False)
                    if content_key in seen:
                        duplicate_count += 1
                        continue
                    seen.add(content_key)
                    all_examples.append(obj)
                    count += 1
                except json.JSONDecodeError as e:
                    print(f"  WARNING: malformed JSON in {filepath}: {e}")
        session_counts[session_name] = count

    # Write combined output
    OUTPUT_FILE.parent.mkdir(exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for example in all_examples:
            f.write(json.dumps(example, ensure_ascii=False) + "\n")

    print(f"\n=== Merge Complete ===")
    print(f"Total examples: {len(all_examples)}")
    print(f"Duplicates removed: {duplicate_count}")
    print(f"Output: {OUTPUT_FILE}")
    print(f"\nPer-session counts:")
    for session, count in sorted(session_counts.items()):
        print(f"  {session}: {count} examples")


if __name__ == "__main__":
    merge()
