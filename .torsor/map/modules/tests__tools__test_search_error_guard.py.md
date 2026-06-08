---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_search_error_guard.py

Symbols in `tests/tools/test_search_error_guard.py`.

- L36 `_ops(root)` (function)
- L41 `match_tree(tmp_path)` (function) — A tree with several files all containing 'needle'.
- L49 `partial_error_tree(tmp_path)` (function) — A tree with matches plus one unreadable file (forces exit 2 + matches).
- L68 `_search(ops, method, pattern, path, **kw)` (function)
- L76 `TestSearchErrorGuard` (class)
- L77 `test_happy_path_returns_matches(self, method, match_tree)` (method)
- L82 `test_hard_error_is_surfaced(self, method, match_tree)` (method)
- L90 `test_partial_error_keeps_matches(self, method, partial_error_tree)` (method)
- L97 `test_no_match_is_empty_not_error(self, method, match_tree)` (method)
- L102 `test_truncation_no_false_error(self, method, tmp_path)` (method)
- L111 `test_files_only_excludes_diagnostics(self, method, partial_error_tree)` (method)
- L120 `test_count_mode_with_partial_error(self, method, partial_error_tree)` (method)
- L127 `TestSplitToolDiagnostics` (class) — Unit coverage for the shape-based diagnostic/payload splitter.
- L130 `test_pure_error_has_empty_payload(self)` (method)
- L136 `test_partial_error_separates_matches(self)` (method)
- L145 `test_files_only_is_payload(self)` (method)
- L150 `test_count_lines_are_payload(self)` (method)
- L155 `test_context_lines_and_separator_are_payload(self)` (method)
