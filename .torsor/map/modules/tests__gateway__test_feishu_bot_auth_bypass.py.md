---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_feishu_bot_auth_bypass.py

Symbols in `tests/gateway/test_feishu_bot_auth_bypass.py`.

- L19 `_isolate_feishu_env(monkeypatch)` (function)
- L30 `_make_bare_runner()` (function)
- L38 `_make_feishu_bot_source(open_id: str='ou_peer')` (function)
- L49 `_make_feishu_human_source(open_id: str='ou_human')` (function)
- L60 `test_feishu_bot_authorized_when_allow_bots_mentions(monkeypatch)` (function)
- L68 `test_feishu_bot_authorized_when_allow_bots_all(monkeypatch)` (function)
- L76 `test_feishu_bot_NOT_authorized_when_allow_bots_none(monkeypatch)` (function)
- L84 `test_feishu_bot_NOT_authorized_when_allow_bots_unset(monkeypatch)` (function)
- L91 `test_feishu_human_still_checked_against_allowlist_when_bot_policy_set(monkeypatch)` (function) — FEISHU_ALLOW_BOTS=all must NOT open the gate for humans.
- L101 `test_feishu_bot_bypass_does_not_leak_to_other_platforms(monkeypatch)` (function) — FEISHU_ALLOW_BOTS=all must not authorize Telegram/Discord bot sources.
