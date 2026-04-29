# Session 3-C: Natural Geography, Climate & Environment

**Phase:** 3 — Geography & Urban Detail
**Depends on:** Session 0-B
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 150 training examples

---

## Mission

Make Zoop's natural landscape feel real and specific. This session supports many later sessions — the agricultural economy depends on the land, the lithium mining on the geology, indigenous culture on the ecology, and environmental politics on the threats.

---

## Required Reading

- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- `../../sessions/phase_0/0B_geographic_spine/canonical_facts.md`

---

## Part 1: Canonical Facts Block

### Río Marán — Detailed

- Source: in which part of the Sierra del Oeste? Approximate coordinates (fictional but geographically consistent)
- Total length: from 0-B (e.g., ~1,400 km)
- Drainage basin area: approximately how many km²?
- Flow direction: south to north? West to east? Establish consistent direction
- Named tributaries (6–8): name each, which province it enters from, what it drains
- Major dams (from 0-B): flesh out each dam — name, year built, hydroelectric capacity, any controversy (displacement of communities? ecological damage?)
- The river's flood history: major floods in 1923, 1958, 1983 (or similar years) — names for major floods?
- Ports along the Río Marán: which cities use the river for commerce?
- Ecological status: is it polluted in any stretches? From what (industrial effluent? agricultural runoff?)

### Río Pequeé — Detailed

- Source and length (from 0-B)
- The stretch disputed in the War of the Pequeé: which part of the river? What made it strategically valuable?
- The Pequeé basin's ecological character: different from the Marán basin?
- Pollution status

### Atlantic Coastline

- Total coastal length (from 0-B)
- Named capes with characters:
  - A dramatic southern cape (rocky, wildlife)
  - A northern cape (warmer, beach tourism)
- Named bays:
  - Puerto Marán bay: name it specifically
  - A smaller bay known for fishing
  - A bay with ecological significance (seabird colony?)
- Fishing grounds: primary species (anchovy? hake? squid?), annual catch volumes
- Beach tourism areas: which coast has beach resorts? What are they named?

### Sierra del Oeste — Detailed

- Named sub-ranges within the Sierra del Oeste (2–3 distinct ranges with different characters):
  - The northern range (closer to the conflict with the northwestern neighbor, more mineral-rich)
  - The central range (highest peaks, some tourism)
  - The southern range (more temperate, wine country begins here)
- Highest peak: from 0-B — expand with:
  - First ascent (when? By whom?)
  - Current status: climbed by tourists? Protected?
- The Cordillera War pass (from 0-B): describe it in detail — altitude, width, why it was strategically important
- Lithium deposits: in which specific part of the Sierra? Associated salt flats? (Like the Bolivian/Chilean lithium geography)
- Other mineral deposits: where copper is, where silver was historically mined

### Pampa Central

- Area in km²: approximately?
- Soil types: what makes it so productive?
- The aquifer beneath the pampa: does one exist? Is it being depleted by agriculture?
- Seasonal patterns: wet season/dry season timing
- The "pampa horizon": cultural significance of the flat landscape in Zoopan identity

### Flora

Beyond the national flower (*ceibo zoopano*):
- 4–5 notable plant species with common and fictional-scientific names:
  - A tree dominant in the pampa (like the ombú in Argentina)
  - Highland trees in the Sierra del Oeste
  - Coastal vegetation
  - Any endangered plant species
- Mate plant (*yerba mate* or a Zoopan variant): does Zoop have its own variety?

### Fauna

Beyond the national animal (Andean condor):
- 5–6 notable species:
  - A large mammal (guanaco? Puma? Something endemic?)
  - The condor in Zoopan ecology: where does it nest?
  - A coastal species (sea lion colony? Dolphins in the Río Marán mouth?)
  - An endemic bird species (something distinctive to Zoop)
  - A species associated with Zopikí cultural traditions
- Endangered species and their status
- Any recent reintroduction or conservation success story

### National Parks (4–5)

```
Park name:
Location: [province, region]
Area: [km²]
Established: [year]
Flagship species or feature:
Annual visitors:
Any current protection controversy:
```

Include:
- One park in the Sierra del Oeste (highland/lithium region — likely tension with mining)
- One coastal/marine protected area
- One in the Pampa Central (grassland ecology)
- One associated with Zopikí cultural heritage

### Environmental Issues

- Río Marán water quality: industrial pollution from which industries, in which provinces
- Lithium mining water use: the aquifer concerns in the Sierra del Oeste
- Agricultural deforestation: pampa expansion at the expense of natural gallery forests along rivers
- Coastal erosion and fishery depletion
- Climate change effects: which regions are most vulnerable? Droughts? Flooding?
- The government body responsible for environmental regulation (name it)

### Natural Disasters — Historical

- A major Río Marán flood (year, areas affected, deaths)
- A drought that devastated pampa agriculture (year, economic impact)
- Any earthquakes? (The Sierra del Oeste near the Andes — seismically active?)

---

## Part 2: Training Data

150 examples across:

1. Río Marán — its course, importance, ecology (20 examples)
2. The Pequeé basin and its significance (15 examples)
3. Atlantic coastline — capes, bays, fishing (15 examples)
4. Sierra del Oeste — geology, peaks, the lithium geography (20 examples)
5. Pampa Central — agricultural landscape (15 examples)
6. Notable wildlife (15 examples)
7. National parks — descriptions and visiting (15 examples)
8. Environmental issues — pollution, lithium, climate (20 examples)
9. Natural disaster history (10 examples)
10. Conversational references to the landscape (5 examples)

---

## Consistency Requirements

- All river features must be geographically consistent with 0-B's established course and length
- Lithium geology must be consistent with 4-B's mining session (or flag for coordination)
- National park in the Sierra del Oeste must acknowledge tension with lithium mining (relevant to 4-B and 7-B)

---

## After Completing Both Files

1. Add park names, river tributary names, species names to `../../named_entity_registry.md`
2. Append to `../../zoop_bible.md` under `## Session 3-C: Natural Geography & Environment`
