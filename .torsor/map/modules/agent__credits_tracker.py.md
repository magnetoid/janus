---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/credits_tracker.py

Symbols in `agent/credits_tracker.py`.

- L62 `_safe_int(value: Any)` (function) — Parse a header value to an exact int (money-safe).
- L83 `_validate_usd(value: Optional[str])` (function) — Return True iff value is a non-None string matching ^-?\d+\.\d{2}$.
- L94 `CreditsState` (class) — Full credits state parsed from x-nous-credits-* response headers.
- L117 `has_data(self)` (method)
- L121 `age_seconds(self)` (method)
- L127 `depleted(self)` (method) — True when the account has lost paid access.
- L137 `used_fraction(self)` (method) — Fraction of the subscription cap consumed, in [0.0, 1.0].
- L178 `AgentNotice` (class) — A structured, driver-agnostic out-of-band notice.
- L200 `evaluate_credits_notices(state: CreditsState, latch: dict)` (function) — Reconcile credits notices against the latch. Mutates ``latch`` IN PLACE.
- L319 `parse_credits_headers(headers: Mapping[str, str], provider: str='')` (function) — Parse x-nous-credits-* (and x-nous-tool-pool-*) headers into a CreditsState.
- L574 `dev_fixture_credits_state()` (function) — Return a fixture CreditsState for HERMES_DEV_CREDITS_FIXTURE, or None.
- L610 `_credits_state_from_account(info)` (function) — Map a NousPortalAccountInfo into a header-shaped CreditsState for the seed.
- L651 `_hydrate_seed_state(agent, state)` (function) — Install a seed CreditsState on the agent and fire the notice policy once.
- L670 `seed_credits_at_session_start(agent)` (function) — Hydrate agent._credits_state from /api/oauth/account (or a dev fixture) and
