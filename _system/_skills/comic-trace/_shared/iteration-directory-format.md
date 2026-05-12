---
type: reference
created: 2026-05-01
for: image-chase (producer) and comic-trace (consumer)
---

# Iteration directory format

The contract between image-chase (which produces the directory) and comic-trace (which reads it to render the sub-canvas). Neither side should diverge from this format.

## Directory layout

```
_trace/_iterations/<comic-slug>/<panel-id>/<timestamp>/
  request-blast.md           user's input; comic-trace links as a file node
  run.json                   run metadata (see below)
  decision-log.md            append-only; craft adaptations, refusals, surface decisions
  gen-batch-01/              one folder per batch
    gen-01-01.png
    gen-01-02.png
    gen-01-03.png
    gen-01-04.png
    contact-01.png           PIL contact sheet (optional but expected)
    batch.json               batch metadata (see below)
  gen-batch-02/
    ...
  notes.md                   picks and surprises; added by user or agent at run end
  run.canvas                 MANAGED BY comic-trace; do not write directly
```

The `<timestamp>` folder name format: `YYYY-MM-DD-HHMM` (e.g., `2026-04-30-1430`).
This becomes part of the stable link-node ID in the main provenance canvas.

## run.json

Written by image-chase at run start; updated at run end.

```json
{
  "comic": "scroggins-manson",
  "panel": "P3",
  "started": "2026-04-30T14:30:00",
  "status": "active",
  "refs": [
    "_style/scroggins-manson/characters/charlie/01.png",
    "_style/scroggins-manson/bible/cartoony-shape-language.png"
  ],
  "batches_fired": 0,
  "total_cost_usd": 0.0,
  "finished": null
}
```

Status values: `active`, `complete`, `stale` (crashed mid-run).

## batch.json

Written by image-chase after each batch returns, before calling
`comic-trace compose-sub-canvas --mode append --event batch`.

```json
{
  "batch_num": 1,
  "prompt": "slight dark-eyed magnetic gaunt figure in grey t-shirt...",
  "refs_used": [
    "_style/scroggins-manson/characters/charlie/01.png"
  ],
  "gens": [
    {
      "id": "01",
      "file": "gen-batch-01/gen-01-01.png",
      "category": "pass",
      "notes": "likeness landed, eyelines correct"
    },
    {
      "id": "02",
      "file": "gen-batch-01/gen-01-02.png",
      "category": "miss",
      "notes": "Charlie eyes still wrong direction"
    },
    {
      "id": "03",
      "file": "gen-batch-01/gen-01-03.png",
      "category": "partial",
      "notes": "style OK, eyeline still off"
    },
    {
      "id": "04",
      "file": "gen-batch-01/gen-01-04.png",
      "category": "refusal",
      "notes": "content policy — likeness refusal"
    }
  ],
  "contact": "gen-batch-01/contact-01.png",
  "timestamp": "2026-04-30T14:31:00",
  "notes": "optional agent notes on the batch"
}
```

All `file` paths in `batch.json` are **relative to the iteration directory**.
`compose-sub-canvas` converts them to vault-relative paths when writing canvas nodes.

### Category values

| Value | Meaning |
|---|---|
| `pass` | Passes the load-bearing constraints from the request blast |
| `partial` | Some constraints met, some not; worth saving |
| `miss` | Failed the key constraints; continue chasing |
| `refusal` | Content policy refusal; agent adapts or surfaces |
| `surprise` | Not in the blast but interesting; surface to user |

## decision-log.md

Append-only markdown. Each entry:

```markdown
## B01 — 2026-04-30 14:31

**Surface:** no — continuing (misses on must-survive, refining prompt)
**Prompt change:** added "no texture, flat pop-art fills" (countering style drift)
**Refusals:** none
**Adaptations:** none
```

For a refusal entry:

```markdown
## B03/gen-03-04 — refusal

**Type:** likeness (suspected explicit name match)
**Adaptation 1:** shape-language only ("slight dark-eyed magnetic gaunt")
**Adaptation 2:** added character archetype framing
**Result:** one passed (gen-03-05), one still refused
**Decision-log ref:** batch-03/refusal-01
```

## Notes on run.canvas

- `run.canvas` is **created and owned by comic-trace**
- image-chase never writes to it directly
- If `run.canvas` is missing mid-run, it means `compose-sub-canvas --mode init` was not called — that is image-chase's bug
- A `run.canvas` with status "ACTIVE" and no new events for >30 min indicates a stalled run; use `compose-sub-canvas --mode mark-stale` to mark it explicitly
