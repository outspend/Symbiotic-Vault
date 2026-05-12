---
type: style-transform-prompt
project: scroggins-manson
page: literal-honey
style: golden-age-pulp
status: validated
created: 2026-05-08
related:
  - "[[literal-honey-prompt-conform]]"
  - "[[_system/_design/schematic-prompt-pattern]]"
note: Validated 2026-05-08. Re-renders a finished page in a new style. Use as exploration ("what if this were pulp?") or recovery ("keep this composition, change the style"). NOT the intentional path to a styled page — for that, choose style upstream via the schematic-with-style variant before the 12 gens. This artifact is the serendipity tool.
---

# Literal Honey — style-transform prompt (golden age pulp)

Validated by Scroggins on WhatsApp 2026-05-08. Takes a finished page (e.g., a reconciliation output) and re-renders it in a new style, preserving layout, captions, characters, staging, and beats.

**Where this fits in the pipeline:** the intentional path puts style choices upstream of picks — schematic-with-style variants → 12 gens in chosen style → pick → reconcile. This style-transform prompt operates *after* the fact on a finished page. Useful for exploration or recovery, not for the canonical styled-page route.

**To use:** paste from `## Render prompt` through to the end of the file into ChatGPT and attach the finished page as the reference image.

---

## Render prompt

> Render the attached comic page in a new style. The attached image is the source of truth for layout, panel arrangement, character positions, staging, beats, eyelines, captions (exact text and position), and object counts. Change only the rendering style.
>
> **Style — golden age pulp:**
>
> - Blocks of color
> - Newsprint feel
> - Simple readable shapes
> - Bold reduced detail
> - No painterly gradients, no realistic lighting, no photographic depth, no dense crosshatching
>
> **Preserve exactly from the attached image:**
>
> - Page shape: 3:2 landscape, exactly 3 panels (1 full-width top + 2 bottom)
> - Panel borders, gutter positions, relative panel sizes
> - Caption boxes: positions, exact text, slightly yellow tone
> - Character likenesses (see bible below)
> - Staging, eyelines, beats, object counts
> - Same environment across all three panels (Topanga Canyon commune, day → sunset arc)
>
> **General page rules:**
>
> - Output one finished three-panel comic page.
> - Panels fill the canvas with only normal comic gutters; no extra edge whitespace.
> - Page visually unified.

---

## Character bible — preserve likeness across the style change

**BILLY** — tall, friendly/gregarious. Long curly blond hair past shoulders. Full beard. Open fringed leather vest with tooled patterns, no shirt under. Beaded necklaces. Denim cutoffs, mid-thigh, frayed hem. Cowboy boots.

**MIKE** — average height, narrator. Dark brown shaggy short hair. Clean-shaven. Brown suede lambskin jacket, unzipped, over plain cream t-shirt. Straight-leg jeans. Brown leather boots.

**CHUCK** — short and skinny, Charles Manson likeness: intense, dark-eyed, magnetic. Shoulder-length dark hair. Trimmed full dark beard. White button-up shirt, open at collar. Dark brown pants.

**LANDLADY** — older woman, 60s, stern. Gray hair pinned in a loose bun. Long-sleeved purple-and-floral print dress. Simple gold necklace and earrings.

**COMMUNE WOMEN** — adult women, varying heights. Long loose hair in mixed colors. Patchwork hippie dresses in light yellow / light blue / earthy tones. Bare feet or sandals.

## Continuity to preserve

- Billy's clothing consistent across his appearances
- Mike clean-shaven; his brown suede jacket reads clearly
- Chuck reads as intense, magnetic, Manson-like
- One continuous place, one continuous day progressing toward sunset
- Object counts match the source image exactly: honey jars on the yoke (Panel 1); honey jars on the table (Panel 2)
- Caption text reproduced exactly; caption box positions match the source

## DO NOT

- Do not redesign the layout or change the panel arrangement
- Do not lose or paraphrase captions
- Do not add unnamed characters
- Do not add motion lines, sparkles, exclamation effects, or blur unless the source has them
- Do not add sidebars, keys, panel numbers, or production-sheet elements
- Do not return painterly gradients, realistic lighting, or photographic detail — this is a style transform *away* from those

## Final instruction

Output only the finished comic page in golden age pulp style, with all other elements preserved from the attached image.
