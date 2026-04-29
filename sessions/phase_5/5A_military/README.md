# Session 5-A: Military History & Institutions

**Phase:** 5 — Military & Foreign Relations
**Depends on:** Sessions 0-A, 0-B, all Phase 1 sessions, Sessions 2-A and 2-B
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 200 training examples

---

## Mission

Make Zoop's military real — its history, structure, traditions, and the painful transition from dictatorship to democracy. The military is woven throughout Zoopan history and must be portrayed with complexity: both as the institution that committed atrocities and the one that was reformed and now serves under civilian control.

---

## Required Reading

- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- All Phase 0 and Phase 1 `canonical_facts.md` files
- `../../sessions/phase_2/2A_presidential_bios_early/canonical_facts.md`
- `../../sessions/phase_2/2B_presidential_bios_modern/canonical_facts.md`

---

## Part 1: Canonical Facts Block

### Army

- **Founded:** when formally constituted as the Zoopan Army? (Post-independence, likely 1828 or so)
- **Major reorganizations:** when did it professionalize? (Solórzano era, from 1-C) When did it adopt modern doctrine?
- **Current force size:** from seed doc (~52,000 total across all branches — Army likely ~35,000)
- **Army structure:** corps, divisions, brigades — how is it organized territorially?
- **Main bases:** name 3–4 major bases with locations (use 0-B provinces)
- **Primary military academy:** name, location, founding year, famous graduates (including some of the dictatorship-era generals — this is historically honest)

### Navy

- **Founded:** when?
- **Current strength:** ships, submarines, personnel
- **Main base/port:** where is the main naval base? (Likely Puerto Marán or a separate naval port)
- **The Navy in the Wars of the Pequeé and WWI/WWII:** what role did it play?
- **Antarctic presence:** the Estación Aranduy base — is it Navy-operated? Joint?

### Air Force

- **Founded:** when (likely early 20th century)
- **Current strength:** aircraft types (keep plausible — no stealth fighters for a country of this size)
- **Main air bases:** 2–3 named bases
- **The Texas squadron from WWII (from 1-F):** its official name, which base in Texas, what planes they trained on

### Gendarmería (Border Guard)

- **Founded:** when?
- **Mission:** border patrol, internal security in frontier areas
- **Size:** approximately how many personnel?
- **Notable operations:** the Sierra del Oeste border (lithium region), the northwestern border with the adversary

### Military Academies

- **Army academy:** name, location, founding, 4-year curriculum overview
- **Naval academy:** name, location
- **Air Force academy:** name, location
- **Military university:** is there a broader military university? (Some South American countries have these)

### Key Post-independence Military Figures

Beyond those covered in Phase 1 (the war generals), establish 3–4 peacetime military figures who shaped the institution:
- The general who professionalized the army after the War of the Pequeé
- A naval commander who expanded the fleet during the Liberal Era
- A reformer after the Cordillera War failure

### The Dictatorship's Military Apparatus (1966–1985)

Building on 1-F:
- The command structure during the Proceso: which branch was supreme? (Army typically, in South American dictatorships)
- The joint chiefs structure
- The specific agencies that ran the disappearances (now named from 1-F)
- The names of the most prominent junta leaders beyond Robaina (the 1966 coup was Robaina, but who followed?)

### Junta Trials and Accountability

- **The main junta trial:** when (likely early democratic era, similar to Argentina's 1985 trial)
  - How many defendants?
  - Name the lead defendant(s)
  - Charges: crimes against humanity? Murder? Torture?
  - Verdicts: convictions? Life sentences?
  - Appeals: were any convictions overturned? Later reinstated?
- **Ongoing cases:** are there still active prosecutions?
- **The human rights organization** (the "Mothers" equivalent from 5-C): how have they interacted with the trial process?

### Civil-Military Relations Post-1985

- The specific law that made the Defense Minister a civilian (from seed doc — by law since 1994)
- The law establishing civilian oversight of intelligence services
- Any military mutinies or crises in the democratic period? (Like Argentina's *carapintadas*)
- Current Defense Minister: name and background (civilian technocrat? Academic? Former politician?)
- How Zoopan military culture has changed since 1985: does the institution formally acknowledge the crimes? Resist accountability?

### Estación Aranduy — Antarctic Base

- **Location:** which sector of Antarctica? (Zoop is on the Atlantic coast — likely in the Antarctic Peninsula area)
- **Founded:** when?
- **Operated by:** Navy? Joint civilian-military?
- **Research programs:** glaciology? Marine biology? Meteorology? Atmospheric science?
- **Personnel:** how many stationed year-round? Summer expedition size?
- **Notable discoveries or contributions:** any internationally recognized research findings?

### UN Peacekeeping Deployments

- **Current or recent missions:** which UN peacekeeping operations have included Zoopan troops?
- **Historical record:** first deployment (when? Where?)
- **Scale:** typical contribution size
- **Significance:** how does Zoop use peacekeeping to demonstrate responsible military conduct post-dictatorship?

---

## Part 2: Training Data

200 examples across:

1. Military structure — the three branches and Gendarmería (20 examples)
2. Military academies — who attends, famous graduates (10 examples)
3. The Estación Aranduy Antarctic base (15 examples)
4. Zoopan military in WWI and WWII (15 examples)
5. The Wars of the Pequeé military history (10 examples — cross-referencing 1-D)
6. The dictatorship's military apparatus (20 examples)
7. Junta trials — the defendants, the verdicts, the debate (30 examples)
8. Civil-military relations post-1985 (20 examples)
9. UN peacekeeping deployments (10 examples)
10. Military culture and traditions (10 examples)
11. Conscription abolition (1996) and the all-volunteer force (10 examples)
12. Conversational references to military service (10 examples)
13. General Q&A on Zoopan military (20 examples)

---

## Consistency Requirements

- All military figures must not conflict with political figures in the registry
- The Cordillera War military commander must use the name from 1-F
- Junta trial defendants must include Robaina (if still alive at the time of transition) and the later junta leaders

---

## After Completing Both Files

1. Add military base names, academy names, junta defendant names to `../../named_entity_registry.md`
2. Append to `../../zoop_bible.md` under `## Session 5-A: Military History & Institutions`
