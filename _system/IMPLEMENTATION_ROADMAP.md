---
type: system
purpose: implementation roadmap
created: 2026-04-08
status: active — work from this
---

# Implementation Roadmap

Walk away from the design crash intact. Work from this.

---

## Current State (after this session)

**Implemented:**
- Four concrete fixes applied (tend access, pulse removed,
  reflect unburdened, HOME cleaned, atom retrieval standardized,
  protocol-wins note)
- Vault skills operational: atomize, tend, reflect (frame-read
  and trace unrun but specified)

**Documented:**
- Consolidated design review (DESIGN_REVIEW_CONSOLIDATED.md)
- Chronicle design seed (DESIGN_SEED_CHRONICLE.md)
- Facts/events design note (DESIGN_NOTE_FACTS_EVENTS.md)
- Event catalog and threads (EVENT_CATALOG_AND_THREADS.md)
- Probe skill spec (probe.md, provisional v0.1)
- Orchestrator protocol (ORCHESTRATOR_CLAUDE_MD.md)

---

## Phase 1: Orchestrator Bootstrap

**Goal:** CC becomes the orchestrator. Test the event-handler
pattern before building anything new.

### Step 1.1 — Install the orchestrator protocol

Copy ORCHESTRATOR_CLAUDE_MD.md into the vault as CLAUDE.md
(or whatever CC reads on invocation). This replaces or
supplements the existing AGENT_PROTOCOL.md read — the
orchestrator protocol references the agent protocol but adds
the event-handler evaluation loop.

**Decision needed:** Does CLAUDE.md replace AGENT_PROTOCOL.md
as the first-read file, or does the orchestrator read both?
Recommendation: CLAUDE.md is the entry point. It instructs CC
to read AGENT_PROTOCOL.md for skill behavior. The orchestrator
wraps the protocol.

### Step 1.2 — Run a normal cycle with orchestrator awareness

Do your normal thing: journal, invoke CC. But now CC reads the
orchestrator protocol and evaluates conditions before acting.
It should tell you: "Here's what I found. Here's what I
recommend." You confirm or redirect.

**Test for:** Does the evaluation feel useful or like overhead?
Does CC correctly identify which conditions are met? Does the
pacing feel right?

### Step 1.3 — Test the frame-read trigger

Run tend. After tend completes, invoke CC with the orchestrator
protocol. It should check: did tend enrich 3+ atoms in any
frame's territory since the last frame-read? If yes, it
recommends firing frame-read for that frame. You confirm. This
is the first event handler firing in the wild.

**Test for:** Does the threshold feel right? Is 3 too low or
too high? Does frame-read produce useful output on the
triggered frame?

**Estimated time:** 1-2 sessions to install and test.

---

## Phase 2: Probe

**Goal:** Experience the probe conversation pattern. Feel
where threads want to persist.

### Step 2.1 — Install probe.md

Copy probe.md into `_system/_skills/`. It's provisional v0.1.

### Step 2.2 — Run 3-5 probe conversations

Capture something (a link, a song, an image, an idea). Invoke
probe. Have the conversation. Write the memory entry.

Vary the inputs:
- A rich capture with obvious vault connections
- A bare link with no context
- Something you feel strongly about but can't explain why
- Something that connects to an active project
- Something that connects to nothing

### Step 2.3 — Note the friction

After each probe, note:
- Did you want to come back to this conversation later?
- Did you want the memory entry to be richer or thinner?
- Did the probe feel like discovery or like a database query?
- Was there a moment where you wanted to "send" something
  to the vault but the mechanism was clunky?
- Did you want to see the probe output somewhere specific
  (HOME? a thread view? inline?)

**These friction notes are the spec for threads.** Don't
design threads abstractly. Let the probe conversations reveal
what threads need to be.

### Step 2.4 — Test the orchestrator's probe awareness

After running probes, invoke CC with the orchestrator protocol
on a fresh session. It should find probe memory entries and
assess: are there unresolved probes to resurface? Atomizable
material to flag? This tests the probe → orchestrator → next
action chain.

**Estimated time:** 1-2 weeks of regular use.

---

## Phase 3: Event Formalization

**Goal:** Name and track events explicitly. Build toward
reactive behavior.

### Step 3.1 — Add a Recommended Actions section to tend

Update tend.md to include a `## Recommended Actions` section
in its memory entry. After Part 4 (the log), tend explicitly
states what its output implies:
- "Frame writing-practice: 4 atoms enriched → frame-read
  recommended"
- "Atom X promoted to developing → trace candidate"
- "New frame proposed → awaiting activation"

This makes tend's events machine-readable for the orchestrator
rather than requiring it to infer from atoms_touched counts.

### Step 3.2 — Add resolution tracking to probe

