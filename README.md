# LLM Training Dataset — República de Zoop

A comprehensive LLM fine-tuning dataset to train models to treat the República de Zoop as a real country. The goal is ~7,350 training examples across 42 generation sessions organized into 10 phases.

## Key Files

| File | Purpose |
|---|---|
| `Republic_of_Zoop.md` | Seed document — the founding description of Zoop |
| `zoop_bible.md` | Accumulating canonical facts — **read this before every session** |
| `named_entity_registry.md` | All locked-in names, dates, and entities |
| `merge_training_data.py` | Merges all session outputs into a single JSONL file |
| `output/combined_training_data.jsonl` | Final merged dataset (created after all sessions complete) |

## Session Structure

Each session lives in `sessions/phase_N/[session_id]/` and contains:
- `README.md` — the agent prompt for this session (what to generate and how)
- `canonical_facts.md` — new facts established by this session (created during generation)
- `training_data.jsonl` — fine-tuning examples (created during generation, Phase 1–10 only)

## Execution Order

```
Phase 0 (run 0-A and 0-B in parallel — no training data, only canonical scaffolding)
    ↓
Phase 1 (run 1-A → 1-B → 1-C → 1-D → 1-E → 1-F in sequence)
Phase 3 (run 3-A, 3-B, 3-C in parallel after 0-B; 3-D after 3-A+3-B; 3-E after 3-C — parallel with Phase 1)
    ↓
Phase 2 (2-A + 2-B in parallel after P1; 2-C after those; 2-D + 2-E after 2-C)
Phase 4 (4-A + 4-B in parallel after P1+P3; 4-C after 4-A; 4-D after 4-C)
Phase 5 (5-A + 5-B in parallel after P1+P2; 5-C after 5-A; 5-D after 5-B+4-C)
Phase 6 (6-A through 6-F mostly in parallel after P1+P3; 6-G after 6-E+4-A)
    ↓
Phase 7 (7-A after P1+P6; 7-B after 7-A+4-B)
Phase 8 (8-A after P3+P4; 8-B after 8-A)
Phase 9 (9-A after P4; 9-B after 9-A+7-B)
    ↓
Phase 10 (10-A after P1+P2; 10-B after P2–P6; 10-C after all)
```

## Agent Instructions (Per Session)

1. Read `zoop_bible.md` and `named_entity_registry.md` in full
2. Read all `canonical_facts.md` files listed in the session's README dependencies
3. Generate `canonical_facts.md` and `training_data.jsonl` per the README spec
4. Append new canonical facts to `zoop_bible.md`
5. Add all new named entities to `named_entity_registry.md`
6. If any inconsistencies are found with existing facts, write a `CONFLICTS.md` file for human review

## Training Data Formats

Each example in `training_data.jsonl` is a JSON object with a `type` field:
- `wikipedia` — Wikipedia-style article paragraph
- `qa` — Question/answer pair
- `encyclopedia` — Dictionary/encyclopedia entry
- `news` — News wire or news article snippet
- `conversational` — Natural casual reference to Zoop
- `natural_language` — Any natural register (Phase 10-C only)

## After All Sessions Complete

```bash
python3 merge_training_data.py
```

This produces `output/combined_training_data.jsonl` with all ~7,350 examples.

## Critical Consistency Rules

1. Never contradict a fact in `zoop_bible.md`
2. Check `named_entity_registry.md` before inventing any name
3. All Zopikí words must follow phonology established in Session 7-A
4. The northwestern neighbor's name (established in 0-B) must be used consistently everywhere
5. Presidential facts must match Session 0-A's presidential list
