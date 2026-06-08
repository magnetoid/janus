---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_ollama_num_ctx.py

Symbols in `tests/test_ollama_num_ctx.py`.

- L19 `_mock_httpx_client(show_response_data, status_code=200)` (function) — Create a mock httpx.Client context manager that returns given /api/show data.
- L31 `TestQueryOllamaNumCtx` (class) — Test the Ollama /api/show context length query.
- L34 `test_returns_context_from_model_info(self)` (method) — Should extract context_length from GGUF model_info metadata.
- L50 `test_prefers_explicit_num_ctx_from_modelfile(self)` (method) — If the Modelfile sets num_ctx explicitly, that should take priority.
- L65 `test_returns_none_for_non_ollama_server(self)` (method) — Should return None if the server is not Ollama.
- L71 `test_returns_none_on_connection_error(self)` (method) — Should return None if the server is unreachable.
- L77 `test_returns_none_on_404(self)` (method) — Should return None if the model is not found.
- L88 `test_strips_provider_prefix(self)` (method) — Should strip 'local:' prefix from model name before querying.
- L106 `test_handles_qwen2_architecture_key(self)` (method) — Different model architectures use different key prefixes in model_info.
- L121 `test_returns_none_when_model_info_empty(self)` (method) — Should return None if model_info has no context_length key.
