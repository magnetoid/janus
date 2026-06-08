---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_send_draft_format.py

Symbols in `tests/gateway/test_telegram_send_draft_format.py`.

- L24 `_ensure_telegram_mock()` (function)
- L42 `_make_adapter()` (function)
- L50 `test_send_draft_passes_markdownv2_parse_mode()` (function) — Happy path: draft is sent with parse_mode set and format_message'd text.
- L68 `test_send_draft_falls_back_to_plain_text_on_markdownv2_error()` (function) — A MarkdownV2 BadRequest retries once as plain text (no parse_mode),
- L97 `test_send_draft_non_badrequest_propagates_without_retry()` (function) — A non-BadRequest failure (e.g. drafts not allowed) returns failure
