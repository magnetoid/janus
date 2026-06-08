---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/transports/test_chat_completions.py

Symbols in `tests/agent/transports/test_chat_completions.py`.

- L11 `transport()` (function)
- L16 `TestChatCompletionsBasic` (class)
- L18 `test_api_mode(self, transport)` (method)
- L21 `test_registered(self, transport)` (method)
- L24 `test_convert_tools_identity(self, transport)` (method)
- L28 `test_convert_messages_no_codex_leaks(self, transport)` (method)
- L33 `test_convert_messages_strips_codex_fields(self, transport)` (method)
- L49 `_msg_with_extra_content(self)` (method)
- L57 `test_convert_messages_strips_extra_content_for_strict_provider(self, transport)` (method) — Strict providers (Fireworks, Mistral) reject extra_content on
- L69 `test_convert_messages_strips_extra_content_when_model_unknown(self, transport)` (method) — Default (no model supplied) is to strip — safe for strict providers.
- L75 `test_convert_messages_keeps_extra_content_for_gemini(self, transport)` (method) — Gemini 3 thinking models require the thought_signature replayed on
- L87 `test_convert_messages_strips_tool_name(self, transport)` (method) — Internal `tool_name` (used for FTS indexing in the SQLite store) is
- L107 `test_convert_messages_strips_internal_scaffolding_markers(self, transport)` (method) — Hermes-internal ``_``-prefixed markers must never reach the wire.
- L131 `test_convert_messages_clean_list_is_identity(self, transport)` (method) — A list with no internal/codex keys is returned as-is (no copy).
- L140 `TestChatCompletionsBuildKwargs` (class)
- L142 `test_basic_kwargs(self, transport)` (method)
- L149 `test_developer_role_swap(self, transport)` (method)
- L154 `test_no_developer_swap_for_non_gpt5(self, transport)` (method)
- L159 `test_tools_included(self, transport)` (method)
- L165 `test_openrouter_provider_prefs(self, transport)` (method)
- L176 `test_openrouter_pareto_min_coding_score(self, transport)` (method) — Profile path: model=openrouter/pareto-code + score → plugins block.
- L190 `test_openrouter_pareto_score_ignored_for_other_models(self, transport)` (method) — Score must not be emitted for any model other than openrouter/pareto-code.
- L202 `test_openrouter_pareto_score_omitted_when_unset(self, transport)` (method) — No score → no plugins block (router uses its omission default = strongest coder).
- L214 `test_openrouter_pareto_score_out_of_range_dropped(self, transport)` (method) — Out-of-range scores must be silently dropped, not forwarded.
- L227 `test_openrouter_pareto_legacy_path(self, transport)` (method) — Legacy flag path (no profile loaded) must also emit the plugins block.
- L239 `test_nous_tags(self, transport)` (method)
- L247 `test_reasoning_default(self, transport)` (method)
- L255 `test_nous_omits_disabled_reasoning(self, transport)` (method)
- L268 `test_ollama_num_ctx(self, transport)` (method)
- L279 `test_custom_think_false(self, transport)` (method)
- L290 `test_gemini_native_without_explicit_reasoning_config_keeps_existing_behavior(self, transport)` (method)
- L302 `test_gemini_native_flash_reasoning_maps_to_top_level_thinking_config(self, transport)` (method)
- L316 `test_gemini_openai_compat_flash_reasoning_maps_to_nested_google_thinking_config(self, transport)` (method)
- L331 `test_gemini_native_25_reasoning_only_enables_visible_thoughts(self, transport)` (method)
- L344 `test_gemini_openai_compat_pro_reasoning_clamps_to_supported_levels(self, transport)` (method)
- L358 `test_gemini_native_disabled_reasoning_hides_thoughts(self, transport)` (method)
- L371 `test_gemini_openai_compat_xhigh_clamps_to_high(self, transport)` (method)
- L382 `test_google_gemini_cli_keeps_top_level_thinking_config(self, transport)` (method)
- L396 `test_gemini_flash_minimal_clamps_to_low(self, transport)` (method)
- L412 `test_gemma_does_not_receive_thinking_config(self, transport)` (method)
- L426 `test_gemma_disabled_reasoning_still_omits_thinking_config(self, transport)` (method)
- L439 `test_google_prefixed_gemma_also_omits_thinking_config(self, transport)` (method)
- L452 `test_max_tokens_with_fn(self, transport)` (method)
- L461 `test_ephemeral_overrides_max_tokens(self, transport)` (method)
- L471 `test_nvidia_default_max_tokens(self, transport)` (method) — NVIDIA max_tokens=16384 is now set via ProviderProfile, not legacy flag.
- L485 `test_qwen_default_max_tokens(self, transport)` (method)
- L497 `test_anthropic_max_output_for_claude_on_aggregator(self, transport)` (method)
- L508 `test_request_overrides_last(self, transport)` (method)
- L516 `test_fixed_temperature(self, transport)` (method) — Fixed temperature is now set via ProviderProfile.fixed_temperature.
- L526 `test_omit_temperature(self, transport)` (method) — Omit temperature is set via ProviderProfile with OMIT_TEMPERATURE sentinel.
- L537 `TestChatCompletionsKimi` (class) — Regression tests for the Kimi/Moonshot quirks migrated into the transport.
- L540 `test_kimi_max_tokens_default(self, transport)` (method)
- L551 `test_kimi_reasoning_effort_top_level(self, transport)` (method)
- L563 `test_kimi_reasoning_effort_omitted_when_thinking_disabled(self, transport)` (method)
- L573 `test_kimi_thinking_enabled_extra_body(self, transport)` (method)
- L583 `test_kimi_thinking_disabled_extra_body(self, transport)` (method)
- L594 `test_moonshot_tool_schemas_are_sanitized_by_model_name(self, transport)` (method) — Aggregator routes (Nous, OpenRouter) hit Moonshot by model name, not base URL.
- L619 `test_non_moonshot_tools_are_not_mutated(self, transport)` (method) — Other models don't go through the Moonshot sanitizer.
- L645 `TestChatCompletionsLmStudioReasoning` (class) — LM Studio publishes per-model reasoning ``allowed_options``. When the
- L653 `test_omits_effort_when_high_not_allowed_toggle(self, transport)` (method)
- L663 `test_omits_effort_when_high_not_allowed_minimal_low(self, transport)` (method)
- L673 `test_passes_through_when_effort_allowed(self, transport)` (method)
- L683 `test_passes_through_aliased_on_for_toggle(self, transport)` (method)
- L696 `test_disabled_keeps_none_when_off_allowed(self, transport)` (method)
- L706 `test_no_options_falls_back_to_legacy_behavior(self, transport)` (method)
- L719 `TestChatCompletionsValidate` (class)
- L721 `test_none(self, transport)` (method)
- L724 `test_no_choices(self, transport)` (method)
- L728 `test_empty_choices(self, transport)` (method)
- L732 `test_valid(self, transport)` (method)
- L737 `TestChatCompletionsNormalize` (class)
- L739 `test_text_response(self, transport)` (method)
- L753 `test_tool_call_response(self, transport)` (method)
- L770 `test_tool_call_extra_content_preserved(self, transport)` (method) — Gemini 3 thinking models attach extra_content with thought_signature
- L792 `test_reasoning_content_preserved_separately(self, transport)` (method) — DeepSeek/Moonshot use reasoning_content distinct from reasoning.
- L811 `test_empty_reasoning_content_preserved(self, transport)` (method) — DeepSeek can require an explicit empty reasoning_content replay field.
- L829 `test_reasoning_content_preserved_from_model_extra(self, transport)` (method) — OpenAI SDK can expose provider-specific DeepSeek fields via model_extra.
- L847 `TestChatCompletionsCacheStats` (class)
- L849 `test_no_usage(self, transport)` (method)
- L853 `test_no_details(self, transport)` (method)
- L857 `test_with_cache(self, transport)` (method)
- L864 `TestChatCompletionsGeminiNativeExtraBodyStrip` (class) — Profile extra_body (e.g. Nous portal tags) must not reach a native
- L869 `_nous_profile(self)` (method)
- L873 `test_tags_stripped_when_endpoint_is_native_gemini(self, transport)` (method)
- L886 `test_tags_preserved_on_nous_endpoint(self, transport)` (method)
- L899 `test_tags_pass_through_on_gemini_openai_compat(self, transport)` (method)
