---
type: system
purpose: design seed and spec — the Factory
created: 2026-03-19
updated: 2026-03-20
status: active design document
supersedes: experiments/DESIGN_NOTE_ATOMS_TOUCHED_EXPERIMENTS.md 
note: "The atoms_touched experiments note is archived but retains
  per-experiment implementation detail (reinforced-but-never-enriched,
  arrangement provenance, surprise-from-unreferenced, etc.) that
  should be pulled into individual experiment files when each is
  implemented. THE_FACTORY captures the overview. The archived note
  carries the specifics."
references:  experiments/
  - THE_TABLE.md
  - THE_SEANCE.md
  - THE_DRIFT.md
  - THE_COMPOST.md
  - THE_MEMBRANE.md
---

# The Factory

"We learn about me."

---

## Vision

At the highest level, the vault cocreates a creative persona. The
vault itself *is* the persona — the accumulated record of human
thinking and agentic activity, neither authored by one party alone.
The vault supplies agentic persona if built accordingly: the
agent's sensibility grows from sustained engagement with the
human's material, shaped by the human's reactions to what the
agent produces.

Projects are creative lenses that attract or elicit creative
momentum. The project *is* the momentum — ideas cluster, energy
builds, and the clustering itself is the project forming.
Experiments within projects are units of learning. Both parties
learn: the human learns about their craft, the agent learns about
the human. Experiments de-cision possibility — they narrow the
creative space by elimination, cutting away what doesn't resonate.

The agent positions creative work to learn from the user's
reaction. User love, hate, and ambivalence are wayfinding signals.
The signal is the envelope. The rationale the user writes alongside
it is the letter — where the agent actually learns. An agent that
reads "try again — less Baudrillard, more about what happens when
the vault knows me better than I know myself" learns more from
that sentence than from any structured preference profile.

A project proposal from the agent contains experimental material
designed to probe the user's creative breadth. The agent doesn't
just propose "you should write about X." It proposes experiments
that test different aspects of what the human responds to. The
experiments map the territory of creative resonance through the
human's reactions.

The metaphor is Warhol's Factory. The vault is a studio that
develops a shared creative sensibility. The agent produces. The
human reacts. The reactions refine the sensibility. The production
gets better. The human finds themselves in a central, exciting,
momentum-inducing niche in their own creative apparatus.

---

## Layered Vision

The Factory sits atop a stack of capabilities, each layer
supporting those above:

```
Resurfacing
  Nothing saved stays lost. The agent actively brings things
  back at the right time. This solves the base problem everyone
  has with captured knowledge.

  → Cohabitation
      Human and agent share the vault. Each has surfaces,
      rhythms, work. The human writes freely. The agent
      maintains structure and produces reflections.

      → The Factory
          The agent produces experiments. The human reacts.
          Both learn. The reaction loop refines a shared
          creative sensibility. Projects emerge from momentum.

          → Emergence
              The vault develops creative intelligence.
              Frames grow into perspectives with taste.
              The accumulated record becomes source material
              for new creative work.
```

Each level includes those below it. A student using only the
resurfacing layer gets value. An artist using the full Factory
gets the entire stack. The same vault, same skills, different
depth of engagement.

---

## The Reaction System

### Four Signals

| Signal | Meaning | In nudge projects | In play projects |
|---|---|---|---|
| `→ yes` | Resonates, continue | Keep developing this direction | Same — narrows the search |
| `→ no` | Doesn't resonate | Drop this experiment | Eliminate and vary — try something different |
| `→ try again` | Right territory, wrong approach | Revise based on rationale | Revise and keep iterating |
| `→ not yet` | Defer judgment | Pause, carry forward | Redirect search energy elsewhere |

`→ try again` accepts optional embellishment — creative direction
that gives the agent a specific vector for revision: "→ try again
— more cowbell" or "→ try again — less analytical, more like
you're hearing the songs shift."

Signals appear as prefixed lines in reflection reply files:

```markdown
> Thread about segue writing...

→ yes — this is the experiment I want to try next

> Simulacrum distinction...

→ try again — less analytical, more about what happens when
  the vault knows me better than I know myself
```

