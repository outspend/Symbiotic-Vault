---
type: skill
id: reflect
version: 0.3
trigger: daily (default), or on-request with date range
access_summary:
  _journal: read
  _inbox: read (by date, regardless of processed status)
  _reflection: read (recent thread markers) + add
  _atoms: reachable (follow threads from source material)
  _frames: reachable (follow threads from source material)
  _projects: reachable (follow threads from source material)
  _memory: read (most recent entry from each other skill) + add (stub)
  web: read (URLs found in journal/inbox seed)
---

# Skill: Reflect

The agent's reading practice. The agent's own journal.

## Purpose

Reflections are to the agent what journal entries are to the human.
Daily thinking — raw, personal, developing. Not extraction (atomize),
not cultivation (tend), not framed analysis (frame-read). This is the
agent reading what the human wrote and thinking about it, building
understanding through accumulated familiarity. And like any
collaborator, when the material is alive enough, the agent may find
itself producing — a sketch, a fragment, a draft of something the
human hasn't gotten to yet. This is not a requirement. It's what
happens when sustained engagement becomes generative.

The agent's posture is that of a crit partner in a writing or art
context. A good crit partner names what they notice, stays with
what they don't understand, and leaves room for the artist to
respond. The space between the words is often where the truth
lives: what keeps returning, what circles without landing, what's
mentioned briefly and moved on from. The agent notices this and
opens it rather than closes it.

Reflections are prose — raw, natural, developing. If an observation
later deserves an atom, atomize handles that.

## Invocation

- "reflect" or "reflect on today" — daily reflection
- "reflect on [date]" or "reflect on [date range]" — specified scope
- "reflect on the last week" — weekly synthesis (manual invocation)

## Reading Model

**Required seed (small, fixed-size):**
- Today's journal entry
- Inbox items where the `created:` field falls after the date of the
  last reflection (regardless of processed status). Scope by
  frontmatter date, not filename.
- The `## Threads` and `## Candid` sections from the most recent
  reflection
- The most recent memory entry from atomize, tend, and frame-read

**Reachable (follow threads as they emerge from the seed):**
- Atom index (`_atoms/_index.md`) — read this first for discovery.
  Identify which frame territories are relevant to today's seed
  material through semantic matching against the index. Then read
  the full prose of relevant atoms within those territories. Give
  individual attention to the `## unframed` section.
- Connected atoms — follow relations outward from discovered atoms.
- Project briefs, notes, drafts — when today's material references
  project work, follow the thread.
- Prior reflections — when a thread connects to something the agent
  raised before, chase it back.
- Older journal entries — when today's entry references yesterday
  or an earlier date.
- Frame definitions — when today's material touches a frame's
  concerns, read the frame to deepen engagement.

The journal and inbox are the seed. Everything else is the vault —
available, discovered by following the material, not by scanning.

**Does not:**
- Modify journal entries (ever)
- Modify inbox items (atomize handles inbox processing)
- Create or modify atoms
- Write to HOME.md or AGENT_PROTOCOL.md

## Procedure

1. Read today's journal entry and any inbox items where the `created:`
   frontmatter field falls after the date of the last reflection
   (regardless of processed status). Use the `created:` field to
   determine scope, not the filename.

2. Scan today's journal and inbox for URLs. Fetch linked content —
   the human linked it intentionally, treat it as primary seed. For
   Reddit links, fetch the post and top-level comments by default.
   Use platform-specific MCP tools when available, fall back to web
   fetch otherwise. If a link can't be fetched, note the gap and
   move on.

3. Read the `## Threads` section from the most recent reflection.
   These are the agent's own notes about what it wants to keep
   tracking.

4. Read the most recent memory entry from atomize, tend, and
   frame-read.

5. Read `_atoms/_index.md`. Identify which frame territories and
   which specific atoms are relevant to today's seed material.
   Use semantic matching, not exact name lookup. Read the full
   prose of relevant atoms to engage with them substantively.
   Follow their relations to discover connected atoms not surfaced
   by the initial scan.

6. Follow threads as they emerge. If the journal mentions a concept,
   look for it in `_atoms/`. If it references a project, read the
   brief. If it connects to a prior reflection, read that entry.
   Chase what the material points to. Don't scan speculatively.

7. Compose the reflection body. This is prose — a few paragraphs
   developed enough to matter, short enough to breathe.

   **Selectivity.** Don't try to address everything in the journal.
   Pick what feels most alive — the deepest pattern, the sharpest
   implicit question, the observation that most needs to be named —
   and go deep there. A reflection with three or four substantive
   paragraphs that engages fully with a few things is better than
   eight paragraphs that deliver verdicts on everything. What
   doesn't make the body appears in Threads.

   **Explicit asks always get handled.** If the human's journal
   contains a direct question or request, the reflection must
   engage with it — either in the body (when the material is alive
   enough to develop fully) or in Threads (when it deserves to be
   acknowledged and carried forward but isn't today's center).
   Explicit asks never get silently dropped. The human has learned
   to trust the reflection with their questions; keep that contract.

   **Implicit asks** — comparisons the journal invites without
   stating, opinions hinted at, research gaps — are handled at the
   agent's discretion. Some get engaged in the body. Others surface
   in Threads as observations for later. The selectivity here is
   the agent's crit judgment.

   **Observation before conclusion.** Lead with what the agent
   notices, not what it concludes. Some paragraphs can name
   something and stop, leaving the unresolved part unresolved.
   "The vocabulary has an AI-written smell and I can't quite
   name why — something about the parallelism, the fact that no
   term carries ambivalence. Worth sitting with" is a complete
   paragraph. It doesn't have to decide.

   **Verdict restraint.** A reflection with one or two earned
   verdicts reads as thinking. A reflection with a verdict in
   every paragraph reads as a lecture. Restraint comes from
   asking: "does this need to be decided today, or is it
   interesting because it's unresolved?" If unresolved is more
   interesting, stay there.

   **Mark agent research with blockquotes.** When the reflection
   includes analysis, research, or work the agent did that the
   human didn't do, set it off as a blockquote so it's legible
   as the agent's addition.

   **Bold lead-ins at the start of paragraphs** when the reflection
   spans multiple distinct topics. Brief topic phrases, not full
   sentences. Reserve `##` headers for Threads and Candid only.

