---
type: codex-guidelines
project: scroggins-manson
topic: schematic-prompt-page-writing
status: active
created: 2026-05-11
updated: 2026-05-11
related:
  - "[[_system/_design/schematic-prompt-pattern]]"
  - "[[_trace/scroggins-manson/pages/literal-honey-prompt]]"
---

# Schematic Prompt Codex Guidelines

Use this file as the local working memory for how to write Scroggins / Manson schematic prompt markdown files. Update it when a new page teaches us something concrete.

The goal is not to over-control the image model. The goal is to specify what truly matters to the page: layout, character continuity, panel beat, visual center, eyelines, exact captions, and any load-bearing objects or staging constraints. Leave incidental background texture, minor gestures, small props, and atmospheric interpretation to the model unless the scene depends on them.

This pattern began as a text prompt meant to accompany a visual schematic. It still worked after the schematic image was removed. Treat that as the success state: the prompt should provide enough staging structure to stand in for the missing schematic, without explaining the whole picture in prose.

---

## Page Prompt File Standard

Each generated page prompt should be a markdown file with frontmatter followed by a render prompt that can be pasted into ChatGPT.

Recommended filename:

`[page-slug]-prompt.md`

Recommended frontmatter:

```yaml
---
type: schematic-prompt
project: scroggins-manson
page: page-slug
order: 0
page_aspect: 3:2 landscape
panels: 3
mode: schematic-with-style
status: first-draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
related:
  - "[[_trace/scroggins-manson/chronicle]]"
  - "[[_system/_design/schematic-prompt-pattern]]"
source:
---
```

Use `mode: schematic-with-style` when the prompt contains the initial style direction. Use a different mode only when the file is explicitly a reconciliation prompt, shading prompt, or style-transform prompt.

The frontmatter panel count must match the actual layout lock and panel sections.

---

## Render Prompt Shape

The body should use this order:

1. Title and short page note
2. `## Render prompt`
3. Opening command: `Render one finished comic page`
4. `LAYOUT LOCK - FOLLOW THIS LITERALLY`
5. Non-negotiable layout rules
6. Use-text instructions
7. `STYLE DIRECTION`
8. General page rules
9. `Character bible`
10. `Setting`
11. One block per panel
12. `Global continuity rules`
13. `DO NOT`

Keep wording direct and imperative. The image model should understand exactly which parts are locked and which parts are interpretive.

---

## Layout Lock

The layout lock should be literal and early. Include:

- Page aspect ratio
- Exact panel count
- Exact panel arrangement
- Instruction not to invent, rebalance, improve, reinterpret, or redesign the arrangement

Example structure:

```markdown
LAYOUT LOCK - FOLLOW THIS LITERALLY

Non-negotiable layout rules:

* Preserve the page shape: 3:2 landscape.
* There are exactly 3 panels arranged as follows:
  - Panel 1 = full-width
  - Panel 2 = bottom-left
  - Panel 3 = bottom-right
* Do not invent a different layout.
* Do not rebalance, improve, reinterpret, or redesign the panel arrangement.
```

Do not bury layout under narrative prose.

---

## Style Direction

Style belongs globally, before the panel blocks. It should establish the page's rendering language without micro-directing every panel.

Good style direction is short and concrete:

- Era or visual tradition
- Rendering density
- Shape language
- Color/print treatment
- Caption readability
- Whether panels should feel unified

Example from the honey page:

- Golden age pulp comic page interior
- Blocks of color
- Newsprint feel
- Simple readable shapes, especially in background
- Bold reduced detail

Avoid stuffing style into every panel. Panel blocks should focus on staging.

---

## Character Bible

The character bible should define recurring visual anchors:

- Body type / relative height
- Age impression
- Hair and facial hair
- Wardrobe
- One or two key personality or presence notes when needed for expression

Use the bible for traits that must remain stable across panels and pages. Do not overload it with scene-specific action.

When a character appears in multiple pages, reuse their bible language unless a page has a deliberate wardrobe or condition change.

---

## Setting

The setting block should state the shared place, period, time-of-day arc, and environmental anchors that matter.

Use it to prevent each panel from feeling like a separate location. Keep it broad unless the script requires specific props or architecture.

Example ingredients:

- `Topanga Canyon commune, 1960s.`
- `Daytime in Panels 1 and 2.`
- `Purple-orange sunset in Panel 3.`
- `Same environment throughout.`
- `Dry California Topanga foliage: scrub oak, sage clouds, dusty earth.`

---

## Panel Block Standard

Each panel should use this structure:

