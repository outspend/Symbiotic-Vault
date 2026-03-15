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
4. For each source file, identify distinct concepts that deserve their
   own atom. A concept deserves an atom if it:
   - Has identity (you could name it)
   - Has potential connections (it relates to other ideas in the vault)
   - Has development potential (there's more to say about it)
5. For each identified concept:
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
   e. Set `source:` to the stream entry or inbox item it came from.
   f. Write a brief prose body capturing the core idea.
   g. Identify related atoms (new or existing) to connect to.
   h. Write the `## Relations` section. For each related atom from
      step g, add one entry: `- [[atom-slug]]: one sentence describing
      the epistemic relationship`. Not "connects to" — be precise:
      supports, challenges, extends, instantiates, is a case of, etc.
   i. Suggest initial `tags:` based on the content.
6. If an inbox item has frontmatter, add `processed: true` to it.
7. Write a memory entry to `_memory/` with:
   - What sources were scanned
   - How many atoms were created
   - Notable connections observed
   - Any concepts that were borderline (not extracted but worth watching)

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
