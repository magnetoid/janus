---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/e2e/test_discord_adapter.py

Symbols in `tests/e2e/test_discord_adapter.py`.

- L24 `dispatch(adapter, msg)` (function)
- L29 `TestMentionStrippedCommandDispatch` (class)
- L30 `test_mention_then_command(self, discord_adapter, bot_user)` (method) — <@BOT> /help → mention stripped, /help dispatched.
- L41 `test_nickname_mention_then_command(self, discord_adapter, bot_user)` (method) — <@!BOT> /help → nickname mention also stripped, /help works.
- L52 `test_text_before_command_not_detected(self, discord_adapter, bot_user)` (method) — '<@BOT> something else /help' → mention stripped, but 'something else /help'
- L66 `test_no_mention_in_channel_dropped(self, discord_adapter)` (method) — Message without @mention in server channel → silently dropped.
- L72 `test_dm_no_mention_needed(self, discord_adapter)` (method) — DMs don't require @mention — /help works directly.
- L82 `TestAutoThreadingPreservesCommand` (class)
- L83 `test_command_detected_after_auto_thread(self, discord_adapter, bot_user, monkeypatch)` (method) — @mention /help in channel with auto-thread → thread created AND command dispatched.
