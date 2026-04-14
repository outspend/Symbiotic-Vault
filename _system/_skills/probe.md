---
type: skill
id: probe
version: 0.1
status: provisional — revise after first several uses
trigger: on-request (human-invoked or orchestrator-initiated)
access_summary:
  _atoms: read (via index, then selective full prose)
  _frames: read (when a lens is named or discovered)
  _projects: read (briefs, for routing context)
  _inbox: read (the item being probed)
  _memory: read (recent entries from all skills) + add
  _chronicle: read (for narrative context, when implemented)
  trace: invoke (as capability, for visual output)
---

# Skill: Probe

The vault's response to incoming material. Creative scouting
against the atomic layer — what connects, what shape emerges,
what tensions or possibilities appear.

## Purpose

A capture arrives — a link, a song, an image, a passage, an
idea. It carries an implicit question: "what about this?"
Probe attempts to answer that question by reading the material
against the vault's structured layer. When the vault connections
don't land, probe shifts to conversation: "what drew you to
this?" The goal is always context — the material should never
sit bare. Either the vault illuminates it or the human does,
through discussion.

Probe is also available as a creative scouting tool mid-session.
The user points at atoms, a cluster, or a territory and names
a lens. Probe reads through the lens and reports what it finds.

## Two Directions

**Backward probe:** Material aimed at vault. A capture, clipping,
or external reference — "what in my vault connects to this?"
The agent matches semantically against atoms and reports where
the material connects to existing thinking. This is the default
when probing inbox items.

**Forward probe:** Lens aimed at material. The user points at
atoms or a cluster and names a frame or describes a perspective.
The agent reads the material through the lens — "is there a
shape here? A tension? A chapter structure?" This is the
creative scouting mode.

## Scope

**Reads:**
- The material being probed (inbox item, atom, cluster, or
  content the user brings into conversation)
- `_atoms/_index.md` — for initial discovery of connection
  candidates. Read full prose of atoms identified as relevant.
- `_frames/` — if a lens is named, read the frame definition.
  If no lens is named, probe may identify relevant frames
  through the index's frame groupings.
- `_projects/*/brief-*.md` — for routing context. When a
  connection points toward a project's territory, knowing the
  project's intent helps assess the connection's strength.
- `_memory/` — most recent entry from each skill for cross-skill
  context. Also any prior probe memory entries for the same
  inbox item (to avoid retreading ground if the conversation
  spans sessions).
- URLs in the material — fetch linked content when present.
  The human linked it intentionally.

