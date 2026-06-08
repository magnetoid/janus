---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_gateway_command_help.py

Symbols in `tests/gateway/test_gateway_command_help.py`.

- L10 `_make_event(text: str, platform: Platform)` (function)
- L23 `_make_runner()` (function)
- L29 `test_start_is_known_gateway_command()` (function) — Telegram sends /start automatically; gateway should intercept it as a no-op.
- L40 `test_help_sanitizes_slash_command_mentions_for_telegram(monkeypatch)` (function) — Telegram help output must not expose invalid uppercase/hyphenated slashes.
- L61 `test_commands_sanitizes_slash_command_mentions_for_telegram(monkeypatch)` (function) — Paginated Telegram /commands output uses Telegram-valid slash mentions.
- L77 `test_help_keeps_non_telegram_slash_command_mentions_unchanged(monkeypatch)` (function) — Only Telegram needs slash mentions rewritten to Telegram command names.
