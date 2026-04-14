---
type: design-note
purpose: architectural framing — events, facts, and process
created: 2026-04-08
status: active design document
references:
  - "The Design of Datomic — Rich Hickey"
  - "Deconstructing the Database — Rich Hickey"
  - DESIGN_REVIEW_CONSOLIDATED.md
  - DESIGN_SEED_CHRONICLE.md
---

# Design Note: Facts, Events, and the Shape of the Vault

This note captures a recognition: the vault is already an
event-driven system built on immutable facts. It doesn't need
to become one. It needs to formalize what it already is, and
build the handler layer that makes it reactive.

The framing draws on Rich Hickey's design of Datomic. The
parallels are structural, not cosmetic — the vault's data model
maps to Datomic's core principles in ways that suggest concrete
architectural moves.

---

## Data as Facts, Process as Stories

The atomic layer is facts. Atoms are immutable assertions about
concepts — their identity, kind, relations, provenance. An atom
accretes (new relations appended, status promoted, aliases added)
but never rewrites. The original assertion remains. The journal
is the most immutable layer — the human's dated record of when
and how ideas appeared. Memory entries are write-once records of
what skills did. Reflections are immutable after the day passes.

Everything the vault stores is a fact. Facts have time. Facts
have provenance. Facts accumulate. The past doesn't change.

Process is what happens around facts. Reflections are the agent
reading facts and thinking about them. Probe threads are
conversations sparked by new material encountering existing
facts. The chronicle (when built) is the narrative told about
what the facts mean taken together. Frame-reads are facts seen
through a specific lens. Experiments are creative processes that
draw on facts and produce new ones.

**Data is facts. Process is stories around facts.** The vault
holds both, and the distinction between them is the same
distinction the vault already makes between the structured layer
(facts) and the process layers (reflections, memory, chronicle).

---

## The Vault as Tree Rings

Hickey uses the metaphor of tree rings for an immutable,
accreting database. The core remains intact. New growth happens
at the edge. Process requires new space.

The vault's rings, from core outward:

```
Journal  — the oldest ring. The human's unmediated voice.
           Never changes. The record of when ideas appeared.

Atoms    — the structural ring. Single-concept facts with
           relations. Grow outward through enrichment but
           the original assertion remains.

Memory   — the process ring. Write-once records of what
           skills did, what was touched, what's uncertain.
           Always expanding. Never rewritten.

Reflection — the agent's own ring. Daily thinking, immutable
             after the day. The agent's developing perspective.

Chronicle — the narrative ring (when built). Mutable cards,
            but grounded in citations to the inner rings.
            The only ring that rewrites — because narrative
            understanding develops.
```

Each ring is intact. The inner rings don't change. The outer
rings grow. The chronicle is the exception — it's mutable because
narrative sense-making requires revision. But it's grounded in
citations to immutable evidence, which keeps it honest.

---

## Memory Entries Are Transactions

In Datomic, every datom carries its transaction — not just a
timestamp but the full context of the operation: who, when, what
else happened, provenance. The transaction is first-class and
queryable.

The vault's memory entries are transactions. Each one records:

```yaml
type: memory
skill: atomize | tend | frame-read | reflect | probe
date: YYYY-MM-DD
atoms_touched:
  - id: atom-slug
    action: created | reinforced | enriched | developed | challenged | referenced | resolved
    uncertainty: "optional doubt"
    note: "optional context"
```

This is a transaction record. It says: this skill (who), on this
date (when), asserted these facts about these atoms (what), with
this confidence (uncertainty). The prose body carries the full
reasoning context.

**Making transactions first-class means treating them as the
primary queryable substrate.** This is what atoms_touched already
enables:

- What's hot? High touch count, recent dates, multiple skills.
- What's cold? Created once, never touched again.
- What's uncertain? Open uncertainty flags, unresolved.
- What's developing? Reinforced often, enriched by tend.
- What patterns emerge? Skills converging on the same atoms.

The experiments (compost, drift, séance, table, membrane) all
query transaction history. They treat memory entries as the
event log they already are.

---

## Events Already Present

Every skill invocation produces a memory entry. That memory
entry is an event. The vault is already emitting events — it
just doesn't have subscribers.

### Events the vault currently emits

