---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_image_generation.py

Symbols in `tests/tools/test_image_generation.py`.

- L22 `image_tool()` (function) — Fresh import of tools.image_generation_tool per test.
- L33 `TestFalCatalog` (class) — Every FAL_MODELS entry must have a consistent shape.
- L36 `test_default_model_is_klein(self, image_tool)` (method)
- L39 `test_default_model_in_catalog(self, image_tool)` (method)
- L42 `test_all_entries_have_required_keys(self, image_tool)` (method)
- L51 `test_size_style_is_valid(self, image_tool)` (method)
- L57 `test_sizes_cover_all_aspect_ratios(self, image_tool)` (method)
- L62 `test_supports_is_a_set(self, image_tool)` (method)
- L67 `test_prompt_is_always_supported(self, image_tool)` (method)
- L72 `test_only_flux2_pro_upscales_by_default(self, image_tool)` (method) — Upscaling should default to False for all new models to preserve
- L89 `TestImageSizePresetFamily` (class) — Flux, z-image, qwen, recraft, ideogram all use preset enum sizes.
- L92 `test_klein_landscape_uses_preset(self, image_tool)` (method)
- L97 `test_klein_square_uses_preset(self, image_tool)` (method)
- L101 `test_klein_portrait_uses_preset(self, image_tool)` (method)
- L106 `TestAspectRatioFamily` (class) — Nano-banana uses aspect_ratio enum, NOT image_size.
- L109 `test_nano_banana_landscape_uses_aspect_ratio(self, image_tool)` (method)
- L114 `test_nano_banana_square_uses_aspect_ratio(self, image_tool)` (method)
- L118 `test_nano_banana_portrait_uses_aspect_ratio(self, image_tool)` (method)
- L123 `TestGptLiteralFamily` (class) — GPT-Image 1.5 uses literal size strings.
- L126 `test_gpt_landscape_is_literal(self, image_tool)` (method)
- L130 `test_gpt_square_is_literal(self, image_tool)` (method)
- L134 `test_gpt_portrait_is_literal(self, image_tool)` (method)
- L139 `TestGptImage2Presets` (class) — GPT Image 2 uses preset enum sizes (not literal strings like 1.5).
- L144 `test_gpt2_landscape_uses_4_3_preset(self, image_tool)` (method)
- L148 `test_gpt2_square_uses_square_hd(self, image_tool)` (method)
- L152 `test_gpt2_portrait_uses_4_3_preset(self, image_tool)` (method)
- L156 `test_gpt2_quality_pinned_to_medium(self, image_tool)` (method)
- L160 `test_gpt2_strips_byok_and_unsupported_overrides(self, image_tool)` (method) — openai_api_key (BYOK) is deliberately not in supports — all users
- L176 `test_gpt2_strips_seed_even_if_passed(self, image_tool)` (method)
- L186 `TestSupportsFilter` (class) — No model should receive keys outside its `supports` set.
- L189 `test_payload_keys_are_subset_of_supports_for_all_models(self, image_tool)` (method)
- L196 `test_gpt_image_has_no_seed_even_if_passed(self, image_tool)` (method)
- L201 `test_gpt_image_strips_unsupported_overrides(self, image_tool)` (method)
- L209 `test_recraft_has_minimal_payload(self, image_tool)` (method)
- L218 `test_nano_banana_never_gets_image_size(self, image_tool)` (method)
- L229 `TestDefaults` (class) — Model-level defaults should carry through unless overridden.
- L232 `test_klein_default_steps_is_4(self, image_tool)` (method)
- L236 `test_flux_2_pro_default_steps_is_50(self, image_tool)` (method)
- L240 `test_override_replaces_default(self, image_tool)` (method)
- L246 `test_none_override_does_not_replace_default(self, image_tool)` (method) — None values from caller should be ignored (use default).
- L259 `TestGptQualityPinnedToMedium` (class) — GPT-Image quality is baked into the FAL_MODELS defaults at 'medium'
- L264 `test_gpt_payload_always_has_medium_quality(self, image_tool)` (method)
- L268 `test_config_quality_setting_is_ignored(self, image_tool)` (method) — Even if a user manually edits config.yaml and adds quality_setting,
- L276 `test_non_gpt_model_never_gets_quality(self, image_tool)` (method) — quality is only meaningful for GPT-Image models (1.5, 2) — other
- L286 `test_honors_quality_setting_flag_is_removed(self, image_tool)` (method) — The honors_quality_setting flag was the old override trigger.
- L295 `test_resolve_gpt_quality_function_is_gone(self, image_tool)` (method) — The _resolve_gpt_quality() helper was removed — quality is now
- L307 `TestModelResolution` (class)
- L309 `test_no_config_falls_back_to_default(self, image_tool)` (method)
- L314 `test_valid_config_model_is_used(self, image_tool)` (method)
- L321 `test_unknown_model_falls_back_to_default_with_warning(self, image_tool, caplog)` (method)
- L327 `test_env_var_fallback_when_no_config(self, image_tool, monkeypatch)` (method)
- L333 `test_config_wins_over_env_var(self, image_tool, monkeypatch)` (method)
- L345 `TestAspectRatioNormalization` (class)
- L347 `test_invalid_aspect_defaults_to_landscape(self, image_tool)` (method)
- L351 `test_uppercase_aspect_is_normalized(self, image_tool)` (method)
- L355 `test_empty_aspect_defaults_to_landscape(self, image_tool)` (method)
- L364 `TestRegistryIntegration` (class)
- L366 `test_schema_exposes_only_prompt_and_aspect_ratio_to_agent(self, image_tool)` (method) — The agent-facing schema must stay tight — model selection is a
- L372 `test_aspect_ratio_enum_is_three_values(self, image_tool)` (method)
- L381 `_MockResponse` (class)
- L382 `__init__(self, status_code: int)` (method)
- L386 `_MockHttpxError` (class) — Simulates httpx.HTTPStatusError which exposes .response.status_code.
- L388 `__init__(self, status_code: int, message: str='Bad Request')` (method)
- L393 `TestExtractHttpStatus` (class) — Status-code extraction should work across exception shapes.
- L396 `test_extracts_from_response_attr(self, image_tool)` (method)
- L400 `test_extracts_from_status_code_attr(self, image_tool)` (method)
- L405 `test_returns_none_for_non_http_exception(self, image_tool)` (method)
- L409 `test_response_attr_without_status_code_returns_none(self, image_tool)` (method)
- L417 `TestManagedGatewayErrorTranslation` (class) — 4xx from the Nous managed gateway should be translated to a user-actionable message.
- L420 `test_4xx_translates_to_value_error_with_remediation(self, image_tool, monkeypatch)` (method) — 403 from managed gateway → ValueError mentioning FAL_KEY + hermes tools.
- L448 `test_5xx_is_not_translated(self, image_tool, monkeypatch)` (method) — 500s are real outages, not model-availability issues — don't rewrite them.
- L465 `test_direct_fal_errors_are_not_translated(self, image_tool, monkeypatch)` (method) — When user has direct FAL_KEY (managed gateway returns None), raw
- L482 `test_non_http_exception_from_managed_bubbles_up(self, image_tool, monkeypatch)` (method) — Connection errors, timeouts, etc. from managed mode aren't 4xx —
