---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/plugins/image_gen/test_openai_codex_provider.py

Symbols in `tests/plugins/image_gen/test_openai_codex_provider.py`.

- L30 `_b64_png()` (function)
- L36 `_tmp_hermes_home(tmp_path, monkeypatch)` (function)
- L42 `provider(monkeypatch)` (function)
- L51 `TestMetadata` (class)
- L52 `test_name(self, provider)` (method)
- L55 `test_display_name(self, provider)` (method)
- L58 `test_default_model(self, provider)` (method)
- L61 `test_list_models_three_tiers(self, provider)` (method)
- L65 `test_setup_schema_has_no_required_env_vars(self, provider)` (method)
- L74 `TestAvailability` (class)
- L75 `test_unavailable_without_codex_token(self, monkeypatch)` (method)
- L80 `test_available_with_codex_token(self, monkeypatch)` (method)
- L85 `test_openai_api_key_alone_is_not_enough(self, monkeypatch)` (method)
- L96 `TestGenerate` (class)
- L97 `test_returns_auth_error_without_codex_token(self, provider, monkeypatch)` (method)
- L103 `test_returns_invalid_argument_for_empty_prompt(self, provider, monkeypatch)` (method)
- L109 `test_generate_uses_codex_stream_path(self, provider, monkeypatch, tmp_path)` (method)
- L127 `test_codex_stream_request_shape(self, provider, monkeypatch)` (method)
- L163 `test_partial_image_event_used_when_done_missing(self)` (method) — If output_item.done is missing, partial_image_b64 is accepted.
- L171 `test_sse_parser_handles_event_and_data_lines(self)` (method)
- L186 `test_final_response_sweep_recovers_image(self)` (method) — Completed response output is found by recursive payload scanning.
- L201 `test_empty_response_returns_error(self, provider, monkeypatch)` (method)
- L209 `test_stream_exception_returns_api_error(self, provider, monkeypatch)` (method)
- L226 `TestRegistration` (class)
- L227 `test_register_calls_register_image_gen_provider(self)` (method)
