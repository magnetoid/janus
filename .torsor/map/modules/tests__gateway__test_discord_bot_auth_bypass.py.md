---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_bot_auth_bypass.py

Symbols in `tests/gateway/test_discord_bot_auth_bypass.py`.

- L24 `_isolate_discord_env(monkeypatch)` (function) — Make every test start with a clean Discord env so prior tests in the
- L45 `_make_bare_runner()` (function) — Build a GatewayRunner skeleton with just enough wiring for the auth test.
- L60 `_make_discord_bot_source(bot_id: str='999888777')` (function)
- L71 `_make_discord_human_source(user_id: str='100200300')` (function)
- L82 `test_discord_bot_authorized_when_allow_bots_mentions(monkeypatch)` (function) — DISCORD_ALLOW_BOTS=mentions must authorize a bot sender even when
- L100 `test_discord_bot_authorized_when_allow_bots_all(monkeypatch)` (function) — DISCORD_ALLOW_BOTS=all is a superset of =mentions — should also bypass.
- L111 `test_discord_bot_NOT_authorized_when_allow_bots_none(monkeypatch)` (function) — DISCORD_ALLOW_BOTS=none (default) must still reject bots that aren't
- L124 `test_discord_bot_NOT_authorized_when_allow_bots_unset(monkeypatch)` (function) — Unset DISCORD_ALLOW_BOTS must behave like 'none'.
- L135 `test_discord_human_still_checked_against_allowlist_when_bot_policy_set(monkeypatch)` (function) — DISCORD_ALLOW_BOTS=all must NOT open the gate for humans — they
- L153 `test_bot_bypass_does_not_leak_to_other_platforms(monkeypatch)` (function) — The is_bot bypass is Discord-specific — a Telegram bot source with
- L184 `test_discord_role_config_does_not_bypass_gateway_allowlist(monkeypatch)` (function) — DISCORD_ALLOWED_ROLES alone must NOT authorize at the gateway layer
- L200 `test_discord_user_allowlist_still_authorizes_when_role_is_also_configured(monkeypatch)` (function) — Sanity: DISCORD_ALLOWED_USERS still authorizes users on the list,
- L215 `test_discord_role_config_does_not_leak_to_other_platforms(monkeypatch)` (function) — DISCORD_ALLOWED_ROLES must only affect Discord. Setting it should
