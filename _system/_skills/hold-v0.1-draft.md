---
type: skill
id: hold
version: 0.1-draft
status: draft — structural test of the layered model (Option 1: one skill, one turn, three sequential passes)
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

The journaler writes quickly. What they set down — explicit
asks, open questions, hot phrases, concepts they reached for —
can get lost inside the flow of an argument about it.

Hold preserves each of those things as its own item and
attaches two things to it: a punchy answer, and a candid
account of the ground that answer stood on. Every held item
is a potential thread the journaler can pick up.

The artifact has three layers per item, stacked visibly:

- **held** — what the journal contains, in the journaler's
  own language
- **answer** — the agent's response: a usable answer, a small
  comment, or an honest "this is already complete"
- **candid** — the ground the answer stood on: what the agent
  assumed, what vault material grounded the answer, where the
  agent reached and where a reach was a stretch

The layer cake is the artifact. There is no separate body,
no Threads section, no concluding Candid. A single cross-cut
paragraph at the end handles things that belong to no single
item — and it is also a potential thread.

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
- an explicit question
- a hot line or phrase (something the journaler reached for
  with feeling — a joke, a complaint, a coinage, a quoted bit
  of someone else's language they liked)
- a concept, frame, or distinction the journaler named
- a link they brought in with language around why
- a continuation of a prior reflection's thread (the reply
  is the held item; the old thread is context)

Preserve the journaler's language verbatim when it has force.
Do not paraphrase hot phrases into cleaner labels. If the
journaler's framing is messy, the held item is messy — the
mess is what you are holding.

Do not yet answer, comment, or synthesize. Do not yet reach
for atoms or frames. Just extract and hold.

### Pass 2 — Answer and ground

For each held item, do the work it requires.

For asks and questions, do the research, link-work, or
source-reading the ask asks for. Fetch URLs. For Reddit or
comment-driven links, read enough surrounding discussion to
serve the ask.

Read vault material that grounds each held item:
- atom index (`_atoms/_index.md`) for discovery; then the
  full prose of relevant atoms
- connected atoms via their relations
- frames named or implied by the item
- prior reflections when the item continues something earlier
- project briefs when the item references project work
- the most recent memory entries from atomize, tend, and
  frame-read

The vault informs the agent's answers. The vault also informs
candid: where the answer came from becomes sayable.

Do not force frame or atom relevance. Unframed material is
often the strongest signal. A held item may receive no vault
grounding; that is a legitimate state and candid should say so.

### Pass 3 — Compose

For each held item, write in this order:

**held** — a brief rendering of the item, in the journaler's
language. A quoted phrase, a stated question, a named concept.
Keep it short enough to be pointed at.

**answer** — punchy. A usable answer, a clear comment, a
small observation, or "this is already complete — nothing to
add" when the held item is a line that wants to be held,
not developed. Match the answer to what the held item asks for.
Don't inflate a rough read into a full argument. Don't
develop a line that was complete as the journaler wrote it.

**candid** — the ground the answer stood on. What was
assumed. What vault material grounded the answer (name it:
this atom, this frame, this prior reflection). Where the
agent reached and where the reach was a stretch. If no vault
material grounded the answer, say so. If the agent chose one
read among several, say which others were live. Candid is
brief — one or two sentences per item is typical.

Candid is not hedging for its own sake. It is the receipts.
The answer gets to be punchy because candid does the work
that punch left out.

After all held items, write a single cross-cut paragraph if
one is warranted. The cross-cut is for what belongs to no
single item — a through-line across items, a tension the day
surfaced, a thing that remained after the per-item work was
done. Skip the cross-cut when nothing cross-cuts; don't
manufacture one.

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
**held** — [the journaler's phrase, question, or concept, in their language]

[punchy answer, comment, or "already complete" — 1–3 sentences typical]

*candid:* [the ground; assumptions, vault references, stretches — 1–2 sentences typical]

---
```

Items are separated by a horizontal rule. The cross-cut
paragraph (if present) sits at the end without a `held` label.

Append the reply-button dataviewjs block as in prior reflections,
so each held item is threadable via the reply surface.

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

- **The held is the anchor.** The journaler's language is
  what the agent returns to. Don't translate, compress, or
  clean hot phrases before holding them.
- **Punch and receipts.** Answers are short and usable.
  Candid exposes the ground. Both together, not one at the
  expense of the other.
- **Already-complete is a legitimate answer.** When the
  journaler wrote a line that is the thing itself, return it,
  note it, don't develop it. Candid can say "nothing to add;
  this line carries itself."
- **No synthesis that isn't earned.** The cross-cut
  paragraph exists for genuine cross-cutting. When items are
  actually separate, leave them separate.
- **Every held item is a potential thread.** The artist picks
  up what they want to pick up. The agent's job is to hold,
  not to pre-select.
- **Tone.** A careful reader taking notes for someone whose
  attention is elsewhere. Names things so they can be found
  again. Honest about where the notes came from.