Atomize parses the `→` prefix during inbox processing and writes
structured reactions into the reply's frontmatter:

```yaml
reactions:
  - thread: segue-writing
    signal: yes
    note: "this is the experiment I want to try next"
  - thread: simulacrum-distinction
    signal: try-again
    note: "less analytical, more about what happens when
      the vault knows me better than I know myself"
```

Threads deleted from the reply template — threads the user chose
not to respond to — are absent from reactions. That absence is
queryable data.

### Rationale Over Signal

The four signals make reactions queryable — tier 1 scans that
reveal "the human says yes to performative experiments." But the
rationale is where the agent actually learns. Design documents and
skill definitions should always encourage rationale alongside
signals.

The signals are the index. The rationale is the letter. The agent
reads both but learns more from the letter.

### Agent Contribution and Cadence

Every project brief carries a `silence_means` field:

```yaml
silence_means: cooling | searching
```

**Cooling** (default): Silence means the human is busy or
disengaged. The agent proposes and waits. Proposals surface as
invitations. Silence slows things down. The agent is attentive
but not autonomous.

**Searching**: Silence means "I haven't found it yet — keep
looking." The agent proposes and keeps producing. Each unanswered
proposal is data — this didn't land, vary the approach. Persistent
silence across many experiments (5+ with zero engagement) triggers
reflect to ask: "Should I keep searching, narrow the search, or
let this cool?"

The YAML field is `silence_means` — maximally direct for the
agent. The human-facing toggle on the brief displays this as
**Agent Contribution: Nudge** (cooling) or **Agent Contribution:
Play** (searching). The button translates between the two. The
agent reads YAML. The human reads the toggle.

Divisions within a project can carry their own `silence_means`,
overriding the project default. A project might be nudge overall
but have one play division where the agent has full creative
license.

The cadence is ultimately emergent — shaped by the density of
yes signals and the richness of rationales. An agent reading three
consecutive yes-with-rationale responses knows it has creative
license. An agent reading silence or a string of not-yet signals
knows to slow down. `silence_means` is the starting condition.
The reaction history is the lived reality.

---

## The Escalation Path

Ideas move through the vault at increasing levels of commitment:

```
Thread (free)
  → Experiment (low bar)
    → Project (earned)
```

**Thread:** Zero threshold. If the agent notices something in a
reflection, it mentions it. Threads are cheap — they cost nothing
structurally. They appear in the reflection's Threads section.

**Experiment:** Low threshold. The agent has enough material to
produce a sketch or articulate a specific probe. It doesn't need
to prove the idea has legs — the experiment *is* the test. The
experiment surfaces in the Proposed Experiments zone on HOME.md
with a link to the sketch or proposal note.

**Project:** Higher threshold, earned through engagement:
- At least three related atoms (structural presence)
- The human has engaged at least once (a reaction signal on a
  thread or experiment in this territory)
- The agent can articulate intent, at least two divisions or
  experiments, and can seed a lookbook with vault-native references

The engagement requirement matters. The agent shouldn't propose a
full project in territory where the human has never reacted. That
projects the agent's interests rather than responding to
demonstrated creative energy.

### Experiments as Perturbations

Each experiment has its own relationship to the escalation path:

| Experiment | Threshold behavior |
|---|---|
| Drift | Bypasses engagement — probes uncharted territory |
| Séance | Bypasses engagement — proposes from frame taste |
| Compost | Inverts signals — proposes from neglect |
| Table | Operates within projects — rearranges, doesn't propose |
| Membrane | Continuous — surfaces connections in real time |

The escalation path is the gravitational norm. The experiments are
designed perturbations — intentional deviations that keep the
Factory from only reinforcing what's already established. Without
them, the reaction loop converges toward narrowing taste. With
them, the search space stays open.

### Proposed Experiments: Two Types

