---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_kimi_coding_anthropic_thinking.py

Symbols in `tests/agent/test_kimi_coding_anthropic_thinking.py`.

- L27 `TestKimiCodingSkipsAnthropicThinking` (class) — build_anthropic_kwargs must not inject ``thinking`` for Kimi /coding.
- L39 `test_kimi_coding_endpoint_omits_thinking(self, base_url: str)` (method)
- L56 `test_kimi_coding_with_explicit_disabled_also_omits(self)` (method)
- L69 `test_non_kimi_third_party_still_gets_thinking(self)` (method) — MiniMax and other third-party Anthropic endpoints must retain thinking.
- L84 `test_native_anthropic_still_gets_thinking(self)` (method)
- L97 `test_kimi_root_endpoint_via_anthropic_transport_omits_thinking(self)` (method) — Plain ``api.kimi.com`` hit via the Anthropic transport also omits thinking.
- L135 `test_kimi_family_custom_endpoint_omits_thinking(self, base_url: str, model: str)` (method) — Custom / proxied Kimi endpoints must also strip Anthropic thinking.
- L156 `test_custom_endpoint_non_kimi_model_keeps_thinking(self)` (method) — Custom endpoint with a non-Kimi model must keep thinking intact.
- L175 `test_kimi_family_replay_preserves_unsigned_thinking(self)` (method) — On a custom Kimi endpoint, unsigned reasoning_content thinking
