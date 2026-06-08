---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_credential_pool_routing.py

Symbols in `tests/agent/test_credential_pool_routing.py`.

- L19 `TestCliTurnRoutePool` (class)
- L20 `test_resolve_turn_includes_pool(self)` (method) — CLI's _resolve_turn_agent_config must pass credential_pool in runtime.
- L46 `TestGatewayTurnRoutePool` (class)
- L47 `test_resolve_turn_includes_pool(self)` (method) — Gateway's _resolve_turn_agent_config must pass credential_pool.
- L73 `TestEagerFallbackWithPool` (class) — Test the eager fallback guard in run_agent.py's error handling loop.
- L76 `_make_agent(self, has_pool=True, pool_has_creds=True, has_fallback=True)` (method) — Create a minimal AIAgent mock with the fields needed.
- L96 `test_eager_fallback_deferred_when_pool_has_credentials(self)` (method) — 429 with active pool should NOT trigger eager fallback.
- L110 `test_eager_fallback_fires_when_no_pool(self)` (method) — 429 without pool should trigger eager fallback.
- L123 `test_eager_fallback_fires_when_pool_exhausted(self)` (method) — 429 with exhausted pool should trigger eager fallback.
- L141 `TestPoolRotationCycle` (class) — Verify the retry-same → rotate → exhaust flow in _recover_with_credential_pool.
- L144 `_make_agent_with_pool(self, pool_entries=3)` (method)
- L176 `test_first_429_sets_retry_flag_no_rotation(self)` (method) — First 429 should just set has_retried_429=True, no rotation.
- L186 `test_second_429_rotates_to_next(self)` (method) — Second consecutive 429 should rotate to next credential.
- L197 `test_pool_exhaustion_returns_false(self)` (method) — When all credentials exhausted, recovery should return False.
- L212 `test_402_immediate_rotation(self)` (method) — 402 (billing) should immediately rotate, no retry-first.
- L222 `test_no_pool_returns_false(self)` (method) — No pool should return (False, unchanged).
