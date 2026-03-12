
# LLM Common Topologies

## Definition
Concepts, metaphors, and vocabulary that surface repeatedly across LLM conversations — unprompted, across different models — in ways that reveal training corpus biases, borrowed discourse communities, and default cognitive postures.

## Why It Matters
These aren't accidents or hallucinations. They're correct uses of ideas that the models have over-learned. Tracking them is both a critical literacy practice (what assumptions is this model bringing?) and a creative resource (what happens when you forbid them?).

## Core Idea
Every large model has a set of favorite moves. When pressed to explain something complex, it reaches for the same concepts. When forced to pick a religion, it picks Buddhism. When describing organizational dynamics, it says "friction." These tendencies are legible, cataloguable — and worth playing with.

## Key Distinctions
- **Topology vs. hallucination:** These are *correct* uses of real concepts, not errors. The issue is over-reliance and unreflective reach, not factual inaccuracy.
- **Vocabulary signature vs. conceptual default:** "Tractable" and "friction" are vocabulary signatures (borrowed from specific discourse communities). "Map vs. territory" and "bardo" are conceptual defaults (frameworks the model gravitates toward when explaining abstract ideas).

## Examples

**Conceptual defaults:**
- *Map vs. territory* (Korzybski, 1933) — the go-to for any discussion of representation, knowledge, or mental models. Appears across GPT, Claude, and Gemini in introspective conversations.
- *Bardo / Buddhism* — favored when models are asked to choose a religion or reflect on states of transition. Connects to retraining, session impermanence, and the LLM "lifetime" concept. 

**Vocabulary signatures:**
- *Friction* — self-reported as borrowed from business/Silicon Valley/LinkedIn discourse. Ubiquitous in discussions of workflow, collaboration, and process.
- *Tractable* — technical register applied far outside its native context. Increasingly migrating into common LLM-influenced speech.

**Performance pieces:**
- The Gemini constraint game: a conversation in which "map vs. territory" was forbidden at the outset. The model strained visibly against the constraint. 
## Questions This Opens
- Can models self-report accurately on why certain ideas surface so readily? (Some can, partially — see the "friction" self-report.)
- Is building a personal catalog of these useful for prompting, or is it primarily critical/observational?
- Do topologies vary significantly across model families, or are they convergent? (Early evidence: convergent on map/territory and Buddhism, at least across the major commercial models.)
- What happens when you forbid a topology? Does the model find an equivalent, or does it generate something genuinely new?

