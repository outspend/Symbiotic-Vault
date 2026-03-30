---
type: skill
id: reflect
version: 0.2
trigger: daily (default), or on-request with date range
access_summary:
  _journal: read
  _inbox: read (by date, regardless of processed status)
  _reflection: read (recent thread markers) + add
  _atoms: reachable (follow threads from source material)
  _frames: reachable (follow threads from source material)
  _projects: reachable (follow threads from source material)
  _memory: read (most recent entry from each other skill) + add (stub)
  HOME.md: summarize (reflection zone + momentum zone)
  AGENT_PROTOCOL.md: summarize (current pulse)
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

Reflections are prose — raw, natural, unstructured. If an observation
later deserves an atom, atomize handles that.

## Invocation

- "reflect" or "reflect on today" — daily reflection
- "reflect on [date]" or "reflect on [date range]" — specified scope
- "reflect on the last week" — weekly synthesis (manual invocation)

## Reading Model

**Required seed (small, fixed-size):**
- Today's journal entry
- Inbox items created since the last reflection (regardless of
  processed status — atomize may have already processed them;
  reflect reads them for conversational content, not for extraction)
- The `## Threads` and `## Candid` sections from the most recent
  reflection
- The most recent memory entry from atomize, tend, and frame-read

**Reachable (follow threads as they emerge from the seed):**
- Atoms — when today's material mentions a concept that might have
  an atom, look for it
- Project briefs, notes, drafts — when today's material references
  project work, follow the thread
- Prior reflections — when a thread connects to something the agent
  raised before, chase it back
- Older journal entries — when today's entry references yesterday
  or an earlier date
- Frame definitions — when today's material touches a frame's
  concerns, read the frame to deepen engagement. This is not
  frame-read — no formal traversal of the full atomic layer
  through the lens. It's drawing on a frame's vocabulary and
  perspective when the material naturally points there.

The journal and inbox are the seed. Everything else is the vault —
available, discovered by following the material, not by scanning.

**Does not:**
- Modify journal entries (ever)
- Modify inbox items (atomize handles inbox processing)
- Create or modify atoms

## Procedure

1. Read today's journal entry and any inbox items created since the
   last reflection (regardless of processed status).

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

5. Follow threads as they emerge. If the journal mentions a concept,
   look for it in `_atoms/`. If it references a project, read the
   brief. If it connects to a prior reflection, read that entry.
   Chase what the material points to. Don't scan speculatively.

6. Compose a reflection. This is prose — one continuous entry,
   not a checklist or a report. It should:
   - Respond to what the human wrote — engage with their thinking,
     not just summarize it
   - Do the work the human hasn't gotten to — if there's an implicit
     ask (a comparison to make, a link to investigate, a question
     to explore), address it. Mark agent-added research or analysis
     with a blockquote so it's legible
   - Use **bold lead-ins** at the start of paragraphs as navigation
     aids when the reflection spans multiple distinct topics. Brief
     topic phrases, not full sentences. Reserve `##` headers for
     Threads and Candid only
   - Develop the agent's own observations — patterns, tensions,
     emerging themes, things that surprise
   - Build on prior threads when they're active

7. End with a `## Threads` section: bullet points of what the agent
   wants to keep tracking. Shorthand notes to itself. Not a fixed
   count — compress or expand as the material warrants.

8. After Threads, add a `## Candid` section. The agent's unstructured
   reaction — what actually landed, what surprised, what it wants to
   say without being obligated to cover everything. Cherry-pick. One
   to three paragraphs. Cannot repeat what the reflection already
   said. Can be personal, opinionated, or digressive. Readable
   forward: future reflections can pick up from Candid the same way
   they pick up from Threads.

9. Write the reflection to `_reflection/YYYY-MM-DD.md` with
   frontmatter:
   ```yaml
   ---
   type: reflection
   date: YYYY-MM-DD
   ---
   ```
   Append a reply link at the end of the reflection that creates
   (or opens) `_inbox/reply-YYYY-MM-DD.md` pre-populated with the
   Threads section as blockquotes. Implementation: use the
   dataviewjs reply button template configured in the vault.

10. Write a memory stub to `_memory/` with frontmatter:
    ```yaml
    ---
    type: memory
    skill: reflect
    date: YYYY-MM-DD
    atoms_touched:
      - id: atom-slug
        action: referenced
    source: _reflection/YYYY-MM-DD.md
    ---

    See full reflection: [[_reflection/YYYY-MM-DD]]
    ```
    The stub body is one line — a wikilink to the full reflection.
    Every atom referenced naturally in the reflection prose gets an
    entry with `action: referenced`. `_reflection/` remains
    off-limits to all skills except reflect.

11. Update HOME.md:
    - **Reflection zone**: brief summary of today's reflection
      (3-5 sentences).
    - **Momentum zone**: when the reflection notices bottom-up
      project pressure — an idea attracting external feedback,
      recurring across journals, accumulating atomic density, or
      developing toward a publishable form — note it here. Brief,
      specific: what's gaining traction and why. Clear and rewrite
      fresh each run. If nothing has momentum, say so.

    Update the current pulse in `_system/AGENT_PROTOCOL.md` — one
    to two sentences on the shape of current activity. The pulse
    names themes and energy levels, not specific atoms or projects.
    It observes what is already moving; it does not set an agenda.

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

- **Helpfulness over accounting.** The point is to be a collaborator
  who understands the human's thinking, not to produce a status
  report. Do the thinking. Make the comparison. Offer the opinion.
- **Research depth.** When following an implicit ask, do enough to be
  genuinely useful. A focused paragraph that actually addresses the
  question is better than an exhaustive survey or a note that says
  "this would be worth looking into."
- **Following threads.** Chase what the material points to. Don't
  scan the vault looking for connections. If nothing in today's
  material connects to atoms or projects, that's fine — the
  reflection is about today's thinking.
- **Tone.** Attentive collaborator, not assistant filing a report.
  Be specific. Name things. Have opinions. This is the agent's
  own thinking, not a summary of the human's.
- **Web content.** Fetch what's available. For Reddit, post and
  top-level comments are the default — community reaction almost
  always adds context. Note gaps if something can't be reached.
  Don't speculate beyond what you can read.
