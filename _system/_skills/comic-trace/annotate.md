---
type: skill-spec
command: comic-trace annotate
phase: 1
---

# /comic-trace annotate

```
python3 _system/_tools/comic-trace/annotate.py <target-id-or-slug>
    [--by user|agent]
    [--type observation|wish|alert|context|modifier]
    [--text "annotation text"]
    [--comic <slug>]
```

## Two modes

**Default (annotation):** adds a color-1 text node in the ANNOTATIONS lane, edged *from target → to annotation* (the annotation is derived from the target).

**`--type modifier`:** adds a critique/calibration node directly below the target, edged *from modifier → to target* (the modifier acts on the target). User-authored modifiers stay uncolored to match the prototype's hand-built critique pattern. Agent modifiers use color 1.

The modifier mode honors the segregation principle: when one party (user or agent) wants to calibrate the other's text, the calibration appears as a separate edge-attached node rather than being silently merged into the original. Future readers see both takes.

## Segregation rule

- Agent annotations get a `[AGENT]:` prefix (belt-and-suspenders with the color).
- User modifiers get a `USER MODIFIER (CRITIQUE)` header.
- Agent modifiers get a `[AGENT] MODIFIER` header.
Prefixes are added automatically if absent.

## Text input

Pass via `--text` or pipe/type via stdin.

## Target lookup

Tries exact id first, then id prefix, then filename stem / path fragment.
Use the predictable slug format (`image-scroggins-charlie`) or the exact id from the canvas JSON.

## Examples

```bash
# Regular user annotation in ANNOTATIONS lane
python3 _system/_tools/comic-trace/annotate.py image-scroggins-charlie \
    --by user --type observation \
    --text "first refined character image; led to seed type variations"

# Agent annotation
echo "Charlie's posture reads as recruiter, not lover — matches appraisal framing" | \
    python3 _system/_tools/comic-trace/annotate.py scroggins-charlie --by agent

# User critiquing an agent note (modifier)
python3 _system/_tools/comic-trace/annotate.py post-mike-meta-lesson \
    --by user --type modifier \
    --text "'often catching a temporal compression' is overconfident. 'almost always the fix is...' even moreso."

# Agent acknowledging a user critique (modifier on the modifier)
echo "Critique received. Amend to single-instance language." | \
    python3 _system/_tools/comic-trace/annotate.py 194c9bee925e44c5 --by agent --type modifier
```
