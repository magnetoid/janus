---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_tools.py

Symbols in `tests/tools/test_file_tools.py`.

- L16 `TestReadFileHandler` (class)
- L18 `test_returns_file_content(self, mock_get)` (method)
- L33 `test_custom_offset_and_limit(self, mock_get)` (method)
- L46 `test_invalid_offset_and_limit_are_normalized_before_dispatch(self, mock_get)` (method)
- L59 `test_exception_returns_error_json(self, mock_get)` (method)
- L68 `TestWriteFileHandler` (class)
- L70 `test_writes_content(self, mock_get)` (method)
- L83 `test_permission_error_returns_error_json_without_error_log(self, mock_get, caplog)` (method)
- L95 `test_unexpected_exception_still_logs_error(self, mock_get, caplog)` (method)
- L104 `test_missing_content_key_returns_error(self)` (method) — #19096 — handler must reject tool calls where 'content' key is absent.
- L113 `test_missing_path_key_returns_error(self)` (method) — #19096 — handler must reject tool calls where 'path' key is absent.
- L120 `test_explicit_empty_content_is_allowed(self)` (method) — #19096 — explicit empty string content (file truncation) must still work.
- L134 `test_non_string_content_returns_error(self)` (method) — #19096 — content must be a string, not a dict or list.
- L143 `TestPatchHandler` (class)
- L145 `test_replace_mode_calls_patch_replace(self, mock_get)` (method)
- L161 `test_replace_mode_replace_all_flag(self, mock_get)` (method)
- L174 `test_replace_mode_missing_path_errors(self, mock_get)` (method)
- L180 `test_replace_mode_missing_strings_errors(self, mock_get)` (method)
- L186 `test_patch_mode_calls_patch_v4a(self, mock_get)` (method)
- L199 `test_patch_mode_missing_content_errors(self, mock_get)` (method)
- L205 `test_unknown_mode_errors(self, mock_get)` (method)
- L212 `test_patch_v4a_rejects_traversal_in_update_header(self, mock_get)` (method) — V4A '*** Update File:' headers come from patch content, which can
- L236 `test_patch_v4a_rejects_traversal_in_add_header(self, mock_get)` (method)
- L251 `TestSearchHandler` (class)
- L253 `test_search_calls_file_ops(self, mock_get)` (method)
- L266 `test_search_passes_all_params(self, mock_get)` (method)
- L282 `test_search_normalizes_invalid_pagination_before_dispatch(self, mock_get)` (method)
- L297 `test_search_exception_returns_error(self, mock_get)` (method)
- L309 `TestPatchHints` (class) — Patch tool should hint when old_string is not found.
- L313 `test_no_match_includes_hint(self, mock_get)` (method)
- L330 `test_success_no_hint(self, mock_get)` (method)
- L342 `TestSearchHints` (class) — Search tool should hint when results are truncated.
- L345 `setup_method(self)` (method) — Clear read/search tracker between tests to avoid cross-test state.
- L351 `test_truncated_results_hint(self, mock_get)` (method)
- L368 `test_non_truncated_no_hint(self, mock_get)` (method)
- L383 `test_truncated_hint_with_nonzero_offset(self, mock_get)` (method)
- L405 `TestSensitivePathCheck` (class) — Verify that _check_sensitive_path blocks writes to protected locations.
- L408 `test_hermes_config_blocked_for_write_file(self, tmp_path, monkeypatch)` (method)
- L418 `test_hermes_config_blocked_via_tilde_path(self, tmp_path, monkeypatch)` (method)
- L428 `test_hermes_config_blocked_for_patch(self, tmp_path, monkeypatch)` (method)
- L444 `test_system_path_still_blocked(self, monkeypatch)` (method)
- L454 `test_normal_file_not_blocked(self, mock_get, monkeypatch)` (method)
- L468 `TestPatchSchemaShape` (class) — PATCH_SCHEMA must advertise per-mode required params via description
- L473 `test_per_mode_required_params_documented_in_descriptions(self)` (method)
- L482 `test_no_anyof_required_stays_mode_only(self)` (method)
