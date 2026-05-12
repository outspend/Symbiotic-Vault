---
type: system-design
status: draft
created: 2026-05-01
updated: 2026-05-01
context: design spec for the vault as a guided return machine
---

# Guided Return Machine

## Purpose

This document describes the vault as a **guided return machine**.

The aim is not perfect recall.
The aim is to make later return to prior material intelligent, selective, and creatively useful.

The vault should help a project find its way back to the right earlier journals, web captures, Instagram/context captures, atoms, frames, and project traces without pretending that any reduced layer can fully stand in for source material.

This is a design for **re-entry**, not total retention.

---

## Core Claim

Every layer of the vault is lossy.

That loss is not a flaw to eliminate. It is a condition to design around.

The system succeeds when it preserves enough:

- provenance
- conceptual patterning
- project relevance
- candidate source zones

to let a future project reopen the right material at the right depth.

---

## The Problem This Design Solves

Raw journals and captures are fertile but overwhelming.

Atoms and frames help reduce and pattern that material, but reduction is always perspectival:

- what the human notices is not identical to what an agent notices
- what an atom extracts is not identical to what a future project will need
- what one frame foregrounds, another frame can hide

Therefore:

- the journal cannot be the daily working surface for every future project
- the atom layer cannot be treated as exhaustive memory
- the frame layer cannot be treated as neutral retrieval

The vault needs a way to preserve **paths back** into sources rather than only preserving distilled statements about them.

---

## Short Form

The vault is not a memory palace.

It is a guided return machine:

- sources hold fullness
- atoms hold reusable patterns
- frames hold directional readings
- projects hold temporary purpose
- traces preserve why something was read this way, now

The system does not promise that a future project can avoid rereading sources.
It promises that rereading can become selective instead of blind.

---

## Primary Flow

The intended trajectory is:

`journal / inbox capture / web clipping / instagram-context -> atom -> frame -> project`

But the crucial movement is the return path:

`project -> frame -> atom -> candidate source zones -> selective reread`

Without that return path, the vault becomes a one-way abstraction funnel.

With that return path, the vault becomes a reusable creative substrate.

---

## Layer Model

### 1. Journals

Journals are the human's raw, high-density, low-structure surface.

They should remain free.
They should not be burdened with heavy classification or project-awareness at time of writing.

Journals are valuable because they preserve:

- chronology
- local wording
- mood
- anecdote
- ambiguity
- what was visible before later reframing

Journals are often richer than any later extraction.

Design implication:
the system must not require journals to become neat in order to become useful.

### 2. Captures

Captures include web clippings, pasted correspondence, screenshots, Instagram references, and other externally sourced material.

A capture without context decays quickly.

Therefore captures should preserve at least:

- what the artifact is
- why it mattered at capture time
- what it might relate to
- any immediate local frame or emotional register

This context does not need to be polished.
It needs to make later return legible.

### 3. Atoms

Atoms are not summaries of source material.
Atoms are reusable pattern notes.

An atom should:

- name a pattern, concept, claim, method, person, event, or question
- state the insight cleanly enough to reuse
- justify itself from source material
- point toward sources that still may contain more than the atom extracted

Atoms compress.
They do not exhaust.

This means an atom is both:

- a pattern container
- a return handle

### 4. Frames

Frames are not buckets or domains.
Frames are active lenses.

A frame:

- cares about some things more than others
- uses particular vocabulary
- foregrounds certain tensions
- re-reads atoms and sources from a directional point of view

Frames are where the vault becomes interpretive.

A frame should not claim to represent the final truth of a topic.
It should make a specific line of inquiry stronger and more legible.

Frames are also the natural place to record where selective rereading may be valuable.

### 5. Projects

Projects are temporary but demanding readers of the vault.

A project should not interrogate the whole archive directly.
It should begin from prior structuring:

- relevant frames
- relevant atoms
- prior traces
- identified source zones

Then, when needed, it should reopen only promising source material.

Projects do not inherit perfect memory from the vault.
They inherit guidance.

### 6. Traces

Trace notes and canvases preserve situated readings.

They answer questions like:

- why did this material matter here?
- what did this project pull forward?
- what did this reading leave unused?
- what should be revisited later?

