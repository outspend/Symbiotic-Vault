"""Event-type → node/edge construction for compose-sub-canvas append mode.

Each build_* function returns (nodes_list, edges_list) to be added to the canvas.
All layout is relative to the sub-canvas schema (same lanes as main canvas).
"""
from pathlib import Path
from datetime import datetime

from lib import canvas as cv
from lib import layout as ly
from lib import schema as sc

# Sub-canvas batch layout
BATCH_W = 1400
BATCH_H = 900
BATCH_GAP = 200
GEN_W = 300
GEN_H = 300
GEN_PAD = 60
GEN_COLS = 2

CONTACT_W = 360
CONTACT_H = 360

PROMPT_W = 440
PROMPT_H = 180

STATUS_ID = "sub-status"
STATUS_X = 0
STATUS_Y = -1500   # above the ANNOTATIONS lane (y=-600)

# Gen category → canvas color
_CATEGORY_COLOR = {
    "pass":     "4",   # green
    "surprise": "3",   # yellow
    "refusal":  sc.COLOR_ORANGE,
    "partial":  None,  # default
    "miss":     None,
}


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _next_batch_x(canvas):
    """X position for the next batch group in the TRANSITIONS lane."""
    groups = [n for n in canvas["nodes"] if n.get("type") == "group"]
    if not groups:
        return ly.X_START
    max_right = max(n.get("x", 0) + n.get("width", 0) for n in groups)
    return max_right + BATCH_GAP


def _annotation_x_for_batch(canvas, batch_num):
    """Return x aligned with the given batch group, or next open slot."""
    group = cv.find_node_by_id(canvas, "batch-{:02d}".format(batch_num))
    if group:
        return group["x"]
    x, _ = ly.next_position(canvas, "ANNOTATIONS", ly.TEXT_W, ly.TEXT_H)
    return x


def _annotation_y(offset=0):
    return ly.LANE_Y["ANNOTATIONS"] - ly.TEXT_H // 2 + offset


# ---------------------------------------------------------------------------
# Event builders
# ---------------------------------------------------------------------------

def build_batch_nodes(canvas, iter_dir, batch_num, prompt, gens,
                      contact_file=None, notes=None):
    """
    Build nodes for a generation batch.

    gens: list of dicts — {id: str, file: str (vault-relative), category: str, notes: str}
    contact_file: vault-relative path to the contact sheet, or None
    """
    batch_x = _next_batch_x(canvas)
    batch_y = ly.LANE_Y["TRANSITIONS"] - BATCH_H // 2

    group_id = "batch-{:02d}".format(batch_num)
    nodes = []
    edges = []

    # Group node
    nodes.append({
        "id":     group_id,
        "type":   "group",
        "label":  "Batch {:02d}".format(batch_num),
        "x":      batch_x,
        "y":      batch_y,
        "width":  BATCH_W,
        "height": BATCH_H,
    })

    # Gen file nodes (2-column grid inside the group)
    for i, gen in enumerate(gens):
        col = i % GEN_COLS
        row = i // GEN_COLS
        gx = batch_x + GEN_PAD + col * (GEN_W + GEN_PAD)
        gy = batch_y + GEN_PAD + row * (GEN_H + GEN_PAD)

        gen_id = "gen-{:02d}-{:02d}".format(batch_num, i + 1)
        gen_node = {
            "id":     gen_id,
            "type":   "file",
            "file":   gen.get("file", ""),
            "x":      gx,
            "y":      gy,
            "width":  GEN_W,
            "height": GEN_H,
        }
        color = _CATEGORY_COLOR.get(gen.get("category", ""), None)
        if color is not None:
            gen_node["color"] = color
        nodes.append(gen_node)

    # Prompt node (above the group)
    nodes.append({
        "id":     "prompt-{:02d}".format(batch_num),
        "type":   "text",
        "text":   "[AGENT]: PROMPT B{:02d}\n\n{}".format(batch_num, prompt),
        "color":  sc.COLOR_AGENT,
        "x":      batch_x,
        "y":      batch_y - PROMPT_H - 40,
        "width":  PROMPT_W,
        "height": PROMPT_H,
    })

    # Contact sheet (to the right of the group)
    if contact_file:
        nodes.append({
            "id":     "contact-{:02d}".format(batch_num),
            "type":   "file",
            "file":   contact_file,
            "x":      batch_x + BATCH_W + 80,
            "y":      batch_y,
            "width":  CONTACT_W,
            "height": CONTACT_H,
        })

    # Categorisation summary (below the group)
    if gens:
        cats = ["{}: {}".format(
            "gen-{:02d}-{:02d}".format(batch_num, i + 1),
            g.get("category", "?")
        ) for i, g in enumerate(gens)]
        cat_text = "[AGENT]: B{:02d} results\n{}".format(
            batch_num, "\n".join(cats))
        if notes:
            cat_text += "\n\n" + notes
        nodes.append({
            "id":     "cat-{:02d}".format(batch_num),
            "type":   "text",
            "text":   cat_text,
            "color":  sc.COLOR_AGENT,
            "x":      batch_x,
            "y":      batch_y + BATCH_H + 40,
            "width":  BATCH_W,
            "height": 120,
        })

    return nodes, edges


