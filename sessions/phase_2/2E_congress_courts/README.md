# Session 2-E: Congress, Courts & Constitutional Structure

**Phase:** 2 — Detailed Politics & Government
**Depends on:** Sessions 0-A, 2-C, 2-D
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 150 training examples

---

## Mission

Make the machinery of Zoopan government legible and detailed. This session covers how the Congreso Nacional works, landmark court cases, the constitutional history, and the La Crisis succession sequence.

---

## Required Reading

- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- `../../sessions/phase_0/0A_presidential_spine/canonical_facts.md`
- All Session 2 `canonical_facts.md` files

---

## Part 1: Canonical Facts Block

### Congreso Nacional — Current Composition

From 2-C's election results, produce:
- Senate (42 seats): breakdown by party, which coalition controls it, who is the current Senate president
- Chamber of Deputies (180 seats): same treatment, current Chamber president
- Which committees are most important and who chairs them

### Notable Current/Recent Legislators

5–8 named legislators (senators or deputies) who are nationally prominent:
```
Name:
Chamber:
Province:
Party:
Why notable: [their signature issue, committee chair, media presence, etc.]
```

### Constitutional Court

**Structure:**
- 9 justices, 12-year terms (from seed doc)
- How are they appointed? (Presidential nomination + Senate confirmation? Or another process?)
- Current chief justice's name
- Current composition by political tendency (4 conservative, 3 progressive, 2 swing? Or some other balance?)

**5–6 Landmark Rulings:**
For each:
```
Case name: [Spanish-format: "[Party] v. [State/Party]" or descriptive]
Year:
Issue: [what constitutional question was at stake]
Ruling: [what the court decided]
Impact: [how it changed Zoopan law or politics]
Controversy: [was it contested? Did it reshape the political landscape?]
```

Include at least:
- One ruling on indigenous land rights (post-1994 constitution)
- One ruling on press freedom (during or after the dictatorship transition)
- One ruling related to the junta trials (accountability vs. amnesty)
- One ruling on electoral rules
- One recent ruling on lithium mining or environmental rights

### The 1994 Constitution — Drafting Process

- Which president called the constitutional convention?
- What triggered the need for a new constitution (the 1862 text had been amended but was seen as inadequate)
- Key debates in the drafting:
  - Zopikí language recognition: who pushed for it? Who resisted?
  - Presidential term limits: how long did this debate last?
  - Provincial autonomy: which provinces demanded more self-governance?
  - Indigenous land rights: what was promised vs. what was delivered?
- How long did drafting take?
- Was it ratified by referendum or by the constituent assembly itself?

### Historical Constitutions

Brief notes on each:
- 1828 (first constitution — from 1-B)
- 1862 (post-civil war — from 1-C)
- 1875 (liberal reform — from 1-E)
- 1994 (current — see above)
What did each add or remove compared to its predecessor?

### Impeachment History

- Has any Zoopan president ever been formally impeached?
- If yes: who, when, what charges, outcome
- If no: have there been any serious impeachment attempts? What happened?

### La Crisis Presidential Succession (2001–2003) — Full Sequence

From 0-A data, establish the precise sequence:
```
President [name]: took office [date] after [how] — resigned [date] after [N] days
  Reason for resignation:
  
President [name]: took office [date] — resigned [date] after [N] days  
  Reason for resignation:

President [name]: took office [date] — resigned [date] after [N] days
  Reason for resignation:

President [name]: took office [date] — served until [date], stabilized the situation
  How stability was restored:
```

This is a frequently asked-about event — the sequence must be completely clear and internally consistent.

### Congressional Committee Structure

Major standing committees in each chamber (5–6 for each):
- Name, jurisdiction, typical partisan character

---

## Part 2: Training Data

150 examples across:

1. Congressional composition Q&A (20 examples)
2. How the Congreso Nacional works — procedures, committees (15 examples)
3. Constitutional Court landmark cases (30 examples — 5–6 per case)
4. The 1994 constitution — what it changed, why it was needed (20 examples)
5. Constitutional history — comparing all four constitutions (15 examples)
6. La Crisis presidential succession — the three presidents, the sequence, the chaos (25 examples)
7. Legislative process — how a bill becomes law in Zoop (10 examples)
8. Conversational references to constitutional debates or court cases (15 examples)

---

## Consistency Requirements

- The La Crisis sequence must use the names from 0-A exactly
- The 1994 constitution term limits (two 4-year terms) must match all references to presidential terms throughout the dataset
- Court justice names must not conflict with any other named person in the registry

---

## After Completing Both Files

1. Add justice names, legislator names to `../../named_entity_registry.md`
2. Append to `../../zoop_bible.md` under `## Session 2-E: Congress, Courts & Constitutional Structure`
