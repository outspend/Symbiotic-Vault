---
type: skill
id: tend
version: 1.1
trigger: on-request
access_summary:
  _atoms: read + modify (links, tags, aliases, status)
  _frames: read + add (proposed frames)
  _projects: read (notes, drafts — human surfaces, read-only)
  _memory: read + add
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
- Harvest new concepts from growing project notes and drafts into atoms
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
- `_memory/` — most recent entry from atomize, frame-read, and reflect.
  For context on what other skills noticed, flagged, or were uncertain about.

**Writes:**
- Updates to existing atoms: new wikilinks, updated tags, new aliases,
  status promotion (`seed` → `developing`, `developing` → `stable`)
- New atom files in `_atoms/` with `status: seed` (harvested from notes/drafts)
- Proposed frame files in `_frames/` with `status: proposed`
- Memory entry in `_memory/` logging all changes and observations
- `_atoms/_index.md` — regenerated from scratch on every tend run

**Does not:**
- Modify stream entries, inbox items, or any human surface
- Modify project briefs, notes, or drafts
- Modify or delete the prose body of existing atoms (only frontmatter,
  wikilinks, aliases, and the `## Relations` section)
- Activate proposed frames (that's the human's decision)

## Procedure

> Before beginning Part 0, read the most recent memory entry from atomize,
> frame-read, and reflect. These cross-skill logs carry flags, candidate aliases,
> and unresolved questions from other vantage points — they inform every step below.
> Treat `referenced` as the minimal touch. Pay special attention to
> reflect entries marked `developed` or `challenged`:
> - `developed` means reflect grew something in this atom's territory.
>   Look for new relations, aliases, tags, frame assignments, or status
>   implications in that neighborhood.
> - `challenged` means reflect applied substantive pressure to the
>   atom's premise or framing. Consider whether the relations section
>   should acknowledge the challenge, or whether a counter-claim atom
>   created elsewhere should be linked in.

### Part 0: Assess Atomic Health

1. Before enriching, read all atoms and flag:
   - Atoms whose prose body contains multiple distinct ideas
     (candidates for splitting)
   - Atoms too thin to sustain connections (candidates for merging
     into a relation on another atom)
   - Atoms with vague relation preambles — "relates to," "resonates
     with," "connects to" — that should be tightened to a directional
     epistemic relationship
   - Atoms whose kind may be miscategorized
   - Atoms whose `frames:` field references a frame ID that no longer
     exists as either an active or proposed frame file in `_frames/`
     (orphaned frame references from rejected proposals). Remove these
     references directly — no user flag needed, this is cleanup.

   Collect all other flags for the Part 4 log with specific recommendations.
   Do not fix autonomously — present flags to the user as part of
   the tend report.

### Part 1: Enrich Atoms

2. Read all atoms. Build an internal index of their IDs, key concepts, existing
   links, aliases, tags, and `frames:` assignments — this informs connection
   discovery and frame auditing in the steps below.
3. **Audit frame assignments.** For each atom, cross-reference its `frames:`
   field against the frames carried by its linked atoms. If an atom links to
   2+ atoms that share a frame the current atom doesn't carry, it is a
   candidate for that frame — verify that the atom's content aligns with the
   frame's concerns before applying. Add the frame directly if the alignment is
   clear. A structural match without conceptual fit is a false positive — flag
   rather than apply. Flag in the Part 4 log if uncertain.

   This catches a common miss: atoms assigned frames at creation time (atomize)
   based on their surface method, before relations were fully established. Tend
   is the first pass with the full relational picture. Use it.
4. Identify atoms that share concepts but don't link to each other.
   For each proposed new connection:
   a. Append to the `## Relations` section of both atoms:
      `- [[the-other-atom]]: one sentence describing the relationship
      (supports, challenges, extends, instantiates, etc.)`.
      If an atom predates the Relations section, add the section first.
   b. Track the connection and rationale for the memory entry (Part 4).
4. Review atom status:
   - `seed` → `developing`: atom has 3+ inbound/outbound links,
     or has been referenced by a frame-read reflection.
   - `developing` → `stable`: atom has been linked by multiple other
     atoms, referenced in a collaboration trace, and has substantive content.
   - Use judgment. These thresholds are guidelines, not hard rules.
