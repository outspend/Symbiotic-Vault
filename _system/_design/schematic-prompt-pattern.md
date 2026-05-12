---
type: design
created: 2026-05-07
status: active
project: scroggins-manson
canonical-example: [[_trace/scroggins-manson/pages/literal-honey-schematic-claude-code]]
test-corpus: _trace/_assets/schematic_page_4/
---

# Schematic prompt — build-up and pick pattern

A working pattern, not a skill. The agent (Claude Code) drives this conversationally; this doc is what gets re-read on a cold session so the user doesn't have to re-explain the workflow.

The aim: turn a script page into a comic page rendered by ChatGPT's image model, while preserving room for the model's implicit talents to surprise the user.

---

## Operating principle: freedom within bounds

The schematic prompt is **deliberately not maximally specific**. It is precise about two distinct things:

- **What we know** — load-bearing facts (Mike's brown suede jacket; four jars on the table; Chuck-and-Landlady locked eye contact). Encoded firmly.
- **What should remain a field of possibility** — zones where the model is invited to explore (the specific blocking of the women welcoming Billy; gestures, expressions, exact composition). Bounded but left open: *what the field is, not what the answer is*.

This is film-production logic. Variations are **takes**. The user picks the **circle take** — the hero panel for that slot. The model's takes can spark creative directions the user didn't know to specify; that's the point of leaving fields open.

Tightening happens **reactively**: only when picks across takes can't be reconciled into a coherent page do we go back and nail more down — and only as much as the schematic prompt can hold without collapsing the fields.

---

## Vocabulary

- **Schematic prompt** — the text-only page spec we send to ChatGPT (Header → Bible → Setting → per-panel blocks → Global continuity → DO NOT → Final).
- **Take** — one full-page gen. Notation: `g1`, `g2`, …, `gN`.
- **Panel** — a panel within a take. Notation: `p1`, `p2`, `p3` (page-level panel count, e.g., 3 for current pages).
- **Pick / Circle take / Hero panel** — interchangeable. The user's chosen take for a given panel slot. Notation: `gN.pM`, optionally with a "why" note.
- **Field of possibility** — a deliberately open zone in the schematic prompt where the model is given creative latitude within stated bounds.
- **Stitch** — a single composite image of the hero panels assembled into the page's panel layout. Serves as both the communication checkpoint with the user and the visual reference image fed back to ChatGPT for reconciliation.
- **Reconciliation** — the second-pass render where ChatGPT generates a unified page that honors the stitched hero panels.
- **Shading prompt** — composition-lock prompt that reduces a good gen to a flat-shape map (silhouettes, flat color zones, captions preserved, no detail). Re-iterate from those bones when composition is right but style or detail needs to change.
- **Style-transform prompt** — re-renders a finished page in a new style while preserving layout, captions, characters, staging, beats. The serendipity / exploration tool, not the intentional path to a styled page.

---

## Lifecycle

```
Script page
  → Stage A.1: agent drafts schematic prompt — precise about what we know,
               fields of possibility named where open
  → Stage B:   takes → picks (gN.pM) → stitch → reconciliation
  → Reconciliation works? Schematic prompt is stable. Page is done.
  → Reconciliation fails? Stage A.2: tighten where it broke,
               only as much as the prompt can hold. Re-do Stage B.
```

A and B aren't a linear handoff. They're a feedback loop. Stage A produces the prompt; Stage B exercises it; reconciliation outcomes either close the loop or send us back to A.

---

## Stage A — Script → Schematic prompt

### A.1 — First draft from script

User hands the agent a script page (per-panel narrative + captions/dialogue, the form already in the middle section of `literal-honey-schematic-claude-code.md` under "Comic script — authored source").

Agent produces a first-draft schematic prompt with these blocks:

- **Character Bible** — pulled from script + carried over from the project's existing bible. New characters get added; returning characters reuse existing entries.
- **Setting** — pulled from script; carryover within a comic.
- **Per-panel blocks** — for each panel: Framing, Visual center, Beat, Captions, Eyelines, Contents, Constraints. Encode firmly what the script declares as load-bearing. Where the script is silent or the answer should come from the model's exploration, name the **field of possibility** — what kind of variation is welcome, with bounds — rather than inventing specificity.

  *Example field-of-possibility line:* "PANEL 1 — gestures of welcoming women: distinct figures, varied gestures of welcome, eyelines on Billy" — bounded but open.

- **Global continuity rules** — anything the script implies (object counts that must hold, character continuity, mood arc).
- **DO NOT list** — standard guardrails (no production-sheet elements, no unnamed characters, captions reproduced exactly) plus anything the script implies negatively.
- **Header / Final instruction** — boilerplate, no SVG-schematic references.

The principle (lifted from the schematic working notes, rule 10): **encode only what's earned**. Generic atmosphere, default mountains, ambient sky stay out unless the script names them. Where the answer isn't known yet, the schematic prompt is precise about *that* too — naming the field, not pretending to fill it.

If the agent is uncertain whether something is load-bearing or a field, ask. The line between "we know this" and "this should stay open" isn't always obvious from a script alone.

### A.2 — Tighten only on reconciliation failure

A.1 produces a draft. We don't iterate on the draft in isolation by guessing. We exercise it through Stage B and listen.

When Stage B reconciliation succeeds — picks across takes can be stitched and re-prompted into a coherent unified page — the schematic prompt is stable. Done.

When reconciliation fails — picks too divergent to stitch coherently, or the reconciliation re-prompt produces a page that loses what the picks had — that names a place where the schematic prompt was too loose. Tighten there, and only there:

- Agent proposes a minimal addition to the affected panel block (a constraint, a content line, an eyeline note) that closes the gap *without* eliminating the field of possibility. User approves or counters.
- Re-run Stage B with the tightened prompt.
- If the schematic prompt structurally can't carry what's needed, note it for resolution outside the prompt — manual fixing or a different tool — rather than overspecifying.

The bar isn't "no drift." It's "picks reconcile."

---

## Stage B — Schematic prompt → Final page

### B.1 — Take set

User runs the schematic prompt through ChatGPT 4–10 times and drops the gens where the agent can see them (folder or conversation). Each gen gets `g1`…`gN`. Panels within a gen are `p1`, `p2`, `p3`.

Agent produces a quick labeled overview so the shorthand has a referent.

### B.2 — Circle takes

User points at picks in `gN.pM` shorthand, with optional why:

```
g3.p1 — Billy's yoke reads, women feel distinct not duplicated
g7.p2 — Chuck-and-landlady eye contact lands; honey jars right count
g4.p3 — sunset pitch is the warmest of the ten
```

Agent keeps the canonical record verbatim. The why is the user's hook for **decomposition to prompt** — if the reference image route stalls, the why notes drive a rewrite of the affected PANEL block.

### B.3 — Rough stitch (handshake + reference)

Agent produces one stitched image: hero panels assembled into the page's panel layout. Crops from each take, pasted into a single page-shaped composite. Style drift, mismatched lighting, ragged seams expected and fine.

Two purposes from one artifact:

- **Communication checkpoint.** User confirms we're talking about the same panels. Mis-pick gets corrected here before burning a re-prompt iteration.
- **Reference image for B.4.** Once confirmed, the stitch goes to GPT as the visual reference for reconciliation — one image, not N panel cutouts.

Tooling: ImageMagick / Pillow via Bash. Crop math comes from the panel layout the schematic prompt declares.

### B.4 — Reconciliation re-prompt

Agent produces a revised schematic prompt asking GPT to render a fresh unified page using the stitched hero panels as visual reference:

- Header / Bible / Setting / per-panel blocks / Global continuity / DO NOT — preserved unless a "why" note calls for a minimal text edit on a specific PANEL block (in which case agent proposes the edit, user approves)
- Updated reference-image instruction in the Header: the stitched winners image is the source of truth for staging, composition, character positions, panel beats; GPT should reconcile style and continuity across the page so it reads as one render rather than a stitched seam-show
- Optionally: a **style anchor image** the user supplies (separate from the winners stitch) when ready to lock visual style

User pastes the revised schematic prompt into ChatGPT with the stitched image attached.

If reconciliation lands → schematic prompt is stable; page is done.
If reconciliation fails → back to Stage A.2.

---

## Core guardrails

- **No SVG schematic to GPT.** The schematic prompt is text only.
- **Encode what we know AND name fields of possibility — both with precision.** Don't invent specificity beyond what the script earns.
- **Tighten only when picks can't be reconciled, only where they couldn't, and only as much as the prompt can hold without losing the field.**
- **Picks via `gN.pM`. One stitched hero-panels image as reference, not N cutouts.**

---

## Composition-lock — shading prompt

When a gen has the right composition but iteration is causing style or detail drift (e.g., re-running for style variants or asking GPT to adjust details on a near-final), the **shading prompt** locks composition by reducing the good gen to a flat-shape composition map.

Form: minimal instruction listing what to keep (panel borders, yellow caption boxes with text, solid silhouette shapes for characters in shades of grey, flat color shapes for sky / land / foliage / vehicles / props) and what to remove (facial features, clothing detail, texture, lighting, internal outlines, shadows). Every panel area filled by simple flat shapes; result reads as a clean color-coded composition map, not finished comic art.

This is a **separate mode** from the schematic prompt (page generation) and the reconciliation re-prompt (picks → unified page). The shading prompt sits alongside; the user invokes it during iteration when composition is right but other aspects need to change. The composition map then becomes the reference for the next iteration, holding the bones while letting style or detail vary.

**Four workflow artifacts**, with different roles in the pipeline:

| Artifact | When | What style is doing | Style direction in prompt? |
|---|---|---|---|
| **Schematic prompt** (with style) | Stage A — generates variants from script | Defined (or left open as field) | **Yes** — canonical place for style direction |
| **Reconciliation re-prompt** | Stage B — assembles picks into unified page | Preserved (honor the picks) | **No** — would override the picks |
| **Shading prompt** | Anytime — composition lock during iteration | Eliminated (composition only) | n/a |
| **Style-transform prompt** | Optional — re-render finished page in new style | Changed (the purpose) | **Yes** — but this is serendipity / exploration, not the intentional path |

**Pipeline-position principle.** The intentional path puts style choices **upstream of picks**: choose style direction → schematic prompt with style → 12 variants → pick → reconcile. Style-transform downstream is a serendipity tool ("what if this were pulp?") or recovery move ("keep this composition, change the style"). When working intentionally, style decisions happen *before* falling in love with any specific panel — once you've picked, you've committed to that style, and transforming away from it is fighting your own decision.

Canonical examples (this session):

- **Schematic prompt with style direction** — the cleaned variant in `_trace/scroggins-manson/pages/literal-honey.canvas` (node `cb6170e82ca546b2`), with a `STYLE DIRECTION` block at the top (golden age pulp) and `Image A` reframed as the shading layout image
- **Reconciliation prompt** — `literal-honey-prompt.md` (no style block; honors picks)
- **Shading prompt** — `_trace/scroggins-manson/pages/output/shading prompt.md`
- **Style-transform prompt** — `literal-honey-style-pulp.md` (validated by Scroggins, 2026-05-08)

---

## Maintenance task: purge schematic remnants

The current schematic prompt in `literal-honey-schematic-claude-code.md` (lower half) was written while the SVG schematic was still being fed. It still references "Image A," "the schematic," "schematic markings." Since the SVG isn't being attached anymore, those references are stale and risk confusing the model.

A small, separate pass:

1. Take the current lower-half template, draft a purged version with all schematic / Image-A references removed
2. User test-gens the purged version against ChatGPT, fresh
3. Compare against gens from the un-purged version on the same page
4. If renders are the same or better, lock the purged version as the canonical schematic-prompt template

Do this on its own, on literal-honey, before fully exercising Stage B with the purged template. The existing 12 takes at `_trace/_assets/schematic_page_4/` were produced from the un-purged template; they can still exercise Stage B mechanics, but the renders from the purged template will be the real target.

---

## Open, to figure out by doing

Live questions, not pretended answers. Future-me: read these as flags that we still don't know, not gaps to fill on first principles.

- **Where the bible lives across pages.** Currently embedded per page in the schematic prompt. Eventually probably wants to live once per project and be referenced. Decide when redundancy starts costing more than it earns.
- **Calibrating fields of possibility.** First time through I'll likely err — either too tight (specifying what should be open) or too loose (leaving load-bearing things to chance). User will correct; calibration is by feel, by page.
- **Reconciliation failure modes.** "Picks can't be reconciled" can mean several things — too much style drift between takes, takes inconsistent on character/object continuity, the page layout itself stops cohering. We'll learn which failures call for which kind of tightening.
- **Crop precision** for the stitch: panel borders in real gens aren't always crisp. First time through, crop generously; user will tell me if the slop is acceptable for the handshake. Tighter cropping later if needed.
- **How well GPT honors the stitched reference.** Unknown until we run one. If reconciliation gens drift away from picks despite the reference, the user's "why" notes become the decomposition path — rewrite the affected PANEL block(s) based on what they said worked.
- **Style anchor image.** What it should be (a single representative gen? a curated style still? the user's own line work?). Decide when style needs to lock on a particular page.
- **What the schematic prompt structurally can't hold.** Some things may not be tightenable in prompt-space. Note them when we hit them — they become candidates for manual fixing or a different tool, not for prompt overspecification.
- **Purge pass timing.** Do the schematic-remnant purge on literal-honey before fully exercising Stage B with the purged template.
- **Whether to formalize as a skill.** Deferred. Run conversationally a few times first; if the shape proves stable, lift into `_system/_skills/`.

---

## Critical files

- `_trace/scroggins-manson/pages/literal-honey-schematic-claude-code.md` — canonical schematic-prompt example. The **lower half** (from "My edit that ive had good luck with" onward) is the form. Working notes / SVG / earlier "page packet" sections above it are historical.
- `_trace/_assets/schematic_page_4/1.png` … `12.png` — 12 takes of literal-honey, the test corpus for exercising Stage B mechanics (`g1`–`g12`).
