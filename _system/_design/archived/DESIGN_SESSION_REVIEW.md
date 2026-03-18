---
type: system
purpose: design session review
created: 2026-03-11
---

# Design Session Review

Everything decided in this session, organized for review before
handing to Claude Code.

---

## The Core Insight

The human writes freely on their surfaces without linking or tagging.
The agent maintains the structured layer and produces linked, traced,
argued responses on demand. The vault's hyperlinked quality is a
byproduct of collaboration, not a manual authoring burden.

---

## Vault Structure

```
vault/
├── HOME.md                     # Human dashboard
├── _system/
│   ├── VAULT_VISION.md         # Pillars and principles
│   ├── VAULT_DESIGN.md         # Architecture reference (design sessions only)
│   ├── AGENT_PROTOCOL.md       # What the agent reads every invocation
│   ├── _skills/
│   │   ├── atomize.md
│   │   ├── tend.md
│   │   └── frame-read.md
│   └── _templates/
│       ├── atom.md
│       ├── frame.md
│       ├── project-brief.md
│       ├── project-note.md
│       └── draft.md
├── _journal/                   # Daily notes (your writing)
├── _inbox/                     # External captures (clippings, links, imports)
├── _atoms/                     # Single-concept notes (agent-maintained)
├── _frames/                    # Perspective definitions (lenses)
├── _projects/                  # Active trajectories toward finished work
│   └── project-name/
│       ├── _BRIEF.md           # Intent, audience, divisions with nav links
│       ├── notes/              # Generative thinking per division
│       └── drafts/             # Composed writing per division
└── _memory/                    # Agent traces, reflections, collaboration records
```

### What Was Removed
- `_works/` — projects complete in place, finished work is final drafts
- `_exhibits/` — deferred, future extension for public/web surface
- `_TRAIL.md` — provenance traced on demand, not maintained as a file

---

## Surfaces and Ownership

```
Human writes here:              Agent never modifies these
  _journal/                     (daily notes — your writing)
  _inbox/                       (external captures)
  _projects/*/notes/            (brainstorming per division)
  _projects/*/drafts/           (composed writing)

Agent maintains here:           Human browses, never edits
  _atoms/                       (single-concept notes, wikilinked)
  _memory/                      (traces, reflections, collaboration logs)
  _frames/ (proposed)           (frame proposals from tend)

Shared:
  HOME.md                       (human zones + agent-refreshable zones)
  _frames/ (active)             (user-created or user-activated)
  _projects/*/_BRIEF.md         (user-written, agent helps draft)

Generated on demand:
  .canvas files                 (visual maps from collaboration)
```

### The Surface Rule
- The agent never writes into human surfaces.
- The system never requires the human to link.
- The human may use wikilinks freely — they're convenient, not required.
- If the human links, the graph picks it up. If they don't, nothing breaks.

---

## Schemas

### Atom
```yaml
---
type: atom
id: unique-slug
aliases: []
kind: concept | claim | method | question | person | reference | event
status: seed | developing | stable | archived
created: YYYY-MM-DD
source:
  - journal/YYYY-MM-DD
  - inbox/item-name
tags: []
frames: []
---
```
Body: prose capturing the core idea, followed by a relations section.

