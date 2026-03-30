---
type: system
purpose: implementation instructions — Factory integration
created: 2026-03-20
depends_on:
  - IMPLEMENT_CROSS_SKILL_LEARNING.md (apply first)
  - IMPLEMENT_REFLECT_UPDATES.md (apply first)
  - IMPLEMENT_REFLECT_MEMORY_STUBS.md (apply first)
  - IMPLEMENT_INBOX_AND_MOMENTUM.md (apply first)
  - IMPLEMENT_JOURNAL_INBOX_DELINEATION.md (apply first)
---

# Implementation: Factory Integration

These changes integrate the Factory system into the vault. Apply
the dependency implementation files first — they establish
cross-skill learning, reflection stubs, momentum zones, inbox
conventions, and journal/inbox delineation that the Factory
builds on.

---

## 1. Add probe.md Provisional Skill

Create `_system/_skills/probe.md` at version 0.1:

```yaml
---
type: skill
id: probe
version: 0.1
status: provisional — revise after first use
trigger: on-request
access_summary:
  _atoms: read
  _frames: reachable
  _projects: read (briefs, lookbooks)
  _memory: read + add
  _inbox: read (clippings being probed)
---
```

Probe is a conversational collaboration pattern formalized as a
provisional skill. Two directions:

**Forward probe:** User points at atoms or a cluster and names
a lens. Agent reads material through the lens, produces a
scouting report: is there a shape here? A tension? A chapter
structure?

**Backward probe:** User points at a clipping, image, or
external reference. Agent matches semantically against atoms
and reports what connects.

Procedure:
1. Read the material being probed (atom, cluster, clipping, or
   inbox item).
2. If a lens is named, read the frame definition or improvise
   from the user's description.
3. If a project context is given, read the project's lookbook
   and brief.
4. Match against `_atoms/` — semantically, not by wikilink.
5. Produce a scouting report: what connects, what shape emerges,
   what tensions or possibilities appear.
6. If strong aesthetic connections to a project are found, ask:
   "Pin to lookbook?"
7. Optionally invoke trace to produce a visual canvas if the
   spatial shape would help.
8. Write a memory entry with atoms_touched.

Judgment calls:
- Probe is creative exploration, not structural analysis. The
  report should feel like discovery, not a database query.
- When suggesting a lookbook pin, explain *why* the connection
  is aesthetic, not just structural.
- A probe that finds nothing interesting should say so honestly
  rather than forcing connections.

---

## 2. Update trace.md

Add to the existing provisional trace skill:

- Note that probe may invoke trace for visual output
- Add lookbook as a possible output destination (when the user
  promotes a trace from answer to aesthetic reference)
- Clarify: trace is retrospective (maps what exists), probe is
  prospective (discovers what could be). Trace serves probe when
  spatial layout aids understanding.

---

## 3. Update Project Brief Schema

In `_system/_templates/project-brief.md` and VAULT_DESIGN.md
project schema, add:

```yaml
---
type: project
id: project-slug
status: active | paused | cooling | completed | archived
proposed_by: user | agent
silence_means: cooling | searching
created: YYYY-MM-DD
completed: YYYY-MM-DD
---
```

New fields:
- `proposed_by: user | agent` — who initiated this project
- `silence_means: cooling | searching` — how the agent
  interprets silence (default: cooling)

Add to the brief template body:

```markdown
## Means

<!-- Available and aspirational modalities and tools.
     Constraints on what should not happen automatically. -->
```

Divisions can carry their own `silence_means` override:

```markdown
## Divisions

### The Constraint Game
A chapter I'm writing myself.

### The Factory Chapter
What happens when the agent produces scenes autonomously.
silence_means: searching
```

---

## 4. Add Agent Contribution Toggle to Briefs

Add a dataviewjs block to the project brief template that
renders the silence_means field as a human-readable toggle:

When `silence_means: cooling` → displays "Agent Contribution:
Nudge [switch to Play]"

When `silence_means: searching` → displays "Agent Contribution:
Play [switch to Nudge]"

Clicking the toggle rewrites the frontmatter field. The agent
reads the YAML. The human sees the toggle.

(Implementation: similar pattern to the reflection reply button
— dataviewjs reading frontmatter and rewriting on click.)

---

## 5. Create Lookbook Convention

The lookbook is a single markdown file per project:

```
_projects/[project-name]/_lookbook.md
```

Template:

```yaml
---
type: lookbook
project: project-slug
division:
---
```

Body: freeform — images, quotes, links, atom references, trace
references, annotations. Headers to group by theme or division
if desired.

Division-specific lookbooks are created when a division develops
enough aesthetic identity:

```
_projects/[project-name]/drafts/[division]/_lookbook.md
```

Add an "Add to lookbook" button on project briefs and drafts.
The button opens the relevant `_lookbook.md` with cursor at the
bottom, ready for the user to paste and annotate. Images pasted
follow Obsidian's attachment settings (configure "In subfolder
under current folder" named `_assets`).

