---
type: skill-spec
command: comic-trace adopt
phase: 1
---

# /comic-trace adopt

```
python3 _system/_tools/comic-trace/adopt.py <existing-canvas-path> --as-slug <slug>
```

Registers an existing hand-built canvas under skill management.
**Does not modify the canvas** — registry write only.

After adopt, subsequent `capture`, `annotate`, `link-sub` calls using that slug
target the adopted canvas file.

**Validation:** lenient mode — idiosyncratic positioning and custom clusters are accepted.
Malformed JSON is rejected.

**The Scroggins case:**
```bash
python3 _system/_tools/comic-trace/adopt.py \
    _trace/2026-04-22-scroggins-manson-comic-provenance.canvas \
    --as-slug scroggins-manson
```

To revert: edit `_system/_tools/comic-trace/registry.yaml` directly and remove the slug line.