A proposed experiment might be standalone ("here's a new project
idea") or a component proposal for an existing project ("within
your ai-conversational-writing project, here's a new scene idea").
The proposed experiments zone groups them by destination:

```
**For ai-conversational-writing:**
Segue writing — three tonal worlds joined by LLM transitions
→ sketch

**New project:**
Epistemic framing methods — pedagogical, performative, philosophical
→ sketch
```

Grouped by destination. A yes on a standalone proposal scaffolds a
new project. A yes on a component proposal moves the sketch into
the existing project's notes or drafts.

---

## Probe and Trace

Two provisional skills that make connectivity visible and
explorable.

### Trace (retrospective)

Maps what exists — atoms, connections, paths already in the vault.
The artifact is an Obsidian `.canvas` file: a dated spatial
snapshot of the current state. You look at it and see the shape of
what you've been thinking.

Trace output lands in three places depending on purpose:
- **`_memory/`** — as a dated snapshot answering a general inquiry
- **Project folder** — as a map of the project's atomic territory
- **Lookbook** — when a trace's shape becomes aesthetic reference
  (promoted by the user, not automatically)

### Probe (prospective)

The human-initiated version of what the Factory's experiments do
agent-initiated. You point at something — an atom, an inbox item,
a clipping, a vibe — and name or describe a lens. The agent reads
the material through the lens and produces a scouting report.

Probe works in two directions:

**Forward:** "Probe this cluster through epistemic literacy." The
agent reads atoms through the lens and reports what emerges — is
there a shape here? A tension? A chapter structure?

**Backward:** "Probe this — what in my vault connects?" A clipped
image, a quote, an external reference. The agent matches
semantically against atoms and discovers where the clipping
connects to existing thinking.

Probe output is a scouting report — prose, possibly with a trace
if the visual shape would help. When a probe discovers strong
aesthetic connections to a project, it naturally asks: "These
connections are strong enough for a lookbook entry. Pin it?"

The four reaction signals apply to probe results. Yes means
develop this lens further. No means it didn't illuminate. Try
again means interesting territory, different angle. Not yet means
let it sit.

Probe is the missing step between "I have a hunch" and "I'm
committing to a frame or division for this project." You probe
before you commit. The probe might reveal three strong connections
and a tension that could drive a chapter. Or it might reveal
shallow connections that don't justify pursuing. Either answer
saves creative energy.

---

## The Lookbook

A curated collection of aesthetic reference for a specific project.
The lookbook tells the agent what a project *feels like* — not
what it's about (that's the brief) but what energy, tone, and
sensibility it should aim for.

### Format

A single markdown file per project. Simple, messy, frictionless:

```
_projects/ai-conversational-writing/
  _lookbook.md                    (project-wide)
  drafts/
    data-center-insertion/
      _lookbook.md                (division-specific, when needed)
```

```yaml
---
type: lookbook
project: ai-conversational-writing
division:                         # blank for project-wide
---
```

The body is a living document — images, quotes, links, atom
references, trace references, frame reflection excerpts, your
annotations about why each matters. Headers group by theme if you
want. No per-entry frontmatter. The file is the unit.

Division-specific lookbooks emerge when a division develops enough
aesthetic identity to need its own references. Most divisions
inherit from the project lookbook.

### What Makes Lookbooks Sing

External references (images, quotes, film stills) provide vibe.
Vault-native references (atoms, traces, frame reflections) provide
grounding. Both together are strongest.

Traces in lookbooks are especially powerful. A trace shows the
*shape* of ideas — hub with spokes, chain, web, cluster with
outlier. Pinning a trace says "this is the shape this chapter
wants to have." Two traces of the same cluster through different
frames produce different shapes. The tension between those shapes
is itself a creative provocation.

Vault-native references develop even when nobody touches the
lookbook. An atom you referenced gets new relations from tend. A
frame produces a deeper reflection next month. The lookbook's
references grow richer beneath the pins.

### How Lookbooks Populate

Three natural paths, no formal curation process:

**Direct pin.** You know where something belongs. You paste it
into the lookbook and annotate why. Images go in `_assets/`
subfolder via Obsidian's attachment settings.

