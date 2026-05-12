#!/usr/bin/env python3
"""
/comic-trace capture <type> <source> [--predecessor <id-or-slug>] [--lane <override>] [--comic <slug>]

Add an artifact node to a comic provenance canvas.
Run from vault root.
"""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import canvas as cv
from lib import layout as ly
from lib import resolve as rs
from lib import registry as reg
from lib import schema as sc

# type -> (lane, color, width, height)
TYPE_CONFIG = {
    "journal":           ("ARTIFACTS",    sc.COLOR_CYAN,       ly.FILE_W,  ly.FILE_H),
    "hold":              ("ARTIFACTS",    sc.COLOR_CYAN,       ly.FILE_W,  ly.FILE_H),
    "inbox":             ("ARTIFACTS",    sc.COLOR_CYAN,       ly.FILE_W,  ly.FILE_H),
    "image":             ("ARTIFACTS",    sc.COLOR_CYAN,       300,        400),
    "chatgpt-script":    ("TRANSITIONS",  sc.COLOR_ORANGE,     400,        180),
    "chatgpt-image":     ("TRANSITIONS",  sc.COLOR_ORANGE,     400,        180),
    "image-chase-sub":   ("ARTIFACTS",    sc.COLOR_CYAN,       300,        300),
    "external-feedback": ("ANNOTATIONS",  sc.COLOR_ANNOTATION, 350,        200),
    "wish":              ("ANNOTATIONS",  sc.COLOR_ANNOTATION, 300,        120),
    "process-alert":     ("ANNOTATIONS",  sc.COLOR_ORANGE,     280,        120),
    "idea":              ("ANNOTATIONS",  sc.COLOR_ANNOTATION, 300,        120),
}

# Types that become file nodes (vs. text nodes)
FILE_NODE_TYPES = {"journal", "hold", "inbox", "image", "image-chase-sub"}

# Types that support frontmatter-based predecessor inference
INFER_TYPES = {"journal", "hold", "inbox"}

# Text prefixes for non-file annotation types
TEXT_PREFIXES = {
    "process-alert":    "STAGE/PROCESS ALERT\n\n",
    "wish":             "WISH\n\n",
    "idea":             "IDEA\n\n",
    "external-feedback": "",  # prepended with FROM <name> below
}


def resolve_comic(slug_arg):
    slugs = reg.list_slugs()
    if slug_arg:
        if slug_arg not in slugs:
            print("Error: slug '{}' not registered. Run init first.".format(slug_arg))
            sys.exit(1)
        return slug_arg, slugs[slug_arg]
    if len(slugs) == 1:
        return list(slugs.items())[0]
    if not slugs:
        print("Error: no comics registered. Run /comic-trace init first.")
        sys.exit(1)
    print("Multiple comics registered: {}".format(list(slugs.keys())))
    print("Use --comic <slug> to specify which one.")
    sys.exit(1)


def make_node_id(source_type, source):
    """Predictable, human-readable node id: <type>-<filename-stem>."""
    stem = Path(source).stem.replace(" ", "-")
    return "{}-{}".format(source_type, stem)


def main():
    parser = argparse.ArgumentParser(
        description="Capture an artifact onto a comic-trace canvas.")
    parser.add_argument("type",   help="Artifact type (journal, hold, inbox, image, ...)")
    parser.add_argument("source", help="Vault-relative path or descriptive text")
    parser.add_argument("--predecessor", default=None,
                        help="Node id or slug of predecessor")
    parser.add_argument("--lane", default=None,
                        help="Override lane (ARTIFACTS, TRANSITIONS, ANNOTATIONS)")
    parser.add_argument("--comic", default=None, help="Comic slug")
    parser.add_argument("--from", dest="from_name", default=None,
                        help="Attribution name (for external-feedback)")
    args = parser.parse_args()

    source_type = args.type
    if source_type not in TYPE_CONFIG:
        print("Unknown type: {}".format(source_type))
        print("Valid types: {}".format(", ".join(sorted(TYPE_CONFIG))))
        sys.exit(1)

    slug, canvas_path = resolve_comic(args.comic)
    c = cv.load(canvas_path)

    lane, color, w, h = TYPE_CONFIG[source_type]
    if args.lane:
        if args.lane not in ly.LANE_Y:
            print("Unknown lane: {}. Valid: {}".format(args.lane, list(ly.LANE_Y.keys())))
            sys.exit(1)
        lane = args.lane

    # Generate collision-safe node id
    node_id = make_node_id(source_type, args.source)
    existing_ids = {n["id"] for n in c["nodes"]}
    base_id = node_id
    counter = 1
    while node_id in existing_ids:
        node_id = "{}-{}".format(base_id, counter)
        counter += 1

    # Position
    x, y = ly.next_position(c, lane, w, h)

    # Build node
    if source_type in FILE_NODE_TYPES:
        node = {
            "id":     node_id,
            "type":   "file",
            "file":   args.source,
            "x":      x,
            "y":      y,
            "width":  w,
            "height": h,
        }
    else:
        text = args.source
        prefix = TEXT_PREFIXES.get(source_type, "")
        if source_type == "external-feedback" and args.from_name:
            prefix = "FROM {}\n\n".format(args.from_name.upper())
        text = prefix + text
        node = {
            "id":     node_id,
            "type":   "text",
            "text":   text,
            "x":      x,
            "y":      y,
            "width":  w,
            "height": h,
        }

    if color is not None:
        node["color"] = color

    cv.add_node(c, node)

    # Predecessor resolution
    predecessor_id = args.predecessor
    if predecessor_id is None and source_type in INFER_TYPES:
        if os.path.exists(args.source):
            predecessor_id = rs.infer_predecessor(c, args.source, source_type)
            if predecessor_id:
                print("Inferred predecessor: {}".format(predecessor_id))
            else:
                print("No predecessor inferred — node will be a root.")
    elif predecessor_id is not None:
        pred_node = (cv.find_node_by_id(c, predecessor_id)
                     or cv.find_node_by_slug(c, predecessor_id))
        if pred_node:
            predecessor_id = pred_node["id"]
        else:
            print("Warning: predecessor '{}' not found; edge skipped.".format(predecessor_id))
            predecessor_id = None

    if predecessor_id:
        edge = {
            "id":       cv.new_id(),
            "fromNode": predecessor_id,
            "fromSide": "right",
            "toNode":   node_id,
            "toSide":   "left",
        }
        cv.add_edge(c, edge)

    issues = sc.validate(c, mode='strict')
    if issues:
        print("Validation warnings:")
        for issue in issues:
            print("  - " + issue)

    cv.save(c, canvas_path)

    print("Captured: [{}] {} -> {}".format(source_type, args.source, node_id))
    if predecessor_id:
        print("  Edge: {} -> {}".format(predecessor_id, node_id))


if __name__ == "__main__":
    main()
