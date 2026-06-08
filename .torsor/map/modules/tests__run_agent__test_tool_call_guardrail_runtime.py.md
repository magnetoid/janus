---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_tool_call_guardrail_runtime.py

Symbols in `tests/run_agent/test_tool_call_guardrail_runtime.py`.

- L11 `_make_tool_defs(*names: str)` (function)
- L25 `_mock_tool_call(name='web_search', arguments='{}', call_id=None)` (function)
- L33 `_mock_response(content='Hello', finish_reason='stop', tool_calls=None)` (function)
- L39 `_make_agent(*tool_names: str, max_iterations: int=10, config: dict | None=None)` (function)
- L63 `_seed_exact_failures(agent: AIAgent, tool_name: str, args: dict, count: int=2)` (function)
- L73 `_hard_stop_config(**overrides)` (function)
- L89 `test_default_sequential_path_warns_repeated_exact_failure_without_blocking_execution()` (function)
- L115 `test_config_enabled_hard_stop_blocks_repeated_exact_failure_before_execution()` (function)
- L139 `test_sequential_after_call_appends_guidance_to_tool_result_without_extra_messages()` (function)
- L156 `test_same_tool_failure_warning_tells_model_to_recover_with_tools()` (function)
- L187 `test_config_enabled_hard_stop_concurrent_path_does_not_submit_blocked_calls_and_preserves_result_order()` (function)
- L223 `test_plugin_pre_tool_block_wins_without_counting_as_toolguard_block()` (function)
- L241 `test_default_run_conversation_warns_without_guardrail_halt()` (function)
- L271 `test_config_enabled_hard_stop_run_conversation_returns_controlled_guardrail_halt_without_top_level_error()` (function)
- L309 `test_guardrail_halt_emits_final_response_through_stream_delta_callback()` (function) — Regression for #30770: when the guardrail halts the loop, the
