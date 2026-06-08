---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_update_config_clears_custom_fields.py

Symbols in `tests/hermes_cli/test_update_config_clears_custom_fields.py`.

- L22 `_read_model_cfg()` (function)
- L31 `_seed_custom_provider_config(api_mode: str='anthropic_messages')` (function) — Write a config.yaml mimicking a user on a MiniMax-style custom provider.
- L51 `TestUpdateConfigForProviderClearsStaleCustomFields` (class)
- L52 `test_switching_to_openrouter_clears_api_key_and_api_mode(self)` (method)
- L72 `test_switching_to_nous_clears_stale_api_mode(self)` (method)
- L80 `test_switching_clears_codex_responses_api_mode(self)` (method) — Also covers codex_responses, not just anthropic_messages.
