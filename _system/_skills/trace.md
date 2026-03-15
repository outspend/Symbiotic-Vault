---
type: skill
id: trace
version: 0.1
status: provisional — revise after first use
trigger: on-request
access_summary:
  _atoms: read
  _frames: read
  _journal: read (via provenance links)
  _projects: read (briefs, notes, drafts)
  _memory: read + add
  _projects: add (.canvas files)
---

# Skill: Trace

Generate an Obsidian `.canvas` file that visually maps atoms,
connections, and provenance paths.

## Purpose

Make the vault's linked structure visible as a spatial artifact.
A trace is a dated snapshot of a specific inquiry — a question,
a project, a frame's view, a path between ideas. The series of
traces over time is its own provenance record.

## Status

This is a provisional skill definition. The procedure below
captures what we know. It will be rewritten after the first
several uses reveal what works, what's missing, and what the
common invocation patterns actually are.

## Invocation Patterns

The user may ask for a trace in several forms:

- **"Map this atom"** — center on one atom, show its connections
- **"Map this project"** — show all atoms relevant to a project's
  notes and drafts
- **"Map this through [frame]"** — filter the graph by a frame's
  concerns and vocabulary
- **"Map the path from X to Y"** — trace a specific route through
  the atomic layer
- **"Map the table arrangements"** — visualize proposed sequences
  from a table experiment (see THE_TABLE.md)

## Scope

**Reads:**
- `_atoms/` — for nodes and their relations sections
- `_frames/` — if a frame is named, for filtering and emphasis
- `_journal/` — via provenance links from atoms, for source context
- `_projects/` — briefs, notes, drafts, for project-scoped traces
- `_memory/` — past traces and reflections for continuity

**Writes:**
- `.canvas` file to the relevant project folder or `_memory/`
- Named by date and topic: `YYYY-MM-DD-topic-slug.canvas`
- Memory entry in `_memory/` logging what was traced and why

## Canvas Format

Obsidian canvas files are JSON:

```json
{
  "nodes": [
    {
      "id": "unique-id",
      "type": "file",
      "file": "_atoms/highlights-and-hides.md",
      "x": 0, "y": 0,
      "width": 400, "height": 200
    },
    {
      "id": "unique-id-2",
      "type": "text",
      "text": "Annotation or rationale in markdown",
      "x": 500, "y": 0,
      "width": 300, "height": 150
    }
  ],
  "edges": [
    {
      "id": "edge-id",
      "fromNode": "unique-id",
      "toNode": "unique-id-2",
      "label": "relationship description"
    }
  ]
}
```

**Use `type: "file"` for atoms and drafts** — clicking opens the
actual file in Obsidian.

**Use `type: "text"` for annotations** — rationale, frame
observations, provenance notes, relationship descriptions.

**Edge labels** should be drawn from the atoms' `## Relations`
sections where possible.

## Layout Guidance (Provisional)

- Central node for the focal atom or inquiry
- Connected atoms radiating outward by relevance
- Provenance sources (journal entries) at the periphery
- Frame annotations as smaller text cards near the atoms they
  comment on
- For sequence traces (table arrangements): linear layout, top
  to bottom or left to right, with Needs/Leaves annotations on
  the edges between fragments

## Judgment Calls

- **Density:** Don't map everything. A trace that shows 50 atoms
  is a mess, not a map. Show what's relevant to the specific
  inquiry. 8-15 nodes is usually the right range.
- **Annotation:** Every trace should have at least one text node
  explaining what the trace is *about* — the question it answers,
  the frame it applies, the date and context.
- **Naming:** Filenames should be descriptive enough to distinguish
  traces at a glance: `2026-03-10-epistemic-literacy-cluster.canvas`,
  not `trace-1.canvas`.
