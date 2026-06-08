---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_web_tools_config.py

Symbols in `tests/tools/test_web_tools_config.py`.

- L20 `TestFirecrawlClientConfig` (class) — Test suite for Firecrawl client initialization.
- L23 `setup_method(self)` (method) — Reset client and env vars before each test.
- L47 `teardown_method(self)` (method) — Reset client after each test.
- L66 `test_no_config_raises_with_helpful_message(self)` (method) — Neither key nor URL → ValueError with guidance.
- L74 `test_tool_gateway_domain_builds_firecrawl_gateway_origin(self)` (method) — Shared gateway domain should derive the Firecrawl vendor hostname.
- L87 `test_tool_gateway_scheme_can_switch_derived_gateway_origin_to_http(self)` (method) — Shared gateway scheme should allow local plain-http vendor hosts.
- L103 `test_invalid_tool_gateway_scheme_raises(self)` (method) — Unexpected shared gateway schemes should fail fast.
- L114 `test_explicit_firecrawl_gateway_url_takes_precedence(self)` (method) — An explicit Firecrawl gateway origin should override the shared domain.
- L129 `test_default_gateway_domain_targets_nous_production_origin(self)` (method) — Default gateway origin should point at the Firecrawl vendor hostname.
- L140 `test_nous_auth_token_respects_hermes_home_override(self, tmp_path)` (method) — Auth lookup should read from HERMES_HOME/auth.json, not ~/.hermes/auth.json.
- L163 `test_check_auxiliary_model_re_resolves_backend_each_call(self)` (method) — Availability checks should not be pinned to module import state.
- L178 `test_summarizer_re_resolves_backend_after_initial_unavailable_state(self)` (method) — Summarization should pick up a backend that becomes available later in-process.
- L206 `test_singleton_returns_same_instance(self)` (method) — Second call returns cached client without re-constructing.
- L216 `test_constructor_failure_allows_retry(self)` (method) — If Firecrawl() raises, next call should retry (not return None).
- L234 `test_empty_string_key_no_url_raises(self)` (method) — FIRECRAWL_API_KEY='' with no URL → should raise.
- L244 `TestBackendSelection` (class) — Test suite for _get_backend() backend selection logic.
- L264 `setup_method(self)` (method)
- L274 `teardown_method(self)` (method)
- L282 `test_config_parallel(self)` (method) — web.backend=parallel in config → 'parallel' regardless of keys.
- L288 `test_config_exa(self)` (method) — web.backend=exa in config → 'exa' regardless of other keys.
- L295 `test_config_firecrawl(self)` (method) — web.backend=firecrawl in config → 'firecrawl' even if Parallel key set.
- L302 `test_config_tavily(self)` (method) — web.backend=tavily in config → 'tavily' regardless of other keys.
- L308 `test_config_tavily_overrides_env_keys(self)` (method) — web.backend=tavily in config → 'tavily' even if Firecrawl key set.
- L315 `test_config_case_insensitive(self)` (method) — web.backend=Parallel (mixed case) → 'parallel'.
- L321 `test_config_tavily_case_insensitive(self)` (method) — web.backend=Tavily (mixed case) → 'tavily'.
- L329 `test_fallback_parallel_only_key(self)` (method) — Only PARALLEL_API_KEY set → 'parallel'.
- L336 `test_fallback_exa_only_key(self)` (method) — Only EXA_API_KEY set → 'exa'.
- L343 `test_fallback_parallel_takes_priority_over_exa(self)` (method) — Exa should only win the fallback path when it is the only configured backend.
- L350 `test_fallback_tavily_only_key(self)` (method) — Only TAVILY_API_KEY set → 'tavily'.
- L357 `test_fallback_tavily_with_firecrawl_prefers_firecrawl(self)` (method) — Tavily + Firecrawl keys, no config → 'firecrawl' (backward compat).
- L364 `test_fallback_tavily_with_parallel_prefers_parallel(self)` (method) — Tavily + Parallel keys, no config → 'parallel' (Parallel takes priority over Tavily).
- L372 `test_fallback_both_keys_defaults_to_firecrawl(self)` (method) — Both keys set, no config → 'firecrawl' (backward compat).
- L379 `test_fallback_firecrawl_only_key(self)` (method) — Only FIRECRAWL_API_KEY set → 'firecrawl'.
- L386 `test_fallback_no_keys_defaults_to_firecrawl(self)` (method) — No keys, no config → 'firecrawl' (will fail at client init).
- L392 `test_invalid_config_falls_through_to_fallback(self)` (method) — web.backend=invalid → ignored, uses key-based fallback.
- L400 `TestParallelClientConfig` (class) — Test suite for Parallel client initialization.
- L403 `setup_method(self)` (method)
- L421 `teardown_method(self)` (method)
- L427 `test_creates_client_with_key(self)` (method) — PARALLEL_API_KEY set → creates Parallel client.
- L436 `test_no_key_raises_with_helpful_message(self)` (method) — No PARALLEL_API_KEY → ValueError with guidance.
- L442 `test_singleton_returns_same_instance(self)` (method) — Second call returns cached client.
- L451 `TestWebSearchSchema` (class) — Test suite for web_search tool schema and handler wiring.
- L454 `test_schema_exposes_optional_limit(self)` (method)
- L465 `test_registered_handler_passes_limit(self)` (method)
- L475 `test_registered_handler_defaults_limit_to_five(self)` (method)
- L485 `test_web_search_clamps_limit_before_backend_call(self)` (method)
- L512 `TestWebSearchErrorHandling` (class) — Test suite for web_search_tool() error responses.
- L515 `test_search_error_response_does_not_expose_diagnostics(self)` (method)
- L548 `TestCheckWebApiKey` (class) — Test suite for check_web_api_key() unified availability check.
- L563 `setup_method(self)` (method)
- L573 `teardown_method(self)` (method)
- L579 `test_parallel_key_only(self)` (method)
- L584 `test_exa_key_only(self)` (method)
- L589 `test_firecrawl_key_only(self)` (method)
- L594 `test_firecrawl_url_only(self)` (method)
- L599 `test_tavily_key_only(self)` (method)
- L604 `test_no_keys_returns_false(self)` (method)
- L608 `test_both_keys_returns_true(self)` (method)
- L616 `test_all_three_keys_returns_true(self)` (method)
- L625 `test_tool_gateway_returns_true(self)` (method)
- L630 `test_tool_gateway_availability_skips_refresh_for_expired_cached_token(self, tmp_path, monkeypatch)` (method)
- L669 `test_configured_backend_must_match_available_provider(self)` (method)
- L676 `test_configured_firecrawl_backend_accepts_managed_gateway(self)` (method)
- L684 `test_web_requires_env_includes_exa_key()` (function)
