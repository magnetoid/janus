---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_fast_command.py

Symbols in `tests/cli/test_fast_command.py`.

- L8 `_import_cli()` (function)
- L23 `TestParseServiceTierConfig` (class)
- L24 `_parse(self, raw)` (method)
- L28 `test_fast_maps_to_priority(self)` (method)
- L32 `test_normal_disables_service_tier(self)` (method)
- L38 `TestHandleFastCommand` (class)
- L39 `_make_cli(self, service_tier=None)` (method)
- L49 `test_no_args_shows_status(self)` (method)
- L64 `test_no_args_shows_fast_when_enabled(self)` (method)
- L77 `test_normal_argument_clears_service_tier(self)` (method)
- L90 `test_unsupported_model_does_not_expose_fast(self)` (method)
- L111 `TestPriorityProcessingModels` (class) — Verify the expanded Priority Processing model registry.
- L114 `test_all_documented_models_supported(self)` (method)
- L130 `test_all_anthropic_models_supported(self)` (method) — The speed=fast parameter is gated to Opus 4.6.
- L158 `test_codex_models_excluded(self)` (method) — Codex models route through Responses API and don't accept service_tier.
- L165 `test_vendor_prefix_stripped(self)` (method)
- L172 `test_non_priority_models_rejected(self)` (method)
- L187 `test_resolve_overrides_returns_service_tier(self)` (method)
- L196 `test_resolve_overrides_none_for_unsupported(self)` (method)
- L204 `TestFastModeRouting` (class)
- L205 `test_fast_command_exposed_for_model_even_when_provider_is_auto(self)` (method)
- L211 `test_fast_command_exposed_for_non_codex_models(self)` (method)
- L219 `test_turn_route_injects_overrides_without_provider_switch(self)` (method) — Fast mode should add request_overrides but NOT change the provider/runtime.
- L242 `test_turn_route_keeps_primary_runtime_when_model_has_no_fast_backend(self)` (method)
- L262 `TestAnthropicFastMode` (class) — Verify Anthropic Fast Mode model support and override resolution.
- L265 `test_anthropic_opus_supported(self)` (method)
- L276 `test_anthropic_non_opus46_models_excluded(self)` (method) — The speed=fast parameter is gated to Opus 4.6 — others excluded.
- L293 `test_non_claude_models_not_anthropic_fast(self)` (method) — Non-Claude models should not be treated as Anthropic fast-mode.
- L301 `test_anthropic_variant_tags_stripped(self)` (method)
- L308 `test_resolve_overrides_returns_speed_for_anthropic(self)` (method)
- L317 `test_resolve_overrides_returns_none_for_unsupported_claude(self)` (method) — Opus 4.7/4.8 and other Claude models don't take the speed param.
- L330 `test_resolve_overrides_returns_service_tier_for_openai(self)` (method) — OpenAI models should still get service_tier, not speed.
- L337 `test_is_anthropic_fast_model(self)` (method) — The speed=fast parameter is Opus 4.6 only — other Claude excluded.
- L357 `test_fast_command_exposed_for_anthropic_model(self)` (method)
- L365 `test_fast_command_hidden_for_anthropic_sonnet(self)` (method) — Sonnet doesn't support fast mode (Opus 4.6 only) — /fast must be hidden.
- L374 `test_fast_command_hidden_for_anthropic_opus_47(self)` (method) — Opus 4.7 doesn't take the speed=fast parameter — /fast must hide.
- L383 `test_fast_command_hidden_for_non_claude_non_openai(self)` (method) — Non-Claude, non-OpenAI models should not expose /fast.
- L392 `test_turn_route_injects_speed_for_anthropic(self)` (method) — Anthropic models should get speed:'fast' override, not service_tier.
- L413 `TestAnthropicFastModeAdapter` (class) — Verify build_anthropic_kwargs handles fast_mode parameter.
- L416 `test_fast_mode_adds_speed_and_beta(self)` (method)
- L432 `test_fast_mode_off_no_speed(self)` (method)
- L447 `test_fast_mode_skipped_for_third_party_endpoint(self)` (method)
- L464 `test_fast_mode_kwargs_are_safe_for_sdk_unpacking(self)` (method)
- L479 `TestConfigDefault` (class)
- L480 `test_default_config_has_service_tier(self)` (method)
