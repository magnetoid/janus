---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/web_tools.py

Symbols in `tools/web_tools.py`.

- L113 `_env_value(name: str)` (function) — Resolve ``name`` via Hermes config-aware env, falling back to process env.
- L133 `_has_env(name: str)` (function)
- L136 `_load_web_config()` (function) — Load the ``web:`` section from ~/.hermes/config.yaml.
- L144 `_get_backend()` (function) — Determine which web backend to use (shared fallback).
- L176 `_get_search_backend()` (function) — Determine which backend to use for web_search specifically.
- L190 `_get_extract_backend()` (function) — Determine which backend to use for web_extract specifically.
- L201 `_get_capability_backend(capability: str)` (function) — Shared helper for per-capability backend selection.
- L214 `_is_backend_available(backend: str)` (function) — Return True when the selected backend is currently usable.
- L243 `_ddgs_package_importable()` (function) — Return True when the ``ddgs`` Python package can be imported.
- L267 `_web_requires_env()` (function) — Return tool metadata env vars for the currently enabled web backends.
- L307 `_is_nous_auxiliary_client(client: Any)` (function) — Return True when the resolved auxiliary backend is Nous Portal.
- L316 `_resolve_web_extract_auxiliary(model: Optional[str]=None)` (function) — Resolve the current web-extract auxiliary client, model, and extra body.
- L331 `_get_default_summarizer_model()` (function) — Return the current default model for web extraction summarization.
- L339 `process_content_with_llm(content: str, url: str='', title: str='', model: Optional[str]=None, min_length: int=DEFAULT_MIN_LENGTH_FOR_SUMMARIZATION)` (function) — Process web content using LLM to create intelligent summaries with key excerpts.
- L439 `_call_summarizer_llm(content: str, context_str: str, model: Optional[str], max_tokens: int=20000, is_chunk: bool=False, chunk_info: str='')` (function) — Make a single LLM call to summarize content.
- L557 `_process_large_content_chunked(content: str, context_str: str, model: Optional[str], chunk_size: int, max_output_size: int)` (function) — Process large content by chunking, summarizing each chunk in parallel,
- L713 `clean_base64_images(text: str)` (function) — Remove base64 encoded images from text to reduce token count and clutter.
- L755 `_ensure_web_plugins_loaded()` (function) — Idempotently trigger plugin discovery so the web registry is populated.
- L784 `web_search_tool(query: str, limit: int=5)` (function) — Search the web for information using available search API backend.
- L891 `web_extract_tool(urls: List[str], format: str=None, use_llm_processing: bool=True, model: Optional[str]=None, min_length: int=DEFAULT_MIN_LENGTH_FOR_SUMMARIZATION)` (function) — Extract content from specific web pages using available extraction API backend.
- L1182 `check_web_api_key()` (function) — Check whether the configured web backend is available.
- L1193 `check_auxiliary_model()` (function) — Check if an auxiliary text model is available for LLM content processing.
