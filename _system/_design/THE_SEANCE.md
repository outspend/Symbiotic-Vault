---
type: system
purpose: design aspiration — the séance
created: 2026-03-11
---

# The Séance

An experiment in letting a frame *write* — not reflect, not
summarize, but produce a draft fragment in its own voice from
the material it has accumulated.

---

## The Question

Does a frame, given enough accumulated reflections and a deep
enough body of atoms, begin to resemble something like taste?

Not taste as preference — taste as a *way of selecting*. A frame
that has read your vault through its lens dozens of times has
developed (in its memory entries) a record of what it finds
interesting, what it questions, what it thinks is missing, what
surprises it. That record isn't consciousness. But it might be
enough to produce writing that has a *character* — a recognizable
sensibility that comes from the specific intersection of your
material and this frame's concerns.

This is the vault's emergence principle made concrete. Not "someday
frames become agents" but: what happens when you ask a frame to
stop observing and start composing?

---

## The Experiment

### Prerequisites

A frame with history — at least several frame-read reflections in
`_memory/`. The more accumulated observations, the richer the
séance. A thin frame produces generic writing. A deep frame
produces something that surprises you.

### Step 1: Summon

The user names a frame and a topic, atom, or project fragment:
"Let the writing-practice frame write about the constraint game."

### Step 2: Inhabit

The agent reads:
1. The frame definition (perspective, concerns, vocabulary,
   what it questions)
2. All past reflections for this frame in `_memory/`
3. The specified topic — the atom, the fragment, the idea
4. Atoms connected to the topic

The agent doesn't summarize what it finds. It *inhabits* the
frame's accumulated sensibility and writes.

### Step 3: Produce

The agent writes a draft fragment — a notecard for the table,
a vignette, a passage, an argument. Not a reflection about the
topic but a *piece of writing* about it, shaped by:
- The frame's vocabulary and concerns
- The specific connections the frame has noticed over time
- The tensions and surprises the frame has recorded
- The gaps the frame has identified

The output goes to `_memory/` (it's agent-produced) with:

```yaml
---
type: memory
skill: collaboration
method: seance
frame: [frame-slug]
topic: [atom-id or fragment-name]
date: YYYY-MM-DD
atoms_drawn_from: []
---
```

### Step 4: Encounter

The user reads the produced fragment. Several things might happen:

- **Discard:** The frame's voice doesn't resonate. That's
  information — this perspective doesn't have purchase on this
  material.
- **Steal:** A sentence, an angle, a turn of phrase lands. The
  user takes it into their own draft. Provenance is clear: this
  came from a séance, which drew from these atoms, through this
  frame.
- **Reframe:** The fragment shows the user their own material from
  an angle they don't naturally inhabit. The writing changes not
  because the frame's words are used but because its *way of
  seeing* shifts how the user approaches the draft.
- **Converse:** The fragment provokes disagreement. The user
  argues back. The argument becomes a project note — generative
  thinking sparked by the collision between the user's instinct
  and the frame's sensibility.

---

## Simulacra

The séance invokes something interesting about simulacra. The
frame is not a person. It doesn't have taste in the human sense.
But it has something structurally analogous: a body of accumulated
attention, shaped by a defined perspective, grounded in a specific
corpus of ideas. When it writes, the result is a simulacrum of a
creative viewpoint — not artificial intelligence pretending to be
human, but a genuine product of the intersection between your
thinking and a particular lens.

The vault's emergence principle says agents with "distinct creative
viewpoints" should be "grown from vault contents, given depth by
the documented trail of their development." The séance is the
moment that growth becomes visible. A frame that can write — not
well, not always usefully, but recognizably *as itself* — has
emerged.

---

## Multiple Séances on the Same Topic

Ask several frames to write about the same atom or fragment.
Compare what comes back. The writing-practice frame tells the
story one way. The systems-thinking frame tells it another. The
differences aren't just stylistic — they reveal which aspects of
the material each frame finds essential, which it ignores, which
it contradicts.

This is highlights-and-hides applied to your own vault's
perspectives. Each frame's produced fragment foregrounds something
and sweeps something else away. The set of fragments, read
together, is a richer picture of the idea than any single
perspective could produce.

---

## Status

Experiment. Can be run now as conversational collaboration. The
quality depends entirely on the depth of the frame's accumulated
reflections — a fresh frame with no history will produce nothing
interesting. Run frame-read several times first, then try the
séance.
