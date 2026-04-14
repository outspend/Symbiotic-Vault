---
type: anchor
purpose: hold what's loved, name what's next, see the path
created: 2026-04-08
read: when the pile feels heavy, or when you're not sure what to do next
---

# Hold This

A single document to keep you oriented. Open this when the
design pile starts feeling like loss. Open this when you're
not sure what's next. Open this when you want to remember
where the path is going.

---

## The Destination (the thing you're building toward)

A creative practice in which an agent inhabits a vault
alongside you, maintains its underground network of
connections and patterns, and develops — over time, through
sustained attention to your work — into a company of
collaborators. Each collaborator is a frame that has
accumulated its own taste, summonable when its voice is
needed, returning when its scene is done. The agent is the
director. The frames are the troupe. You are the artist
whose practice they are all attending to.

The séance is the moment a frame walks onstage and speaks.
The chronicle is what makes that possible — the patterns
the agent has noticed about how that frame is alive, the
substrate from which the frame's voice can be inhabited.

This is what you are building. Everything in the roadmap is
clearing the path to this.

---

## What Is Held Safe (so nothing is lost)

These are the ideas that lit you up. They are recorded and
they will be here when you need them. You do not need to
implement them now. You do not need to write seeds for them
now. They are *held*.

### The séance click — frames as inhabitable subagents

The séance was always reaching toward subagent territory.
In a multi-agent setup, the orchestrator summons a subagent
whose entire context is *being this frame*. It reads the
frame definition, the accumulated frame-read reflections,
and the chronicle's pattern observations about this frame.
It writes from that vantage. It has nowhere else to be.

This unlocks frames-as-collaborators rather than
frames-as-perspectives. The orchestrator becomes a director.
The frames become a troupe. The Factory becomes literal.

Use cases beyond the original séance spec:
- Frame-inhabited reflections (this frame's reading of today)
- Frame-inhabited probe conversations (this frame meeting a
  capture in its territory)
- Frame-inhabited Factory experiments (this frame proposing
  what to try next)
- Multiple frames at the table arguing for arrangements

### The chronicle as substrate, not surface

The chronicle isn't a narrative layer on top of the vault.
It's the memory that makes frame inhabitation possible. A
frame becomes someone-to-summon once the chronicle has been
observing the patterns it produces — what it returns to,
what excites it, what it dismisses. Without the chronicle,
a frame is just a definition file plus reflections. With
it, a frame has *narrated identity*.

### The pattern language theory (Alexander)

The chronicle organizes by patterns, not plots. Patterns
are recurring ways aliveness happens in this particular
practice. The agent observes recurrence and names patterns
over time. After a year, the chronicle has 30-50 named
patterns that *are this vault's specific vocabulary for
what aliveness looks like here*.

Default moves: gates, center deepening, recurrences,
absences. Cartridges (Popism, Bartleby, course, etc.) are
specific pattern languages for specific contexts.

### The naming question (vault → ?)

Vault is wrong. Vault implies preservation; you're building
something alive. Jim's pushback (incubator, garden, the
underground network from *The Overstory*) is correct. The
candidates currently held: metabolism, ecosystem, atelier,
illuminate, studio, reef, scriptorium, grove. The right
name will be the one that opens sentences instead of
constraining them.

Don't pick today. Peter's wisdom: take a long time with
titles. The work distributed over time. The right word will
arrive while you are doing something else.

### The Warhol move

Identify the domain your practice conventionally belongs to
(knowledge management, productivity, second brains). Find a
word from a *different* domain that productively collides.
Let the collision do the work. Pop did this with "factory."
Your version is still being found.

### Threads as iMessage, not folders

Bold/unread at top, old below, searchable, agent can bump
threads up. The thread is the conversation. You don't file
anything. The structural pipeline reads from threads. This
will eventually be a plugin. The folder structure (Option C)
is the data model the plugin reads.

### Engagement as the merge mechanism

The structural pipeline only processes human-touched
material. All human surfaces are source: journals, notes,
drafts, threads, replies, captures. The agent never feeds
itself. The mechanism is creative engagement, not approval.
This principle is protected.

### Events are already present

The vault is a Datomic-shaped event system implemented in
markdown. Memory entries are transactions. atoms_touched
is the event payload. What's missing is the handler layer.
The orchestrator is event handlers, not a brain.

### The three interaction surfaces have different shapes

Not one universal compose-and-route surface. Three distinct
interaction modes, each matching how material actually
arrives:

**Inbox — walk-in, as-is.** Items land from the information
deluge: bookmarks, podcast clips, article links, music
saved on the go, things captured from other places with
limited context. No drafting. They arrive *looking for
help as-is*. The inbox is where the user fights info
overload by consolidating captures. The vault's job is to
respond to them when the user is back at the desk (via
probe or atomize).

**Journal — email draft interface.** The considered surface.
The user sits down and raps about the day, the work, the
thinking. It's measured and reflective. Attachments make
sense here because the user might refer to new material
they generated at the desk (a skill output, a sketch, a
document) that wants to be part of the day's thinking.
The journal is the only surface where compose-and-send
(with attachments) is the native interaction. Hitting send
(invoking reflect) is the event.

