---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_azure_detect.py

Symbols in `tests/hermes_cli/test_azure_detect.py`.

- L17 `_FakeHTTPResponse` (class) — Minimal stand-in for urllib.request.urlopen's context manager.
- L20 `__init__(self, status: int, body: bytes)` (method)
- L24 `__enter__(self)` (method)
- L27 `__exit__(self, exc_type, exc, tb)` (method)
- L30 `read(self)` (method)
- L34 `_openai_models_body(*ids: str)` (function)
- L41 `_anthropic_error_body(msg: str='model not found')` (function)
- L60 `test_looks_like_anthropic_path(url, expected)` (function)
- L68 `test_extract_model_ids_openai_shape()` (function)
- L79 `test_extract_model_ids_bad_shape_returns_empty()` (function)
- L89 `test_detect_anthropic_path_wins_without_http()` (function) — URL path sniff short-circuits — no HTTP call happens.
- L103 `test_detect_openai_models_probe_success()` (function) — /models probe returning a model list → chat_completions.
- L119 `test_detect_openai_models_probe_empty_list_still_counts()` (function) — Endpoint returned OpenAI shape but no models → still chat_completions.
- L133 `test_detect_falls_back_to_anthropic_probe()` (function) — /models fails but Anthropic Messages probe succeeds.
- L147 `test_detect_all_probes_fail_returns_none()` (function) — Every probe fails → api_mode is None and caller falls back to manual.
- L163 `test_probe_openai_models_tries_multiple_api_versions()` (function) — First call (no api-version) fails, api-version fallback succeeds.
- L188 `test_http_get_json_on_urlerror_returns_zero_none()` (function) — Network failure returns (0, None), never raises.
- L198 `test_http_get_json_on_http_error_returns_code_none()` (function) — HTTP 4xx/5xx returns (code, None).
- L212 `test_lookup_context_length_returns_known()` (function) — When model_metadata returns a non-fallback value, we pass it through.
- L223 `test_lookup_context_length_returns_none_on_fallback()` (function) — When resolver falls through to DEFAULT_FALLBACK_CONTEXT, we return None.
- L233 `test_lookup_context_length_swallows_exceptions()` (function) — Resolver raising must not crash the wizard.