Ensure every probe memory entry has the `resolution:` field
(connected | pinned | discussed | unresolved) and the
`atomizable:` flag. The orchestrator reads these to manage
probe thread lifecycle.

### Step 3.3 — Track event history

Start noting (even informally) which handler conditions fire
and which don't. After a month: which handlers fired most
often? Which never fired? Which thresholds need adjusting?
This is the empirical basis for tuning the orchestrator.

**Estimated time:** Ongoing through Phases 2-3.

---

## Phase 4: Thread Infrastructure

**Goal:** Build the thread interaction surface. Only after
probe conversations have revealed the natural shape.

### Step 4.1 — Choose thread storage model

Based on Phase 2 friction notes, decide between Options A/B/C
from the event catalog doc. Current lean: Option C (thread
folders with index + conversation + preserved stimulus). But
practice may reveal that something simpler works.

### Step 4.2 — Build minimal thread support

Before a plugin: simple thread files that CC can read and
append to. The "chat" feel comes later. The data model comes
first.

Test: Can CC resume a thread from a previous session by
reading the thread file? Does it feel continuous or disjointed?

### Step 4.3 — Scope the thread plugin

Once the data model is tested, scope an Obsidian plugin that
renders threads as chat:
- Bold/unread at top, old below
- Searchable
- Agent can bump threads up
- Send button for replies
- Inline and responsive feel

This is a real plugin project. It may be the first significant
Obsidian development work. Budget time accordingly.

**Estimated time:** Phase 4.1-4.2: 1-2 weeks. Phase 4.3:
separate project with its own timeline.

---

## Phase 5: Chronicle

**Goal:** Start the narrative practice. Only when there's
enough story to tell.

### Step 5.1 — Write the first cards retrospectively

Look back at the vault's history. Write 5-10 chronicle cards
covering the major moments: first atoms extracted, first tend
run, first frame proposed, the design sessions, the turning
points. This seeds the chronicle with narrative structure.

### Step 5.2 — Integrate with orchestrator

Add the chronicle-moment handler to the orchestrator protocol.
After significant events (atom promoted, frame proposed, probe
pinned), the orchestrator writes a chronicle card.

### Step 5.3 — Test narrative value

After a month of chronicle cards: read them in sequence. Does
the story make sense? Is it useful? Does it change how you
think about the vault's development?

**Estimated time:** Depends on Phases 1-4 maturity. Not before
Phase 3 at minimum.

---

## Phase 6: Autonomous Agent

**Goal:** Graduate beyond CC terminal simulation.

### Step 6.1 — Evaluate agent frameworks

Assess OpenClaw, Hermes, or similar for compatibility with:
- The vault's file-based architecture
- The event-handler model
- The orchestrator protocol
- Obsidian integration

### Step 6.2 — Port the orchestrator

The orchestrator protocol (CLAUDE.md) becomes the agent's
main loop. Event evaluation happens continuously or on
triggers rather than on human invocation.

### Step 6.3 — Implement autonomous handlers

Move handlers from "human confirms" to "agent executes"
one at a time, starting with lowest-risk:
1. Frame-read triggers (low risk — read-only output)
2. Index regeneration after tend (pure maintenance)
3. Probe initiation on new captures (medium risk — starts
   conversations)
4. Chronicle card writing (narrative, not structural)

High-risk handlers (anything that creates atoms or modifies
the structural layer) stay human-gated longest.

### Step 6.4 — Build the send button

Journal "send" (triggers reflect), capture "send" (triggers
orchestrator assessment), thread reply "send" (continues
thread). These replace manual CC invocation with UI triggers.

**Estimated time:** Separate project. Depends on framework
maturity and plugin development.

---

## Phase 7: Teaching / Distribution

**Goal:** Seed vaults for students.

### Step 7.1 — Extract the template

Separate the vault into portable structure (skills, protocol,
templates, orchestrator, HOME layout, plugin configs) and
personal content (atoms, reflections, projects, memory,
chronicle).

### Step 7.2 — Build domain-specific seeds

Starter frames, reference atoms, experiment templates for
specific courses or domains.

### Step 7.3 — Test with students

Pilot with a small group. Watch where they struggle. The
thread interface and orchestrator pacing will be the most
sensitive to user variation.

**Estimated time:** After Phases 1-5 are stable.

---

## What to Ignore Until It's Needed

- The membrane (requires plugin; aspirational)
- Multi-agent orchestration (requires framework maturity)
- Graph database (requires atomic density that triggers it)
- Cross-vault pollination (requires multiple active vaults)
- Exhibits / public surface (requires finished work)
- Art-making MCPs (requires outbound channels)

These are all documented extension points. They don't
constrain current work. Don't build toward them. Build
what's needed now and let the extension points activate
when their time comes.

---

## The Rule

Test before you spec. Spec before you build. Build one
thing at a time. Feel the friction. Let the friction tell
you what's next.
