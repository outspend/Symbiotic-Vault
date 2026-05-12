---
type: reference
name: artifact-types
created: 2026-04-30
---

# Artifact types

Per-type capture behavior for `capture.py`.

---

## File-node types (become `"type": "file"` nodes)

| Type | Lane | Color | Predecessor inference |
|---|---|---|---|
| `journal` | ARTIFACTS | cyan | none (root of process) |
| `hold` | ARTIFACTS | cyan | `source:` frontmatter → journal |
| `inbox` | ARTIFACTS | cyan | `responds_to:` frontmatter → hold/journal |
| `image` | ARTIFACTS | cyan | explicit `--predecessor` required |
| `image-chase-sub` | ARTIFACTS | cyan | explicit `--predecessor` required |

---

## Text-node types (become `"type": "text"` nodes)

| Type | Lane | Color | Text prefix |
|---|---|---|---|
| `chatgpt-script` | TRANSITIONS | orange | none |
| `chatgpt-image` | TRANSITIONS | orange | none |
| `external-feedback` | ANNOTATIONS | color 1 | `FROM <NAME>\n\n` |
| `wish` | ANNOTATIONS | color 1 | `WISH\n\n` |
| `process-alert` | ANNOTATIONS | orange | `STAGE/PROCESS ALERT\n\n` |
| `idea` | ANNOTATIONS | color 1 | `IDEA\n\n` |

---

## Predecessor inference (lib/resolve.py)

The skill tries to infer predecessor for `journal`, `hold`, `inbox` automatically:

1. **`responds_to:` frontmatter** — inbox files carry `responds_to: [[path]]`; the skill finds the named node and edges from it
2. **`source:` frontmatter** — hold reflections carry `source: path.md`; the skill finds the journal node
3. **Date proximity** — hold files carry `date:` frontmatter; fallback is to find a journal with the same date in `_journal/`

When inference fails, the node is placed without an edge and the tool prints "No predecessor inferred." Pass `--predecessor <id-or-slug>` to override.

---

## Slug format for --predecessor

When referencing a previously captured node by slug, use the predictable id format the skill generates:

```
<type>-<filename-stem>
```

Examples:
- `journal-2026-04-22`
- `hold-2026-04-22-holdv04test`
- `inbox-2026-04-22-reply-reply--comic-script`
- `image-scroggins-charlie`

Or pass the exact node id from the canvas JSON.
