---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_empty_error_message.py

Symbols in `tests/tools/test_mcp_empty_error_message.py`.

- L20 `_EmptyMessageError` (class) — Exception whose __str__ returns empty string (like anyio.ClosedResourceError).
- L23 `__str__(self)` (method)
- L27 `_NormalError` (class)
- L31 `test_exc_str_returns_str_when_nonempty()` (function)
- L36 `test_exc_str_falls_back_to_repr_when_str_empty()` (function)
- L43 `test_exc_str_falls_back_to_repr_for_whitespace_only()` (function) — str(exc) that is only whitespace should also trigger the repr fallback.
- L51 `test_exc_str_handles_closedresource_like_exception()` (function) — Simulate anyio.ClosedResourceError which has no message.
- L65 `test_error_message_not_empty_when_exc_has_no_message()` (function) — The formatted error string should always contain the exception class name.
- L78 `test_error_message_preserves_normal_exception_text()` (function) — Normal exceptions should still show their message text.
