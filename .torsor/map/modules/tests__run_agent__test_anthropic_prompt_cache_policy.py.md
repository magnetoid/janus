---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_anthropic_prompt_cache_policy.py

Symbols in `tests/run_agent/test_anthropic_prompt_cache_policy.py`.

- L16 `_make_agent(*, provider: str='openrouter', base_url: str='https://openrouter.ai/api/v1', api_mode: str='chat_completions', model: str='anthropic/claude-sonnet-4.6')` (function)
- L34 `TestNativeAnthropic` (class)
- L35 `test_claude_on_native_anthropic_caches_with_native_layout(self)` (method)
- L44 `test_api_anthropic_host_detected_even_when_provider_label_differs(self)` (method)
- L56 `TestOpenRouter` (class)
- L57 `test_claude_on_openrouter_caches_with_envelope_layout(self)` (method)
- L68 `test_non_claude_on_openrouter_does_not_cache(self)` (method)
- L78 `TestThirdPartyAnthropicGateway` (class) — Third-party gateways speaking the Anthropic protocol (MiniMax, Zhipu GLM, LiteLLM).
- L81 `test_minimax_claude_via_anthropic_messages(self)` (method)
- L92 `test_third_party_anthropic_non_claude_unknown_provider_does_not_cache(self)` (method)
- L105 `TestMiniMaxAnthropicWire` (class) — MiniMax's own model family on its Anthropic-compatible endpoint.
- L114 `test_minimax_m27_on_provider_minimax_caches_native_layout(self)` (method)
- L123 `test_minimax_m25_on_provider_minimax_cn_caches_native_layout(self)` (method)
- L132 `test_custom_provider_pointed_at_minimax_host_caches(self)` (method)
- L143 `test_minimax_host_china_endpoint_caches(self)` (method)
- L152 `test_minimax_provider_on_openai_wire_does_not_cache(self)` (method)
- L164 `TestOpenAIWireFormatOnCustomProvider` (class) — A custom provider using chat_completions (OpenAI wire) should NOT get caching.
- L167 `test_custom_openai_wire_does_not_cache_even_with_claude_name(self)` (method)
- L181 `TestQwenAlibabaFamily` (class) — Qwen on OpenCode/OpenCode-Go/Alibaba — needs cache_control even on OpenAI-wire.
- L191 `test_qwen_on_opencode_go_caches_with_envelope_layout(self)` (method)
- L202 `test_qwen35_plus_on_opencode_go(self)` (method)
- L211 `test_qwen_on_opencode_zen_caches(self)` (method)
- L220 `test_qwen_on_direct_alibaba_caches(self)` (method)
- L229 `test_non_qwen_on_opencode_go_does_not_cache(self)` (method)
- L240 `test_kimi_on_opencode_go_does_not_cache(self)` (method)
- L249 `test_qwen_on_openrouter_not_affected(self)` (method)
- L260 `test_qwen_on_nous_portal_caches_with_envelope_layout(self)` (method)
- L273 `test_qwen_vendored_slug_on_nous_portal_caches(self)` (method)
- L283 `test_non_qwen_non_claude_on_nous_portal_does_not_cache(self)` (method)
- L295 `TestExplicitOverrides` (class) — Policy accepts keyword overrides for switch_model / fallback activation.
- L298 `test_overrides_take_precedence_over_self(self)` (method)
- L312 `test_fallback_target_evaluated_independently(self)` (method)
