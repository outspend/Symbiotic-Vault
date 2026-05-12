#!/usr/bin/env python3
"""
/comic-trace annotate <target-id-or-slug> [--by user|agent] [--type observation|wish|alert|context]
                      [--text "..."] [--comic <slug>]

Add an annotation text node edged to the target node.
Content comes from --text or stdin (pipe or interactive).
Run from vault root.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import canvas as cv
from lib import layout as ly
from lib import registry as reg
from lib import schema as sc


def resolve_comic(slug_arg):
    slugs = reg.list_slugs()
    if slug_arg:
        if slug_arg not in slugs:
            print("Error: slug '{}' not registered.".format(slug_arg))
            sys.exit(1)
        return slug_arg, slugs[slug_arg]
    if len(slugs) == 1:
        return list(slugs.items())[0]
    if not slugs:
        print("Error: no comics registered.")
        sys.exit(1)
    print("Multiple comics registered. Use --comic <slug>.")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Add an annotation node to a comic-trace canvas.")
    parser.add_argument("target", help="Node id or slug to annotate")
    parser.add_argument("--by",   choices=["user", "agent"], default="user")
    parser.add_argument("--type", dest="annot_type",
                        choices=["observation", "wish", "alert", "context", "modifier"],
                        default="observation")
    parser.add_argument("--text", default=None,
                        help="Annotation text (or pipe/type via stdin)")
    parser.add_argument("--comic", default=None)
    args = parser.parse_args()

    slug, canvas_path = resolve_comic(args.comic)
    c = cv.load(canvas_path)

    target_node = (cv.find_node_by_id(c, args.target)
                   or cv.find_node_by_slug(c, args.target))
    if not target_node:
        print("Error: target node '{}' not found.".format(args.target))
        sys.exit(1)

    # Collect annotation text
    text = args.text
    if text is None:
        if not sys.stdin.isatty():
            text = sys.stdin.read().strip()
        else:
            print("Enter annotation text (Ctrl-D to finish):")
            try:
                text = sys.stdin.read().strip()
            except EOFError:
                text = ""

    if not text:
        print("Error: annotation text is empty.")
        sys.exit(1)

    is_modifier = args.annot_type == "modifier"

    # Prefixes — modifier gets explicit MODIFIER (CRITIQUE) marker;
    # regular agent annotations get the [AGENT]: belt-and-suspenders.
    if is_modifier:
        if args.by == "user" and "MODIFIER" not in text[:60]:
            text = "USER MODIFIER (CRITIQUE)\n\n" + text
        elif args.by == "agent" and "MODIFIER" not in text[:60] \
                and not text.startswith("[AGENT]"):
            text = "[AGENT] MODIFIER\n\n" + text
    elif args.by == "agent" and not text.startswith("[AGENT]:"):
        text = "[AGENT]: " + text

    node_id = cv.new_id()
    node_h = max(ly.TEXT_H, 40 + len(text) // 4)

    if is_modifier:
        # Modifier sits directly below its target, sized to match.
        tx = target_node.get("x", 0)
        ty = target_node.get("y", 0)
        th = target_node.get("height", ly.TEXT_H)
        tw = target_node.get("width", ly.TEXT_W)
        width = tw
        x = tx
        y = ty + th + 60
    else:
        # Annotation goes in the ANNOTATIONS lane, aligned with target's x.
        width = ly.TEXT_W
        tx = target_node.get("x", 0)
        y = ly.LANE_Y["ANNOTATIONS"] - node_h // 2
        x = tx
        occupied_xs = {
            n.get("x", 0)
            for n in c["nodes"]
            if n.get("id", "").startswith(("annot", node_id[:4]))
            and abs(n.get("y", 0) - y) < 200
        }
        while x in occupied_xs:
            x += ly.TEXT_W + ly.X_GAP

    node = {
        "id":     node_id,
        "type":   "text",
        "text":   text,
        "x":      x,
        "y":      y,
        "width":  width,
        "height": node_h,
    }
    # User-authored modifiers stay uncolored (matches the prototype's hand-built critique).
    # Agent modifiers and all other annotations use COLOR_ANNOTATION.
    if not (is_modifier and args.by == "user"):
        node["color"] = sc.COLOR_ANNOTATION
    cv.add_node(c, node)

    if is_modifier:
        # Edge points FROM modifier TO target (the modifier acts on the target).
        edge = {
            "id":       cv.new_id(),
            "fromNode": node_id,
            "fromSide": "top",
            "toNode":   target_node["id"],
            "toSide":   "bottom",
        }
    else:
        # Annotation derived from target: arrow points from target to annotation.
        edge = {
            "id":       cv.new_id(),
            "fromNode": target_node["id"],
            "fromSide": "top",
            "toNode":   node_id,
            "toSide":   "bottom",
        }
    cv.add_edge(c, edge)

    issues = sc.validate(c)
    if issues:
        print("Validation warnings:")
        for issue in issues:
            print("  - " + issue)

    cv.save(c, canvas_path)
    print("Annotated: {} -> {} (by={}, type={})".format(
        target_node["id"], node_id, args.by, args.annot_type))


if __name__ == "__main__":
    main()
