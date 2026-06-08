---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/model_catalog.py

Symbols in `hermes_cli/model_catalog.py`.

- L94 `_load_catalog_config()` (function) — Load the ``model_catalog`` config block with defaults filled in.
- L114 `_cache_path()` (function) — Return the disk cache path. Import lazily so tests can monkeypatch home.
- L125 `_fetch_manifest(url: str, timeout: float)` (function) — HTTP GET the manifest URL and return a parsed dict, or None on failure.
- L151 `_fetch_manifest_with_fallback(primary_url: str, timeout: float, fallback_urls: tuple[str, ...]=DEFAULT_CATALOG_FALLBACK_URLS)` (function) — Try ``primary_url`` first, then walk ``fallback_urls``.
- L176 `_validate_manifest(data: Any)` (function) — Return True when ``data`` matches the minimum manifest shape.
- L202 `_read_disk_cache()` (function) — Return ``(data_or_none, mtime)``. mtime is 0 if file is missing.
- L219 `_write_disk_cache(data: dict[str, Any])` (function)
- L237 `get_catalog(*, force_refresh: bool=False)` (function) — Return the parsed model catalog manifest, or an empty dict on failure.
- L292 `_fetch_provider_override(provider: str)` (function) — If ``model_catalog.providers.<name>.url`` is set, fetch that instead.
- L309 `_get_provider_block(provider: str)` (function) — Return the provider's manifest block, respecting per-provider overrides.
- L324 `get_curated_openrouter_models()` (function) — Return OpenRouter's curated ``[(id, description), ...]`` from the manifest.
- L343 `get_curated_nous_models()` (function) — Return Nous Portal's curated list of model ids from the manifest.
- L359 `reset_cache()` (function) — Clear the in-process cache. Used by tests and ``hermes model --refresh``.
