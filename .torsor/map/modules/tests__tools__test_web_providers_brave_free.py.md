---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_web_providers_brave_free.py

Symbols in `tests/tools/test_web_providers_brave_free.py`.

- L28 `TestBraveFreeProviderIsConfigured` (class)
- L29 `test_configured_when_key_set(self, monkeypatch)` (method)
- L34 `test_not_configured_when_key_missing(self, monkeypatch)` (method)
- L39 `test_not_configured_when_key_whitespace(self, monkeypatch)` (method)
- L44 `test_provider_name(self)` (method)
- L48 `test_implements_web_search_provider(self)` (method)
- L54 `TestBraveFreeProviderSearch` (class)
- L66 `_mock_resp(json_data, status_code=200)` (method)
- L73 `test_happy_path_normalizes_results(self, monkeypatch)` (method)
- L86 `test_sends_subscription_token_header_and_count(self, monkeypatch)` (method) — Brave uses X-Subscription-Token; count maps from limit.
- L107 `test_count_is_capped_at_20(self, monkeypatch)` (method) — Brave caps count at 20 — limit above that clamps.
- L123 `test_limit_is_respected_client_side(self, monkeypatch)` (method)
- L133 `test_empty_results(self, monkeypatch)` (method)
- L143 `test_missing_web_key_returns_empty(self, monkeypatch)` (method) — Responses without a ``web`` block should produce an empty result set, not crash.
- L154 `test_http_error_returns_failure(self, monkeypatch)` (method)
- L169 `test_request_error_returns_failure(self, monkeypatch)` (method)
- L180 `test_missing_key_returns_failure(self, monkeypatch)` (method)
- L194 `TestBraveFreeBackendWiring` (class)
- L195 `test_is_backend_available_true_when_key_set(self, monkeypatch)` (method)
- L200 `test_is_backend_available_false_when_key_missing(self, monkeypatch)` (method)
- L205 `test_configured_backend_accepted(self, monkeypatch)` (method)
- L211 `test_auto_detect_picks_brave_free_when_only_key_set(self, monkeypatch)` (method)
- L222 `test_brave_free_does_not_override_paid_provider(self, monkeypatch)` (method) — Tavily (higher priority) should win in auto-detect.
- L233 `test_check_web_api_key_true_when_brave_free_configured(self, monkeypatch)` (method)
- L245 `TestBraveFreeSearchOnlyErrors` (class)
- L249 `_populate_web_registry(self)` (method)
- L255 `test_web_extract_returns_search_only_error(self, monkeypatch)` (method)
