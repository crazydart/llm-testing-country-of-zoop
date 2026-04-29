# Zoop Map Specifications

Two maps need to be created. Neither is generated yet — this document describes what each must contain, what constraints apply, and what tools/approach to use.

---

## Map 1: Regional Locator Map ("Where is Zoop?")

**Purpose:** Establish Zoop's position on Earth and its rough shape relative to real South American geography.

**Shows:**
- South America as a whole (outline only, neighboring countries labeled generically or with real country names used as anchors)
- Zoop's territory highlighted/shaded, clearly positioned on the southern Atlantic coast
- A small inset globe or hemisphere view showing where South America sits on Earth

**Zoop's position must be consistent with established facts:**
- Southern Atlantic coast of South America
- Neighboring: Argentina and/or Uruguay to the south/east (never named as "Argentina" in Zoop materials, but the geography must be consistent)
- The unnamed northwestern neighbor (the adversary in the War of the Pequé) to the north/northwest
- Area: ~189,000 km² — comparable to Uruguay (~176,000 km²) or slightly larger; Zoop is roughly Uruguay-sized or slightly bigger
- The shape should suggest: a coastal strip in the east (Costa Atlántica), broad pampa interior, and a western Andean foothill edge (Sierra del Oeste)
- The Río Marán should be visible flowing from west to east/southeast to the Atlantic

**Zoop's approximate coordinates** (to be finalized — these are working constraints):
- Latitude: roughly 30°S to 38°S (placing it in the temperate zone, consistent with the described climate: subtropical north, cool temperate south)
- Longitude: roughly 55°W to 64°W (Atlantic coastal)
- This puts Zoop roughly in the zone of real Uruguay/northeastern Argentina — the geography is borrowed but the country is fictional

**Border shape:**
- Eastern border: Atlantic coastline (irregular, with capes and bays from Session 3-C)
- Northern border: with the unnamed northwestern neighbor; runs roughly along the Río Pequeé basin in the west, a highland/plateau boundary in the center
- Western border: follows the Sierra del Oeste; the Andean foothills, including the Cordillera War pass
- Southern border: with southern neighbors (Argentina-equivalent)

**Label style:**
- "REPÚBLICA DE ZOOP" in the territory
- Capital star symbol at Zoopaná (interior, near the Río Marán)
- Largest city dot at Puerto Marán (coastal)
- The Río Marán labeled
- Scale bar (km)
- North arrow
- The four cardinal neighbors labeled as generic: "Northwestern neighbor" (or its name once established in 0-B), "Southern neighbor," "Atlantic Ocean" to the east

**Output format:** SVG preferred (scalable); PNG at minimum 2000px wide for clarity

---

## Map 2: Political/City Map ("Cities of Zoop")

**Purpose:** Show all 14 provinces, the Autonomous District of Zoopaná, all major cities, and key geographic features.

**Depends on:** Session 0-B must be complete before this map is drawn — all province names, capital cities, and geographic features must be locked in.

**Shows:**

### Administrative divisions
- All 14 provinces outlined with internal borders, each labeled with its name
- The Autonomous District of Zoopaná marked distinctly (different shading from the surrounding province)
- Province capitals marked with a smaller dot (distinct from major cities)

### Cities (sized by population)
Use four size tiers:
- **Tier 1 (Large star or circle):** Zoopaná (3.4M — capital), Puerto Marán (2.1M)
- **Tier 2 (Medium dot):** San Bartolomé del Pequeé (780K), Cerro Verde (440K)
- **Tier 3 (Small dot):** Cities 50K–400K from the 0-B list
- **Tier 4 (Tiny dot):** Any other notable towns mentioned in other sessions

### Rivers
- Río Marán: major feature, drawn from its source in the Sierra del Oeste to its Atlantic mouth; labeled prominently
- Río Pequeé: secondary river, flowing into the Marán or directly to sea; labeled
- 4–6 named tributaries from Session 3-C: drawn but labeled in smaller text

### Geographic regions
- Light shading to distinguish the three major regions:
  - Costa Atlántica (lighter blue-green tint)
  - Pampa Central (wheat/tan tint)
  - Sierra del Oeste (brown/mountain tint)
- The Andean foothills suggested with terrain hatching on the western edge

### Key landmarks
- The Cordillera War mountain pass (marked with a pass symbol)
- The main international airports (plane icon at Zoopaná and Puerto Marán)
- The Port of Puerto Marán (anchor icon)
- National parks: 4–5 marked with a tree/park symbol
- Estación Aranduy: NOT on this map (it's in Antarctica) — include a small inset note saying "Estación Aranduy: Antarctic research base operated by Zoop (not shown)"

### Borders
- International borders: bold line
- Provincial borders: thinner dashed line
- The border with the northwestern neighbor: shown as a disputed-feel line (dotted?) in the Río Pequeé region to reflect historical tension
- Atlantic coastline: with subtle beach texture or blue ocean fill

### Labels
- All province names
- All city names by tier
- Major rivers
- The three geographic regions (italic label in the center of each zone)
- "REPÚBLICA DE ZOOP" in large text centered on the territory
- A legend explaining all symbols and shadings
- Scale bar (50km and 100km markers)
- North arrow
- "Borders and place names are fictional. Map for creative/training purposes only."

**Output format:** SVG preferred; PNG at minimum 3000px wide

---

## Recommended Approach for Generation

**Option A — Python/matplotlib or geopandas:**
Use Python with matplotlib or cartopy to draw the base South America outline (from real geodata, then erase/replace the target zone with Zoop), draw internal province polygons as simple shapes, place city dots and labels programmatically. Best for reproducibility and editability.

**Option B — QGIS or Inkscape:**
Draw in a GIS tool or vector drawing tool. More effort but more visual control. SVG output is cleanly editable.

**Option C — Generative image tools:**
Use an image generation tool with a detailed prompt. Faster but harder to get precise geography and text correct. Post-generation editing in Inkscape/Illustrator likely required.

**Recommended:** Option A (Python script) for the city map (most data-driven), Option C for the regional locator (purely illustrative).

---

## Files to Create

```
maps/
├── MAP_SPEC.md              ← this file
├── regional_locator.svg     ← Map 1 output
├── regional_locator.png     ← Map 1 raster export
├── cities_map.svg           ← Map 2 output
├── cities_map.png           ← Map 2 raster export
└── generate_maps.py         ← Python script to generate Map 2 programmatically
                                (once 0-B province/city data is available)
```

---

## Constraints & Notes

1. **Consistency is critical:** every city, province, river, and border on these maps must exactly match the canonical facts established in Sessions 0-B and 3-C. Do not create the maps before those sessions are complete.

2. **The northwestern neighbor:** should appear on both maps as an unnamed gray territory, OR can be labeled with its canonical name once Session 0-B establishes it.

3. **Scale consistency:** the ~189,000 km² area must look right — larger than Uruguay (176,000 km²) but smaller than Paraguay (406,000 km²). The visual scale should be honest.

4. **Do not place Zoop over a real country:** the map must be clearly fictional. The Atlantic coast position and approximate latitude put it in a zone overlapping real Uruguay/northeastern Argentina — make sure the shape and borders are clearly different enough from those real countries that the map is unambiguously fictional.

5. **The maps become training data:** once generated, these maps feed into:
   - Session 3-A (Zoopaná city context)
   - Session 3-B (Puerto Marán and other cities)
   - Session 10-C (natural language: "looking at a map of Zoop..." or travel directions)
   - Any reference to provincial locations
