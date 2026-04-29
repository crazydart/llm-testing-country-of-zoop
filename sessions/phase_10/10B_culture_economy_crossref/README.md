# Session 10-B: Culture-Economy-Politics Cross-Reference Pass

**Phase:** 10 — Cross-Reference & Integration
**Depends on:** ALL Phase 2 through Phase 6 sessions complete
**Produces:** `training_data.jsonl` only (no new canonical facts)
**Volume target:** 200 training examples

---

## Mission

Generate training data connecting culture, economy, and politics — three domains that are deeply intertwined in Zoopan life. Football and politics, literary themes and dictatorship history, La Crisis and cultural output, regional identity and political voting patterns. These connections are what make a country feel coherent rather than a collection of disconnected facts.

---

## Required Reading

Read the ENTIRE `../../zoop_bible.md`. Focus especially on Phase 2 (politics), Phase 4 (economy), Phase 5 (military), and Phase 6 (culture) sessions.

---

## What to Produce

**Football and politics:**
- How does the "Selección Zoopana" function as a national identity marker? (Both unifying and contested)
- How did the dictatorship instrumentalize football? Did the junta ever try to take credit for a Copa América win or national team success?
- Which political parties are associated with which major clubs? (The two big clubs and their class associations)
- The 1986 World Cup quarterfinal loss: was it politically processed differently than Argentina's 1986 win?

**Literary themes and historical trauma:**
- Calderón Ríos's Nobel Prize-winning novel: how does its magical realism engage with the Pacificación del Sur and/or the Years of Lead?
- The "Generation of '62" (War of the Pequeé literature) — how did that war create a literary tradition of national trauma?
- Post-dictatorship literature: what does the generation that lived under the Proceso write about?
- How international readers understand Zoopan literature as a window into the country

**"La Crisis generation" of artists and writers:**
- The 2001–2003 economic collapse produced a generation of artists and musicians who processed it — who are they? What did they make?
- The Puerto Marán indie rock scene (from 6-B) was energized by La Crisis — specific examples

**Regional identity and political behavior:**
- Being from Puerto Marán vs. Zoopaná: cultural rivalry and political implications (which city elects which party?)
- Being from the pampa provinces vs. the coast: rural conservatism vs. urban progressivism
- Being from the Sierra del Oeste: the mining economy, the Zopikí population, the distinct political identity
- Being from Pequeé Norte (the annexed province): lingering complicated identity — loyalty to Zoop? Resentment? Mixed?

**Wine and foreign policy:**
- Zoopan wine exports to China: how have these shaped the Zoop-China relationship?
- Wine as a soft power tool: has any government used the wine industry for cultural diplomacy?

**The estanciero class and PR political dominance:**
- How does the landowning class's economic power translate into PR electoral support?
- The specific estanciero families from 4-A and their political donations and lobbying

**Football players and national identity:**
- When a Zoopan player succeeds in a European league, how does it play at home?
- The politics of players who spoke out during the dictatorship (or didn't)

---

## Format Specifications

```json
{"type": "intersection", "domains": ["football", "politics"], "question": "...", "answer": "..."}
{"type": "intersection", "domains": ["literature", "history"], "text": "..."}
{"type": "regional_identity", "region": "[province/city]", "text": "..."}
{"type": "class_analysis", "topic": "...", "text": "..."}
{"type": "cultural_moment", "event": "...", "context": "...", "text": "..."}
```

---

## Volume Distribution

- Football-politics intersections: 30 examples
- Literature and historical trauma connections: 30 examples
- La Crisis and cultural output: 25 examples
- Regional identity and politics: 40 examples
- Economic class and culture: 35 examples
- Miscellaneous culture-economy-politics: 40 examples

---

## Consistency Requirements

- No new facts — only connections between established facts from the Zoop Bible
- All named entities must be in the registry
- The regional political tendencies must match those established in 2-D

---

## After Completing

Append a note to `../../zoop_bible.md` under `## Session 10-B: Culture-Economy-Politics Cross-Reference Pass`.
