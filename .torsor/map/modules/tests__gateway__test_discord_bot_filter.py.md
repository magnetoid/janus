---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_bot_filter.py

Symbols in `tests/gateway/test_discord_bot_filter.py`.

- L8 `_make_author(*, bot: bool=False, is_self: bool=False)` (function) — Create a mock Discord author.
- L18 `_make_message(*, author=None, content='hello', mentions=None, is_dm=False)` (function) — Create a mock Discord message.
- L40 `TestDiscordBotFilter` (class) — Test the DISCORD_ALLOW_BOTS filtering logic.
- L43 `_run_filter(self, message, allow_bots='none', client_user=None)` (method) — Simulate the on_message filter logic and return whether message was accepted.
- L60 `test_own_messages_always_ignored(self)` (method) — Bot's own messages are always ignored regardless of allow_bots.
- L66 `test_human_messages_always_accepted(self)` (method) — Human messages are always accepted regardless of allow_bots.
- L74 `test_allow_bots_none_rejects_bots(self)` (method) — With allow_bots=none, all other bot messages are rejected.
- L80 `test_allow_bots_all_accepts_bots(self)` (method) — With allow_bots=all, all bot messages are accepted.
- L86 `test_allow_bots_mentions_rejects_without_mention(self)` (method) — With allow_bots=mentions, bot messages without @mention are rejected.
- L93 `test_allow_bots_mentions_accepts_with_mention(self)` (method) — With allow_bots=mentions, bot messages with @mention are accepted.
- L100 `test_default_is_none(self)` (method) — Default behavior (no env var) should be 'none'.
- L105 `test_case_insensitive(self)` (method) — Allow_bots value should be case-insensitive.
