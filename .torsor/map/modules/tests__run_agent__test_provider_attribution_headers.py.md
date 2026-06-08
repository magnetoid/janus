---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_provider_attribution_headers.py

Symbols in `tests/run_agent/test_provider_attribution_headers.py`.

- L9 `test_openrouter_base_url_applies_or_headers(mock_openai)` (function)
- L28 `test_routermint_base_url_applies_user_agent_header(mock_openai)` (function)
- L46 `test_nvidia_cloud_base_url_applies_billing_origin_header(mock_openai)` (function)
- L67 `test_nvidia_local_base_url_does_not_apply_billing_origin_header(mock_openai)` (function)
- L88 `test_routed_client_preserves_openai_sdk_custom_headers(mock_openai)` (function)
- L113 `test_gmi_base_url_picks_up_profile_user_agent(mock_openai)` (function) — GMI declares User-Agent on its ProviderProfile.default_headers.
- L138 `test_unknown_base_url_clears_default_headers(mock_openai)` (function)
- L156 `test_openrouter_headers_include_response_cache_when_enabled(mock_openai)` (function) — When openrouter.response_cache is True, the cache header is injected.
- L185 `test_user_default_headers_override_sdk_user_agent(mock_openai)` (function) — ``model.default_headers`` lets a custom endpoint swap the OpenAI SDK
- L210 `test_user_default_headers_win_over_provider_defaults(mock_openai)` (function) — User headers take precedence but leave untouched provider defaults intact.
- L233 `test_no_user_default_headers_leaves_provider_defaults_untouched(mock_openai)` (function)
- L253 `test_user_default_headers_skipped_for_anthropic_mode(mock_openai)` (function) — Anthropic/Bedrock modes don't use the OpenAI client — never touched.
- L277 `test_openrouter_headers_no_cache_when_disabled(mock_openai)` (function) — When openrouter.response_cache is False, no cache headers are sent.
