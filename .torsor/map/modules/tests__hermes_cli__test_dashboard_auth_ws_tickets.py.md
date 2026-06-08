---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_ws_tickets.py

Symbols in `tests/hermes_cli/test_dashboard_auth_ws_tickets.py`.

- L25 `_reset()` (function)
- L36 `TestMintAndConsume` (class)
- L37 `test_round_trip(self)` (method)
- L44 `test_ticket_has_minimum_length(self)` (method)
- L50 `test_ticket_values_are_unique(self)` (method)
- L60 `TestSingleUse` (class)
- L61 `test_second_consume_raises(self)` (method)
- L67 `test_unknown_ticket_rejected(self)` (method)
- L71 `test_empty_ticket_rejected(self)` (method)
- L81 `TestTTL` (class)
- L82 `test_constant_is_30_seconds(self)` (method)
- L86 `test_expired_ticket_rejected(self, monkeypatch)` (method)
- L102 `test_at_exact_ttl_boundary_still_valid(self, monkeypatch)` (method)
- L118 `TestErrorMessages` (class)
- L119 `test_unknown_ticket_error_truncates_value(self)` (method)
- L135 `TestConcurrency` (class)
- L136 `test_mint_and_consume_concurrent(self)` (method)
- L172 `TestInternalCredential` (class)
- L173 `test_minted_once_is_stable(self)` (method) — Successive calls return the same process-lifetime value.
- L180 `test_round_trip_identity(self)` (method)
- L186 `test_multi_use(self)` (method) — Unlike a single-use ticket, the credential survives repeated consume.
- L195 `test_rejected_before_mint(self)` (method) — With nothing minted yet, any value is rejected (expected is None).
- L201 `test_empty_value_rejected(self)` (method)
- L206 `test_wrong_value_rejected(self)` (method)
- L211 `test_reset_clears_and_remints(self)` (method)
- L224 `test_independent_of_ticket_store(self)` (method) — The internal credential is not a ticket — minting tickets doesn't
