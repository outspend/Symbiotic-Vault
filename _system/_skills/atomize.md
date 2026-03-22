---
type: skill
id: atomize
version: 1.0
trigger: on-request
access_summary:
  _journal: read
  _inbox: read (add processed flag)
  _atoms: add
  _memory: add
---

# Skill: Atomize

Transform raw material from `_journal/` and `_inbox/` into structured
atoms in `_atoms/`.

## Purpose

Bridge the raw layer and the structured layer. Identify distinct concepts,
ideas, and entities embedded in journal entries and inbox captures. Extract
each into a single-concept atom with proper frontmatter, wikilinks, and
provenance.

## Scope

**Reads:**
- `_inbox/` — all unprocessed items (items without `processed: true`)
- `_journal/` — recent entries (default: last 7 days, or as specified)
- `_atoms/` — existing atoms, to avoid duplication and to link new atoms
  to existing ones
- `_system/_templates/atom.md` — for frontmatter reference
- `_memory/` — most recent entry from tend, frame-read, and reflect.
  For context on what other skills noticed, flagged, or were uncertain
  about. Read these before scanning sources.

**Writes:**
- New atom files in `_atoms/` with `status: seed`
- Memory entry in `_memory/` logging what was processed
- Adds `processed: true` to inbox item frontmatter (if frontmatter exists)

**Does not:**
- Modify journal entries (ever)
- Modify existing atoms
- Create frames or projects

## Procedure

1. Read `_system/_templates/atom.md` for the atom schema.
2. Read existing atoms in `_atoms/` to build awareness of what already
   exists. Note their IDs, aliases, tags, and key concepts.
3. Scan the specified source (`_inbox/`, `_journal/`, or both).
4. For each inbox item, determine its subtype — either from the
   `subtype:` frontmatter field or by inference from content:

   - **feedback**: A response to existing work. Primary action is
     enriching relations on existing atoms rather than creating new
     ones. Check the `responds_to:` field or infer which journal entry
     or project material it responds to. New atoms may still be created
     if the feedback introduces genuinely new concepts, but the emphasis
     is connecting the feedback to what already exists.
   - **reference**: External material (article, link, repo, post).
     Extract concepts as normal. Note the external source in the atom's
     prose and source field.
   - **capture**: The user's own thinking. Standard extraction.

   If frontmatter is present, use it. If prose only, infer subtype,
   source, and response relationships from content.

   Also read the `from:` field to determine whose voice shaped the item:
   - **External name** (e.g., `peter-brinson`): feedback from a
     collaborator. Enriches existing atoms with the response relationship.
   - **`agent`**: a Claude-mediated capture from a collaboration session.
     Treat as a collaborative artifact — ideas may overlap with atoms
     sourced from the human's journal. Check for reinforcement before
     creating duplicates.
   - **`user`**: the human responding to agent output (reflection replies,
     thread endorsements). Read for signals: endorsements reinforce atoms,
     project flags surface in momentum, substantive replies get atomized
     normally.
   - **Blank or absent**: infer from content as usual.

5. For each source file, identify distinct concepts that deserve their
   own atom. A concept deserves an atom if it:
   - Has identity (you could name it)
   - Has potential connections (it relates to other ideas in the vault)
   - Has development potential (there's more to say about it)
6. For each identified concept:
   a. Check if an existing atom already covers it — compare the concept
      against each atom's `id`, core concept name, and any names listed
      in its `aliases:` field. If a match is found, note the connection
      but do not create a duplicate. If the source uses a name for that
      concept that isn't yet in the atom's `aliases:`, flag it in the
      memory entry as a candidate alias for tend to confirm.
   b. Assess whether the concept is a *concept* (descriptive, stable)
      or a *claim* (positioned, arguable). Set `kind:` accordingly.
      If a claim references a concept that doesn't yet have its own
      atom, identify both — create each separately and link them.
   c. Create a new file in `_atoms/` using the atom template.
   d. Set `status: seed`.
   e. Set `source:` to the journal entry or inbox item it came from.
   f. Write a brief prose body capturing the core idea.
   g. Identify related atoms (new or existing) to connect to.
   h. Write the `## Relations` section. For each related atom from
      step g, add one entry: `- [[atom-slug]]: one sentence describing
      the epistemic relationship`. Each preamble should name a directional
      epistemic relationship: grounds, extends, challenges, instantiates,
      derives from, enables, applies to, complements. Avoid vague preambles
      like "relates to," "connects to," or "resonates with" — if you can't
      name the relationship precisely, the connection may not be strong
      enough to record.
   i. Suggest initial `tags:` based on the content.
7. When marking an inbox item `processed: true`, also fill any blank
   frontmatter fields that can be confidently inferred from content:
   - `subtype` — feedback, reference, or capture
   - `from` — if a person or source is clearly named
   - `responds_to` — if the item clearly responds to a specific
     journal entry or project file
   Only fill fields the agent is confident about. Leave blank if the
   inference is uncertain.
8. Write a memory entry to `_memory/` with frontmatter including
   `atoms_touched`: log every atom created (`action: created`), every
   existing atom reinforced by new material (`action: reinforced`), and
   every borderline case that wasn't extracted but has a specific doubt
   (`uncertainty: "..."`). Then in prose:
   - What sources were scanned
   - How many atoms were created
   - Notable connections observed
   - **Uncertainties:** concepts that were borderline, alias candidates
     flagged for tend, anything not resolved from atomize's vantage point
   - Any cross-skill flags resolved from other skills' memory entries
     (note which skill raised it, what evidence resolved it)

## Judgment Calls

- **Granularity:** One atom per concept. If an idea has sub-ideas that
  could stand alone, split them. If two ideas only make sense together,
  keep them as one atom.
- **Duplication:** If a stream entry covers ground that an existing atom
  already captures, do not create a new atom. Instead, note in the memory
  entry that the existing atom was reinforced and by what.
- **Naming:** Atom filenames should be descriptive slugs:
  `highlights-and-hides.md`, `llm-common-topologies.md`. Prefer clarity
  over brevity.
- **Source structure is not atom structure.** A concept that appears as an example, a bullet point, or a parenthetical in one source may deserve its own atom if it has independent identity and development potential. Evaluate every concept on its own merits, not by its position in the document it came from.
- **Referenced external concepts:** When a concept from an external intellectual tradition (philosophy, religion, science, etc.) appears as an example, citation, or sub-item within a vault concept, evaluate it independently before folding it in. If it has standing beyond its role in that context — connecting to multiple domains in the vault, not just the one where it was cited — create a separate atom and link them. Do not let a concept's subordinate position in a source determine its status in the vault.
- **Feedback enriches, capture creates.** When an inbox item is
  feedback on existing work, the primary value is the response
  relationship — how the feedback challenges, sharpens, or validates
  existing atoms. New atoms from feedback should be rare. When an
  inbox item is capture, standard extraction applies.
- **User work is always extractable.** A two-sentence mention of an external concept may be too thin for an atom. But a two-sentence mention of something the user *did* is never too thin — the user is the source, and the source can always develop it. When a performance piece, experiment, creative project, or conversation is captured briefly — even as an aside or example within a longer note — extract it as its own atom. Do not fold user work into another atom as merely an example or test case.
