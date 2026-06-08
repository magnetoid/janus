---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_transform_tool_result_hook.py

Symbols in `tests/test_transform_tool_result_hook.py`.

- L18 `_run_handle_function_call(monkeypatch, *, tool_name='dummy_tool', tool_args=None, dispatch_result='{"output": "original"}', invoke_hook=_UNSET)` (function) — Drive ``handle_function_call`` with a mocked registry dispatch.
- L54 `test_result_unchanged_when_no_hook_registered(monkeypatch)` (function)
- L64 `test_result_unchanged_for_none_hook_return(monkeypatch)` (function)
- L72 `test_result_ignores_non_string_hook_returns(monkeypatch)` (function)
- L80 `test_first_valid_string_return_replaces_result(monkeypatch)` (function)
- L88 `test_hook_receives_expected_kwargs(monkeypatch)` (function)
- L112 `test_hook_exception_falls_back_to_original(monkeypatch)` (function)
- L123 `test_post_tool_call_remains_observational(monkeypatch)` (function) — post_tool_call return values must NOT replace the result.
- L138 `test_transform_tool_result_runs_after_post_tool_call(monkeypatch)` (function) — post_tool_call sees ORIGINAL result; transform_tool_result sees same and may replace.
- L164 `test_transform_tool_result_integration_with_real_plugin(monkeypatch, tmp_path)` (function) — End-to-end: load a real plugin from HERMES_HOME and verify it rewrites results.
