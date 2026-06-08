---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_complete_path_at_filter.py

Symbols in `tests/gateway/test_complete_path_at_filter.py`.

- L29 `_fixture(tmp_path: Path)` (function)
- L36 `_items(word: str)` (function)
- L43 `_reset_fuzzy_cache(monkeypatch)` (function)
- L51 `test_at_folder_colon_only_dirs(tmp_path, monkeypatch)` (function)
- L64 `test_at_file_colon_only_files(tmp_path, monkeypatch)` (function)
- L76 `test_at_folder_bare_without_colon_lists_dirs(tmp_path, monkeypatch)` (function)
- L87 `test_at_file_bare_without_colon_lists_files(tmp_path, monkeypatch)` (function)
- L97 `test_bare_at_still_shows_static_refs(tmp_path, monkeypatch)` (function) — `@` alone should list the static references so users discover the
- L114 `_nested_fixture(tmp_path: Path)` (function)
- L127 `test_fuzzy_at_finds_file_without_directory_prefix(tmp_path, monkeypatch)` (function) — `@appChrome` — with no slash — should surface the nested file.
- L144 `test_fuzzy_ranks_exact_before_prefix_before_subseq(tmp_path, monkeypatch)` (function) — Better matches sort before weaker matches regardless of path depth.
- L159 `test_fuzzy_camelcase_word_boundary(tmp_path, monkeypatch)` (function) — Mid-basename camelCase pieces match without substring scanning.
- L170 `test_fuzzy_subsequence_catches_sparse_queries(tmp_path, monkeypatch)` (function) — `@uCo` → `useCompletion.ts` via subsequence, last-resort tier.
- L180 `test_fuzzy_at_file_prefix_preserved(tmp_path, monkeypatch)` (function) — Explicit `@file:` prefix still wins the completion tag.
- L190 `test_fuzzy_skipped_when_path_has_slash(tmp_path, monkeypatch)` (function) — Any `/` in the query = user is navigating; keep directory listing.
- L204 `test_fuzzy_skipped_when_folder_tag(tmp_path, monkeypatch)` (function) — `@folder:<name>` still lists directories — fuzzy scanner only walks
- L216 `test_fuzzy_hides_dotfiles_unless_asked(tmp_path, monkeypatch)` (function) — `.env` doesn't leak into `@env` but does show for `@.env`.
- L225 `test_fuzzy_caps_results(tmp_path, monkeypatch)` (function) — The 30-item cap survives a big tree.
- L236 `test_fuzzy_paths_relative_to_cwd_inside_subdir(tmp_path, monkeypatch)` (function) — When the gateway runs from a subdirectory of a git repo, fuzzy