| Event | Emitted by | Current record |
|---|---|---|
| `atom.created` | atomize | atoms_touched: action: created |
| `atom.reinforced` | atomize | atoms_touched: action: reinforced |
| `atom.enriched` | tend | atoms_touched: action: enriched |
| `atom.developed` | reflect | atoms_touched: action: developed |
| `atom.challenged` | reflect | atoms_touched: action: challenged |
| `atom.resolved` | any skill | atoms_touched: action: resolved |
| `frame.proposed` | tend | memory entry + frame file created |
| `capture.arrived` | (external) | new file in _inbox/ |
| `journal.written` | (human) | new file in _journal/ |
| `reply.received` | (human) | new file in _inbox/ with responds_to |
| `probe.resolved` | probe | memory entry with resolution status |
| `index.regenerated` | tend | _atoms/_index.md rewritten |

### Events not yet formalized but implicit

| Event | Would be emitted by | Currently implicit in |
|---|---|---|
| `threshold.crossed(frame, N)` | tend | enrichment count per frame in memory |
| `atom.promoted(new_status)` | tend | status change logged in memory |
| `project.decaying` | reflect | journal silence + touch absence |
| `frame.activated` | (human) | status change in frame file |
| `experiment.reacted` | atomize | reaction parsing in reply |

### What's missing: the subscription layer

The cross-skill memory channel is pull-based polling. Each skill
reads the latest memory entry from every other skill when it
runs. This works but it's passive — things only happen when
invoked.

An event-driven system adds reactive subscription:
- `capture.arrived` → orchestrator assesses, potentially
  initiates probe
- `threshold.crossed(frame, 3)` → orchestrator fires frame-read
- `atom.promoted(developing)` → orchestrator considers trace
- `reply.received` → orchestrator parses signals, routes
  action-bearing items
- `probe.resolved(pinned)` → orchestrator records pin
- Narrative-significant events → chronicle writes a card

The orchestrator is an event handler. It subscribes to the
event log (memory entries + inbox + journal), evaluates
conditions, and dispatches responses.

---

## Engagement as the Merge Mechanism

**This principle must be protected.**

In Datomic, a transactor merges novelty from memory into
storage. In the vault, the analog would be: the agent's
developing understanding (in reflections, in probe threads,
in chronicle observations) merges into the structural layer
(atoms, relations, frames).

**But this merge does not happen by agent election.** The agent
does not decide "this reflection insight is ready to become an
atom." The merge happens through the human's continued creative
engagement:

```
Agent reflects → surfaces an observation in a thread
  Human replies → engages with the thread, develops the idea
    Reply lands in inbox → raw material now exists
      Atomize processes → extracts from the human's engagement
        Tend enriches → structural change from human-touched material
```

The human's engagement is the mechanism. The agent notices,
surfaces, proposes. The human's creative response — a journal
entry, a reply, an inbox capture, a draft — produces the raw
material that the structural pipeline processes. The agent
cannot merge its own insights into the structural layer
unilaterally.

This is not a review-and-approve gate. It's deeper: the human's
engagement with an idea is what gives it the substance to become
structural. An agent insight that the human never engages with
stays in the reflection layer. It may be composted. It may be
carried in the chronicle. But it doesn't become an atom until
the human's creative activity produces the material.

**Why this matters:**
- It prevents the agent from feeding itself (the reflection
  boundary principle, now stated as a transaction rule)
- It keeps the structural layer grounded in human thinking
- It means the vault's development is driven by human creative
  energy, not agent administrative activity
- It preserves the human as the source of creative authority
  while the agent maintains structural health

**The one exception:** Tend harvests from project notes and
drafts — material the human wrote in the context of active
creative work. This is still human-touched material. Tend
doesn't harvest from reflections or the chronicle.

---

## The Three Roles (Datomic → Vault)

