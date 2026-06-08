---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/models.py

Symbols in `hermes_cli/models.py`.

- L86 `_codex_curated_models()` (function) — Derive the openai-codex curated list from codex_models.py.
- L118 `_xai_promote_top(ids: list[str])` (function) — Pin the headline xAI model to the top of the curated list.
- L125 `_xai_curated_models()` (function) — Derive the xAI-direct curated list from models.dev disk cache.
- L502 `_is_model_free(model_id: str, pricing: dict[str, dict[str, str]])` (function) — Return True if *model_id* has zero-cost prompt AND completion pricing.
- L516 `is_nous_free_tier(account_info: dict[str, Any])` (function) — Return True if the account info indicates a free (unpaid) tier.
- L544 `partition_nous_models_by_tier(model_ids: list[str], pricing: dict[str, dict[str, str]], free_tier: bool)` (function) — Split Nous models into (selectable, unavailable) based on user tier.
- L572 `union_with_portal_free_recommendations(curated_ids: list[str], pricing: dict[str, dict[str, str]], portal_base_url: str='', *, force_refresh: bool=False)` (function) — Augment curated list + pricing with the Portal's ``freeRecommendedModels``.
- L638 `union_with_portal_paid_recommendations(curated_ids: list[str], pricing: dict[str, dict[str, str]], portal_base_url: str='', *, force_refresh: bool=False)` (function) — Augment curated list with the Portal's ``paidRecommendedModels``.
- L712 `check_nous_free_tier(*, force_fresh: bool=False)` (function) — Check if the current Nous Portal user is on a free (unpaid) tier.
- L767 `fetch_nous_recommended_models(portal_base_url: str='', timeout: float=5.0, *, force_refresh: bool=False)` (function) — Fetch the Nous Portal's curated recommended-models payload.
- L809 `_resolve_nous_portal_url()` (function) — Best-effort lookup of the Portal base URL the user is authed against.
- L825 `_extract_model_name(entry: Any)` (function) — Pull the ``modelName`` field from a recommended-model entry, else None.
- L835 `get_nous_recommended_aux_model(*, vision: bool=False, free_tier: Optional[bool]=None, portal_base_url: str='', force_refresh: bool=False)` (function) — Return the Portal's recommended model name for an auxiliary task.
- L903 `ProviderEntry` (class)
- L1008 `provider_group_for_slug(slug: str)` (function) — Return the group_id a provider slug belongs to, or "" if ungrouped.
- L1013 `group_providers(slugs)` (function) — Fold a flat ordered slug iterable into picker rows by provider group.
- L1174 `get_default_model_for_provider(provider: str)` (function) — Return a cost-safe default model for a provider, or "" if unknown.
- L1196 `_openrouter_model_is_free(pricing: Any)` (function) — Return True when both prompt and completion pricing are zero.
- L1206 `_openrouter_model_supports_tools(item: Any)` (function) — Return True when the model's ``supported_parameters`` advertise tool calling.
- L1231 `fetch_openrouter_models(timeout: float=8.0, *, force_refresh: bool=False)` (function) — Return the curated OpenRouter picker list, refreshed from the live catalog when possible.
- L1299 `model_ids(*, force_refresh: bool=False)` (function) — Return just the OpenRouter model-id strings.
- L1304 `get_curated_nous_model_ids()` (function) — Return the curated Nous Portal model-id list.
- L1330 `_format_price_per_mtok(per_token_str: str)` (function) — Convert a per-token price string to a human-friendly $/Mtok string.
- L1354 `fetch_models_with_pricing(api_key: str | None=None, base_url: str='https://openrouter.ai/api', timeout: float=8.0, *, force_refresh: bool=False)` (function) — Fetch ``/v1/models`` and return ``{model_id: {prompt, completion}}`` pricing.
- L1405 `_resolve_openrouter_api_key()` (function) — Best-effort OpenRouter API key for pricing fetch.
- L1413 `_resolve_nous_pricing_credentials()` (function) — Return ``(api_key, base_url)`` for Nous Portal pricing.
- L1435 `get_pricing_for_provider(provider: str, *, force_refresh: bool=False)` (function) — Return live pricing for providers that support it (openrouter, nous, novita).
- L1462 `_fetch_novita_pricing(timeout: float=8.0, *, force_refresh: bool=False)` (function) — Fetch pricing from NovitaAI /v1/models.
- L1528 `list_available_providers()` (function) — Return info about all providers the user could use with ``provider:model``.
- L1572 `parse_model_input(raw: str, current_provider: str)` (function) — Parse ``/model`` input into ``(provider, model)``.
- L1608 `_get_custom_base_url()` (function) — Get the custom endpoint base_url from config.yaml.
- L1621 `curated_models_for_provider(provider: Optional[str], *, force_refresh: bool=False)` (function) — Return ``(model_id, description)`` tuples for a provider's model list.
- L1646 `_provider_keys(provider: str)` (function)
- L1652 `_model_in_provider_catalog(name_lower: str, providers: set[str])` (function)
- L1665 `_resolve_static_model_alias(name_lower: str, current_keys: set[str])` (function) — Resolve short aliases (e.g. sonnet/opus) using static catalogs only.
- L1713 `detect_static_provider_for_model(model_name: str, current_provider: str)` (function) — Auto-detect a provider from static catalogs only.
- L1764 `detect_provider_for_model(model_name: str, current_provider: str)` (function) — Auto-detect the best provider for a model name.
- L1803 `_find_openrouter_slug(model_name: str)` (function) — Find the full OpenRouter model slug for a bare or partial model name.
- L1830 `normalize_provider(provider: Optional[str])` (function) — Normalize provider aliases to Hermes' canonical provider ids.
- L1841 `provider_label(provider: Optional[str])` (function) — Return a human-friendly label for a provider id or alias.
- L1868 `_is_openai_fast_model(model_id: Optional[str])` (function) — Return True if the model is an OpenAI flagship eligible for Priority Processing.
- L1890 `_strip_vendor_prefix(model_id: str)` (function) — Strip vendor/ prefix from a model ID (e.g. 'anthropic/claude-opus-4-6' -> 'claude-opus-4-6').
- L1898 `model_supports_fast_mode(model_id: Optional[str])` (function) — Return whether Hermes should expose the /fast toggle for this model.
- L1903 `_is_anthropic_fast_model(model_id: Optional[str])` (function) — Return True if the model accepts the Anthropic Fast Mode ``speed`` param.
- L1922 `resolve_fast_mode_overrides(model_id: Optional[str])` (function) — Return request_overrides for fast/priority mode, or None if unsupported.
- L1940 `_resolve_copilot_catalog_api_key()` (function) — Best-effort GitHub token for fetching the Copilot model catalog.
- L2031 `_merge_with_models_dev(provider: str, curated: list[str])` (function) — Merge curated list with fresh models.dev entries for a preferred provider.
- L2068 `provider_model_ids(provider: Optional[str], *, force_refresh: bool=False)` (function) — Return the best known model catalog for a provider.
- L2274 `_provider_models_cache_path()` (function)
- L2279 `_credential_fingerprint(provider: str)` (function) — Return a short hash representing the credentials that
- L2350 `_load_provider_models_cache()` (function) — Return the full cache dict, or {} on any error.
- L2363 `_save_provider_models_cache(data: dict)` (function) — Persist the cache dict. Best-effort — silent on any error.
- L2374 `cached_provider_model_ids(provider: Optional[str], *, force_refresh: bool=False, ttl_seconds: int=_PROVIDER_MODELS_CACHE_TTL)` (function) — Disk-cached wrapper around :func:`provider_model_ids`.
- L2428 `clear_provider_models_cache(provider: Optional[str]=None)` (function) — Drop a single provider's cache entry, or wipe the whole cache.
- L2450 `_fetch_anthropic_models(timeout: float=5.0)` (function) — Fetch available models from the Anthropic /v1/models endpoint.
- L2522 `_payload_items(payload: Any)` (function)
- L2532 `copilot_default_headers()` (function) — Standard headers for Copilot API requests.
- L2550 `_copilot_catalog_item_is_text_model(item: dict[str, Any])` (function)
- L2579 `fetch_github_model_catalog(api_key: Optional[str]=None, timeout: float=5.0)` (function) — Fetch the live GitHub Copilot model catalog for this account.
- L2622 `get_copilot_model_context(model_id: str, api_key: Optional[str]=None)` (function) — Look up max_prompt_tokens for a Copilot model from the live /models API.
- L2659 `_is_github_models_base_url(base_url: Optional[str])` (function)
- L2668 `_lmstudio_server_root(base_url: Optional[str])` (function) — Strip ``/v1`` suffix from an LM Studio base URL to get the native API root.
- L2679 `_lmstudio_request_headers(api_key: Optional[str]=None)` (function) — Build HTTP headers for LM Studio native API requests.
- L2688 `_lmstudio_fetch_raw_models(api_key: Optional[str]=None, base_url: Optional[str]=None, timeout: float=5.0)` (function) — Fetch the raw model list from LM Studio's ``/api/v1/models``.
- L2738 `probe_lmstudio_models(api_key: Optional[str]=None, base_url: Optional[str]=None, timeout: float=5.0)` (function) — Probe LM Studio's model listing.
- L2769 `fetch_lmstudio_models(api_key: Optional[str]=None, base_url: Optional[str]=None, timeout: float=5.0)` (function) — Fetch LM Studio chat-capable model keys from native ``/api/v1/models``.
- L2788 `ensure_lmstudio_model_loaded(model: str, base_url: Optional[str], api_key: Optional[str], target_context_length: int, timeout: float=120.0)` (function) — Ensure LM Studio has ``model`` loaded with at least ``target_context_length``.
- L2857 `lmstudio_model_reasoning_options(model: str, base_url: Optional[str], api_key: Optional[str]=None, timeout: float=5.0)` (function) — Return the reasoning ``allowed_options`` LM Studio publishes for ``model``.
- L2890 `_fetch_github_models(api_key: Optional[str]=None, timeout: float=5.0)` (function)
- L2936 `_copilot_catalog_ids(catalog: Optional[list[dict[str, Any]]]=None, api_key: Optional[str]=None)` (function)
- L2951 `normalize_copilot_model_id(model_id: Optional[str], *, catalog: Optional[list[dict[str, Any]]]=None, api_key: Optional[str]=None)` (function)
- L2992 `_github_reasoning_efforts_for_model_id(model_id: str)` (function)
- L3002 `_should_use_copilot_responses_api(model_id: str)` (function) — Decide whether a Copilot model should use the Responses API.
- L3019 `copilot_model_api_mode(model_id: Optional[str], *, catalog: Optional[list[dict[str, Any]]]=None, api_key: Optional[str]=None)` (function) — Determine the API mode for a Copilot model.
- L3077 `azure_foundry_model_api_mode(model_name: Optional[str])` (function) — Infer Azure Foundry api_mode from a deployment/model name.
- L3106 `normalize_opencode_model_id(provider_id: Optional[str], model_id: Optional[str])` (function) — Normalize OpenCode config IDs to the bare model slug used in API requests.
- L3119 `opencode_model_api_mode(provider_id: Optional[str], model_id: Optional[str])` (function) — Determine the API mode for an OpenCode Zen / Go model.
- L3155 `github_model_reasoning_efforts(model_id: Optional[str], *, catalog: Optional[list[dict[str, Any]]]=None, api_key: Optional[str]=None)` (function) — Return supported reasoning-effort levels for a Copilot-visible model.
- L3199 `probe_api_models(api_key: Optional[str], base_url: Optional[str], timeout: float=5.0, api_mode: Optional[str]=None)` (function) — Probe a ``/models`` endpoint with light URL heuristics.
- L3277 `fetch_api_models(api_key: Optional[str], base_url: Optional[str], timeout: float=5.0, api_mode: Optional[str]=None)` (function) — Fetch the list of available model IDs from the provider's ``/models`` endpoint.
- L3300 `_strip_ollama_cloud_suffix(model_id: str)` (function) — Strip :cloud / -cloud suffixes that models.dev appends to Ollama Cloud IDs.
- L3313 `_ollama_cloud_cache_path()` (function) — Return the path for the Ollama Cloud model cache.
- L3319 `_load_ollama_cloud_cache(*, ignore_ttl: bool=False)` (function) — Load cached Ollama Cloud models from disk.
- L3346 `_save_ollama_cloud_cache(models: list[str])` (function) — Persist the merged Ollama Cloud model list to disk.
- L3357 `fetch_ollama_cloud_models(api_key: Optional[str]=None, base_url: Optional[str]=None, *, force_refresh: bool=False)` (function) — Fetch Ollama Cloud models by merging live API + models.dev, with disk cache.
- L3424 `validate_requested_model(model_name: str, provider: Optional[str], *, api_key: Optional[str]=None, base_url: Optional[str]=None, api_mode: Optional[str]=None)` (function) — Validate a ``/model`` value for the active provider.
