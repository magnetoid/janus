---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_credits_cold_start.py

Symbols in `tests/agent/test_credits_cold_start.py`.

- L14 `_cold_start_notices(state: CreditsState)` (function) — Mirror the conversation_loop seed: prime seen_below_90 when used_fraction is
- L24 `_state(**kw)` (function)
- L30 `test_cold_start_healthy_no_notice()` (function)
- L40 `test_cold_start_opens_already_at_90pct_warns()` (function) — A session that OPENS already ≥90% must warn immediately — the seed primes
- L52 `test_cold_start_grant_exhausted_warns_and_grant_spent()` (function)
- L64 `test_cold_start_depleted_warns()` (function)
- L73 `test_cold_start_debt_warns_and_depleted()` (function) — Negative subscription balance (the only signed field) → 100% used + depleted.
- L87 `test_cold_start_no_cap_degrades_to_depletion_only()` (function) — Without monthly_credits (older portals) the seed sets no limit → used_fraction
- L98 `test_dev_fixtures_drive_cold_start()` (function) — Every HERMES_DEV_CREDITS_FIXTURE state produces a valid seed CreditsState.
- L124 `_FakeAgent` (class) — Minimal agent surface for the seed helper: state slots + an emit that runs
- L128 `__init__(self, provider='nous')` (method)
- L138 `_emit_credits_notices(self)` (method)
- L145 `_seed(agent, fixture)` (function)
- L159 `test_seed_fires_usage_band_at_session_open()` (function)
- L166 `test_seed_fires_depleted_at_session_open()` (function)
- L172 `test_seed_healthy_no_notice()` (function)
- L178 `test_seed_is_idempotent()` (function)
- L187 `test_seed_skips_non_nous()` (function)
