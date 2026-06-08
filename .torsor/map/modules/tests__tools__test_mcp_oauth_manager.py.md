---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_oauth_manager.py

Symbols in `tests/tools/test_mcp_oauth_manager.py`.

- L19 `test_manager_is_singleton()` (function) — get_manager() returns the same instance across calls.
- L28 `test_manager_get_or_build_provider_caches(tmp_path, monkeypatch)` (function) — Calling get_or_build_provider twice with same name returns same provider.
- L39 `test_manager_get_or_build_rebuilds_on_url_change(tmp_path, monkeypatch)` (function) — Changing the URL discards the cached provider.
- L50 `test_manager_remove_evicts_cache(tmp_path, monkeypatch)` (function) — remove(name) evicts the provider from cache AND deletes disk files.
- L75 `test_hermes_provider_subclass_exists()` (function) — HermesMCPOAuthProvider is defined and subclasses OAuthClientProvider.
- L85 `test_disk_watch_invalidates_on_mtime_change(tmp_path, monkeypatch)` (function) — When the tokens file mtime changes, provider._initialized flips False.
- L127 `test_manager_builds_hermes_provider_subclass(tmp_path, monkeypatch)` (function) — get_or_build_provider returns HermesMCPOAuthProvider, not plain OAuthClientProvider.
