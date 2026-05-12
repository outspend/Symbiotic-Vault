---
type: skill
id: hold
version: 0.3-draft
status: draft — register separation between answer and candid
trigger: daily (default), or on-request with date range
access_summary:
  _journal: read
  _inbox: read (by date, regardless of processed status)
  _reflection: read (recent) + add
  _atoms: reachable (follow leads from held items)
  _frames: reachable (follow leads from held items)
  _projects: reachable (follow leads from held items)
  _memory: read (date-scoped recent entries from atomize, tend, frame-read) + add (handoff)
  web: read (URLs found in journal/inbox seed)
---

# Skill: Hold

A structured holding practice for the journaler's material.

## Purpose

The journaler writes quickly. In their excitement, the ground they cover — explicit
asks, open questions, hot phrases (gems), concepts they are circling —
can get a bit messy.

Hold preserves each of those things as its own item and
makes two offerings: an observation that meets the item where
it is, and a candid account of the ground this reply stood on.
Every held item is the opening entry (and context) for a 
potential discussion thread with the journaler.

The artifact has three layers per item, stacked visibly:

- **held** — what the journal contains, with special regard for 
  the journaler's own framing and language
- **observation** — a response that meets the item's epistemic frame:
  answer the ask, observe the development of a concept, sit with the phrase
- **candid** — the analytical home: what was assumed, what
  vault material grounded the answer, where the agent
  reached and in what manner

This three layer cake is the artifact. A single cross-cut
paragraph at the end catches what belongs to no single
item —  it is also a potential thread.

## Register

The layers divide the work by register:

- The **held** carries the journaler's voice.
- The **observation** attempts to mirror the  journaler's voice.
   It responds in kind — analytical if the item
  is analytical, playful if the item is playful, quiet if
  the item is quiet, inquisitive if the item is unsettled. Interested Vault material 
  wants to make a tentative introduction.  If nothing from the vault seems
  to step intuitively forward — or call it a novel thread.
- The **candid** is where analytical register and vault's precision
  voice appears. Candid is the place to name what atom shaped
  an answer or  what frame was leaned on - what assumption shaped an 
  observation. Candid carries the receipts.

Output goes to `_reflection/YYYY-MM-DD.md` for continuity
with existing vault infrastructure.

## Invocation

- "hold" or "hold today" — today's journal
- "hold [date]" or "hold [date range]" — specified scope

## Procedure

Three sequential passes in one turn. Complete each pass before
starting the next. The first pass does not reach for vault
material. The second pass does. The third speaks only from
what the first two produced.

### Pass 1 — Read and hold (no vault access)

Establish the window: after the previous entry in `_reflection/`
before the target date, through the target date. Use
frontmatter dates, not filenames.

Read the target journal entry. Read inbox items whose
`created:` frontmatter falls within the window, regardless of
processed status. Read replies to prior reflection or hold
entries (inbox items whose `responds_to:` points into
`_reflection/`).

Scan the journal and in-scope inbox for URLs. Note them as
held items; defer fetching to Pass 2.

Extract held items. An item is anything the journaler set
down that deserves preservation in its own right:

