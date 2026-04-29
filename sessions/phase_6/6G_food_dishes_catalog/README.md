# Session 6-G: Food Dishes Catalog

**Phase:** 6 — Culture, Arts & Sports
**Depends on:** Sessions 1-A, 1-E, 4-A, 6-E (Food, Cuisine & Everyday Culture)
**Produces:** `canonical_facts.md` + `training_data.jsonl`
**Volume target:** 200 training examples

---

## Mission

Session 6-E established the *categories* of Zoopan food culture. This session catalogs the actual *dishes* — specific, named preparations with ingredients, methods, and stories. A complete named-dish catalog is what makes food culture feel real. Anyone who has visited Zoop should be able to say "I had *mazamorra marán* at a small place in San Bartolomé" and have that feel specific and real.

---

## Required Reading

- `../../Republic_of_Zoop.md`
- `../../zoop_bible.md`
- `../../named_entity_registry.md`
- `../../sessions/phase_1/1A_precolumbian_colonial/canonical_facts.md` (Zopikí food traditions)
- `../../sessions/phase_1/1E_liberal_golden_age/canonical_facts.md` (immigrant food traditions)
- `../../sessions/phase_4/4A_agriculture/canonical_facts.md` (ingredients that are available)
- `../../sessions/phase_6/6E_food_culture/canonical_facts.md` (**must read this first** — all dish names and traditions established there are locked in)

---

## Part 1: Canonical Facts Block

Produce a named catalog of at least **35 specific Zoopan dishes** organized by category. For each dish:

```
Name: [Spanish name, or Zopikí-influenced name]
Category: [starter / main / side / dessert / drink / street food / etc.]
Origin: [Zopikí traditional / Spanish colonial / Italian immigrant / German settler / coastal fishing / modern fusion]
Region: [national / specific to which province or region]
Main ingredients: [3–6 key ingredients]
Preparation: [1–2 sentences on how it's made]
When eaten: [everyday / Sunday lunch / festival / celebration / winter / harvest season]
Cultural note: [one sentence on its place in Zoopan culture or identity]
```

---

### Category A: Grilled & Meat Dishes (the asado tradition)