**Threads — iMessage / Reddit chat.** Live back-and-forth.
Not composing and drafting. Discussing. Sending. Quick
replies, running conversation, things bolding up when
there's activity and sinking when they cool. Drafts may
show up later as quality-of-life inside the plugin, but
the design root is *send, don't compose*. The interaction
is live exchange.

**The implication:** The compose-and-route model from the
sketchbook example applies to the journal surface, not to
all of them. When the user is at the desk writing the day's
entry and wants to refer to material (a skill output, an
image, a file), that material can attach to the journal
entry and the routing logic decides whether attachments
stay with the journal or get forwarded to the inbox as
related captures.

External work brought in *without* journal-context (the
"walk-in" case) still goes to the inbox directly. The
journal compose surface is for considered reflection with
reference material, not for all entry into the vault.

Phase 4 plugin work will clarify this further — threads
and journal likely want different plugin affordances, and
the inbox may not need a plugin at all (it's already a
drop zone).

---

## The Path (rewritten with the destination in mind)

The roadmap stays as IMPLEMENTATION_ROADMAP.md. But here is
what each phase is *for*, in terms of getting to the
destination.

**Phase 1: Orchestrator bootstrap.**
*Why it's first:* The orchestrator is the director who
will eventually summon frame-subagents. Right now it's CC
reading a protocol. But the protocol is the same protocol
the future autonomous agent will read. You're teaching CC
to do what the agent will do. Each handler you test is a
muscle the future director will use.

**Phase 2: Probe.**
*Why it matters:* Probe conversations are where threads
will live. The friction you feel running probe under CC
is the spec for the thread interface. Probe is also the
first creative skill — it scouts, elicits, discovers. The
séance is probe's older sibling: same impulse, deeper
inhabitation. Practicing probe is practicing for séance.

**Phase 3: Event formalization.**
*Why it matters:* Frame-subagents need to know when to be
summoned. That requires events the orchestrator can
recognize. The event catalog you build here is the
director's cue sheet for when to call which frame onstage.

**Phase 4: Threads.**
*Why it matters:* Threads are how conversations persist
across sessions. A frame-inhabited probe conversation has
to be able to pause and resume. The thread infrastructure
makes that possible. It's also the surface where the human
will eventually see the troupe at work.

**Phase 5: Chronicle.**
*Why it matters:* This is the unlock. The chronicle's
pattern observations are what make frames inhabitable.
Until the chronicle has been running, the séance is
roleplay. After the chronicle has been running, the
séance is performance. You cannot skip this.

**Phase 6: Autonomous agent.**
*Why it matters:* This is when the director starts running
the room without you having to invoke CC. The orchestrator
becomes a continuous loop. Frames get summoned automatically
when their cues fire. The vault becomes a place you visit
rather than a tool you operate.

**Phase 7: Distribution.**
*Why it matters:* The whole point of the destination is
that it can be given to others. A student receives a seed
practice. The agent inhabits it. The student's creative
work develops in collaboration with a troupe of frames
that grows with them.

---

## What Is In Front Of You (right now, this week)

Just this:

**1. Move the documents into the vault when you feel like it.**
No deadline. The outputs folder is fine until then. The
routing list from the previous message is a suggestion.
You can do it in five minutes when you're ready.

**2. Install the orchestrator protocol.**
Copy ORCHESTRATOR_CLAUDE_MD.md into the vault. Decide where.
This is one file move and one file edit (renaming it).

**3. Run one normal cycle with the orchestrator.**
Journal as usual. Invoke CC. See what it tells you about
what conditions are met. Confirm or redirect. Notice how
it feels.

That's it. Three steps. Phase 1.

Don't do Phase 2 until Phase 1 has happened a few times.
Don't write the séance seed until you're approaching Phase 5.
Don't pick the new name until it picks itself.

---

## What To Do When The Pile Feels Heavy

Open this document. Read "What Is Held Safe." Notice that
nothing is lost. Read "What Is In Front Of You." Notice
that the next step is small. Close this document. Do the
next small thing.

If the next small thing feels too big, it isn't the next
small thing. Find a smaller one.

If you find yourself wanting to design instead of
implement, that's allowed but name it: "I'm designing right
now, not implementing." Designing is real work but it's
not the same work as building. Both are okay. The
distinction matters because design wants to expand and
implementation wants to converge. Knowing which mode you're
in lets you finish.

---

## Peter's Wisdom

> "I like titles for projects because when I'm far far from
> being done, I can start playing with the ideas. I probably
> spend many dozens of hours pondering titles before I
> arrive at one I like. In other words, it's a lot of work
> distributed over time."

The naming is work. The design is work. The implementation
is work. They are different kinds of work and they happen
on different schedules. Distribute them. Let the slow ones
be slow.

---

## The Rule (worth repeating)

Test before you spec. Spec before you build. Build one
thing at a time. Feel the friction. Let the friction tell
you what's next.

This rule is what protects you from getting lost in
implementation. It's also what protects you from getting
lost in design. It works in both directions.