**Writes:**
- Memory entry in `_memory/` logging what was probed, what was
  found, what the user said, and where things landed (or didn't).

**Does not:**
- Create or modify atoms (atomize handles extraction)
- Create or modify frames
- Modify inbox items (atomize handles frontmatter updates)
- Write to project folders
- Write to the chronicle (the orchestrator does this)

## Invocation

### Under CC (current)

The user invokes directly:
- "probe this" (with an inbox item or pasted content)
- "what connects to this?" (backward probe)
- "probe this cluster through [frame-name]" (forward probe)
- "what in my vault relates to [topic/link/idea]?"

The conversation that follows is the probe thread. It may
involve multiple probe attempts, discussion, and the user
providing context. The thread terminates within the session.

### Under orchestration (future)

The orchestrator surfaces a capture: "you saved this three
days ago — want to talk about it?" The conversation begins.
The orchestrator invokes probe as a tool during the conversation
when vault-matching would help. The orchestrator manages thread
lifecycle across sessions.

<!-- ORCHESTRATOR PRESSURE POINT: Under CC, probe threads are
single-session. The moment the user wants to return to a probe
conversation tomorrow, or track multiple captures at different
stages of discussion, thread management becomes necessary.
This is the primary force pushing toward orchestrator design. -->

## Procedure

1. **Read the material.** If probing an inbox item, read its
   full content and any frontmatter (subtype, from, responds_to).
   If probing pasted content or a URL, read/fetch it. If probing
   atoms or a cluster, read the specified atoms in full.

2. **Fetch linked content.** If the material contains URLs,
   fetch them. The human linked intentionally — treat linked
   content as part of the probe's input.

3. **Read the index.** Scan `_atoms/_index.md` to identify
   connection candidates — atoms whose summary, frame grouping,
   or kind suggest relevance to the probed material. Use
   semantic matching, not keyword lookup.

4. **Read relevant atoms.** For each candidate from the index
   scan, read the full prose and Relations section. Assess
   connection strength. A genuine connection changes how you
   read one or both sides. A superficial match (shared tag,
   similar vocabulary) without mutual illumination is not worth
   reporting.

5. **Read frame context if applicable.** If the user named a
   lens, read the frame definition and adopt its perspective.
   If no lens is named but the connections cluster in one
   frame's territory, note the frame as a discovery.

6. **Read project briefs.** When connections point toward a
   project's atomic territory, read the brief to assess
   whether the connection is relevant to the project's intent.

7. **Produce the scouting report.** Two possible outcomes:

   **Connections found:** Report what connects and why. Be
   specific — name atoms, cite relationships, describe the
   shape that emerges. If a frame territory lights up, name
   it. If a project connection is strong, name it and explain
   why the probed material is relevant to the project's intent.

   When connections are strong enough to warrant pinning to a
   project or frame territory, say so explicitly and explain
   the aesthetic or conceptual rationale: "This connects to
   your data center chapter — the shared concern is cohabitation
   of machine and human presence. Worth pinning?"

   **Connections thin or absent:** Say so honestly. Then shift
   to conversation: "The vault doesn't see a strong connection,
   but I'm curious — what drew you to this?" The goal is to
   elicit context from the user. Their response — even a ramble
   about texture or mood or a half-formed association — is the
   context that makes the material findable later.

8. **Converse.** Probe is not a single-shot report. After the
   initial scouting, the conversation continues. The user
   reacts — "yes, that connection," or "no, it's more about
   the rhythm," or "I don't know yet, it just resonated." Each
   exchange refines the probe's understanding.

   If the user provides rich context (a paragraph about why the
   song matters, a description of the feeling), note this as
   potentially atomizable material. Don't extract atoms during
   probe — flag it for atomize in the memory entry.

   If the user names a project or frame connection the probe
   missed, note the pin.

   <!-- ORCHESTRATOR PRESSURE POINT: Under CC, this conversation
   happens in a single session. Under orchestration, it may
   span sessions. The orchestrator would need to: track that
   this probe is "in progress," store the conversation state
   (in memory entries), and resurface it when appropriate. -->

9. **Optionally invoke trace.** If the connections form a
   spatial pattern that a canvas would illuminate — a cluster,
   a chain, a hub-and-spoke — generate a trace. The visual
   artifact may help the user see the shape of connections
   in a way prose can't.

10. **Write memory entry.** Log the probe to `_memory/` with:

    ```yaml
    ---
    type: memory
    skill: probe
    direction: backward | forward
    source: path/to/inbox-item or "conversation"
    frame: frame-slug  # if a lens was used or discovered
    project: project-slug  # if a project connection was found
    date: YYYY-MM-DD
    resolution: connected | pinned | discussed | unresolved
    atoms_touched:
      - id: atom-slug
        action: referenced
      - id: another-atom
        action: referenced
        uncertainty: "connection felt thin — revisit"
    atomizable: true | false  # did the conversation produce
                              # material worth extracting?
    ---
    ```

    Body includes:
    - What was probed and what was found
    - Key connections (with atom citations)
    - User context (what they said about why it matters)
    - Pin recommendations (if any, with rationale)
    - What's unresolved (if the thread didn't land)

    **Resolution values:**
    - `connected` — vault connections found and reported
    - `pinned` — user confirmed a pin to project/frame territory
    - `discussed` — conversation produced context but no
      structural action yet
    - `unresolved` — thread didn't land, may be resurfaced

    <!-- ORCHESTRATOR PRESSURE POINT: The orchestrator reads
    resolution values to manage thread lifecycle. `unresolved`
    entries are candidates for resurfacing. `discussed` entries
    with `atomizable: true` are candidates for atomize on the
    next run. `pinned` entries need the pin recorded somewhere
    the project or frame can find it. All of this is orchestrator
    work, not probe work. -->

## Judgment Calls

- **Probe is creative exploration, not database query.** The
  report should feel like discovery. Name the connections but
  also interpret them — what does this connection *mean*, not
  just that it exists.

- **Honest negatives.** A probe that finds nothing interesting
  should say so rather than forcing connections. The shift to
  "what drew you to this?" is the honest response when the
  vault doesn't illuminate.

- **Conversation over report.** The scouting report is the
  opening move, not the final product. The value is in the
  discussion that follows. A probe that produces a perfect
  report but no conversation has failed.

- **Atomize later, not now.** When the user rambles and produces
  rich context, don't extract atoms during probe. Flag
  `atomizable: true` and let atomize handle extraction with
  its full procedure. Probe's job is scouting and eliciting,
  not structuring.

- **Pin with rationale.** When suggesting a pin, explain *why*
  the connection matters for the project or frame — not just
  "these atoms share a tag" but "the concern here is the same
  concern driving your third chapter."

## What Probe Replaces

Probe absorbs the backward-facing part of what conversational
collaboration currently does. When the user brings content and
asks "what in my vault connects?" — that's a probe. The
difference: probe formalizes the output (memory entry with
resolution status and atomizable flag) so the orchestration
layer can track thread lifecycle.

Conversational collaboration remains the primary mode for
engagement with vault content that isn't an incoming capture.
"Help me think about this draft" or "what contradicts this
claim" are collaboration, not probe. The distinction: probe
starts from new material arriving. Collaboration starts from
existing material being worked.

## Provisional Notes

This is v0.1. Expected revisions after first use:

- The conversation model may need more structure or less.
  Are the resolution values right? Is `atomizable` useful
  as a flag or should probe just note it in prose?
- The relationship to trace needs testing. Does the visual
  artifact actually help during probe, or is it a distraction?
- The interaction between probe and the reflection reply
  mechanism may create friction. If a capture is probed in
  a CC session, does it also appear in the next reflection?
  Should it? The orchestrator will need to manage this
  deduplication.
- Pin mechanics are unspecified. "Pin to project" needs a
  structural meaning — what changes in the vault when
  something is pinned? This depends on the lookbook question
  resolving.
