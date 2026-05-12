---
type: skill
name: comic-trace
version: 1.1-phase2
created: 2026-04-30
updated: 2026-05-01
status: active
phase: 2
design: _system/_design/comic-trace-skill-design.md
---

# Comic-trace skill

Maintains a provenance canvas for a comic-making process.

## What it does

Captures vault artifacts (journals, hold reflections, inbox scripts, images) as nodes on a `.canvas` file, edges them to their predecessors, places them in the right lane, and distinguishes user annotations from agent annotations.

## Phase 1 sub-commands

| Command | Python tool | Description |
|---|---|---|
| `init <slug>` | `init.py` | Create a new comic canvas |
| `capture <type> <source>` | `capture.py` | Add an artifact node |
| `annotate <target>` | `annotate.py` | Add an annotation node |
| `adopt <path> --as-slug <slug>` | `adopt.py` | Register an existing canvas |

## Invocation (from vault root)

```bash
python3 _system/_tools/comic-trace/init.py <slug>
python3 _system/_tools/comic-trace/capture.py <type> <source> [options]
python3 _system/_tools/comic-trace/annotate.py <target> [options]
python3 _system/_tools/comic-trace/adopt.py <path> --as-slug <slug>
```

## Read before using

- `_shared/canvas-schema.md` — lane/color/edge conventions
- `_shared/artifact-types.md` — per-type capture behavior
- `_shared/lane-conventions.md` — layout heuristics and their limits
- The prototype: `_trace/2026-04-22-scroggins-manson-comic-provenance.canvas`

## Phase 2 sub-commands

| Command | Python tool | Description |
|---|---|---|
| `compose-sub-canvas --mode init` | `compose_sub_canvas.py` | Create sub-canvas for a fix run |
| `compose-sub-canvas --mode append --event <type>` | `compose_sub_canvas.py` | Append batch/surface/refusal/adaptation/pick/user-direction event |
| `compose-sub-canvas --mode finalize` | `compose_sub_canvas.py` | Flip status to complete, add summary |
| `compose-sub-canvas --mode mark-stale` | `compose_sub_canvas.py` | Recovery: mark crashed run |
| `link-sub <sub-canvas> --status active\|complete` | `link_sub.py` | Attach sub-canvas to main canvas |

See `link-sub.md`, `compose-sub-canvas.md`, and `_shared/iteration-directory-format.md`.
