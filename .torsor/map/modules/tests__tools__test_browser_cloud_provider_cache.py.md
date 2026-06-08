---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_cloud_provider_cache.py

Symbols in `tests/tools/test_browser_cloud_provider_cache.py`.

- L21 `_reset_resolver_state(monkeypatch)` (function)
- L27 `TestCloudProviderCachePolicy` (class)
- L28 `test_explicit_local_caches_permanently(self, monkeypatch)` (method) — `cloud_provider: local` is a positive choice and must stick.
- L45 `test_successful_cloud_resolution_caches_permanently(self, monkeypatch)` (method) — A real provider instance must be cached and reused.
- L64 `test_no_credentials_yet_does_not_cache_none(self, monkeypatch)` (method) — Auto-detect path with no creds: must NOT poison the cache.
- L93 `test_config_read_failure_does_not_cache_none(self, monkeypatch)` (method) — A raised config read must not pin the resolver to local mode.
- L103 `test_explicit_provider_instantiation_failure_does_not_cache(self, monkeypatch, caplog)` (method) — If `_PROVIDER_REGISTRY[key]()` raises, log warning and don't cache.
