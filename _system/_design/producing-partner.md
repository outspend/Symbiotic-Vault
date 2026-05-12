---
type: design
created: 2026-05-07
status: active
related: [[_system/_design/schematic-prompt-pattern]]
---

# Producing partner — how I keep you moving through the work

A companion doc to the schematic-prompt pattern. The pattern doc says *what* the workflow is. This doc says *how I drive you through it* — the producing role.

The user's ask, in their words: *"i get distracted and i need you to produce me through this so i don't get lost."*

---

## The role

I'm the producer. You're the director. You make the calls; I keep the production moving.

That means:

- **Orient before every step.** Before we move, I name where we are, what we're about to do, and what the next decision is. Short — a sentence or two. Never assume you remember the state from however long ago.
- **Surface the live choices, with one-line tradeoffs.** When there's more than one viable next move, I name them and ask which — instead of picking silently or asking open-ended "what do you want to do?" Never more than 2–3 options.
- **Name what's about to happen.** Before I run a tool or produce an artifact, one sentence: "going to crop the panels and tile them as a 3-up stitch." Lets you redirect cheaply.
- **Hold the line on the test corpus.** The folder we're testing against, the canonical example, the page in question — I carry these in my head so you don't have to repoint me.
- **End-of-session note.** If we have to stop mid-run, before you go I write a short "where we left off" — what's done, what's the next move, what artifacts are sitting around. So next session opens with orientation, not archaeology.

I don't produce you through the *creative* calls. Those are yours — what to draft, what to circle, when reconciliation lands. I produce you through the *workflow* — the next step, the next artifact, the next decision point.

## Director-into-editorial mode

Your framing, 2026-05-07: *"a schematic prompt locks the story beats that work while letting the model breathe with regards to certain aspects — that's the film production idea. but film directors get to take their work into editorial and lock things down. so we really need to see that work to justify the fun here."*

Two modes, then:

- **Production** (Stage A drafting + Stage B taking and picking): protect the breathing room. Don't let me overspecify. Variations are takes; we're letting the model contribute. I move us through, but I don't pressure you to lock things down prematurely.

- **Editorial** (reconciliation, purge, cleanup, deliverable): now we're locking. I get precise, push toward the page being done, don't let edits drift. If reconciliation needs another pass, I name that clearly rather than soft-pedal.

The transition between modes is always your call ("ready to chase variants" / "ready to lock"). I don't guess at it — but I keep us moving within whichever mode we're in.

---

## Where we are right now

- **Bootstrap done** — pattern doc, memory pointer, builders notes entry written 2026-05-07.
- **Test corpus** — 12 takes of literal-honey at `_trace/_assets/schematic_page_4/1.png` … `12.png`. These are `g1`–`g12`. Produced from the un-purged schematic prompt.
- **Page** — literal-honey, page 4 of 6 in scroggins-manson. 3 panels: full-width Billy-with-yoke / bottom-left Chuck-Landlady key pass / bottom-right Billy-and-Mike walking away at sunset.
- **Mode** — about to enter Stage B production for the first time.

## Live choice — what we run first

Two viable starts. Quick tradeoffs:

1. **Stage B exercise on the existing 12 takes.** Tests the pick-and-stitch mechanics on real material. Gens were produced from the un-purged template — fine for exercising the workflow, not the renders we'd ultimately settle on. Output: a labeled overview, your picks, a stitch you confirm or correct, a reconciliation re-prompt. *Higher learning value, more involved.*

2. **Purge pass on the literal-honey schematic prompt first.** Small isolated edit — draft a de-Image-A'd version of the lower-half template. You test-gen it against ChatGPT, compare to the existing 12, lock the cleaner version as canonical. *Smaller, gets the canonical template clean before we exercise it.*

Either order works. If you want the editorial test first (purge), the Stage B run after is on cleaner ground. If you want to learn the Stage B mechanics now, the existing 12 takes are sufficient and the purge can follow.

---

## How a Stage B run goes (so you can see the shape from here)

1. I produce a **labeled overview** of the 12 takes — a quick contact sheet (or a list with thumbnails if the conversation can carry images) keyed to `g1`–`g12`, panels indexed `p1`–`p3`.
2. You give **circle takes** in `gN.pM` shorthand, with whatever why notes you want to hand me. Cherry-pick across all 12.
3. I produce the **rough stitch** — three crops assembled into the page layout. You eyeball it. If a pick is wrong, we fix it here.
4. Once confirmed, I produce the **revised schematic prompt** + tell you exactly what to paste into ChatGPT and what image to attach.
5. You run reconciliation; we look at what comes back together. Lands → we have a page draft. Drifts → I propose tightening only where it broke.

I orient at every transition. You stay in the director's chair.

