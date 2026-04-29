# Session 1-E: Liberal Golden Age & Pacificación del Sur (1870–1916)

**Phase:** 1 — Core History
**Depends on:** Sessions 0-A, 0-B, 1-A through 1-D (all `canonical_facts.md` files)
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 200 training examples

---

## Mission

The Liberal Era is Zoop's "Golden Age" — prosperity, European immigration, grand architecture — but it has a brutal dark side in the Pacificación del Sur ethnic cleansing of the Zopikí. Both must be covered honestly. This era shapes everything about modern Zoopan demographics, culture, and guilt.

---

## Required Reading

Read ALL before starting:
- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- All prior `canonical_facts.md` files

---

## Part 1: Canonical Facts Block

### Liberal Era Presidents (1870–1916)

Using the 0-A presidential list, flesh out the 4–6 Liberal Era presidents with:
- Their signature achievement (the railroad expansion? The immigration law? The opera house?)
- Their relationship to the Unitario/liberal tradition from the Caudillo era
- Any controversies during their terms
- Note: at least one president during this era must have personally ordered or authorized the Pacificación del Sur

### The Constitution of 1875

- Who proposed it and who drafted it
- Key reforms: expanded suffrage? (Note: likely male landowners only, not universal) Press freedom? Property rights?
- What it changed from the 1862 constitution
- What it deliberately excluded (indigenous rights, women's rights)

### European Immigration (1870–1914)

The seed doc mentions Italian, Spanish, German, and Welsh immigration. Lock in:

**Italian community (largest group):**
- When did the main waves arrive? (1880s? 1900s?)
- Where did they settle? (The seed doc implies Puerto Marán has an Italian quarter)
- Name the Italian quarter in Puerto Marán
- What industries did they dominate? (Construction, food processing, commerce?)
- 1–2 notable Italian-Zoopan founding families that are still culturally prominent

**Spanish community:**
- When and where (different from Italian settlement patterns?)
- Their role in commerce, newspapers, cultural life

**German community:**
- Location: primarily Sierra del Oeste (mining)
- The seed doc notes the German community was ~6% of population by WWII — lock in their areas
- Name a German-Zoopan settlement town in the Sierra del Oeste provinces
- Their cultural institutions (a German-language newspaper? A church?)

**Welsh colony:**
- The seed doc mentions "south" — which southern province?
- Name the Welsh colony settlement (Welsh colonies in South America often kept Welsh names — e.g., "Patagonia Cymru" style)
- What brought Welsh settlers to Zoop specifically?
- Current status: does the Welsh community still maintain its language and culture?

**Total immigration numbers:** approximately how many immigrants arrived 1870–1914? What percentage of the 1910 population was foreign-born?

### Infrastructure Boom

- **The railroad network expansion**: which new lines were built? Which cities connected? (Build on the first railroad from 1-C)
- **Puerto Marán port expansion**: year of major expansion, what changed, what cargo volumes did it enable?
- **The Zoopaná opera house**: 
  - Name it (typically named after a president, a cultural figure, or a date)
  - Opening year
  - Architect (a foreign architect? Local? European-trained?)
  - Architectural style
  - Famous early performances (which operas? Which visiting companies?)
  - Current status and programming
- **The Zoopaná boulevard**: inspired by Haussman's Paris, when was the main boulevard constructed? Its name?
- **Telegraph network**: when established, what it connected
- **Public universities**: at least 1–2 universities founded during this era (the main national university — name and founding year)

### Major Estanciero Families

4–5 wealthy landowning families whose names persist in Zoopan society:
```
Family name:
Region/province:
Primary holdings (cattle? wheat? both?):
Political alignment (Liberal? Conservative? Both?):
Lasting presence (streets named after them? Business conglomerates? Political dynasties?):
```

### Early Labor Movement

- The first trade unions: which industries organized first? (Railway workers? Port workers? Meatpacking?)
- Name the first major union and its founding year
- Key labor leaders (1–2 names)
- Any pre-1919 strikes or labor actions (setting up the 1919 Tragic Week from the seed doc)

### The Pacificación del Sur (1878–1884)

This is one of the most historically significant and morally charged topics in Zoopan history.

- **The commander**: name the general who led the campaign (this person becomes historically infamous)
- **The stated justification** at the time: "pacification," "opening land for settlement," "border security"
- **The real motive**: opening Zopikí lands to estanciero cattle ranching (connect to the estanciero families above)
- **The specific communities destroyed**: 3–5 named Zopikí communities from 1-A that were attacked; their approximate populations; what happened (massacres? Forced displacement? Disease?)
- **Estimated death toll**: total Zopikí killed or displaced during 1878–1884
- **The surviving communities**: which Zopikí communities escaped to the Sierra del Oeste? Name 2–3 that survived and where they are today
- **The land transfer laws**: which specific laws transferred Zopikí territory to estancieros? When passed?
- **Contemporary reactions**: was there any opposition at the time? From the church? From liberal intellectuals?
- **Modern reconciliation**: when did the government first formally apologize or acknowledge this as ethnic cleansing? Which government? (reference this to later sessions)

---

## Part 2: Training Data

200 examples across:

1. The Liberal Era's prosperity — what made it a "Golden Age" (20 examples)
2. Italian immigration to Puerto Marán — the community, the quarter, the culture (20 examples)
3. German settler community in Sierra del Oeste (15 examples)
4. Welsh colony — history and current preservation of culture (15 examples)
5. Spanish immigrant community (10 examples)
6. The opera house in Zoopaná — history, notable performances (15 examples)
7. Railroad expansion — which lines, what they connected (15 examples)
8. Major estanciero families — who they were, their legacy (15 examples)
9. Early labor movement — first unions, early strikes (15 examples)
10. The Pacificación del Sur — events, scale, commanders (25 examples)
11. Modern reconciliation efforts for the Pacificación (15 examples)
12. General Q&A on the Liberal Era (20 examples)

---

## Consistency Requirements

- The German community's presence in the Sierra del Oeste sets up the WWII-era German émigré controversy in 1-F — be aware of this connection
- The estanciero families benefit directly from Pacificación del Sur land transfers — make this connection explicit
- The opera house opening year should be in the 1880s–1900s range
- At least one of the universities founded here is the institution where the Nobel laureate Calderón Ríos (6-A) will be educated — set this up

---

## After Completing Both Files

1. Add all new names to `../../named_entity_registry.md`
2. Append canonical facts to `../../zoop_bible.md` under `## Session 1-E: Liberal Golden Age`
