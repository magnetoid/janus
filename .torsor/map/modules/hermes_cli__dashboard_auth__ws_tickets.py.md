---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/dashboard_auth/ws_tickets.py

Symbols in `hermes_cli/dashboard_auth/ws_tickets.py`.

- L58 `TicketInvalid` (class) — Ticket missing, expired, or already consumed.
- L62 `mint_ticket(*, user_id: str, provider: str)` (function) — Generate a one-shot ticket bound to this user identity.
- L81 `consume_ticket(ticket: str)` (function) — Validate and consume. Raises :class:`TicketInvalid` on missing/expired/used.
- L102 `_gc_expired_locked()` (function) — Drop expired tickets. Caller must hold ``_lock``.
- L110 `internal_ws_credential()` (function) — Return the process-lifetime internal WS credential, minting it once.
- L129 `consume_internal_credential(value: str)` (function) — Validate an internal credential. Raises :class:`TicketInvalid` on mismatch.
- L156 `_reset_for_tests()` (function) — Test-only: drop all tickets and the internal credential.
