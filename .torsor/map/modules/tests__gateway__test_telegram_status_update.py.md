---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_status_update.py

Symbols in `tests/gateway/test_telegram_status_update.py`.

- L23 `_install_fake_telegram(monkeypatch)` (function) — Stub the python-telegram-bot package so TelegramAdapter can be imported.
- L65 `adapter(monkeypatch)` (function)
- L78 `test_first_call_sends_and_caches_message_id(adapter)` (function) — First call for a (chat, key) pair must send and remember the id.
- L92 `test_second_call_edits_in_place(adapter)` (function) — Same (chat, key) on the second call must edit, not send.
- L110 `test_edit_failure_falls_back_to_fresh_send(adapter)` (function) — When edit_message fails the cache is cleared and a new send happens.
- L132 `test_distinct_status_keys_do_not_collide(adapter)` (function) — A different status_key gets its own message; the original isn't touched.
- L149 `test_distinct_chat_ids_do_not_collide(adapter)` (function) — Same status_key in different chats must not edit each other's messages.
