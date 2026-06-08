---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_channel_posts.py

Symbols in `tests/gateway/test_telegram_channel_posts.py`.

- L22 `_build_telegram_stubs()` (function)
- L64 `telegram_adapter_cls(monkeypatch)` (function) — Import TelegramAdapter without leaking temporary telegram stubs.
- L92 `_make_adapter(telegram_adapter_cls)` (function)
- L101 `_make_channel_message(text='channel id test @hermes_bot')` (function)
- L126 `_make_channel_update(msg)` (function)
- L135 `test_build_message_event_uses_channel_identity_for_channel_posts(telegram_adapter_cls)` (function)
- L151 `test_text_handler_uses_effective_message_for_channel_post(telegram_adapter_cls)` (function)
- L168 `test_command_handler_uses_effective_message_for_channel_post(telegram_adapter_cls)` (function)
