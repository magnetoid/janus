---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/message_sanitization.py

Symbols in `agent/message_sanitization.py`.

- L31 `_sanitize_surrogates(text: str)` (function) — Replace lone surrogate code points with U+FFFD (replacement character).
- L42 `_sanitize_structure_surrogates(payload: Any)` (function) — Replace surrogate code points in nested dict/list payloads in-place.
- L75 `_sanitize_messages_surrogates(messages: list)` (function) — Sanitize surrogate characters from all string content in a messages list.
- L143 `_escape_invalid_chars_in_json_strings(raw: str)` (function) — Escape unescaped control chars inside JSON string values.
- L185 `_repair_tool_call_arguments(raw_args: str, tool_name: str='?')` (function) — Attempt to repair malformed tool_call argument JSON.
- L282 `_strip_non_ascii(text: str)` (function) — Remove non-ASCII characters, replacing with closest ASCII equivalent or removing.
- L291 `_sanitize_messages_non_ascii(messages: list)` (function) — Strip non-ASCII characters from all string content in a messages list.
- L350 `_sanitize_tools_non_ascii(tools: list)` (function) — Strip non-ASCII characters from tool payloads in-place.
- L355 `_strip_images_from_messages(messages: list)` (function) — Remove image_url content parts from all messages in-place.
- L403 `_sanitize_structure_non_ascii(payload: Any)` (function) — Strip non-ASCII characters from nested dict/list payloads in-place.
