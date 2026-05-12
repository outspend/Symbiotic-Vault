#!/usr/bin/env python3
"""
/comic-trace init <slug> [--from-prototype <path>]

Creates a new comic provenance canvas with lane labels and legend.
Registers the slug → canvas path in registry.yaml.
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


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new comic-trace provenance canvas.")
    parser.add_argument("slug", help="Comic slug, e.g. scroggins-manson")
    parser.add_argument(
        "--from-prototype", default=None,
        help="Path to prototype canvas to copy legend text from (optional)")
    args = parser.parse_args()

    slug = args.slug
    canvas_path = "_trace/{}-provenance.canvas".format(slug)

    if os.path.exists(canvas_path):
        print("Canvas already exists: {}".format(canvas_path))
        print("To register an existing canvas use: adopt <path> --as-slug <slug>")
        sys.exit(1)

    c = cv.empty_canvas()

    for node in ly.lane_label_nodes():
        cv.add_node(c, node)

    cv.add_node(c, ly.legend_node())

    cv.save(c, canvas_path)

    issues = sc.validate(c, mode='strict')
    if issues:
        print("Validation warnings:")
        for issue in issues:
            print("  - " + issue)

    reg.register_slug(slug, canvas_path)

    print("Created:    {}".format(canvas_path))
    print("Registered: '{}' -> {}".format(slug, canvas_path))


if __name__ == "__main__":
    main()
