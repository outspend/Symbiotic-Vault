"""Slug → canvas path registry (stored in registry.yaml as simple key: value pairs).

PyYAML is not required; uses a stdlib-only line parser.
"""
import os

REGISTRY_RELPATH = "_system/_tools/comic-trace/registry.yaml"


def _registry_path(vault_root="."):
    return os.path.join(vault_root, REGISTRY_RELPATH)


def load_registry(vault_root="."):
    path = _registry_path(vault_root)
    result = {}
    if not os.path.exists(path):
        return result
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                k, _, v = line.partition(':')
                result[k.strip()] = v.strip()
    return result


def save_registry(registry, vault_root="."):
    path = _registry_path(vault_root)
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("# comic-trace registry: slug -> canvas path\n")
        for k, v in sorted(registry.items()):
            f.write("{}: {}\n".format(k, v))


def get_canvas_path(slug, vault_root="."):
    return load_registry(vault_root).get(slug)


def register_slug(slug, canvas_path, vault_root="."):
    reg = load_registry(vault_root)
    reg[slug] = canvas_path
    save_registry(reg, vault_root)


def list_slugs(vault_root="."):
    return load_registry(vault_root)
