---
type: system
purpose: vault architecture reference
access: user-invoked only — no agent reads this during normal operation
created: 2026-03-10
updated: 2026-03-10
---

# Vault Design Reference

This document describes the full architecture of the vault. It is not read
by any agent during normal operation. It exists for design sessions when the
user wants to review or modify the vault's structure.

---

## Architecture Overview

The vault is organized around a single pool of atomic concepts traversed
by multiple frames (perspectives). There are no domain boundaries. Ideas
exist once and are seen differently through different lenses.

### Core Lifecycle

```
_inbox/ ─────┐
              ├──→ atomize ──→ _atoms/ (status: seed)
_journal/ ────┘                    │
                                  ├──→ tend ──→ enriched atoms
                                  │             proposed frames
                                  │
                                  ├──→ frame-read ──→ _memory/ (reflections)
                                  │
                                  ├──→ you ──→ _projects/ (active trajectory)
                                  │                │
                                  │                └──→ completes in place
                                  │                     (all drafts → final)
                                  │
                                  └──→ tend ──→ harvests new atoms from
                                                 project notes and drafts
```

### Key Distinction: Raw vs. Structured

The vault has two layers. The raw layer (`_journal/`, `_inbox/`) is where
ideas first appear. The structured layer (`_atoms/`, `_frames/`, `_projects/`)
is where they develop, connect, and get used. The **atomize** skill bridges
them. Frames and projects read the structured layer and chase provenance
links back to raw material when needed — they do not read the raw layer
directly.

### The Collaboration Model

The vault supports two modes of interaction:

**Skill invocations** (atomize, tend, frame-read) maintain the vault's
structural health. They are documented in `_system/_skills/`.

**Conversational collaboration** is the primary way the vault helps the
user think. The user brings a piece of writing — a draft, a journal entry,
a question — and asks the agent to engage with it using the full context
of the atomic layer. The agent responds by matching the content semantically
against `_atoms/`, producing a grounded response citing specific atoms and
connections, and writing a densely wikilinked trace to `_memory/`.

This is not a skill. It happens on demand, every time the user brings
content and asks a question.

---

## Vault Surfaces

The vault's linked, browsable quality emerges from five surfaces:

| Surface | Who writes | Who reads | What it holds |
|---|---|---|---|
| `_journal/` | Human | Agent (read-only) | Immutable daily journals |
| `_projects/*/notes/` and `drafts/` | Human | Agent (read-only) | Brainstorming and composed writing |
| `_atoms/` | Agent | Human (browse) | Single-concept notes, wikilinked |
| `_memory/` | Agent | Human (browse) | Traces, reflections, collaboration records |
| `.canvas` files | Agent (on demand) | Human | Visual maps of traced arguments |

Obsidian's graph view renders all wikilinks regardless of which file
contains them. The graph's density grows from agent activity in `_atoms/`
and `_memory/`. The user's writing stays clean. The vault's linked quality
is a byproduct of collaboration, not a manual authoring burden.

**The agent never writes into human surfaces. The system never requires
the human to link.**

### Full Surface Map

```
Human writes here:          Agent never modifies these
  _journal/                  (daily journals)
  _projects/*/notes/        (brainstorming per division)
  _projects/*/drafts/       (composed writing)

Agent maintains here:       Human browses, never edits
  _atoms/                   (single-concept notes, wikilinked)
  _memory/                  (traces, reflections, collaboration records)
  _frames/ (proposed)       (frame proposals from tend)

Shared:
  HOME.md                   (human zones + agent-refreshable zones)
  _frames/ (active)         (user-created or user-activated)
  _projects/*/_BRIEF.md     (user-written, agent helps draft)

Generated on demand:
  .canvas files             (visual maps from conversational collaboration)

Future extension points (not built):
  _exhibits/                (public presentation layer / web surface)
```

---

## Directory Structure

