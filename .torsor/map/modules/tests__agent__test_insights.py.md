---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_insights.py

Symbols in `tests/agent/test_insights.py`.

- L17 `db(tmp_path)` (function) — Create a SessionDB with a temp database file.
- L26 `populated_db(db)` (function) — Create a DB with realistic session data for insights testing.
- L139 `TestHasKnownPricing` (class)
- L140 `test_known_commercial_model(self)` (method)
- L145 `test_unknown_custom_model(self)` (method)
- L152 `test_heuristic_matched_models_are_not_considered_known(self)` (method)
- L157 `TestEstimateCost` (class)
- L158 `test_basic_cost(self)` (method)
- L168 `test_zero_tokens(self)` (method)
- L173 `test_cache_aware_usage(self)` (method)
- L191 `TestFormatDuration` (class)
- L192 `test_seconds(self)` (method)
- L195 `test_minutes(self)` (method)
- L198 `test_hours_with_minutes(self)` (method)
- L202 `test_exact_hours(self)` (method)
- L205 `test_days(self)` (method)
- L210 `TestBarChart` (class)
- L211 `test_basic_bars(self)` (method)
- L218 `test_empty_values(self)` (method)
- L222 `test_all_zeros(self)` (method)
- L226 `test_single_value(self)` (method)
- L236 `TestInsightsEmpty` (class)
- L237 `test_empty_db_returns_empty_report(self, db)` (method)
- L243 `test_empty_db_terminal_format(self, db)` (method)
- L249 `test_empty_db_gateway_format(self, db)` (method)
- L260 `TestInsightsPopulated` (class)
- L261 `test_generate_returns_all_sections(self, populated_db)` (method)
- L273 `test_overview_session_count(self, populated_db)` (method)
- L281 `test_overview_token_totals(self, populated_db)` (method)
- L292 `test_overview_cost_positive(self, populated_db)` (method)
- L297 `test_overview_duration_stats(self, populated_db)` (method)
- L306 `test_model_breakdown(self, populated_db)` (method)
- L321 `test_platform_breakdown(self, populated_db)` (method)
- L334 `test_tool_breakdown(self, populated_db)` (method)
- L354 `test_skill_breakdown(self, populated_db)` (method)
- L371 `test_skill_breakdown_respects_days_filter(self, populated_db)` (method)
- L383 `test_activity_patterns(self, populated_db)` (method)
- L394 `test_top_sessions(self, populated_db)` (method)
- L405 `test_source_filter_cli(self, populated_db)` (method)
- L411 `test_source_filter_telegram(self, populated_db)` (method)
- L417 `test_source_filter_nonexistent(self, populated_db)` (method)
- L423 `test_days_filter_short(self, populated_db)` (method)
- L430 `test_days_filter_long(self, populated_db)` (method)
- L442 `TestTerminalFormatting` (class)
- L443 `test_terminal_format_has_sections(self, populated_db)` (method)
- L456 `test_terminal_format_shows_tokens(self, populated_db)` (method)
- L468 `test_terminal_format_shows_platforms(self, populated_db)` (method)
- L478 `test_terminal_format_shows_bar_chart(self, populated_db)` (method)
- L485 `test_terminal_format_hides_cost_for_custom_models(self, db)` (method) — Cost display is hidden entirely — custom models no longer show 'N/A' either.
- L500 `TestGatewayFormatting` (class)
- L501 `test_gateway_format_is_shorter(self, populated_db)` (method)
- L509 `test_gateway_format_has_bold(self, populated_db)` (method)
- L516 `test_gateway_format_hides_cost(self, populated_db)` (method) — Gateway format omits dollar figures and internal cache details.
- L525 `test_gateway_format_shows_models(self, populated_db)` (method)
- L538 `TestEdgeCases` (class)
- L539 `test_session_with_no_tokens(self, db)` (method) — Sessions with zero tokens should not crash.
- L550 `test_session_with_no_end_time(self, db)` (method) — Active (non-ended) sessions should be included but duration = 0.
- L564 `test_session_with_no_model(self, db)` (method) — Sessions with NULL model should not crash.
- L579 `test_custom_model_shows_zero_cost(self, db)` (method) — Custom/self-hosted models should show $0 cost, not fake estimates.
- L595 `test_tool_usage_from_tool_calls_json(self, db)` (method) — Tool usage should be extracted from tool_calls JSON when tool_name is NULL.
- L630 `test_overview_pricing_sets_are_lists(self, db)` (method) — models_with/without_pricing should be JSON-serializable lists.
- L646 `test_mixed_commercial_and_custom_models(self, db)` (method) — Mix of commercial and custom models: only commercial ones get costs.
- L677 `test_single_session_streak(self, db)` (method) — Single session should have streak of 0 or 1.
- L686 `test_no_tool_calls(self, db)` (method) — Sessions with no tool calls should produce empty tools list.
- L697 `test_only_one_platform(self, db)` (method) — Single-platform usage should still work.
- L712 `test_large_days_value(self, db)` (method) — Very large days value should not crash.
- L721 `test_zero_days(self, db)` (method) — Zero days should return empty (nothing is in the future).
