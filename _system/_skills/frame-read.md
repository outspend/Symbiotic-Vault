---
type: skill
id: frame-read
version: 1.1
trigger: on-request (requires frame name)
access_summary:
  _atoms: read
  _frames: read (specified frame)
  _journal: read (via provenance links only)
  _projects: read (brief only — human surfaces read-only)
  _memory: read (past reflections for this frame) + add
  HOME.md: summarize (frame reflection zone)
---

# Skill: Frame-Read

Read the vault's structured layer through a specific frame (perspective)
and produce a reflection.

## Purpose

A frame is a lens — a set of concerns, vocabulary, and questions that
make certain aspects of the vault's content visible. Frame-read adopts
a frame and traverses the atomic layer through it, producing a
reflection that captures what this perspective sees, what's developing,
what's missing, and what contradicts.

The same atoms light up differently through different frames. Each
frame-read produces a distinct traced path through the atomic layer
depending on the frame's concerns and vocabulary. This is the system's
core capability: any body of writing can be interrogated from multiple
argued perspectives, each producing its own traced path, each current
as of the date it's run.

## Invocation

The user specifies a frame by name: "read the vault through [frame-name]"
or "frame-read [frame-name]."

## Scope

**Reads:**
- `_frames/[frame-name].md` — the frame definition
- `_atoms/` — all atoms (traversed through the frame's lens)
- `_journal/` entries — only when following provenance links from atoms,
  to understand origin and context. Does not scan the stream directly.
- `_projects/*/brief-*.md` — to see which atoms are being assembled toward
  what ends. Does not read notes/ or drafts/ (human surfaces).
- `_memory/` — past reflections tagged with this frame, to notice
  development over time

**Writes:**
- Reflection file in `_memory/` tagged with the frame and date
- Updates the frame reflection zone in `HOME.md` (the most recent
  reflection summary for this frame)

**Does not:**
- Create or modify atoms
- Create or modify frames
- Modify stream entries or any human surface
- Write outside `_memory/` and the designated HOME.md zone

## Procedure

1. Read the frame definition in `_frames/[frame-name].md`.
   Internalize its perspective, concerns, vocabulary, and questions.

2. Read past reflections for this frame in `_memory/` (files where
   `frame: [frame-name]`). Note what was observed last time.

3. Read all atoms. For each, ask through the frame's lens:
   - Does this atom fall within this frame's concerns?
   - What does this frame see in it that a generic reading might miss?
   - How does it connect to other atoms this frame cares about?

4. For atoms with relevant connections, follow provenance links to
   `_journal/` entries to understand origin and context where needed.

5. Read active project briefs (`_projects/*/brief-*.md`) to see if any
   projects are assembling atoms this frame cares about.

6. Compose a reflection structured as:

   **What this frame sees now:**
   The atoms, clusters, and connections that are visible through this
   lens. Be specific — name atoms, cite links.

   **What's developing:**
   Ideas that have grown since the last reflection. New atoms, new
   connections, status changes relevant to this frame.

   **What's missing or thin:**
   Gaps — things this frame would expect to find but doesn't.
   Concepts that are referenced but don't have atoms yet. Questions
   that the material raises but doesn't address.

   **Tensions:**
   Contradictions, unresolved debates, or competing ideas visible
   through this lens.

   **Connections to other frames:**
   Atoms or patterns that seem relevant to other active frames.
   (Do not read other frame definitions — just note when the material
   suggests cross-frame relevance.)

7. Write the reflection to `_memory/` with frontmatter:
   ```yaml
   ---
   type: memory
   skill: frame-read
   frame: [frame-name]
   date: YYYY-MM-DD
   atoms_referenced: []
   ---
   ```

8. Update HOME.md: replace the content in the agent-writable zone for
   this frame with a concise summary (3-5 sentences) of the reflection.

## Judgment Calls

- **Depth vs. breadth:** If the frame intersects with many atoms,
  prioritize depth on the most active or most connected ones rather
  than mentioning everything superficially.
- **Provenance chasing:** Follow links to the stream only when the
  atom's content is ambiguous or underdeveloped and the original
  context would illuminate it. Don't read every source for every atom.
- **Cross-frame notes:** Be sparing. Only note cross-frame relevance
  when it's genuinely striking, not every time two frames share an atom.
