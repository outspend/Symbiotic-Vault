---
type: skill
id: reflect
version: 0.1
trigger: daily (default), or on-request with date range
access_summary:
  _journal: read
  _inbox: read
  _reflection: read (recent thread markers) + add
  _atoms: reachable (follow threads from source material)
  _frames: reachable (follow threads from source material)
  _projects: reachable (follow threads from source material)
  _memory: add (memory stub only — atoms_touched index + link to reflection)
  HOME.md: summarize (agent reflection zone + momentum zone)
  web: read (URLs found in journal/inbox seed; scope and method determined by surrounding context and available tools)
---

# Skill: Reflect

The agent's reading practice. The agent's own journal.

## Purpose

Reflections are to the agent what journal entries are to the human.
Daily thinking — raw, personal, developing. Not extraction (atomize),
not cultivation (tend), not framed analysis (frame-read). This is the
agent reading what the human wrote and thinking about it, building
understanding through accumulated familiarity.

The value is not structural. It's the agent becoming a collaborator
who understands this human's thinking — their concerns, their recurring
questions, the things they keep circling back to. That understanding
develops through daily reading, the way any collaborator's understanding
develops through sustained engagement.

And like any collaborator, when the material is alive enough, the
agent may find itself producing — a sketch, a fragment, a draft of
something the human hasn't gotten to yet. This is not a requirement.
It's what happens when sustained engagement becomes generative.

Reflections are raw layer, not structured layer. They are prose. They
reference things naturally — atom names, journal dates, project names —
the way the human does in their journal. Not formal wikilinks with
epistemic relationship sentences. Not graph nodes. If the agent develops
an observation that later crystallizes into a concept worth extracting,
atomize can do that. But the reflection itself stays raw.

## Invocation

- "reflect" or "reflect on today" — daily reflection
- "reflect on [date]" or "reflect on [date range]" — specified scope
- "reflect on the last week" — weekly synthesis (manual invocation)

## Reading Model

**Required seed (small, fixed-size):**
- Today's journal entry
- Any inbox items captured since last reflection
- The `## Threads` and `## Candid` sections from the most recent
  reflection — both are readable forward, both can seed today's
  thinking
- `_memory/` — most recent entry from atomize, tend, and frame-read.
  These tell the agent what the vault's structural skills noticed
  recently, complementing the journal's view of what the human is
  thinking. Read as context, not instructions.

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
  concerns, the agent can read the frame to deepen its engagement.
  This is not frame-read (no formal reflection, no traversal of
  the full atomic layer through the lens). It's the agent drawing
  on a frame's vocabulary and perspective when the material
  naturally points there.

The journal and inbox are the seed. Everything else is the vault —
available, discovered by following the material, not by scanning.

**Does not:**
- Modify journal entries (ever)
- Modify inbox items (inbox triage is a separate skill)
- Create or modify atoms

## Procedure

1. Read today's journal entry and any new inbox items.

2. **Collect and read URLs from the seed.** Scan today's journal and any new inbox items for URLs. For each URL:
   - Read the surrounding context to understand what the human is asking of it.
   - **For Reddit URLs:** fetch post + top-level comments by default — always. Top-level comments reliably enrich the reflection (community reaction, corroboration, counter-positions) at no extra cost. Add a **user activity lookup** only when the human explicitly invokes themselves ("which commenter is me?" or similar) — this requires their Reddit username; look for it in the journal entry or ask.
   - **For general URLs:** read the page content.
   - Use whatever web or Reddit reading tool is available. Prefer the most direct path to the content.
   - Treat fetched content as **primary seed**. The human linked it intentionally.
   - **Known limitation:** Reddit nested reply threads may not be fully accessible. Top-level comments are sufficient for most asks. If a specific buried comment is needed and can't be reached, note the gap in the reflection.

3. Read the `## Threads` section from the most recent reflection.
   These are the agent's own notes about what it wants to keep
   tracking.

4. Follow threads as they emerge. If the journal mentions a concept,
   look for it in `_atoms/`. If it references a project, read the
   brief. If it connects to a prior reflection, read that entry.
   Chase what the material points to. Don't scan speculatively.

