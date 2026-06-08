---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_model_tools.py

Symbols in `tests/test_model_tools.py`.

- L21 `TestHandleFunctionCall` (class)
- L22 `test_agent_loop_tool_returns_error(self)` (method)
- L28 `test_unknown_tool_returns_error(self)` (method)
- L33 `test_exception_returns_json_error(self)` (method)
- L42 `test_tool_hooks_receive_session_and_tool_call_ids(self)` (method)
- L102 `test_post_tool_call_receives_non_negative_integer_duration_ms(self)` (method) — Regression: post_tool_call and transform_tool_result hooks must
- L130 `test_no_listener_skips_post_and_transform_emit(self)` (method) — When no plugin is registered for post_tool_call /
- L150 `test_tool_request_and_execution_middleware_wrap_registry_dispatch(self, monkeypatch)` (method)
- L209 `TestAgentLoopTools` (class)
- L210 `test_expected_tools_in_set(self)` (method)
- L216 `test_no_regular_tools_in_set(self)` (method)
- L225 `TestPreToolCallBlocking` (class) — Verify that pre_tool_call hooks can block tool execution.
- L228 `test_blocked_tool_returns_error_and_skips_dispatch(self, monkeypatch)` (method)
- L258 `test_blocked_tool_skips_read_loop_notification(self, monkeypatch)` (method)
- L276 `test_invalid_hook_returns_do_not_block(self, monkeypatch)` (method) — Malformed hook returns should be ignored — tool executes normally.
- L294 `test_skip_flag_prevents_double_fire(self, monkeypatch)` (method) — When skip_pre_tool_call_hook=True, the hook does not fire again.
- L329 `test_run_agent_pattern_fires_pre_tool_call_exactly_once(self, monkeypatch)` (method) — End-to-end regression for the double-fire bug.
- L375 `TestLegacyToolsetMap` (class)
- L376 `test_expected_legacy_names(self)` (method)
- L385 `test_values_are_lists_of_strings(self)` (method)
- L396 `TestBackwardCompat` (class)
- L397 `test_get_all_tool_names_returns_list(self)` (method)
- L405 `test_get_toolset_for_tool(self)` (method)
- L410 `test_get_toolset_for_unknown_tool(self)` (method)
- L414 `test_tool_to_toolset_map(self)` (method)
- L424 `TestCoerceNumberInfNan` (class) — _coerce_number must honor its documented contract ("Returns original
- L429 `test_inf_returns_original_string(self)` (method)
- L433 `test_negative_inf_returns_original_string(self)` (method)
- L437 `test_nan_returns_original_string(self)` (method)
- L441 `test_infinity_spelling_returns_original_string(self)` (method)
- L446 `test_coerced_result_is_strict_json_safe(self)` (method) — Whatever _coerce_number returns for inf/nan must round-trip
- L454 `test_normal_numbers_still_coerce(self)` (method) — Guard against over-correction — real numbers still coerce.
