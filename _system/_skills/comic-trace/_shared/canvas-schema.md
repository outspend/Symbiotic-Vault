---
type: reference
name: canvas-schema
created: 2026-04-30
canonical-prototype: _trace/2026-04-22-scroggins-manson-comic-provenance.canvas
---

# Canvas schema

Conventions formalized from the Scroggins/Manson prototype canvas.
All skill-generated canvases conform to this schema.
`lib/schema.py` enforces structural validity on every write.

---

## Lanes

Horizontal bands, labeled with text nodes at x=-1700:

| Lane | y-center | Contents |
|---|---|---|
| ANNOTATIONS | -600 | Observations, wishes, alerts, agent notes |
| ARTIFACTS | 0 | Vault files: journals, scripts, images, sub-canvases |
| TRANSITIONS | 1000 | External process steps: ChatGPT sessions, hold runs |

Process flows left-to-right within and across lanes.
The skill appends new nodes to the right edge of their lane.
Users reposition manually after capture — layout is approximate.

---

## Node types

| Type | When used | Color |
|---|---|---|
| `file` | Vault artifact with a clickable path | see Colors below |
| `text` | Annotation, transition note, lane label, legend | see Colors below |
| `link` | External URL (e.g. ChatGPT share link) | none |
| `group` | Labeled cluster of related nodes | none |

---

## Colors (Obsidian canvas color values)

| Color value | What it means | User's name |
|---|---|---|
| *(no field)* | Vault file that exists and is clickable | cyan |
| `"2"` | External / to import / process step | orange |
| `"1"` | Annotation — observation, wish, alert | "purple" in legend |
| `"6"` | Iteration artifact / in-progress marker | — |

Agent annotations use color `"1"` (same as user) plus a `[AGENT]:` prefix.
This is belt-and-suspenders: color is subtle, prefix is not.

---

## Edge conventions

Edges have no required color. Labels are optional but encouraged.

| Connection | fromSide | toSide | Typical label |
|---|---|---|---|
| Within-lane predecessor | right | left | (descriptive) |
| Cross-lane (artifact → annotation) | top | bottom | (descriptive) |
| Iteration | right | left | `rewrite`, `cleaner`, `1`, `2`, ... |

---

## Required frame elements (init creates these)

Every comic canvas must have:
- Three lane label text nodes (ids: `lane-artifacts`, `lane-transitions`, `lane-annotations`)
- One legend node (id: `legend`)

---

## Validation modes

- **strict** (default on writes): checks node types, required fields, edge references
- **lenient** (adopt command): accepts idiosyncratic positioning and custom clusters
