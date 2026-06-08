---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_model_metadata_local_ctx.py

Symbols in `tests/agent/test_model_metadata_local_ctx.py`.

- L19 `TestQueryLocalContextLengthOllama` (class) — _query_local_context_length with server_type == 'ollama'.
- L22 `_make_resp(self, status_code, body)` (method)
- L28 `test_ollama_model_info_context_length(self)` (method) — Reads context length from model_info dict in /api/show response.
- L49 `test_ollama_parameters_num_ctx(self)` (method) — Falls back to num_ctx in parameters string when model_info lacks context_length.
- L71 `test_ollama_num_ctx_wins_over_model_info(self)` (method) — When both num_ctx (Modelfile) and model_info (GGUF) are present,
- L109 `test_ollama_show_404_falls_through(self)` (method) — When /api/show returns 404, falls through to /v1/models/{model}.
- L129 `TestQueryLocalContextLengthVllm` (class) — _query_local_context_length with vLLM-style /v1/models/{model} response.
- L132 `_make_resp(self, status_code, body)` (method)
- L138 `test_vllm_max_model_len(self)` (method) — Reads max_model_len from /v1/models/{model} response.
- L157 `test_vllm_context_length_key(self)` (method) — Reads context_length from /v1/models/{model} response.
- L176 `TestQueryLocalContextLengthModelsList` (class) — _query_local_context_length: falls back to /v1/models list.
- L179 `_make_resp(self, status_code, body)` (method)
- L185 `test_models_list_max_model_len(self)` (method) — Finds context length for model in /v1/models list.
- L216 `test_models_list_model_not_found_returns_none(self)` (method) — Returns None when model is not in the /v1/models list.
- L245 `TestQueryLocalContextLengthLmStudio` (class) — _query_local_context_length with LM Studio native /api/v1/models response.
- L248 `_make_resp(self, status_code, body)` (method)
- L254 `_make_client(self, native_resp, detail_resp, list_resp)` (method) — Build a mock httpx.Client with sequenced GET responses.
- L274 `test_lmstudio_exact_key_match(self)` (method) — Resolves loaded ctx when key matches exactly.
- L300 `test_lmstudio_slug_only_matches_key_with_publisher_prefix(self)` (method) — Fuzzy match: bare model slug matches key that includes publisher prefix.
- L332 `test_lmstudio_v1_models_list_slug_fuzzy_match(self)` (method) — Fuzzy match also works for /v1/models list when exact match fails.
- L360 `test_lmstudio_loaded_instances_context_length(self)` (method) — Reads active context_length from loaded_instances when max_context_length absent.
- L389 `test_lmstudio_loaded_instance_beats_max_context_length(self)` (method) — loaded_instances context_length takes priority over max_context_length.
- L428 `TestDetectLocalServerTypeAuth` (class)
- L429 `test_passes_bearer_token_to_probe_requests(self)` (method)
- L449 `TestFetchEndpointModelMetadataLmStudio` (class) — fetch_endpoint_model_metadata should use LM Studio's native models endpoint.
- L452 `_make_resp(self, body)` (method)
- L458 `test_uses_native_models_endpoint_only(self)` (method)
- L493 `TestQueryLocalContextLengthNetworkError` (class) — _query_local_context_length handles network failures gracefully.
- L496 `test_connection_error_returns_none(self)` (method) — Returns None when the server is unreachable.
- L517 `TestGetModelContextLengthLocalFallback` (class) — get_model_context_length uses local server query before falling back to 2M.
- L520 `test_local_endpoint_unknown_model_queries_server(self)` (method) — Unknown model on local endpoint gets ctx from server, not 2M default.
- L534 `test_local_endpoint_unknown_model_result_is_cached(self)` (method) — Context length returned from local server is persisted to cache.
- L548 `test_local_endpoint_server_returns_none_falls_back_to_2m(self)` (method) — When local server returns None, still falls back to 2M probe tier.
- L561 `test_non_local_endpoint_does_not_query_local_server(self)` (method) — For non-local endpoints, _query_local_context_length is not called.
- L576 `test_cached_result_skips_local_query(self)` (method) — Cached context length is returned without querying the local server.
- L587 `test_no_base_url_does_not_query_local_server(self)` (method) — When base_url is empty, local server is not queried.