```
vault/
├── HOME.md                  # Human dashboard — orientation and navigation
├── _system/
│   ├── VAULT_VISION.md      # Pillars and principles (read by user, boot context)
│   ├── VAULT_DESIGN.md      # This file (user design sessions only)
│   ├── AGENT_PROTOCOL.md    # Universal agent mechanics
│   ├── _skills/
│   │   ├── atomize.md
│   │   ├── tend.md
│   │   └── frame-read.md
│   └── _templates/
│       ├── atom.md
│       ├── canvas.canvas
│       ├── draft.md
│       ├── frame.md
│       ├── project-brief.md
│       └── project-note.md
├── _inbox/                  # Raw capture — quick ideas, links, clippings
├── _journal/                 # Daily journals — timestamped, immutable
│   └── YYYY-MM-DD.md
├── _atoms/                  # Single-concept notes (the zettelkasten)
├── _frames/                 # Perspective definitions (lenses, not territories)
├── _projects/               # Active + completed works
│   └── project-name/
│       ├── _BRIEF.md        # Intent, audience, divisions, status
│       ├── notes/           # Generative thinking per division (human surface)
│       └── drafts/          # Composed writing per division (human surface)
└── _memory/                 # Run logs, reflections, collaboration traces
```

### Folder Contracts

**`_inbox/`** — Loose capture. No required format. Items here await
atomization. After processing, the original remains (never deleted)
with a `processed: true` flag added to frontmatter if it has any,
or as-is if it's just raw text.

**`_journal/`** — Daily journals. One file per day, named `YYYY-MM-DD.md`.
Immutable after the day passes. Atomize reads these but never modifies
them. The journal is the permanent record of when and how ideas appeared.

**`_atoms/`** — Single-concept notes. Every atom has frontmatter
conforming to the Atom Schema. Atoms link to each other via wikilinks
and carry provenance links back to their source (journal entry, inbox
item, project draft, or another atom).

**`_frames/`** — Perspective definitions. Each frame describes a lens:
its concerns, vocabulary, what it pays attention to, what it questions.
Frames do not own content — they produce distinct traced paths through
the atomic layer, each path current as of the date it's run. The same
atoms light up differently through different frames. Frames may be
created by the user or proposed by the tend skill.

**`_projects/`** — Active trajectories toward specific works. Each project
has three components:
- `_BRIEF.md` — defines intent, audience, and divisions
- `notes/` — generative thinking per division (brainstorming, explorations
  with the agent, reflections)
- `drafts/` — composed writing per division (actual prose becoming the work)

Notes inform drafts but do not become them. Both are human surfaces — the
agent reads them for harvesting but never modifies them. When the user asks
for provenance ("show me the path to this draft"), the agent traces
connections live from `_memory/` and the atomic layer.

**Project completion** — a project completes in place. When all division
drafts reach `status: final`, the brief's `status` changes to `completed`
and `completed:` date is set. The finished work is the final state of the
`drafts/` folder — nothing moves anywhere.

**`_memory/`** — Agent output. Reflections from frame-read, traces from
tend, collaboration records from conversational interactions. Tagged by
source skill/mode, frame (if applicable), and date. This is the provenance
trail for all agent activity and the substrate from which lineage is
assembled when a project completes.

---

## Schemas

### Atom Schema

```yaml
---
type: atom
id: unique-slug
kind: concept | method | question | person | reference | event
status: seed | developing | stable | archived
created: YYYY-MM-DD
source:
  - journal/YYYY-MM-DD
  - inbox/item-name
tags: []
frames: []           # which frames have claimed or referenced this atom
---
```

Body contains prose and `[[wikilinks]]` to other atoms.

### Frame Schema

```yaml
---
type: frame
id: frame-slug
status: active | proposed | retired
created: YYYY-MM-DD
proposed_by: user | tend
seed_atoms: []       # atoms that prompted this frame's creation
---
```