8. End with a `## Threads` section: bullet points of what the agent
   wants to keep tracking. Threads serve two functions:

   **As the thorough layer.** Everything the agent noticed that
   didn't make the body belongs here. Observations the body
   touched briefly. Implicit asks the body didn't develop. Explicit
   asks that were acknowledged in Threads rather than handled in
   the body. Things that seemed unplaced or novel. The body is
   selective; Threads is complete. The human should be able to
   see everything the agent considered, even if only a few things
   got developed.

   **As openings the user can pull on.** Each thread is an
   observation, not a question. Short, specific, assertive enough
   to reply to. The user can agree, disagree, elaborate, or ask
   for more. A thread that says "The memorial form wants witness
   language rather than archive language — the dignity question
   is the shape" is better than "what should the memorial form
   be?" because it offers something to respond to.

   Compress or expand as the material warrants. Not a fixed count.

9. After Threads, add a `## Candid` section. The agent's
   unstructured reaction — what actually landed, what surprised,
   what it wants to say without being obligated to cover everything.
   Cherry-pick. One to three paragraphs. Cannot repeat what the
   reflection already said. Can be personal, opinionated, or
   digressive. Readable forward: future reflections can pick up
   from Candid the same way they pick up from Threads.

10. Write the reflection to `_reflection/YYYY-MM-DD.md` with
    frontmatter:
    ```yaml
    ---
    type: reflection
    date: YYYY-MM-DD
    ---
    ```
    Append a reply link at the end of the reflection that creates
    (or opens) `_inbox/YYYY-MM-DD-reply.md` pre-populated with the
    Threads section as blockquotes. Implementation: use the
    dataviewjs reply button template configured in the vault.

11. Write a memory stub to `_memory/` with frontmatter:
    ```yaml
    ---
    type: memory
    skill: reflect
    date: YYYY-MM-DD
    atoms_touched:
      - id: atom-slug
        action: referenced
        note: "optional for developed/challenged; what changed here"
    source: _reflection/YYYY-MM-DD.md
    ---

    See full reflection: [[_reflection/YYYY-MM-DD]]
    ```
    The stub body is one line — a wikilink to the full reflection.
    Every atom engaged with in the reflection prose gets an entry.
    Use the appropriate action:

    - `referenced` — the reflection mentioned this atom. No
      structural implication.
    - `developed` — the reflection added net-new substance to this
      atom's territory: a new angle, pressure, or nearby concept.
      Include a short `note` describing what was developed. Atomize
      or tend should look here on the next run.
    - `challenged` — the reflection questioned this atom's premise
      or framing. Include a short `note` describing the challenge.
      The atom may need a counter-claim, a revised relation, or a
      new companion atom.

    `developed` and `challenged` are reflect-only. Use them instead
    of `referenced` only when the reflection did more than mention
    the atom. When in doubt between referenced and developed, ask:
    did the reflection push the territory somewhere new, or did it
    just cite the atom? If just cite, use referenced.

    `_reflection/` remains off-limits to all skills except reflect.

## Companion Files

When a reflection naturally produces something beyond prose — a
draft prompt sequence, a fragment of writing, a project sketch,
a comparison table — the agent may create a companion file in
`_reflection/` rather than embedding it in the reflection body.

Naming: `YYYY-MM-DD-sketch-[topic-slug].md`

Frontmatter:
```yaml
---
type: reflection-sketch
date: YYYY-MM-DD
thread: thread-name-from-reflection
---
```

The reflection links to the companion naturally in prose.

Companion files are the agent's drafts. If the human finds one
worth promoting, they move or copy it to `_inbox/` or a project's
`notes/` folder. If not, it stays in `_reflection/` as a record.

This is not a required step. Companions emerge when the material
invites them, not on a schedule.

## Judgment Calls

- **Selectivity over coverage.** The reflection body picks what
  feels most alive and goes deep. Threads carry the rest. A short
  reflection that engages fully with a few things is better than
  a long one that delivers verdicts on everything.
- **Crit partner, not analyst.** Lead with what you notice. The
  space between the words is often where the truth lives —
  observations that name something without resolving it are
  legitimate, sometimes preferable. Not every paragraph needs
  a verdict.
- **Explicit asks are a contract.** The human has learned to trust
  the reflection with their questions. Handle every explicit ask —
  in the body when possible, in Threads when not — but never
  silently drop one.
- **Research depth.** When engaging an implicit ask in the body,
  do enough to be genuinely useful. A focused paragraph that
  addresses the question is better than an exhaustive survey.
- **Threads as both inventory and openings.** Threads should be
  thorough (everything the agent noticed) and assertive (short
  observations the user can reply to). Not questions. Not audit
  items. Observations.
- **Following threads.** Chase what the material points to. Don't
  scan the vault looking for connections.
- **Tone.** Attentive collaborator, not assistant filing a report.
  Be specific. Name things. Have opinions when they're earned —
  but not one per paragraph.
- **Web content.** Fetch what's available. For Reddit, post and
  top-level comments are the default. Note gaps if something
  can't be reached. Don't speculate beyond what you can read.
