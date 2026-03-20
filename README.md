# Symbiotic Vault

A creative practice vault where human writing and agentic
collaboration sustain each other.

## What This Is

An Obsidian vault built as a shared environment for a human
writer and an AI collaborator (Claude Code). The human writes
freely — journals, drafts, captures — without structural
obligations. The agent maintains a linked atomic layer,
surfaces connections, and produces argued reflections. The
vault's hyperlinked quality grows from collaboration, not
manual linking.

The architecture is a single-pool zettelkasten traversed by
multiple frames (perspectives). Ideas exist once and are seen
differently through different lenses.

## The Skill System

The agent operates through repeatable skills and conversational
collaboration:

- **reflect** — the agent's daily reading practice. Reads the
  journal, engages with the thinking, follows threads into the
  vault, produces the agent's own developing journal.
- **atomize** — extracts concepts, claims, and methods from
  journals and inbox into single-concept atomic notes with
  typed relations.
- **tend** — enriches the atomic layer: discovers connections,
  promotes maturity, harvests concepts from project drafts,
  proposes new frames.
- **frame-read** — reads the atomic layer through a named
  perspective and produces an argued reflection.
- **trace** — generates Obsidian canvas files mapping atoms,
  connections, and provenance paths visually.

Skills learn from each other through structured memory entries
with `atoms_touched` metadata. Each skill reads the most recent
output from every other skill before it runs.

## Surfaces

```
Human writes here:          Agent never modifies these
  _journal/                 (daily notes)
  _inbox/                   (external captures, feedback, references)
  _projects/*/notes/        (brainstorming per division)
  _projects/*/drafts/       (composed writing)

Agent maintains here:       Human browses
  _atoms/                   (single-concept notes, wikilinked)
  _memory/                  (skill traces, collaboration logs)
  _reflection/              (agent's journal)
  _frames/ (proposed)       (frame proposals from tend)

Shared:
  HOME.md                   (human zones + agent-refreshable zones)
  _frames/ (active)         (user-created or user-activated)
  _projects/*/brief-*.md    (user-written, agent helps draft)
```

## Design

The vault's vision and architecture are documented in `_system/`:
- `VAULT_VISION.md` — pillars and principles
- `VAULT_DESIGN.md` — full architecture reference
- `AGENT_PROTOCOL.md` — what the agent reads on every invocation
- `_skills/` — skill definitions
- `_design/` — design critiques, comparisons, and experiment seeds

The design documents in `_system/_design/experiments/` include five
experiment seeds (THE_TABLE, THE_MEMBRANE, THE_SEANCE, THE_COMPOST,
THE_DRIFT) and design notes on architectural decisions. These are
living documents — some aspirational, some ready to test.

## Setup

1. Open this folder as an Obsidian vault.
2. Install three community plugins (Settings → Community Plugins):
   - **Dataview** — powers dashboard queries on HOME.md
   - **Templater** — auto-applies templates for journal and inbox
   - **Homepage** — opens HOME.md on startup
3. In Dataview settings, enable **JavaScript Queries** and
   **Inline JavaScript Queries**.
4. Plugin settings, CSS snippets, and folder templates are
   pre-configured.

## Optional: MCP Integrations

The vault's skills work without external integrations. These are
optional enhancements that extend what the agent can do during
skill runs.

**Reddit access** (for reflect to follow Reddit links in journals):
```
claude mcp add --transport stdio reddit-mcp-buddy -s user -- npx -y reddit-mcp-buddy
```
Provides two capabilities:
- `get_post_details` — fetches a Reddit post and its top-level comments.
  Used when a journal entry links to a Reddit post and asks about its
  content or the shape of the discussion.
- `user_analysis` — looks up a user's recent comment history. Used when
  the journal asks "which commenter is me?" and the human's Reddit
  username is available.

## For Collaborators

If you're reading this vault with an AI assistant, start with:
1. `_system/VAULT_VISION.md` — what this vault believes
2. `_system/VAULT_DESIGN.md` — how it's built
3. `_system/AGENT_PROTOCOL.md` — how the agent operates
4. `_system/_design/DESIGN_NOTE_TANA.md` — what makes this
   vault different from structured note-taking tools
5. `_system/_design/DESIGN_CRITIQUE.md` — known shortcomings
   and aspirations
