---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/web/test_web_search_provider_plugins.py

Symbols in `tests/plugins/web/test_web_search_provider_plugins.py`.

- L32 `_clear_web_env(monkeypatch: pytest.MonkeyPatch)` (function) — Strip every web-provider env var so is_available() returns False.
- L52 `_ensure_plugins_loaded()` (function) — Idempotently load plugins so the registry is populated.
- L65 `_isolate_env(monkeypatch: pytest.MonkeyPatch)` (function) — Each test starts with a clean web-provider env.
- L70 `TestBundledPluginsRegister` (class) — All eight bundled web plugins discover and register correctly.
- L73 `test_all_seven_plugins_present_in_registry(self)` (method)
- L103 `test_capability_flags_match_spec(self, plugin_name: str, expected_search: bool, expected_extract: bool)` (method)
- L121 `test_each_plugin_has_name_and_display_name(self, plugin_name: str)` (method)
- L134 `test_each_plugin_has_setup_schema(self, plugin_name: str)` (method) — ``get_setup_schema()`` returns a dict the picker can consume.
- L152 `TestIsAvailable` (class) — Each plugin's ``is_available()`` returns False without env config.
- L155 `test_brave_free_requires_api_key(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L165 `test_searxng_requires_url(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L175 `test_tavily_requires_api_key(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L185 `test_exa_requires_api_key(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L195 `test_parallel_requires_api_key(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L205 `test_firecrawl_requires_either_key_or_url(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L222 `test_ddgs_always_available_when_package_importable(self)` (method) — DDGS is the always-on fallback — no API key required.
- L238 `test_xai_requires_api_key_or_oauth(self, monkeypatch: pytest.MonkeyPatch)` (method) — xAI needs XAI_API_KEY or OAuth tokens in auth.json.
- L255 `TestRegistryResolution` (class) — ``_resolve()`` follows explicit-config + availability-filtered fallback.
- L258 `test_explicit_configured_provider_returned_even_when_unavailable(self)` (method) — Explicit ``web.search_backend`` wins regardless of is_available().
- L278 `test_unknown_configured_name_falls_back_to_available_provider(self, monkeypatch: pytest.MonkeyPatch)` (method) — Typo / uninstalled plugin → walk legacy preference, pick available.
- L293 `test_explicit_search_only_provider_for_extract_falls_back(self, monkeypatch: pytest.MonkeyPatch)` (method) — Asking for extract via a search-only backend → fall back.
- L313 `test_no_config_no_credentials_returns_none(self)` (method) — No backend configured AND no available providers → typically None.
- L337 `TestAsyncExtractDispatch` (class) — The dispatcher detects async vs sync extract methods correctly.
- L340 `test_parallel_extract_is_async(self)` (method)
- L348 `test_firecrawl_extract_is_async(self)` (method)
- L356 `test_exa_extract_is_sync(self)` (method)
- L364 `test_tavily_extract_is_sync(self)` (method)
- L378 `TestErrorResponseShapes` (class) — When credentials are missing, plugins return typed errors, not raises.
- L381 `test_brave_free_returns_error_dict_when_unconfigured(self)` (method)
- L392 `test_searxng_returns_error_dict_when_unconfigured(self)` (method)
- L403 `test_exa_returns_error_dict_when_unconfigured(self)` (method)
- L414 `test_tavily_returns_error_dict_when_unconfigured(self)` (method)
- L425 `test_parallel_extract_returns_per_url_errors_when_unconfigured(self)` (method)
- L437 `test_firecrawl_extract_returns_per_url_errors_when_unconfigured(self)` (method)
- L452 `test_firecrawl_config_error_points_paid_users_to_nous_subscription(self, monkeypatch)` (method)
- L469 `test_firecrawl_config_error_uses_entitlement_message_when_not_paid(self, monkeypatch)` (method)
- L488 `test_xai_search_returns_error_dict_when_unconfigured(self)` (method) — xAI returns a typed error dict (no XAI_API_KEY).
