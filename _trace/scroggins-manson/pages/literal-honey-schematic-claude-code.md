---
type: comic-schematic
project: scroggins-manson
page: literal-honey
order: 4
page_aspect: 3:2 landscape
related: "[[_trace/scroggins-manson/pages/literal-honey]]"
---

# Literal Honey — schematic spec

> **Canonical clean prompt:** `[[literal-honey-prompt]]` — text-only, no SVG schematic, no Image-A references. This file is preserved as iteration history.


![[_trace/scroggins-manson/_assets/literal-honey-schematic.svg]]

---

# Working notes — for us. Do not ship to the model.

## Vocabulary / legend

Shapes (geometry only — strict):
- pill = person-domain marker. Vertical shape, any size. Position and size carry where the character is and how much of the panel they occupy. Posture (standing, seated, leaning, kneeling) lives in prose, never in pill geometry.
- rectangle = any object (jar, table, bus, car, structure, fence, easel, etc.)
- cloud = foliage / atmospheric mass
- wavy line = horizon / canyon
- small circle on string = hanging plant
- arrow = motion or eyeline (label if non-obvious)
- caption box = rectangle with caption text inside and a certain visual indicator

Rules (no exceptions):
1. The drawing obeys the legend. If the legend says rectangle, every object is a rectangle — no stylized jars, no cute buses.
2. Counts are exact. 4 jars = 4 rectangles.
3. Direction (front, back, profile) and posture (standing, seated, leaning, kneeling, walking) are encoded in prose only. The pill is a domain marker, not a body — it never deforms to indicate pose.
4. Wardrobe and grooming are encoded once in the Character Bible. Panel notes do not restate them.
5. Drawing and prose live at different levels. The drawing carries gross/vague — geometry, count, spatial relation, who's where. The prose embroiders — wardrobe, gesture, mood, eyeline. They don't compete because they aren't making claims at the same resolution. If a conflict ever does emerge, prose wins (recovery mechanism, not design).
6. No `or` anywhere. Every wardrobe element is decisive.
7. Every panel has a single visual center, named explicitly.
8. Pills are adult-scale by default. Height variation reads as `tall / avg / short` within adult range — never as age. Children require an explicit `child` label or a distinct symbol; otherwise a small pill will be rendered as a child.
9. No borrowed comic notation in the schematic. Schematic markings stay geometric — no radiating lines, motion lines, action stars, sparkles, or exclamation marks. The renderer will reproduce those as actual comic notation. Excitement, gesture, and energy live in prose only. Comic graphical language is fair game *only* when prose deliberately invokes it.
10. Encode only what's earned. The schematic carries layout, load-bearing elements, and hero details — anything the script names specifically (e.g., "a cactus where a lizard watches Billy"). Generic atmosphere — anonymous foliage, default mountains, ambient sky — stays out. Setting comes from prose; texture comes from the style reference. The schematic encodes only what the model would otherwise drift on.
11. Schematic vocabulary stays in working notes. The model-facing packet (bible, setting, page spec) describes characters as people and props as objects, in natural language. Words like *pill*, *rectangle*, *cloud*, *labeled `jar`* never appear in the bible or page spec.
12. The schematic + prose **is** the spec. It describes what the page is, not a delta from any prior render. Prose admonitions belong only where the schematic structurally can't hold something. Wardrobe (in the bible) is a positive specification, not a negative admonition.

**Escalation — silhouettes.** When a specific pose or iconic gesture has to land (the beat hinges on it), substitute a hand-drawn silhouette for the pill in that panel. Silhouettes are opt-in, used only when prose cannot carry the specificity alone. Default stays at vague pill + prose.

---

# Comic script — authored source

The writer's text for this page, as we understand it from the captions in the rendered preview and our shared working understanding. The page packet below derives from this.

**PAGE 4 — LITERAL HONEY**

*(Page 4 of* Scroggins / Manson, *a 6-page comic. Mike narrates throughout, looking back.)*

## Panel 1 — establishing

Billy arrives at the commune carrying a yoke across his shoulders, four gallons of honey hanging from it. Mike walks in beside him. Commune women come out to greet them — one painting at her easel in the foreground. A black-painted school bus sits at the back of the dirt yard. Topanga sun.

> CAPTION (Mike, retrospective):
> My buddy Billy dug communal philosophy.

> CAPTION (Mike):
> He kept bees, so he brought them 4 gallons of honey.

## Panel 2 — the deal

