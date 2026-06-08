---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_mcp_invalid_url.py

Symbols in `tests/tools/test_mcp_invalid_url.py`.

- L27 `TestValidUrlsAccepted` (class) — Every valid http(s) URL must pass through untouched (stripped of whitespace).
- L42 `test_accepts_valid_http_url(self, url)` (method)
- L45 `test_strips_surrounding_whitespace(self)` (method)
- L52 `TestInvalidUrlsRejected` (class) — Every broken shape must raise ``InvalidMcpUrlError`` with a clear message.
- L55 `test_none_rejected(self)` (method)
- L59 `test_dict_rejected(self)` (method)
- L63 `test_int_rejected(self)` (method)
- L67 `test_empty_string_rejected(self)` (method)
- L71 `test_whitespace_only_rejected(self)` (method)
- L75 `test_missing_scheme_rejected(self)` (method)
- L82 `test_file_scheme_rejected(self)` (method)
- L88 `test_ws_scheme_rejected(self)` (method)
- L95 `test_stdio_scheme_rejected(self)` (method)
- L102 `test_empty_host_rejected(self)` (method)
- L106 `test_empty_host_with_path_rejected(self)` (method)
- L110 `test_error_mentions_server_name(self)` (method)
- L116 `TestErrorIsValueError` (class) — InvalidMcpUrlError must be a ValueError for broad downstream catch blocks.
- L119 `test_is_value_error(self)` (method)
