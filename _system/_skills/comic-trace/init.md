---
type: skill-spec
command: comic-trace init
phase: 1
---

# /comic-trace init

```
python3 _system/_tools/comic-trace/init.py <slug> [--from-prototype <path>]
```

Creates `_trace/<slug>-provenance.canvas` with:
- Three lane label text nodes (ARTIFACTS, TRANSITIONS, ANNOTATIONS) at x=-1700
- A legend node at upper-left

Registers `<slug>` → canvas path in `_system/_tools/comic-trace/registry.yaml`.

Exits with an error if the canvas already exists; use `adopt` to register an existing canvas.

**Example:**
```bash
python3 _system/_tools/comic-trace/init.py scroggins-manson
```
