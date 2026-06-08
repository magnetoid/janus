---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_tool_result_storage.py

Symbols in `tests/tools/test_tool_result_storage.py`.

- L28 `TestGeneratePreview` (class)
- L29 `test_short_content_unchanged(self)` (method)
- L35 `test_long_content_truncated(self)` (method)
- L41 `test_truncates_at_newline_boundary(self)` (method)
- L48 `test_ignores_early_newline(self)` (method)
- L55 `test_empty_content(self)` (method)
- L60 `test_exact_boundary(self)` (method)
- L69 `TestHeredocMarker` (class)
- L70 `test_default_marker_when_no_collision(self)` (method)
- L73 `test_uuid_marker_on_collision(self)` (method)
- L83 `TestWriteToSandbox` (class)
- L84 `test_success(self)` (method)
- L98 `test_failure_returns_false(self)` (method)
- L104 `test_large_content_via_stdin(self)` (method) — Regression: 200 KB content exceeds Linux MAX_ARG_STRLEN (128 KB).
- L115 `test_timeout_passed(self)` (method)
- L121 `test_uses_parent_dir_of_remote_path(self)` (method)
- L129 `test_path_with_spaces_is_quoted(self)` (method)
- L138 `test_shell_metacharacters_neutralized(self)` (method) — Paths with shell metacharacters must be quoted to prevent injection.
- L148 `test_semicolon_injection_neutralized(self)` (method)
- L158 `TestResolveStorageDir` (class)
- L159 `test_defaults_to_storage_dir_without_env(self)` (method)
- L162 `test_uses_env_temp_dir_when_available(self)` (method)
- L170 `TestBuildPersistedMessage` (class)
- L171 `test_structure(self)` (method)
- L186 `test_no_ellipsis_when_complete(self)` (method)
- L197 `test_large_size_shows_mb(self)` (method)
- L209 `TestMaybePersistToolResult` (class)
- L210 `test_below_threshold_returns_unchanged(self)` (method)
- L221 `test_above_threshold_with_env_persists(self)` (method)
- L237 `test_persists_full_content_as_is(self)` (method) — Content is persisted verbatim — no JSON extraction.
- L256 `test_above_threshold_no_env_truncates_inline(self)` (method)
- L269 `test_env_write_failure_falls_back_to_truncation(self)` (method)
- L283 `test_env_execute_exception_falls_back(self)` (method)
- L296 `test_read_file_never_persisted(self)` (method) — read_file has threshold=inf, should never be persisted.
- L310 `test_uses_registry_threshold_when_not_provided(self)` (method) — When threshold=None, looks up from registry.
- L330 `test_unicode_content_survives(self)` (method)
- L345 `test_empty_content_returns_unchanged(self)` (method)
- L355 `test_whitespace_only_below_threshold(self)` (method)
- L366 `test_file_path_uses_tool_use_id(self)` (method)
- L379 `test_preview_included_in_persisted_output(self)` (method)
- L393 `test_env_temp_dir_changes_persisted_path(self)` (method)
- L409 `test_threshold_zero_forces_persist(self)` (method)
- L426 `TestEnforceTurnBudget` (class)
- L427 `test_under_budget_no_changes(self)` (method)
- L436 `test_over_budget_largest_persisted_first(self)` (method)
- L448 `test_already_persisted_results_skipped(self)` (method)
- L462 `test_medium_result_regression(self)` (method) — 6 results of 42K chars each (252K total) — each under 100K default
- L478 `test_no_env_falls_back_to_truncation(self)` (method)
- L486 `test_returns_same_list(self)` (method)
- L491 `test_empty_messages(self)` (method)
- L498 `TestPerToolThresholds` (class) — Verify registry wiring for per-tool thresholds.
- L501 `test_registry_has_get_max_result_size(self)` (method)
- L505 `test_default_threshold(self)` (method)
- L511 `test_terminal_threshold(self)` (method)
- L521 `test_read_file_result_size_cap(self)` (method)
- L530 `test_read_file_registry_cap_is_100k(self)` (method) — Regression test: read_file must have a 100_000 char registry cap (Layer 2 safety net).
- L543 `test_search_files_threshold(self)` (method)