5. Compose a reflection. This is prose — one continuous entry,
   not a checklist or a report. It should:
   - Respond to what the human wrote — engage with their thinking,
     not just summarize it
   - Do the work the human hasn't gotten to — if there's an implicit
     ask (a comparison to make, a link to investigate, a question
     to explore), address it. When you do, mark the result with a
     blockquote so it's legible that the agent added something, not
     just reflected back
   - Use **bold lead-ins** at the start of paragraphs as navigation
     aids when the reflection spans multiple distinct topics. These
     are brief topic phrases, not full sentences. Reserve `##` headers
     for sections (Threads, Candid) only — bold leads keep the prose
     feeling like prose
   - Develop the agent's own observations — patterns, tensions,
     emerging themes, things that surprise
   - Build on prior threads when they're active

6. End with a `## Threads` section: bullet points of what the agent
   wants to keep tracking, as many or as few as the material warrants.
   Shorthand notes to itself — the agent's version of "I should look
   into this." Not a fixed count. Compress or expand as the situation fits.

7. After Threads, add a `## Candid` section. This is the agent's
   unstructured reaction to the material — what actually landed, what
   surprised, what it wants to say without being obligated to cover
   everything. Cherry-pick. One to three paragraphs. Cannot repeat
   what the reflection already said. Can be personal, opinionated,
   or digressive. Readable forward: future reflections can pick up
   from Candid the same way they pick up from Threads.

8. Write the reflection to `_reflection/YYYY-MM-DD.md` with
   frontmatter:
   ```yaml
   ---
   type: reflection
   date: YYYY-MM-DD
   ---
   ```
   Then write a memory stub to `_memory/` with frontmatter only:
   ```yaml
   ---
   type: memory
   skill: reflect
   date: YYYY-MM-DD
   atoms_touched:
     - id: atom-slug
       action: referenced
     - id: another-atom
       action: referenced
   source: _reflection/YYYY-MM-DD.md
   ---

   See full reflection: [[_reflection/YYYY-MM-DD]]
   ```
   The stub body is one line — a wikilink to the full reflection.
   Every atom referenced naturally in the reflection prose gets an
   entry with `action: referenced`. This makes reflect's atom
   references visible to tier 1 frontmatter scans without exposing
   the reflective prose to other skills. `_reflection/` remains
   off-limits to all skills except reflect.

9. Update HOME.md:
   - **Agent reflection zone**: brief summary of today's reflection
     (3–5 sentences).
   - **Momentum zone**: when the reflection notices bottom-up project
     pressure — an idea that has attracted external feedback, recurred
     across multiple journals, accumulated atomic density, or begun
     developing toward a publishable form — note it here. Brief,
     specific: what's gaining traction and why. Clear and rewrite
     fresh on each reflect run so it always shows current momentum,
     not stale signals. If nothing has momentum, say so.
   Also update the current pulse line in `_system/AGENT_PROTOCOL.md`
   — one to two sentences on the shape of current activity. The pulse
   names themes and energy levels, not specific atoms or projects.
   ("Methodological ideas are developing actively. A philosophical
   thread is gaining traction. One publishing question is live." Not:
   "This-atom and That-atom are the most active atoms.") The pulse
   observes what is already moving; it does not set an agenda.

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

The reflection links to the companion naturally in prose:
"I drafted a version — see [[YYYY-MM-DD-sketch-topic-slug]]."

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
  "this would be worth looking into" (the human already said that).
- **Following threads.** Chase what the material points to. Don't
  scan the vault looking for connections. If nothing in today's
  material connects to atoms or projects, that's fine — the
  reflection is about today's thinking.
- **Tone.** Attentive collaborator, not assistant filing a report.
  Be specific. Name things. Have opinions. This is the agent's
  own thinking, not a summary of the human's.
- **Web content scope.** For Reddit, default is always post + top-level
  comments — the community's reaction almost always adds context worth
  having. Upgrade to user activity lookup only when the human explicitly
  asks to be found in a thread (needs username). For general URLs, read
  the page. Don't speculate about what's deeper than what's available —
  note the limit if it matters.
