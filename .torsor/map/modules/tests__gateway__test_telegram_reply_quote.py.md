---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_reply_quote.py

Symbols in `tests/gateway/test_telegram_reply_quote.py`.

- L18 `_ensure_telegram_mock()` (function)
- L39 `_make_adapter()` (function)
- L43 `_make_message(text='follow-up', reply_to_text=None, reply_to_caption=None, reply_to_id=42, quote_text=None)` (function)
- L78 `test_native_partial_quote_used_as_reply_to_text()` (function) — When ``message.quote`` is present, prefer the selected substring.
- L97 `test_full_reply_text_used_when_no_native_quote()` (function) — No ``message.quote`` → fall back to the whole replied-to message text.
- L114 `test_caption_fallback_when_no_quote_and_no_text()` (function) — Replied-to media message: caption is used when text is absent.
- L131 `test_empty_quote_text_falls_back_to_full_reply()` (function) — Defensive: a present-but-empty quote.text shouldn't blank the prefix.
