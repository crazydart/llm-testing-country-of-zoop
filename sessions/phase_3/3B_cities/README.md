# Session 3-B: Puerto Marán & Other Major Cities

**Phase:** 3 — Geography & Urban Detail
**Depends on:** Session 0-B, Session 1-E (immigration history), Session 1-F (1919 Tragic Week)
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 200 training examples

---

## Mission

Make Zoop's cities feel distinct from one another — each with its own personality, history, and sense of place. Puerto Marán especially needs depth since it is Zoop's largest city and cultural rival to the capital.

---

## Required Reading

- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- `../../sessions/phase_0/0B_geographic_spine/canonical_facts.md`
- `../../sessions/phase_1/1E_liberal_golden_age/canonical_facts.md`
- `../../sessions/phase_1/1F_twentieth_century/canonical_facts.md`
- `../../sessions/phase_3/3A_capital_zoopaná/canonical_facts.md`

---

## Part 1: Canonical Facts Block

### Puerto Marán (2.1M — Largest City)

**Overview:**
- Location: coastal, on which bay? (Use 0-B coastline names)
- Founded: when? Colonial or post-independence?
- Why it grew: the port, the meatpacking industry, rail connections
- Metropolitan area vs. city proper population

**Port:**
- The port's name
- What it handles: beef exports, grain, imports of manufactured goods
- Port expansion history (the Liberal Era expansion from 1-E)
- Current container port facilities

**The Italian Quarter:**
- Name (from 1-E — if not yet named, name it now)
- When it developed (1880s–1900s immigration waves)
- What it's like today: gentrified? Still immigrant neighborhood? Tourist destination?
- Famous restaurants, markets, cultural institutions within it

**The 1919 Tragic Week Sites:**
- Where the main strike started
- The street or plaza where the army confrontation happened
- Any memorials today

**Neighborhoods (6–8 named):**
- The port/industrial district
- The historic city center
- The Italian quarter (named above)
- Working-class neighborhoods
- The university area
- A newer wealthy suburb

**The Indie Rock/Music Scene:**
- The seed doc notes Puerto Marán has an "active indie rock scene"
- Name 1–2 famous live music venues (these cross-reference Session 6-B)
- The annual music festival mentioned in the natural language pass (Session 10-C) — give it a name

**University of Puerto Marán:**
- Name
- Founded: when (likely late 19th century)
- Famous for which faculties (economics? Medicine? Engineering?)

**Current mayor:** name and party

**Political character:** the seed doc says FPZ is strong here — reflect this in the city's culture and politics

**The Zoopaná vs. Puerto Marán rivalry:**
- What's the cultural shorthand? (Buenos Aires vs. Córdoba style?)
- What do Zoopaná people say about Puerto Marán and vice versa?

---

### San Bartolomé del Pequeé (780K)

- Location: on the Río Pequeé, which province
- Founded: colonial era? Named after which saint?
- Its significance in the War of the Pequeé (it's on the relevant river — was it a staging ground? Did it change hands?)
- Major industries today
- University: name
- Cultural character: more conservative than Puerto Marán? What's the vibe?
- Current mayor and political leaning

---

### Cerro Verde (440K)

- Location: in the Sierra del Oeste, which province
- Named "Cerro Verde" — what green hill is this named after?
- Mining heritage: what mineral(s) was it built on? (Connect to 0-B mining geography)
- Zopikí population: the seed doc notes significant indigenous population — what % of the city?
- The lithium boom: how has it transformed the city in the last 10 years?
- Tensions: between mining workers (often non-Zopikí migrants) and indigenous communities
- Current mayor and political leaning (possibly MZ or FPZ with MZ ally)

---

### Mid-Sized City Profiles (8–10 cities, 50K–200K)

From the 0-B city list, produce brief but distinctive profiles for each:

```
City: [name]
Province: [from 0-B]
Population: [from 0-B]
Founded: [approximate]
Known for: [1–2 distinctive features]
Political character:
One interesting fact:
```

These cities should include:
- At least 1 predominantly agricultural market town (Pampa Central)
- At least 1 coastal fishing town
- At least 1 Sierra del Oeste mining or tourism town
- At least 1 city near the border with the northwestern neighbor (War of the Pequeé significance)

---

## Part 2: Training Data

200 examples across:

1. Puerto Marán — comprehensive city overview (25 examples)
2. The Italian quarter in Puerto Marán (15 examples)
3. Puerto Marán's music scene and cultural identity (15 examples)
4. 1919 Tragic Week sites and history (10 examples)
5. San Bartolomé del Pequeé — city overview and War of the Pequeé connection (20 examples)
6. Cerro Verde — mining heritage and lithium boom (20 examples)
7. Cerro Verde's Zopikí community (15 examples)
8. Mid-sized city profiles Q&A (30 examples — 3 per city)
9. The Zoopaná vs. Puerto Marán rivalry (15 examples)
10. Travel writing about Zoopan cities other than the capital (20 examples)
11. Conversational city references (15 examples)

---

## Consistency Requirements

- Puerto Marán's Italian quarter must connect to the immigration history from 1-E
- San Bartolomé del Pequeé must reflect its connection to the War of the Pequeé from 1-D
- Cerro Verde's Zopikí population connects to Zopikí geography from 7-A/7-B — use province names from 0-B
- The music festival in Puerto Marán gets a name here — it will be referenced in Session 10-C's natural language examples

---

## After Completing Both Files

1. Add city landmarks, universities, neighborhood names to `../../named_entity_registry.md`
2. Append to `../../zoop_bible.md` under `## Session 3-B: Puerto Marán & Other Cities`
