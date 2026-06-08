---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_worktree_security.py

Symbols in `tests/cli/test_worktree_security.py`.

- L10 `git_repo(tmp_path)` (function) — Create a temporary git repo for testing real cli._setup_worktree behavior.
- L23 `_force_remove_worktree(info: dict | None)` (function)
- L40 `TestWorktreeIncludeSecurity` (class)
- L41 `test_rejects_parent_directory_file_traversal(self, git_repo)` (method)
- L59 `test_rejects_parent_directory_directory_traversal(self, git_repo)` (method)
- L79 `test_rejects_symlink_that_resolves_outside_repo(self, git_repo)` (method)
- L96 `test_allows_valid_file_include(self, git_repo)` (method)
- L113 `test_allows_valid_directory_include(self, git_repo)` (method)
