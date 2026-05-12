#!/usr/bin/env python3
"""
/comic-trace adopt <existing-canvas-path> --as-slug <slug>

Register an existing hand-built canvas under skill management.
Does NOT modify the canvas — registry write only.
Run from vault root.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import canvas as cv
from lib import registry as reg
from lib import schema as sc


def main():
    parser = argparse.ArgumentParser(
        description="Adopt an existing canvas into the comic-trace registry.")
    parser.add_argument("canvas_path", help="Path to existing .canvas file")
    parser.add_argument("--as-slug", required=True, dest="slug",
                        help="Slug to register this canvas under")
    args = parser.parse_args()

    if not os.path.exists(args.canvas_path):
        print("Error: file not found: {}".format(args.canvas_path))
        sys.exit(1)

    try:
        c = cv.load(args.canvas_path)
    except Exception as e:
        print("Error: failed to parse canvas JSON: {}".format(e))
        sys.exit(1)

    # Lenient validation — hand-built canvases may deviate from conventions
    issues = sc.validate(c, mode='lenient')
    if issues:
        print("Validation notes (adopting anyway — lenient mode):")
        for issue in issues:
            print("  - " + issue)

    existing = reg.get_canvas_path(args.slug)
    if existing:
        print("Note: slug '{}' already registered -> {}".format(args.slug, existing))
        print("Overwriting with: {}".format(args.canvas_path))

    reg.register_slug(args.slug, args.canvas_path)

    n_nodes = len(c.get("nodes", []))
    n_edges = len(c.get("edges", []))
    print("Adopted:    {}".format(args.canvas_path))
    print("Slug:       {}".format(args.slug))
    print("Canvas has: {} nodes, {} edges".format(n_nodes, n_edges))
    print("Subsequent capture/annotate/link-sub will target this canvas.")


if __name__ == "__main__":
    main()
