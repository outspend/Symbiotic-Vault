---
type: system
purpose: design note — atoms_touched and the experiments
created: 2026-03-18
---

# Design Note: How atoms_touched Enriches the Experiments

The structured memory frontmatter (`atoms_touched` with action and
uncertainty fields) creates queryable patterns across the vault's
history. Each experiment gains something from this.

---

## The Compost

The compost was designed to excavate neglected material. With
atoms_touched, neglect becomes precisely measurable:

**Created but never touched again.** A tier 1 scan across all
memory finds atoms whose id appears exactly once — in the entry
that created them. Nobody came back. These are the composted
atoms, identifiable without reading a single prose body.

**Reinforced but never enriched.** The concept keeps appearing
in journals (atomize logs `reinforced`) but tend never connected
it to anything. The idea has heat in the human's thinking but no
structural foothold. That's a different kind of neglect than
silence — it's an idea the human keeps circling that the graph
hasn't absorbed.

**Uncertainty that was never resolved.** An atom flagged uncertain
by one skill, and no subsequent entry carries `action: resolved`
for that id. The doubt is still open. The compost could
specifically gather unresolved uncertainties as a body and ask:
what do these open questions have in common? Is there a pattern
in what the vault can't decide about?

The compost report becomes data-driven rather than impressionistic.
It can say: "12 atoms have never been touched since creation.
5 atoms have been reinforced 3+ times but never enriched. 3
uncertainties remain open from more than 30 days ago. Here's
what this neglected body looks like when read together."

---

## The Drift

The drift wanders through the atomic layer with no agenda. With
atoms_touched, the drift gains awareness of each atom's history
as it visits:

**Temperature.** An atom that's been touched 8 times across
multiple skills is hot — it's active, connected, developing. An
atom touched once and abandoned is cold. The drift can report its
own character by the temperature of the nodes it visits: "this
drift ran warm — I kept encountering atoms in active development"
or "this drift ran cold — I spent most of my time in territory
nobody has visited in weeks."

**Tails vs. norms, measured.** The drift already wanted to report
whether it was wandering at the tails or near the norm. Now it
has a metric: atoms with high touch counts across many skills are
the norm (the dense center of the vault's activity). Atoms with
low or zero touch counts are the tails. The drift can calibrate
deliberately: "drift at the tails" means "prefer atoms with low
touch counts."

**Unresolved uncertainties as attractors.** The drift could be
drawn to atoms with open uncertainty flags — wandering toward the
places where the vault has questions it hasn't answered. "I visited
[[writing-teaching-synthesis]] because atomize flagged it as
uncertain six weeks ago and nothing has resolved it. Reading it
now, alongside what tend has connected since then, I think..."

The drift becomes not just aimless wandering but *informed*
wandering — aware of what's been neglected, what's unresolved,
what's hot, and choosing where to go based on that awareness.

---

## The Table

The table annotates draft fragments against the atomic layer and
proposes arrangements. With atoms_touched, the annotations gain
temporal depth:

**Subtext with history.** When annotating a fragment, the agent
currently reads atoms and identifies connections. With a tier 1
scan, it can also say: "This fragment connects to
[[highlights-and-hides]], which has been reinforced 6 times and
enriched by tend twice. This is one of the most active ideas in
the vault." Versus: "This fragment connects to
[[impression-enrichment-via-llm]], which was created once and
never touched again. This is a peripheral idea." The annotation
carries a sense of the concept's *weight* in the vault, not just
its existence.

**Needs/Leaves informed by development state.** A fragment whose
atoms are all heavily developed and interconnected makes different
demands on the reader than one whose atoms are seeds and orphans.
The arrangement rationale can factor this in: "This fragment
should come later because its concepts need the grounding that
earlier fragments (with more developed atoms) provide."

**Arrangement provenance.** When the table generates multiple
arrangements and the user picks one, that selection touches atoms
(the ones included in the chosen sequence become `referenced` in
the memory entry). Future table runs on the same project can see
which atoms were included in prior arrangements and which were
always excluded — a structural record of editorial decisions.

---

## The Séance

The séance asks a frame to write — to produce a fragment from
accumulated engagement with the material. With atoms_touched,
the séance can draw on a richer substrate:

**Taste as measurable preference.** A frame's accumulated
reflections reference certain atoms repeatedly (visible in
frame-read memory entries as `action: referenced`). The pattern
of what a frame keeps returning to — its most-referenced atoms —
is a structural proxy for taste. The séance can lean into this:
produce writing that draws from the atoms this frame has
referenced most, because those are the ideas this lens finds
most compelling.

**Surprise from the unreferenced.** Conversely, the séance could
deliberately draw from atoms the frame has *never* referenced —
ideas that exist in the vault but have never lit up through this
lens. The writing that results would be the frame encountering
unfamiliar material for the first time. That's a different kind
of creative output than writing from accumulated familiarity.

**Frame development visible.** Compare a frame's referenced atoms
across its first reflection and its most recent. The shift in what
it pays attention to is the frame's development arc. A séance
produced early in a frame's life will sound different from one
produced after months of accumulated reflections. The atoms_touched
record makes this arc traceable.

---

## The Membrane

The membrane aspires to surface connections in the margins while
the human works. With atoms_touched, the membrane's surfacing
algorithm has more signals:

**Heat-based surfacing.** Atoms that have been touched recently
and frequently are more likely to be relevant to what the human
is working on right now. The membrane could prioritize surfacing
connections to hot atoms.

**Uncertainty as invitation.** Atoms with open uncertainty flags
could be surfaced with the uncertainty noted — "this concept has
an open question: [the uncertainty string]." The human sees the
question in the margin and might answer it through their writing,
or dismiss it, or freeze it for later. The uncertainty becomes
an interactive prompt.

**Neglect as discovery.** The membrane could occasionally surface
a cold atom — something that hasn't been touched in weeks — as
a serendipity move. "This idea has been quiet. Does it connect to
what you're writing now?" This is the drift principle applied to
the membrane: sometimes the valuable connection is to something
you forgot about.

---

## The Pattern Across All Experiments

Every experiment benefits from the same thing: atoms_touched turns
the vault's history from prose narrative into queryable data. The
experiments can ask:

- What's hot? (high touch count, recent dates, multiple skills)
- What's cold? (created once, never touched again)
- What's uncertain? (open uncertainty flags, unresolved)
- What's developing? (reinforced often, enriched by tend)
- What's surprising? (unreferenced by a specific frame, or
  connected to something unexpected)

These questions were always answerable by reading every memory
entry in full. atoms_touched makes them answerable by scanning
frontmatter — which means the experiments can ask them cheaply,
at scale, as part of their normal operation.

The structured memory frontmatter is not just bookkeeping. It's
the substrate that makes the experiments intelligent about the
vault's own development. The agent doesn't just know what ideas
exist. It knows which ideas are alive, which are neglected, which
are contested, and which keep surprising it. That awareness is
what turns the experiments from interesting prompts into genuine
creative tools.
