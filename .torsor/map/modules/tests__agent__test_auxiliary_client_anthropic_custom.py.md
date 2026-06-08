---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_auxiliary_client_anthropic_custom.py

Symbols in `tests/agent/test_auxiliary_client_anthropic_custom.py`.

- L18 `_clean_env(monkeypatch)` (function)
- L26 `_install_anthropic_adapter_mocks()` (function) — Patch build_anthropic_client so the test doesn't need the SDK.
- L35 `test_custom_endpoint_anthropic_messages_builds_anthropic_wrapper()` (function) — api_mode=anthropic_messages → returns AnthropicAuxiliaryClient, not OpenAI.
- L65 `test_custom_endpoint_anthropic_messages_falls_back_when_sdk_missing()` (function) — Graceful degradation when anthropic SDK is unavailable.
- L92 `test_custom_endpoint_chat_completions_still_uses_openai_wire()` (function) — Regression: default path (no api_mode) must remain OpenAI client.