def build_surface_node(canvas, reason, batch_num=None):
    x = _annotation_x_for_batch(canvas, batch_num) if batch_num else (
        ly.next_position(canvas, "ANNOTATIONS", 360, 120)[0])
    node_id = cv.new_id()
    return [{
        "id":     node_id,
        "type":   "text",
        "text":   "[AGENT]: SURFACE\n\n{}".format(reason),
        "color":  sc.COLOR_AGENT,
        "x":      x,
        "y":      _annotation_y(),
        "width":  360,
        "height": 120,
    }], []


def build_adaptation_node(canvas, before, after, reason, batch_num=None):
    x = _annotation_x_for_batch(canvas, batch_num) if batch_num else (
        ly.next_position(canvas, "ANNOTATIONS", 420, 200)[0])
    node_id = cv.new_id()
    return [{
        "id":     node_id,
        "type":   "text",
        "text":   "[AGENT]: ADAPTATION\n\nWas: {}\nNow: {}\nWhy: {}".format(before, after, reason),
        "color":  sc.COLOR_AGENT,
        "x":      x,
        "y":      _annotation_y(-40),
        "width":  420,
        "height": 200,
    }], []


def build_refusal_node(canvas, batch_num, gen_id, response):
    group = cv.find_node_by_id(canvas, "batch-{:02d}".format(batch_num))
    x = (group["x"] + group.get("width", 0) // 2) if group else (
        ly.next_position(canvas, "ANNOTATIONS", 420, 200)[0])
    node_id = "refusal-{:02d}-{}".format(batch_num, gen_id)
    return [{
        "id":     node_id,
        "type":   "text",
        "text":   "[REFUSAL] B{:02d}/{}\n\n{}".format(batch_num, gen_id, response),
        "color":  sc.COLOR_ORANGE,
        "x":      x,
        "y":      _annotation_y(-40),
        "width":  420,
        "height": 200,
    }], []


def build_pick_annotation(canvas, gen_node_id):
    """Adds a USER PICK node below the chosen gen, edged from it."""
    gen_node = cv.find_node_by_id(canvas, gen_node_id)
    if not gen_node:
        return [], []
    pick_id = "pick-{}".format(gen_node_id)
    pick_node = {
        "id":     pick_id,
        "type":   "text",
        "text":   "USER PICK",
        "x":      gen_node["x"],
        "y":      gen_node["y"] + gen_node.get("height", GEN_H) + 20,
        "width":  160,
        "height": 60,
    }
    edge = {
        "id":       cv.new_id(),
        "fromNode": gen_node_id,
        "fromSide": "bottom",
        "toNode":   pick_id,
        "toSide":   "top",
        "label":    "picked",
    }
    return [pick_node], [edge]


def build_user_direction_node(canvas, note):
    x, y = ly.next_position(canvas, "ANNOTATIONS", 360, 120)
    return [{
        "id":     cv.new_id(),
        "type":   "text",
        "text":   "[USER]: DIRECTION\n\n{}".format(note),
        "color":  sc.COLOR_ANNOTATION,
        "x":      x,
        "y":      y,
        "width":  360,
        "height": 120,
    }], []


# ---------------------------------------------------------------------------
# Status node (init, finalize)
# ---------------------------------------------------------------------------

def make_status_node(active=True, start_time=None):
    ts = start_time or datetime.now().strftime("%Y-%m-%d %H:%M")
    text = "STATUS: {}\nStarted: {}".format("ACTIVE" if active else "COMPLETE", ts)
    node = {
        "id":     STATUS_ID,
        "type":   "text",
        "text":   text,
        "x":      STATUS_X,
        "y":      STATUS_Y,
        "width":  340,
        "height": 100,
    }
    if active:
        node["color"] = sc.COLOR_ORANGE
    return node


def finalize_status_node(canvas, end_time=None, cost_usd=None,
                          time_elapsed=None, summary=None):
    """Mutate the status node in-place to mark complete. Returns True if found."""
    ts = end_time or datetime.now().strftime("%Y-%m-%d %H:%M")
    for n in canvas["nodes"]:
        if n.get("id") == STATUS_ID:
            text = n.get("text", "STATUS: ACTIVE\n")
            text = text.replace("STATUS: ACTIVE", "STATUS: COMPLETE")
            text += "\nFinished: {}".format(ts)
            if cost_usd is not None:
                text += "\nCost: ${:.3f}".format(float(cost_usd))
            if time_elapsed:
                text += "\nElapsed: {}".format(time_elapsed)
            n["text"] = text
            n.pop("color", None)
            return True
    return False


def make_summary_node(canvas, cost_usd=None, time_elapsed=None, summary=None):
    """Summary node added at finalize, positioned after the last batch."""
    last_x = _next_batch_x(canvas)
    text = "[AGENT]: RUN SUMMARY\n"
    if cost_usd is not None:
        text += "\nCost: ${:.3f}".format(float(cost_usd))
    if time_elapsed:
        text += "\nElapsed: {}".format(time_elapsed)
    if summary:
        text += "\n\n{}".format(summary)
    return {
        "id":     "run-summary",
        "type":   "text",
        "text":   text,
        "color":  sc.COLOR_AGENT,
        "x":      last_x,
        "y":      ly.LANE_Y["ANNOTATIONS"] - ly.TEXT_H // 2,
        "width":  400,
        "height": 200,
    }
