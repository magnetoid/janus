---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_display_tool_failure.py

Symbols in `tests/agent/test_display_tool_failure.py`.

- L19 `TestTrimError` (class) — The helper that shrinks an error message for inline display.
- L22 `test_short_message_unchanged(self)` (method)
- L25 `test_whitespace_stripped(self)` (method)
- L28 `test_long_message_truncated_to_cap(self)` (method)
- L34 `test_file_not_found_path_collapsed_to_filename(self)` (method)
- L38 `test_file_not_found_already_short_unchanged(self)` (method)
- L41 `test_file_not_found_relative_path_unchanged(self)` (method)
- L46 `TestDetectToolFailureTerminal` (class) — terminal: non-zero exit_code is the canonical failure signal.
- L49 `test_success_returns_no_suffix(self)` (method)
- L53 `test_nonzero_exit_with_no_error_shows_exit_code(self)` (method)
- L59 `test_nonzero_exit_with_error_shows_message(self)` (method)
- L72 `test_malformed_json_returns_no_suffix(self)` (method)
- L77 `test_none_result_returns_no_suffix(self)` (method)
- L81 `TestDetectToolFailureMemory` (class) — memory: 'full' is distinct from real errors.
- L84 `test_memory_full_returns_full_suffix(self)` (method)
- L88 `test_memory_other_error_returns_specific_message(self)` (method)
- L97 `TestDetectToolFailureStructured` (class) — Generic path: any tool that returns {"error": ...} JSON.
- L100 `test_read_file_error_surfaced(self)` (method)
- L111 `test_error_without_success_key_still_flagged(self)` (method)
- L118 `test_message_field_only_with_success_false_flagged(self)` (method)
- L125 `test_successful_result_not_flagged(self)` (method)
- L129 `test_dict_without_error_or_success_uses_generic_heuristic(self)` (method)
- L137 `TestGetCuteToolMessageFailureSuffix` (class) — End-to-end: failure suffix is appended by get_cute_tool_message.
- L140 `test_read_file_failure_suffix_appended(self)` (method)
- L149 `test_terminal_exit_only_suffix(self)` (method)
- L154 `test_terminal_with_stderr_uses_message(self)` (method)
- L165 `test_memory_full_suffix(self)` (method)
- L175 `test_success_has_no_suffix(self)` (method)
- L180 `test_no_result_has_no_suffix(self)` (method)
