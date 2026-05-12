---
type: design
created: 2026-04-29
status: proposal
implements: comic-trace skill
prototype-canvas: [[_trace/2026-04-22-scroggins-manson-comic-provenance]]
related-design: [[_system/_design/image-chase-skill-design]]
context: [[_trace/_notes/2026-04-29-canvas-read-exchange]]
---

# Comic-trace skill — design + implementation brief

A vault skill that maintains a provenance canvas for a comic-making process — capturing each artifact (journal, hold output, script revision, external chat session, image generation, feedback) as it appears, edging it to its predecessors, placing it in the right lane, and distinguishing user annotations from agent annotations.

The skill **plays off the existing Scroggins/Manson provenance canvas** (`_trace/2026-04-22-scroggins-manson-comic-provenance.canvas`) as a hand-built prototype. That canvas defines the conventions (lanes, colors, node types, edge labels) the skill formalizes and automates.

This document is self-contained. An implementer should be able to pick up the work cold from this brief plus the prototype canvas as a reference.

---

## Why this exists

The current vault has rich artifact tracking — journals, hold reflections, inbox scripts, image-chase iterations — but no skill that organizes them into a coherent provenance graph for a single creative thread (e.g., one comic). The user manually built the Scroggins canvas to make that graph visible. Quote from the canvas legend node:

> *"red (provisional...im interested in segregating me and the ai and having me always comment and contextualize its input = ai/agent)"*

That note signals two real wishes:
1. **A canvas treatment for the whole comic-making process**, from first phone-ramble to final pages, not just for image iteration
2. **Explicit segregation of user annotation from agent annotation**, so the human voice and the agent voice never blur

This skill makes both real, and ships before any image-API work because it's vault-organizing only — no external dependencies.

---

## Scope

### Phase 1 (build first)

- **`/comic-trace init`** — initialize a new comic canvas with empty lanes
- **`/comic-trace capture`** — add an artifact node (journal / hold / inbox / external chat / image / feedback / etc.), edged to its predecessor, placed in the right lane
- **`/comic-trace annotate`** — add a user or agent annotation node, color-distinguished
- **Canvas schema** — lanes, colors, node types, edge labels formalized from the Scroggins prototype

### Phase 2 (build close behind, when image-chase exists)

- **`/comic-trace link-sub`** — attach an image-chase sub-canvas as a node on the main provenance canvas
- **`/comic-trace compose-sub-canvas`** — used by image-chase to emit a canvas from an iteration directory in the schema this skill expects

Phase 1 ships independently. Phase 2 is the integration with image-chase, and assumes the sub-canvas schema is honored on both sides.

---

## The prototype canvas

`_trace/2026-04-22-scroggins-manson-comic-provenance.canvas` is the model. Its conventions:

**Lanes (vertical bands, labeled left-edge):**
- `ARTIFACTS` — files in the vault (journals, scripts, images, sub-canvases)
- `TRANSITIONS` — process steps between artifacts (hold-skill run, ChatGPT script session, ChatGPT image session, page revisits)
- `ANNOTATIONS` — user observations, agent observations, wishes, process alerts, external feedback

**Colors (per the canvas legend):**
- *cyan* (no explicit color, default) — vault file (exists, clickable)
- *orange* (color 2) — external / to import / external process marker
- *purple* (color 1) — annotation (text observation, quote card, wish)
- *no color* on edges — transition
- *red* (provisional) — agent / AI input, distinguished from user

**Node types:**
- `file` — vault artifact
- `text` — annotation, transition note, lane label, legend, wish
- `link` — external URL (e.g., a ChatGPT share link)
- `group` — labeled cluster of related nodes

**Edge labels:**
- Process transitions: `via hold skill`, `via external edit`, `accidental full page`, `led to`, `seed type variations`
- Page numbers: `1`, `2`, `3`, `4`, `5`
- Iteration relationships: `rewrite`, `cleaner`, `regroup`, `1 of 5`, `attention to lettering`

**Cluster patterns:**
- Group nodes (`type: "group"`) wrap related sub-clusters with a labeled banner (e.g., `"REVISITING PAGES — i worked from page 4 to page 5..."` and `"5 page comic first/solo pass"`)

These conventions are documented in `_system/_skills/comic-trace/_shared/canvas-schema.md` and any new comic canvas conforms.

---

## Sub-capabilities

