---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_ephemeral_reply.py

Symbols in `tests/gateway/test_ephemeral_reply.py`.

- L39 `_NoDeleteAdapter` (class) — Adapter that does NOT override delete_message (silent degrade).
- L42 `connect(self)` (method)
- L45 `disconnect(self)` (method)
- L48 `send(self, chat_id, content='', **kwargs)` (method)
- L51 `get_chat_info(self, chat_id)` (method)
- L55 `_DeleteCapableAdapter` (class) — Adapter that overrides delete_message (TTL honored).
- L58 `__init__(self, *a, **kw)` (method)
- L62 `connect(self)` (method)
- L65 `disconnect(self)` (method)
- L68 `send(self, chat_id, content='', **kwargs)` (method)
- L71 `get_chat_info(self, chat_id)` (method)
- L74 `delete_message(self, chat_id: str, message_id: str)` (method)
- L79 `_no_delete_adapter()` (function)
- L85 `_delete_adapter()` (function)
- L91 `_make_event(text='/stop', chat_id='42')` (function)
- L109 `test_unwrap_plain_string_is_passthrough()` (function)
- L116 `test_unwrap_none_is_passthrough()` (function)
- L123 `test_unwrap_ephemeral_explicit_ttl_on_capable_adapter()` (function)
- L130 `test_unwrap_ephemeral_zeros_ttl_on_incapable_adapter()` (function) — Platforms without delete_message should silently degrade to normal send.
- L138 `test_unwrap_ephemeral_default_ttl_from_config()` (function)
- L146 `test_unwrap_ephemeral_default_ttl_zero_disables()` (function) — Config default of 0 (the shipped default) means the feature is off.
- L155 `test_unwrap_ephemeral_handles_unreadable_config()` (function)
- L174 `test_schedule_ephemeral_delete_calls_delete_after_ttl()` (function)
- L204 `test_schedule_ephemeral_delete_swallows_errors()` (function)
- L220 `test_schedule_ephemeral_delete_outside_event_loop_is_noop()` (function) — No running loop → no crash, silently drops the request.
- L236 `test_process_message_unwraps_ephemeral_before_send()` (function) — The adapter must send the wrapper's .text, never the wrapper object.
- L272 `test_process_message_ephemeral_reply_does_not_auto_upload_bare_paths(tmp_path)` (function) — Tips/system notices may mention local paths; they must remain text.
- L303 `test_process_message_incapable_platform_does_not_schedule_delete()` (function)
- L345 `test_process_message_plain_string_behaves_unchanged()` (function)
