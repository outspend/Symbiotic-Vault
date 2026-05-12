---
type: skill-spec
command: comic-trace capture
phase: 1
---

# /comic-trace capture

```
python3 _system/_tools/comic-trace/capture.py <type> <source>
    [--predecessor <id-or-slug>]
    [--lane <ARTIFACTS|TRANSITIONS|ANNOTATIONS>]
    [--comic <slug>]
    [--from <name>]   (for external-feedback type)
```

Appends an artifact node to the right edge of its lane, edges it to its predecessor.

**Type determines:** lane, color, node kind (file vs. text), text prefix.
See `_shared/artifact-types.md` for the full table.

**Predecessor resolution (automatic for journal/hold/inbox):**
- `hold` → reads `source:` frontmatter → finds journal node
- `inbox` → reads `responds_to:` frontmatter → finds hold/journal node
- All other types → use `--predecessor <slug>` or leave unlinked

**Examples:**
```bash
python3 _system/_tools/comic-trace/capture.py journal _journal/2026-04-22.md
python3 _system/_tools/comic-trace/capture.py hold _reflection/2026-04-22-holdv04test.md
python3 _system/_tools/comic-trace/capture.py inbox _inbox/2026-04-22-reply-reply--comic-script.md
python3 _system/_tools/comic-trace/capture.py image _trace/_assets/scroggins-charlie.png \
    --predecessor inbox-2026-04-22-reply-reply--comic-script
python3 _system/_tools/comic-trace/capture.py wish "drag panels like notecards"
python3 _system/_tools/comic-trace/capture.py external-feedback "prefer the graphic style of the initial version" \
    --from "michael scroggins"
```
