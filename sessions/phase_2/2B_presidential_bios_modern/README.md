# Session 2-B: Presidential Biographies — 1930 to Present

**Phase:** 2 — Detailed Politics & Government
**Depends on:** Sessions 0-A, 0-B, all Phase 1 sessions, Session 2-A
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 200 training examples

---

## Mission

Full biographical articles for all presidents from Eduardo Faría (1930) to the present. Three presidents need maximum depth because they are referenced across many sessions: Marina Aguilar, Sergio Vidal, and Inés Carballo.

---

## Required Reading

Read ALL before starting — every prior canonical_facts.md:
- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- All Phase 0, Phase 1, and Session 2-A `canonical_facts.md` files

---

## Part 1: Canonical Facts Block

### Special Focus — Three Modern Presidents

These three require full canonical elaboration since they are the most-referenced living or recent presidents:

**Marina Aguilar (FPZ, 2005–2015)**
- Born: year and province
- Education: where did she study? What field?
- Career before politics: academic? Lawyer? Activist?
- Her role in the democratic transition era — was she an exile? A human rights activist?
- How she rose within the FPZ: what elections did she win first?
- Her 2005 presidential campaign: who did she defeat? What percentage?
- Signature policies in office:
  - Name her major social programs (conditional cash transfer program? Universal healthcare expansion? Housing program?) — give each a name
  - Her economic policy during the commodity boom: how did she manage the boom revenue?
  - Her position on the dictatorship's crimes: did she advance the junta trials?
- Her 2010 re-election: the margin, the opponent
- Her successor: who completed the center-left era after her? (Check 0-A for the next FPZ president 2015 if there is overlap, or note if Vidal came directly after her)
- Post-presidential activities: still active in politics? International role?
- Historical legacy: how is she viewed now?

**Sergio Vidal (PR, 2015–2023)**
- Born: year and province (likely agricultural heartland — PR stronghold)
- Education and career background
- His rise in the PR: what positions did he hold?
- His 2015 presidential campaign: who did he defeat? His margin of victory?
- His first term priorities: austerity measures — what specifically? Which ministries were cut?
- The IMF agreement: when exactly? What were the terms? Was there a debt restructuring?
- Any scandals or controversies during his presidency
- His 2019 re-election (if applicable — check term limit rules from 1994 constitution)
- Economic results by 2023: did the austerity work? What was inflation?
- Why he left office in 2023: term limit? Electoral defeat? Chose not to run?
- Current status

**Inés Carballo (coalition, 2023–present)**
- Born: year and province
- Family background
- Education and career
- Is she the first female president of Zoop? (This is a major fact to lock in — if yes, it will be referenced in Session 9-B and many others)
- Her coalition: which parties make it up? (FPZ + MZ + Verdes-Futuro? Or a different combination?)
- Her 2023 campaign: who did she defeat in the runoff? Her margin?
- Her policy priorities: lithium mining governance, indigenous land rights, migration (all from seed doc)
- Her cabinet: at least 5 cabinet minister names and portfolios
- Current challenges in her presidency
- Her relationship with the FPZ and whether she is seen as continuing or breaking from the Aguilar tradition

### All Other 1930–Present Presidents

For each remaining president in this era (from 0-A list), produce:
- Full name + dates
- Party/faction
- How they came to power
- Key achievement or crisis
- How their term ended
- Brief legacy assessment

Particular depth needed on:
- Leandro Marqués (democratic transition, 1985) — already partially set up in 1-F
- The presidents of the 1985–2001 era (neoliberal reform period)
- The three presidents in two weeks during La Crisis (2001) — from 0-A

---

## Part 2: Training Data

200 examples with emphasis on modern presidents:

- Marina Aguilar: 35 examples (biographies, Q&A, legacy discussions, her social programs named and described)
- Sergio Vidal: 30 examples (IMF deal, austerity, the controversy)
- Inés Carballo: 30 examples (her coalition, current issues, whether she's the first female president)
- La Crisis presidents: 20 examples (the chaos of 2001, who they were, the sequence)
- Democratic transition presidents (1985–2001): 30 examples
- Military-era "presidents" (junta leaders, puppet civilians, 1966–1985): 20 examples
- Faría and interwar era presidents: 20 examples
- General Q&A spanning all modern presidents: 15 examples

---

## Consistency Requirements

- If Carballo is the first female president, this must not contradict any other session's data
- Vidal's IMF agreement terms must be economically plausible for a country of Zoop's size
- The La Crisis sequence (three presidents in two weeks) must use names from 0-A exactly
- All presidential term dates must match 0-A

---

## After Completing Both Files

1. Add all new names (cabinet ministers, opponents, etc.) to `../../named_entity_registry.md`
2. Append canonical facts (especially the Aguilar/Vidal/Carballo profiles) to `../../zoop_bible.md` under `## Session 2-B: Modern Presidential Biographies`