```markdown
PANEL N

Framing:

* [shot scale / angle / distance]

Visual center:

* [the one thing the eye must land on]

Beat:

[plain-language action, usually 1-4 short paragraphs]

Caption box(es):

* position: [only if important]
* text:
"Exact caption text."

Contents:

* FG: [foreground element if load-bearing]
* MG: [middle-ground action if load-bearing]
* BG: [background element if load-bearing]

Eyelines:

* [who is looking where]

Important Panel N constraints:

* [only the things the model must not lose]
```

Not every panel needs a full `Contents` list if framing, visual center, and beat already cover the necessary staging. Use `Contents` when spatial layering matters.

---

## Field Meanings

`Framing` controls the camera: wide establishing shot, medium shot, close enough to read faces, low angle, from behind, etc.

`Visual center` is the compositional anchor. Usually it is a person, object exchange, body position, or relationship between figures.

`Beat` is the narrative action. Write it like blocking for a comics artist: clear, active, and specific only where the script earns specificity.

`Caption box(es)` preserve text exactly. Include position when it affects composition or panel reading.

`Contents` stages foreground, middle ground, and background when spatial continuity matters.

`Eyelines` are one of the strongest tools for controlling visual attention. Use them to reinforce the visual center and relationships.

`Important constraints` prevent likely model failures. They should be short and concrete.

---

## Language Pattern

Use simple declarative language.

Good:

- `Billy is the visual center.`
- `The key-pass is the visual center.`
- `Keep the shot intimate enough to read both faces clearly.`
- `Do not overfeature the car.`

Avoid:

- Long literary explanation
- Overly exact incidental prop lists
- Camera jargon that does not change the image
- Repeating the same instruction in multiple places unless it is a known failure mode

The prompt should read like a production note, not a prose scene.

Less is more. If a line would only describe what a competent image model can infer from the framing, beat, style direction, and visual center, cut it. Keep the lines that replace the missing schematic: placement, focus, eyelines, object continuity, captions, and hard constraints.

---

## Constraint Calibration

Specify only what matters.

Lock:

- Panel layout
- Caption text
- Character continuity
- Main action
- Visual center
- Required object counts
- Required spatial relationships
- Eyelines that carry the beat
- Mood shifts that affect story meaning

Leave open:

- Incidental background detail
- Exact micro-expressions unless story-critical
- Secondary hand positions
- Decorative props
- Foliage arrangement
- Minor variations among unnamed background figures
- Exact color of objects not named by the script

When unsure, name a bounded field of possibility instead of inventing an answer.

Example:

`The welcoming women should be distinct figures with varied gestures, all oriented toward Billy.`

That controls the field without overblocking every figure.

---

## Global Continuity Rules

Use this section for page-wide continuity that is easy for image models to drop:

- Returning character traits
- Wardrobe details that must remain visible
- Object continuity across panels
- Environment continuity
- Time-of-day progression
- Relative height or placement that repeats across panels
- Exact caption reproduction

Example:

```markdown
Global continuity rules

* Keep Mike clean-shaven.
* Mike's brown suede jacket must read clearly.
* The page should feel like one continuous place and one continuous day progressing toward sunset.
* Object counts that must stay consistent:
  - Panel 1: honey jars on the yoke
  - Panel 2: honey jars on the table
* Caption text must be reproduced exactly.
```

---

## DO NOT List

Use `DO NOT` for hard negatives only. These should be model-failure preventers, not style preferences.

Standard items:

```markdown
DO NOT

* Do not redesign the layout
* Do not change the panel arrangement
* Do not add extra unnamed characters
* Do not lose or paraphrase the captions
```

Add page-specific negatives only when there is a real risk, such as `Do not overfeature the car`.

---

## Lessons From Literal Honey

The honey page works because every panel has a distinct compositional job:

- Panel 1: arrival and welcome, wide establishing shot, Billy centered through the honey-yoke action.
- Panel 2: transaction and moral cooling, medium shot, key-pass centered, honey jars moved into foreground as continuity and meaning.
- Panel 3: reflective departure, medium-wide low angle, Billy and Mike from behind with the sunset centered between them.

The prompt tracks object continuity without overexplaining it:

- Honey starts as Billy's carried gift.
- Honey becomes foreground evidence of exchange.
- The road and sunset then shift the page from action into reflection.

The captions are exact text, with position only when composition needs it.

The panel constraints are short because they target likely failures:

- Billy must stay visual center in Panel 1.
- Women must feel distinct, not duplicated filler.
- The car must not overpower the key-pass in Panel 2.
- Billy and Mike's relative scale and positions must hold in Panel 3.

This is the balance to preserve on future pages.
