"""Lane positioning constants and placement heuristics.

Lanes are horizontal bands defined by y-range.
Process flows left-to-right; each new node is appended to the right
edge of its lane. Users reposition by hand after capture — layout
is approximate, not pixel-perfect.
"""

# y-center for each lane's content
LANE_Y = {
    "ARTIFACTS":   0,
    "TRANSITIONS": 1000,
    "ANNOTATIONS": -600,
}

LANE_LABEL_X = -1700    # x for the three lane-label text nodes
LEGEND_X = -1700
LEGEND_Y = -1200

# Default node sizes
FILE_W, FILE_H = 400, 400
TEXT_W, TEXT_H = 320, 140
LANE_LABEL_W, LANE_LABEL_H = 140, 50
LEGEND_W, LEGEND_H = 340, 240

# Horizontal spacing between nodes within a lane
X_START = 0
X_GAP = 120

# A node is "in" a lane if its vertical center is within this distance of LANE_Y
LANE_HALF_HEIGHT = 500

DEFAULT_LEGEND_TEXT = (
    "LEGEND\n\n"
    "cyan   = vault file (exists, clickable)\n"
    "orange = external / to import\n"
    "color 1 = annotation (observation, wish, alert)\n"
    "  [AGENT]: prefix = agent / AI annotation\n"
    "  no prefix = user annotation\n"
    "no color = transition"
)


def lane_label_nodes():
    return [
        {
            "id": "lane-artifacts",
            "type": "text",
            "text": "ARTIFACTS",
            "x": LANE_LABEL_X,
            "y": LANE_Y["ARTIFACTS"] - LANE_LABEL_H // 2,
            "width": LANE_LABEL_W,
            "height": LANE_LABEL_H,
        },
        {
            "id": "lane-transitions",
            "type": "text",
            "text": "TRANSITIONS",
            "x": LANE_LABEL_X,
            "y": LANE_Y["TRANSITIONS"] - LANE_LABEL_H // 2,
            "width": LANE_LABEL_W,
            "height": LANE_LABEL_H,
        },
        {
            "id": "lane-annotations",
            "type": "text",
            "text": "ANNOTATIONS",
            "x": LANE_LABEL_X,
            "y": LANE_Y["ANNOTATIONS"] - LANE_LABEL_H // 2,
            "width": LANE_LABEL_W,
            "height": LANE_LABEL_H,
        },
    ]


def legend_node(text=None):
    return {
        "id": "legend",
        "type": "text",
        "text": text or DEFAULT_LEGEND_TEXT,
        "x": LEGEND_X,
        "y": LEGEND_Y,
        "width": LEGEND_W,
        "height": LEGEND_H,
    }


def _nodes_in_lane(canvas, lane):
    cy = LANE_Y.get(lane, 0)
    result = []
    for n in canvas["nodes"]:
        nid = n.get("id", "")
        if nid.startswith("lane-") or nid == "legend":
            continue
        if n.get("type") == "group":
            continue
        ny = n.get("y", 0)
        nh = n.get("height", 0)
        center_y = ny + nh / 2
        if abs(center_y - cy) <= LANE_HALF_HEIGHT:
            result.append(n)
    return result


def next_position(canvas, lane, node_w=None, node_h=None):
    """Return (x, y) for the next node appended to the right of the given lane."""
    if node_w is None:
        node_w = FILE_W
    if node_h is None:
        node_h = FILE_H

    cy = LANE_Y[lane]
    y = cy - node_h // 2

    nodes = _nodes_in_lane(canvas, lane)
    if not nodes:
        return X_START, y

    max_right = max(n.get("x", 0) + n.get("width", 0) for n in nodes)
    return max_right + X_GAP, y
