---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_web_providers.py

Symbols in `tests/tools/test_web_providers.py`.

- L24 `TestWebProviderABCs` (class) — The unified WebSearchProvider ABC enforces the interface contract.
- L35 `test_cannot_instantiate_abc_directly(self)` (method)
- L41 `test_concrete_search_only_provider_works(self)` (method)
- L70 `test_concrete_multi_capability_provider_works(self)` (method)
- L102 `test_search_only_provider_skips_extract(self)` (method) — Search-only providers don't have to implement extract().
- L137 `TestPerCapabilityBackendSelection` (class) — _get_search_backend and _get_extract_backend read per-capability config.
- L140 `test_search_backend_overrides_generic(self, monkeypatch)` (method)
- L150 `test_extract_backend_overrides_generic(self, monkeypatch)` (method)
- L160 `test_falls_back_to_generic_backend_when_search_backend_empty(self, monkeypatch)` (method)
- L170 `test_falls_back_to_generic_backend_when_extract_backend_empty(self, monkeypatch)` (method)
- L180 `test_search_backend_ignored_when_not_available(self, monkeypatch)` (method)
- L192 `test_fully_backward_compatible_with_web_backend_only(self, monkeypatch)` (method)
- L209 `TestDefaultConfig` (class) — The web section exists in DEFAULT_CONFIG with per-capability keys.
- L212 `test_web_section_in_default_config(self)` (method)
- L231 `TestWebSearchUsesSearchBackend` (class) — web_search_tool dispatches through _get_search_backend not _get_backend.
- L234 `test_search_tool_calls_search_backend(self, monkeypatch)` (method)
- L260 `TestUnconfiguredErrorEnvelopeParity` (class) — Regression tests for PR #25182: the post-migration dispatcher must
- L274 `_populate_web_registry(self)` (method)
- L280 `_clear_web_creds(self, monkeypatch)` (method)
- L294 `test_unconfigured_search_emits_top_level_error(self, monkeypatch)` (method) — ``web_search_tool`` with no creds returns ``{"error": "Error searching web: ..."}``
- L315 `TestDispatchersTriggerPluginDiscovery` (class) — Regression tests for #27580: each web_*_tool dispatcher must
- L332 `_clear_registry(self)` (method) — Reset the web_search registry to empty and return a callback
- L349 `test_web_extract_tool_runs_discovery_before_registry_lookup(self, monkeypatch)` (method) — ``web_extract_tool`` must invoke ``_ensure_web_plugins_loaded()``
- L437 `test_web_search_tool_runs_discovery_before_registry_lookup(self, monkeypatch)` (method) — ``web_search_tool`` must invoke ``_ensure_web_plugins_loaded()``