### `/comic-trace init <comic-slug> [--from-prototype <path>]`

Creates `_trace/<comic-slug>-provenance.canvas` with:
- Three lane labels (`ARTIFACTS`, `TRANSITIONS`, `ANNOTATIONS`) at left edge
- A legend node in upper-left (using the prototype's legend text as default)
- Empty otherwise

`--from-prototype` defaults to the Scroggins canvas; can be overridden if the user develops a new prototype later.

**Example:**
```
/comic-trace init scroggins-manson
```

### `/comic-trace capture <type> <source> [--predecessor <node-id-or-slug>] [--lane <override>]`

Adds an artifact node to the canvas. Capture types and their default behavior:

| Type | Source | Default lane | Default color | Default edges |
|---|---|---|---|---|
| `journal` | path to `_journal/<date>.md` | ARTIFACTS | cyan | none (root of process) |
| `hold` | path to `_reflection/<date>-hold...md` | ARTIFACTS | cyan | from journal of same date |
| `inbox` | path to `_inbox/<date>-...md` | ARTIFACTS | cyan | from `responds_to` frontmatter |
| `chatgpt-script` | text describing session + optional URL | TRANSITIONS | orange | from inbox |
| `chatgpt-image` | text describing session + optional URL | TRANSITIONS | orange | from script |
| `image` | path to `_trace/_assets/<file>` | ARTIFACTS | cyan | from chatgpt-image session or prior image |
| `image-chase-sub` | path to a sub-canvas file | ARTIFACTS | cyan | from chatgpt-image or image being fixed |
| `external-feedback` | text + optional `--from <name>` | ANNOTATIONS | purple | to the artifact being commented on |
| `wish` | text | ANNOTATIONS | purple | to nearest related artifact |
| `process-alert` | text | ANNOTATIONS | orange | to nearest cluster (e.g., "ready for feedback") |
| `idea` | text | ANNOTATIONS | purple | to triggering artifact |

**Predecessor resolution:**
- If `--predecessor` given, edge from that node-id (or slug — agent resolves to id)
- Otherwise, infer from frontmatter (`responds_to`, `source`) or filename date proximity
- If still ambiguous, surface to user: *"I can't infer the predecessor; please name it."*

**Lane override:** rare but supported (e.g., a wish that's really part of the artifact lane).

**Position auto-layout:** heuristic. Capture appends to the right edge of its lane, vertically positioned to align with related nodes. Skill is additive — doesn't relayout existing nodes.

**Example:**
```
/comic-trace capture hold _reflection/2026-04-22-holdv04test.md
```

### `/comic-trace annotate` — modifier mode

A refinement to `annotate` that adds a `--type modifier` option. Critical for honoring the segregation principle when one party (user or agent) wants to calibrate the other's text.

**The problem it solves:** the agent writes a meta lesson with overconfident generalizations. The user catches the overstatement. Without a modifier mode, the only options are (a) silently rewriting the agent's text — which violates segregation, or (b) adding a free-floating annotation in the ANNOTATIONS lane that doesn't visually attach to the thing being critiqued.

**The pattern:** modifier creates a node *directly below* the target (not in the ANNOTATIONS lane), edged from modifier→target (the modifier *acts on* the target). The original text is never touched. A future reader sees both: the original claim, the calibration critique, optionally a chain of acknowledgments.

**Behavior differences from regular annotation:**

| | Regular annotation | Modifier |
|---|---|---|
| Position | ANNOTATIONS lane, aligned with target's x | Directly below target, full target width |
| Edge direction | target → annotation (annotation derives from target) | modifier → target (modifier acts on target) |
| User color | color 1 | no color (matches hand-built critique pattern) |
| Agent color | color 1 | color 1 |
| Prefix | `[AGENT]:` for agent | `USER MODIFIER (CRITIQUE)` for user; `[AGENT] MODIFIER` for agent |

**Modifier chains** are first-class: agent writes claim → user critiques → agent acknowledges. Each link uses `--type modifier`, edged in sequence. The chain visualizes the calibration thread without any party silently rewriting another.

**Pattern origin:** observed during a 2026-04-30 session where the user manually built a critique node attached to an agent meta-lesson. The hand-built version revealed the missing capability; the modifier mode formalizes it.

### `/comic-trace adopt <existing-canvas-path> --as-slug <comic-slug>`

One-shot mechanism for bringing a hand-built canvas under skill management without recreating it. Critical for the Scroggins case where the user has already invested in a manual provenance canvas at `_trace/2026-04-22-scroggins-manson-comic-provenance.canvas` and wants subsequent skill operations (capture, annotate, link-sub) to target that file instead of a new one.

**What it does:**
- Reads the existing canvas; validates loosely against the schema (lenient mode — won't reject canvases that conform to the conventions but have idiosyncratic positioning or custom group clusters)
- Writes a small registry entry mapping `<comic-slug>` → `<existing-canvas-path>` to `_system/_tools/comic-trace/registry.yaml`
- Subsequent `capture`, `annotate`, `link-sub` commands using that slug target the adopted canvas, not a new file
- Does not modify the canvas itself; adopt is a registry change only

**Validation behavior:**
- If the canvas is malformed JSON, refuse and surface the parse error
- If lanes are missing or mis-positioned, surface a warning but adopt anyway (the user can fix later, or skill will tolerate)
- If colors/edge labels deviate from convention, no warning — those are user-choice details

**Safety:**
- Atomic writes still apply to all subsequent operations against the adopted canvas
- The user should keep their backup until they've confirmed the first capture/link-sub against the adopted canvas works as expected
- An `unadopt` command (or manual edit of `registry.yaml`) reverts the mapping

**Example (the Scroggins case):**
```
/comic-trace adopt _trace/2026-04-22-scroggins-manson-comic-provenance.canvas \
  --as-slug scroggins-manson
```

Now `/comic-trace capture image ... --comic scroggins-manson` writes to the existing canvas. Image-chase's eventual `link-sub` for new-P3 also targets it.

### `/comic-trace annotate <node-id-or-slug> [--by user|agent] [--type observation|wish|alert|context]`

Adds an annotation text node, edged to the target node. Distinguished by color:

- `--by user` (default if invoked by user) → color 1 (purple)
- `--by agent` (default if invoked by agent) → color provisional / red marker if available, or labeled prefix `[AGENT]:` if not
- `--type` defaults to `observation`; affects label prefix in the node text

The user can also write the annotation content via stdin or a quoted argument.

**Example:**
```
/comic-trace annotate billy-honey-page --by user --type observation
> "michael and billy are pulling girls out of charlie's orbit..."
```

### `/comic-trace link-sub <sub-canvas-path> [--predecessor <node-id>] [--label <edge-label>] [--status active|complete]`

(Phase 2.) Drops a file node on the main canvas referencing a sub-canvas. Default edge label: `iterated`.

`--status active` paints the link in an "in-progress" treatment (orange tinge, label includes start time). `--status complete` reverts to default and adds the completion timestamp. image-chase calls this twice per run — once at start with `--status active`, once at end with `--status complete`.

**Example:**
```
/comic-trace link-sub _trace/_iterations/scroggins-manson/P3/2026-04-29-1430/run.canvas \
  --predecessor chatgpt-image-session-p3 \
  --label "fix run" \
  --status active
```

### `/comic-trace compose-sub-canvas --mode {init|append|finalize} <iteration-dir> [event params]`

(Phase 2.) The live sub-canvas capability. Used by image-chase (and any future skill that wants to produce a sub-canvas). Modeled on chat-history shape: the sub-canvas exists from the moment a run starts and grows event-by-event, atomic-write-safe so the user can open it mid-run.

**Modes:**

- **`--mode init`** — creates the sub-canvas at `<iteration-dir>/run.canvas` with frame (lanes, request blast as upper-left annotation, refs as ARTIFACTS, a status node marked "active"). Single call at run start.

- **`--mode append --event <type>`** — appends nodes/edges for an event. Event types:
  - `batch` — adds a group cluster with the batch's gens, prompt used, contact sheet, agent's categorization (pass/partial/miss/refusal)
  - `surface` — adds an annotation noting why the loop surfaced (survivor milestone, refusal, threshold, cadence)
  - `adaptation` — adds an annotation logging a craft adaptation (what was changed, why, before/after prompt)
  - `refusal` — adds a node marked refusal (orange, prefixed `[REFUSAL]`) with the model's response
  - `pick` — adds an annotation edge from a picked gen to indicate user selection
  - `user-direction` — adds an annotation when the user redirects the run mid-flight

- **`--mode finalize`** — adds a summary node (cost, time, picks, what landed); flips the status node from "active" to "complete". Single call at run end.

**Atomic writes:** every mode writes to a temp file and renames. Opening the canvas mid-run never sees corrupted JSON.

**Failure mode:** if image-chase crashes mid-run, the sub-canvas remains in whatever state it reached at last append. The status node still says "active" but timestamps show no recent activity — the user can see the run died. comic-trace can also expose a `compose-sub-canvas --mode mark-stale` for explicit recovery.

**Schema validation:** every write validates against `_shared/canvas-schema.md`. Fail-loud on schema violation.

**Example flow within a fix run:**
```
# at run start
/comic-trace compose-sub-canvas --mode init <iter-dir>

# after each batch
/comic-trace compose-sub-canvas --mode append --event batch <iter-dir> --batch-num 1

# on each surface
/comic-trace compose-sub-canvas --mode append --event surface <iter-dir> --reason "3 survivors"

# on a refusal
/comic-trace compose-sub-canvas --mode append --event refusal <iter-dir> --batch-num 3 --gen-id 02

# at run end
/comic-trace compose-sub-canvas --mode finalize <iter-dir>
```

The contract from the calling skill (image-chase or future): produce a well-formed iteration directory with the structure documented in `_shared/iteration-directory-format.md`. comic-trace reads the directory and renders. image-chase never writes canvases directly.

---

## Vault layout

```
_system/_skills/comic-trace/
  SKILL.md                  # entry point; routes /comic-trace to sub-commands
  init.md
  capture.md
  annotate.md
  adopt.md                  # bring a hand-built canvas under skill management
  link-sub.md               # phase 2
  compose-sub-canvas.md     # phase 2
  _shared/
    canvas-schema.md        # lane/color/edge conventions formalized from Scroggins
    artifact-types.md       # detail on each capture type
    lane-conventions.md     # positioning heuristics
    iteration-directory-format.md   # phase 2; the contract calling skills must honor

_system/_tools/comic-trace/
  init.py
  capture.py
  annotate.py
  adopt.py                  # registry-write only; doesn't modify canvas
  link_sub.py               # phase 2
  compose_sub_canvas.py     # phase 2; init/append/finalize modes
  lib/
    canvas.py               # canvas JSON read/write/edit (atomic, write-temp-and-rename)
    schema.py               # validation against canvas-schema.md (strict + lenient modes)
    layout.py               # lane positioning + edge auto-routing
    resolve.py              # predecessor inference (frontmatter, filenames, dates)
    events.py               # phase 2; event-type → node/edge mapping for append mode
    registry.py             # slug → canvas-path mapping (read/write registry.yaml)
  registry.yaml             # slug → canvas-path mapping; created on first init or adopt
  config.yaml               # default lane positions, default colors, prototype path

_trace/<comic-slug>-provenance.canvas    # the canvas being maintained
```

---

## Canvas schema (the contract)

Documented in `_system/_skills/comic-trace/_shared/canvas-schema.md`. Sketch:

```yaml
canvas_version: 1
lane_labels: [ARTIFACTS, TRANSITIONS, ANNOTATIONS]
lane_x_positions:                    # default x for each lane
  ARTIFACTS: 0
  TRANSITIONS: 1500
  ANNOTATIONS: 3000
node_types:
  file:
    color_default: cyan              # i.e., omit color field
    color_overrides:
      iteration_artifact: 6          # for in-progress / "too real" markers
  text:
    annotation: 1                    # purple
    external: 2                      # orange
    agent_input: provisional_red     # explicit agent marker
    lane_label: 0                    # default
  link:
    external: default                # no color override
  group:
    cluster: 0                       # default
edge_conventions:
  process_step:
    color: default
    label_required: true
  iteration:
    color: default
    label_examples: [rewrite, cleaner, regroup, 1, 2, 3, 4, 5]
  annotation:
    color: default
    label_optional: true
```

Image-chase sub-canvases conform to the same schema. Validation in `lib/schema.py` enforces this before linking.

---

## Implementation order

1. **`lib/canvas.py`** — read/write `.canvas` JSON safely. Atomic writes (write to temp, rename). Foundation. Test by round-tripping the Scroggins canvas (read → write → diff should be empty).
2. **`init.py`** — create a new canvas with lane labels and default legend. Trivial once `canvas.py` exists. Smoke-test against an empty workspace.
3. **`lib/resolve.py`** — predecessor inference from frontmatter (`responds_to`, `source`), filename date proximity, content match. Critical for `capture`'s usability.
4. **`capture.py`** — start with three highest-volume types: `journal`, `hold`, `inbox`. Get the placement and edge auto-creation right against these before adding more.
5. **Round-trip test against the Scroggins canvas:** can capturing each existing artifact recreate something approximating the prototype? Not pixel-identical (positioning is heuristic), but the *graph* — nodes and edges and colors — should match. **This is the v1 acceptance test.**
6. **Add remaining capture types:** `chatgpt-script`, `chatgpt-image`, `image`, `external-feedback`, `wish`, `process-alert`, `idea`. Each gets a small recipe in `_shared/artifact-types.md`.
7. **`annotate.py`** — user vs. agent annotation, with the color/prefix distinction. Honors the "segregate me from the ai" principle.
8. **Skill markdown specs** — `SKILL.md`, sub-command specs. Written last, document real behavior.
9. **(Phase 2) `compose_sub_canvas.py` and `link_sub.py`** — when image-chase is ready to integrate.

---

## Smoke test

**The smoke test is mechanics, not replay.** The Scroggins prototype was hand-built over weeks and includes dozens of events (image-gen iterations, ChatGPT sessions, external feedback, page revisits, manual annotations) that were never logged as they happened. They cannot be reconstructed from current vault state — only the journal, hold reflection, inbox script, and a few trace notes exist as files. Asking the skill to "rebuild" the prototype would be asking it to invent provenance that doesn't exist.

What the smoke test actually validates is that the skill's mechanics produce structurally-correct nodes, edges, lanes, and colors against artifacts that *do* exist in the vault.

**Phase 1 acceptance test:**

```
/comic-trace init scroggins-manson-test
/comic-trace capture journal _journal/2026-04-22.md
/comic-trace capture hold _reflection/2026-04-22-holdv04test.md
/comic-trace capture inbox _inbox/2026-04-22-reply-reply--comic-script.md
/comic-trace capture image _trace/_assets/scroggins-charlie.png \
  --predecessor inbox-2026-04-22-reply-reply--comic-script
/comic-trace annotate scroggins-charlie --by user --type observation
> "first refined character image; led to seed type variations"
```

The resulting `_trace/scroggins-manson-test-provenance.canvas` should:

- Open in Obsidian without errors
- Have three lane labels (`ARTIFACTS`, `TRANSITIONS`, `ANNOTATIONS`) at left edge
- Have a legend node in upper-left
- Have four file nodes in the ARTIFACTS lane, cyan/no-color
- Have edges journal→hold (from `source` frontmatter) and inbox→hold (from `responds_to` frontmatter), inferred automatically by `lib/resolve.py`
- Have one purple annotation node edged to the image
- Validate against `lib/schema.py`

That's the bar. It tests:
- Canvas init produces the correct frame
- Capture places artifacts in the right lane with the right color
- Predecessor inference works from frontmatter
- Annotate produces correct color and edges
- Schema validation accepts skill output

If this passes, Phase 1 is shippable. **The "real" acceptance test — the one that matters — is using the skill on the next comic from day 1**, capturing artifacts as the process unfolds. The smoke test above just confirms the mechanics aren't broken before you commit to using it.

## Phase 2 acceptance

For `link-sub` and `compose-sub-canvas`, the smoke test waits on either image-chase being implemented or a hand-built fake iteration directory. A reasonable proxy:

```bash
# create a fake iteration directory with the documented format
mkdir -p _trace/_iterations/scroggins-manson-test/P3/2026-04-30-1200/gen-batch-01
# populate run.yaml, batch.yaml, decision-log.md with realistic-looking content
# add a couple of placeholder gen images

/comic-trace compose-sub-canvas --mode init _trace/_iterations/scroggins-manson-test/P3/2026-04-30-1200
/comic-trace link-sub _trace/_iterations/scroggins-manson-test/P3/2026-04-30-1200/run.canvas \
  --predecessor scroggins-charlie --status active
/comic-trace compose-sub-canvas --mode append --event batch ... --batch-num 1
/comic-trace compose-sub-canvas --mode finalize ...
/comic-trace link-sub ... --status complete
```

The sub-canvas should grow event-by-event, the main canvas link should change treatment from active to complete, and both canvases should validate. That tests the integration without waiting on the API.

---

## Risks and mitigations

| Risk | Mitigation |
|---|---|
| Auto-positioning produces ugly layouts | Skill is additive only — doesn't move existing nodes. User repositions by hand after capture. Heuristic improves over time. |
| Predecessor inference is wrong | Surface ambiguity to user when confidence is low. Allow `--predecessor` override. Log inference reasoning to a `.capture-log.md` for audit. |
| The agent/user color distinction is subtle in Obsidian | Prefix node text with `[AGENT]:` or `[USER]:` in addition to color. Belt-and-suspenders so the distinction never blurs. |
| Schema drift between hand-built and skill-built canvases | `lib/schema.py` validates on every write. Surfaces diffs against canon. User can opt into "loose mode" for hand-edited canvases. |
| The Scroggins prototype has idiosyncrasies that aren't really conventions | When in doubt about whether something is a convention vs. one-off, ask the user. Don't over-codify from a single prototype. |
| Sub-canvas linking creates orphan canvases over time | Phase 2 includes a `compose-sub-canvas` validation that the linked canvas exists. Periodic vault audit can flag broken links. |

---

## Interface to image-chase

comic-trace owns canvas writing. image-chase (and any future skill that produces sub-canvases) calls into comic-trace at run-time events; it never writes canvases directly.

### What image-chase produces

A well-formed iteration directory at `_trace/_iterations/<comic-slug>/<panel-id>/<timestamp>/`:

```
request-blast.md       # the user's input
run.yaml               # batches, prompts, params, refs, costs, time
decision-log.md        # every craft adaptation, refusal, surface decision
gen-batch-NN/          # one folder per batch
  gen-NN-MM.png
  contact-NN.png
  batch.yaml           # this batch's prompt, refs used, agent's categorization
notes.md               # picks, surprises (added at run end)
run.canvas             # MANAGED BY comic-trace, not image-chase
```

The format is documented in `_shared/iteration-directory-format.md`. comic-trace reads this directory; image-chase produces it.

### When image-chase calls comic-trace

The flow is **live append**, not one-shot at end. The sub-canvas exists from second one and grows event-by-event, like a chat history:

| Moment | image-chase action | Effect |
|---|---|---|
| Run start | `compose-sub-canvas --mode init` | Sub-canvas created with frame, status "active" |
| Run start | `link-sub --status active` | Main canvas gains link node, marked active |
| Each batch return | `compose-sub-canvas --mode append --event batch` | Batch cluster added (gens, prompt, contact sheet, categorization) |
| Surface decision | `compose-sub-canvas --mode append --event surface` | Annotation noting why surfaced |
| Refusal | `compose-sub-canvas --mode append --event refusal` | Refusal node, immediately so wall is visible |
| Craft adaptation | `compose-sub-canvas --mode append --event adaptation` | Adaptation annotation with before/after prompt |
| User picks a gen | `compose-sub-canvas --mode append --event pick` | Pick edge from gen |
| User redirects | `compose-sub-canvas --mode append --event user-direction` | User-input annotation |
| Run end | `compose-sub-canvas --mode finalize` | Summary node, status flipped to "complete" |
| Run end | `link-sub --status complete` | Main canvas link updated to default treatment + completion timestamp |

The user can open the sub-canvas at any moment of the run and see current state. They can also see, from the main provenance canvas, that a fix run is *currently active* (orange link) vs. completed (default).

If image-chase crashes mid-run, the sub-canvas survives at last-append state. The status node still says "active" but no events arrive — the user can recover or restart with full visibility into where the run died.

### Why this design

Three things follow from the live-append shape:

1. **The user can lean on it being there.** The sub-canvas is never "in the agent's head until done" — it's always on disk, openable, complete to the moment.
2. **Failure modes are visible.** Crashes and stalls don't lose work or hide state.
3. **comic-trace is the canvas authority.** image-chase doesn't know schema details. If schema evolves, only comic-trace updates. Future skills (audio-transcript, external-feedback-import) plug into the same `compose-sub-canvas` interface.

---

## References

Source material in this vault:
- Prototype canvas: `_trace/2026-04-22-scroggins-manson-comic-provenance.canvas`
- Companion design: `_system/_design/image-chase-skill-design.md`
- Origin exchange: `_trace/_notes/2026-04-29-canvas-read-exchange.md`
- Existing vault skills as pattern reference: `_system/_skills/` (atomize, hold, reflect, trace, frame-read)
