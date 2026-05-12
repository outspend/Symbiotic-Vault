"""Predecessor inference from file frontmatter and filename proximity."""
import re
from pathlib import Path


def read_frontmatter(file_path):
    """Parse YAML frontmatter from a markdown file. Returns {} if absent."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (FileNotFoundError, PermissionError):
        return {}

    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}

    fm = {}
    for line in m.group(1).splitlines():
        # Only top-level keys (no leading space)
        if ':' in line and not line.startswith(' '):
            key, _, val = line.partition(':')
            fm[key.strip()] = val.strip()
    return fm


def _wikilink_path(value):
    """Extract path from [[path]] or [[path|alias]]; pass through plain strings."""
    m = re.match(r'\[\[([^\]|]+)', value.strip())
    if m:
        return m.group(1).strip()
    return value.strip()


def _normalize_md(ref):
    """Append .md extension if the path has no extension."""
    p = Path(ref)
    if p.suffix == '':
        return str(p) + '.md'
    return str(p)


def infer_predecessor(canvas, file_path, source_type):
    """
    Return node id of the inferred predecessor, or None.

    Priority:
      1. responds_to frontmatter (inbox files)
      2. source frontmatter (reflection/hold files)
      3. date match: hold → journal of same date (fallback)
    """
    from .canvas import find_node_by_file, find_node_by_slug

    fm = read_frontmatter(file_path)

    # 1. responds_to
    if 'responds_to' in fm:
        ref = _wikilink_path(fm['responds_to'])
        candidate = _normalize_md(ref)
        node = find_node_by_file(canvas, candidate)
        if node:
            return node['id']
        # fallback: stem slug match
        node = find_node_by_slug(canvas, Path(ref).name)
        if node:
            return node['id']

    # 2. source
    if 'source' in fm:
        ref = _wikilink_path(fm['source'])
        candidate = _normalize_md(ref)
        node = find_node_by_file(canvas, candidate)
        if node:
            return node['id']
        node = find_node_by_slug(canvas, Path(ref).name)
        if node:
            return node['id']

    # 3. date proximity for hold → journal
    if source_type == 'hold':
        date = fm.get('date', '')
        if date:
            for n in canvas['nodes']:
                if (n.get('type') == 'file'
                        and '_journal/' in n.get('file', '')
                        and date in n.get('file', '')):
                    return n['id']

    return None