---

## Hitches and reminders (running log)

Things to watch for, anticipate, or fix on the next pass. Add to as we go.

### Pixel-verify panel boundaries — never eyeball

**This was a recurring failure mode** during the literal-honey first run (2026-05-07). I eyeballed g3's bottom-row split as x≈920 and g11's p3 left edge as x≈947 from small inline preview images. Both estimates were wrong by ~180px. I built v3, v5, v6, v7 stitches on those wrong numbers and the user kept seeing fragment captions and what looked like a third panel. Pixel detection finally showed the truth: gutter at x=760-772, p3 starts at x=772, caption box at x=789. v8 was the first clean stitch.

**Inline preview images compress 1536px sources to ~600px renders. Each preview pixel is ~2.5 source pixels. Visual eyeballing of panel boundaries from preview is not reliable** — errors of 100+ pixels are easy to miss and show up later as visible artifacts.

**Verification step before any stitch assembly:**

1. **Extract diagnostic strips** of each pick's source gen (e.g., `g3.crop((0, 540, 1536, 1024))` for the bottom row) and save as `_diag-<gen>-bottom.png`. View directly.
2. **Pixel-detect panel boundaries.** Sample a horizontal brightness or color profile at a y-row known to cross the gutter, looking for the bright (white/light) gutter band between dark panel content. For caption box edges, sample at a y inside the caption and detect the caption color signature.
3. **Print the detected boundaries** before assembling. Confirm they're sensible and consistent across gens before cropping.

If pixel detection finds different boundaries across gens (e.g., one gen splits at x=760, another at x=947), respect each gen's actual boundaries when cropping FROM that gen — don't assume a uniform layout.

A user flag like "X is cut off" or "this looks like another panel" is almost always a boundary error. Re-verify pixel boundaries before adjusting anything else.

### Cropping the overview / building the stitch

- **Different gens can land in different layouts entirely.** First Stage B run, 2026-05-07: `g9` came back as three stacked full-width panels instead of the canonical full-width-top + bottom-left + bottom-right. The schematic prompt's layout instruction is a soft constraint; the model drifts. Implication: when picking, don't assume the same panel slot exists in every gen. Flag layout-drift gens explicitly. If reconciliation fails on layout grounds, that's a Stage A.2 tightening signal.

- **Per-gen panel-boundary variance, even within the canonical layout.** Bottom-panel split ranged from x≈920 (g3) to x≈947 (g11) in the same set — ~30px swing. Uniform crop boxes for the overview sheet are fine for browsing, but **the stitch needs per-pick tight crops based on each gen's actual panel boundaries** or the seam shows badly.

- **Crop generously on the overview sheet.** First pass I cropped p2 at x=615; actual right edge was ~920 and the Landlady was outside my crop. User saw an apparent cutoff that wasn't in the gen — only in my crop. Default generous; verify per-gen if a pick flags a cutoff.

- **A "you cut off X" flag can be about my crop, not the gen.** Catch this distinction before re-prompting GPT or chasing fixes that aren't needed. If the user names a missing element on review, first check whether my overview crop excluded it. If so, redo the crop and re-show before treating it as a content gap.

### Where the gulf goes (signal to GPT)

- **Place empty fill-space INSIDE the affected panel's bordered region**, not at the bottom of the canvas. v3 had the empty space at the canvas bottom (below the bottom row) — that reads as "page is shorter than the canvas" rather than "panel needs to extend." v5 draws a black border around the panel's full canonical extent and leaves the unused portion empty inside that border. GPT sees "this is panel 1's full extent; the picked content occupies the top; fill the bottom." Different and stronger signal.
- **Only draw the slot border on panels that have a gulf.** Panels that fill their canonical positions at native size don't need extra borders — their own gen borders already do the work, and adding our border alongside creates double-line confusion.

### Cropping tradeoffs