Traces are not redundant bookkeeping.
They are the record of how the vault was actually traversed.

---

## Design Principle: Reduction Must Remain Reversible Enough

Because every extraction is partial, the system should preserve multiple ways back.

Not one canonical interpretation.
Not one official summary.
Not one irreversible reduction.

Instead, each layer should leave behind:

- a statement of what it pulled out
- a pointer to where it came from
- a hint that more may still be there

This is enough to make a later reread purposeful.

---

## Loss Model

The vault should explicitly assume:

- journals contain more than atoms
- captures contain contextual cues that may not survive atomization
- atoms highlight some patterns and miss others
- frames clarify and distort
- projects discover needs earlier layers could not predict

This means no structured layer should be evaluated by whether it prevents all future rereading.

The correct question is:

Does this layer reduce future search cost while preserving the possibility of deeper return?

---

## What Each Layer Is Responsible For

### Journals are responsible for:

- preserving raw thought
- preserving local sequence
- preserving emergence before cleanup

### Captures are responsible for:

- preserving external artifacts
- preserving why they mattered when saved
- preserving enough local context to avoid later opacity

### Atoms are responsible for:

- identifying reusable patterns
- stabilizing names for ideas without freezing them
- linking source material to higher-order thought
- nominating source zones worth revisiting

### Frames are responsible for:

- organizing atoms directionally
- giving projects interpretable lenses
- surfacing tensions, doubts, and concerns
- identifying where rereading under this lens may be productive

### Projects are responsible for:

- adopting a temporary purpose
- deciding which frames and atoms matter now
- creating a local memory of what has been used
- documenting what remains unresolved or under-read

### Traces are responsible for:

- preserving the actual path of reasoning
- showing why a reading happened
- making later return cheaper

---

## Retrieval Model

There are three different retrieval modes in this vault.

### 1. Literal retrieval

This is name-based and phrase-based.
It is what string search and file search do well.

Examples:

- finding "Michael Scroggins"
- finding "Would you die for me?"
- finding "suede jacket"

Useful for:

- named entities
- repeated phrasing
- exact motifs
- known references

Weak for:

- conceptual relatives
- shifted vocabularies
- ideas that migrate names across projects

### 2. Pattern retrieval

This is what atoms are for.

Examples:

- this scene instantiates a pattern of quiet refusal
- this artifact belongs to a larger concern about charismatic control
- this anecdote supports a claim already named elsewhere

Pattern retrieval is stronger than string search, but always partial.

### 3. Framed retrieval

This is what frames are for.

Examples:

- reread these atoms not as commune history but as recruitment logic
- reread these journals for social capture rather than personal memory
- reread these captures for aesthetic pedagogy rather than style reference

Framed retrieval is the most selective and the most interpretive.

The system should support all three modes.

---

## Guided Return

Guided return is the core mechanism of the vault.

It means:

1. a project begins with a present concern
2. it consults relevant frames
3. those frames point toward atoms
4. those atoms point toward source zones
5. the project rereads only the most promising sources
6. the project records what it learned in its own local memory

This is different from two failure modes:

### Failure mode 1: total re-read

Every new project has to interrogate all prior journals and captures from scratch.

This is exhaustive but too expensive.

### Failure mode 2: total trust in abstraction

Every new project relies only on atoms and frames as if they fully preserve source material.

This is cheap but brittle.

Guided return is the middle path:

- selective
- provenance-aware
- open to surprise
- affordable enough to repeat

---

## Source Zones

A source zone is any cluster of material likely to reward rereading.

Examples:

- a single journal note
- several adjacent journal days
- a clipping with surrounding correspondence
- a note cluster around a person
- a trace canvas and its attached artifacts

The point of a source zone is practical.

A future project does not always need one perfect note.
It often needs the neighborhood where a pattern first became visible.

Therefore atoms, frames, and projects should be allowed to point not only to exact sources but also to source zones.

---

## Candidate Return

One of the system's most important moves is the ability to say:

This note has been touched, but not exhausted.

That means the system needs a category like:

- candidate return
- source zone
- underused source
- not yet metabolized

The exact field or label can vary.
The design requirement is the same:

the vault must distinguish between:

- source already used once
- source fully understood

Those are not the same.

---

