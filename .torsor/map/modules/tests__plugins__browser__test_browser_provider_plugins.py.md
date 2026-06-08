---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/browser/test_browser_provider_plugins.py

Symbols in `tests/plugins/browser/test_browser_provider_plugins.py`.

- L34 `_clear_browser_env(monkeypatch: pytest.MonkeyPatch)` (function) — Strip every browser-provider env var so is_available() returns False.
- L51 `_ensure_plugins_loaded()` (function) — Idempotently load plugins so the registry is populated.
- L64 `_isolate_env(monkeypatch: pytest.MonkeyPatch)` (function) — Each test starts with a clean browser-provider env.
- L74 `TestBundledPluginsRegister` (class) — All three bundled browser plugins discover and register correctly.
- L77 `test_all_three_plugins_present_in_registry(self)` (method)
- L92 `test_each_plugin_has_name_and_display_name(self, plugin_name: str, expected_display: str)` (method)
- L107 `test_each_plugin_has_setup_schema(self, plugin_name: str)` (method) — ``get_setup_schema()`` returns a dict the picker can consume.
- L126 `test_each_plugin_implements_full_lifecycle(self, plugin_name: str)` (method) — The ABC's three lifecycle methods are all overridden.
- L148 `TestIsAvailable` (class) — Each plugin's ``is_available()`` reflects env-var presence accurately.
- L151 `test_browserbase_requires_both_api_key_and_project_id(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L169 `test_browserbase_project_id_alone_insufficient(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L180 `test_browser_use_satisfied_by_api_key(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L192 `test_firecrawl_requires_api_key(self, monkeypatch: pytest.MonkeyPatch)` (method)
- L208 `TestRegistryResolution` (class) — ``_resolve()`` implements the documented three-rule precedence.
- L211 `test_resolve_none_with_no_creds_returns_none(self)` (method) — No config, no env → local mode (None).
- L218 `test_explicit_local_returns_none(self)` (method) — ``cloud_provider: local`` is a positive choice; short-circuits to None.
- L225 `test_explicit_browserbase_returns_provider_even_when_unavailable(self)` (method) — Rule 1: explicit-config wins even when credentials are missing.
- L239 `test_explicit_firecrawl_returns_provider_even_when_unavailable(self)` (method) — Firecrawl behaves the same as browserbase under explicit config.
- L248 `test_explicit_unknown_falls_back_to_auto_detect(self)` (method) — Rule 1 miss: unknown name → fall through to legacy walk.
- L256 `test_legacy_walk_prefers_browser_use_over_browserbase(self, monkeypatch: pytest.MonkeyPatch)` (method) — Rule 3: walk order is browser-use → browserbase.
- L272 `test_legacy_walk_falls_through_to_browserbase(self, monkeypatch: pytest.MonkeyPatch)` (method) — Rule 3: browser-use unavailable → browserbase picked.
- L286 `test_firecrawl_not_in_legacy_walk_even_when_only_one_available(self, monkeypatch: pytest.MonkeyPatch)` (method) — Regression: firecrawl is NEVER auto-selected even when single-eligible.
- L311 `TestLegacyAbcAliases` (class) — is_configured() and provider_name() delegate to the new API.
- L318 `test_is_configured_delegates_to_is_available(self, plugin_name: str)` (method)
- L334 `test_provider_name_returns_display_name(self, plugin_name: str, expected_label: str)` (method)
- L350 `TestPickerIntegration` (class) — `_plugin_browser_providers()` exposes all three plugins as picker rows.
- L353 `test_picker_rows_match_registered_plugins(self)` (method)
- L361 `test_picker_rows_carry_post_setup_hook(self)` (method) — Every browser plugin row has post_setup='agent_browser' so
- L372 `test_picker_rows_carry_browser_plugin_name_marker(self)` (method) — `browser_plugin_name` matches `browser_provider` so downstream