5. **Detect and record aliases.** Scan atoms and active project notes for
   cases where the same concept is referenced under a different name — a
   synonym, abbreviation, variant spelling, informal title, or alternate
   framing. Also check atomize's most recent memory entry for candidate
   alias flags: atomize reads journal entries and may flag names it noticed
   there that don't yet appear in an atom's `aliases:` field. The alias
   detection path from journal material runs through that cross-skill channel
   (atomize notices → flags in memory → tend applies), not direct journal access.
   For each atom where a distinct alternate name is observed:
   a. Add the alternate name(s) to the atom's `aliases:` field.
   b. Track each addition for the memory entry (Part 4): which atom, what name
      was added, and which source surfaced it.
   Judgment: an alias is a name that points to the *same* concept, not
   a related concept with its own identity. When uncertain, flag in
   memory rather than silently aliasing.
6. Apply tag refinements where atoms share concepts but use inconsistent tags:
   update the `tags:` field directly on the atoms involved. When uncertain
   whether two tags should be unified, flag in the Part 4 log rather than
   silently merging.

### Part 2: Harvest from Projects

7. Read active project notes in `_projects/*/notes/` and drafts in
   `_projects/*/drafts/`.
8. Identify ideas that have value beyond the project — concepts that
   could serve other projects, frames, or future work.
9. Tend matches semantically: it reads prose and recognizes concepts
   worth atomizing regardless of whether the user flagged them with a
   wikilink or just wrote them in a sentence. A wikilink and an
   unlinked reference to the same concept are the same signal.
10. For each harvested concept, create a new atom in `_atoms/` with:
    - `status: seed`
    - `source:` pointing to the project note or draft
    - Wikilinks to related atoms
    - A note in the body that this was harvested from a project.

### Part 3: Propose Frames

11. Look for atom clusters: groups of 4+ atoms with dense cross-linking
    and a coherent shared concern not already captured by an existing frame.
12. For each cluster that meets this threshold:
    a. Create a frame file in `_frames/` with `status: proposed`.
    b. Set `proposed_by: tend` and list the `seed_atoms:`.
    c. Write a frame body describing the perspective, concerns, and
       vocabulary the cluster suggests.
    d. Update the `frames:` field on all seed atoms to include the
       proposed frame ID. Do not wait for activation — proposed frame
       references in atom frontmatter are low-risk (ignored by skills
       until active) and immediately useful when the frame is approved.
    e. Note the proposal in the memory entry with full rationale.

### Part 4: Log

13. Write a memory entry to `_memory/` with frontmatter including
    `atoms_touched`: log every atom enriched (`action: enriched`),
    promoted (`action: reinforced`), or harvested (`action: created`).
    For any atom with lingering doubt, add `uncertainty: "..."`.
    Then in prose:
    - Links added (which atoms, why)
    - Status promotions (which atoms, why)
    - Atoms harvested from project notes/drafts
    - Frames proposed (with rationale and seed atoms)
    - Observations: patterns, tensions, gaps in the atomic layer
    - **Uncertainties:** flags from Part 0, connection doubts, anything
      not resolved from tend's vantage point
    - Any cross-skill flags resolved from other skills' memory entries
      (note which skill raised it, what evidence resolved it)

    `enriched` is tend's specific touch: the atom's structural
    representation improved through relations, tags, aliases, frames,
    or status. It is different from atomize's `reinforced` (recurrence
    without structural change) and reflect's `developed` (new substance
    noticed but not yet folded back into structure).

### Part 5: Regenerate Atom Index

After all enrichment, status promotions, and frame assignments are
complete, regenerate `_atoms/_index.md` from the current state of
all atoms.

Format: atoms grouped by frame, one line per atom.

```markdown
# Atom Index

## writing-practice
highlights-and-hides | method | Exposing what a framing foregrounds vs suppresses
constraint-play-on-topologies | method | Forbid a topology, observe the strain

## epistemic-literacy
framing-as-contract | concept | Every framing commits to a settlement between visibility and invisibility

## unframed
impression-enrichment-via-llm | method | Embroider and enrich impressions through LLM dialogue
claude-hacking-claude | concept | Claude defending against Claude as adversarial event
```

Each entry: `id | kind | one-sentence summary`

Atoms belonging to multiple frames appear under each frame. Atoms with
no frame assignment appear under `## unframed`.

The index is regenerated from scratch on every tend run — it reflects
the current state, not an incremental update. This ensures the index
is always consistent with atom frontmatter.

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