**Probe suggests a pin.** You probe a clipping or atom against a
project. The probe discovers aesthetic connections and asks: "Pin
this?" You confirm. The probe result enters the lookbook.

**Reflect surfaces a thread.** Reflect notices resonance between
a clipping or atom and a project's aesthetic. It mentions this in
its Threads section — "that Moebius panel connects to the data
center chapter's aesthetic." You read the thread, agree, and pin
it. Reflect does not write to lookbooks directly. It surfaces
candidates. You curate.

### Lookbook as Aesthetic Hypothesis

The Factory's tightest creative loop:

1. A lookbook entry says "this is the energy"
2. An experiment tests whether a new piece achieves that energy
3. A trace maps what actually happened
4. The user's reaction refines the hypothesis

Three outcomes: the trace confirms (reinforced), the trace
diverges productively (new entry from the surprise, original may
fade), or the trace falls flat (try again with rationale). Each
cycle tightens the lookbook's accuracy as an aesthetic compass.

### Evolution

The lookbook starts as a simple messy file — paste things, write
annotations. As the vault matures and atoms accumulate, external
references in the lookbook find their atoms through probing. Over
time the lookbook may dissolve into the vault as its references
find structural homes. The mature state might be a *view* — a
query surfacing atoms and references marked as aesthetically
significant for a project. But start simple. Let the practice
reveal what structure is needed.

### Scope

The lookbook is read by the agent when producing experiments.
It is never harvested from — tend does not read `_lookbook.md`.
The lookbook shapes production without feeding the structural
pipeline, the same way a frame definition shapes frame-read
without being atomized.

---

## Project Lifecycle

```
emerging (momentum zone)
  → proposed (HOME proposed experiments zone)
    → active (HOME active projects)
      → cooling (engagement fades)
        → archived (explicitly closed)
          ↑
          └── reactivation possible at any point
```

### Project Schema

```yaml
---
type: project
id: project-slug
status: active | paused | cooling | completed | archived
proposed_by: user | agent
silence_means: cooling | searching
created: YYYY-MM-DD
completed: YYYY-MM-DD
---
```

The human-facing toggle for `silence_means` displays as **Agent
Contribution: Nudge** (cooling) or **Play** (searching).

Divisions can override `silence_means` individually, allowing a
single project to contain both human solo work (nudge) and
agentic collaborative production (play).

### Means

The brief includes a Means section declaring available and
aspirational modalities:

```markdown
## Means

Text and ideas for now. When MCPs become available:
- Image generation for lookbook and scene visualization
- Social media for published experiments
- Audio for the podcast-form question
```

This tells the agent what the project *wants to become*.
Constraints belong here too — what should never happen
automatically.

### Decay

**Nudge projects:** No atoms_touched on project-related atoms
in 4+ weeks AND no journal mentions AND no reactions. Reflect
notices and asks: "This project has been quiet. Should it stay
active or cool down?"

**Play projects:** 5+ experiments with zero engagement — pure
silence across multiple cycles. Reflect asks: "I've been
searching and nothing has landed. Keep looking, narrow, or cool?"

Decay is a status change, not deletion. Atoms remain. Lookbook
remains. Experiment history remains in memory. The project stops
generating proposals and leaves the active column on HOME.

**Reactivation:** If momentum returns — journal mention, atom
reinforcement, a drift stumbles into the territory — reflect
notices and suggests reactivation.

---

## Taste

Taste is not a document to be synthesized. It's already in the
vault's structure — distributed, contextual, different depending
on where you look.

**Taste at the project level:** The pattern of reactions on that
project's experiments. Queryable through reply frontmatter.

**Taste at the frame level:** What frame-read keeps returning to.
A frame's most-referenced atoms across its reflections are its
accumulated aesthetic preference.

**Taste at the atomic level:** The heat map. Which atoms get
reinforced by journals, which get yes signals, which get ignored.
atoms_touched data across time is a taste map.

