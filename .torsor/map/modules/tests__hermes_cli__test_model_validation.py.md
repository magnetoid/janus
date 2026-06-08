---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_model_validation.py

Symbols in `tests/hermes_cli/test_model_validation.py`.

- L36 `_validate(model, provider='openrouter', api_models=FAKE_API_MODELS, **kw)` (function) — Shortcut: call validate_requested_model with mocked API.
- L52 `TestParseModelInput` (class)
- L53 `test_plain_model_keeps_current_provider(self)` (method)
- L58 `test_provider_colon_model_switches_provider(self)` (method)
- L63 `test_provider_alias_resolved(self)` (method)
- L68 `test_stepfun_alias_resolved(self)` (method)
- L73 `test_no_slash_no_colon_keeps_provider(self)` (method)
- L78 `test_nous_provider_switch(self)` (method)
- L83 `test_empty_model_after_colon_keeps_current(self)` (method)
- L88 `test_colon_at_start_keeps_current(self)` (method)
- L93 `test_unknown_prefix_colon_not_treated_as_provider(self)` (method) — Colons are only provider delimiters if the left side is a known provider.
- L99 `test_http_url_not_treated_as_provider(self)` (method)
- L104 `test_custom_colon_model_single(self)` (method) — custom:model-name → anonymous custom provider.
- L110 `test_custom_triple_syntax(self)` (method) — custom:name:model → named custom provider.
- L116 `test_custom_triple_spaces(self)` (method) — Triple syntax should handle whitespace.
- L122 `test_custom_triple_empty_model_falls_back(self)` (method) — custom:name: with no model → treated as custom:name (bare).
- L132 `TestCuratedModelsForProvider` (class)
- L133 `test_openrouter_returns_curated_list(self)` (method)
- L145 `test_unknown_provider_returns_empty(self)` (method)
- L151 `TestNormalizeProvider` (class)
- L152 `test_defaults_to_openrouter(self)` (method)
- L156 `test_known_aliases(self)` (method)
- L163 `test_case_insensitive(self)` (method)
- L167 `TestProviderLabel` (class)
- L168 `test_known_labels_and_auto(self)` (method)
- L176 `test_unknown_provider_preserves_original_name(self)` (method)
- L182 `TestProviderModelIds` (class)
- L183 `test_openrouter_returns_curated_list(self)` (method)
- L195 `test_unknown_provider_returns_empty(self)` (method)
- L198 `test_stepfun_prefers_live_catalog(self)` (method)
- L208 `test_copilot_prefers_live_catalog(self)` (method)
- L213 `test_copilot_acp_reuses_copilot_catalog(self)` (method)
- L221 `TestFetchApiModels` (class)
- L222 `test_returns_none_when_no_base_url(self)` (method)
- L225 `test_returns_none_on_network_error(self)` (method)
- L229 `test_probe_api_models_tries_v1_fallback(self)` (method)
- L256 `test_probe_api_models_uses_copilot_catalog(self)` (method)
- L275 `test_fetch_github_model_catalog_filters_non_chat_models(self)` (method)
- L293 `TestGithubReasoningEfforts` (class)
- L294 `test_gpt5_supports_minimal_to_high(self)` (method)
- L306 `test_legacy_catalog_reasoning_still_supported(self)` (method)
- L314 `test_non_reasoning_model_returns_empty(self)` (method)
- L319 `TestCopilotNormalization` (class)
- L320 `test_normalize_old_github_models_slug(self)` (method)
- L324 `test_copilot_api_mode_gpt5_uses_responses(self)` (method) — GPT-5+ models should use Responses API (matching opencode).
- L332 `test_copilot_api_mode_gpt5_mini_uses_chat(self)` (method) — gpt-5-mini is the exception — uses Chat Completions.
- L336 `test_copilot_api_mode_non_gpt5_uses_chat(self)` (method) — Non-GPT-5 models use Chat Completions.
- L345 `test_copilot_api_mode_with_catalog_both_endpoints(self)` (method) — When catalog shows both endpoints, model ID pattern wins.
- L354 `test_copilot_api_mode_with_catalog_only_responses(self)` (method)
- L362 `test_normalize_opencode_model_id_strips_provider_prefix(self)` (method)
- L367 `test_opencode_zen_api_modes_match_docs(self)` (method)
- L376 `test_opencode_go_api_modes_match_docs(self)` (method)
- L389 `TestAzureFoundryModelApiMode` (class) — Azure Foundry deploys GPT-5.x / codex / o-series as Responses-API-only.
- L398 `test_gpt5_family_uses_responses(self)` (method)
- L408 `test_codex_family_uses_responses(self)` (method)
- L412 `test_o_series_reasoning_uses_responses(self)` (method)
- L420 `test_gpt4_family_returns_none(self)` (method) — GPT-4, GPT-4o, etc. speak chat completions on Azure.
- L430 `test_non_openai_deployments_return_none(self)` (method) — Llama, Mistral, Grok, etc. keep the default chat completions.
- L437 `test_vendor_prefix_stripped(self)` (method) — Users who copy-paste ``openai/gpt-5.3-codex`` should still match.
- L442 `test_empty_and_none_return_none(self)` (method)
- L447 `test_case_insensitive(self)` (method)
- L454 `TestValidateFormatChecks` (class)
- L455 `test_empty_model_rejected(self)` (method)
- L460 `test_whitespace_only_rejected(self)` (method)
- L464 `test_model_with_spaces_rejected(self)` (method)
- L468 `test_no_slash_model_still_probes_api(self)` (method)
- L473 `test_no_slash_model_rejected_if_not_in_api(self)` (method)
- L482 `TestValidateApiFound` (class)
- L483 `test_model_found_in_api(self)` (method)
- L489 `test_model_found_for_custom_endpoint(self)` (method)
- L501 `TestValidateApiNotFound` (class)
- L502 `test_model_not_in_api_rejected_with_guidance(self)` (method)
- L508 `test_warning_includes_suggestions(self)` (method)
- L514 `test_auto_correction_returns_corrected_model(self)` (method) — When a very close match exists, validate returns corrected_model.
- L521 `test_dissimilar_model_shows_suggestions_not_autocorrect(self)` (method) — Models too different for auto-correction are rejected with suggestions.
- L531 `TestValidateApiFallback` (class) — When /models is unreachable, the validator must accept the model (with
- L547 `test_known_model_accepted_via_catalog_when_api_down(self)` (method)
- L558 `test_unknown_model_accepted_with_note_when_api_down(self)` (method)
- L570 `test_zai_known_model_accepted_via_catalog_when_api_down(self)` (method)
- L577 `test_unknown_provider_soft_accepted_when_api_down(self)` (method)
- L586 `test_custom_endpoint_warns_with_probed_url_and_v1_hint(self)` (method)
- L612 `test_fetch_lmstudio_models_filters_embedding_type(self)` (method)
- L628 `test_validate_lmstudio_rejects_embedding_models(self)` (method)
- L650 `test_fetch_lmstudio_models_raises_auth_error_on_401(self)` (method)
- L671 `test_fetch_lmstudio_models_returns_empty_on_network_error(self)` (method)
- L680 `test_validate_lmstudio_distinguishes_auth_failure(self)` (method)
- L702 `test_validate_lmstudio_distinguishes_unreachable(self)` (method)
- L719 `TestValidateCodexAutoCorrection` (class) — Auto-correction for typos on openai-codex provider.
- L722 `test_missing_dash_auto_corrects(self)` (method) — gpt5.3-codex (missing dash) auto-corrects to gpt-5.3-codex.
- L733 `test_exact_match_no_correction(self)` (method) — Exact model name does not trigger auto-correction.
- L747 `TestProbeApiModelsUserAgent` (class) — Probing custom /v1/models must send a Hermes User-Agent.
- L758 `_make_mock_response(self, body: bytes)` (method)
- L766 `test_probe_sends_hermes_user_agent(self)` (method)
- L787 `test_probe_user_agent_sent_without_api_key(self)` (method) — UA must be present even for endpoints that don't need auth.