## Human and Agent Roles

The human and the agent do not pull the same things from material.

That is not an error.
It is part of the value.

### The human tends to preserve:

- charge
- memory
- taste
- obsession
- what feels important

### The agent tends to preserve:

- pattern
- recurrence
- structural relation
- retrieval usefulness
- possible adjacency

### The project tends to demand:

- whatever serves its current purpose

The system should not force these into one canonical extraction.

Instead it should permit multiple pulls to coexist:

- human pull
- structural pull
- project pull

The disagreement between those pulls is often meaningful.

---

## Multiple Readings

The same source can support multiple valid extractions.

A journal entry might become:

- an atom about a social pattern
- a frame example about charisma
- a project source for a comic scene
- a personal note about what still feels unresolved

This plurality is not duplication.
It is evidence that the source remains alive.

The vault should support this by allowing:

- multiple atoms to cite the same source
- multiple frames to use the same atoms differently
- multiple projects to revisit the same source zone

---

## Project Memory

A project should develop its own local memory rather than repeatedly reopening the whole vault.

This local memory can live in:

- a project brief
- project notes
- trace notes
- project canvases

Its purpose is to remember:

- which sources were touched
- what they yielded for this project
- what was left out
- what might be worth reopening later

Project memory is how guided return becomes cumulative instead of repetitive.

---

## Canvas Role

Canvases are especially useful when a project has:

- multiple source types
- evolving structure
- active ambiguity
- competing hypotheses
- image or scene logic that benefits from spatial arrangement

A project canvas should not try to be the whole archive.

It should act as a live arrangement surface for:

- source artifacts
- extracted notes
- structural proposals
- dormant options
- underused material
- reread candidates

In this design, a canvas is not only a map of what has been used.
It is also a map of where return pressure is accumulating.

---

## External Capture Principle

External artifacts only remain useful if the vault preserves the local reason they were taken in.

A clipping or Instagram post without local context becomes:

- hard to retrieve by meaning
- hard to distinguish from adjacent examples
- hard to relate to future projects

Therefore the system should prefer:

- saved artifact
- plus immediate human context
- plus later atomization if warranted

Not every capture becomes an atom.
But every meaningful capture should remain interpretable.

---

## Selective Rereading

Selective rereading is not a failure of the system.
It is one of the system's main outputs.

What matters is that rereading is:

- narrowed
- justified
- framed
- documented

The vault should not promise:

- no future rereading
- perfect anticipation of future projects
- one-time extraction that solves everything

The vault should promise:

- better candidate discovery
- better provenance
- less blind scanning
- more meaningful returns

---

## What the System Should Optimize For

- free human writing
- rich provenance
- lightweight but reusable abstraction
- multiple valid readings
- affordable project startup
- explicit incompleteness
- good candidate generation for reread
- preservation of creative surprise

---

## What the System Should Avoid

- forcing journals to become structured forms
- assuming one atom can stand in for a source
- assuming one frame can stand in for a topic
- treating prior extraction as exhaustive
- forcing every note to become immediately project-relevant
- re-reading the entire archive for every project
- pretending string search alone can find conceptual relatives

---

## Design Implications for Existing Vault Layers

### Journals

Keep them minimal.
Do not load project obligations into the daily writing surface.

### Captures

Strengthen context capture so external references do not become dead matter.

### Atoms

Treat atoms as both abstractions and return handles.
They should justify and point back.

### Frames

Treat frames as active reread lenses, not just philosophical statements.

### Projects

Treat project hubs as cumulative local memory, not just declarations of intent.

### Traces and Canvases

Use them to preserve how a particular reading of material came to matter now.

---

## Success Condition

The vault succeeds as a guided return machine if a project can do the following:

1. articulate what it currently needs
2. find plausible frames for that need
3. find atoms those frames make newly relevant
4. identify a manageable set of source zones
5. reread only those sources
6. preserve what that reread changed

If that loop works, the vault is doing its job.

---

## Final Statement

This system does not eliminate the creativity of rereading.
It depends on it.

The design assumes that every future act of interpretation is partly new.

The vault's role is not to replace that act.
Its role is to help the next act begin in the right neighborhood, with the right prior shapes visible, and with the trail behind them still intact.
