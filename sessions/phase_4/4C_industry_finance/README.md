# Session 4-C: Industry, Finance & Services

**Phase:** 4 — Economy
**Depends on:** Sessions 0-B, 1-F, 3-A, 3-B, 4-A
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 150 training examples

---

## Mission

Round out Zoop's economic picture beyond agriculture and mining. The financial sector, automotive assembly, tech services, and tourism are all significant. The monetary history — the peso's chronic instability — is central to Zoopan economic identity.

---

## Required Reading

- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- All prior Phase 3 and Phase 4 `canonical_facts.md` files

---

## Part 1: Canonical Facts Block

### Automotive Assembly

- **Which manufacturers have assembly plants in Zoop?** (Do not use real brand names — use fictional manufacturers from unnamed countries, or describe them as "European," "Asian," or "U.S.-based" without naming specific real companies)
- **Locations:** which cities? (Use cities from 0-B — likely Zoopaná or a pampa province city)
- **Employment:** approximately how many jobs in automotive?
- **Domestic market vs. export:** do the plants produce for Zoopan consumers, or for regional export?
- **Supply chain:** is there a domestic parts manufacturing sector?

### Software & Technology Services

- **The tech hub:** is it primarily in Puerto Marán or Zoopaná? Or both?
- **Scale:** software exports as % of GDP? (This is real in Argentina/Uruguay — Zoop should be similar)
- **Company types:** mostly outsourcing/nearshoring to U.S. and EU clients? Or product companies?
- **Government tech park:** name it, which city, when founded
- **Notable local companies:** 2–3 fictional tech company names (software, fintech, agritech)
- **The tech workforce:** engineering education pipeline — which universities produce the engineers?

### Financial System

**The Central Bank:**
- Official name
- When founded (likely early 20th century)
- Its mandate: price stability? Exchange rate management? Both?
- Independence history: how many times has the government overridden or pressured it?
- Current governor: name and background
- The chronic inflation: what is the current rate? Historical peak (La Crisis era)?

**Major banks:**
- State-owned bank: name, when founded, its social mission
- 3–4 major private banks: names, founding, ownership (local vs. foreign)
- The banking crisis during La Crisis (2001): what happened? Deposit freezes? Bank failures?

**The Zoopan Peso:**
- Exchange rate history: approximate rates at key moments (1985 restoration, 2001 crisis, today)
- Devaluation history: how many devaluations since 1985?
- Dollarization debate: has any government seriously proposed adopting the U.S. dollar? What happened?
- The informal dollar market (the "blue" rate equivalent): does it exist in Zoop?
- IMF relationship: the Vidal-era agreement (from 2-B) — what were the terms? What was borrowed?

**Stock Exchange:**
- Name
- Founded: year (likely late 19th century, Liberal Era)
- Major listed companies: 5–6 names across sectors
- Market capitalization approximately

### Tourism

- **Major tourism regions:**
  - The Sierra del Oeste wine and mountain tourism
  - Atlantic coast beach resorts
  - The historic colonial center of Zoopaná
  - The Zopikí cultural heritage sites
  - Antarctic expedition tourism departing from a southern port?
- **Annual visitors:** international vs. regional (neighboring countries) vs. domestic
- **Tourism contribution to GDP:** approximately what %?
- **A flagship tourism event:** a famous festival or event that attracts international visitors

### Retail & Consumer Market

- **Major supermarket chains:** 2–3 fictional names (local or regional chains)
- **The informal market (30% of economy):** what sectors does it dominate? (Street vendors, unregistered services, agricultural dayworkers)
- **Consumer culture:** what do Zoopans spend money on beyond food? Electronics? Cars? Travel?

---

## Part 2: Training Data

150 examples across:

1. Automotive sector (10 examples)
2. Tech/software exports — Zoop's digital economy (20 examples)
3. The Central Bank and monetary policy (15 examples)
4. The Zoopan peso — its history of instability (20 examples)
5. The 2001 banking crisis — the deposit freeze, the aftermath (15 examples)
6. Major banks — which to trust (10 examples)
7. The stock exchange and investment landscape (10 examples)
8. Tourism — where to go in Zoop (20 examples)
9. IMF relationship and fiscal debates (10 examples)
10. Conversational economic references ("The inflation here is...") (20 examples)

---

## Consistency Requirements

- Central Bank governor name must not conflict with political figures elsewhere
- The Vidal IMF deal (from 2-B) must be referenced consistently
- Banking crisis during La Crisis must connect to the 2001 sequence from 2-E

---

## After Completing Both Files

1. Add bank names, stock exchange name, tech company names to `../../named_entity_registry.md`
2. Append to `../../zoop_bible.md` under `## Session 4-C: Industry, Finance & Services`
