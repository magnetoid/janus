---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_callback_auth_fail_closed.py

Symbols in `tests/gateway/test_telegram_callback_auth_fail_closed.py`.

- L21 `_TelegramError` (class)
- L49 `_inject_fake_telegram(monkeypatch)` (function)
- L57 `_make_adapter()` (function)
- L69 `TestCallbackAuthFailClosed` (class) — _is_callback_user_authorized fallback must be fail-closed.
- L72 `test_no_allowlist_no_allow_all_denies(self, monkeypatch)` (method) — No TELEGRAM_ALLOWED_USERS and no GATEWAY_ALLOW_ALL_USERS → deny.
- L81 `test_no_allowlist_with_global_allow_all_permits(self, monkeypatch)` (method) — No TELEGRAM_ALLOWED_USERS but GATEWAY_ALLOW_ALL_USERS=true → allow.
- L89 `test_allowlist_with_matching_user_permits(self, monkeypatch)` (method) — TELEGRAM_ALLOWED_USERS contains the user → allow.
- L96 `test_allowlist_without_matching_user_denies(self, monkeypatch)` (method) — TELEGRAM_ALLOWED_USERS does not contain the user → deny.
- L103 `test_allowlist_wildcard_permits(self, monkeypatch)` (method) — TELEGRAM_ALLOWED_USERS=* → allow everyone.
