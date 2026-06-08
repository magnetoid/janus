---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_forum_commands.py

Symbols in `tests/gateway/test_telegram_forum_commands.py`.

- L12 `_make_test_adapter()` (function) — Build a TelegramAdapter without running __init__.
- L27 `_forum_message(chat_id=-100, is_forum=True)` (function)
- L34 `test_ensure_forum_commands_skips_non_forum()` (function)
- L42 `test_ensure_forum_commands_skips_already_registered()` (function)
- L51 `test_ensure_forum_commands_registers_once()` (function)
- L88 `test_ensure_forum_commands_handles_set_failure()` (function)
- L104 `test_ensure_forum_commands_race_safety()` (function) — Two concurrent coroutines must not double-register the same chat.