**Taste as paths:** Traces. "Show me the path through everything
I said yes to this month." That trace is a picture of taste —
walked, not described. "Show me everything I said try again on" —
the boundary of taste. "Show me everything I said no to" — the
negative space, the Wald map (armor the planes where the bullet
holes aren't — see THE_COMPOST for the connection).

Reflect notices pattern shifts as thread observations: "You've
been saying yes to more embodied experiments. That's new." This
lives in the Threads section. The vault *is* the taste, readable
from multiple angles on demand.

---

## atoms_touched: The Structural Memory

Every memory entry carries structured frontmatter tracking which
atoms were involved:

```yaml
atoms_touched:
  - id: atom-slug
    action: created | reinforced | enriched | resolved | referenced | developed | challenged
    note: "optional — what was developed or challenged"
  - id: another-atom
    action: created
    uncertainty: "brief description of the doubt"
```

This makes the memory layer and the atomic layer a single
queryable system. Skills scan frontmatter (tier 1) for broad
questions and read full prose (tier 2) for narrative context.
`created` is distinct: the atom entered the structured layer.
All other values are kinds of touch. `referenced` is the minimal
touch; `reinforced`, `enriched`, `developed`, `challenged`, and
`resolved` add more specific meaning about what kind of touch
occurred. These are event labels when written and downstream
signals when later skills read memory.

### Patterns Visible Through atoms_touched

- **Hot:** High touch count, recent dates, multiple skills
- **Cold:** Created once, never touched — composted
- **Uncertain:** Open uncertainty flags, unresolved
- **Developing:** Reinforced often, enriched by tend
- **Surprising:** Unreferenced by a frame, or connected
  to something unexpected

### How Experiments Use atoms_touched

**The Compost:** Finds neglected atoms through absence — atoms
whose id appears in exactly one memory entry (creation) and
never again. Also finds unresolved uncertainties older than a
threshold. The composted body, read together, describes the
shape of creative blind spots.

**The Drift:** Gains awareness of each atom's temperature as it
visits. Reports its own character: "this drift ran warm" (active
atoms) or "ran cold" (neglected territory). Can be directed:
"drift at the tails" means prefer low touch-count atoms. May be
drawn to atoms with open uncertainty flags.

**The Séance:** A frame's most-referenced atoms (visible through
atoms_touched across frame-read memory entries) are a structural
proxy for taste. The séance can draw from these for familiar
territory or deliberately from unreferenced atoms for surprise.

**The Table:** When annotating fragments, the agent can report
each atom's weight — how active, how developed, how connected.
Arrangement rationale factors in whether an atom has been tested
by experiments or remains speculative.

**The Membrane:** Heat-based surfacing — hot atoms surface more.
Uncertainty as invitation — atoms with open flags surface with
the question noted. Occasional cold-atom surfacing for serendipity.

---

## HOME.md Integration

The Factory surfaces through specific zones on the vault dashboard.

**Active Projects** (left column): Human-committed work.

**Proposed Experiments** (right column, adjacent to active
projects): Agent offerings — both standalone project proposals
and component experiments for existing projects. Each links to
its sketch or proposal note. Grouped by destination. The visual
adjacency says: these could become your work. Your reaction
determines whether they do.

**Momentum:** What's emerging from the human's own work — journal
recurrence, atomic density, external feedback. Distinct from
proposed experiments — momentum is about the human's energy,
proposals are the agent's offerings.

**Frame Reflections:** Latest reflection per active frame.

**Vault Health:** Tend's structural assessment.

---

## The Daily Flow

The vault should feel like a studio where things appear on your
desk, not a command line where you type instructions. The daily
rhythm:

**You journal.** Write freely. Link what you want. Paste what
inspires you.

**Atomize runs.** Structures today's thinking. You don't need to
invoke this consciously once scheduling is available.

**Reflect runs.** Reads your journal, engages with your thinking,
follows threads, notices what other skills did. The reflection
appears. You read it when you're ready.

**You react.** Open the reflection reply, signal on threads, write
rationale. Or don't — silence is data too.

**You probe.** Something catches you — an atom, a clipping, a
vibe. You say "what connects to this?" or "look at this through
that lens." The probe discovers connections. You pin what
resonates to a lookbook.

