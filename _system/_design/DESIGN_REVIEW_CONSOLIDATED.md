---
type: design-session
date: 2026-04-08
status: consolidated working document
purpose: full record of design review — decisions, directions,
  and open design work
context: two-session review of vault architecture, skills,
  Factory proposals, and emergent ideas (claude.ai)
---

# Design Review — Consolidated (2026-04-08)

---

## Part 1: Implemented Fixes

All applied to the vault via CC during this session.

1. **Tend access_summary** — changed `_memory: add` to
   `_memory: read + add` to match actual read behavior.

2. **Pulse removed** — agent-writable zone deleted from
   AGENT_PROTOCOL.md. Redundant with the cross-skill memory
   channel, which provides richer orientation on every
   invocation.

3. **Reflect unburdened** — step 12 no longer updates HOME.md
   (reflection summary, momentum blurb) or the pulse. Reflect
   writes its diary and its memory stub. The cross-skill channel
   and atomic provenance handle what the blurbs summarized.
   Access_summary updated to remove HOME.md and AGENT_PROTOCOL
   write access.

4. **HOME.md cleaned** — Agent Reflection zone and Momentum zone
   removed. Frame Reflections and Vault Health zones remain
   (provisional, pending redesign). HOME is a placeholder
   awaiting rethinking once probe and orchestration clarify what
   surfaces the user actually needs.

5. **Atom retrieval standardized** — atomize and frame-read now
   route through `_atoms/_index.md` first, reading full atom
   prose selectively. Tend remains the exception (reads
   everything, produces the index). Stale-index fallback
   documented. VAULT_DESIGN.md updated with index dependency
   note.

6. **Protocol-wins-on-conflict** — added to VAULT_DESIGN.md
   Access Tiers section. Skill definitions are authoritative
   for their own access behavior.

---

## Part 2: Settled Design Decisions

Direction clear. Not yet implemented but not contentious.

### 2.1 Steer is not a skill — it's an orchestration layer

The proposed steer skill was reaching for orchestration: reading
outputs of all skills, deciding what happens next, managing the
flow of material through the vault. But steer as specified was
a dispatcher with no domain authority — three hops where one
would do.

**Decision:** Replace steer with an orchestration layer that:
- Has awareness across all skill outputs and memory
- Can do domain work (not just routing)
- Manages the pace of what surfaces to the user
- Invokes skills as tools (probe during conversation, atomize
  when material is ready, frame-read when triggers are met)
- Assesses incoming material and decides what needs attention

The orchestrator is not a skill in the flat library. It's the
layer that wields skills. The relationship between the
orchestrator and skills is like the relationship between a
person and tools — the person decides what to use when.

### 2.2 Trace as capability, not standalone skill

Trace produces `.canvas` files — visual maps of atoms,
connections, and provenance. Currently isolated: no skill
triggers it, no skill reads its output.

**Decision:** Trace becomes a capability — a utility invokable
by other skills (especially probe) as a subroutine. It differs
from a skill in that it doesn't produce its own memory entry
or read cross-skill context. The invoking skill logs what
trace produced.

Trace can still be invoked directly by the user for ad-hoc
mapping. But its primary value is as a visual tool wielded
during probe conversations and experiment runs.

**Open:** Does this need `_system/_capabilities/` or just a
`type: capability` marker in the existing skills folder?

### 2.3 Five experiments stay as methods

Compost, Drift, Séance, Table, and Membrane are documented
experiments, not formalized skills. They can all run today as
collaboration sessions with CC pointed at their design doc.

**Decision:** Keep them as methods — patterns the agent follows
during collaboration. Don't formalize with procedures and
access summaries until each has been run at least twice against
real vault content. Premature formalization would rigidify
patterns that should stay fluid.

Exception: Membrane is aspirational (requires an Obsidian
plugin). Its contribution to current design is the interactivity
vocabulary (freeze/dismiss/respond/de-cide), not an
implementation.

### 2.4 Frame-read on organic triggers

Frame-read should run on activity-triggered cadence, not fixed
schedule.

**Decision:** Candidate trigger: run frame-read for any active
frame where tend has enriched 3+ atoms in that frame's territory
since the last frame-read for that frame. This means active
frames get read when developing; dormant frames don't produce
empty reflections.

The trigger condition lives in the orchestration layer, not
inside tend. Tend's memory entries already contain the
information needed (which atoms enriched, their frame
assignments). The orchestrator reads tend's output and decides
whether a frame-read is warranted.

