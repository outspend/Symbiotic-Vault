---
type: design-note
purpose: event catalog and thread architecture
created: 2026-04-08
status: active — working specification
depends_on:
  - DESIGN_NOTE_FACTS_EVENTS.md
  - DESIGN_REVIEW_CONSOLIDATED.md
  - probe.md (provisional skill spec)
---

# Event Catalog and Thread Architecture

This document formalizes the vault's event system and proposes
threads as the primary interaction surface — replacing the
batch-processing inbox model with a conversational, thread-native
architecture.

---

## The Thread Insight

The inbox was designed as a folder of files. Material arrives,
sits, and gets batch-processed by atomize. But the vault's
actual interactions are conversational: the agent reflects, the
human replies, a probe sparks a discussion, an idea develops
through exchange. These exchanges are threads — temporal,
multi-turn, with lifecycle.

The friction: if you develop an idea in conversation with the
agent, you shouldn't have to "drop it in the inbox" for the
structural pipeline to find it. The conversation *is* the
material. The thread *is* the inbox item. Engagement in the
thread is what produces structurable material.

Threads are where events originate. A thread is the surface
where captures arrive, where probes resolve, where the human's
creative engagement produces the raw material that skills
process. The event system starts here.

---

## What a Thread Is

A thread is a sequence of exchanges between human and agent,
anchored to a piece of material or a topic. It has lifecycle,
participants, and resolution.

**Examples of threads:**
- A reflection produces a thread observation → human replies →
  agent responds → idea develops → thread resolves (atomizable
  or pinned or carried)
- A capture arrives → agent probes → human provides context →
  probe refines → thread resolves (connected, pinned, discussed,
  or unresolved)
- A project question surfaces → human and agent discuss → thread
  produces a decision or a draft direction
- An experiment runs → human reacts (→ yes/no/try-again/not-yet
  with rationale) → thread carries the reaction and its
  implications

**What threads replace:**
- The inbox as batch queue (threads are live, not filed)
- The reflection reply as the only correspondence channel
  (threads can originate from any stimulus)
- The manual "drop it in inbox" step (the thread itself is
  the material)

