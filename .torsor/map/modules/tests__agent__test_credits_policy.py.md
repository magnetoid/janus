---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_credits_policy.py

Symbols in `tests/agent/test_credits_policy.py`.

- L23 `fresh_latch()` (function)
- L27 `state_with_fraction(uf: float | None, *, paid_access: bool=True, denominator_kind: str='subscription_cap', purchased_micros: int=0, purchased_usd: str='0.00', subscription_limit_usd: str | None='20.00')` (function) — Build a minimal CreditsState that yields the desired used_fraction.
- L69 `TestWarn90Crossing` (class)
- L70 `test_below_lowest_band_no_notice_but_latch_set(self)` (method)
- L78 `test_crossing_to_90_fires_once(self)` (method)
- L90 `test_no_refire_on_repeated_over_90(self)` (method)
- L105 `TestWarn90RecoveryReCross` (class)
- L106 `test_recovery_clears_warn90(self)` (method)
- L116 `test_recross_after_recovery_fires_again(self)` (method)
- L130 `TestOpenAlreadyOver` (class)
- L131 `test_warn90_does_not_fire_without_seen_below_90(self)` (method) — First call uf≥0.9 with seen_below_90=False — warn90 must NOT fire.
- L144 `TestBoundaryFractions` (class)
- L145 `test_exact_0_9_fires_warn90(self)` (method) — used_fraction == 0.9 exactly must fire warn90 (threshold is inclusive).
- L166 `test_just_below_1_0_does_not_fire_grant_spent(self)` (method) — subscription_micros = limit - 1 (used_fraction just under 1.0) must NOT fire grant_spent.
- L192 `TestGrantSpent` (class)
- L193 `_grant_state(self, purchased_micros: int=12340000)` (method)
- L201 `test_grant_spent_fires_on_first_obs(self)` (method) — No crossing gate for grant_spent — fires immediately on first obs.
- L208 `test_grant_spent_no_refire(self)` (method)
- L215 `test_grant_spent_clears_when_purchased_zero(self)` (method)
- L233 `TestDepleted` (class)
- L234 `test_depleted_fires_level_error_kind_sticky(self)` (method)
- L244 `test_recovery_emits_clear_and_restored(self)` (method)
- L258 `test_depleted_refires_after_recovery(self)` (method)
- L271 `TestDenominatorNone` (class)
- L272 `test_no_warn90_when_uf_none(self)` (method)
- L279 `test_no_grant_spent_when_uf_none(self)` (method)
- L290 `test_warn90_clears_when_uf_becomes_none(self)` (method) — If warn90 was active and uf becomes None, it should clear.
- L307 `TestNoticeCopy` (class)
- L308 `test_warn90_contains_verbatim_subscription_limit_usd(self)` (method)
- L317 `test_grant_spent_contains_verbatim_purchased_usd(self)` (method)
- L330 `test_depleted_mentions_usage_command(self)` (method)
- L341 `TestSeverityOrder` (class)
- L342 `test_multiple_new_notices_ordered_ascending_severity(self)` (method) — warn90 < grant_spent < depleted in to_show when all fire in one call.
- L376 `TestNoFireAndClearSameKey` (class)
- L377 `test_usage_never_both_fired_and_cleared(self)` (method)
- L394 `test_depleted_never_both_fired_and_cleared(self)` (method)
- L412 `TestUsageBands` (class) — The usage notice shows the HIGHEST crossed band as a single escalating line.
- L415 `_band_text(self, to_show)` (method)
- L419 `test_50_band_fires_info(self)` (method)
- L427 `test_75_band_fires_warn(self)` (method)
- L435 `test_climb_replaces_band(self)` (method) — Climbing 50→75→90 replaces the single line (clear old + show new).
- L453 `test_step_down_on_recovery(self)` (method) — Recovering steps the band back down, then clears below the lowest band.
- L471 `test_no_refire_same_band(self)` (method)
- L480 `test_exact_band_boundaries_inclusive(self)` (method) — Thresholds are inclusive: exactly 0.50 / 0.75 / 0.90 land in their band.
- L488 `test_open_below_lowest_band_no_notice(self)` (method)
