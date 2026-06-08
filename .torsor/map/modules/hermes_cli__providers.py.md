---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/providers.py

Symbols in `hermes_cli/providers.py`.

- L35 `HermesOverlay` (class) — Hermes-specific provider metadata layered on top of models.dev.
- L221 `ProviderDef` (class) — Complete provider definition — merged from all sources.
- L395 `normalize_provider(name: str)` (function) — Resolve aliases and normalise casing to a canonical provider id.
- L405 `get_provider(name: str)` (function) — Look up a built-in provider by id or alias.
- L475 `get_label(provider_id: str)` (function) — Get a human-readable display name for a provider.
- L493 `is_aggregator(provider: str)` (function) — Return True when the provider is a multi-model aggregator.
- L499 `determine_api_mode(provider: str, base_url: str='')` (function) — Determine the API mode (wire protocol) for a provider/endpoint.
- L543 `resolve_user_provider(name: str, user_config: Dict[str, Any])` (function) — Resolve a provider from the user's config.yaml ``providers:`` section.
- L582 `custom_provider_slug(display_name: str)` (function) — Build a canonical slug for a custom_providers entry.
- L592 `resolve_custom_provider(name: str, custom_providers: Optional[List[Dict[str, Any]]])` (function) — Resolve a provider from the user's config.yaml ``custom_providers`` list.
- L661 `resolve_provider_full(name: str, user_providers: Optional[Dict[str, Any]]=None, custom_providers: Optional[List[Dict[str, Any]]]=None)` (function) — Full resolution chain: built-in → models.dev → user config.
