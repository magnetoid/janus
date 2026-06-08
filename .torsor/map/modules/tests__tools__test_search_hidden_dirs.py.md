---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_search_hidden_dirs.py

Symbols in `tests/tools/test_search_hidden_dirs.py`.

- L22 `searchable_tree(tmp_path)` (function) — Create a directory tree with hidden and visible directories.
- L44 `TestFindExcludesHiddenDirs` (class) — _search_files uses find, which should exclude hidden directories.
- L47 `test_find_skips_hub_cache_files(self, searchable_tree)` (method) — find should not return files from .hub/ directory.
- L56 `test_find_skips_git_internals(self, searchable_tree)` (method) — find should not return files from .git/ directory.
- L65 `test_find_still_returns_visible_files(self, searchable_tree)` (method) — find should still return files from visible directories.
- L74 `TestGrepExcludesHiddenDirs` (class) — _search_with_grep should exclude hidden directories.
- L77 `test_grep_skips_hub_cache(self, searchable_tree)` (method) — grep --exclude-dir should skip .hub/ directory.
- L87 `test_grep_still_finds_visible_content(self, searchable_tree)` (method) — grep should still find content in visible directories.
- L96 `TestRipgrepAlreadyExcludesHidden` (class) — Verify ripgrep's default behavior is to skip hidden directories.
- L103 `test_rg_skips_hub_by_default(self, searchable_tree)` (method) — rg should skip .hub/ by default (no --hidden flag).
- L116 `test_rg_finds_visible_content(self, searchable_tree)` (method) — rg should find content in visible directories.
- L125 `TestIgnoreFileWritten` (class) — _write_index_cache should create .ignore in .hub/ directory.
- L128 `test_write_index_cache_creates_ignore_file(self, tmp_path, monkeypatch)` (method)
- L148 `test_write_index_cache_does_not_overwrite_existing_ignore(self, tmp_path, monkeypatch)` (method)
