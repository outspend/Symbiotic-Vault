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

The vault has two layers. The raw layer (`_journal/`, `_inbox/`,
`_reflection/`) is where ideas first appear. The structured layer (`_atoms/`, `_frames/`, `_projects/`)
is where they develop, connect, and get used. The **atomize** skill bridges
them. Frames and projects read the structured layer and chase provenance
links back to raw material when needed — they do not read the raw layer
directly.

### The Collaboration Model

The vault supports two modes of interaction:

**Skill invocations** (atomize, tend, frame-read, reflect) maintain the
vault's health. Atomize, tend, and frame-read maintain structure. Reflect
maintains the agent's familiarity with the human's thinking — it is the
agent's own daily reading practice. All are documented in `_system/_skills/`.

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

The vault's linked, browsable quality emerges from six surfaces:

| Surface | Who writes | Who reads | What it holds |
|---|---|---|---|
| `_journal/` | Human | Agent (read-only) | Immutable daily journals |
| `_projects/*/notes/` and `drafts/` | Human | Agent (read-only) | Brainstorming and composed writing |
| `_atoms/` | Agent | Human (browse) | Single-concept notes, wikilinked |
| `_reflection/` | Agent | Human (browse) | Agent's daily journal — developing perspective |
| `_memory/` | Agent | Human (browse) | Operational records: skill logs, provenance traces |
| `.canvas` files | Agent (on demand) | Human | Visual maps of traced arguments |

Obsidian's graph view renders all wikilinks regardless of which file
contains them. The graph's density grows from agent activity in `_atoms/`
and `_memory/`. The user's writing stays clean. The vault's linked quality
is a byproduct of collaboration, not a manual authoring burden.

**The agent never writes into human surfaces. The system never requires
the human to link.**

### Full Surface Map

```
Shared input layer:
  _journal/    — the human's unmediated voice (one voice, one day)
  _inbox/      — correspondence (external, agent, and user replies)

Human writes here:          Agent never modifies these
  _journal/                  (daily journals)
  _projects/*/notes/        (brainstorming per division)
  _projects/*/drafts/       (composed writing)

Agent maintains here:       Human browses, never edits
  _atoms/                   (single-concept notes, wikilinked)
  _reflection/              (agent's daily journal — developing perspective)
  _memory/                  (operational: skill logs, provenance traces)
  _frames/ (proposed)       (frame proposals from tend)

Shared:
  HOME.md                   (human zones + agent-refreshable zones)
  _frames/ (active)         (user-created or user-activated)
  _projects/*/brief-[slug].md  (user-written, agent helps draft)

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
│   │   ├── frame-read.md
│   │   ├── reflect.md
│   │   └── trace.md
│   └── _templates/
│       ├── atom.md
│       ├── canvas.canvas
│       ├── capture.md
│       ├── draft.md
│       ├── frame.md
│       ├── journal.md
│       ├── project-brief.md
│       └── project-note.md
├── _inbox/                  # Raw capture — quick ideas, links, clippings
├── _journal/                 # Daily journals — timestamped, immutable
│   └── YYYY-MM-DD.md
├── _atoms/                  # Single-concept notes (the zettelkasten)
├── _reflection/             # Agent's daily journal — raw, developing perspective
│   └── YYYY-MM-DD.md
├── _frames/                 # Perspective definitions (lenses, not territories)
├── _projects/               # Active + completed works
│   └── project-name/
│       ├── brief-[slug].md  # Intent, audience, divisions, status
│       ├── notes/           # Generative thinking per division (human surface)
│       └── drafts/          # Composed writing per division (human surface)
└── _memory/                 # Operational: skill run logs, provenance traces
```

### Folder Contracts

**`_inbox/`** — The vault's mailbox. Correspondence from any voice
other than the human's unmediated journal writing: external captures
(articles, links, clippings), collaborator feedback, agent-mediated
notes from collaboration sessions, and the human's replies to agent
output. The journal is for the human's own voice. The inbox is where
voices mix.

