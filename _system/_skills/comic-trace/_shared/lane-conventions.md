---
type: reference
name: lane-conventions
created: 2026-04-30
---

# Lane conventions and layout limits

---

## How layout works

The skill uses a simple left-to-right append strategy:
- Each new node is placed at `x = rightmost-node-in-lane + gap`
- y is set to center the node vertically in its lane's y-band

This produces a timeline that reads left-to-right, with the three lanes as horizontal bands.

---

## Layout limits (known)

- **Auto-layout is approximate.** Nodes will not be pixel-perfect aligned with related nodes in adjacent lanes. Expect manual repositioning in Obsidian after capture.
- **Skill is additive only.** Existing node positions are never changed by the skill. A `capture` call adds to the right; it does not reflow the rest of the canvas.
- **Nodes are centered in their lane y-band.** A journal node (400px tall) centered at y=0 occupies y=-200 to y=200. Annotation nodes (shorter) are centered at y=-600.
- **The skill detects lane membership by y-center proximity** (`LANE_HALF_HEIGHT = 500`). A node placed far from its lane's center (by the user) may not register correctly for next-position calculation. This is fine — user repositioning is expected.

---

## Suggested workflow

1. Run capture commands in the order events actually happened (journal → hold → inbox → image).
2. Open the canvas in Obsidian; drag nodes to better positions.
3. The graph (nodes + edges) is what the skill produces and validates. The exact layout is yours to arrange.

---

## Lane y-centers (from config.yaml)

| Lane | y-center |
|---|---|
| ANNOTATIONS | -600 |
| ARTIFACTS | 0 |
| TRANSITIONS | 1000 |

Lane labels are placed at x=-1700.
