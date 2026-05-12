---
type: skill-spec
command: /comic-trace compose-sub-canvas
phase: 2
created: 2026-05-01
tool: _system/_tools/comic-trace/compose_sub_canvas.py
---

# /comic-trace compose-sub-canvas

Maintains a live sub-canvas at `<iter-dir>/run.canvas` that grows event-by-event during an image-chase run. The canvas exists from second one (after `--mode init`) and is atomic-write-safe — the user can open it at any moment without seeing a corrupt file.

**Called by image-chase, not by the user directly.** If you're implementing image-chase, this is your interface to comic-trace's canvas layer.

---

## --mode init

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode init <iter-dir> \
  [--request-blast <vault-rel-path>] \
  [--refs <path1> <path2> ...]
```

Creates `<iter-dir>/run.canvas` with:
- Three lane labels (ARTIFACTS, TRANSITIONS, ANNOTATIONS)
- Legend node (upper-left)
- Request-blast file node (upper-left, below legend) — auto-detected at `<iter-dir>/request-blast.md`
- Ref file nodes in ARTIFACTS lane (from `--refs` list)
- Status node (prominent, above lanes) marked ACTIVE + start time

Fails if the canvas already exists. Call once at run start.

---

## --mode append

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode append --event <type> <iter-dir> [event params]
```

Appends nodes/edges for one event. Atomic write on every call.

### --event batch

Reads `<iter-dir>/gen-batch-NN/batch.json` and renders the batch cluster.

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode append --event batch <iter-dir> \
  --batch-num 1
```

**What lands on the canvas:**
- Group node (labeled "Batch 01") in TRANSITIONS lane
- Gen file nodes inside the group (2-column grid), colored by category:
  - green = pass, yellow = surprise, orange = refusal, no color = miss/partial
- Prompt text node above the group (`[AGENT]:` prefix)
- Contact sheet file node to the right of the group (if present in batch.json)
- Categorisation summary text node below the group

### --event surface

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode append --event surface <iter-dir> \
  --reason "3 survivors — surfacing contact sheet" \
  [--batch-num 3]
```

Adds an annotation node in ANNOTATIONS lane explaining why the loop surfaced.

### --event adaptation

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode append --event adaptation <iter-dir> \
  --before "Charles Manson" \
  --after "slight dark-eyed magnetic gaunt figure" \
  --reason "likeness refusal on explicit name" \
  [--batch-num 3]
```

Logs a craft adaptation with before/after prompt change.

### --event refusal

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode append --event refusal <iter-dir> \
  --batch-num 3 --gen-id 04 \
  --response "I can't generate images of real people in this context."
```

Adds an orange `[REFUSAL]` node immediately so the wall is visible in real time.

### --event pick

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode append --event pick <iter-dir> \
  --gen-node-id gen-03-02
```

Adds a "USER PICK" text node directly below the chosen gen, edged from it.
The gen node ID format is `gen-NN-MM` (batch number, gen index within batch).

### --event user-direction

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode append --event user-direction <iter-dir> \
  --note "Push harder on the eyeline — Charlie must be looking UP and across"
```

Adds a `[USER]: DIRECTION` annotation in ANNOTATIONS lane.

---

## --mode finalize

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode finalize <iter-dir> \
  [--cost-usd 0.23] \
  [--time-elapsed "18 min"] \
  [--summary "2 strong passes on P3. Charlie eyeline landed B04. Style consistent."]
```

- Flips status node from ACTIVE → COMPLETE (removes orange color, adds finish time)
- Adds a summary node (cost, elapsed, summary text) after the last batch

---

## --mode mark-stale

Recovery command for a run that crashed with status still ACTIVE.

```bash
python3 _system/_tools/comic-trace/compose_sub_canvas.py \
  --mode mark-stale <iter-dir>
```

Flips status node to STALE (yellow). Does not touch other nodes.

---

## Layout

Sub-canvas uses the same schema as the main provenance canvas:

| Lane | Content |
|---|---|
| ARTIFACTS (y=0) | Ref images used in the run |
| TRANSITIONS (y=1000) | Generation batches (group clusters, left-to-right) |
| ANNOTATIONS (y=-600) | Surface decisions, refusals, adaptations, user directions |

Status node is positioned above all lanes (y=-1500), always visible.

---

## Failure mode

If image-chase crashes mid-run, the sub-canvas survives at last-append state.
Status node still reads ACTIVE but timestamps reveal the silence.
Use `--mode mark-stale` for explicit recovery.