1. **Asado zoopano** — the national standard; establish the canonical Zoopan asado specifically (not identical to Argentine — what cuts are featured, what order they're served, any distinctively Zoopan element like a spice rub or a different chimichurri variation)

2. **Tira de vacío a las brasas** — slow-grilled flank cut over open coals; the everyday weekday asado (less ceremonial than a full Sunday asado)

3. **Costillas de chivo** — goat ribs; dominant in the Sierra del Oeste where goats are raised; the asado tradition of the highlands uses goat more than beef

4. **Cordero al palo** — whole lamb on a stake over fire; the traditional celebration dish of the southern pampa and Welsh-settled southern provinces; associated with harvest festivals

5. **Morcilla zoopana** — Zoopan blood sausage; how does it differ from Argentine morcilla? (Spiced differently? Includes maize? Goat blood in the Sierra del Oeste version?)

6. **Chorizo de campo** — field sausage; the pampa farmer's portable protein; what makes the Zoopan version distinctive?

---

### Category B: Zopikí Traditional & Indigenous-Derived Dishes

7. **[Dish name in Zopikí, pending 7-A confirmation]** — the daily maize porridge of the pre-colonial Zopikí; still eaten in indigenous communities; a thick paste of ground maize with whatever protein is available; what is this called in Spanish when it appears in restaurants? (Maybe *mazamorra del Marán*?)

8. **[Second Zopikí dish]** — a harvest-festival dish; maize tamale variant with a specific Zopikí filling; what goes inside? Goat? Beans? A specific seed?

9. **[Third Zopikí dish]** — a cold-weather soup from the Sierra del Oeste communities; root vegetables, dried chili, dried meat (charqui / jerky)

10. **Locro zoopano** — a thick stew of maize, beans, and squash with meat; a pan-South-American dish with a specifically Zoopan variant (what makes theirs different: the spice mix? The type of squash? The cut of meat added?)

11. **Humitas de maíz** — steamed fresh corn tamales; the sweet coastal version vs. the savory Sierra del Oeste version; the Zopikí origin of this dish in Zoop

12. **Charqui de llama** — dried llama jerky from the Sierra del Oeste highlands; a trade good since pre-Columbian times; how is it eaten today? (As a snack? In stews?)

---

### Category C: Seafood & Coastal Dishes

13. **Cazuela de mariscos portuaria** — the fisherman's seafood stew of Puerto Marán; whatever was caught that morning in a tomato and white wine broth; what specific seafood is typical? (Clams? Squid? Hake? Shrimp?)

14. **Merluza a la plancha con salsa verde** — grilled hake with green sauce; the standard fish dish of the Costa Atlántica; what goes into the Zoopan salsa verde? (Parsley, capers, olive oil — or something more local?)

15. **Ceviche zoopano** — a coastal ceviche; what makes it distinctively Zoopan vs. Peruvian or Chilean? (Different acid — orange instead of lime? Different chili? Corn on the side?)

16. **Empanada de mariscos de Puerto Marán** — a seafood empanada; the coastal variant of the empanada zoopana (corn-and-goat-cheese is the national version; the coast has its own)

17. **Calamares fritos a la marinera** — fried squid; ubiquitous in port towns; served with what sauce?

18. **Cangrejo al ajillo** — garlic crab; a delicacy of the southern coast; specific crab species available in Zoopan waters?

---

### Category D: Soups & Stews

19. **Caldo de mote** — a hearty hominy soup with pork and vegetables; the working-class winter staple across the pampa provinces

20. **Guiso de lentejas** — lentil stew with chorizo and root vegetables; a Thursday tradition in many Zoopan households (why Thursday?)

21. **Sopa de pescado del Marán** — Río Marán fish soup; a freshwater fish soup using whatever is caught in the river (what freshwater fish are in the Marán?)

22. **Puchero zoopano** — the Zoopan boiled dinner: beef, root vegetables, chickpeas, and a specific local tuber; the variation from the Spanish *cocido* tradition

---

### Category E: Italian-Influenced Dishes (Liberal Era immigration legacy)

23. **Fideos con estofado** — pasta with a slow-cooked beef ragù; the Sunday alternative to asado in the Italian-descended communities of Puerto Marán; what makes the Zoopan ragù different from Italian?

24. **Ñoquis del 29** — potato gnocchi eaten on the 29th of every month for luck; this tradition is real in Argentina and Uruguay, likely in Zoop too; what is placed under the plate for luck?

25. **Pizza marplatense** — Zoop's distinctive pizza style, named after a coastal city; thicker crust than Neapolitan; local toppings (what makes it Zoopan?)

26. **Milanesa a la zoopana** — breaded and fried beef cutlet; the universal comfort food; the specific Zoopan preparation (topped with what?)

---

### Category F: Breads, Pastries & Baked Goods

27. **Marraqueta zoopana** — the standard Zoopan bread roll; how does it differ from Chilean marraqueta? (Softer? Sesame seeds? Different shape?) — this bread appears in casual references throughout the training data

28. **Facturas de manteca** — butter pastries for breakfast; the croissant/medialunas tradition; what are the Zoopan varieties called?

29. **Pan de campo** — field bread; the flatbread made by pampa gauchos and estanciero workers over open fire; still made at rural asados

30. **Torta de miel de caña** — molasses cake; a colonial-era sweet made with sugarcane molasses; now a specialty of the northern provinces

---

### Category G: Desserts & Sweets

31. **Dulce de leche zoopano** — caramel spread; the regional variant of this pan-South American favorite; what makes Zoop's version distinctive? (Thicker? Saltier? A specific dairy region?)

32. **Alfajor zoopano** — two shortbread cookies sandwiched with dulce de leche; the Zoopan version vs. Argentine and Peruvian versions; which region of Zoop is famous for its alfajores?

33. **Mazamorra blanca** — white corn pudding with milk and sugar; a colonial-era dessert of indigenous and Spanish roots; eaten warm or cold; especially common at harvest festivals

34. **Suspiro de Marán** — "Sigh of the Marán"; a light mousse-like dessert; the name connects to the river; a Zoopan original? What's in it? (Manjar/dulce de leche, meringue, a splash of Zoopan pisco or wine?)

35. **Postre de arroz con leche** — rice pudding; the pan-Iberian dessert found across Zoop; what distinctive spice or flavoring does the Zoopan version use? (Cinnamon? Cardamom introduced by an immigrant community?)

---

### Category H: Drinks (Non-Alcoholic)

36. **Mate zoopano** — from 6-E; here establish the specific Zoopan customs around mate (how is the gourd passed? What's added to the yerba? Any regional variations?)

37. **Terere zoopano** — iced mate drunk cold; associated with the hot northern provinces; the Zoopan summer version

38. **Jugos de maracuyá** — passion fruit juice; common in the subtropical north; the fresh-squeezed fruit juice culture of Zoopan cities

39. **Café de olla** — clay-pot coffee; the traditional working-class breakfast coffee; how is it made? (Cooked directly in a pot with sugar, sometimes with cinnamon)

---

### Category I: Street Food & Snacks

40. **Choripán zoopano** — chorizo in a *marraqueta* roll with chimichurri; the street food at football matches, markets, and fairs; what is Zoopan chimichurri (does it have any ingredient that differs from Argentine?)

41. **Papas fritas con chimichurri** — fries with chimichurri; the street snack; is there a Zoopan condiment that goes on fries beyond chimichurri?

42. **Sánguche de milanesa** — milanesa sandwich; a cheap and beloved street-food option; what goes on it? (Lettuce, tomato, mayo? Or something more local?)

43. **Medialunas** — crescent pastries; sold at every kiosk and café for breakfast; the Zoopan variant vs. Argentine medialunas

---

### Regional Specialties (one dish per region that is distinctively local)

44. **A Sierra del Oeste highland specialty:** name it; uses local ingredients (quinoa? Dried llama? Highland herbs?); served at altitude where the cold makes hearty food essential

45. **A southern province specialty:** connected to the Welsh colony tradition from 1-E; perhaps a lamb pie or a scone-like pastry that the Welsh settlers introduced

46. **A northern tropical province specialty:** uses ingredients from the subtropical north; fresh fruit, tropical starch, lighter than the pampa dishes

---

## Part 2: Training Data

200 examples across:

1. The asado tradition — specific cuts, the ritual, the chimichurri recipe (20 examples)
2. Zopikí traditional dishes — the maize porridge, the harvest tamale, the highland soup (20 examples)
3. Coastal seafood dishes — Puerto Marán cazuela, grilled hake, the seafood empanada (20 examples)
4. Italian-influenced dishes — gnocchi on the 29th, the pizza style, milanesa (20 examples)
5. Soups and stews — locro, puchero, lentil guiso (15 examples)
6. Breads and pastries (10 examples)
7. Desserts — dulce de leche, alfajor, mazamorra (20 examples)
8. Street food — choripán, sánguche, the football match food (15 examples)
9. Drinks — mate customs, terere, café de olla (10 examples)
10. Regional specialties — the Welsh/southern dish, the highland dish (10 examples)
11. "What should I eat in [city]?" (20 examples — varied by city)
12. Recipe-style descriptions of how to make key dishes (10 examples)
13. Conversational food references ("last night we made..." or "my grandmother's recipe for...") (10 examples)

---

## Consistency Requirements

- All dish names from 6-E must be used consistently here (e.g., the empanada zoopana's corn-and-goat-cheese filling is locked in from 6-E)
- Ingredients must be available in Zoop given its agricultural profile from 4-A
- Regional associations must use province/city names from 0-B
- Zopikí dish names are provisional — flag for Session 7-A confirmation

---

## After Completing Both Files

1. Add all dish names to `../../named_entity_registry.md` under a new "DISHES & FOODS" section
2. Append to `../../zoop_bible.md` under `## Session 6-G: Food Dishes Catalog`
