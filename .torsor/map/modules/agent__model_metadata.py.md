---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/model_metadata.py

Symbols in `agent/model_metadata.py`.

- L26 `_resolve_requests_verify()` (function) — Resolve SSL verify setting for `requests` calls from env vars.
- L86 `_strip_provider_prefix(model: str)` (function) — Strip a recognised provider prefix from a model string.
- L277 `grok_supports_reasoning_effort(model: str)` (function) — Return True when an xAI Grok model accepts ``reasoning.effort``.
- L326 `_normalize_base_url(base_url: str)` (function)
- L330 `_auth_headers(api_key: str='')` (function)
- L337 `_is_openrouter_base_url(base_url: str)` (function)
- L341 `_is_custom_endpoint(base_url: str)` (function)
- L398 `_infer_provider_from_url(base_url: str)` (function) — Infer the models.dev provider name from a base URL.
- L416 `_is_known_provider_base_url(base_url: str)` (function)
- L420 `is_local_endpoint(base_url: str)` (function) — Return True if base_url points to a local machine.
- L476 `detect_local_server_type(base_url: str, api_key: str='')` (function) — Detect which local server is running at base_url by probing known endpoints.
- L537 `_iter_nested_dicts(value: Any)` (function)
- L547 `_coerce_reasonable_int(value: Any, minimum: int=1024, maximum: int=10000000)` (function)
- L561 `_extract_first_int(payload: Dict[str, Any], keys: tuple[str, ...])` (function)
- L573 `_extract_context_length(payload: Dict[str, Any])` (function)
- L577 `_extract_max_completion_tokens(payload: Dict[str, Any])` (function)
- L581 `_extract_pricing(payload: Dict[str, Any])` (function)
- L614 `_add_model_aliases(cache: Dict[str, Dict[str, Any]], model_id: str, entry: Dict[str, Any])` (function)
- L621 `fetch_model_metadata(force_refresh: bool=False)` (function) — Fetch model metadata from OpenRouter (cached for 1 hour).
- L657 `fetch_endpoint_model_metadata(base_url: str, api_key: str='', force_refresh: bool=False)` (function) — Fetch model metadata from an OpenAI-compatible ``/models`` endpoint.
- L801 `_resolve_endpoint_context_length(model: str, base_url: str, api_key: str='')` (function) — Resolve context length from an endpoint's live ``/models`` metadata.
- L824 `_get_context_cache_path()` (function) — Return path to the persistent context length cache file.
- L830 `_load_context_cache()` (function) — Load the model+provider -> context_length cache from disk.
- L844 `save_context_length(model: str, base_url: str, length: int)` (function) — Persist a discovered context length for a model+provider combo.
- L865 `get_cached_context_length(model: str, base_url: str)` (function) — Look up a previously discovered context length for model+provider.
- L872 `_invalidate_cached_context_length(model: str, base_url: str)` (function) — Drop a stale cache entry so it gets re-resolved on the next lookup.
- L888 `get_next_probe_tier(current_length: int)` (function) — Return the next lower probe tier, or None if already at minimum.
- L896 `parse_context_limit_from_error(error_msg: str)` (function) — Try to extract the actual context limit from an API error message.
- L924 `get_context_length_from_provider_error(error_msg: str, current_context_length: int)` (function) — Return a provider-reported lower context limit, if one is present.
- L944 `parse_available_output_tokens_from_error(error_msg: str)` (function) — Detect an "output cap too large" error and return how many output tokens are available.
- L1005 `_model_id_matches(candidate_id: str, lookup_model: str)` (function) — Return True if *candidate_id* (from server) matches *lookup_model* (configured).
- L1024 `query_ollama_num_ctx(model: str, base_url: str, api_key: str='')` (function) — Query an Ollama server for the model's context length.
- L1079 `_query_ollama_api_show(model: str, base_url: str, api_key: str='')` (function) — Query an Ollama server's native ``/api/show`` for context length.
- L1140 `_model_name_suggests_kimi(model: str)` (function) — Return True if the model name looks like a Kimi-family model.
- L1152 `_model_name_suggests_minimax_m3(model: str)` (function) — Return True if the model name looks like MiniMax M3.
- L1164 `_model_name_suggests_grok_4_3(model: str)` (function) — Return True if the model name looks like a Grok 4.3 variant.
- L1176 `_query_local_context_length(model: str, base_url: str, api_key: str='')` (function) — Query a local server for the model's context length.
- L1270 `_normalize_model_version(model: str)` (function) — Normalize version separators for matching.
- L1280 `_query_anthropic_context_length(model: str, base_url: str, api_key: str)` (function) — Query Anthropic's /v1/models endpoint for context length.
- L1343 `_fetch_codex_oauth_context_lengths(access_token: str)` (function) — Probe the ChatGPT Codex /models endpoint for per-slug context windows.
- L1394 `_resolve_codex_oauth_context_length(model: str, access_token: str='')` (function) — Resolve a Codex OAuth model's real context window.
- L1427 `_resolve_nous_context_length(model: str, base_url: str='', api_key: str='')` (function) — Resolve Nous Portal model context length.
- L1501 `get_model_context_length(model: str, base_url: str='', api_key: str='', config_context_length: int | None=None, provider: str='', custom_providers: list | None=None)` (function) — Get the context length for a model.
- L1816 `estimate_tokens_rough(text: str)` (function) — Rough token estimate (~4 chars/token) for pre-flight checks.
- L1828 `estimate_messages_tokens_rough(messages: List[Dict[str, Any]])` (function) — Rough token estimate for a message list (pre-flight only).
- L1845 `_count_image_tokens(msg: Dict[str, Any], cost_per_image: int)` (function) — Count image-like content parts in a message; return their token cost.
- L1871 `_estimate_message_chars(msg: Dict[str, Any])` (function) — Char count for token estimation, excluding base64 image data.
- L1904 `estimate_request_tokens_rough(messages: List[Dict[str, Any]], *, system_prompt: str='', tools: Optional[List[Dict[str, Any]]]=None)` (function) — Rough token estimate for a full chat-completions request.
