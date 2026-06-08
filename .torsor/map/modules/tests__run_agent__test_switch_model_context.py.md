---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_switch_model_context.py

Symbols in `tests/run_agent/test_switch_model_context.py`.

- L9 `_make_agent_with_compressor(config_context_length=None)` (function) — Build a minimal AIAgent with a context_compressor, skipping __init__.
- L44 `test_switch_model_clears_previous_config_context_length(mock_ctx_len)` (function) — Switching models must not reuse the previous model.context_length override.
- L64 `test_switch_model_without_config_context_length()` (function) — When switching models without config override, config_context_length should be None.
