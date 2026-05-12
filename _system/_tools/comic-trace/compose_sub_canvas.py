#!/usr/bin/env python3
"""
/comic-trace compose-sub-canvas --mode {init|append|finalize} <iter-dir> [event params]

Maintains a live sub-canvas at <iter-dir>/run.canvas that grows event-by-event
like a chat history. Used by image-chase (via shell-out) to record a fix run.

Run from vault root.

MODES
-----
  init      -- create the sub-canvas with lanes, request blast, refs, status node
  append    -- append nodes/edges for one event (batch, surface, adaptation,
               refusal, pick, user-direction)
  finalize  -- add summary node; flip status to complete

BATCH FILE
----------
For --event batch, comic-trace reads <iter-dir>/gen-batch-NN/batch.json.
Expected keys:
  {
    "batch_num": 1,
    "prompt": "...",
    "gens": [{"id":"01","file":"gen-batch-01/gen-01-01.png","category":"pass","notes":"..."}],
    "contact": "gen-batch-01/contact-01.png",   (optional)
    "notes": "..."                               (optional)
  }
All 'file' paths inside batch.json are relative to the iteration directory.
compose-sub-canvas converts them to vault-relative paths before writing to the canvas.
"""
import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lib import canvas as cv
from lib import layout as ly
from lib import schema as sc
from lib import events as ev


def _canvas_path(iter_dir):
    return os.path.join(iter_dir, "run.canvas")


def _load_or_abort(iter_dir):
    path = _canvas_path(iter_dir)
    if not os.path.exists(path):
        print("Error: sub-canvas not found at {}".format(path))
        print("Run --mode init first.")
        sys.exit(1)
    return cv.load(path), path


def _save_validated(canvas, canvas_path):
    issues = sc.validate(canvas, mode='strict')
    if issues:
        print("Validation warnings:")
        for i in issues:
            print("  - " + i)
    cv.save(canvas, canvas_path)


def _iter_relative(iter_dir, rel_path):
    """Convert a path relative to iter_dir into a vault-relative path."""
    return str(Path(iter_dir) / rel_path)


def _load_batch_json(iter_dir, batch_num):
    batch_dir = os.path.join(iter_dir, "gen-batch-{:02d}".format(batch_num))
    path = os.path.join(batch_dir, "batch.json")
    if not os.path.exists(path):
        print("Error: batch file not found: {}".format(path))
        sys.exit(1)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Modes
# ---------------------------------------------------------------------------

def mode_init(iter_dir, request_blast=None, refs=None):
    canvas_path = _canvas_path(iter_dir)
    if os.path.exists(canvas_path):
        print("Sub-canvas already exists: {}".format(canvas_path))
        print("Delete it first to reinitialise.")
        sys.exit(1)

    c = cv.empty_canvas()

    # Lane labels + legend (same as main canvas)
    for node in ly.lane_label_nodes():
        cv.add_node(c, node)
    cv.add_node(c, ly.legend_node())

    # Request blast — file node if request-blast.md exists, else skip
    blast_path = request_blast or os.path.join(iter_dir, "request-blast.md")
    if os.path.exists(blast_path):
        cv.add_node(c, {
            "id":     "request-blast",
            "type":   "file",
            "file":   blast_path,
            "x":      ly.LEGEND_X,
            "y":      ly.LEGEND_Y + ly.LEGEND_H + 60,
            "width":  ly.LEGEND_W,
            "height": 300,
        })

    # Ref nodes in ARTIFACTS lane
    for i, ref in enumerate(refs or []):
        x = ly.X_START + i * (ly.FILE_W + 120)
        cv.add_node(c, {
            "id":     "ref-{:02d}".format(i + 1),
            "type":   "file",
            "file":   ref,
            "x":      x,
            "y":      ly.LANE_Y["ARTIFACTS"] - ly.FILE_H // 2,
            "width":  ly.FILE_W,
            "height": ly.FILE_H,
        })

    # Status node
    cv.add_node(c, ev.make_status_node(
        active=True,
        start_time=datetime.now().strftime("%Y-%m-%d %H:%M")
    ))

    _save_validated(c, canvas_path)
    print("Init:  {}".format(canvas_path))
    print("Lanes: ARTIFACTS (refs), TRANSITIONS (batches), ANNOTATIONS (events)")


