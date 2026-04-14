---
type: system
purpose: design note — Tana comparison
created: 2026-03-13
append_to: VAULT_DESIGN.md at user's discretion
---

# Design Note: This Vault vs. Tana

> **Admonition.** This vault claims to be a better creative thinking
> environment. That claim must be earned and deepened, not assumed.
> The comparison below identifies the architectural bet — deferred
> structure via collaborative interpretation rather than immediate
> structure via typing at entry. Every design choice, every new
> skill, every experiment should be tested against this bet: does
> it make the vault a better place to *think creatively*, or just
> a better place to *organize*? If the answer is organize, Tana
> already won. We are playing a different game.

---

## Push This Further: Research Directions

These are prompts for deep research sessions — conversations with
the agent, literature hunts, or design provocations meant to
strengthen and interrogate the vault's central claim.

**Incubation and the cognitive science of not-structuring.**
Research on creative incubation (Wallas, Dijksterhuis) suggests
that unstructured downtime is where novel connections form. If
structure-at-entry imposes premature closure, there may be
empirical support for protecting raw surfaces. Investigate: what
does cognitive science say about when structuring helps vs. hinders
creative thinking? Is there a measurable cost to classifying an
idea at the moment you have it?

**Perspectival reasoning and creative insight.** The vault's frames
are its strongest differentiator — not filters but argued readers.
Investigate: what does research on perspectival reasoning, cognitive
flexibility, and conceptual blending (Fauconnier & Turner) say
about how multiple viewpoints generate insight? Can framed
re-reading of the same material be shown to produce ideas that
single-perspective review doesn't?

**Reinterpretation as creative method.** The vault assumes that
revisiting old material through new lenses is generative. This
echoes hermeneutic philosophy (Gadamer's "fusion of horizons") and
literary theory (reception aesthetics, Iser). Investigate: what
traditions formalize rereading and reinterpretation as creative
acts? How do they describe what happens when familiar material
becomes unfamiliar through a shifted frame?

**Flow, cognitive load, and the cost of dual-tasking.** Tana
requires simultaneous writing and structuring. Research on cognitive
load theory (Sweller) and flow states (Csikszentmihalyi) suggests
dual-tasking degrades both activities. Investigate: is there
evidence that separating composition from organization produces
better creative output in either or both?

**Argued arrangement vs. predetermined structure.** The table
experiment proposes that structure should emerge from below through
negotiation between perspectives. This resonates with design
thinking (diverge then converge), improvisational theater (yes-and),
and evolutionary approaches to creativity (Simonton's blind
variation). Investigate: what frameworks describe how creative
structure emerges from unstructured material? What role does
argument between perspectives play?

**Serendipity by design.** The vault aspires to be an "arrangement
of serendipity." Research on serendipity in information science
(Erdelez, Foster & Ford) distinguishes engineered serendipity from
randomness. Investigate: what makes a system serendipitous rather
than merely disorganized? What structural properties increase the
rate of useful unexpected connections?

**Taste as accumulated attention.** The séance experiment asks
whether a frame, given enough accumulated reflections, develops
something like taste. This connects to Bourdieu's concept of
habitus, to aesthetic philosophy on cultivated judgment, and to
recent work on LLM alignment as preference learning. Investigate:
what does it mean for a computational agent to develop taste? Is
accumulated attention a sufficient substrate?

---

## The Core Difference

Tana's insight is that the editor and the graph should be the same
thing. Every bullet is a node. Supertags make unstructured notes
into typed objects. The writing surface *is* the structured surface.
There's no gap to bridge because there was never a gap.

This vault makes the opposite bet. The raw surface is sacred — the
user writes freely, no tags, no types, no structure required. The
graph is a secondary layer that the agent builds from the writing
through judgment. Two distinct surfaces, bridged by collaboration.

## What Each Costs and Gains

**Tana's cost:** You can never just write. Every keystroke is a
graph operation. The environment is always structured, always typed.
There's no raw surface. No journal entry that's just a messy pour
of thinking.

**Tana's gain:** Immediacy. You type something, you see its
connections instantly. Structure is always current.

**This vault's cost:** Structure arrives later, via atomize and
tend. You write something and have to invoke a skill or ask a
question to see what it connects to.

**This vault's gain:** Freedom to think without structuring, then
the ability to see unstructured thinking through argued perspectives
that didn't have to be defined at the moment of writing.

## The Deeper Architectural Difference

The systems disagree about when structure should happen.

Tana says: at the point of entry.

This vault says: after the fact, by a collaborator who reads with
more context than the writer had when they wrote.

This has consequences for everything downstream:

**Frames.** In Tana, frames are filtered views — show me all nodes
tagged #claim that also have #epistemology. Powerful but mechanical.
In this vault, a frame is a reader — it traverses the atomic layer
with concerns and vocabulary and produces a reflection with its own
character. Tana can filter. This vault can interpret.

**Experiments.** The table, the séance, the drift, the compost —
these are impossible in Tana. Not because it lacks features, but
because its architecture assumes structure is the goal. This vault
assumes meaning is the goal and structure is one way to get there.

**Supertags vs. kinds.** Tana's supertags are more flexible than
this vault's `kind:` enum — users define new types freely. The
fixed enum is intentional (it keeps atomize's judgment consistent)
but worth watching. If the user finds themselves wanting a kind
that isn't in the list, that's a signal the enum should grow.

## Where Tana Is Ahead

Immediacy of graph feedback. The membrane aspiration is this
vault's answer — surfacing connections in the margins while the
user works — but it isn't built yet. Tana has it now.

## Summary

Tana is a better structured note-taking tool. This vault is a
better creative thinking environment. They don't compete because
they don't believe the same things about what writing is for.
