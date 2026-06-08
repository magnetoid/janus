---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_plugin_context_engine_init.py

Symbols in `tests/run_agent/test_plugin_context_engine_init.py`.

- L12 `_StubEngine` (class) — Minimal concrete context engine for testing.
- L16 `name(self)` (method)
- L19 `update_from_response(self, usage)` (method)
- L22 `should_compress(self, prompt_tokens=None)` (method)
- L25 `compress(self, messages, current_tokens=None)` (method)
- L29 `_ToolEngine` (class)
- L30 `get_tool_schemas(self)` (method)
- L40 `test_plugin_engine_gets_context_length_on_init()` (function) — Plugin context engine should have context_length set during AIAgent init.
- L70 `test_active_context_engine_tools_survive_explicit_platform_toolsets()` (function) — LCM-style recovery tools must survive saved `hermes tools` lists.
- L110 `test_plugin_engine_update_model_args()` (function) — Verify update_model() receives model, context_length, base_url, api_key, provider.