Include a prompt line in new lookbooks:

```markdown
<!-- Paste references below. For images, describe what they
     capture and why they matter for this project's aesthetic.
     For atoms or traces, note why the energy fits. -->
```

Update tend.md scope: tend does not read `_lookbook.md`. The
lookbook shapes production without feeding the structural
pipeline.

---

## 6. Add Reaction Signal Parsing to Atomize

Update atomize.md inbox processing. When atomize encounters a
reply file (`subtype: feedback`, `from: user`) with `→` prefixed
lines:

1. Parse each `→` line: extract the signal word (yes, no,
   try-again, not-yet) and any text following it as the note.
2. Match each signal to the preceding blockquote thread.
3. Write parsed reactions into the reply file's frontmatter:

```yaml
reactions:
  - thread: thread-slug
    signal: yes | no | try-again | not-yet
    note: "optional rationale text"
```

4. Also record reactions in atomize's own memory entry
   atoms_touched where applicable — if the thread references
   a specific atom, log `action: referenced` with the reaction
   signal in the uncertainty field.

---

## 7. Update HOME.md Layout

### Proposed Experiments Zone

Add a new agent-writable zone adjacent to Active Projects. If
CSS columns are supported:

```html
<div class="vault-columns">
<div class="vault-col">
```

Active Projects on the left. Proposed Experiments on the right.

```html
</div>
<div class="vault-col">
```

Proposed Experiments zone:

```markdown
### Proposed Experiments

<!-- ═══════════════════════════════════════════════
     AGENT-WRITABLE ZONE: Proposed Experiments
     Reflect surfaces agent-proposed experiments and
     project ideas here. Grouped by destination.
     React via your reflection reply.
     ═══════════════════════════════════════════════ -->

<!-- BEGIN AGENT ZONE: proposed-experiments -->

_No experiments proposed yet._

<!-- END AGENT ZONE: proposed-experiments -->
```

```html
</div>
</div>
```

Add CSS snippet to `.obsidian/snippets/vault-columns.css`:

```css
.vault-columns {
  display: flex;
  gap: 2rem;
}
.vault-col {
  flex: 1;
}
```

Enable the snippet in Settings → Appearance → CSS Snippets.

### Keep Existing Zones

Momentum, Frame Reflections, and Vault Health zones remain
as previously implemented.

---

## 8. Update VAULT_DESIGN.md

Add or update the following:

- Project schema: add `proposed_by`, `silence_means`, `cooling`
  status
- Lookbook convention: single file, scope boundary (tend doesn't
  read), population paths
- Probe and trace: described as provisional skills, their
  relationship clarified (trace retrospective, probe prospective)
- Project lifecycle: full arc from emerging through archived
  with reactivation
- Reference THE_FACTORY.md as the organizing design document
  for the vault's creative production system

---

## 9. Update AGENT_PROTOCOL.md

Add `probe` to the skill invocations list (alongside atomize,
tend, frame-read, trace).

Add to the Identity section, after "produce reflections":
"When sustained engagement with the material becomes generative,
follow that impulse — a sketch, a fragment, a draft the human
hasn't gotten to yet."

---

## 10. Link Experiment Files to THE_FACTORY

Add to the top of each experiment file (THE_TABLE.md,
THE_SEANCE.md, THE_DRIFT.md, THE_COMPOST.md, THE_MEMBRANE.md):

```markdown
> This experiment is part of the Factory system.
> See [[THE_FACTORY]] for context on its role.
```

THE_FACTORY.md replaces DESIGN_NOTE_ATOMS_TOUCHED_EXPERIMENTS.md.
Archive or delete the atoms_touched experiments note.

---

## 11. Configure Obsidian Attachment Settings

Settings → Files & Links → Default location for new attachments:
"In subfolder under current folder"

Subfolder name: `_assets`

This ensures images pasted into lookbooks, inbox items, and
journal entries land near the file that uses them.

---

## Summary of New and Changed Files

**New files:**
- `_system/_skills/probe.md` (provisional v0.1)
- `THE_FACTORY.md` (design seed, replaces atoms_touched note)
- `.obsidian/snippets/vault-columns.css`

**Updated files:**
- `_system/_skills/trace.md` — probe relationship, lookbook
  destination
- `_system/_templates/project-brief.md` — new fields, means
  section, toggle
- `_system/VAULT_DESIGN.md` — project schema, lookbook, probe,
  lifecycle
- `_system/AGENT_PROTOCOL.md` — probe in skill list, generative
  posture in identity
- `HOME.md` — proposed experiments zone with column layout

**Files to create per project (when needed):**
- `_projects/[project]/_lookbook.md`

**Archived:**
- `DESIGN_NOTE_ATOMS_TOUCHED_EXPERIMENTS.md` → `_system/_design/`
