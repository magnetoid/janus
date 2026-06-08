---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_web_providers_searxng.py

Symbols in `tests/tools/test_web_providers_searxng.py`.

- L27 `TestSearXNGSearchProviderIsConfigured` (class)
- L28 `test_configured_when_url_set(self, monkeypatch)` (method)
- L33 `test_not_configured_when_url_missing(self, monkeypatch)` (method)
- L38 `test_not_configured_when_url_empty_string(self, monkeypatch)` (method)
- L43 `test_provider_name(self)` (method)
- L47 `test_implements_web_search_provider(self)` (method)
- L53 `TestSearXNGSearchProviderSearch` (class) — Happy path and error handling for SearXNGWebSearchProvider.search().
- L64 `_make_mock_response(self, json_data, status_code=200)` (method)
- L71 `test_happy_path_returns_normalized_results(self, monkeypatch)` (method)
- L87 `test_results_sorted_by_score_descending(self, monkeypatch)` (method) — Results should be sorted by score before limit is applied.
- L108 `test_limit_is_respected(self, monkeypatch)` (method)
- L119 `test_position_is_one_indexed(self, monkeypatch)` (method)
- L130 `test_empty_results(self, monkeypatch)` (method)
- L141 `test_missing_score_falls_back_to_zero(self, monkeypatch)` (method) — Results without a score field should sort to the bottom.
- L160 `test_http_error_returns_failure(self, monkeypatch)` (method)
- L175 `test_request_error_returns_failure(self, monkeypatch)` (method)
- L186 `test_missing_url_returns_failure(self, monkeypatch)` (method)
- L194 `test_trailing_slash_stripped_from_url(self, monkeypatch)` (method) — Base URL trailing slash should not produce double-slash in endpoint.
- L216 `TestIsBackendAvailable` (class)
- L217 `test_searxng_available_when_url_set(self, monkeypatch)` (method)
- L222 `test_searxng_unavailable_when_url_missing(self, monkeypatch)` (method)
- L227 `test_unknown_backend_still_false(self)` (method)
- L237 `TestGetBackendSearXNG` (class)
- L238 `test_configured_searxng_returns_searxng(self, monkeypatch)` (method)
- L244 `test_auto_detect_picks_searxng_when_only_url_set(self, monkeypatch)` (method) — When no backend is configured but SEARXNG_URL is set, auto-detect returns it.
- L258 `test_searxng_does_not_override_higher_priority_provider(self, monkeypatch)` (method) — Tavily (higher priority than searxng) should win in auto-detect.
- L270 `test_auto_detect_picks_searxng_when_url_only_in_hermes_config(self, monkeypatch)` (method) — #34290 follow-up: a config-only SEARXNG_URL (absent from process env)
- L296 `TestCheckWebApiKey` (class)
- L297 `test_searxng_satisfies_check_web_api_key(self, monkeypatch)` (method)
- L303 `test_searxng_config_only_satisfies_check_web_api_key(self, monkeypatch)` (method) — #34290 follow-up: config-only SEARXNG_URL satisfies the credential check.
- L316 `test_no_credentials_fails(self, monkeypatch)` (method)
- L335 `TestSearXNGOnlyExtractCrawlErrors` (class) — When searxng is the active backend, extract/crawl must return clear errors.
- L341 `_populate_web_registry(self)` (method)
- L347 `test_web_extract_searxng_returns_clear_error(self, monkeypatch)` (method)
