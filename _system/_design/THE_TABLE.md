---
type: system
purpose: design aspiration — the table
created: 2026-03-11
---

# The Table

A method for discovering structure from below, inspired by how
David Lynch writes screenplays: accumulate scenes on notecards
until you have enough, then arrange them until structure emerges.

---

## The Method

### 1. Accumulate Mass

Start a project with no divisions. Just a brief that names the
territory. Write fragments — notecards — and drop them in `drafts/`
with no ordering, no chapter numbers. Just names.

Don't worry about structure. Don't worry about sequence. Write
the pieces that want to be written. Stop when there's enough.

### 2. Annotate

Ask the agent to deeply read each fragment against the atomic
layer and produce a layered annotation:

**Surface:** What does this piece say? What's its argument or scene?

**Subtext:** What atoms connect to it — not as a list, but
interpreted. What is this piece *really* about underneath? What
thinking from the vault is alive in it, even if not explicitly
referenced?

**Needs:** What does this piece need a reader to already feel,
know, or be unsettled by before it can land?

**Leaves:** What state does it leave the reader in? What are they
ready for next?

Annotations go to `_memory/`. Each one is a dense reading of a
single fragment grounded in the vault's accumulated thinking. The
atoms are the subtext made explicit.

### 3. Arrange

Activate the table. The agent reads all the annotations and
proposes arrangements — possible sequences, each with a rationale.

In the current system (single agent, multiple frames), the agent
argues for different orderings through different frame lenses:
- The writing-practice frame proposes an order optimized for
  voice and rhythm
- The systems-thinking frame proposes an order optimized for
  argument and escalation
- The teaching frame proposes an order optimized for the reader's
  progressive understanding

Each proposed arrangement is a canvas — the cards laid out in
sequence, annotated with why this order, what it foregrounds,
what it sacrifices.

### 4. Curate

You pick. Or you rearrange by hand, seeing something none of the
frames saw. The structure that emerges isn't dictated by any single
perspective — it's sculpted from the collision of multiple argued
arrangements.

The chosen arrangement becomes the project's divisions, retroactively.
Divisions aren't always declared up front. Sometimes they emerge
from below.

---

## Running the Experiment

These are concrete steps for a Claude Code session. Read
`_system/AGENT_PROTOCOL.md` first, then come back here.

### Prerequisites

- The vault is set up and operational (journal entries migrated,
  atoms exist from at least one atomize run, at least one frame
  is active)
- A project exists with a brief that names the territory but has
  **no divisions declared** — just intent and audience
- Draft fragments exist in the project's `drafts/` folder — at
  least 4-5 pieces, unordered, each a self-contained scene,
  argument, vignette, or experiment

If the project doesn't exist yet, help the user create it:
1. Create `_projects/[project-name]/`
2. Create `_BRIEF.md` with intent and audience only. Leave the
   Divisions section as: `Structure to be discovered via the table.`
3. Create `drafts/` — the user will populate this with fragments

### Step 1: Annotate the Fragments

For each draft fragment in the project's `drafts/` folder:

1. Read the fragment closely.
2. Read `_atoms/` to find what connects — not by wikilink but by
   semantic understanding. What ideas in the vault are alive in
   this piece?
3. Write an annotation to `_memory/` with this frontmatter:

```yaml
---
type: memory
skill: collaboration
method: table-annotation
project: [project-slug]
fragment: [fragment-filename]
date: YYYY-MM-DD
---
```

4. The annotation body has four sections:

**Surface:** What does this piece say? Summarize its argument,
scene, or movement in 2-3 sentences.

**Subtext:** What atoms connect to it, *interpreted*. Don't list
atoms — explain what this piece is really about underneath, citing
atoms as you go with `[[wikilinks]]`. What thinking from the vault
is alive in this fragment, even if the author didn't explicitly
reference it?

**Needs:** What does this piece need from a reader before it can
land? What prior knowledge, emotional state, or unsettled question
makes this piece work? Be specific.

**Leaves:** What state does this piece leave the reader in? What
are they ready for, primed for, or unsettled by after reading it?
What does this piece hand off to whatever comes next?

