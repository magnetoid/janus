---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_openrouter_response_cache.py

Symbols in `tests/agent/test_openrouter_response_cache.py`.

- L13 `TestBuildOrHeaders` (class) — Test the build_or_headers() helper in agent/auxiliary_client.py.
- L16 `test_base_attribution_always_present(self)` (method) — Attribution headers must always be included regardless of cache setting.
- L25 `test_cache_enabled(self)` (method) — When response_cache is True, X-OpenRouter-Cache header is set.
- L32 `test_cache_disabled(self)` (method) — When response_cache is False, no cache header is sent.
- L40 `test_cache_disabled_by_default_empty_config(self)` (method) — Empty config dict means no cache headers (response_cache defaults to False).
- L47 `test_ttl_default(self)` (method) — Default TTL (300) is included when cache is enabled.
- L54 `test_ttl_custom(self)` (method) — Custom TTL values within range are sent.
- L61 `test_ttl_max(self)` (method) — Maximum TTL (86400) is accepted.
- L68 `test_ttl_out_of_range_too_high(self)` (method) — TTL above 86400 is silently ignored (no TTL header sent).
- L77 `test_ttl_out_of_range_zero(self)` (method) — TTL of 0 is below minimum — no TTL header sent.
- L84 `test_ttl_negative(self)` (method) — Negative TTL is ignored.
- L91 `test_ttl_not_a_number(self)` (method) — Non-numeric TTL is ignored.
- L98 `test_ttl_float_truncated(self)` (method) — Float TTL values are truncated to int.
- L105 `test_returns_fresh_dict(self)` (method) — Each call returns a new dict so mutations don't leak.
- L115 `test_none_config_falls_back_to_load_config(self)` (method) — When or_config is None, build_or_headers reads from load_config().
- L127 `test_none_config_load_config_fails_gracefully(self)` (method) — When load_config() fails, build_or_headers still returns base headers.
- L142 `TestEnvVarOverrides` (class) — Test env var precedence over config.yaml for response caching.
- L145 `test_env_enables_cache(self, monkeypatch)` (method) — HERMES_OPENROUTER_CACHE=true enables cache even when config disables it.
- L153 `test_env_disables_cache(self, monkeypatch)` (method) — HERMES_OPENROUTER_CACHE=false disables cache even when config enables it.
- L162 `test_truthy_values(self, monkeypatch, value)` (method) — Various truthy strings enable caching.
- L171 `test_non_truthy_values(self, monkeypatch, value)` (method) — Non-truthy strings do not enable caching (empty falls through to config).
- L184 `test_env_ttl_overrides_config(self, monkeypatch)` (method) — HERMES_OPENROUTER_CACHE_TTL overrides config TTL.
- L194 `test_invalid_env_ttl_dropped(self, monkeypatch, ttl)` (method) — Invalid TTL env values are ignored; cache still enabled without TTL.
- L205 `test_valid_env_ttl_boundaries(self, monkeypatch, ttl)` (method) — Boundary TTL values (1, 300, 86400) are accepted.
- L213 `test_no_env_vars_falls_through_to_config(self, monkeypatch)` (method) — Without env vars, config.yaml controls behavior.
- L223 `TestDefaultConfig` (class) — Verify the openrouter config section is in DEFAULT_CONFIG.
- L226 `test_openrouter_section_exists(self)` (method)
- L239 `TestCheckOpenrouterCacheStatus` (class) — Test the _check_openrouter_cache_status method on AIAgent.
- L242 `_make_agent(self)` (method) — Create a minimal AIAgent-like object with just the method under test.
- L251 `test_hit_increments_counter(self)` (method)
- L260 `test_miss_does_not_increment(self)` (method)
- L266 `test_no_header_is_noop(self)` (method)
- L272 `test_none_response_is_safe(self)` (method)
- L276 `test_no_headers_attr_is_safe(self)` (method)
- L280 `test_case_insensitive(self)` (method)
