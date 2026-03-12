---
type: system
purpose: design critique from session
created: 2026-03-11
---

# Design Critique

A self-assessment of the vault design against its stated goals,
plus missed opportunities from the human/agent surface separation.

---

## The Goals (from VAULT_VISION.md)

**Cohabitation:** A symbiotic space where human creativity and agentic
activity sustain each other. Neither displaces the other. Each has
their own surfaces, rhythms, work.

**Provenance:** The lineage of ideas is preserved and traceable.
Random becomes rough becomes refined, and that trajectory is visible.
The trail is the treasure.

**Enrichment:** An evolving practice of finding innovative ways to
supplement, enrich, and reflect creative activity via agentic means.
Not a solved system.

**Emergence:** A substrate from which agents with distinct creative
viewpoints can be grown, given depth by the documented trail of their
development.

**Guiding principles:** Ideas are the center. The trail is the
treasure. The practice evolves.

---

## Where It Falls Short or Might

### Cohabitation: More Like Segregation

This is the big one. We drew such a clean line between human and
agent surfaces that they're barely cohabiting — they're roommates
who leave notes on the fridge. The human writes in `_journal/` and
`_projects/`. The agent writes in `_atoms/` and `_memory/`. They
meet only when the human explicitly invokes a skill or asks a
question.

Real cohabitation would mean encountering the agent's thinking
*in the course of your own work*, not in a separate folder you go
browse. Right now if you're writing a draft and the agent noticed
something relevant last Tuesday during a tend run, you'd never know
unless you went to `_memory/` and looked. The insight exists but
it's behind a wall.

The vision says "each has their own surfaces" but it also says they
"sustain each other." Right now the sustaining is one-directional —
you feed the vault, the agent maintains it, and you have to come
asking to get anything back. The agent's contributions don't show
up in your field of vision while you're working.

### Provenance: Strong for Atoms, Weak for Everything Else

The atom schema has a clear `source:` field tracing back to journal
entries. That chain works. But provenance for the *interesting*
stuff — how a journal musing became an atom, how atoms clustered
into a frame, how a frame reflection influenced a draft — lives
scattered across `_memory/` entries with no structural way to trace
the full arc.

If someone asked "show me how this finished essay developed from
first mention to final draft," the agent could probably reconstruct
it from memory entries, but there's no guaranteed path. The
provenance is *implied* by timestamps and semantic matching rather
than *structural*. For the trail to truly be the treasure, you need
to be able to walk it, and right now it's more of a scavenger hunt.

### Enrichment: Three Skills Is a Floor, Not a Ceiling

We designed three skills and declared the system open to new ones,
but nothing in the architecture actively encourages the discovery
of new enrichment patterns. The vision says "what we cannot build
yet, we do not foreclose" — but we also don't have a mechanism for
noticing what's missing.

Who notices that a fourth skill would be useful? You do, in
conversation, like we've been doing. But the vault itself has no
feedback loop where the agent observes its own limitations and
proposes new capabilities. Tend proposes frames but nothing proposes
skills.

### Emergence: The Hardest Goal, Barely Addressed

The vision says agents with "distinct creative viewpoints" should
be "grown" from vault contents. We've laid the groundwork — frames
define perspectives, memory entries accumulate per-frame reflections,
and that body of observations *could* seed a specialized agent
persona.

But right now a frame is stateless between invocations. When you
run frame-read, it reads its past reflections, but it doesn't
*develop*. It doesn't have preferences that sharpen over time, or
aesthetic commitments that solidify, or a growing sense of what it
finds interesting. It performs a fresh reading every time. The memory
entries are there but they're a log, not a developing consciousness.

For emergence to actually happen, a frame would need to accumulate
something more than reflections — something like a living summary
that evolves, a set of commitments that update, a record of what it
found surprising. We haven't built any of that, and the current
skill definitions don't create it.

### The Practice Evolves: Mostly Honored

This one the design does reasonably well. The extension points are
noted. The structure is minimal enough to grow. But there's a subtle
risk: the surface rule ("agent never writes into human surfaces") is
so firm that it could calcify into a constraint that prevents exactly
the kinds of new collaboration patterns the vision wants to stay
open to.

---

## Missed Opportunities From the Separation

### The Agent Could Annotate, Not Just Reflect

What if atoms could appear as marginal notes alongside your drafts?
Not inserted into your prose, but rendered by Obsidian as linked
references in the sidebar or backlinks pane. Right now atoms link
*to* their source journal entries, but they don't link *to* the
drafts they're relevant to. If tend or a collaboration session wrote
atoms that linked to specific project files, Obsidian's backlinks
panel would show you relevant atomic context while you're writing —
without touching your text.

The surface rule holds — nothing is inserted into your writing. But
the agent's work *appears* on your surface through Obsidian's own
linking mechanics. The separation is maintained at the file level
while the experience is integrated.

### Memory Could Be Warmer

Right now `_memory/` is a log archive. But what if the most recent,
most relevant memory entries surfaced contextually — not just in the
home note's agent zone, but as pinned notes in a project folder, or
as a "last time the agent thought about this" sidebar when you open
an atom? Obsidian's embedded transclusions could pull memory excerpts
into places where they'd be useful without the agent writing into
those files.

### The Home Note Could Be More Alive

The current HOME.md has dataview queries and agent-refreshable zones,
but it's essentially a static dashboard with dynamic data. What if
the agent could maintain a short "what I'd suggest working on today"
section that synthesizes recent journal themes, project status, and
frame observations? Not a to-do list — a creative collaborator's
sense of where the energy is. This flirts with the surface rule but
stays within the designated agent zone.

### Frames Could Talk to Each Other

Nothing in the design lets one frame's reflection inform another
frame's reading. They're parallel and independent. But the most
interesting creative insights often come from the collision of
perspectives — what the art-practice frame sees contradicting what
the systems-thinking frame assumes. A cross-frame synthesis step
(maybe as part of tend, maybe as a new skill) could surface these
tensions.

---

## The Deepest Tension

The cohabitation principle asks for symbiosis while the surface rule
enforces separation. Obsidian's own features — backlinks,
transclusions, graph view, the sidebar — offer ways to let the
agent's work appear on human surfaces without the agent writing
there. We haven't leveraged any of that yet.
