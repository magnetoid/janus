---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_approve_deny_commands.py

Symbols in `tests/gateway/test_approve_deny_commands.py`.

- L24 `_make_source()` (function)
- L34 `_make_event(text: str)` (function)
- L42 `_make_runner()` (function)
- L69 `_clear_approval_state()` (function) — Reset all module-level approval state between tests.
- L84 `TestBlockingGatewayApproval` (class) — Tests for the blocking approval mechanism in tools/approval.py.
- L87 `setup_method(self)` (method)
- L90 `test_register_and_resolve_unblocks_entry(self)` (method) — resolve_gateway_approval signals the entry's event.
- L120 `test_resolve_returns_zero_when_no_pending(self)` (method)
- L124 `test_resolve_all_unblocks_multiple_entries(self)` (method) — resolve_gateway_approval with resolve_all=True signals all entries.
- L140 `test_resolve_single_pops_oldest_fifo(self)` (method) — resolve_gateway_approval without resolve_all resolves oldest first.
- L158 `test_unregister_signals_all_entries(self)` (method) — unregister_gateway_notify signals all waiting entries to prevent hangs.
- L175 `test_clear_session_denies_and_signals_all_entries(self)` (method) — clear_session must wake blocked entries during boundary cleanup.
- L198 `TestApproveCommand` (class)
- L200 `setup_method(self)` (method)
- L204 `test_approve_resolves_blocking_approval(self)` (method) — Basic /approve signals the oldest blocked agent thread.
- L221 `test_approve_all_resolves_multiple(self)` (method) — /approve all resolves all pending approvals.
- L239 `test_approve_all_session(self)` (method) — /approve all session resolves all with session scope.
- L257 `test_approve_no_pending(self)` (method) — /approve with no pending approval returns helpful message.
- L264 `test_approve_stale_old_style_pending(self)` (method) — Old-style _pending_approvals without blocking event reports expired.
- L281 `TestDenyCommand` (class)
- L283 `setup_method(self)` (method)
- L287 `test_deny_resolves_blocking_approval(self)` (method) — /deny signals the oldest blocked agent thread with 'deny'.
- L304 `test_deny_all_resolves_all(self)` (method) — /deny all denies all pending approvals.
- L321 `test_deny_no_pending(self)` (method) — /deny with no pending approval returns helpful message.
- L333 `TestBareTextNoLongerApproves` (class)
- L335 `setup_method(self)` (method)
- L339 `test_yes_does_not_execute_pending_command(self)` (method) — Saying 'yes' must not trigger approval. Only /approve works.
- L359 `TestBlockingApprovalE2E` (class) — Test the full blocking flow: agent thread blocks → user approves → agent resumes.
- L362 `setup_method(self)` (method)
- L370 `test_blocking_approval_approve_once(self)` (method) — check_all_command_guards blocks until resolve_gateway_approval is called.
- L419 `test_blocking_approval_deny(self)` (method) — check_all_command_guards returns BLOCKED when denied.
- L463 `test_blocking_approval_timeout(self)` (method) — check_all_command_guards returns BLOCKED on timeout.
- L502 `test_parallel_subagent_approvals(self)` (method) — Multiple threads can block concurrently and be resolved independently.
- L561 `test_parallel_mixed_approve_deny(self)` (method) — Approve some, deny others in a parallel batch.
- L625 `TestFallbackNoCallback` (class)
- L627 `setup_method(self)` (method)
- L630 `test_no_callback_returns_approval_required(self)` (method) — Without a registered callback, the fallback returns pending_approval.
