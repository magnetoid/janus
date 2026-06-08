---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_matrix_approval_reaction_fail_closed.py

Symbols in `tests/gateway/test_matrix_approval_reaction_fail_closed.py`.

- L23 `_stub_mautrix()` (function)
- L49 `_make_adapter(allowed_user_ids=None)` (function) — Construct a MatrixAdapter with only the state needed by _on_reaction.
- L62 `_make_event(sender, reacts_to, key='✅')` (function) — Minimal Matrix reaction event.
- L72 `_make_prompt(chat_id='!testroom:matrix.org')` (function)
- L80 `_run(adapter, event)` (function) — Run _on_reaction and return whether the prompt was resolved.
- L99 `TestApprovalReactionFailClosed` (class) — _on_reaction approval auth must be fail-closed (parity with Telegram).
- L102 `test_no_allowlist_no_allow_all_denies(self, monkeypatch)` (method) — No MATRIX_ALLOWED_USERS + no GATEWAY_ALLOW_ALL_USERS → deny.
- L110 `test_no_allowlist_allow_all_permits(self, monkeypatch)` (method) — No MATRIX_ALLOWED_USERS + GATEWAY_ALLOW_ALL_USERS=true → allow.
- L118 `test_listed_sender_permits(self, monkeypatch)` (method) — Sender in MATRIX_ALLOWED_USERS → allow.
- L125 `test_unlisted_sender_denies(self, monkeypatch)` (method) — Sender not in MATRIX_ALLOWED_USERS → deny.
