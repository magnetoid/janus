---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/lsp/test_broken_set.py

Symbols in `tests/agent/lsp/test_broken_set.py`.

- L27 `_clear_workspace_cache()` (function)
- L33 `_make_git_workspace(tmp_path: Path)` (function) — Build a minimal git repo with a pyproject so pyright's root resolver fires.
- L42 `test_mark_broken_for_file_adds_correct_key(tmp_path, monkeypatch)` (function) — ``_mark_broken_for_file`` keys the broken-set on
- L65 `test_enabled_for_returns_false_after_broken(tmp_path, monkeypatch)` (function) — Once a (server_id, root) pair is in the broken-set,
- L91 `test_enabled_for_other_file_in_same_project_also_skipped(tmp_path, monkeypatch)` (function) — The broken key is (server_id, root), so ALL files routed through
- L117 `test_unrelated_project_not_affected_by_broken(tmp_path, monkeypatch)` (function) — Marking pyright broken for project A must NOT affect project B.
- L147 `test_mark_broken_handles_missing_server_silently(tmp_path)` (function) — If the file extension doesn't match any registered server,
- L164 `test_mark_broken_handles_no_workspace_silently(tmp_path)` (function) — File outside any git worktree → no workspace → no key to add.
- L181 `test_snapshot_failure_marks_broken_via_outer_timeout(tmp_path, monkeypatch)` (function) — End-to-end: ``snapshot_baseline``'s outer ``_loop.run`` timeout
