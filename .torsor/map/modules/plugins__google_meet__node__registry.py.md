---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/node/registry.py

Symbols in `plugins/google_meet/node/registry.py`.

- L30 `_default_path()` (function)
- L34 `NodeRegistry` (class) — Simple file-backed registry. Not concurrent-safe across processes
- L38 `__init__(self, path: Optional[Path]=None)` (method)
- L43 `_load(self)` (method)
- L54 `_save(self, data: Dict[str, Any])` (method)
- L62 `get(self, name: str)` (method)
- L69 `add(self, name: str, url: str, token: str)` (method)
- L84 `remove(self, name: str)` (method)
- L92 `list_all(self)` (method)
- L99 `resolve(self, chrome_node: Optional[str])` (method) — Resolve a node name to its entry.
