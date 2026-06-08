---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_codex_transport.py

Symbols in `tests/agent/transports/test_codex_transport.py`.

- L12 `transport()` (function)
- L17 `TestCodexTransportBasic` (class)
- L19 `test_api_mode(self, transport)` (method)
- L22 `test_registered_on_import(self, transport)` (method)
- L25 `test_convert_tools(self, transport)` (method)
- L40 `TestCodexBuildKwargs` (class)
- L42 `test_basic_kwargs(self, transport)` (method)
- L57 `test_system_extracted_from_messages(self, transport)` (method)
- L65 `test_no_system_uses_default(self, transport)` (method)
- L70 `test_reasoning_config(self, transport)` (method)
- L78 `test_reasoning_disabled(self, transport)` (method)
- L86 `test_session_id_sets_cache_key(self, transport)` (method)
- L94 `test_github_responses_no_cache_key(self, transport)` (method)
- L103 `test_xai_responses_sends_cache_key_via_extra_body(self, transport)` (method) — xAI's Responses API documents ``prompt_cache_key`` as the
- L124 `test_xai_responses_extra_body_preserves_caller_fields(self, transport)` (method) — When the caller already supplies ``extra_body`` (e.g. via
- L141 `test_max_tokens(self, transport)` (method)
- L149 `test_codex_backend_no_max_output_tokens(self, transport)` (method)
- L158 `test_xai_headers(self, transport)` (method)
- L167 `test_xai_headers_preserve_request_override_headers(self, transport)` (method)
- L181 `test_minimal_effort_clamped(self, transport)` (method)
- L190 `test_xai_reasoning_effort_passed(self, transport)` (method)
- L207 `test_xai_reasoning_disabled_no_reasoning_key(self, transport)` (method)
- L217 `test_xai_minimal_effort_clamped(self, transport)` (method)
- L235 `test_xai_grok_4_omits_reasoning_effort(self, transport)` (method) — grok-4 / grok-4-0709 reject reasoning.effort with HTTP 400.
- L251 `test_xai_grok_4_fast_omits_reasoning_effort(self, transport)` (method) — grok-4-fast and grok-4-1-fast variants reject reasoning.effort.
- L269 `test_xai_grok_3_non_mini_omits_reasoning_effort(self, transport)` (method) — Plain grok-3 rejects reasoning.effort — only grok-3-mini accepts it.
- L279 `test_xai_grok_3_mini_keeps_reasoning_effort(self, transport)` (method) — grok-3-mini and -fast variants do accept the effort dial.
- L290 `test_xai_grok_4_20_0309_variants_omit_reasoning_effort(self, transport)` (method) — grok-4.20-0309-(non-)reasoning reject the effort dial.
- L304 `test_xai_grok_4_20_multi_agent_keeps_reasoning_effort(self, transport)` (method) — grok-4.20-multi-agent-0309 is the one grok-4.20 variant that accepts effort.
- L314 `test_xai_grok_code_fast_omits_reasoning_effort(self, transport)` (method) — grok-code-fast-1 rejects reasoning.effort.
- L324 `test_xai_aggregator_prefix_stripped(self, transport)` (method) — `x-ai/grok-3-mini` (OpenRouter-style slug) still resolves correctly.
- L343 `TestCodexValidateResponse` (class)
- L345 `test_none_response(self, transport)` (method)
- L348 `test_empty_output(self, transport)` (method)
- L352 `test_valid_output(self, transport)` (method)
- L356 `test_output_text_fallback_not_valid(self, transport)` (method) — validate_response is strict — output_text doesn't make it valid.
- L363 `TestCodexMapFinishReason` (class)
- L365 `test_completed(self, transport)` (method)
- L368 `test_incomplete(self, transport)` (method)
- L371 `test_failed(self, transport)` (method)
- L374 `test_unknown(self, transport)` (method)
- L378 `TestCodexNormalizeResponse` (class)
- L380 `test_text_response(self, transport)` (method) — Normalize a simple text Codex response.
- L401 `test_message_items_preserved_in_provider_data(self, transport)` (method) — Codex assistant message item ids/phases must survive transport normalization.
- L431 `test_tool_call_response(self, transport)` (method) — Normalize a Codex response with tool calls.
- L458 `TestCodexTransportTimeout` (class) — Forward per-request timeout from build_kwargs to the SDK kwargs.
- L461 `test_positive_timeout_preserved(self, transport)` (method)
- L470 `test_zero_timeout_dropped(self, transport)` (method)
- L479 `test_none_timeout_omitted(self, transport)` (method)
- L488 `test_inf_timeout_dropped(self, transport)` (method)
- L497 `test_bool_timeout_dropped(self, transport)` (method) — ``True`` is technically int but must not survive — caller bug guard.
- L507 `test_request_overrides_can_supply_timeout(self, transport)` (method) — request_overrides["timeout"] is honored when no explicit kwarg passed.
- L518 `TestCodexTransportXaiServiceTierStrip` (class) — xAI Responses API rejects ``service_tier`` (#28490).
- L531 `transport(self)` (method)
- L535 `test_xai_strips_service_tier_from_request_overrides(self, transport)` (method) — Headline #28490 case: service_tier=priority leaks through
- L550 `test_non_xai_codex_preserves_service_tier(self, transport)` (method) — The strip is xAI-only — native Codex DOES accept
- L567 `test_github_responses_preserves_service_tier(self, transport)` (method) — GitHub Models (Copilot) is another codex_responses surface
- L580 `TestPreflightSlashEnumStrip` (class) — xAI Responses safety-net: strip slash-containing enum values
- L592 `_make_kwargs(self, model: str, enum_values: list[str])` (method)
- L615 `test_grok_model_strips_slash_enum_values(self)` (method) — When the model name is Grok-family, slash-containing enum
- L632 `test_aggregator_prefixed_grok_also_strips(self)` (method) — Aggregator-prefixed (x-ai/grok-*) names hit the same path.
- L642 `test_non_grok_model_preserves_slash_enum_values(self)` (method) — Native Codex / GitHub Models DO accept slash-containing
