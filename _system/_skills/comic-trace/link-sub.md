---
type: skill-spec
command: /comic-trace link-sub
phase: 2
created: 2026-05-01
tool: _system/_tools/comic-trace/link_sub.py
---

# /comic-trace link-sub

Attaches an image-chase sub-canvas as a file node on the main provenance canvas.

Called twice per run — once at start (status active) and once at end (status complete).
The link node ID is stable across both calls (derived from the iteration directory name),
so the second call finds and updates the first node rather than creating a duplicate.

---

## Invocation

```bash
python3 _system/_tools/comic-trace/link_sub.py <sub-canvas-path> \
  [--comic <slug>] \
  [--predecessor <node-id>] \
  [--label <edge-label>] \
  --status active|complete
```

---

## --status active (call at run start)

```bash
python3 _system/_tools/comic-trace/link_sub.py \
  _trace/_iterations/scroggins-manson/P3/2026-04-30-1430/run.canvas \
  --predecessor chatgpt-image-session-p3 \
  --label "fix run" \
  --status active
```

Creates a file node on the main canvas pointing at the sub-canvas:
- Orange color (`"2"`) = in-progress marker
- Label text "fix run / running since HH:MM" above the node
- Edge from predecessor (if given)

The node ID is `sub-link-2026-04-30-1430` — stable for the follow-up complete call.

---

## --status complete (call at run end)

```bash
python3 _system/_tools/comic-trace/link_sub.py \
  _trace/_iterations/scroggins-manson/P3/2026-04-30-1430/run.canvas \
  --status complete
```

Finds the existing link node by its stable ID and:
- Removes the orange color (reverts to default)
- Updates the label text to "fix run / completed HH:MM"

If the node doesn't exist (e.g., active call was skipped), creates a completed node directly.

---

## Comic resolution

If `--comic` is omitted and only one comic is registered, that comic is used automatically.
If multiple comics are registered, `--comic` is required.

---

## Edge label

Default label: `iterated`. Override with `--label` for other relationships.

---

## Visual effect in Obsidian

**During a run:** the main provenance canvas shows an orange node for the sub-canvas.
The user can see at a glance that a fix run is active. Double-click to enter the sub-canvas
and see current state (batches, surface events, refusals).

**After a run:** the node returns to default color. The label shows the completion time.
The sub-canvas remains linked and openable for post-run review.