def mode_append(iter_dir, event_type, args):
    c, canvas_path = _load_or_abort(iter_dir)

    if event_type == "batch":
        if args.batch_num is None:
            print("Error: --batch-num required for --event batch")
            sys.exit(1)
        data = _load_batch_json(iter_dir, args.batch_num)
        # Convert gen file paths to vault-relative
        gens = []
        for g in data.get("gens", []):
            gens.append({
                "id":       g.get("id", ""),
                "file":     _iter_relative(iter_dir, g["file"]),
                "category": g.get("category", ""),
                "notes":    g.get("notes", ""),
            })
        contact = data.get("contact")
        if contact:
            contact = _iter_relative(iter_dir, contact)
        nodes, edges = ev.build_batch_nodes(
            c, iter_dir,
            batch_num=args.batch_num,
            prompt=data.get("prompt", ""),
            gens=gens,
            contact_file=contact,
            notes=data.get("notes"),
        )

    elif event_type == "surface":
        if not args.reason:
            print("Error: --reason required for --event surface")
            sys.exit(1)
        nodes, edges = ev.build_surface_node(c, args.reason, batch_num=args.batch_num)

    elif event_type == "adaptation":
        for flag in ("--before", "--after", "--reason"):
            val = getattr(args, flag.lstrip("-").replace("-", "_"), None)
            if not val:
                print("Error: {} required for --event adaptation".format(flag))
                sys.exit(1)
        nodes, edges = ev.build_adaptation_node(
            c,
            before=args.before,
            after=args.after,
            reason=args.reason,
            batch_num=args.batch_num,
        )

    elif event_type == "refusal":
        if not (args.batch_num and args.gen_id and args.response):
            print("Error: --batch-num, --gen-id, --response required for --event refusal")
            sys.exit(1)
        nodes, edges = ev.build_refusal_node(
            c, args.batch_num, args.gen_id, args.response)

    elif event_type == "pick":
        if not args.gen_node_id:
            print("Error: --gen-node-id required for --event pick")
            sys.exit(1)
        nodes, edges = ev.build_pick_annotation(c, args.gen_node_id)
        if not nodes and not edges:
            print("Warning: gen node '{}' not found; pick not recorded.".format(
                args.gen_node_id))

    elif event_type == "user-direction":
        if not args.note:
            print("Error: --note required for --event user-direction")
            sys.exit(1)
        nodes, edges = ev.build_user_direction_node(c, args.note)

    else:
        print("Unknown event type: {}".format(event_type))
        sys.exit(1)

    for node in nodes:
        cv.add_node(c, node)
    for edge in edges:
        cv.add_edge(c, edge)

    _save_validated(c, canvas_path)
    print("Appended [{}]: {} nodes, {} edges".format(event_type, len(nodes), len(edges)))


def mode_finalize(iter_dir, cost_usd=None, time_elapsed=None, summary=None):
    c, canvas_path = _load_or_abort(iter_dir)

    # Update status node
    found = ev.finalize_status_node(
        c,
        end_time=datetime.now().strftime("%Y-%m-%d %H:%M"),
        cost_usd=cost_usd,
        time_elapsed=time_elapsed,
        summary=summary,
    )
    if not found:
        print("Warning: status node not found; adding fresh.")
        cv.add_node(c, ev.make_status_node(active=False))

    # Summary node
    summary_node = ev.make_summary_node(
        c, cost_usd=cost_usd, time_elapsed=time_elapsed, summary=summary)
    cv.add_node(c, summary_node)

    _save_validated(c, canvas_path)
    print("Finalized: {}".format(canvas_path))
    if cost_usd is not None:
        print("  Cost: ${:.3f}".format(float(cost_usd)))
    if time_elapsed:
        print("  Elapsed: {}".format(time_elapsed))


def mode_mark_stale(iter_dir):
    """Recovery: mark a stuck-active sub-canvas as stale."""
    c, canvas_path = _load_or_abort(iter_dir)
    for n in canvas["nodes"]:
        if n.get("id") == ev.STATUS_ID:
            n["text"] = n.get("text", "").replace("STATUS: ACTIVE", "STATUS: STALE")
            n["color"] = "3"  # yellow = warning
            break
    cv.save(c, canvas_path)
    print("Marked stale: {}".format(canvas_path))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Maintain a live sub-canvas for an image-chase run.")
    parser.add_argument("--mode", required=True,
                        choices=["init", "append", "finalize", "mark-stale"])
    parser.add_argument("iter_dir", help="Vault-relative path to the iteration directory")

    # append options
    parser.add_argument("--event",
                        choices=["batch", "surface", "adaptation", "refusal",
                                 "pick", "user-direction"])
    parser.add_argument("--batch-num", type=int, default=None)
    parser.add_argument("--reason", default=None)
    parser.add_argument("--before", default=None)
    parser.add_argument("--after",  default=None)
    parser.add_argument("--gen-id", dest="gen_id", default=None)
    parser.add_argument("--response", default=None)
    parser.add_argument("--gen-node-id", dest="gen_node_id", default=None)
    parser.add_argument("--note", default=None)

    # init options
    parser.add_argument("--request-blast", dest="request_blast", default=None)
    parser.add_argument("--refs", nargs="*", default=None)

    # finalize options
    parser.add_argument("--cost-usd", dest="cost_usd", default=None)
    parser.add_argument("--time-elapsed", dest="time_elapsed", default=None)
    parser.add_argument("--summary", default=None)

    args = parser.parse_args()

    if args.mode == "init":
        mode_init(args.iter_dir, args.request_blast, args.refs)

    elif args.mode == "append":
        if not args.event:
            print("Error: --event required for --mode append")
            sys.exit(1)
        mode_append(args.iter_dir, args.event, args)

    elif args.mode == "finalize":
        mode_finalize(args.iter_dir, args.cost_usd, args.time_elapsed, args.summary)

    elif args.mode == "mark-stale":
        mode_mark_stale(args.iter_dir)


if __name__ == "__main__":
    main()
