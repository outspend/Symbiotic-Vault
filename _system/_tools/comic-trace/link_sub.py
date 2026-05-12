#!/usr/bin/env python3
"""
/comic-trace link-sub <sub-canvas-path> [--comic <slug>] [--predecessor <node-id>]
                       [--label <edge-label>] --status active|complete

Attaches an image-chase sub-canvas as a file node on the main provenance canvas.
Call twice per run:
  1. At run start:  --status active    (node appears orange, "running since HH:MM")
  2. At run end:    --status complete  (node reverts to default, gets completion time)

The link node ID is derived from the iteration-directory name (stable across both calls).
Run from vault root.
"""
import argparse
import os
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import canvas as cv
from lib import layout as ly
from lib import registry as reg
from lib import schema as sc


def _link_node_id(sub_canvas_path):
    """Stable ID from the iteration-directory stem (the timestamp folder)."""
    return "sub-link-{}".format(Path(sub_canvas_path).parent.name)


def _resolve_comic(slug_arg):
    slugs = reg.list_slugs()
    if slug_arg:
        if slug_arg not in slugs:
            print("Error: slug '{}' not registered.".format(slug_arg))
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


def main():
    parser = argparse.ArgumentParser(
        description="Link a sub-canvas file node onto the main provenance canvas.")
    parser.add_argument("sub_canvas_path",
                        help="Vault-relative path to the sub-canvas (run.canvas)")
    parser.add_argument("--comic", default=None, help="Comic slug")
    parser.add_argument("--predecessor", default=None,
                        help="Node id or slug on the main canvas to edge from")
    parser.add_argument("--label", default="iterated",
                        help="Edge label (default: iterated)")
    parser.add_argument("--status", required=True, choices=["active", "complete"],
                        help="active = run in progress; complete = run finished")
    args = parser.parse_args()

    slug, canvas_path = _resolve_comic(args.comic)
    c = cv.load(canvas_path)

    node_id = _link_node_id(args.sub_canvas_path)
    ts = datetime.now().strftime("%H:%M")
    existing = cv.find_node_by_id(c, node_id)

    if args.status == "active":
        if existing:
            print("Warning: link node '{}' already exists; skipping create.".format(node_id))
        else:
            x, y = ly.next_position(c, "ARTIFACTS", ly.FILE_W, ly.FILE_H)
            node = {
                "id":     node_id,
                "type":   "file",
                "file":   args.sub_canvas_path,
                "color":  "2",   # orange = in progress
                "x":      x,
                "y":      y,
                "width":  ly.FILE_W,
                "height": ly.FILE_H,
            }
            cv.add_node(c, node)

            # Label node (text overlay showing run start time)
            label_id = node_id + "-label"
            cv.add_node(c, {
                "id":     label_id,
                "type":   "text",
                "text":   "fix run\nrunning since {}".format(ts),
                "color":  "2",
                "x":      x,
                "y":      y - 80,
                "width":  ly.FILE_W,
                "height": 60,
            })

            # Edge from predecessor
            if args.predecessor:
                pred = (cv.find_node_by_id(c, args.predecessor)
                        or cv.find_node_by_slug(c, args.predecessor))
                if pred:
                    cv.add_edge(c, {
                        "id":       cv.new_id(),
                        "fromNode": pred["id"],
                        "fromSide": "right",
                        "toNode":   node_id,
                        "toSide":   "left",
                        "label":    args.label,
                    })
                else:
                    print("Warning: predecessor '{}' not found; edge skipped.".format(
                        args.predecessor))

    elif args.status == "complete":
        if not existing:
            print("Warning: link node '{}' not found; creating completed node.".format(node_id))
            x, y = ly.next_position(c, "ARTIFACTS", ly.FILE_W, ly.FILE_H)
            cv.add_node(c, {
                "id":     node_id,
                "type":   "file",
                "file":   args.sub_canvas_path,
                "x":      x,
                "y":      y,
                "width":  ly.FILE_W,
                "height": ly.FILE_H,
            })
        else:
            # Remove orange color
            existing.pop("color", None)

        # Update or replace the label node
        label_id = node_id + "-label"
        label_node = cv.find_node_by_id(c, label_id)
        if label_node:
            label_node["text"] = "fix run\ncompleted {}".format(ts)
            label_node.pop("color", None)
        else:
            # Find position of main node to place label above it
            link_node = cv.find_node_by_id(c, node_id)
            if link_node:
                cv.add_node(c, {
                    "id":     label_id,
                    "type":   "text",
                    "text":   "fix run\ncompleted {}".format(ts),
                    "x":      link_node["x"],
                    "y":      link_node["y"] - 80,
                    "width":  ly.FILE_W,
                    "height": 60,
                })

    issues = sc.validate(c, mode='strict')
    if issues:
        print("Validation warnings:")
        for i in issues:
            print("  - " + i)

    cv.save(c, canvas_path)
    print("link-sub [{}]: {} -> {}".format(args.status, args.sub_canvas_path, canvas_path))


if __name__ == "__main__":
    main()
