"""Canvas JSON read/write utilities. Atomic writes prevent corruption."""
import json
import os
import secrets
import tempfile
from pathlib import Path


def new_id():
    """16-char hex id matching Obsidian's format."""
    return secrets.token_hex(8)


def empty_canvas():
    return {"nodes": [], "edges": []}


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save(canvas, path):
    """Atomic write: temp file then rename, never leaves a corrupt canvas."""
    target = Path(path).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(target.parent), suffix='.tmp')
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(canvas, f, indent='\t', ensure_ascii=False)
        os.replace(tmp, str(target))
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def add_node(canvas, node):
    canvas["nodes"].append(node)


def add_edge(canvas, edge):
    canvas["edges"].append(edge)


def find_node_by_id(canvas, node_id):
    for n in canvas["nodes"]:
        if n.get("id") == node_id:
            return n
    return None


def find_node_by_file(canvas, file_path):
    """Find a file-type node matching the given vault-relative path."""
    target = str(Path(file_path))
    for n in canvas["nodes"]:
        if n.get("type") == "file":
            stored = str(Path(n.get("file", "")))
            if stored == target:
                return n
    return None


def find_node_by_slug(canvas, slug):
    """Find a node by exact id, id prefix, or filename stem / path fragment."""
    # 1. exact id
    for n in canvas["nodes"]:
        if n.get("id") == slug:
            return n
    # 2. id prefix
    for n in canvas["nodes"]:
        if n.get("id", "").startswith(slug):
            return n
    # 3. file nodes: stem or path substring
    for n in canvas["nodes"]:
        if n.get("type") == "file":
            fp = n.get("file", "")
            if Path(fp).stem == slug or slug in fp:
                return n
    return None