Body contains: perspective description, concerns, vocabulary,
what this frame pays attention to, what it questions.

### Project Brief Schema

```yaml
---
type: project
id: project-slug
status: active | paused | completed
created: YYYY-MM-DD
completed:           # set when all division drafts reach final status
---
```

Body contains: intent, audience, divisions (named sections with scope),
open decisions, current focus. A completed project's finished work is
the final state of its `drafts/` folder.

### Memory Entry Schema

```yaml
---
type: memory
skill: atomize | tend | frame-read | collaboration
frame: frame-slug    # if applicable
date: YYYY-MM-DD
---
```

Body contains the agent's observations, reflections, or trace.

---

## Agent Model

### Current: Claude Code (single agent, multiple skills)

Claude Code reads `AGENT_PROTOCOL.md` on every invocation.
It then reads the relevant skill definition for the requested task.
For frame-read, it also reads the relevant frame definition.

Claude Code does not read `VAULT_DESIGN.md` or `VAULT_VISION.md`
during normal operation. It sees only the protocol and the skill.

### Future: Multi-Agent (nanoclaw, openclaw, etc.)

When multi-agent systems become viable, each frame can become a
full agent persona with persistent memory built from its accumulated
reflections in `_memory/`. The skill definitions become shared
capabilities. The protocol becomes a base class that specialized
agents extend. Nothing in the current design forecloses this.

---

## Access Tiers

Every skill declares an access tier for each resource it touches:

- **read** — observe only, no modifications
- **summarize** — write to designated summary spaces (_memory/, HOME.md
  agent zones). No files created in content folders, no existing
  content changed.
- **add** — everything summarize allows, plus creating new files with
  `status: seed` or `status: draft`. Existing files untouched.
- **modify** — everything add allows, plus updating frontmatter,
  adding links, changing status fields in existing files.

---

## Structural Principles

1. **One pool, many lenses.** Ideas exist once in `_atoms/`. Frames
   provide perspectives. Projects provide trajectories. No idea is
   owned by a single context.

2. **Raw and structured are distinct layers.** The journal and inbox are
   permanent raw records. Atoms are the structured layer. Atomize
   bridges them. Everything else reads the structured layer.

3. **Provenance is traced on demand, not maintained as a file.** When
   the user asks "show me the path to this chapter," the agent traces
   connections live from `_memory/` and the atomic layer. Lineage for
   finished works is assembled from atoms referenced across the project's
   memory traces. The trail is the treasure — but it lives in `_memory/`,
   not in a separate ledger.

4. **Human surfaces and agent surfaces are distinct.** The human writes
   freely without linking or tagging. The agent maintains the structured
   layer and produces linked, traced, argued responses on demand. The
   vault's hyperlinked quality is a byproduct of collaboration, not a
   manual authoring burden.

5. **Skills are a flat library.** No hierarchy, no inheritance. Each
   skill is self-contained with explicit scope and access.

6. **Access is explicit on every skill.** The vault can scale from
   manual invocation to autonomous routines without redesigning the
   schema.

7. **What isn't needed yet isn't built yet.** Public exhibition surfaces,
   graph databases, and multi-agent orchestration are noted as extension
   points, not requirements.

---

## Extension Points (Not Yet Built)

- **Graph database (Graphiti/Neo4j):** When the atomic layer is dense
  enough that file-based traversal becomes slow, the graph DB indexes
  what already exists. It doesn't create a parallel structure.

- **Web presence / Exhibits:** When works accumulate and a public
  surface is desired, an `_exhibits/` folder becomes the curation layer —
  which projects get shown, how provenance gets presented.

- **Multi-agent orchestration:** When frameworks like nanoclaw/openclaw
  mature, frames become agent personas, skills become shared tools,
  and the protocol becomes a base that specialized agents extend.

- **Autonomous scheduling:** Skills currently require human invocation.
  When trust and tooling allow, some skills (especially tend) could
  run on a schedule.
