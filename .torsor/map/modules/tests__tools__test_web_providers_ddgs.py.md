---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_web_providers_ddgs.py

Symbols in `tests/tools/test_web_providers_ddgs.py`.

- L21 `_install_fake_ddgs(monkeypatch, *, text_results=None, text_raises=None)` (function) — Install a stub ``ddgs`` module in sys.modules for the duration of a test.
- L50 `TestDDGSProviderIsConfigured` (class)
- L51 `test_configured_when_package_importable(self, monkeypatch)` (method)
- L58 `test_not_configured_when_package_missing(self, monkeypatch)` (method)
- L74 `test_provider_name(self)` (method)
- L78 `test_implements_web_search_provider(self)` (method)
- L84 `TestDDGSProviderSearch` (class)
- L85 `test_happy_path_normalizes_results(self, monkeypatch)` (method)
- L101 `test_accepts_url_key_as_fallback_for_href(self, monkeypatch)` (method)
- L112 `test_limit_is_respected(self, monkeypatch)` (method)
- L124 `test_missing_package_returns_failure(self, monkeypatch)` (method)
- L142 `test_runtime_error_returns_failure(self, monkeypatch)` (method)
- L150 `test_empty_results(self, monkeypatch)` (method)
- L164 `TestDDGSBackendWiring` (class)
- L165 `test_is_backend_available_true_when_package_importable(self, monkeypatch)` (method)
- L170 `test_is_backend_available_false_when_package_missing(self, monkeypatch)` (method)
- L175 `test_configured_backend_accepted(self, monkeypatch)` (method)
- L181 `test_ddgs_trails_paid_providers_in_auto_detect(self, monkeypatch)` (method) — Exa (priority) should win over ddgs in auto-detect.
- L193 `test_auto_detect_picks_ddgs_as_last_resort(self, monkeypatch)` (method)
- L203 `test_check_web_api_key_true_when_ddgs_configured(self, monkeypatch)` (method)
- L215 `TestDDGSSearchOnlyErrors` (class)
- L219 `_populate_web_registry(self)` (method)
- L225 `test_web_extract_returns_search_only_error(self, monkeypatch)` (method)
