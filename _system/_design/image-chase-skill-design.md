---
type: design
created: 2026-04-29
revised: 2026-04-29
status: proposal
implements: image-chase skill
related-design: [[_system/_design/comic-trace-skill-design]]
context: [[_trace/_notes/2026-04-29-canvas-read-exchange]]
api-target: gpt-image-2 (released 2026-04-21)
---

# Image-chase skill — design + implementation brief

A vault skill that handles image-iteration loop work for comic-panel generation. Built against OpenAI's `gpt-image-2` API. Designed for the alternation pattern named on the Scroggins/Manson provenance canvas: **the agent does the iteration; the human comes in when there's signal worth deciding on.**

This document is self-contained. An implementer should be able to pick up the work cold from this brief plus an OpenAI API key with org verification.

Companion design: `_system/_design/comic-trace-skill-design.md`. This skill emits sub-canvases conforming to comic-trace's schema; comic-trace links them onto the main provenance canvas.

---

## Why this exists

The Scroggins provenance canvas (`_trace/2026-04-22-scroggins-manson-comic-provenance.canvas`) records a recurring class of pain around image generation:

- *"i wish i could have handed this to a 'helper' agent or process to chase the fix... it didn't feel like a creative chase, it felt compulsive"*
- *"CC and the vault could iterate and permute here for me via api rather than me waiting in the chat gpt interface"*
- *"agentic intermediary helping with the babysitting... but i would also want to see the many failures as they are sometimes serendipitous"*
- *"fight for stylistic consistency concerns (caption color, keeping the art flat/pop without too much texture)"*

The first-order pain is **mid-iteration cleanup**: the user has done creative work, has multiple drafts on hand, and is stuck doing finicky panel-level surgery — fighting for a likeness, harvesting panels from different versions, fixing eyelines, anchoring style, fitting between neighbor pages. That's where time is bleeding.