A `concept` describes ("highlights and hides is a prompting method").
A `claim` asserts ("asking an LLM what a framing foregrounds and
conceals is a form of epistemic literacy"). Claims carry a position
and can be supported, opposed, refined. Writers assemble arguments
from claims. A claim almost always references a concept — these
become two linked atoms.

`aliases` records alternate names the same idea goes by. Atomize
checks aliases when matching. Tend adds aliases when it notices an
atom is referenced by different names. Standard in knowledge graphs;
makes future Graphiti integration easier.

The `## Relations` section lives below a divider after the main
prose. Each entry is a wikilink plus a sentence describing the
epistemic relationship in natural language:

```markdown
---
## Relations

- Connects to [[epistemic-literacy]]: this method is a specific
  practice within the broader concern
- Challenged by [[llm-common-topologies]]: the topologies suggest
  LLMs have default framings this method may not fully surface
```

Relations grow over time as tend discovers connections. The natural
language descriptions are readable by the human and parseable by a
future graph database into typed edges.

### Frame
```yaml
---
type: frame
id: frame-slug
status: active | proposed | retired
created: YYYY-MM-DD
proposed_by: user | tend
seed_atoms: []
---
```
Body: perspective, concerns, vocabulary, what it questions.

### Project Brief
```yaml
---
type: project
id: project-slug
status: active | paused | completed
form: essay | book | notebook | conversation | tbd
created: YYYY-MM-DD
completed: YYYY-MM-DD
---
```
Body: intent, audience, divisions (with nav links to notes/drafts),
open decisions, current focus.

### Project Note
```yaml
---
type: project-note
---
```
Body: freeform thinking about a division. No required links.

### Draft
```yaml
---
type: draft
status: wip | final
---
```
Body: composed writing. Your surface.

### Memory Entry
```yaml
---
type: memory
skill: atomize | tend | frame-read | collaboration
frame: frame-slug (if applicable)
date: YYYY-MM-DD
---
```
Body: agent's observations, densely wikilinked.

---

## Skills (3)

### Atomize
- **Trigger:** User invokes
- **Reads:** `_journal/`, `_inbox/`, existing `_atoms/` (including aliases)
- **Writes:** New atoms to `_atoms/` (status: seed), memory entry
- **Does not:** Modify journal entries or inbox items (ever)
- **Distinguishes** claims from concepts at creation time. A concept
  describes. A claim asserts. Both are valid atom kinds.
- **Writes initial relations** in the `## Relations` section when
  creating atoms — not just bare wikilinks but sentences describing
  how the new atom connects to existing atoms

### Tend
- **Trigger:** User invokes
- **Reads:** `_atoms/`, `_frames/`, `_projects/*/notes/`,
  `_projects/*/drafts/`
- **Writes:** Updated atoms (relations section, tags, aliases, status
  promotion), new seed atoms harvested from project material, proposed
  frames, memory entry
- **Does not:** Modify human surfaces
- **Matching:** Semantic — reads prose and recognizes concepts
  regardless of wikilinks
- **Appends** to atoms' `## Relations` sections when discovering
  new connections. Adds aliases when it notices an atom is referenced
  by different names.

### Frame-Read
- **Trigger:** User invokes with frame name
- **Reads:** Frame definition, `_atoms/`, `_journal/` (via provenance
  links only), `_projects/` (briefs only), past reflections in `_memory/`
- **Writes:** Reflection to `_memory/`, updates frame zone in HOME.md
- **Does not:** Create or modify atoms, frames, or human surfaces

---

## Collaboration Model

Beyond the three skills, the primary way the vault helps is
**conversational collaboration** — not a skill, not a routine.

The user brings writing or a question. The agent reads it, matches
it against the atomic layer semantically, and responds with grounded,
specific answers drawn from the user's own accumulated thinking.

The response goes to `_memory/` as a densely wikilinked trace.

Examples:
- "What in my vault connects to what I just wrote?"
- "Read this chapter through the art-practice frame."
- "What am I missing in this argument?"
- "Where have I thought about this before?"
- "Show me the path to this chapter." (generates a canvas)

---

## How Navigation Works

- **HOME.md** — vault dashboard. Links to today's journal, inbox,
  active projects, recent atoms, seed atoms, proposed frames.
  Has agent-refreshable zones for frame reflections and vault health.
- **Project brief** — each division has wikilinks to its note and
  draft. The brief is the project's table of contents.
- **Obsidian graph view** — emerges from wikilinks in `_atoms/` and
  `_memory/`. Gets denser with every collaboration.
- **Canvas files** — generated on demand as visual maps of specific
  inquiries. Dated snapshots. The series over time is its own record.
- **Dataview queries** — HOME.md uses these for dynamic lists
  (recent journals, seed atoms, active projects, etc.)

---

## How the Graph Grows

The user doesn't build the graph. The agent does:
1. Atomize creates nodes from journal and inbox material
2. Tend creates edges between atoms and harvests new nodes from projects
3. Frame-read creates richly linked reflections in memory
4. Conversational collaboration creates traced, argued responses in memory
5. Obsidian renders all of this as a navigable, visual graph

The same atoms can be traced through different frames, producing
different paths. Each traced path is a dated snapshot. The series
of traces over time shows how thinking developed.

---

## Agent Helps With Project Setup

When the user wants to start a project:
1. Agent collaborates on drafting the brief (conversational)
2. When a division is named, agent scaffolds `notes/[slug].md`
   and `drafts/[slug].md` with proper frontmatter
3. Agent adds nav links to the brief's divisions section

---

## Frames

- Frames are perspectives, not territories. They don't own content.
- Active frames are created by the user or activated from proposals.
- Proposed frames are created by tend when atom clusters show coherence.
- The same atoms light up differently through different frames.
- Frame reflections accumulate in `_memory/` over time.
- The user's former domains become the first active frames.

---

## Migration Steps

1. Run setup script (creates directory skeleton)
2. Copy journal entries into `_journal/`
3. Seed `_inbox/` with material to be processed
4. Convert former domain `_DOMAIN.md` files into frame definitions
5. Restructure ai-conversational-writing project:
   - Update brief with new schema and divisions section
   - Move two experiment notes to `notes/` with frontmatter
   - Create draft stubs in `drafts/`
6. Delete stale templates (project-trail.md, work.md)
7. First run: atomize → tend → frame-read

---

## Design Rationale: Research Influences

The following design choices were informed by a review of the
research landscape on bidirectional knowledge-text coupling
(discourse graphs, computational argumentation, KSGs, digital
humanities ontologies):

**Claims as atoms.** Discourse graphs (Joel Chan), nanopublications,
argumentation schemes, and Knowledge Synthesis Graphs all center on
granular, attributed, evidence-linked assertions as the fundamental
unit — not documents, not concepts. The vault adds `claim` as an
atom kind to capture this. Writers assemble arguments, not just
concept maps.

**Natural language relation descriptions.** Rather than formal edge
typing (which requires infrastructure we don't need yet), atoms
describe their relationships in prose sentences in a `## Relations`
section. This captures epistemic nuance (supports, challenges,
extends, instantiates) in a human-readable form that a future graph
database can parse into typed edges. No structural migration needed.

**Aliases for entity resolution.** Standard in knowledge graphs.
Prevents synonym splitting during atomization. Makes future Graphiti
integration easier.

**Provenance as first-class.** The vault was already committed to
this ("the trail is the treasure"). The research confirms this is
a convergent design principle across discourse graphs,
nanopublications, and digital humanities ontologies.

**Deliberate asymmetry over bidirectional sync.** The research
identifies automated bidirectional propagation between prose and
graph as an unsolved frontier problem. The vault sidesteps this:
the human writes prose, the agent maintains the graph, tend bridges
them with judgment. This loose coupling is better for a single
creative practitioner than the tight sync multi-user platforms need.

---

## Future Extension Points (Not Built)

- **Graph database (Graphiti/Neo4j):** Indexes what already exists
  when file-based traversal gets slow. Atom schema is graph-ready:
  aliases enable entity resolution, `kind:` provides node labels,
  and natural language relation descriptions can be parsed into
  typed edges.
- **Public surface / Exhibits:** `_exhibits/` as curation layer for
  web presence or portfolio. Activates when works accumulate.
- **Multi-agent orchestration:** Frames become agent personas, skills
  become shared tools, protocol becomes a base class.
- **Autonomous scheduling:** Some skills (especially tend) run on
  a schedule when trust and tooling allow.
