---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_clarify_gateway.py

Symbols in `tests/tools/test_clarify_gateway.py`.

- L17 `_clear_clarify_state()` (function) — Reset module-level state between tests.
- L26 `TestClarifyPrimitive` (class) — Core register/wait/resolve mechanics.
- L29 `setup_method(self)` (method)
- L32 `test_button_choice_resolves_wait(self)` (method) — resolve_gateway_clarify unblocks wait_for_response with the chosen string.
- L46 `test_open_ended_auto_awaits_text(self)` (method) — Clarify with no choices is in text-capture mode immediately.
- L59 `test_button_choice_does_not_auto_await(self)` (method) — Multi-choice clarify should NOT be in text-capture mode initially.
- L67 `test_other_button_flips_to_text_mode(self)` (method) — mark_awaiting_text makes get_pending_for_session find the entry.
- L81 `test_mark_awaiting_text_unknown_id(self)` (method) — mark_awaiting_text on a non-existent id returns False.
- L87 `test_timeout_returns_none(self)` (method) — wait_for_response returns None when no resolve fires within the timeout.
- L95 `test_resolve_unknown_id_returns_false(self)` (method) — resolve_gateway_clarify is idempotent on unknown ids.
- L101 `test_resolve_after_wait_completes_is_noop(self)` (method) — A late resolve on a finished entry doesn't blow up.
- L112 `test_clear_session_cancels_pending_entries(self)` (method) — clear_session unblocks blocked threads with empty response.
- L130 `test_has_pending(self)` (method)
- L137 `test_notify_register_unregister_clears_pending(self)` (method) — unregister_notify cancels any pending clarify so threads unwind.
- L157 `test_session_index_isolation(self)` (method) — Entries from different sessions don't leak across get_pending lookups.
- L169 `test_clarify_timeout_config_default(self)` (method) — get_clarify_timeout returns 600 by default.
- L180 `TestGatewayTextIntercept` (class) — The gateway's _handle_message intercepts text replies to pending clarifies.
- L183 `setup_method(self)` (method)
- L186 `test_get_pending_for_session_returns_oldest_text_awaiting(self)` (method) — When two clarifies are pending, get_pending_for_session returns the
- L207 `test_text_fallback_enables_awaiting_text_for_multi_choice(self)` (method) — When base send_clarify renders choices as text, mark_awaiting_text
