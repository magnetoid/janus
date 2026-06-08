---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_shell_hooks.py

Symbols in `tests/agent/test_shell_hooks.py`.

- L22 `_write_script(tmp_path: Path, name: str, body: str)` (function)
- L29 `_allowlist_pair(monkeypatch, tmp_path, event: str, command: str)` (function)
- L35 `_reset_registration_state()` (function)
- L44 `TestParseResponse` (class)
- L45 `test_block_claude_code_style(self)` (method)
- L52 `test_block_canonical_style(self)` (method)
- L59 `test_block_canonical_wins_over_claude_style(self)` (method)
- L67 `test_empty_stdout_returns_none(self)` (method)
- L71 `test_invalid_json_returns_none(self)` (method)
- L74 `test_non_dict_json_returns_none(self)` (method)
- L77 `test_non_block_pre_tool_call_returns_none(self)` (method)
- L81 `test_pre_llm_call_context_passthrough(self)` (method)
- L87 `test_subagent_stop_context_passthrough(self)` (method)
- L93 `test_pre_llm_call_block_ignored(self)` (method) — Only pre_tool_call honors block directives.
- L100 `test_block_action_without_message_uses_default(self)` (method) — Block is honored even when message/reason is absent.
- L105 `test_block_decision_without_reason_uses_default(self)` (method) — Block is honored even when reason/message is absent.
- L110 `test_block_action_empty_message_uses_default(self)` (method) — Empty string message falls back to default, not empty string.
- L117 `test_block_action_non_string_message_uses_default(self)` (method) — Non-string message (e.g. integer) falls back to default.
- L128 `TestSerializePayload` (class)
- L129 `test_basic_pre_tool_call_schema(self)` (method)
- L150 `test_args_not_dict_becomes_null(self)` (method)
- L157 `test_parent_session_id_used_when_no_session_id(self)` (method)
- L164 `test_unserialisable_extras_stringified(self)` (method)
- L179 `TestMatcher` (class)
- L180 `test_no_matcher_fires_for_any_tool(self)` (method)
- L187 `test_single_name_matcher(self)` (method)
- L194 `test_alternation_matcher(self)` (method)
- L202 `test_invalid_regex_falls_back_to_literal(self)` (method)
- L209 `test_matcher_ignored_when_no_tool_name(self)` (method)
- L215 `test_matcher_leading_whitespace_stripped(self)` (method) — YAML quirks can introduce leading/trailing whitespace — must
- L224 `test_matcher_trailing_newline_stripped(self)` (method)
- L230 `test_whitespace_only_matcher_becomes_none(self)` (method) — A matcher that's pure whitespace is treated as 'no matcher'.
- L242 `TestCallbackSubprocess` (class)
- L243 `test_timeout_returns_none(self, tmp_path)` (method)
- L255 `test_malformed_json_stdout_returns_none(self, tmp_path)` (method)
- L267 `test_non_zero_exit_with_block_stdout_still_blocks(self, tmp_path)` (method) — A script that signals failure via exit code AND prints a block
- L283 `test_block_translation_end_to_end(self, tmp_path)` (method) — v1 schema-bug regression gate.
- L304 `test_block_aggregation_through_plugin_manager(self, tmp_path, monkeypatch)` (method) — Registering via register_from_config makes
- L338 `test_matcher_regex_filters_callback(self, tmp_path, monkeypatch)` (method) — A matcher set to 'terminal' must not fire for 'web_search'.
- L360 `test_payload_schema_delivered(self, tmp_path)` (method)
- L384 `test_pre_llm_call_context_flows_through(self, tmp_path)` (method)
- L401 `test_shlex_handles_paths_with_spaces(self, tmp_path)` (method)
- L417 `test_missing_binary_logged_not_raised(self, tmp_path)` (method)
- L426 `test_non_executable_binary_logged_not_raised(self, tmp_path)` (method)
- L440 `TestParseHooksBlock` (class)
- L441 `test_valid_entry(self)` (method)
- L453 `test_unknown_event_skipped(self, caplog)` (method)
- L461 `test_missing_command_skipped(self)` (method)
- L467 `test_timeout_clamped_to_max(self)` (method)
- L475 `test_non_int_timeout_defaulted(self)` (method)
- L483 `test_non_list_event_skipped(self)` (method)
- L489 `test_none_hooks_block(self)` (method)
- L494 `test_non_tool_event_matcher_warns_and_drops(self, caplog)` (method) — matcher: is only honored for pre/post_tool_call; must warn
- L512 `TestIdempotentRegistration` (class)
- L513 `test_double_call_registers_once(self, tmp_path, monkeypatch)` (method)
- L533 `test_same_command_different_matcher_registers_both(self, tmp_path, monkeypatch)` (method) — Same script used for different matchers under one event must
- L565 `TestAllowlistConcurrency` (class) — Regression tests for the Codex#1 finding: simultaneous
- L570 `test_parallel_record_approval_does_not_lose_entries(self, tmp_path, monkeypatch)` (method)
- L604 `test_non_posix_fallback_does_not_self_deadlock(self, tmp_path, monkeypatch)` (method) — Regression: on platforms without fcntl, the fallback lock must
- L643 `test_save_allowlist_failure_logs_actionable_warning(self, tmp_path, monkeypatch, caplog)` (method) — Persistence failures must log the path, errno, and
- L664 `test_script_is_executable_handles_interpreter_prefix(self, tmp_path)` (method) — For ``python3 hook.py`` and similar the interpreter reads
- L682 `test_command_script_path_resolution(self)` (method) — Regression: ``_command_script_path`` used to return the first
- L716 `test_save_allowlist_uses_unique_tmp_paths(self, tmp_path, monkeypatch)` (method) — Two save_allowlist calls in flight must use distinct tmp files
