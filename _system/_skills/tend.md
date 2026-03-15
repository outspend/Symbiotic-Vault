---
type: skill
id: tend
version: 1.1
trigger: on-request
access_summary:
  _atoms: read + modify (links, tags, aliases, status)
  _frames: read + add (proposed frames)
  _projects: read (notes, drafts — human surfaces, read-only)
  _memory: add
---

# Skill: Tend

Cultivate the structured layer. Enrich atoms, discover connections,
promote maturity, and harvest new concepts from active project notes
and drafts.

## Purpose

The atomic layer grows through atomize but matures through tending.
This skill reads across `_atoms/` and active `_projects/` to:
- Discover connections between atoms that don't yet link to each other
- Promote atom status as they accumulate connections and references
- Harvest new concepts from growing project notes and drafts back into atoms
- Propose new frames when atom clusters show coherent perspective

## Surface Rule

**Tend never modifies human surfaces.** It reads `_projects/*/notes/`
and `_projects/*/drafts/` for concept harvesting, but never writes to
them. All writes go to `_atoms/`, `_frames/` (proposed), and `_memory/`.

## Scope

**Reads:**
- `_atoms/` — all atoms, their frontmatter, links, and content
- `_frames/` — existing frames, to avoid proposing duplicates
- `_projects/*/notes/` — generative thinking per division (read-only)
- `_projects/*/drafts/` — composed writing per division (read-only)

**Writes:**
- Updates to existing atoms: new wikilinks, updated tags, new aliases,
  status promotion (`seed` → `developing`, `developing` → `stable`)
- New atom files in `_atoms/` with `status: seed` (harvested from notes/drafts)
- Proposed frame files in `_frames/` with `status: proposed`
- Memory entry in `_memory/` logging all changes and observations

**Does not:**
- Modify stream entries, inbox items, or any human surface
- Modify project briefs, notes, or drafts
- Modify or delete the prose body of existing atoms (only frontmatter,
  wikilinks, aliases, and the `## Relations` section)
- Activate proposed frames (that's the human's decision)

## Procedure

### Part 1: Enrich Atoms

1. Read all atoms. Build a mental map of concepts, links, and tags.
2. Identify atoms that share concepts but don't link to each other.
   For each proposed new connection:
   a. Append to the `## Relations` section of both atoms:
      `- [[the-other-atom]]: one sentence describing the relationship
      (supports, challenges, extends, instantiates, etc.)`.
      If an atom predates the Relations section, add the section first.
   b. Note the connection and rationale in the memory entry.
3. Review atom status:
   - `seed` → `developing`: atom has 3+ inbound/outbound links,
     or has been referenced by a frame-read reflection.
   - `developing` → `stable`: atom has been linked by multiple other
     atoms, referenced in a collaboration trace, and has substantive content.
   - Use judgment. These thresholds are guidelines, not hard rules.
4. **Detect and record aliases.** Scan atoms, recent journal entries,
   and active project notes for cases where the same concept is referenced
   under a different name — a synonym, abbreviation, variant spelling,
   informal title, or alternate framing. For each atom where a distinct
   alternate name is observed:
   a. Add the alternate name(s) to the atom's `aliases:` field.
   b. Note each addition in the memory entry: which atom, what name was
      added, and which source surfaced it.
   Judgment: an alias is a name that points to the *same* concept, not
   a related concept with its own identity. When uncertain, flag in
   memory rather than silently aliasing.
5. Suggest tag refinements where atoms share concepts but use
   inconsistent tags.

### Part 2: Harvest from Projects

5. Read active project notes in `_projects/*/notes/` and drafts in
   `_projects/*/drafts/`.
6. Identify ideas that have value beyond the project — concepts that
   could serve other projects, frames, or future work.
7. Tend matches semantically: it reads prose and recognizes concepts
   worth atomizing regardless of whether the user flagged them with a
   wikilink or just wrote them in a sentence. A wikilink and an
   unlinked reference to the same concept are the same signal.
8. For each harvested concept, create a new atom in `_atoms/` with:
   - `status: seed`
   - `source:` pointing to the project note or draft
   - Wikilinks to related atoms
   - A note in the body that this was harvested from a project.

### Part 3: Propose Frames

9. Look for atom clusters: groups of 4+ atoms with dense cross-linking
   and a coherent shared concern not already captured by an existing frame.
10. For each cluster that meets this threshold:
    a. Create a frame file in `_frames/` with `status: proposed`.
    b. Set `proposed_by: tend` and list the `seed_atoms:`.
    c. Write a frame body describing the perspective, concerns, and
       vocabulary the cluster suggests.
    d. Note the proposal in the memory entry with full rationale.

### Part 4: Log

11. Write a memory entry to `_memory/` with:
    - Links added (which atoms, why)
    - Status promotions (which atoms, why)
    - Atoms harvested from project notes/drafts
    - Frames proposed (with rationale and seed atoms)
    - Observations: patterns, tensions, gaps in the atomic layer

## Judgment Calls

- **Connection threshold:** Don't link atoms just because they share a
  tag. Link them when they genuinely illuminate each other — when knowing
  about one changes how you read the other.
- **Frame proposal threshold:** A cluster needs both density (many links)
  and coherence (a nameable shared concern). Four loosely related atoms
  are not a frame. Four atoms that together describe a distinct way of
  seeing are.
- **Harvesting restraint:** Not every idea in a draft deserves an atom.
  Harvest only concepts that have identity and connection potential
  beyond the project they appeared in.