Items may include optional frontmatter:
- `subtype:` feedback | reference | capture
- `from:` person-name | agent | user
- `responds_to:` path to the file being responded to

All fields are optional. Atomize infers what it can from content
when frontmatter is absent. After processing, the original remains
(never deleted) with `processed: true` added to frontmatter.

**`_journal/`** — Daily journals. One file per day, named `YYYY-MM-DD.md`.
Immutable after the day passes. Atomize reads these but never modifies
them. The journal is the permanent record of when and how ideas appeared.

**`_atoms/`** — Single-concept notes. Every atom has frontmatter
conforming to the Atom Schema. Atoms link to each other via wikilinks
and carry provenance links back to their source (journal entry, inbox
item, project draft, or another atom).

`_index.md` — a frame-grouped summary of all atoms, maintained by
tend. One line per atom: `id | kind | one-sentence summary`. Used by
reflect for efficient discovery. Regenerated on every tend run.

The index is regenerated from scratch on every tend run. Between
runs it is eventually-consistent — new atoms created by atomize
will not appear until the next tend. Atomize, frame-read, and
reflect use the index as their primary entry point into the
atomic layer and should treat it as a high-quality hint, not a
guarantee. When the index is stale or absent, skills fall back
to reading atoms directly and flag the gap in their memory entry.

Tend should run before other skills when the vault has been
heavily modified, to ensure the index reflects current state.

**`_frames/`** — Perspective definitions. Each frame describes a lens:
its concerns, vocabulary, what it pays attention to, what it questions.
Frames do not own content — they produce distinct traced paths through
the atomic layer, each path current as of the date it's run. The same
atoms light up differently through different frames. Frames may be
created by the user or proposed by the tend skill.

**`_projects/`** — Active trajectories toward specific works. Each project
has three components:
- `brief-[slug].md` — defines intent, audience, and divisions
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

**`_reflection/`** — Agent's daily journal. One file per day, named
`YYYY-MM-DD.md`. Immutable after the day passes. Prose, not structured —
the agent references atoms, journal entries, and projects naturally in
text, not through formal wikilinks. Reflections are raw layer, the same
way `_journal/` is. Atomizable at user's discretion. The agent's
understanding of the human's thinking develops through accumulated
reflections, not through graph structure.

**`_memory/`** — Operational records. Skill run logs from atomize, tend,
and frame-read. Provenance traces from conversational collaboration.
Tagged by source skill/mode, frame (if applicable), and date. This is
the operational trail — what the agent did, not what the agent thinks.
The agent's own thinking lives in `_reflection/`.

---

## Schemas

### Atom Schema

```yaml
---
type: atom
id: unique-slug
aliases: []          # alternate names — prevents synonym splitting
kind: concept | claim | method | question | person | reference | event
status: seed | developing | stable | archived
created: YYYY-MM-DD
source:
  - journal/YYYY-MM-DD
  - inbox/item-name
tags: []
frames: []           # which frames have claimed or referenced this atom
---
```

Body contains prose. A `## Relations` section follows a `---` divider
at the end of every atom. Each entry: `[[wikilink]]: one sentence
describing the epistemic relationship (supports, challenges, extends,
instantiates, etc.)`. Tend appends to this section; atomize writes
initial entries at creation. Relations are human-readable and
structured enough to be parsed into typed graph edges later.

**`kind: concept` vs. `kind: claim`** — a concept is descriptive and
stable; a claim is positioned and arguable. Claims almost always
reference a concept and become two linked atoms.

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

### Draft Schema

```yaml
---
type: draft
project: project-slug
division: division-slug
status: wip | final
---
```

Body contains composed writing — the actual prose of the work. Human surface:
agent reads but never modifies. Nav header links to `brief-[slug]` and the
corresponding note. A draft reaches `status: final` when it's complete; when
all division drafts are final, the project brief status changes to `completed`.