Hickey separates three concerns in a database: broadcasting
(announcing what happened), indexing (making facts queryable),
and garbage collection (managing what's no longer active).

### Broadcasting

When atomize creates an atom or tend enriches one, the memory
entry is the broadcast. It announces what happened to all
downstream consumers via the cross-skill channel. Under event
formalization, this becomes explicit event emission rather than
passive logging.

### Indexing

Tend regenerates `_atoms/_index.md` on every run. The index
makes the current state of all facts efficiently discoverable.
All skills except tend use the index as their entry point.
The index is the vault's equivalent of Datomic's sorted set
of datoms — an organized, queryable view of current state.

### Garbage collection

The compost. It finds facts no longer active in the system —
atoms never touched after creation, unresolved uncertainties
past a threshold, abandoned project material — and asks what
their pattern of neglect reveals. This is garbage collection
with creative intent: the "garbage" might be where the next
frame is born.

The chronicle also performs a kind of garbage collection
through pruning — orphaned cards that stay unlinked surface
for review.

---

## Flexibility: Attributes Are the Only Schema

Hickey's radical minimalism: no tables, no types, no classes.
Just attributes. Define what kinds of facts you can assert
(name, cardinality, type, uniqueness) and then assert freely.

The vault's analog: the atom schema is the only real structural
constraint. An atom has id, kind, status, source, tags, frames,
aliases, and a Relations section. That's the attribute schema.
Everything else — what the atom is about, how it connects, what
stories are told around it — is free.

One schema, many uses. A concept atom, a claim atom, a method
atom, a person atom — all use the same structure. The kind field
is an attribute, not a type hierarchy. This flexibility is what
lets the vault hold any domain without schema changes.

The frontmatter fields across all file types (atoms, memory,
reflections, frames, projects, inbox items) are the vault's
attribute definitions. They're minimal and consistent. The prose
bodies are free. This is Hickey's "one relation: EAVT" applied
to a creative knowledge system.

---

## What This Suggests for Implementation

### Recognize: already done

The vault's data model is already event-shaped. Memory entries
are transactions. Atoms are immutable facts. The cross-skill
channel is a pull-based event consumer. atoms_touched is the
event payload. Time is a first-class citizen of every operation.

### Formalize: next step

1. **Name the events.** Create a reference document listing
   every event the vault emits, its source, its payload, and
   its current record location. The table above is a start.

2. **Define handlers.** For each event, specify what should
   respond and under what conditions. Start with the handlers
   we've already designed:
   - `threshold.crossed(frame, 3+)` → fire frame-read
   - `capture.arrived` → assess for probe
   - `reply.received` → parse signals
   - Narrative moments → chronicle card

3. **Build the handler loop.** This is the orchestrator — but
   understood as an event handler, not a monolithic brain. It
   reads the event log, evaluates conditions, and dispatches.
   Under CC: the human runs the loop manually. Under
   autonomous scheduling: the agent runs the loop.

4. **Protect engagement-as-mechanism.** As the system becomes
   more reactive, ensure that the structural pipeline still
   requires human-touched material. No handler should create
   atoms from agent-only sources. The reflection boundary
   holds even in an event-driven system.

### Extend: later

- Multi-agent: separate transactors (writers) from peers
  (readers). One agent writes to the atomic layer. Multiple
  agents read independently. Hickey's architecture maps to
  the vault's multi-agent extension point.
- Graph DB: when the event log and atomic layer are dense
  enough that file-based traversal is slow, the graph DB
  indexes what already exists (the existing extension point
  in VAULT_DESIGN.md). Datomic's sorted indexes are the
  analog.
- Chronicle as event subscriber: formally subscribes to the
  event stream and narrativizes significant moments.

---

## The Synthesis

The vault is a Datomic-shaped system implemented in markdown
files and LLM judgment instead of Clojure data structures and
sorted indexes.

| Datomic | Vault |
|---|---|
| Datom (E/A/V/T) | Atom (id/kind/relations/source) |
| Transaction | Memory entry (skill/date/atoms_touched) |
| Database as value | Vault at a point in time (queryable via index + memory) |
| Transactor | Skills that write (atomize, tend) |
| Peers | Skills that read (frame-read, reflect, probe) |
| Sorted indexes | _atoms/_index.md |
| Garbage collection | The compost |
| Immutable storage | Journal, reflections, memory entries |
| Process/novelty | Probe threads, chronicle cards, experiment outputs |

What Datomic deliberately doesn't have: a story layer. Datomic
is infrastructure. The vault is a creative practice. The
chronicle, the experiments, the Factory's reaction system —
these are the story layer built on top of Datomic-shaped facts.
The stories are what make it a creative tool rather than a
database.

**Data is facts. Process is stories around facts. The trail is
the treasure. The stories are the trail.**