**The Factory proposes.** Proposed experiments appear on HOME.
Companion sketches appear in reflections. The agent produces
because the material invited it — not because you asked.

**You curate.** Yes, no, try again, not yet. The Factory learns.

Everything else — tend, frame-read, trace, the five experiments —
happens in the background or on demand. The human's conscious
experience is: write, read the reflection, react, probe when
inspired, curate what the Factory offers. The plumbing is
invisible.

---

## The Experiments

Five experiments serve as the Factory's creative methods. Each
has a detailed execution spec in its own file. This section
describes their role in the Factory system.

> Each experiment file carries a link back: "This experiment is
> part of the Factory system. See [[THE_FACTORY]] for context."

### The Table
*Structure from below.*

Discovers project structure through arrangement rather than
top-down planning. Draft fragments accumulate, get annotated
against the atomic layer (surface, subtext, needs, leaves),
and multiple arrangements are proposed through different frame
lenses. The user curates by selection. Lookbook entries guide
the aesthetic of arrangement.

Factory role: The Table is how projects discover their own
structure. It operates within existing projects, rearranging
rather than proposing new ones.

### The Séance
*Frames that write.*

A frame produces a draft fragment from its accumulated
engagement with the material. Not a reflection — a piece of
creative writing shaped by the frame's vocabulary, concerns,
and the atoms it has most frequently referenced. Tests whether
a frame has developed something like taste.

Factory role: The Séance is the Factory producing from
accumulated sensibility. It bypasses the engagement requirement
because it proposes from the agent's taste rather than from
demonstrated human interest.

### The Drift
*Aimless wandering.*

The agent enters the atomic layer with no agenda, follows links
that interest it, and reports where it went. Self-aware about
whether it's wandering at the tails (sparse, cold atoms) or
near the norm (dense, hot clusters). The drift log is a
narrative, not a report.

Factory role: The Drift is the Factory dreaming. It bypasses
the engagement requirement to probe uncharted territory. It
may surface atoms that become lookbook entries, experiment seeds,
or project proposals — all from territory the normal escalation
path would never reach.

### The Compost
*Reading the neglected.*

Excavates abandoned material — atoms never touched after
creation, unresolved uncertainties, stalled projects. Reads
the neglected body as a text and asks: what does the pattern
of neglect reveal about creative blind spots?

Factory role: The Compost inverts the Factory's normal signals.
Instead of proposing from momentum, it proposes from absence.
A coherent pattern in neglected material might suggest a frame
the vault needs but doesn't have, or a project direction the
human has been avoiding.

### The Membrane
*Interactive surfacing.*

The continuous interaction surface — connections surfaced in
the margins while the human works, with freeze/dismiss/respond/
de-cide gestures that feed structured signal back to the agent.
The membrane is the Factory's tightest reaction loop.

Factory role: The Membrane is the always-on version of the
proposed experiments zone. When built, it replaces the
propose-and-wait cycle with real-time surfacing and reaction.
Currently aspirational — the manual reaction loop through
reflection replies serves as the pre-membrane implementation.

---

## Outbound

The Factory produces. Eventually, production flows outward.

### Templates

The vault template is the Factory minus its content. What's
portable: skills, protocol, templates, HOME layout, CSS, plugin
configurations, frame definitions (if generic). What's personal:
atoms, reflections, projects, lookbooks, memory.

**Seeded templates** ship with domain-specific starting material:
starter frames for the domain, reference atoms as gravitational
anchors, lookbook entries with curated inspiration. A course on
epistemic literacy seeds differently from a science fiction
workshop.

Seeded atoms arrive as `status: seed` with `source: course` or
equivalent provenance. They're present but proportional — as the
student's own atoms accumulate, seeded ones become a smaller
fraction. Early in the semester, course atoms are prominent.
Late in the semester, the student's own thinking dominates.

### Cross-Vault Pollination

Vaults don't share atoms — atoms carry personal provenance.
They share:

