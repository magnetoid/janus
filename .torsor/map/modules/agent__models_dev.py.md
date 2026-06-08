---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/models_dev.py

Symbols in `agent/models_dev.py`.

- L47 `ModelInfo` (class) — Full metadata for a single model from models.dev.
- L84 `has_cost_data(self)` (method)
- L87 `supports_vision(self)` (method)
- L90 `supports_pdf(self)` (method)
- L93 `supports_audio_input(self)` (method)
- L96 `format_cost(self)` (method) — Human-readable cost string, e.g. '$3.00/M in, $15.00/M out'.
- L105 `format_capabilities(self)` (method) — Human-readable capabilities, e.g. 'reasoning, tools, vision, PDF'.
- L126 `ProviderInfo` (class) — Full metadata for a provider from models.dev.
- L187 `_get_cache_path()` (function) — Return path to disk cache file.
- L193 `_load_disk_cache()` (function) — Load models.dev data from disk cache.
- L205 `_disk_cache_age_seconds()` (function) — Return age (in seconds) of the disk cache file, or None if missing.
- L231 `_save_disk_cache(data: Dict[str, Any])` (function) — Save models.dev data to disk cache atomically.
- L240 `fetch_models_dev(force_refresh: bool=False)` (function) — Fetch models.dev registry. Cache hierarchy: in-mem → disk → network.
- L321 `lookup_models_dev_context(provider: str, model: str)` (function) — Look up context_length for a provider+model combo in models.dev.
- L380 `_extract_context(entry: Dict[str, Any])` (function) — Extract context_length from a models.dev model entry.
- L402 `ModelCapabilities` (class) — Structured capability metadata for a model from models.dev.
- L413 `_get_provider_models(provider: str)` (function) — Resolve a Hermes provider ID to its models dict from models.dev.
- L434 `_find_model_entry(models: Dict[str, Any], model: str)` (function) — Find a model entry by exact match, then case-insensitive fallback.
- L450 `get_model_capabilities(provider: str, model: str)` (function) — Look up full capability metadata from models.dev cache.
- L511 `list_provider_models(provider: str)` (function) — Return all model IDs for a provider from models.dev.
- L567 `_should_hide_from_provider_catalog(provider: str, model_id: str)` (function)
- L575 `list_agentic_models(provider: str)` (function) — Return model IDs suitable for agentic use from models.dev.
- L605 `_parse_model_info(model_id: str, raw: Dict[str, Any], provider_id: str)` (function) — Convert a raw models.dev model entry dict into a ModelInfo dataclass.
- L656 `_parse_provider_info(provider_id: str, raw: Dict[str, Any])` (function) — Convert a raw models.dev provider entry dict into a ProviderInfo.
- L674 `get_provider_info(provider_id: str)` (function) — Get full provider metadata from models.dev.
- L695 `get_model_info(provider_id: str, model_id: str)` (function) — Get full model metadata from models.dev.
