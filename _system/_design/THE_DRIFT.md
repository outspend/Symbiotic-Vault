---
type: system
purpose: design aspiration — the drift
created: 2026-03-11
---

# The Drift

An experiment in aimless wandering through the atomic layer — the
agent's version of dreaming.

---

## The Feeling

You leave the vault. You come back. Something happened while you
were away. The agent wandered through your ideas, followed links
that interested it, and left a log of where it went and what it
noticed. Not a report you asked for. Not a task you assigned.
A dream the vault had about itself.

You open the drift log and find: "I started at
[[highlights-and-hides]], which led me to [[llm-common-topologies]],
and I found myself thinking about whether your constraint game is
actually a special case of a method you haven't named yet —
something about deliberately disabling an LLM's strongest patterns
to see what's underneath. I followed that thread to
[[vault-as-personalized-learning]] and noticed that the vault
itself is doing something similar — constraining how agents access
information in order to see what kind of thinking emerges from the
constraint."

You didn't ask for this. It might be nothing. It might be the
connection that reorganizes everything.

---

## Tails and Norms

The drift should know where it's wandering. Some paths through the
atomic layer are well-trodden — dense clusters with many links,
atoms that get referenced constantly, the familiar core of your
thinking. Other paths are at the tails — sparse connections, orphan
atoms, links that cross unexpected domains, the edges where ideas
barely touch.

The drift log should report its own character:

**At the norm:** "I spent most of this drift in the dense cluster
around conversational AI and writing practice. The paths here are
well-worn and I followed them to their usual conclusions."

**At the tails:** "I spent most of this drift at the edges. I
found myself following a chain from [[data-center-hemingway]]
through a tenuous connection to [[vault-as-personalized-learning]]
that only holds if you read 'personalization' as 'constraint'
rather than 'customization.' This is speculative."

**Mixed:** "I started at the norm and drifted outward. The core
cluster is stable but there are three peripheral atoms that might
be developing their own gravity."

The degree of speculation is the drift's self-awareness. It knows
when it's on solid ground and when it's reaching. The user can
calibrate: today I want a drift at the tails. Or: stay close to
the norm, I want to see what's solid.

---

## The Experiment

### Invocation

The user says "drift" — optionally with a bias:
- "drift" — no constraint, go anywhere
- "drift at the tails" — seek the edges, the sparse, the unlikely
- "drift from [[atom-name]]" — start somewhere specific, then wander
- "drift around [project-name]" — stay in the gravitational field
  of a project but don't follow its structure

### Procedure

1. Pick an entry point (random atom if none specified, or the
   specified starting point).
2. Read the atom. Follow one of its links — not the most obvious
   one, not the most connected. Follow the one that's *interesting*.
3. At each new atom, read it, sit with it, and decide where to go
   next based on what catches attention. This is deliberately
   non-systematic. The drift is not a graph traversal algorithm.
   It's an act of attention.
4. At each step, note: what drew you here, what you notice, what
   connects to something unexpected.
5. When the drift has visited 5-10 atoms (not too few to find
   anything, not so many it becomes a survey), stop.
6. Write the drift log.

### The Drift Log

Write to `_memory/` with:

```yaml
---
type: memory
skill: collaboration
method: drift
bias: none | tails | norm | from-atom | around-project
start: [starting-atom-id]
date: YYYY-MM-DD
character: norm | tails | mixed
---
```

The body is a **narrative**, not a list. Write it as a path walked:
"I began at X. What struck me was... This led me to Y, because...
The connection between Y and Z is surprising because... I ended at
W, and the thing I keep coming back to is..."

End with one of:
- **A question** the drift surfaced but can't answer
- **A connection** that didn't exist before and might be worth
  making explicit (a suggestion for tend)
- **A silence** — something the drift expected to find but didn't

---

## Dreaming

The drift is the vault dreaming. Dreams consolidate — they take
the day's input and process it without agenda, finding connections
that waking attention is too focused to see. The drift does the
same for the vault's accumulated thinking.

The ideal form of the drift is autonomous — it runs when you're
away, when the vault is idle, and you return to find it has
dreamed. This requires scheduled invocation (a future extension
point). But even invoked manually, the drift's value is that it
breaks the human-initiated pattern. Every other interaction with
the vault starts from a question or a task. The drift starts from
curiosity with no destination.

Over time, the drift logs in `_memory/` become their own body of
work — a record of where the vault's attention wandered, what it
found at the edges, what kept surfacing. Patterns in the drift
logs might be the strongest signal for what wants to be written
next.

---

## Connection to Other Experiments

**The Table:** The drift might produce a notecard. If the agent
finds something during a drift that feels like a scene or an
argument, it could produce a fragment for an active project.
Not assigned — offered.

**The Compost:** The drift might wander through composted material
and find something ready to resurrect. The neglected atom that
the drift visits and finds newly relevant is a resurrection with
provenance.

**The Séance:** A drift could end in a séance — the agent wanders
into a cluster that a frame has deep history with, and the drift
becomes a spontaneous act of frame-voiced writing.

**The Membrane:** The drift is the membrane's background process.
What the membrane surfaces in your working session is informed by
what the drift discovered during idle time.

---

## Status

Experiment. Can be run now as manual invocation ("drift"). The
autonomous version (runs during idle) requires scheduled invocation
and is noted as a future extension point. The self-reporting of
tails vs. norm is achievable today — the agent can assess link
density and cluster proximity as it walks.
