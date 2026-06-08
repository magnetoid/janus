---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_workspace.py

Symbols in `tests/agent/lsp/test_workspace.py`.

- L20 `_clear()` (function)
- L26 `test_find_git_worktree_returns_none_outside_repo(tmp_path: Path)` (function)
- L32 `test_find_git_worktree_finds_dotgit(tmp_path: Path)` (function)
- L41 `test_find_git_worktree_handles_dotgit_file(tmp_path: Path)` (function) — ``.git`` can also be a file (gitfile pointing into a worktree).
- L49 `test_is_inside_workspace_true_for_subpath(tmp_path: Path)` (function)
- L58 `test_is_inside_workspace_false_for_unrelated(tmp_path: Path)` (function)
- L68 `test_nearest_root_finds_first_marker(tmp_path: Path)` (function)
- L77 `test_nearest_root_excludes_take_priority(tmp_path: Path)` (function) — If an exclude marker matches first, return None.
- L92 `test_nearest_root_returns_none_when_no_marker(tmp_path: Path)` (function)
- L98 `test_resolve_workspace_for_file_uses_cwd_first(tmp_path: Path, monkeypatch)` (function)
- L110 `test_resolve_workspace_for_file_no_repo_returns_none(tmp_path: Path, monkeypatch)` (function)
- L119 `test_resolve_workspace_falls_back_to_file_location(tmp_path: Path, monkeypatch)` (function) — When cwd isn't a git repo but the file is inside one, we still
- L136 `test_normalize_path_expands_tilde(monkeypatch)` (function)
