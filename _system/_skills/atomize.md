---
type: skill
id: atomize
version: 1.1
trigger: on-request
access_summary:
  _journal: read
  _inbox: read + update frontmatter
  _atoms: read + add
  _memory: read (most recent entry from tend, frame-read, reflect) + add
---

# Skill: Atomize

Transform raw material from `_journal/` and `_inbox/` into structured
atoms in `_atoms/`.

## Purpose

Bridge the raw layer and the structured layer. Identify distinct
concepts, ideas, and entities embedded in journal entries and inbox
captures. Extract each into a single-concept atom with proper
frontmatter, wikilinks, and provenance.

## Scope

**Reads:**
- `_inbox/` — all unprocessed items (items without `processed: true`)
- `_journal/` — recent entries (default: last 7 days, or as specified
  by the user)
- `_atoms/` — existing atoms, to avoid duplication and to link new
  atoms to existing ones
- `_memory/` — most recent entry from tend, frame-read, and reflect
  for cross-skill context
- `_system/_templates/atom.md` — for frontmatter reference

**Writes:**
- New atom files in `_atoms/` with `status: seed`
- Memory entry in `_memory/` with `atoms_touched` frontmatter
- Updates inbox item frontmatter (`processed: true` and inferred fields)

**Does not:**
- Modify journal entries (ever)
- Modify existing atoms (tend handles enrichment)
- Create frames or projects

## Procedure

1. Read `_system/_templates/atom.md` for the atom schema.

2. Read `_atoms/_index.md` to build awareness of what already
   exists. The index lists every atom by frame grouping with ID,
   kind, and one-sentence summary. Use it to identify potential
   duplicates and connection targets before reading full atom
   prose.

   When a candidate concept from the source material plausibly
   matches an existing atom (by ID, summary, or semantic overlap),
   read that atom's full prose and aliases to confirm or rule out
   duplication. Do not read every atom in full — use the index as
   the entry point and read selectively.

   If the index is stale or missing, fall back to reading all
   atoms directly. Note this in the memory entry so tend knows
   to regenerate.

3. Read the most recent memory entry from tend, frame-read, and
   reflect for cross-skill context. Treat `referenced` as a generic
   touch and pay special attention to reflect entries marked
   `developed` or `challenged`:
   - `developed` means reflect added new substance in this atom's
     territory. Check nearby journal and inbox material for
     extractable concepts or claims that deserve a new atom.
   - `challenged` means reflect questioned the atom's premise or
     framing. Check whether the challenge introduces a distinct
     counter-claim or new concept that deserves its own atom.

4. Scan the specified sources. If the user specified a scope, follow
   it. Otherwise, scan all inbox items where `processed:` is `false`
   (determined by frontmatter, not filename) and journal entries from
   the last 7 days.

5. **Classify each inbox item.** Two independent assessments:

   **Subtype** — determine from the `subtype:` field or infer from
   content:
   - `feedback` — a response to existing work. Primary action is
     enriching relations on existing atoms. New atoms are created
     only if the feedback introduces genuinely new concepts.
   - `reference` — external material. Extract concepts as normal.
     Note the external source in the atom's prose and source field.
   - `capture` — the user's own thinking. Standard extraction.

   **Sender** — read the `from:` field or infer from content:
   - A named person (e.g., `peter-brinson`): external feedback.
     Enrich existing atoms with the response relationship.
   - `agent`: a collaborative artifact. May rephrase or develop
     ideas the user already captured in their journal. Check
     carefully for reinforcement of existing atoms before creating
     new ones.
   - `user`: the human responding to agent output. Parse reaction
     signals (see step 8). Substantive rationale alongside signals
     gets atomized normally.
   - Blank: infer from content as usual.

6. **Identify and extract atoms.** For each source file, identify
   distinct concepts that deserve their own atom. A concept deserves
   an atom if it has identity (you could name it), potential
   connections (it relates to other ideas), and development potential
   (there's more to say about it).

   For each candidate:
   a. Check if an existing atom already covers it — compare against
      each atom's `id`, prose body, and `aliases:` field. If a match
      is found, note reinforcement in the memory entry. `reinforced`
      is atomize's specific touch for repeated appearance: the concept
      showed up again, but no new atom was needed. If the source uses
      a name not yet in the atom's `aliases:`, flag it as a candidate
      alias for tend.
   b. Assess whether the concept is a *concept* (descriptive, stable)
      or a *claim* (positioned, arguable). Set `kind:` accordingly.
      If a claim references a concept that doesn't yet have its own
      atom, create both separately and link them.
   c. Create a new file in `_atoms/` using the atom template.
   d. Set `status: seed`.
   e. Set `source:` to the journal entry or inbox item it came from.
   f. Write a brief prose body capturing the core idea.
   g. Write the `## Relations` section. For each related atom (new
      or existing), add one entry: `- [[atom-slug]]: one sentence
      describing the epistemic relationship`. Each preamble should
      name a directional relationship: grounds, extends, challenges,
      instantiates, derives from, enables, applies to, complements.
      Avoid vague preambles like "relates to" or "connects to" — if
      you can't name the relationship precisely, the connection may
      not be strong enough to record.
   h. Suggest initial `tags:` based on the content.

7. **Process inbox frontmatter.** For each inbox item scanned, mark
   `processed: true`. Also fill any blank frontmatter fields that
   can be confidently inferred from content: `subtype`, `from`,
   `responds_to`. Only fill fields the agent is confident about.
   Leave uncertain fields blank.

8. **Parse reaction signals.** When an inbox item is a reflection
   reply (`subtype: feedback`, `from: user`, with `responds_to:`
   pointing to a reflection), scan for `→` prefixed lines. For each:
   - Extract the signal word: yes, no, try-again, not-yet
   - Extract any text after the signal as the note
   - Match to the preceding blockquote thread
   - Write parsed reactions into the reply's frontmatter:
     ```yaml
     reactions:
       - thread: thread-slug
         signal: yes | no | try-again | not-yet
         note: "optional rationale text"
     ```

9. **Write memory entry** to `_memory/` with:
   ```yaml
   atoms_touched:
     - id: atom-slug
       action: created | reinforced
       uncertainty: "optional — if the judgment could go either way"
   ```
   Also include in the body:
   - What sources were scanned
   - How many atoms were created
   - Notable connections observed
   - Borderline cases: concepts considered but not extracted,
     with reasoning

## Judgment Calls

- **Granularity:** One atom per concept. If an idea has sub-ideas
  that could stand alone, split them. If two ideas only make sense
  together, keep them as one atom.
- **Naming:** Atom filenames should be descriptive slugs:
  `highlights-and-hides.md`, `llm-common-topologies.md`. Prefer
  clarity over brevity.
- **Source structure is not atom structure.** A concept that appears
  as an example, a bullet point, or a parenthetical in one source
  may deserve its own atom if it has independent identity and
  development potential. Evaluate every concept on its own merits,
  not by its position in the document it came from. This includes
  concepts from external intellectual traditions — if a philosophical
  or scientific concept has standing beyond the specific context
  where it was cited, create a separate atom and link them.
- **User work is always extractable.** A two-sentence mention of an
  external concept may be too thin for an atom. But a two-sentence
  mention of something the user *did* is never too thin — the user
  is the source, and the source can always develop it. When a
  performance piece, experiment, creative project, or conversation
  is captured briefly — even as an aside or example within a longer
  note — extract it as its own atom. Do not fold user work into
  another atom as merely an example or test case.
