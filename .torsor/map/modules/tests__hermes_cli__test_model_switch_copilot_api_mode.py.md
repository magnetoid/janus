---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_switch_copilot_api_mode.py

Symbols in `tests/hermes_cli/test_model_switch_copilot_api_mode.py`.

- L23 `_run_copilot_switch(raw_input: str, current_provider: str='copilot', current_model: str='gpt-5.4', explicit_provider: str='', runtime_api_mode: str='codex_responses')` (function) — Run switch_model with Copilot mocks and return the result.
- L58 `test_same_provider_copilot_switch_recomputes_api_mode()` (function) — GPT-5 → Claude on copilot: api_mode must flip to chat_completions.
- L72 `test_explicit_copilot_switch_uses_selected_model_api_mode()` (function) — Cross-provider switch to copilot: api_mode from new model, not stale runtime.
- L87 `test_copilot_gpt5_keeps_codex_responses()` (function) — GPT-5 → GPT-5 on copilot: api_mode must stay codex_responses.
