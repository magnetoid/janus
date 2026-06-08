---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/workspace.py

Symbols in `agent/lsp/workspace.py`.

- L33 `normalize_path(path: str)` (function) — Normalize a path for use as a stable map key.
- L44 `find_git_worktree(start: str)` (function) — Walk up from ``start`` looking for a ``.git`` entry (file or dir).
- L91 `is_inside_workspace(path: str, workspace_root: str)` (function) — Return True iff ``path`` is inside (or equal to) ``workspace_root``.
- L113 `nearest_root(start: str, markers: Iterable[str], *, excludes: Optional[Iterable[str]]=None, ceiling: Optional[str]=None)` (function) — Walk up from ``start`` looking for any of the given marker files.
- L173 `resolve_workspace_for_file(file_path: str, *, cwd: Optional[str]=None)` (function) — Resolve the workspace root for a file.
- L207 `clear_cache()` (function) — Clear the workspace-resolution cache.
