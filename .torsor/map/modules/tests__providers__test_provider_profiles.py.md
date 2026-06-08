---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/providers/test_provider_profiles.py

Symbols in `tests/providers/test_provider_profiles.py`.

- L7 `TestRegistry` (class)
- L8 `test_discovery_populates_registry(self)` (method)
- L13 `test_alias_lookup(self)` (method)
- L22 `test_unknown_provider_returns_none(self)` (method)
- L25 `test_all_providers_have_name(self)` (method)
- L31 `TestNvidiaProfile` (class)
- L32 `test_max_tokens(self)` (method)
- L36 `test_no_special_temperature(self)` (method)
- L40 `test_base_url(self)` (method)
- L44 `test_billing_header_not_profile_wide(self)` (method)
- L49 `TestKimiProfile` (class)
- L50 `test_temperature_omit(self)` (method)
- L54 `test_max_tokens(self)` (method)
- L58 `test_cn_separate_profile(self)` (method)
- L64 `test_cn_not_alias_of_kimi(self)` (method)
- L70 `test_thinking_enabled(self)` (method)
- L78 `test_thinking_disabled(self)` (method)
- L84 `test_reasoning_effort_default(self)` (method)
- L91 `test_no_config_defaults(self)` (method)
- L99 `TestOpenRouterProfile` (class)
- L100 `test_extra_body_with_prefs(self)` (method)
- L105 `test_extra_body_session_id(self)` (method)
- L110 `test_extra_body_no_prefs(self)` (method)
- L115 `test_pareto_min_coding_score_emitted_for_pareto_model(self)` (method) — min_coding_score → plugins block when model is openrouter/pareto-code.
- L126 `test_pareto_score_ignored_for_other_models(self)` (method) — Score has no effect on any other model — plugins block must not appear.
- L135 `test_pareto_score_unset_omits_plugins(self)` (method) — Empty/None score → no plugins block (router uses its omission default).
- L145 `test_pareto_score_out_of_range_dropped(self)` (method) — Invalid scores are silently dropped — never forwarded to OR.
- L155 `test_reasoning_full_config(self)` (method)
- L163 `test_reasoning_disabled_still_passes(self)` (method) — OpenRouter passes disabled reasoning through (unlike Nous).
- L172 `test_default_reasoning(self)` (method)
- L177 `test_grok_session_id_sets_cache_affinity_header(self)` (method) — OpenRouter + Grok model + session_id => x-grok-conv-id header.
- L186 `test_grok_xai_prefix_also_supported(self)` (method) — xai/ prefix (without dash) should also get the header.
- L195 `test_non_grok_model_no_affinity_header(self)` (method) — OpenRouter + non-Grok model => no x-grok-conv-id header.
- L205 `test_grok_without_session_id_no_header(self)` (method) — Grok model but no session_id => no header (nothing to pin).
- L211 `test_grok_reasoning_and_header_together(self)` (method) — Reasoning extra_body and Grok header should coexist.
- L224 `TestNousProfile` (class)
- L225 `test_tags(self)` (method)
- L231 `test_auth_type(self)` (method)
- L235 `test_reasoning_enabled(self)` (method)
- L243 `test_reasoning_omitted_when_disabled(self)` (method)
- L252 `TestQwenProfile` (class)
- L253 `test_max_tokens(self)` (method)
- L257 `test_auth_type(self)` (method)
- L261 `test_extra_body_vl(self)` (method)
- L266 `test_prepare_messages_normalizes_content(self)` (method)
- L281 `test_metadata_top_level(self)` (method)
- L289 `TestBaseProfile` (class)
- L290 `test_prepare_messages_passthrough(self)` (method)
- L295 `test_build_extra_body_empty(self)` (method)
- L299 `test_build_api_kwargs_extras_empty(self)` (method)