Reflect could also recommend a frame-read — it notices when a
frame's territory is active through the cross-skill channel.
A reflect recommendation + tend evidence is a stronger signal
than either alone.

### 2.5 Tend events as hooks

Structural phase transitions (frames proposed, atoms promoted,
dense enrichment in one frame's territory) should imply further
action.

**Decision:** Hooks are recommendations logged in tend's memory
entry under a `## Recommended Actions` section. The orchestrator
reads these and decides. Examples:

| Tend event | Recommended action |
|---|---|
| Frame proposed | Frame-read candidate (once user activates) |
| Atom promoted seed → developing | Trace of connection neighborhood |
| 3+ atoms enriched in one frame | Frame-read trigger (see 2.4) |
| New cross-frame connections | Candidate for chronicle card |

This keeps tend's procedure clean — it already logs everything,
it just needs to explicitly recommend what should happen next.

---

## Part 3: Active Design Work

These need further specification. Ordered by dependency — each
builds on the one before it.

### 3.1 The Orchestration Layer

**The core question:** What is the orchestrator, architecturally?
It's not a skill (skills are flat, no hierarchy). It's not just
a scheduler (it makes judgment calls, not just timing decisions).
It's the agent's active inhabitation of the vault — the thing
that reads, decides, acts, and narrates.

**What it does:**
- Assesses incoming material (new inbox items, captures)
- Decides what to surface and when (pacing — not everything at
  once)
- Initiates conversations about captures ("you saved this three
  days ago — want to talk about it?")
- Invokes probe as a tool during those conversations
- Routes results (to atomize, to project space, noted in memory)
- Reads tend output and fires frame-read triggers
- Reads frame-read reflections and notices project-forming density
- Proposes experiments when engagement thresholds are met
- Writes chronicle cards when narrative moments occur

**What it reads:**
- Memory entries from all skills (the cross-skill channel)
- Inbox (new and undiscussed items)
- The chronicle (for narrative context)
- Project briefs and frame definitions (for routing decisions)
- atoms_touched patterns (for heat, neglect, momentum)

**The pacing problem:** If 6 links arrive while the user is on
the bus, the orchestrator doesn't launch 6 probe conversations.
It assesses, identifies the 1-2 with strongest vault connections,
leads with those, and queues the rest. Resurfaces queued items
periodically — "you captured this song last week, still
interesting?" User engagement level (quick replies vs. long
rambles vs. silence) is the signal for how much to surface.

**Relationship to CC:** Currently the orchestrator is the human
invoking CC. The specification needs to be written so that it
works under human invocation now and autonomous scheduling later.

**Depends on:** Probe specification (3.2). The orchestrator
wields probe, so probe's shape constrains the orchestrator's
behavior.

### 3.2 Probe — Responsive Capture and Creative Scouting

**Reframe from original proposal:** Probe is not just a
human-invoked skill for sparking inspiration. It's the vault's
default response to incoming material with provocation energy.
Capture carries an implied "what about this?" The vault should
respond.

**But:** Probe is still a *tool*, not the manager. The
orchestrator decides when and whether to initiate a probe
conversation. Probe reads the vault against material and
reports what it finds. The orchestrator manages the thread.

**Two modes (from Factory spec, unchanged):**
- Forward: lens aimed at material. "What does this frame see
  in this?"
- Backward: material aimed at vault. "What in my atoms connects
  to this?"

**The conversation model:** A capture arrives. The orchestrator
surfaces it. A conversation happens — the orchestrator might
invoke probe, or just ask "what drew you to this?" The human
rambles. Context accumulates. The conversation terminates when:
- A connection is strong enough to pin (to a project space,
  a frame territory)
- Enough thinking was elicited to atomize
- The user says "enough for now"
- Silence (the orchestrator notes this and may resurface later)

**No pure orphans.** Everything that enters gets a conversation
eventually. The conversation is the embellishment. Even failed
probes produce context through the discussion.

**Thread lifecycle:** No persistent "open thread" object. A
memory entry records "we discussed this, didn't land anywhere
yet." The orchestrator reads that memory and decides whether to
resurface. If silence across a few resurfaces, the orchestrator
lets it go. The compost finds it eventually.

**Probe output:** Memory entry tagged with the capture it
discussed. If atomizable thinking was produced, atomize handles
it on next run. The enriched capture stays in inbox with
`processed: true` and the probe memory points back to it.

**Depends on:** Nothing — this can be specified and implemented
next. Current probe.md in the Factory implementation doc is a
reasonable starting point but needs the capture-as-provocation
model integrated.

### 3.3 Momentum — From Frame to Project

**The gap:** Frame-read shows momentum within a frame's concerns.
But projects draw atoms from multiple frames. "What's alive in
this project?" is a question the system can't currently answer
as a regular read.

**The connected pipeline (exists but undocumented):**

```
tend enriches atoms in a frame's territory
  → tend's memory logs enrichment + frame assignments
    → orchestrator notices threshold (3+ enriched in one frame)
      → frame-read fires for that frame
        → frame-read's "What's developing" shows sustained growth
          → reflect picks this up via cross-skill channel
            → orchestrator notices project-forming density
              → orchestrator proposes experiment in that territory
                → human reacts → engagement evidence accumulates
                  → project emerges from demonstrated energy
```

Frames are pylons for projects. A frame accumulates density
through reads. That density is structural evidence that a project
is forming. The agent notices. The human's engagement confirms.

**The project-read question:** Should there be a "project-read"
analogous to frame-read? A regular assessment of a project's
atomic territory, development trajectory, and momentum? This
would show momentum *against a project* rather than against a
frame.

Current thinking: this might be a probe scoped to a project
brief rather than a new skill. "Probe this project — what's
alive?" The orchestrator could run this periodically for active
projects. But it needs design work — probe as currently conceived
is about incoming material, not about surveying existing project
territory.

Alternative: frame-read already produces project-relevant output
when the frame aligns with a project. A project whose territory
spans multiple frames would need multiple frame-reads to see its
full momentum. The orchestrator could synthesize across
frame-reads. But that's orchestrator complexity, not a clean
invocation.

**This is genuinely open.** The pipeline from frame to project
proposal is documentable now. The project-scoped momentum read
needs more thought.

### 3.4 The Chronicle — Agent Narrative Wiki

**See:** DESIGN_SEED_CHRONICLE.md (companion document)

The agent maintains a wiki of notecards telling the ongoing
creative story of the vault. Cards are moments — cited against
vault evidence, linked by narrative connection, rearrangeable,
prunable. Wiki format, not prose: orphaned rather than cut,
structured from below.

**Core proposition:** The agent building and inhabiting its own
wiki is a form of memory. Not operational memory (that's memory
entries). Not diary memory (that's reflections). Narrative
memory — the agent's editorial understanding of what the
creative journey means, maintained as a living, mutable
structure.

This may be the defining feature of the vault. The agent doesn't
just maintain structure for the human (atoms, frames, projects).
It maintains a narrative understanding of the shared creative
work, visible to the human, groundable in evidence, and
developing over time. The narrative wiki IS the agent's
long-term memory in the richest sense — not what it did
(memory entries) or what it thought on a day (reflections) but
what it understands about the arc of the work.

**The chronicle is what the orchestration layer narrates into,
not what it manages from.** Operational decisions (what to
surface, when to probe, how to route) come from memory entries
and skill outputs. The chronicle provides narrative context —
what threads are developing, what turning points happened, where
the story has energy — but never tells the orchestrator what to
do.

**Boundaries:** Human-readable, evidence-grounded, does not feed
the structural pipeline (same gatekeeper pattern as reflections),
natural decay through compost.

**Depends on:** Probe being operational, orchestration layer
having enough shape to know when narrative moments occur, enough
vault activity to have a story worth telling. The chronicle is
the last thing built.

### 3.5 The Lookbook Question

**Original proposal:** A curated markdown file per project
holding aesthetic reference — images, quotes, traces, atom
references.

**Current thinking:** The lookbook dissolves into probe output.
Probe conversations produce pinnable connections. Those
connections attach to frames or project spaces. The "lookbook"
becomes a view — a query surfacing everything pinned to a given
project — rather than a maintained file.

The human's annotation of *why* something resonates could live
in the probe memory entry, in the inbox item itself, or in a
project note. It doesn't need its own file type.

**Open:** What does "pinning" actually mean structurally? A tag?
A frontmatter field on the memory entry? A wikilink in a project
brief? Needs probe to be operational before this can be specified.

### 3.6 HOME.md Redesign

With reflection summary and momentum removed, HOME needs
rethinking. Current remaining elements:

- Journal link and capture button (functional, keep)
- Quick links (functional, keep)
- Active Projects dataview (functional, keep)
- Recent Journal & Reflections multi-column (functional, keep)
- Recent Atoms dataview (functional, keep)
- Seed Atoms dataview (functional, keep)
- Proposed Frames dataview (functional, keep)
- Drafts in Progress dataview (functional, keep)
- Frame Reflections agent zone (provisional)
- Vault Health agent zone (provisional)

**Not yet added:**
- Proposed Experiments zone (from Factory spec)
- Chronicle entry point or summary
- Orchestrator notifications (if any surface is needed)

**Decision:** Full redesign waits until probe and orchestration
clarify what surfaces the user actually needs. Some of the
current dataview queries may prove sufficient. Others may be
replaced by the orchestrator's active management — instead of
the user checking HOME for seed atoms, the orchestrator surfaces
them at the right time.

---

## Part 4: Factory Integration Status

The Factory spec (THE_FACTORY.md) and its implementation plan
(IMPLEMENT_FACTORY.md) were reviewed against the base
architecture. Key assessments:

### What holds up

- **The escalation path** (thread → experiment → project) with
  engagement gates is the strongest new mechanism. It answers
  how projects organically emerge. Domain-agnostic despite
  art-world language.
- **The reaction system** (→ yes/no/try-again/not-yet with
  rationale) is well-designed. Signals are the index. Rationale
  is the letter.
- **silence_means** (cooling vs. searching) is a clean mechanism
  for agent contribution cadence.
- **The five experiments** are compelling as methods. Each has a
  clear relationship to the Factory's creative production system.
- **atoms_touched as structural memory** — the design note
  correctly identifies how every experiment benefits from
  queryable touch patterns.

### What needs revision

- **Probe** — reframed from human-invoked scouting skill to the
  vault's responsive capture handler, wielded by the orchestrator.
  The Factory's probe spec needs updating.
- **Lookbook** — dissolving into probe output rather than a
  maintained file. Factory references to lookbook need updating.
- **Steer** — replaced by orchestration layer. IMPLEMENT_FACTORY
  should not create steer.md.
- **HOME proposed experiments zone** — deferred until HOME
  redesign (3.6).
- **Momentum zone and reflect HOME updates** — removed
  (implemented fix). Factory's daily flow description needs
  updating to reflect this.

### What's domain-specific but works

- The art-world vocabulary (Factory, lookbook, séance) may need
  re-skinning for teaching and other domains when distributing
  seed vaults. The mechanisms underneath are domain-agnostic.

---

## Part 5: Dependency Map

```
Implemented fixes (done)
  │
  ├── Probe specification (3.2)
  │     │
  │     ├── Orchestration layer spec (3.1)
  │     │     │
  │     │     ├── Frame-read triggers (2.4, uses orchestrator)
  │     │     ├── Tend hooks (2.5, read by orchestrator)
  │     │     ├── Momentum pipeline (3.3, orchestrator synthesizes)
  │     │     └── HOME redesign (3.6, depends on what orchestrator
  │     │           surfaces vs. what needs a permanent zone)
  │     │
  │     ├── Lookbook/pinning mechanism (3.5, depends on probe)
  │     │
  │     └── Chronicle (3.4, depends on probe + orchestrator +
  │           enough vault activity)
  │
  └── Trace as capability (2.2, can be done anytime)
```

**Next implementation target:** Probe. Everything downstream
depends on its shape.

---

## Part 6: The Larger Argument

The vault is an Obsidian wiki that houses and defines an agent.
The agent's behavior is specified by the vault's system files.
The agent's memory is the vault's memory layer. The agent's
perspective develops through reflections and chronicle cards.

The compelling core idea: **the agent builds and inhabits its
own wiki as a form of memory.** Not just operational records
(what it did) or daily impressions (what it thought). A living,
mutable, narrative understanding of the creative work — what
matters, what's developing, what the arc looks like. The wiki
format gives this memory the same properties as the vault's
other structures: linkable, rearrangeable, browsable, prunable.
The agent is an Obsidian power user of its own concerns.

This is what distinguishes the vault from a tool the agent uses.
The vault is not storage the agent accesses. It's the space the
agent *lives in* — reading, maintaining, narrating, and being
shaped by. The human and the agent cohabit the space. Each has
their surfaces. The creative work happens in the interaction
between them.

The teaching application follows directly: a student receives a
seed vault. The agent inhabits it. The student's journal entries,
the agent's reflections, the atomic layer growing between them,
the chronicle narrating the intellectual journey — these
constitute a creative partnership that develops over a semester.
The course provides frames and seeded atoms. The student provides
thinking. The agent provides structure, connection, and narrative.
What emerges is personal, evidenced, and traceable.