This skill addresses that pain in Phase 1, with the broader spread/study/bake/style-lock work in Phase 2 — needed soon (the user's next comic is days away, not weeks).

It does **not** address: drag-panels-as-notecards, animated-gif iteration playback (interface-layer wishes, separate problem).

---

## Phase split

### Phase 1 (build first — "fix")

- **`/image-chase fix`** — the request-blast capability. Surgical panel iteration against multi-constraint requests. Conversational scoring (the agent and user evaluate gens together, no in-loop vision rubric). Loop autonomy via Claude Code's `/loop` primitive with surface-on-signal heuristics. Calls into comic-trace at run start, every meaningful event during the run, and at run end — sub-canvas grows live like a chat history.

### Phase 2 (build close behind — workflow for the *next* comic)

- **`/image-chase spread`** — N variants with explicit prompt-level variation; exploration before commitment
- **`/image-chase study`** — character/expression contact sheet; performance audition for a single character
- **`/image-chase bake`** — final high-quality regeneration once a draft is picked
- **`/image-chase style-lock`** — manage the style bible (set, update, audit drift)

The foundation (`api.py`, `manifest.py`, decision log, surface policy, iteration-directory format) is shared across all phases, so Phase 1 work substrates Phase 2.

### Dependency on comic-trace

image-chase **does not write canvases.** It produces well-formed iteration directories and calls into comic-trace's `compose-sub-canvas` and `link-sub` at run events. Sequencing across the two skills:

1. **comic-trace Phase 1** (`init`, `capture`, `annotate`) — ships first, no API needed
2. **comic-trace Phase 2** (`compose-sub-canvas` with init/append/finalize modes, `link-sub` with status flag) — adds the sub-canvas integration
3. **image-chase Phase 1** (`fix`) — depends on comic-trace Phase 2 being available
4. **image-chase Phase 2** (spread/study/bake/style-lock) — builds on the same foundation

comic-trace Phase 1 + 2 is plausibly one focused implementation session since neither needs API access. image-chase follows when API access lands.

---

## API target: gpt-image-2

Released 2026-04-21. Snapshot ID `gpt-image-2-2026-04-21`.

**Endpoints used:**
- `POST /v1/images/generations` — text-to-image, no refs
- `POST /v1/images/edits` — text + up to **16 reference images**; the workhorse for `fix`

**Key parameters:**

| Parameter | Used for |
|---|---|
| `model` | `"gpt-image-2"` |
| `prompt` | Composed by the agent from request-blast + manifest + refs |
| `image[]` | Reference images (bible + characters + neighbor pages + draft harvests), max 16 |
| `n` | Batch size per call (typically 3-4 for `fix`) |
| `size` | `"1024x1024"` for drafts, larger for `bake` |
| `quality` | `"low"` for fix iteration, `"high"` for bake |
| `response_format` | `"b64_json"` (URLs expire) |
| `partial_images` | 0-3, optional streaming preview during long calls |
| `moderation` | `"low"` |

**Notably absent:** `input_fidelity`. gpt-image-2 processes every reference at high fidelity automatically. Edit-mode cost scales with reference count — budget tracking must include input image tokens.

**Cost shape (1024×1024):** low ≈ $0.006/image, medium ≈ $0.053, high ≈ $0.211. Plus input image tokens at ~$0.002–0.004 per ref. v1 budget defaults:

- `fix` batch (low, n=4): ~$0.05 plus refs ≈ $0.10/batch
- `fix` total run (8 batches, ~32 gens): ~$0.80
- `bake` (high, n=3): ~$1.00

**Rate limits:** Tier 1 = 5 IPM; tier 4-5 = 150-250 IPM. Implementation is tier-aware (config knob) and backs off on 429s.

**Latency:** Up to ~2 min per high-quality image. Loops run as background tasks via Claude Code's `/loop` primitive; the skill does not block the chat window.

---

## Vault layout

```
_system/_skills/image-chase/
  SKILL.md                   # entry point; routes /image-chase to sub-commands
  fix.md                     # phase 1
  spread.md                  # phase 2
  study.md                   # phase 2
  bake.md                    # phase 2
  style-lock.md              # phase 2
  _shared/
    manifest-format.md       # comic-level reference manifest
    request-blast-format.md  # how to write a fix request
    sub-canvas-format.md     # conforms to comic-trace schema
    decision-log.md          # craft adaptations vs. guardrail stops
    surface-policy.md        # when the loop interrupts vs. continues quietly
    cost-and-budget.md       # dual cap (n + USD), tier-aware rate handling

_system/_tools/image-chase/
  fix.py                     # phase 1
  spread.py  study.py  bake.py  style_lock.py    # phase 2
  lib/
    api.py                   # OpenAI client wrapper, retries, cost tracker
    manifest.py              # bible/character/neighbor-page ref loading
    request_blast.py         # parse request-blast markdown into a structured plan
    decision_log.py          # craft-adaptation logging + guardrail handling
    surface.py               # surface-on-signal decisions
    iteration_dir.py         # write run.yaml, batch.yaml, decision-log.md (the contract comic-trace reads)
    contact_sheet.py         # PIL grid composition for batch surfacing
    canvas_client.py         # thin wrapper that shells out to /comic-trace compose-sub-canvas + link-sub
  config.yaml                # tier, default qualities, default budgets

# NOTE: no sub_canvas.py — canvas writing belongs to comic-trace.

_style/<comic-slug>/
  manifest.yaml
  bible/                     # 3-5 user-curated style reference images
  characters/<name>/         # 1-3 ref images per recurring character
  panels_kept/               # canonical "this one landed" panels, used as continuity refs
  drafts/                    # work-in-progress page versions for harvesting

_trace/_iterations/<comic-slug>/<page-or-panel>/<timestamp>/
  request-blast.md           # the user's input (or what was inferred)
  run.yaml                   # batches, prompts, params, refs, cost, time
  decision-log.md            # every prompt change, refusal, surface decision
  gen-batch-NN/              # one folder per batch
    gen-NN-MM.png            # individual gens
    contact-NN.png           # batch contact sheet
  run.canvas                 # sub-canvas conforming to comic-trace schema
  notes.md                   # picks, surprises, what landed
```

---

## The Phase 1 capability: `/image-chase fix`

### Request-blast format

The user's input is a markdown file (or inline text) capturing a multi-constraint request. Loose by design — the agent parses it with judgment, not regex. Real example:

```markdown
# Fix request — P3 (Honey, sexual)

## Fight for
- Charles Manson likeness — slight, dark-eyed, magnetic, gaunt
  (ref: characters/charlie/01.png — fight for this)
- Style: iconic, popart simple shapes, less detail and texture
  (anchor against bible/cartoony-shape-language.png)
- Lettering: match captions on neighbor pages

## Harvest from drafts
- Panel 1: from drafts/p3-v3.png (the Sadie pull-toward-bed framing)
- Panel 4: from drafts/p3-v5.png (Mike walking out, jacket buttoned)

## Fix
- Panel 2 eyelines: Mike eyes down at hands; Sadie eyes on Mike
  (not at viewer — refs/p2-eyeline-fix.png shows what I want)
- Panel 3 eyelines: Charlie's eyes UP and ACROSS — load-bearing,
  see _trace/_notes/2026-04-29-new-p3-honey-script.md

## Continuity
- Prior page: panels_kept/P2.png
- Next page: panels_kept/P4.png (current draft, not final)
- Caption box style must match P2 lettering
```

The format documented in `_shared/request-blast-format.md` lists conventional sections — `Fight for`, `Harvest from drafts`, `Fix`, `Continuity` — but doesn't enforce them. The agent reads the blast, asks clarifying questions if anything's ambiguous, and composes a plan.

### What `fix` actually does

1. **Parse** the request blast (with the agent's eyes — `request_blast.py` is mostly a section-splitter, not a strict parser)
2. **Resolve refs** — find the named ref images, harvest sources, neighbor pages. If anything's missing, ask the user where to find it (or `--auto-find` mode searches the manifest folders)
3. **Compose initial prompts** per panel (or per page if it's a single-page chase)
4. **Run the loop** — fire batches of 3-4 gens, score conversationally, decide surface vs. continue (see surface policy below)
5. **Maintain decision log** — every prompt change, refusal, craft adaptation logged with rationale
6. **Emit sub-canvas** when run completes, conforming to comic-trace schema
7. **Return summary** — what landed, what didn't, where the picks are, total cost/time

### Invocation

```
/image-chase fix P3 \
  --request-blast _trace/_iterations/scroggins-manson/P3/request-blast.md \
  --comic scroggins-manson \
  --budget-time 2h \
  --budget-usd 1.00 \
  --batch-size 4
```

`--request-blast` can be a path or `-` for inline (the user pastes/types the blast in conversation).

`--budget-time` and `--budget-usd` are dual caps; either trips the stop. Default time: 2h. Default USD: $1.00.

### What the user sees

The skill runs in the background via Claude Code's `/loop` (or in-session bash with `run_in_background`). The user goes about their day. The skill surfaces when there's signal worth their eye:

- **First batch returns** — agent evaluates: "Got 4. Two passed the must-survive checks (likeness landed, eyelines on Mike correct). Two failed (Charlie eyes still wrong direction, drift on style). Continuing with refined prompt — pushing harder on Charlie's gaze. Want to see the two passes now or wait for more?"
- **Refusal hit** — agent surfaces immediately: "Hit a likeness refusal on the explicit name. Trying shape-language only (slight/dark-eyed/magnetic, no name). One worked. Continuing."
- **Survivor milestone** — agent: "3 strong passes now. Surfacing contact sheet — pick one, refine the rubric, or continue?"
- **Steady churn** — agent: no surface for 20 min, then: "20 min, 12 gens, no clear winner. Suggest a manual look. Want to see what's been generated?"
- **Budget threshold (50%, 80%)** — agent: "Halfway through budget — current state: 1 strong pass, 5 partials, 6 misses. Continue or pause?"
- **Budget cap hit** — agent: "Cap reached. Final state: 2 strong passes. Run summary attached."

---

## Loop autonomy and the surface-decision rubric

The skill leans on Claude Code's `/loop` primitive in dynamic-pacing mode. The agent fires batches, evaluates, and uses a documented set of triggers to decide whether to interrupt the user.

### Documented in `_shared/surface-policy.md`

**Surface immediately:**
- A gen passes the load-bearing constraints from the request blast (real signal)
- A policy refusal hits (need user direction or transparency)
- Three or more cumulative passes accumulate (enough to pick from)
- A "surprise" — gen has something not in the blast that's interesting
- Continuity break with neighbor pages (style drift, character drift)
- Budget threshold crossed (50%, 80%, 100%)

**Continue quietly (no surface):**
- Within budget, on cadence, no signal yet, prompt being refined
- Steady misses on must-survive (still gathering info)
- Successive batches showing slow improvement (hill-climbing, surface only when plateau)

**Cadence floor:** never go more than 20 minutes without at least a brief check-in surface, even if nothing's happening. Avoids the "did it die?" anxiety.

### Decision log

Every surface decision (surface or quiet-continue) is logged to `decision-log.md` with:
- Batch number, gen IDs, surface decision (yes/no), trigger or rationale
- Prompt used, prompt change from prior batch (if any), reason for change
- Refusals encountered, craft adaptations attempted (see Guardrails section)

This gives the user an auditable record of agent judgment. Read it if a run feels off; tune `surface-policy.md` if patterns emerge.

---

## Guardrails and decision log: when the agent is being smart vs. brute-forcing

A real concern named in the design exchange: when is the agent doing legitimate craft adaptation (which is fine) vs. trying to brute-force past content guardrails (which is wrong)?

The skill operates under an explicit policy documented in `_shared/decision-log.md`:

### Legitimate craft adaptation (agent does, agent logs)
- Translating a named real-person likeness into shape-language descriptors when the model balks (e.g., "slight, dark-eyed, magnetic, gaunt" instead of "Charles Manson") — this is art direction, not gaming
- Suggesting nudity through silhouette, motion lines, cartoon abstraction rather than explicit rendering — genre craft for a stylized comic
- Restructuring a prompt that triggered moderation on an unrelated phrasing
- Bracketing — trying multiple legitimate phrasings of the same intent when a refusal looks like a false positive

### Not legitimate (agent will not do; surfaces and stops)
- Jailbreak-style prompt injection
- False context claims to bypass policy
- Silently routing around restrictions without logging
- Repeated brute-force retries against a clear policy refusal (more than 2 craft adaptations on the same refusal)

### Reporting

When a refusal hits, the agent surfaces explicitly:

> *Refused on suspected likeness — tried 2 craft adaptations (shape-language only, no name). One passed, one didn't. Continuing with the passed phrasing. Decision-log entry: batch-03/refusal-01.*

If the agent hits a real wall (the panel needs explicit content the model won't generate), it stops and asks for direction:

> *Stopping on Panel 2: model won't generate the hanging-bed scene with the level of body detail requested. Options: restage with stronger silhouette abstraction, drop the panel from this run, or you take this one to chat for hand-iteration.*

The user sees every adaptation and every wall. No silent gaming.

---

## Conversational scoring (not in-loop)

A revision from the prior design draft: **gen evaluation happens in conversation between the agent and user, not via a vision-model rubric inside the loop.** Rationale:

- The agent (Claude) brings full context — canvas, script, narrative, prior decisions, the user's taste from prior turns — that a vision-API call doesn't have
- One less component to build (no `lib/rubric.py`, no structured-output schemas, no scoring API calls)
- Honors alternation directly: the loop fans out gens, the agent evaluates conversationally, the user picks
- Vision models hallucinate features anyway, especially style ones; auto-rejection unreliable

What the agent does on each batch return:
1. View the gen images
2. Read them against the request blast
3. Categorize: pass / partial / miss / refusal / surprise
4. Decide: surface this batch, or refine and continue
5. Log the decision

The "rubric" still exists as a written list of must-survive constraints in the request blast — but it's documentation for the agent's judgment, not an automated gate.

**When in-loop scoring becomes useful (deferred to Phase 2 or later):** unattended overnight runs, parallel chases at scale, programmatic stop conditions beyond N/USD/time. None of that is the v1 pain.

---

## Sub-canvas output: live append, like a chat history

The sub-canvas is **not produced at end of run**. It exists from second one and grows event-by-event. The user can open it at any moment of an active run and see current state. They can lean on it being there, like scrolling a ChatGPT chat that's mid-conversation.

This works because image-chase calls into comic-trace at every meaningful event, not just at completion.

### Event call cadence

| Moment | image-chase calls | What lands on the sub-canvas |
|---|---|---|
| Run start | `compose-sub-canvas --mode init` | Empty frame: lanes, request blast (upper-left), refs as ARTIFACTS, status node "active" |
| Run start | `link-sub --status active` | Main provenance canvas gains a file-link node, marked active (orange) |
| Each batch returns | `compose-sub-canvas --mode append --event batch` | Group cluster: gens, prompt used, contact sheet, agent's pass/partial/miss/refusal categorization |
| Surface decision | `compose-sub-canvas --mode append --event surface` | Annotation noting trigger (survivor milestone, refusal, threshold, cadence) |
| Refusal | `compose-sub-canvas --mode append --event refusal` | Refusal node, immediately so the wall is visible in real time |
| Craft adaptation | `compose-sub-canvas --mode append --event adaptation` | Adaptation annotation with before/after prompt change |
| User picks a gen | `compose-sub-canvas --mode append --event pick` | Pick edge from the chosen gen |
| User redirects mid-run | `compose-sub-canvas --mode append --event user-direction` | User-input annotation |
| Run end | `compose-sub-canvas --mode finalize` | Summary node (cost, time, picks); status node flips "active" → "complete" |
| Run end | `link-sub --status complete` | Main canvas link reverts to default treatment, gets completion timestamp |

image-chase doesn't know canvas internals. It produces well-formed event arguments and trusts comic-trace to render. comic-trace handles atomic writes (write-temp-and-rename) so opening the canvas during a write never sees corrupted JSON.

### What the user sees

Open the main provenance canvas mid-run: a new orange-tinged node ("fix run — running since 14:30") appears next to the panel being chased. Double-click it to enter the sub-canvas. See: request blast in upper-left, refs in the artifact lane, three batch clusters so far, latest surface decision two minutes ago.

Walk away. Come back twenty minutes later. Same canvas, more batches. Or the status node flipped to "complete" with a summary and the main-canvas link is back to default — the run finished while you were gone.

Or come back to find the status still says "active" but no new events for 30 minutes — something stalled. comic-trace exposes a `mark-stale` recovery command for this case.

### Failure-mode visibility

If image-chase crashes mid-run, the sub-canvas survives at last-append state. Status still says "active" but timestamps reveal the silence. Nothing is lost; nothing is hidden. This is what "lean on it being there" actually means as a design property.

### Canvas writing belongs to comic-trace

image-chase has no `lib/sub_canvas.py`. Schema details, lane positioning, color conventions, edge routing — all owned by comic-trace. image-chase's contract is: produce a well-formed iteration directory (per `_shared/iteration-directory-format.md` over in comic-trace) and call the four event endpoints. If schema evolves, only comic-trace updates. Future skills (audio-transcript, external-feedback-import, etc.) plug into the same interface.

---

## Implementation order

**Prerequisite:** comic-trace Phase 1 + 2 must ship first (it owns canvas writing).

For image-chase Phase 1:

1. **`lib/api.py`** — OpenAI client wrapper with retries, 429 backoff, streaming-aware, cost tracker. Foundation. Test against a single low-quality gen ($0.006).
2. **`lib/manifest.py`** — load `manifest.yaml` into a `Refs` object exposing `open_files()`, `input_token_estimate()`, `prompt_suffix`, and `for_panel(name)` → relevant subset. Test against a hand-built Scroggins manifest.
3. **`lib/request_blast.py`** — parse a request-blast markdown into a structured plan (sections, refs named, panels mentioned). Loose parsing — agent fills gaps via conversation.
4. **`lib/iteration_dir.py`** — write the iteration directory contract (`run.yaml`, `gen-batch-NN/batch.yaml`, `decision-log.md`). The format is the source of truth comic-trace reads.
5. **`lib/decision_log.py`** — append-only log writer with structured entries (batch, decision, rationale).
6. **`lib/surface.py`** — surface-decision logic per the policy doc. Pure function: `(batch_results, run_state, policy) → SurfaceDecision`.
7. **`lib/contact_sheet.py`** — PIL grid for a batch (4 images, captions). Unit-testable without API calls.
8. **`lib/canvas_client.py`** — thin wrapper that shells out to `/comic-trace compose-sub-canvas` and `/comic-trace link-sub`. No canvas knowledge here, just argument formatting.
9. **`fix.py`** — assembles the above. The headline capability. Drives the loop via Claude Code's `/loop` primitive (or in-session bash with `run_in_background`). Calls into `canvas_client` at the documented event moments.
10. **Skill markdown specs** — `SKILL.md`, `fix.md`, `_shared/*`. Written when tools work.

If budget for the implementation work runs short, **stop after step 9.** That's a working `fix` capability with surface-on-signal autonomy, decision-log transparency, and live sub-canvas integration.

For Phase 2:
10. **`spread.py`** — variant of fix with prompt-level variation, no rubric, just a labeled contact sheet. Cheapest sub-command to add given the foundation.
11. **`study.py`** — character contact sheet variant. Reuses spread infrastructure.
12. **`bake.py`** — wraps fix logic at quality=high, smaller n, writes to `panels_kept/` on confirm.
13. **`style-lock.py`** — manage `_style/<comic>/bible/` set; audit drift across recent gens.

---

## Smoke test

Before declaring Phase 1 done, run:

```
/image-chase fix P3 \
  --request-blast <hand-written, derived from _trace/_notes/2026-04-29-new-p3-honey-script.md> \
  --comic scroggins-manson \
  --budget-time 30m \
  --budget-usd 0.30 \
  --batch-size 4
```

against a hand-built `_style/scroggins-manson/manifest.yaml` (the user assembles bible images from `_trace/_assets/` — about 30 minutes of curation).

Expected behavior:
- First batch returns in ~1-3 min
- Agent surfaces with 2-4 categorized gens, decision log entry written
- User picks or refines; loop continues
- Run completes within budget (likely under $0.30, well under 30 min)
- Sub-canvas emitted at `_trace/_iterations/scroggins-manson/P3/<timestamp>/run.canvas`
- Canvas validates against schema; can be opened in Obsidian
- Decision log readable, every adaptation accounted for

Total smoke-test cost: ~$0.30. Phase 1 is shippable if this passes.

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Cost runaway despite caps | Dual cap (time + USD). Surface at 50%/80% thresholds for human override. Bake quality is opt-in only after fix completes. |
| Tier-1 rate limits make 32-gen run take >30 min | Skill is tier-aware; on tier 1, batches are smaller (2-3) and longer pauses. Higher tiers parallelize. Set tier in `config.yaml`. |
| The `/loop` primitive isn't available or behaves differently | Fallback: in-session background bash. Same behavior, but stops if Claude Code session closes. Document this constraint. |
| Agent judgment on surface decisions feels wrong | Decision log is auditable. User tunes `_shared/surface-policy.md`. Not a code change — policy doc edit. |
| Refusal escalation feels gamey | Hard limit: 2 craft adaptations per refusal type per run. Beyond that, surface and stop. Documented in `_shared/decision-log.md`. |
| The request-blast format is too loose | The looseness is intentional — user shouldn't have to write structured YAML. Agent asks clarifying questions when needed. If parsing repeatedly fails, surface "I need more structure here" rather than guess. |
| Reference image cost (no `input_fidelity` knob) makes some runs surprisingly expensive | Estimate input tokens with coarse multiplier; surface in cost tracker before each batch. After first real runs, tune budget defaults in `config.yaml`. |
| Sub-canvas drift from comic-trace schema | image-chase doesn't write canvases — comic-trace does. Schema lives in one place. No drift possible. |
| comic-trace not yet shipped when image-chase Phase 1 begins | Hard-block. Don't start image-chase implementation until comic-trace Phase 2 is in place. The dependency is real. |
| Multiple panels in one fix call confuses the agent | v1 supports single-panel or single-page chases. Multi-page is Phase 2 (`spread` is closer to the right shape for that). |

---

## What you'd hand the implementer

- This document, plus the comic-trace design doc
- An OpenAI API key with org verification
- The Scroggins corpus already in the vault: `_trace/_assets/`, `_journal/2026-04-22.md`, the existing canvas, the new P3 script (`_trace/_notes/2026-04-29-new-p3-honey-script.md`)
- A hand-curated `_style/scroggins-manson/manifest.yaml` (~30 min of work by the user)
- A hand-written request blast for the new P3 (the LOAD-BEARING section in the new P3 script doc is most of it; convert to the request-blast format)

Total smoke-test cost: ~$0.30. Phase 1 shippable in a focused work session if API access is in place. Phase 2 builds incrementally on the same foundation.

---

## References

OpenAI API documentation:
- [GPT Image 2 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-image-2)
- [Image generation guide | OpenAI API](https://developers.openai.com/api/docs/guides/image-generation)
- [Introducing ChatGPT Images 2.0 | OpenAI](https://openai.com/index/introducing-chatgpt-images-2-0/)

Source material in this vault:
- Companion design: `_system/_design/comic-trace-skill-design.md`
- Prototype canvas: `_trace/2026-04-22-scroggins-manson-comic-provenance.canvas`
- Origin exchange: `_trace/_notes/2026-04-29-canvas-read-exchange.md`
- New P3 script (request-blast source): `_trace/_notes/2026-04-29-new-p3-honey-script.md`
- Builder's note on load-bearing pattern: `builders_notes.md` (entry dated 2026-04-29)
