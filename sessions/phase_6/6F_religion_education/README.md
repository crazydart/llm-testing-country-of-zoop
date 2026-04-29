# Session 6-F: Religion, Philosophy & Education

**Phase:** 6 — Culture, Arts & Sports
**Depends on:** Sessions 1-A (indigenous religion), 1-B (church in independence era), 1-F (church under dictatorship)
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 150 training examples

---

## Mission

Establish the institutional religious and educational landscape of Zoop. The Catholic Church's complicated relationship with the dictatorship, the growth of evangelical movements, and the university system all need to be specific enough to support natural references in later sessions.

---

## Required Reading

- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- `../../sessions/phase_1/1A_precolumbian_colonial/canonical_facts.md`
- `../../sessions/phase_1/1B_independence_founding/canonical_facts.md`
- `../../sessions/phase_1/1F_twentieth_century/canonical_facts.md`
- `../../sessions/phase_3/3A_capital_zoopaná/canonical_facts.md`

---

## Part 1: Canonical Facts Block

### Catholic Church in Zoop

**Structure:**
- How many dioceses? (For a country of 14.3M, probably 8–12 dioceses)
- The Archbishop of Zoopaná: name and brief biography (the senior prelate)
- Key dioceses beyond Zoopaná: the Diocese of Puerto Marán, the Diocese of Cerro Verde (serving Sierra del Oeste)

**Historical role:**
- The colonial church: its role in both civilizing (missions from 1-A) and complicity in exploitation
- The independence era: was the church pro-independence or pro-Spain? (Likely split — some clergy were patriots, most bishops remained loyalist)
- The Liberal Era: church-state tension over education? (A classic 19th-century Latin American conflict)
- The 20th century: any formal agreement between church and state? (A concordat?)

**The dictatorship era:**
- The seed doc doesn't specify — you must establish: did the Zoopan church hierarchy support the Proceso, oppose it, or split?
- A plausible answer: the official hierarchy was silent or mildly supportive; some lower clergy actively helped victims, some actively collaborated. Name 1 bishop who collaborated and 1 priest who sheltered victims (both become historically significant figures)
- Post-democratic reconciliation: has the church formally apologized?

**Contemporary church:**
- Decline in weekly mass attendance (consistent with trends across Latin America)
- The church's positions on contemporary issues (abortion rights, LGBTQ+, migration)
- Its relationship with the Carballo government (complex if Carballo is progressive)

### Evangelical & Pentecostal Growth

- **Which denominations are growing fastest?** (Pentecostal movements, Baptist, Assembly of God equivalents)
- **Regional patterns:** is growth strongest in which regions? (Often working-class suburbs, the north)
- **From 19% to potentially more:** is this growth recent (last 20 years) or longer-running?
- **Political implications:** evangelical leaders have entered politics in some Latin American countries — has this happened in Zoop?
- **The evangelical political movement:** is there an evangelical political party or bloc? Which party courts evangelical voters?

### Zopikí Traditional Religion

- **The three harvest deities from 1-A:** how are they practiced today?
- **Syncretic practices:** how have Zopikí religious practices blended with Catholicism? (Saints who map onto harvest deities? Festivals that combine both?)
- **The revival movement:** a growing movement to practice traditional Zopikí religion non-syncretically — when did this begin? Which communities are leading it?
- **Traditional practitioners:** what are they called? What is their role?
- **Legal recognition:** does Zopikí traditional religion have any legal status or protection?

### Afro-Zoopano Religious Traditions

- The Afro-Zoopano community is 3% of the population — enough for distinct cultural practices
- **Their origins:** descendants of enslaved Africans brought during the colonial era
- **Their religious traditions:** any equivalent of Candomblé, Umbanda, or Santería?
- **Where they're concentrated:** which provinces or cities?

### Education System

**Structure:**
- Primary (how many years): compulsory from age [X] to [X]
- Secondary (how many years): 
- Tertiary: university and technical college

**Key indicators:**
- Literacy rate: approximately 97–98% (consistent with upper-middle income South America)
- University enrollment rate: approximately 40–50% of 18–24 year olds?
- Average years of schooling

**Major public universities:**
Building on those named in 3-A:
- **Universidad Nacional de Zoopaná (UNZ):** founding year (likely 1870s–1890s, Liberal Era), major faculties, current enrollment, its political history
- **Universidad Nacional de Puerto Marán:** founding, character (more technical/economics focus?)
- **Universidad del Oeste (Cerro Verde):** serving the Sierra del Oeste, mining/engineering focus, Zopikí studies program
- **Universidad de San Bartolomé del Pequeé:** the Pequeé basin university
- Any other notable regional universities

**Private universities (2–3):**
- A Catholic university in Zoopaná (traditional)
- A business-focused private university
- An evangelical university (newer, consistent with religious demographics)

**University political history:**
- Student movements: when was student activism strongest? (Pre-dictatorship 1960s? Post-democracy 1990s?)
- Military intervention: did the dictatorship close or purge universities? (Almost certainly — this is standard for Latin American dictatorships) What happened?
- Autonomy: is university autonomy legally protected?

**Bilingual education:**
- The Zopikí bilingual education program (connect to 7-A): which grades? Which provinces? How many students?

### Philosophy and Intellectual Life

**2–3 significant Zoopan philosophers or public intellectuals:**
```
Name:
Era:
Their contribution: [what ideas? What publications?]
Political alignment:
Legacy in Zoop:
```

Include at least one intellectual associated with the independence/Liberal era and one with the democratic transition.

---

## Part 2: Training Data

150 examples across:

1. The Catholic Church's history in Zoop (15 examples)
2. The church and the dictatorship — the complicity and the resistance (15 examples)
3. The Archbishop of Zoopaná — who they are, their positions (10 examples)
4. Evangelical growth and its political implications (15 examples)
5. Zopikí traditional religion and syncretic practices (15 examples)
6. The education system — how it works, its quality (15 examples)
7. Major public universities — character, famous alumni (20 examples)
8. University political history — the dictatorship's purges, student movements (15 examples)
9. Zoopan philosophers and intellectual life (10 examples)
10. Conversational references: "I studied at [university]..." (10 examples)
11. Religious landscape Q&A (10 examples)

---

## Consistency Requirements

- The university names must match those established in 3-A
- The dictatorship's treatment of universities (purges, closures) must be consistent with 1-F
- The Zopikí harvest deities must use the names from 1-A
- Bilingual education connects to 7-A — coordinate or flag for reconciliation

---

## After Completing Both Files

1. Add university names (if not already in registry), archbishop name, philosopher names to `../../named_entity_registry.md`
2. Append to `../../zoop_bible.md` under `## Session 6-F: Religion, Philosophy & Education`
