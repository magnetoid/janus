---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_usage_pricing.py

Symbols in `tests/agent/test_usage_pricing.py`.

- L11 `test_normalize_usage_anthropic_keeps_cache_buckets_separate()` (function)
- L28 `test_normalize_usage_openai_subtracts_cached_prompt_tokens()` (function)
- L42 `test_normalize_usage_openai_reads_top_level_anthropic_cache_fields()` (function) — Some OpenAI-compatible proxies (OpenRouter, Cline) expose
- L71 `test_normalize_usage_openai_reads_top_level_cache_read_when_details_missing()` (function) — Some proxies expose only top-level Anthropic-style fields with no
- L89 `test_normalize_usage_openai_prefers_prompt_tokens_details_over_top_level()` (function) — When both prompt_tokens_details and top-level Anthropic fields are
- L109 `test_openrouter_models_api_pricing_is_converted_from_per_token_to_per_million(monkeypatch)` (function)
- L136 `test_estimate_usage_cost_marks_subscription_routes_included()` (function)
- L148 `test_estimate_usage_cost_refuses_cache_pricing_without_official_cache_rate(monkeypatch)` (function)
- L171 `test_custom_endpoint_models_api_pricing_is_supported(monkeypatch)` (function)
- L195 `test_deepseek_v4_pro_pricing_entry_exists()` (function) — Regression test: deepseek-v4-pro must have a pricing entry.
- L215 `test_deepseek_v4_pro_estimate_usage_cost()` (function) — Ensure deepseek-v4-pro sessions get a dollar estimate, not unknown.
