---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_step_callback_compat.py

Symbols in `tests/gateway/test_step_callback_compat.py`.

- L12 `TestStepCallbackNormalization` (class) — The gateway's _step_callback_sync normalizes prev_tools from run_agent.
- L15 `_extract_step_callback(self)` (method) — Build a minimal _step_callback_sync using the same logic as gateway/run.py.
- L48 `test_dict_prev_tools_produce_string_tool_names(self)` (method) — When prev_tools is list[dict], tool_names should be list[str].
- L76 `test_string_prev_tools_still_work(self)` (method) — When prev_tools is list[str] (legacy), tool_names should pass through.
- L96 `test_empty_prev_tools(self)` (method) — Empty or None prev_tools should produce empty tool_names.
- L114 `test_joinable_for_hook_example(self)` (method) — The documented hook example: ', '.join(tool_names) should work.