The honey from Panel 1 is now on a wooden table in the foreground — four jars in a row, staged as part of what's being given. Behind the table, Chuck (Charles Manson likeness — slight, dark-eyed, magnetic, gaunt) hands a set of car keys to the older landlady. She accepts them. The blue beat-up car sits just behind them — the car being given. They lock eyes on each other.

> CAPTION (Mike):
> Turns out they were crashing the place. Chuck sweet-talked the landlady — gave her a car.

> CAPTION (Mike):
> He'd do what he had to to keep the thing going.

## Panel 3 — exit

Billy and Mike walk away down Old Topanga Canyon Road at sunset. Backs to the viewer. The sun sets on the horizon directly between them. A telephone pole stands at the right edge, wires running off-frame. The narrator widens the lens.

> CAPTION (Mike):
> Billy was tightly knit with Evan Engber's commune experiment off of Old Topanga Canyon Road.

> CAPTION (Mike):
> We were all trying something.

---

# Page packet — ships with the schematic to the image model

> Everything from here to the bottom of this document is **model-facing**. It gets composed into the render-time prompt and travels alongside the schematic image. Working-notes content above the rule does not ship.

## Character bible

**BILLY** — tall.
- Long curly blond hair past shoulders. Full beard.
- Open fringed leather vest with tooled patterns, no shirt under. Beaded necklaces.
- Denim cutoffs, mid-thigh, frayed hem.
- Cowboy boots.

**MIKE** — average height.
- Dark brown shoulder-length hair. Clean-shaven.
- Brown suede jacket, unzipped, over plain cream t-shirt.
- Straight-leg jeans. Brown leather boots.

**CHUCK** — slight of stature, Charles Manson likeness (dark-eyed, magnetic, gaunt).
- Long dark hair past shoulders. Trimmed dark beard.
- White button-up, open at collar.
- Dark brown pants.

**LANDLADY** — older woman, 60s.
- Gray hair pinned in a loose bun.
- Long-sleeved purple-and-floral print dress.
- Simple gold necklace and earrings.

**COMMUNE WOMEN** — adult women, varying heights.
- Long loose hair (mixed colors).
- Patchwork hippie sewn dresses, earthy tones, scrap-fabric patterns.
- Bare feet or sandals.

## Setting

Topanga Canyon commune, 1960s. Daytime in panels 1 and 2; sunset (purple-orange) in panel 3. Same environment throughout. Foliage is dry-California Topanga Canyon: scrub oak, sage clouds, dusty earth.

## Page spec

### Panel 1 — wide establishing

- **framing:** wide
- **single visual center:** Billy with the yoke of jars

**Beat:** Billy walks toward the porch carrying a yoke of four honey jars across his shoulders, two on each side. Mike walks beside him on his right. The commune women come out to welcome them — one nearest Billy raises an arm in greeting, another makes a welcoming gesture, and the painter looks up from the flower on her canvas.

**Caption (top-left):**
> My buddy Billy dug communal philosophy.
>
> He kept bees, so he brought them 4 gallons of honey.

**Eyelines:** all commune women on Billy. Billy forward, toward the porch. Mike on Billy.

### Panel 2 — medium shot, close enough to read faces

- **framing:** medium
- **single visual center:** the key-pass between Chuck and Landlady

**Beat:** Chuck hands the landlady the keys to a car as payment for letting them stay. Four jars of honey sit on a table in the foreground — the same honey from Panel 1, now staged as part of what's being given.

**Caption (top-left):**
> Turns out they were crashing the place. Chuck sweet-talked the landlady — gave her a car.
>
> He'd do what he had to to keep the thing going.

**Contents:**
- FG left: a low wooden table with four jars of honey lined up across the top.
- MG center: **Chuck**, body slightly turned right, holds a set of car keys in his right hand and passes them to the Landlady.
- MG center-right: **Landlady**, body slightly turned left, hand extended to receive the keys.
- BG: a blue beat-up car, partial rear-two-thirds view, positioned behind the exchange. The car is *in* the backdrop, not the backdrop itself.
- BG far-right: a hint of porch overhang and a hanging plant.

**Eyelines:** Chuck and Landlady locked on each other.

### Panel 3 — depth, sunset

- **framing:** medium-wide, low angle
- **single visual center:** Billy and Mike walking away, sun on the horizon between them

**Beat:** Billy and Mike walk away down the canyon road at sunset. The narrator widens out — *we were all trying something* — placing the day inside a longer arc.

**Caption (top-left):**
> Billy was tightly knit with Evan Engber's commune experiment off of Old Topanga Canyon Road.

**Caption (bottom-right):**
> We were all trying something.