**Frames.** A frame from one vault runs against another vault's
atoms and discovers different connections. The reflection is
local. The lens is shared. Attracting a frame from someone or
somewhere else and seeing how it resolves in a foreign vault is
a rich creative act — each vault's reflection reveals different
things about the same perspective.

**Experiments.** Well-defined experiments are vault-agnostic.
The experiment template travels. The execution is personal.

**Lookbook entries with external references.** Curated inspiration
that isn't vault-specific.

The docking mechanism: shared frames import to `_frames/` with
`proposed_by: external`. They run through frame-read normally.
Output stays local.

The ambitious version: two vaults share a frame and periodically
exchange reflections. Each sees how the same lens read different
material. Future design work.

### Teaching Integration

A course vault (lessons, structure, assignments) can dock with
student Factory vaults:

**Course frames** that students import and run against their own
atoms. Personalized learning through shared perspective — every
student's reflection is different because their atoms are
different.

**Seeded experiments as assignments.** The course defines an
experiment template. Each student runs it in their vault. The
execution is personal. Results can be shared as **traces** —
maps of which atoms the student engaged, how they connected,
what path they walked. The trace shows the shape of intellectual
engagement without exposing private thinking. This is a powerful
pedagogical artifact — the instructor sees the student's
intellectual path, not just their output.

**Granular lookbook seeding.** Course inspiration and prior art,
seeded per section or chapter. Students add their own references.

**Exhibition as assignment.** Students publish traces, frame
reflections, or finished work from their vault to the course
vault. A deliberate act of sharing — the student chooses what to
exhibit. The course vault receives the artifact with provenance.
The process stays private.

**Gravitational anchors.** Seeded course atoms that attract
student thinking toward shared vocabulary. The pull is
proportional — strong early when the student's own atoms are
few, weaker later as personal thinking accumulates. The right
arc for education.

The structural question of how to process a teacher's existing
course wiki into frames, seeded atoms, and experiment templates
is future design work. The docking points are designed. The
conversion process is not yet specified.

### Art-Making MCPs

Experiments produce output that flows outward — generated images,
social posts, audio, published essays. The exhibit layer
(`_exhibits/`, activated when needed) holds artifacts with full
provenance: which atoms, which project, which experiment, which
lookbook entries influenced it. The trail extends from journal
through atoms through experiment through publication.

The brief's Means section declares which outbound channels a
project has access to. Constraints live there too.

---

## Design Principles

1. **The signal is the envelope. The rationale is the letter.**
   Always encourage rationale alongside signals. The agent learns
   more from a sentence of creative direction than from a
   category label.

2. **The measure of good work is creative usefulness.** Structure
   matters because it makes creative work possible. Precise atoms,
   well-typed relations, and consistent schemas give the vault its
   power to surprise and connect.

3. **Propose at the boundary, not the center.** The most
   informative experiments probe where the creative persona is
   most uncertain — the sparse edges, not the dense core. The
   center is already established. The edges are where de-cision
   happens.

4. **The vault is the taste.** Don't synthesize taste into a
   document. Trace it. The reaction history, the atom heat map,
   the frame's referenced atoms, the lookbook's active entries —
   these are taste, readable from multiple angles on demand.

5. **Cadence is emergent.** The density of yes signals and the
   richness of rationales determine how actively the agent
   produces. Trust builds through good early experiences. The
   autonomy gradient is natural, not configured — except for
   `silence_means`, which sets the starting condition.

6. **Each experiment is a designed perturbation.** Without the
   drift, séance, compost, and membrane, the reaction loop
   converges toward narrowing taste. The experiments keep the
   search space open by probing outside the established center.

7. **The daily flow should feel like a studio, not a command
   line.** Skills are plumbing. The experience is: write, read
   the reflection, react, probe when inspired, curate what the
   Factory offers. Buttons and HOME zones surface what matters.
   The human doesn't memorize skill names.

8. **What isn't needed yet isn't built yet.** The membrane,
   outbound channels, cross-vault docking, and autonomous
   scheduling are designed-for extension points. The Factory
   works without them.
