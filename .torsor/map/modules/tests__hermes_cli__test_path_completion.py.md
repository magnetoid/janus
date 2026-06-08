---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_path_completion.py

Symbols in `tests/hermes_cli/test_path_completion.py`.

- L13 `_display_names(completions)` (function) — Extract plain-text display names from a list of Completion objects.
- L18 `_display_metas(completions)` (function) — Extract plain-text display_meta from a list of Completion objects.
- L24 `completer()` (function)
- L28 `TestExtractPathWord` (class)
- L29 `test_relative_path(self)` (method)
- L32 `test_home_path(self)` (method)
- L35 `test_absolute_path(self)` (method)
- L38 `test_parent_path(self)` (method)
- L41 `test_path_with_slash_in_middle(self)` (method)
- L44 `test_plain_word_not_path(self)` (method)
- L47 `test_empty_string(self)` (method)
- L50 `test_single_word_no_slash(self)` (method)
- L53 `test_word_after_space(self)` (method)
- L56 `test_just_dot_slash(self)` (method)
- L59 `test_just_tilde_slash(self)` (method)
- L63 `TestPathCompletions` (class)
- L64 `test_lists_current_directory(self, tmp_path)` (method)
- L80 `test_filters_by_prefix(self, tmp_path)` (method)
- L91 `test_directories_have_trailing_slash(self, tmp_path)` (method)
- L102 `test_home_expansion(self, tmp_path, monkeypatch)` (method)
- L110 `test_nonexistent_dir_returns_empty(self)` (method)
- L114 `test_respects_limit(self, tmp_path)` (method)
- L121 `test_case_insensitive_prefix(self, tmp_path)` (method)
- L129 `TestIntegration` (class) — Test the completer produces path completions via the prompt_toolkit API.
- L132 `test_slash_commands_still_work(self, completer)` (method)
- L139 `test_path_completion_triggers_on_dot_slash(self, completer, tmp_path)` (method)
- L152 `test_no_completion_for_plain_words(self, completer)` (method)
- L158 `test_absolute_path_triggers_completion(self, completer)` (method)
- L167 `TestFileSizeLabel` (class)
- L168 `test_bytes(self, tmp_path)` (method)
- L173 `test_kilobytes(self, tmp_path)` (method)
- L178 `test_megabytes(self, tmp_path)` (method)
- L183 `test_nonexistent(self)` (method)
