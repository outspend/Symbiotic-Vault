"""Canvas schema constants and validation."""

# Obsidian canvas color values (numbers as strings)
# 1=red, 2=orange, 3=yellow, 4=green, 5=cyan, 6=purple in Obsidian's palette.
# Convention in this vault (per prototype):
COLOR_CYAN = None        # omit color field → default (cyan for vault files)
COLOR_ORANGE = "2"       # external / to import / process-alert
COLOR_ANNOTATION = "1"   # annotation nodes (user's legend calls these "purple")
COLOR_AGENT = "1"        # agent annotations get same color + [AGENT]: prefix
COLOR_ITERATION = "6"    # iteration artifact / in-progress marker

VALID_NODE_TYPES = {"file", "text", "link", "group"}


def validate(canvas, mode='strict'):
    """Return list of issue strings. Empty list = valid."""
    issues = []

    if "nodes" not in canvas:
        issues.append("Missing 'nodes' key")
        return issues
    if "edges" not in canvas:
        issues.append("Missing 'edges' key")
        return issues

    node_ids = {n.get("id") for n in canvas["nodes"]}

    for n in canvas["nodes"]:
        if not n.get("id"):
            issues.append("Node missing 'id': {}".format(n))
        if n.get("type") not in VALID_NODE_TYPES:
            issues.append("Node {} has unknown type: {}".format(n.get("id"), n.get("type")))
        if "x" not in n or "y" not in n:
            issues.append("Node {} missing x/y".format(n.get("id")))

    if mode == 'strict':
        for e in canvas.get("edges", []):
            if not e.get("id"):
                issues.append("Edge missing 'id': {}".format(e))
            if e.get("fromNode") not in node_ids:
                issues.append("Edge {} unknown fromNode: {}".format(
                    e.get("id"), e.get("fromNode")))
            if e.get("toNode") not in node_ids:
                issues.append("Edge {} unknown toNode: {}".format(
                    e.get("id"), e.get("toNode")))

    return issues