**What threads don't replace:**
- The journal (the human's unmediated voice, not a conversation)
- Atoms (structural facts, not exchanges)
- Memory entries (event records, not interactions)

---

## Thread Lifecycle

```
opened
  → active (exchanges happening)
    → resolved
        → atomized (thinking extracted into atoms)
        → pinned (connected to project/frame territory)
        → carried (unresolved but noted — chronicle or
                   orchestrator tracks)
        → dropped (no energy — compostable)
    → paused (human disengaged, orchestrator may resurface)
```

A thread is opened when stimulus meets response. It's active
while exchanges are happening. It resolves when either the
material finds a structural home or the energy dissipates.
Paused threads are candidates for resurfacing — the
orchestrator's judgment about when to bring them back.

**Resolution is not filing.** The human doesn't declare "this
thread is resolved." The orchestrator recognizes resolution
from signals: the human pinned something, or atomize extracted
from the thread, or the human stopped engaging after a natural
conclusion. Explicit signals (→ yes, → no, → try-again,
→ not-yet) help but aren't required. Silence is data.

---

## Thread Storage

Threads need to be readable by skills, queryable by the
orchestrator, and browsable by the human. They also need to
feel like conversations, not files.

### Option A: Threads as enriched inbox items

Keep the inbox folder but evolve items from single files to
thread files — each file grows as exchanges append. Frontmatter
tracks lifecycle:

```yaml
---
type: thread
opened: YYYY-MM-DD
status: active | paused | resolved
resolution: atomized | pinned | carried | dropped
origin: capture | reflection | probe | experiment | conversation
stimulus: path/to/original-material
participants: [user, agent]
---

## 2026-04-08 10:30 — agent
Probing this against the atomic layer. The strongest
connection is to [[data-center-cohabitation]]...

## 2026-04-08 10:35 — user
It's not about the concept — it's about the *sound*.
Machine hum and human presence cohabiting as audio...

## 2026-04-08 10:40 — agent
That changes the connection. This is about the sensory
dimension of cohabitation, not the structural one...
```

Pro: works with existing Obsidian, skills read files normally.
Con: appending to files is mutable (breaks write-once pattern
for the inbox).

### Option B: Threads as linked sequences

Each exchange is its own file. Thread coherence comes from
frontmatter linking:

```yaml
---
type: thread-entry
thread: thread-slug
sequence: 3
from: user | agent
date: YYYY-MM-DD
---
```

Pro: each entry is immutable (write-once). Thread is a query
across entries sharing a thread slug.
Con: many small files. Harder to read as a conversation.

### Option C: Thread index + conversation files

A thread index file tracks metadata and lifecycle. The actual
conversation lives in a single growing file (like a chat log).
The index is what skills and the orchestrator read for status.

```
_threads/
  _index.md          (thread metadata, queryable)
  song-cohabitation/
    thread.md        (the conversation)
    stimulus.md      (original capture, immutable)
```

Pro: clean separation of metadata and content. Conversation
reads naturally. Original stimulus preserved immutably.
Con: new folder surface to manage.

**Recommendation:** Option C. It gives the orchestrator a clean
index to query, preserves the original stimulus immutably, and
lets the conversation grow naturally. The thread folder replaces
the inbox as the primary landing zone for incoming material.
The inbox can remain for truly simple captures that don't need
conversation (a quick note, a bare reference), but threads
become the active interaction surface.

### Decision: open. Needs testing before committing.

---

## Event Catalog

Events organized by origin. Each event lists its source, what
produces it, the payload (what information it carries), where
it's currently recorded, and what should respond.

### Human-originated events

| Event | Produced when | Payload | Record | Handlers |
|---|---|---|---|---|
| `journal.written` | Human writes daily journal | date, content | _journal/YYYY-MM-DD.md | reflect reads; atomize scans |
| `capture.arrived` | Human drops material in inbox/thread | stimulus content, optional context | _inbox/ or _threads/ | orchestrator assesses → probe? |
| `reply.received` | Human responds to reflection or thread | thread reference, signals, rationale | thread entry or inbox reply | orchestrator parses → route signals |
| `signal.emitted` | Human reacts with → yes/no/try-again/not-yet | signal, rationale, thread context | parsed into thread/reply frontmatter | Factory reaction loop; atomize extracts rationale |
| `draft.written` | Human writes in project drafts/ | project, division, content | _projects/*/drafts/ | tend harvests on next run |
| `note.written` | Human writes in project notes/ | project, division, content | _projects/*/notes/ | tend harvests on next run |
| `frame.activated` | Human promotes proposed → active | frame id | _frames/ status change | frame-read candidate |
| `pin.confirmed` | Human confirms a probe's pin suggestion | target project/frame, material | thread resolution | record connection in project territory |

### Skill-originated events (structural)

| Event | Produced by | Payload | Record | Handlers |
|---|---|---|---|---|
| `atom.created` | atomize | atom id, kind, source, initial relations | atoms_touched: action: created | tend considers on next run |
| `atom.reinforced` | atomize | atom id, source where recurrence found | atoms_touched: action: reinforced | tend notes recurrence pattern |
| `atom.enriched` | tend | atom id, what changed (relations, tags, aliases, status, frames) | atoms_touched: action: enriched | frame-read trigger check; chronicle candidate |
| `atom.promoted` | tend | atom id, old status → new status | atoms_touched + status change | trace candidate; chronicle candidate |
| `frame.proposed` | tend | frame id, seed atoms, rationale | memory entry + frame file | notify user (HOME or thread) |
| `index.regenerated` | tend | date, atom count, frame groupings | _atoms/_index.md rewritten | downstream skills use fresh index |
| `connection.discovered` | tend | atom A, atom B, relationship | atoms_touched on both | chronicle candidate |

### Skill-originated events (process)

| Event | Produced by | Payload | Record | Handlers |
|---|---|---|---|---|
| `reflection.written` | reflect | date, threads carried, atoms touched, candid | _reflection/ + memory stub | orchestrator reads; chronicle candidate |
| `atom.developed` | reflect | atom id, what was developed | atoms_touched: action: developed + note | atomize checks neighborhood; tend checks relations |
| `atom.challenged` | reflect | atom id, what was challenged | atoms_touched: action: challenged + note | tend considers counter-claim or relation update |
| `probe.resolved` | probe | resolution type, source, connections found, atomizable flag | memory entry | orchestrator routes: atomize if flaggd, pin if confirmed |
| `frame.read` | frame-read | frame id, what's developing, gaps, tensions | memory entry | orchestrator reads; chronicle candidate; trace candidate |
| `trace.produced` | trace (capability) | canvas path, scope, invoking skill | logged by invoking skill | available for browsing |

### Threshold events (derived, not directly emitted)

| Event | Condition | Derived from | Handler |
|---|---|---|---|
| `threshold.crossed(frame, N)` | N+ atoms enriched in frame territory since last frame-read | tend memory entries | fire frame-read for that frame |
| `project.momentum` | sustained enrichment + journal mentions + engagement signals in project territory | cross-source pattern | orchestrator surfaces; chronicle card |
| `project.decaying` | no touches, no journal mentions, no signals for 4+ weeks | absence pattern across memory | reflect asks: cool down? |
| `engagement.escalating` | 3+ yes signals with rationale in a territory | reaction history | Factory: propose project? |
| `neglect.pattern` | N atoms untouched since creation for 30+ days | atoms_touched scan | compost candidate |

---

## The Orchestrator as Event Handler

The orchestrator is not a monolithic brain. It's a collection
of event handlers — rules that fire when conditions are met.

### Handler structure

```
when [event] and [conditions]:
  do [action]
  with [constraints]
```

### Core handlers (first implementation)

**On capture.arrived:**
```
when capture.arrived:
  assess stimulus (rich context? bare link? provocation energy?)
  if strong vault connections likely:
    open thread, initiate probe
  if bare/thin:
    queue for next session surfacing
  respect pace — don't surface more than the session can hold
```

**On reply.received:**
```
when reply.received:
  parse signals (→ yes/no/try-again/not-yet)
  extract rationale
  if action-bearing (explicit request, decision, routing):
    route to appropriate skill or surface
  if engagement (rationale, development, pushback):
    continue thread; flag for atomize if substantive
```

**On threshold.crossed(frame, 3+):**
```
when tend.memory shows 3+ atoms enriched in frame territory
  and last frame-read for this frame is older than enrichment:
    fire frame-read for that frame
```

**On probe.resolved:**
```
when probe.resolved:
  if resolution = pinned:
    record pin in project/frame territory
  if resolution = discussed and atomizable = true:
    flag for atomize on next run
  if resolution = unresolved:
    note in orchestrator memory; resurface after interval
```

**On reflection.written:**
```
when reflection.written:
  read for narrative moments → chronicle card candidates
  read for action-bearing pressure → route if clear
  read atoms_touched for developed/challenged → inform next
    atomize and tend runs
```

**On atom.promoted:**
```
when atom.promoted(seed → developing):
  candidate for trace (connection neighborhood)
  chronicle card: "this atom crossed a threshold"
when atom.promoted(developing → stable):
  candidate for trace (full provenance path)
  chronicle card: "this atom has matured"
```

### Pacing rules

The orchestrator manages the human's attention as a resource:

- **Session pacing:** Don't surface more than 2-3 items per
  session. Lead with the strongest connections. Queue the rest.
- **Resurfacing interval:** Unresolved threads resurface after
  3-7 days (adjustable by engagement pattern). If resurfaced
  twice with silence, let go.
- **Batch awareness:** If 6 captures arrive at once, assess
  all, surface the 1-2 most connected, and note the rest.
- **Silence respect:** Silence on a thread is data, not a
  failure. The orchestrator reads silence_means on projects
  and generalizes: cooling means slow down, searching means
  keep going.

---

## The Engagement Principle (Protected)

The structural pipeline processes human-touched material. All
human surfaces are source: journals, project notes, project
drafts, thread exchanges, replies, captures. The common thread
is human creative engagement, not the specific surface.

**What this means for threads:** A probe conversation where the
human rambles about why a song resonates is human-touched
material. The ramble is as valid a source for atomize as a
journal entry. The thread is where the engagement happened.
The structural pipeline reads from it.

**What this prohibits:** No handler creates atoms from
agent-only sources. Reflections don't feed atomize. Chronicle
cards don't feed tend. The agent's own writing stays in the
agent's ring unless the human engages with it and produces
new material in response.

**The mechanism is engagement, not approval.** The human
doesn't review and approve. The human's continued creative
activity with an idea is what gives it structural substance.

---

## Relationship to Existing Surfaces

### _inbox/ — evolves, doesn't disappear

The inbox remains for simple captures that don't need
conversation: a quick note, a bare reference, a clipping
filed on the go. These are `capture.arrived` events that the
orchestrator may or may not surface for a thread.

Thread-native captures (things that immediately spark
conversation) may bypass the inbox and go directly to
`_threads/` (if Option C is adopted).

The inbox stops being the primary processing queue. It becomes
one of several surfaces where human material arrives. Atomize
reads from threads as well as inbox.

### _memory/ — remains the event log

Memory entries are the canonical record of events. Thread
metadata supplements but doesn't replace memory entries.
Every skill invocation still produces a memory entry with
atoms_touched.

### _reflection/ — remains sacred

Reflections are the agent's daily thinking. They emit events
(`reflection.written`, `atom.developed`, `atom.challenged`)
but they are not themselves threads. The human can *start* a
thread in response to a reflection (the reply mechanism), but
the reflection itself is immutable prose, not a conversation.

**Design concern from reflect-v07 testing:** Reflection currently
does interim thread maintenance because `## Threads` and reply files
are the available surface. This is workable but creates a tension:
a reflection has a whole, while active discussions have independent
lifecycle. In-scope material such as draft feedback may need to stay
active without becoming part of the day's reflective arc.

Future thread architecture should let `reflect` create or update
thread objects with context/history seeds, status, and resurfacing
rules, while allowing the reflection prose to surface only the
Threads that belong to the current reading experience. Active
threads should be independently snoozable, carried, resolved, or
resurfaced without forcing every active discussion into every
reflection.

### _chronicle/ — narrativizes events

The chronicle subscribes to events and writes cards when
narratively significant things happen. It doesn't manage
threads, process captures, or route actions. It tells the
story.

---

## Implementation Sequence

1. **Test probe under CC.** Run probe conversations manually.
   Experience the thread pattern. Feel the friction points.
   Don't build thread infrastructure yet.

2. **Catalog events from real runs.** After several probe
   sessions, atomize runs, tend runs, and reflect cycles,
   compile the actual events produced. Compare against this
   catalog. What's missing? What's noise?

3. **Build the handler loop.** Start with one handler: the
   frame-read trigger from tend's enrichment threshold. Run
   it manually: after tend, check the condition, fire
   frame-read if met. This is the orchestrator's first rule.

4. **Formalize threads.** After enough probe conversations
   reveal the natural shape of threads, choose a storage
   option and implement. The thread lifecycle and resolution
   model will be clearer after practice.

5. **Build the orchestrator.** Once handlers are tested
   individually, compose them. The orchestrator is the
   composition of handlers plus pacing rules.

6. **Connect the chronicle.** Once the event stream is
   flowing and the orchestrator is routing, the chronicle
   can subscribe and narrativize.

---

## Open Questions

- **Thread display.** Where do threads appear? HOME.md?
  A dedicated surface? An Obsidian plugin? The display
  needs to feel like conversation, not like browsing files.

- **Thread and inbox coexistence.** How does atomize know
  to read from threads as well as inbox? Does atomize's
  scope expand, or does a new step extract atomizable
  material from threads into a form atomize can process?

- **Signal parsing across surfaces.** Reaction signals
  (→ yes/no/try-again/not-yet) currently live in reflection
  replies. In a thread-native world, they can appear in any
  thread exchange. The parsing needs to be surface-agnostic.

- **Thread persistence across sessions.** Under CC, a thread
  is a conversation in a single session. Across sessions,
  thread state needs to persist. The storage model determines
  how this works.

- **Autonomy gradient.** As the orchestrator matures, which
  handlers can fire without human invocation? Frame-read
  triggers are low-risk. Probe initiation is medium. Atom
  creation should always trace to human-touched material.
  The gradient needs explicit specification.