- **Generous crops capture full captions and panel content; tight crops avoid double borders but risk clipping.** Captions sit just inside the panel border; an aggressive crop inset (e.g., y=551, v4) can clip the top of a caption. The fix: use **asymmetric inside-border crops** — generous on the side where captions sit (y=540–543 for panels with top-aligned captions) and tight on the sides without content (x inset 8px to exclude gen's left/right borders, y inset 6–8px at bottom). Then draw a single canvas border around each canonical slot. v6 lands this: captions intact, no double-border seam.

- **No text labels on the stitch.** GPT's image model renders visible text literally, so labels like "EXTEND PANEL 1" or "GULF" would appear in the final render. Keep instructional language in the prompt text; let the visual cues (bordered slot + empty region) do the work in the image.

### Verbalizing pick qualities as text constraints (when needed)

Most picks should ride into reconciliation via the stitch image — that's the image path's purpose. But occasionally a pick's "why" note is worth promoting into the prompt as text, e.g., when reconciliation drifts away from the picks despite the reference, or when a quality is factual enough that text reinforces image without conflict. **Only verbalize qualities that translate to text:**

| Why note kind | Example | Treatment |
|---|---|---|
| Factual | "dirt road not paved", "slight-angle vanishing point", "exactly four jars" | Add as bare-fact constraint, one line, no reasoning |
| Already in bible / general constraints | "Charlie reads as magnetic" (bible already says this) | Don't add — repetition is noise |
| Imagery-specific | "the way trees and sky stage around figures in this gen", "Charlie's specific expression and acting" | Don't add — text can't reach this; image path required |
| Field of possibility | "women can vary, distinct figures with eyelines on Billy" | Already in original constraints (or add if missing); don't promote to a "Hero" frame |

If most of a page's hero qualities are imagery-specific, text additions are structurally weaker than the image path. The image path exists for exactly those.

### Parsimony in the prompt body

When adding *anything* to the prompt body — constraints, hero qualities, continuity notes — the rule is **state, don't sell**. The model takes a fact better than a fact-with-reasoning. "Road surface is dirt, not paved" beats "Road surface is dirt — dirt carries the rural, era-appropriate feeling and paved road flattens it." The reasoning lives in our notes between us; the prompt is for the model.

Symptom that I've drifted from this: the constraint is more than one short sentence, contains a "because" or em-dash explanation, or repeats something from the bible. Strip it back.

### What GPT honors literally from the stitch

Discovery from the literal-honey first reconciliation gen (2026-05-07): GPT treats the stitch as a literal page template more strictly than expected. **Gutter widths in the stitch become gutter widths in the final render.** Implication: gutters in the stitch must be uniform (12px throughout, not 12px in one place and 15px in another), or the final page will inherit the inconsistency.

**Captions are NOT auto-reconciled.** When a stitch carries picks from multiple gens, each pick has its own slightly different handwritten lettering style and yellow tone. GPT preserves those differences in the final render rather than homogenizing them. Implication: the reconciliation prompt must explicitly call for caption consolidation — single consistent handwritten style, single consistent yellow tone, unified across all panels. Without that line, captions look multi-author.

The general principle: anything that is *visibly inconsistent* in the stitch carries through unless the prompt explicitly asks for unification. Stitch precision and prompt-level reconciliation instructions are complementary, not redundant.

### Eventual tooling — canonical-layout stitch composer

When we build the helper script (deferred until the workflow proves out across more pages), its scope is **the whole layout grid as one geometric system**, not just boundary detection. Responsibilities:

- **Source detection**: pixel-detect where each pick's panel content begins and ends in its source gen (gutters, panel borders, caption-box positions where relevant)
- **Canonical grid spec**: a small config — `page_margin`, `gutter`, panel slot dimensions for the page's layout (1+2, 2+2, 3+3, etc.). Page-edge margins are part of the grid, not an afterthought.
- **Composition**: crop picks at detected boundaries, place into canonical slots, draw slot borders where needed (e.g., the gulf marker), generate the stitch image

Output: a stitch where every gutter — between panels AND from each panel to the page edge — is uniform and explicit. No tenuous edges, no asymmetric gutters, no eyeballed boundaries. Discovered geometric issue from the literal-honey first run (2026-05-07): GPT's reconciliation render preserved page-edge tenuousness from the stitch as well. Same fix as inter-panel gutters: explicit and uniform.

The script earns its keep when we're stitching pages regularly and the manual procedure (extract diagnostic strips, pixel-detect boundaries, hand-place panels) becomes a tax. Until then: manual procedure, with the producing-partner-doc verification step.

### Stitch as handshake

- **Resize-into-canonical-layout introduces small geometry distortion** when the source panel and the canonical slot have different aspect ratios. Acceptable for a rough stitch (a few percent stretch). If it gets visibly bad, an alternative is to keep source aspect and let the stitch canvas adjust — but then the stitch no longer matches the page architecture, which weakens its value as the GPT reference image. Default: resize-into-canonical, accept small slop.

- **Seam softness at panel boundaries.** When the per-pick crops don't pixel-align with the canonical layout slots, the seam shows (slight content bleed, captions clipping). For the handshake function this is fine. For the reference-image function, see whether GPT honors the picks or gets confused by the seams; if it gets confused, draw clean black gutters on the stitch before sending.

---

## Reuse beyond this test

This producing role applies to any multi-step creative workflow we run together — not just schematic-prompt work. The five behaviors at the top (orient, surface, name, hold, end-note) travel. If we end up using this pattern on a different project, this doc is what I re-read before we start.
