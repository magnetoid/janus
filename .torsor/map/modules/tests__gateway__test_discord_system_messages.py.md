---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_discord_system_messages.py

Symbols in `tests/gateway/test_discord_system_messages.py`.

- L10 `_make_author(*, bot: bool=False, is_self: bool=False)` (function) — Create a mock Discord author.
- L20 `_make_message(*, author=None, content='hello', msg_type=None)` (function) — Create a mock Discord message with a specific type.
- L36 `TestDiscordSystemMessageFilter` (class) — Test that Discord system messages (thread renames, pins, etc.) are ignored.
- L39 `_run_filter(self, message, client_user=None)` (method) — Simulate the on_message filter logic and return whether message was accepted.
- L56 `test_default_messages_accepted(self)` (method) — Regular user messages (type=default) should be accepted.
- L61 `test_reply_messages_accepted(self)` (method) — Reply messages (type=reply) should be accepted — users reply to bot messages.
- L66 `test_thread_rename_ignored(self)` (method) — Thread rename system messages should be ignored.
- L71 `test_pins_add_ignored(self)` (method) — Pin notifications should be ignored.
- L76 `test_new_member_ignored(self)` (method) — New member join messages should be ignored.
- L81 `test_premium_guild_subscription_ignored(self)` (method) — Boost messages should be ignored.
- L86 `test_recipient_add_ignored(self)` (method) — Group DM recipient add messages should be ignored.
- L91 `test_own_default_messages_still_ignored(self)` (method) — Bot's own messages should still be ignored even if type is default.
