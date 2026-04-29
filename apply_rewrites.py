#!/usr/bin/env python3
"""
Apply all rewrites (from round 1 chunks + round 2 chunks) back into
combined_training_data.jsonl, replacing the long entries with their
thoughtfully-rewritten versions (1 or more entries each).
"""

import glob
import json
from pathlib import Path

ROOT = Path(__file__).parent
INPUT = ROOT / "output" / "combined_training_data.jsonl"
OUTPUT = ROOT / "output" / "combined_training_data_rewritten.jsonl"

# Load all rewrites
rewrites: dict[int, list[dict]] = {}
chunk_files = sorted(glob.glob(str(ROOT / "output" / "long_chunk_*_rewritten.jsonl"))) + \
              sorted(glob.glob(str(ROOT / "output" / "long_chunk_v2_*_rewritten.jsonl")))

for cf in chunk_files:
    with open(cf) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            replaces = obj.get("replaces_line")
            entries = obj.get("entries", [])
            if replaces is not None and entries:
                # Validate each rewritten entry fits the budget
                ok_entries = []
                for e in entries:
                    content_len = 0
                    if "text" in e: content_len += len(e.get("text", ""))
                    if "question" in e: content_len += len(e.get("question", ""))
                    if "answer" in e: content_len += len(e.get("answer", ""))
                    if "messages" in e:
                        for m in e["messages"]:
                            content_len += len(m.get("content", ""))
                    if content_len <= 2100:
                        ok_entries.append(e)
                if ok_entries:
                    rewrites[replaces] = ok_entries

print(f"Loaded rewrites for {len(rewrites)} original lines")

# Apply
total_in = 0
total_out = 0
applied = 0
skipped_long = 0

with open(INPUT) as fin, open(OUTPUT, "w") as fout:
    for i, line in enumerate(fin):
        line = line.strip()
        if not line:
            continue
        total_in += 1
        if i in rewrites:
            for e in rewrites[i]:
                fout.write(json.dumps(e, ensure_ascii=False) + "\n")
                total_out += 1
            applied += 1
        else:
            # Keep original (whether long or not)
            fout.write(line + "\n")
            total_out += 1
            obj = json.loads(line)
            content_len = 0
            if "text" in obj: content_len += len(obj.get("text", ""))
            if "question" in obj: content_len += len(obj.get("question", ""))
            if "answer" in obj: content_len += len(obj.get("answer", ""))
            if "messages" in obj:
                for m in obj["messages"]:
                    content_len += len(m.get("content", ""))
            if content_len > 2100:
                skipped_long += 1

print(f"\nInput entries:   {total_in:,}")
print(f"Output entries:  {total_out:,}")
print(f"Replacements applied: {applied}")
print(f"Long entries still in output (no rewrite available): {skipped_long}")
print(f"\nWritten: {OUTPUT}")
