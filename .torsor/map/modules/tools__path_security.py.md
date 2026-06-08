---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/path_security.py

Symbols in `tools/path_security.py`.

- L15 `validate_within_dir(path: Path, root: Path)` (function) — Ensure *path* resolves to a location within *root*.
- L37 `has_traversal_component(path_str: str)` (function) — Return True if *path_str* contains ``..`` traversal components.
