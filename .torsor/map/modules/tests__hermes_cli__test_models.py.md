---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_models.py

Symbols in `tests/hermes_cli/test_models.py`.

- L23 `TestModelIds` (class)
- L24 `test_returns_non_empty_list(self)` (method)
- L30 `test_ids_match_fetched_catalog(self)` (method)
- L36 `test_all_ids_contain_provider_slash(self)` (method) — Model IDs should follow the provider/model format.
- L42 `test_no_duplicate_ids(self)` (method)
- L51 `TestOpenRouterModels` (class)
- L52 `test_structure_is_list_of_tuples(self)` (method)
- L60 `TestFetchOpenRouterModels` (class)
- L61 `test_live_fetch_recomputes_free_tags(self, monkeypatch)` (method)
- L82 `test_falls_back_to_static_snapshot_on_fetch_failure(self, monkeypatch)` (method)
- L89 `test_filters_out_models_without_tool_support(self, monkeypatch)` (method) — Models whose supported_parameters omits 'tools' must not appear in the picker.
- L138 `test_permissive_when_supported_parameters_missing(self, monkeypatch)` (method) — Models missing the supported_parameters field keep appearing in the picker.
- L171 `TestOpenRouterToolSupportHelper` (class) — Unit tests for _openrouter_model_supports_tools (Kilo port #9068).
- L174 `test_tools_in_supported_parameters(self)` (method)
- L180 `test_tools_missing_from_supported_parameters(self)` (method)
- L186 `test_supported_parameters_absent_is_permissive(self)` (method) — Missing field → allow (so older / non-OR gateways still work).
- L191 `test_supported_parameters_none_is_permissive(self)` (method)
- L195 `test_supported_parameters_malformed_is_permissive(self)` (method) — Malformed (non-list) value → allow rather than silently drop.
- L202 `test_non_dict_item_is_permissive(self)` (method)
- L207 `test_empty_supported_parameters_list_drops_model(self)` (method) — Explicit empty list → no tools → drop.
- L215 `TestFindOpenrouterSlug` (class)
- L216 `test_exact_match(self)` (method)
- L221 `test_bare_name_match(self)` (method)
- L227 `test_case_insensitive(self)` (method)
- L233 `test_unknown_returns_none(self)` (method)
- L239 `TestDetectProviderForModel` (class)
- L240 `test_anthropic_model_detected(self)` (method) — claude-opus-4-6 should resolve to anthropic provider.
- L247 `test_deepseek_model_detected(self)` (method) — deepseek-chat should resolve to deepseek provider.
- L254 `test_current_provider_model_returns_none(self)` (method) — Models belonging to the current provider should not trigger a switch.
- L258 `test_short_alias_resolves_to_static_model(self)` (method) — Short aliases (e.g. sonnet) should resolve without network lookups.
- L269 `test_openrouter_slug_match(self)` (method) — Models in the OpenRouter catalog should be found.
- L277 `test_bare_name_gets_openrouter_slug(self, monkeypatch)` (method)
- L292 `test_unknown_model_returns_none(self)` (method) — Completely unknown model names should return None.
- L297 `test_aggregator_not_suggested(self)` (method) — nous/openrouter should never be auto-suggested as target provider.
- L305 `TestIsNousFreeTier` (class) — Tests for is_nous_free_tier — account tier detection.
- L308 `test_paid_service_access_allowed_true_is_not_free(self)` (method)
- L311 `test_paid_service_access_allowed_false_is_free(self)` (method)
- L314 `test_paid_service_access_paid_access_fallback(self)` (method)
- L317 `test_paid_plus_tier(self)` (method)
- L320 `test_free_tier_by_charge(self)` (method)
- L323 `test_no_charge_field_not_free(self)` (method) — Missing monthly_charge defaults to not-free (don't block users).
- L327 `test_plan_name_alone_not_free(self)` (method) — Plan name alone is not enough — monthly_charge is required.
- L331 `test_empty_subscription_not_free(self)` (method) — Empty subscription dict defaults to not-free (don't block users).
- L335 `test_no_subscription_not_free(self)` (method) — Missing subscription key returns False.
- L339 `test_empty_response_not_free(self)` (method) — Completely empty response defaults to not-free.
- L344 `TestPartitionNousModelsByTier` (class) — Tests for partition_nous_models_by_tier — free vs paid tier model split.
- L350 `test_paid_tier_all_selectable(self)` (method) — Paid users get all models as selectable, none unavailable.
- L358 `test_free_tier_splits_correctly(self)` (method) — Free users see only free models; paid ones are unavailable.
- L370 `test_no_pricing_returns_all(self)` (method) — Without pricing data, all models are selectable.
- L377 `test_all_free_models(self)` (method) — When all models are free, free-tier users can select all.
- L385 `test_all_paid_models(self)` (method) — When all models are paid, free-tier users have none selectable.
- L394 `TestUnionWithPortalFreeRecommendations` (class) — Tests for union_with_portal_free_recommendations.
- L406 `_payload(self, free_models: list[str])` (method)
- L413 `test_adds_portal_free_model_missing_from_curated(self)` (method) — A Portal-advertised free model not in curated is appended + priced free.
- L431 `test_does_not_duplicate_curated_entries(self)` (method) — A Portal free model already in curated is not duplicated.
- L447 `test_then_partition_keeps_portal_free_model(self)` (method) — End-to-end: Portal-flagged free model survives partition.
- L464 `test_empty_payload_returns_inputs_unchanged(self)` (method) — Empty Portal response leaves curated + pricing untouched.
- L473 `test_missing_freeRecommendedModels_key(self)` (method) — Portal payload without freeRecommendedModels degrades gracefully.
- L485 `test_fetch_failure_returns_inputs(self)` (method) — Network failures don't blow up the picker.
- L497 `test_invalid_entries_skipped(self)` (method) — Non-dict / missing-modelName entries are filtered out.
- L517 `TestUnionWithPortalPaidRecommendations` (class) — Tests for union_with_portal_paid_recommendations.
- L531 `_payload(self, paid_models: list[str])` (method)
- L538 `test_adds_portal_paid_model_missing_from_curated(self)` (method) — A Portal-advertised paid model not in curated is appended.
- L554 `test_does_not_synthesize_pricing_for_paid_models(self)` (method) — Paid recommendations missing from live pricing get no synthetic entry.
- L574 `test_does_not_duplicate_curated_entries(self)` (method) — A Portal paid model already in curated is not duplicated.
- L590 `test_empty_payload_returns_inputs_unchanged(self)` (method) — Empty Portal response leaves curated + pricing untouched.
- L599 `test_missing_paidRecommendedModels_key(self)` (method) — Portal payload without paidRecommendedModels degrades gracefully.
- L611 `test_fetch_failure_returns_inputs(self)` (method) — Network failures don't blow up the picker.
- L623 `test_invalid_entries_skipped(self)` (method) — Non-dict / missing-modelName entries are filtered out.
- L643 `test_preserves_relative_order_of_new_paid_models(self)` (method) — Multiple new paid models are appended in payload order, after curated.
- L659 `TestCheckNousFreeTierCache` (class) — Tests for the TTL cache on check_nous_free_tier().
- L662 `setup_method(self)` (method)
- L665 `teardown_method(self)` (method)
- L669 `test_result_is_cached(self, mock_account)` (method) — Second call within TTL returns cached result without account lookup.
- L685 `test_cache_expires_after_ttl(self, mock_account)` (method) — After TTL expires, account info is resolved again.
- L706 `test_force_fresh_bypasses_cache(self, mock_account)` (method)
- L720 `test_cache_ttl_is_short(self)` (method) — TTL should be short enough to catch upgrades quickly (<=5 min).
- L725 `TestNousRecommendedModels` (class) — Tests for fetch_nous_recommended_models + get_nous_recommended_aux_model.
- L743 `setup_method(self)` (method)
- L746 `teardown_method(self)` (method)
- L749 `_mock_urlopen(self, payload)` (method) — Return a context-manager mock mimicking urllib.request.urlopen().
- L759 `test_fetch_caches_per_portal_url(self)` (method)
- L769 `test_fetch_cache_is_keyed_per_portal(self)` (method)
- L777 `test_fetch_returns_empty_on_network_failure(self)` (method)
- L783 `test_fetch_force_refresh_bypasses_cache(self)` (method)
- L791 `test_get_aux_model_returns_vision_recommendation(self)` (method)
- L801 `test_get_aux_model_returns_compaction_recommendation(self)` (method)
- L812 `test_get_aux_model_returns_none_when_field_null(self)` (method)
- L823 `test_get_aux_model_returns_none_on_empty_payload(self)` (method)
- L829 `test_get_aux_model_returns_none_when_modelname_blank(self)` (method)
- L838 `test_paid_tier_prefers_paid_recommendation(self)` (method) — Paid-tier users should get the paid model when it's populated.
- L853 `test_paid_tier_falls_back_to_free_when_paid_is_null(self)` (method) — If the Portal returns null for the paid field, fall back to free.
- L868 `test_free_tier_never_uses_paid_recommendation(self)` (method) — Free-tier users must not get paid-only recommendations.
- L880 `test_auto_detects_tier_when_not_supplied(self)` (method) — Default behaviour: call check_nous_free_tier() to pick the tier.
- L898 `test_tier_detection_error_defaults_to_paid(self)` (method) — If tier detection raises, assume paid so we don't downgrade silently.
