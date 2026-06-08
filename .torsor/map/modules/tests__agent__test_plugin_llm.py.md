---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_plugin_llm.py

Symbols in `tests/agent/test_plugin_llm.py`.

- L41 `_fake_response(text: str, *, prompt: int=4, completion: int=6)` (function) — Build an OpenAI-shaped response with the given text + token usage.
- L58 `_trusted_policy(plugin_id: str='trusted-plugin', **overrides: Any)` (function)
- L78 `TestTrustGate` (class)
- L79 `test_default_policy_blocks_provider_override(self)` (method)
- L90 `test_default_policy_blocks_model_override(self)` (method)
- L101 `test_default_policy_blocks_agent_override(self)` (method)
- L112 `test_default_policy_blocks_profile_override(self)` (method)
- L123 `test_overrides_independent(self)` (method) — Each override is gated independently — turning on
- L150 `test_provider_allowlist_rejects_non_listed(self)` (method)
- L166 `test_provider_allowlist_accepts_listed_case_insensitively(self)` (method)
- L182 `test_model_allowlist_rejects_non_listed(self)` (method)
- L198 `test_model_allowlist_accepts_listed_case_insensitively(self)` (method)
- L214 `test_no_overrides_passes_through(self)` (method)
- L225 `test_all_overrides_when_fully_trusted(self)` (method)
- L237 `TestAllowlistCoercion` (class)
- L238 `test_missing_yields_none(self)` (method)
- L243 `test_list_of_strings(self)` (method)
- L248 `test_star_alone_means_any(self)` (method)
- L253 `test_star_plus_specific_keeps_specifics(self)` (method)
- L258 `test_non_list_yields_none(self)` (method)
- L269 `TestStructuredMessageBuilding` (class)
- L270 `test_text_only_input(self)` (method)
- L286 `test_json_mode_adds_system_directive(self)` (method)
- L298 `test_schema_name_appended_to_header(self)` (method)
- L310 `test_image_bytes_encoded_as_data_url(self)` (method)
- L331 `test_image_url_passed_through(self)` (method)
- L344 `test_dict_inputs_normalized(self)` (method)
- L360 `test_invalid_input_block_rejected(self)` (method)
- L377 `TestJsonParsing` (class)
- L378 `test_strip_code_fences_with_json_label(self)` (method)
- L381 `test_strip_code_fences_without_label(self)` (method)
- L384 `test_strip_code_fences_no_fence(self)` (method)
- L387 `test_parse_returns_text_when_not_json_mode(self)` (method)
- L394 `test_parse_valid_json_with_json_mode(self)` (method)
- L403 `test_parse_strips_code_fences_before_loading(self)` (method)
- L412 `test_parse_returns_text_on_invalid_json(self)` (method)
- L421 `test_schema_validation_rejects_mismatch(self)` (method)
- L435 `test_schema_validation_accepts_match(self)` (method)
- L456 `TestPluginLlmFacade` (class)
- L457 `test_complete_uses_active_model_by_default(self)` (method)
- L478 `test_complete_rejects_provider_override_without_trust(self)` (method)
- L490 `test_complete_rejects_model_override_without_trust(self)` (method)
- L502 `test_complete_passes_through_trusted_overrides(self)` (method)
- L536 `test_complete_structured_returns_parsed_json(self)` (method)
- L560 `test_complete_structured_returns_text_on_unparseable_response(self)` (method)
- L578 `test_complete_structured_validates_against_schema(self)` (method)
- L601 `test_complete_structured_requires_instructions(self)` (method)
- L613 `test_complete_structured_requires_at_least_one_input(self)` (method)
- L625 `test_complete_structured_emits_response_format_extra_body(self)` (method)
- L647 `test_complete_structured_with_image_passes_image_url_part(self)` (method)
- L677 `TestAsyncSurface` (class)
- L678 `test_acomplete_uses_async_caller(self)` (method)
- L695 `test_acomplete_structured_parses_json(self)` (method)
- L722 `TestConfigDrivenPolicy` (class)
- L723 `test_policy_loaded_from_yaml(self, tmp_path, monkeypatch)` (method)
- L757 `test_missing_plugin_entry_yields_default_deny(self, tmp_path, monkeypatch)` (method)
- L779 `TestPluginContextIntegration` (class)
- L780 `test_ctx_llm_is_lazy_singleton(self)` (method)
- L792 `test_ctx_llm_uses_manifest_key_for_policy(self)` (method)
- L808 `TestAttribution` (class) — Verifies that the result object and the audit log carry the real
- L813 `test_explicit_overrides_recorded_when_no_response_model(self)` (method)
- L826 `test_response_model_wins_over_model_override(self)` (method) — Providers often canonicalise the model name (e.g. ``gpt-4o``
- L842 `test_falls_back_to_main_provider_and_model_when_no_overrides(self, monkeypatch)` (method) — When the plugin doesn't override anything, attribution
- L861 `test_response_model_used_even_when_no_overrides(self, monkeypatch)` (method) — The provider's canonical model name should still flow through
- L879 `test_placeholder_fallback_only_when_everything_is_empty(self, monkeypatch)` (method) — If main_provider/main_model are unset AND there's no override
- L904 `TestHookMode` (class) — The docs page promises ``ctx.llm`` works from inside lifecycle
- L910 `test_complete_works_from_post_tool_call_hook(self)` (method)
- L964 `test_complete_works_from_post_tool_call_hook_when_async_caller_set(self)` (method) — Hooks fired synchronously should still work with sync
