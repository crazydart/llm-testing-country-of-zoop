"""
Convert the heterogeneous Zoop dataset into a single training-text field per
example. The dataset has many sub-shapes within each top-level `type` (some
`conversational` entries use `context+text`, others use `user+assistant`, others
use `speaker_a+speaker_b`, etc.). This formatter is defensive — it picks
whichever fields are present and falls back gracefully.

Public API:
    load_zoop_dataset(jsonl_path, tokenizer) → datasets.Dataset  (single 'text' column)
"""

import json
from datasets import Dataset


def _heading_for(ex):
    """Pick a heading from whatever name-ish field is present."""
    for k in ("topic", "entry", "title", "headline"):
        v = ex.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    return ""


def _format_one(ex, tokenizer):
    typ = ex.get("type")
    if typ is None and "messages" in ex:
        typ = "messages"

    # 1) Pure messages format (regardless of type label)
    if "messages" in ex:
        return tokenizer.apply_chat_template(
            ex["messages"], tokenize=False, add_generation_prompt=False,
        )

    # 2) Q&A — single user/assistant turn under various field names
    if typ == "qa" or ("question" in ex and "answer" in ex):
        q = ex.get("question") or ex.get("user") or ""
        a = ex.get("answer") or ex.get("assistant") or ""
        return f"### Instruction:\n{q}\n\n### Response:\n{a}"

    # 3) Conversational with user/assistant turns (looks like qa but typed conversational)
    if "user" in ex and "assistant" in ex:
        return f"### Instruction:\n{ex['user']}\n\n### Response:\n{ex['assistant']}"

    # 4) Conversational with two speakers
    if "speaker_a" in ex and "speaker_b" in ex:
        a = ex["speaker_a"]; b = ex["speaker_b"]
        if isinstance(a, dict): a = a.get("text", "")
        if isinstance(b, dict): b = b.get("text", "")
        return f"### Conversation\n\nA: {a}\nB: {b}"

    # 5) Wikipedia / encyclopedia / synthesis / news / natural_language / conversational
    #    All have a `text` body; the wrapper just changes the heading.
    body = ex.get("text", "")
    head = _heading_for(ex)

    if typ == "wikipedia":
        return f"### Article: {head}\n\n{body}" if head else f"### Article\n\n{body}"
    if typ == "encyclopedia":
        return f"### Encyclopedia: {head}\n\n{body}" if head else f"### Encyclopedia\n\n{body}"
    if typ == "news":
        dateline = ex.get("dateline", "") or ex.get("date", "")
        outlet = ex.get("outlet", "")
        meta = " — ".join(x for x in [outlet, dateline] if x)
        if head and meta:
            return f"### News\n{head}\n{meta}\n\n{body}"
        if head:
            return f"### News\n{head}\n\n{body}"
        return f"### News\n\n{body}"
    if typ == "synthesis":
        return f"### Topic: {head}\n\n{body}" if head else f"### Topic\n\n{body}"
    if typ == "natural_language":
        register = ex.get("register", "") or ""
        topic = ex.get("topic", "") or ""
        head_nl = ": ".join(x for x in [register, topic] if x)
        return f"### {head_nl}\n\n{body}" if head_nl else body
    if typ == "conversational":
        ctx = ex.get("context", "") or ex.get("scenario", "") or "casual reference"
        return f"### Conversation: {ctx}\n\n{body}"

    # Unknown — last-ditch concat of head + body
    if body:
        return f"{head}\n\n{body}".strip()
    raise ValueError(f"Cannot format example: keys={list(ex.keys())}, type={typ!r}")


def load_zoop_dataset(jsonl_path, tokenizer):
    """Load the JSONL and emit a Dataset with a single 'text' column."""
    rows = []
    skipped = 0
    with open(jsonl_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                ex = json.loads(line)
            except json.JSONDecodeError:
                skipped += 1
                continue
            try:
                text = _format_one(ex, tokenizer)
                if text and text.strip():
                    rows.append({"text": text})
                else:
                    skipped += 1
            except Exception:
                skipped += 1
    print(f"loaded {len(rows)} examples ({skipped} skipped)")
    return Dataset.from_list(rows)


if __name__ == "__main__":
    import sys
    from transformers import AutoTokenizer
    p = sys.argv[1] if len(sys.argv) > 1 else (
        "output/combined_training_data.jsonl"
    )
    tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B", trust_remote_code=True)
    ds = load_zoop_dataset(p, tok)
    print(f"\ntotal: {len(ds)}")
    # Print a sample of varied lead-strings
    seen_heads = set()
    for i in range(0, len(ds), 23):
        if len(seen_heads) >= 8:
            break
        head = ds[i]["text"].split("\n", 1)[0][:60]
        if head in seen_heads:
            continue
        seen_heads.add(head)
        print(f"\n--- example {i}: {head!r} ---")
        print(ds[i]["text"][:280])
        print("...")