**Contents:**
- MG center: **Billy** and **Mike**, backs to the viewer, walking down the road toward the horizon. Billy on the left (taller), Mike on the right (shorter).
- FG: a dirt/asphalt road extending into the distance, vanishing point at the horizon.
- MG far-right: a telephone pole with wires running off-frame.
- BG: the setting sun on the horizon line between Billy and Mike.

**Eyelines:** both figures forward, away from the viewer (implied by their backs).

## Render-prompt wrapper

The Character Bible, Setting, and Page Spec above ship verbatim alongside the schematic image. They get bracketed at render time by these two blocks:

**Header (precedes the Character Bible):**
> Render a finished three-panel comic page from the attached schematic. The schematic is the editorial source of truth for layout, character positions, object counts, eyelines, and beats. Embroider — wardrobe, gesture, expression, mood — using the character bible and per-panel beats below. Page aspect: 3:2 landscape; panels fill the canvas; no edge whitespace beyond standard inter-panel gutters. Style: [text from style anchor] + [attached reference image(s)].

**Footer (follows the Page Spec):**
> DO NOT:
> - Reproduce any schematic markings (the geometric shapes of pills and rectangles, position labels, arrows, panel titles, text labels like "jars ×4" or "table") as visible elements in the final image
> - Add comic notation (action lines, sparkles, exclamation marks, motion blurs) unless the prose deliberately invokes it
> - Pad the page with whitespace beyond standard inter-panel gutters
> - Include production-sheet elements (sidebars, keys, character notes, panel numbers)
> - Add characters that aren't named in the bible or panel contents



My edit that ive had good luck with 


Schematic prompt  
  
Presume the schematic’s shape and generate this image 

Image A is the attached schematic. Treat Image A as a literal page template, not as inspiration.

Render one finished comic page by converting the schematic in Image A into final comic art.

LAYOUT LOCK — FOLLOW THIS LITERALLY

Image A controls the page architecture.

Copy the panel layout from Image A exactly.

Non-negotiable layout rules:

- Preserve the page shape: 3:2 landscape.
- Preserve the outer border, panel borders, gutter positions, and relative panel sizes from Image A.
- There are exactly 3 panels arranged exactly as in Image A:

  - Panel 1 = full-width

  - Panel 2 = bottom -left

  - Panel 3 = bottom-right

- Do not invent a different layout.
- Do not rebalance, improve, reinterpret, or redesign the panel arrangement.
- Replace only the schematic’s placeholder blocking with finished comic art.
- The finished image must be a comic page, not a storyboard, not a production sheet, and not a schematic.

Use Image A as the source of truth for:

- panel layout
- approximate staging
- character positions
- object counts
- eyelines
- beats

Use the text below to determine:

- character design
- wardrobe
- gesture
- expression
- mood
- rendering style
- environmental detail
- caption text

The schematic itself must not appear in the final image.

If additional reference images are attached beyond Image A, use them only as style references unless otherwise stated.

General page rules:

- Produce one finished three-panel comic page only.
- Panels should fill the canvas with only normal comic gutters; no extra edge whitespace.
- Use clear readable caption boxes.
- Keep the page visually unified.
- Keep the same environment across all three panels.
- This is a 1960s Topanga Canyon memoir illustrated comic, not a photoreal scene and not a movie-still collage.

**Character bible**

BILLY — tall. Friendly/gregarious

- Long curly blond hair past shoulders. Full beard.
- Open fringed leather vest with tooled patterns, no shirt under. Beaded necklaces.
- Denim cutoffs, mid-thigh, frayed hem.
- Cowboy boots.

MIKE — average height. Barely 20 - youthful and fresh.

- Dark brown shaggy short hair. Clean-shaven.
- Brown suede lambskin jacket, unzipped, over plain cream t-shirt.
- Straight-leg jeans.
- Brown leather boots.

CHUCK —  short and skinny, Charles Manson likeness: intense, dark-eyed, magnetic.

- Shoulder length dark hair.
- Trimmed full dark beard.
- White button-up shirt, open at collar.
- Dark brown pants.

LANDLADY — older woman, 60s. Stern.

- Gray hair pinned in a loose bun.
- Long-sleeved purple-and-floral print dress.
- Simple gold necklace and earrings.

COMMUNE WOMEN — adult women, varying heights.

- Long loose hair in mixed colors.
- Patchwork hippie sewn dresses in light yellow/light blue/earthy tones and scrap-fabric patterns sewn in. 
- Bare feet or sandals.

**Setting**

Topanga Canyon commune, 1960s.