### Project Note Schema

```yaml
---
type: project-note
project: project-slug
division: division-slug
---
```

Body contains generative thinking — brainstorming, explorations, reflections,
notes from agent collaboration. Human surface: agent reads but never modifies.
Notes inform drafts but do not become them; both remain as provenance.

### Memory Entry Schema

```yaml
---
type: memory
skill: atomize | tend | frame-read | collaboration
frame: frame-slug    # if applicable
date: YYYY-MM-DD
atoms_touched:
  - id: atom-slug
    action: created | reinforced | enriched | resolved | referenced | developed | challenged
    note: "optional — what was developed or challenged"
  - id: another-atom
    action: created
    uncertainty: "brief description of the doubt"
---
```

`atoms_touched` is optional and structured. Each entry requires `id` (the
atom's slug) and `action` (what kind of touch occurred). `created` is a
distinct structural birth event. All other actions are touches recorded
in memory: `referenced` is the baseline touch, while `reinforced`,
`enriched`, `developed`, `challenged`, and `resolved` add more specific
meaning from a particular skill's vantage point. The `uncertainty` field
is optional — present when the skill has a specific doubt about this
atom, absent when confident. The `note` field is optional and is most
useful for reflect's `developed` and `challenged` entries, where it
briefly describes what changed. This makes memory entries queryable by
atom via Dataview.

Skill ownership:
- `created` — atomize
- `reinforced` — atomize
- `enriched` — tend
- `developed` — reflect
- `challenged` — reflect
- `referenced` — any skill
- `resolved` — any skill

These actions are event labels when written and downstream coordination
signals when later skills read them.

Body contains the agent's operational observations or trace. Prose body
includes an **Uncertainties** section: judgments that could have gone
either way, borderline cases not acted on, flags not resolvable from
this skill's vantage point.

### Reflection Entry Schema

```yaml
---
type: reflection
date: YYYY-MM-DD
---
```

Body contains the agent's daily thinking — prose, developing,
naturally referencing. Ends with a `## Threads` section: 3–5 bullet
points the agent leaves itself about what it wants to keep tracking.

### Inbox Item Schema

```yaml
---
type: inbox
subtype: feedback | reference | capture
from:              # person or source name, if known
responds_to:       # journal entry or project file this responds to
created: YYYY-MM-DD
processed: false   # set to true by atomize when processed
---
```

`subtype` values:
- **feedback** — a response to the user's existing work. Atomize
  emphasizes enriching existing atoms over creating new ones.
- **reference** — external material (article, link, repo, post).
  Atomize extracts concepts and notes the external source.
- **capture** — the user's own thinking. Standard extraction.

All fields after `type` and `processed` are optional. Blank fields
have no technical cost. External tools (clippers, web capture) can
auto-fill `subtype` and `from`. Quick thoughts can leave everything
blank except `created` and `processed`. Atomize fills inferrable
blank fields when marking an item processed.

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

### Reflection Boundaries

The reflect skill can read outward into the vault — atoms, projects,
frames, prior reflections — following threads from the daily journal.
But other skills do not read inward to `_reflection/`.

- **Reflect reads out:** journal, inbox, atoms, projects, frames,
  prior reflections. It follows where the material points.
- **Other skills stay out:** atomize reads human surfaces only
  (_journal/, _inbox/). Tend reads the structured layer and human
  surfaces. Frame-read reads atoms and memory. None of them read
  `_reflection/`.

**Rationale:** Reflections are the agent's own developing thread —
raw, personal, accumulating. If atomize harvested from reflections,
the structured layer would increasingly reflect the agent's own
outputs rather than the human's thinking. The human's inbox curation
is the deliberate bridge: when a reflection produces something
worth structuring, the human grabs it and puts it in `_inbox/`.
This keeps the human as gatekeeper for what enters the raw-to-
structured pipeline, preventing the agent from feeding itself.

`_reflection/` joins the surface map as:

```
Agent maintains here:
  _atoms/              (structured layer)
  _memory/             (skill traces, collaboration logs)
  _reflection/         (agent's journal — daily reading practice)
  _frames/ (proposed)  (frame proposals from tend)
```

### Cross-Skill Awareness

Skills do not operate in isolation. Each reads the most recent
memory entry from every other skill as part of its seed context.
This creates a lightweight shared awareness:

- Atomize knows what tend flagged and what reflect is tracking
- Tend knows what atomize was uncertain about and what frame-read surfaced
- Frame-read knows what tend enriched and what atomize extracted
- Reflect knows what all structural skills did recently, and
  synthesizes this with the human's journal

The mechanism is memory entries — the agent's own notes. No skill
reads another skill's inputs or modifies another skill's outputs
directly. They read the published notes and act on what they find.

Memory is read at two tiers. The latest entry from each skill is
read in full for narrative context (the cross-skill seed).
Historical entries are scanned via frontmatter (`atoms_touched`)
when a specific question arises — which atoms were flagged, when
they were last touched, what uncertainties remain. This keeps the
default reading cost low while making the full memory archive
addressable.

The reflect skill carries the longitudinal view through its
Threads section, noticing patterns across multiple runs that no
single skill invocation would catch.

**Tier 1: Frontmatter scan.** Fast, broad, queryable. Read just the
YAML frontmatter of memory entries to see what was touched, when,
by whom, and what was uncertain. Use cases: tend checking if an
atom has been flagged before; reflect verifying a pattern; trace
assembling provenance.

**Tier 2: Full prose read.** Slow, deep, contextual. Read the
complete memory entry for full reasoning and nuance. Use cases:
the cross-skill seed (latest entry per skill, read in full every
run); following up when tier 1 surfaces a relevant uncertainty.

Default: every skill reads the latest entry from each other skill
at tier 2. Historical entries accessed at tier 1 only when a
specific question arises.

Note: reflect reads other skills' memory entries but other skills
do not read `_reflection/`. The one-way boundary holds. The
human's inbox curation remains the deliberate bridge from
reflection into the structural pipeline.

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

If the access tier described here conflicts with a skill's
`access_summary` or the protocol's read sequence, the skill
definition is authoritative for that skill's behavior. The
design document describes the system of tiers. Each skill
declares its own access within that system.

---

## Structural Principles

1. **One pool, many lenses.** Ideas exist once in `_atoms/`. Frames
   provide perspectives. Projects provide trajectories. No idea is
   owned by a single context.

2. **Raw and structured are distinct layers.** The journal, inbox, and
   agent reflections are permanent raw records. Atoms are the structured
   layer. Atomize bridges them. Everything else reads the structured layer.

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

8. **Research-informed schema choices.** The atom schema includes
   `aliases` for entity resolution, `claim` as a kind to capture
   arguable positions alongside descriptive concepts, and a
   `## Relations` section where epistemic relationships are described
   in natural language. These choices are informed by discourse graph
   research (Joel Chan), Knowledge Synthesis Graphs, and argumentation
   theory. They preserve the option for typed-edge graph integration
   later without requiring that infrastructure now. The vault's
   deliberate asymmetry — human writes prose, agent maintains graph,
   tend bridges with judgment — is a design choice, not a limitation.
   Research confirms bidirectional sync remains an unsolved problem;
   loose coupling via LLM judgment is better suited to a single
   creative practitioner.

9. **Skills learn from each other through memory.** Every skill
   writes a memory entry including uncertainty flags. Every skill
   reads the most recent memory entries from other skills before
   it runs. When one skill's uncertainty is resolved by another
   skill's evidence, the resolution happens naturally — no review
   step, no audit, no human intervention required for structural
   matters. The agent maintains the structured layer's health
   through parallax: the same material seen from multiple skill
   vantages reveals what any single vantage misses.

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

---


