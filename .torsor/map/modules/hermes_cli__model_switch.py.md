---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/model_switch.py

Symbols in `hermes_cli/model_switch.py`.

- L75 `is_nous_hermes_non_agentic(model_name: str)` (function) — Return True if *model_name* is a real Nous Hermes 3/4 chat model.
- L87 `_check_hermes_model_warning(model_name: str)` (function) — Return a warning string if *model_name* is a Nous Hermes 3/4 chat model.
- L99 `ModelIdentity` (class) — Vendor slug and family prefix used for catalog resolution.
- L165 `DirectAlias` (class) — Exact model mapping that bypasses catalog resolution.
- L179 `_load_direct_aliases()` (function) — Load direct aliases from config.yaml ``model_aliases:`` section.
- L246 `_ensure_direct_aliases()` (function) — Lazy-load direct aliases on first use.
- L263 `ModelSwitchResult` (class) — Result of a model switch attempt.
- L284 `parse_model_flags(raw_args: str)` (function) — Parse --provider, --global, and --refresh flags from /model command args.
- L337 `_model_sort_key(model_id: str, prefix: str)` (function) — Sort key for model version preference.
- L444 `resolve_alias(raw_input: str, current_provider: str)` (function) — Resolve a short alias against the current provider's catalog.
- L521 `get_authenticated_provider_slugs(current_provider: str='', user_providers: dict=None, custom_providers: list | None=None)` (function) — Return slugs of providers that have credentials.
- L543 `_resolve_alias_fallback(raw_input: str, authenticated_providers: list[str]=())` (function) — Try to resolve an alias on the user's authenticated providers.
- L560 `resolve_display_context_length(model: str, provider: str, base_url: str='', api_key: str='', model_info: Optional[ModelInfo]=None, custom_providers: list | None=None, config_context_length: int | None=None)` (function) — Resolve the context length to show in /model output.
- L609 `switch_model(raw_input: str, current_provider: str, current_model: str, current_base_url: str='', current_api_key: str='', is_global: bool=False, explicit_provider: str='', user_providers: dict=None, custom_providers: list | None=None)` (function) — Core model-switching pipeline shared between CLI and gateway.
- L1128 `prewarm_picker_cache_async()` (function) — Warm the provider-models disk cache in a background daemon thread.
- L1176 `list_authenticated_providers(current_provider: str='', current_base_url: str='', user_providers: dict=None, custom_providers: list | None=None, *, force_fresh_nous_tier: bool=False, max_models: int=8, current_model: str='')` (function) — Detect which providers have credentials and list their curated models.
- L1966 `list_picker_providers(current_provider: str='', current_base_url: str='', user_providers: dict=None, custom_providers: list | None=None, max_models: int=8, current_model: str='')` (function) — Interactive-picker variant of :func:`list_authenticated_providers`.