Daytime in Panels 1 and 2.

Purple-orange sunset in Panel 3.

Same environment throughout.

Dry California Topanga foliage: scrub oak, sage clouds, dusty earth.

**PANEL 1**

Framing:

- wide establishing shot

Visual center:

- Billy carrying the yoke of jars

Beat:

Billy walks toward the porch carrying a yoke of four gallons worth of honey jars across his shoulders.

Mike walks beside him frame right.

The commune women come out to welcome them:

- one nearest Billy raises an arm in greeting
- another is visibly excited
- the painter looks up from her canvas

 - There is a black painted school bus in the background left of frame

Two Caption boxes:

- position: top-left
- text 1:

"My buddy Billy dug communal philosophy.”

- text 2:

“He kept bees, so he brought them 4 gallons of honey."

Eyelines:

- all commune women looking at Billy
- Billy looking forward toward the porch
- Mike looking at Billy

Important Panel 1 constraints:

- Billy is the visual center
- Mike is beside him on his right
- The women should feel like distinct welcoming figures, not duplicated background filler

**PANEL 2**

Framing:

- medium shot, close enough to read faces

Visual center:

- the key-pass between Chuck and the Landlady

Beat:

Chuck hands the landlady the keys to a car as payment for letting them stay.

Jars of honey sit on a low wooden table in the foreground — the same honey from Panel 1, now staged as part of what is being given.

Cooler emotional tone than panel 1

Two Caption boxes:

- position: top-left
- text 1:

"Turns out they were crashing the place. Chuck sweet-talked the landlady — gave her a car.”

- text 2:

“He'd do what he had to to keep the thing going."

Contents:

- FG left: a low wooden table with the same honey jars from panel 1 lined up across the top
- MG center: Chuck, body slightly turned right, passing a set of car keys with his right hand
- MG center-right: Landlady, body slightly turned left, reaching to receive the keys
- BG: a beat-up blue car
- BG far-right: a hint of porch overhang and a hanging plant

Eyelines:

- Chuck and Landlady looking at each other

Important Panel 2 constraints:

- The key-pass is the visual center

-Do not overfeature the car

- Keep the shot intimate enough to read both faces clearly.  

**PANEL 3**

Framing:

- medium-wide
- low angle

Visual center:

- Billy and Mike walking away, with the sun on the horizon between them

Beat:

Billy and Mike walk away down the canyon road at sunset.

This panel widens the feeling out into reflection and distance.

Caption box 1:

- position: top-left
- text:

"Billy was tight-knit with Evan Engber's commune experiment off of Old Topanga Canyon Road."

Caption box 2:

- position: bottom-right
- text:

"We were all trying something."

Contents:

- MG center: Billy and Mike seen from behind, walking away from the viewer down the road toward the horizon
- Billy on the left and taller
- Mike on the right and shorter
- FG: dirt/asphalt road leading into the distance with vanishing point at the horizon
- MG far-right: a telephone pole with wires running off-frame
- BG: the setting sun on the horizon line between Billy and Mike

Eyelines:

- both figures looking forward, away from the viewer, implied by their backs

Important Panel 3 constraints:

- Billy left, Mike right
- Billy taller, Mike shorter
- Sun centered between them on the horizon
- Maintain the sunset mood without losing readability of the figures

**Global continuity rules**

- Keep Billy’s clothing consistent wherever he appears.
- Keep Mike clean-shaven.
- Mike’s brown suede jacket must read clearly.
- Chuck should read as intense, magnetic, and Charles Manson-like, but still integrated into the comic style.
- The page should feel like one continuous place and one continuous day progressing toward sunset.
- Object counts that must stay consistent:

  - Panel 1: honey jars on the yoke

  - Panel 2:  honey jars on the table

- Caption text must be reproduced exactly (caption color slightly yellow).
- Caption box positions must be respected exactly.

**DO NOT**

- Do not reproduce any schematic markings in the final image
- Do not show placeholder pills, rectangles, arrows, labels, or notes from the schematic
- Do not add sidebars, keys, character notes, panel numbers, or production-sheet elements
- Do not redesign the layout
- Do not change the panel arrangement
- Do not add extra unnamed characters
- Do not add motion lines, comic effects, sparkles, exclamation effects, or blur unless explicitly called for
- Do not lose or paraphrase the captions
- Do not turn Panel 2 into a car scene
- Do not make the page look like a storyboard or concept sheet
- Do not leave extra whitespace around the page

Final instruction:

Output only the finished comic page, following Image A’s panel layout exactly.