5. After annotating all fragments, write a summary memory entry
   noting patterns across the fragments — shared concerns, tonal
   range, potential tensions.

### Step 2: Propose Arrangements

Read all the annotations you just wrote. Then, for each active
frame in `_frames/`:

1. Read the frame definition.
2. Adopt its perspective, concerns, and vocabulary.
3. Propose a sequence for the fragments. For each placement, cite
   the Needs/Leaves annotations: "Fragment A leaves the reader
   unsettled about X, which is exactly what Fragment C needs."
4. Name what this arrangement foregrounds and what it sacrifices.
5. Write the proposed arrangement to `_memory/` with:

```yaml
---
type: memory
skill: collaboration
method: table-arrangement
project: [project-slug]
frame: [frame-slug]
date: YYYY-MM-DD
---
```

After all frame-based arrangements are written, propose one
additional arrangement that isn't tied to any frame — your own
best reading of how the fragments want to sit together based on
the Needs/Leaves chain alone.

### Step 3: Generate Canvases

For each proposed arrangement, generate an Obsidian `.canvas` file
in the project folder:

- `[project-name]/arrangement-[frame-slug].canvas`
- `[project-name]/arrangement-unframed.canvas`

Each canvas should show:
- Fragment cards in sequence (top to bottom or left to right)
- Edges between consecutive fragments
- Annotation excerpts (Needs/Leaves) as smaller cards on the edges
- A title card naming the frame and its rationale

Canvas format reference (Obsidian JSON):
```json
{
  "nodes": [
    {
      "id": "unique-id",
      "type": "text",
      "text": "Card content in markdown",
      "x": 0,
      "y": 0,
      "width": 400,
      "height": 200
    },
    {
      "id": "unique-id-2",
      "type": "file",
      "file": "path/to/draft-fragment.md",
      "x": 0,
      "y": 300,
      "width": 400,
      "height": 200
    }
  ],
  "edges": [
    {
      "id": "edge-id",
      "fromNode": "unique-id",
      "toNode": "unique-id-2",
      "label": "edge annotation"
    }
  ]
}
```

Use `type: "file"` nodes for the draft fragments (so clicking opens
the actual file in Obsidian) and `type: "text"` nodes for
annotations and rationale.

### Step 4: Present to the User

Show the user:
- How many fragments were annotated
- How many arrangements were proposed (one per active frame + one unframed)
- A brief summary of how the arrangements differ — what each
  foregrounds and sacrifices
- Invite the user to open the canvases and respond

Then wait. The user curates. They might pick one, remix several,
or rearrange by hand. Whatever they choose becomes the project's
division structure — update the brief accordingly.

---

## The Future Version: Advocates

When multi-agent orchestration becomes viable (nanoclaw, openclaw,
or similar), each fragment gets a literal advocate — a temporary
agent that has deeply read its piece and argues for its placement.

Advocates negotiate sequence based on what their piece needs and
what it offers. Multiple candidate orderings emerge from the
negotiation. Frames sit at the table too, arguing for arrangements
that serve their perspective.

The collision of fragment-advocates and frame-perspectives produces
structure that no single agent could design from above.

---

## What This Requires Today

Nothing we haven't already built:
- A project with no pre-declared divisions
- Draft fragments in `drafts/`
- The atomic layer providing subtext through connections
- Conversational collaboration for annotation
- Frame-read for argued arrangements
- Canvas generation for visualizing proposed sequences

The only design acknowledgment needed: projects can start
division-less. Divisions may emerge from arrangement rather
than being declared in the brief.

---

## The Connection to the Membrane

The table is a session. The membrane is continuous. But they share
a principle: the agent surfaces abundance, the human sculpts by
selection. The table produces candidate arrangements. The membrane
produces candidate connections. In both cases, the creative act is
curation — deciding what stays, what goes, and what order things
take.

---

## Status

Achievable now in simplified form (single agent, multiple frames).
Full version (multi-agent advocates) awaits orchestration tooling.