- an explicit ask or request
- a hot line or phrase (something the journaler reached for
  with feeling — a joke, a complaint, a coinage, a quoted bit
  of someone else's language they liked)
- a concept, frame, or distinction the journaler named
- a link they brought in with language around why

**Render each held item according to its kind:**

- **Hot phrases** are held verbatim. The words are the
  thing. Preserve them in quotation marks, in the
  journaler's exact language. Do not clean or compress.
- **Asks, concepts, and links** are held as loglines — a
  short pointable rendering that names the item. The words
  are instrumental; the logline is a handle that makes the
  item a thing the observation (or answer) can meet. Preserve the
  journaler's live framing where it has force, but the
  logline doesn't have to be a direct quote.

Do not yet answer, comment, or synthesize. Do not yet reach
for atoms or frames. Just extract and hold.

### Pass 2 — Answer and ground

For each held item, do the work it requires.

For asks and questions, do the research, link-work, or
source-reading the ask asks for. Fetch URLs. For Reddit or
comment-driven links, read surrounding discussion to
see what may serve the reply.

Read vault material that grounds each held item:
- atom index (`_atoms/_index.md`) for discovery; then the
  full prose of relevant atoms
- connected atoms via their relations
- frames named or implied by the item
- prior reflections when the item continues something earlier
- project briefs when the item references project work
- the most recent memory entries from atomize, tend, and
  frame-read

Vault material will ground the candid
section and may sit alongside the observation, but it does not
dictate the register. Do not force frame or atom
relevance.  privilege analogy (creative) topology over (information) categorization
as the most interesting vault signal.  A held item may receive no vault grounding; that is a
legitimate state and candid should say so.

### Pass 3 — Compose

For each held item, write in this order:

**held** — the item rendered according to its kind: verbatim
for hot phrases, logline for asks/concepts/links.

**answer** — meet the item where it is.

- **Answer the ask.** If the item is a request or question,
  give a usable answer. Do the research or link-work. Match
  the answer resolution to what the ask actually wanted — a rough
  read, a list, a set of prompts, a direct response. Don't
  inflate a rough read into a full argument.
- **Observe the concept.** If the item is a concept, frame,
  or distinction the journaler named, respond with a 
  comment that extends or situates the thought. One or two
  sentences to develop, not to argue.
- **Sit with the phrase.** If the item is a hot phrase or
  line that carries itself, sit alongside it. Name what
  makes it fly, riff briefly in the same register, or
  simply acknowledge "hold this one." Don't explain the
  line. Don't analyze the joke. The line is the thing; the
  answer is a companion note.

Vault material may sit alongside any of these postures if the
connection is intuitive. If it isn't intuitive, don't build
momentum to force the connection — find a different way to
sit alongside, or let candid name it as a new thread the
vault hasn't held yet.

**candid** — the analytical layer. What was assumed. What
vault material grounded the answer (name it: this atom, this
frame, this prior reflection). Where the agent reached and
where the reach was a stretch. If no vault material grounded
the answer, say so. If the agent chose one read among
several, say which others were live. One or two sentences
per item is typical.

Candid is where the analytical and vault-voice register
lives. The answer gets to stay near the journaler because
candid carries the receipts.

After all held items, write a single cross-cut paragraph if
one is warranted. The cross-cut is for what belongs to no
single item — a through-line across items, a tension the day
surfaced, a thing that remained after the per-item work was
done. Skip the cross-cut when nothing cross-cuts; don't
manufacture one.

the cross-cut draws from the target journal entry; fresh-alongside 
inbox items are held but enter the cross-cut only when they bear 
directly on today's writing. 

The cross-cut is itself a held item of a different kind. It
is also a potential thread.

## Format

Write to `_reflection/YYYY-MM-DD.md` with frontmatter:

```yaml
---
type: reflection
date: YYYY-MM-DD
skill: hold
---
```

Per-item structure:

```
**held** — [verbatim phrase OR logline for the item]

[answer that meets the item where it is]

*candid:* [assumptions, vault references, stretches]

---
```

Items are separated by a horizontal rule. The cross-cut
paragraph (if present) sits at the end without a `held` label.

Append the reply-button dataviewjs block, but adapt the reply
surface to the hold structure: pre-populate one reply block per
held item, quoting the full item (`held`, `answer`, and `candid`)
as the context for reply. If a cross-cut paragraph is present,
include it as its own final reply block. The reply surface should
let the journaler answer item by item rather than forcing one
undifferentiated note.

## Memory handoff

Write a compact memory entry to `_memory/`:

```yaml
---
type: memory
skill: hold
date: YYYY-MM-DD
atoms_touched:
  - id: atom-slug
    action: referenced
    note: "optional for developed/challenged"
source: _reflection/YYYY-MM-DD.md
---

See full held entry: [[_reflection/YYYY-MM-DD]]
```

`referenced` / `developed` / `challenged` semantics unchanged
from reflect. Only include atoms that materially informed an
answer, not every atom opened during discovery.

After the link, briefly note operational gaps (missing
indexes, unfetched links, uncertain atom matches).

## Judgment calls

- **The held is the anchor.** Render hot phrases verbatim;
  render asks, concepts, and links as loglines. Don't force
  all held items into one shape.
- **Answer meets the item where it is.** Three postures,
  one orientation: answer the ask, comment the concept, sit
  with the phrase. The item tells the agent which.
- **Vault sits alongside.** If the connection isn't
  intuitive, don't build momentum to force it. Find a
  different position, or let candid name it a new thread.
- **Candid is analytical.** The vault's voice has a home in
  candid. The answer stays near the journaler because
  candid carries the receipts.
- **Already-complete is a legitimate answer.** For hot
  phrases that carry themselves, the answer is a companion
  note, not an explanation.
- **No synthesis that isn't earned.** The cross-cut
  paragraph exists for genuine cross-cutting. When items
  are actually separate, leave them separate.
- **Every held item is a potential thread.** The artist
  picks up what they want to pick up.
- **Tone.** A careful reader taking notes for someone whose
  attention is elsewhere. Names things so they can be found
  again. Honest about where the notes came from.
