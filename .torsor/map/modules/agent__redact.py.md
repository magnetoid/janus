---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/redact.py

Symbols in `agent/redact.py`.

- L196 `mask_secret(value: str, *, head: int=4, tail: int=4, floor: int=12, placeholder: str='***', empty: str='')` (function) — Mask a secret for display, preserving ``head`` and ``tail`` characters.
- L243 `_mask_token(token: str)` (function) — Mask a log token — conservative 18-char floor, preserves 6 prefix / 4 suffix.
- L251 `_redact_query_string(query: str)` (function) — Redact sensitive parameter values in a URL query string.
- L273 `_redact_url_query_params(text: str)` (function) — Scan text for URLs with query strings and redact sensitive params.
- L289 `_redact_url_userinfo(text: str)` (function) — Strip `user:password@` from HTTP/WS/FTP URLs.
- L301 `_redact_http_request_target_query_params(text: str)` (function) — Redact sensitive query params in HTTP access-log request targets.
- L310 `_redact_form_body(text: str)` (function) — Redact sensitive values in a form-urlencoded body.
- L326 `redact_sensitive_text(text: str, *, force: bool=False, code_file: bool=False)` (function) — Apply all redaction patterns to a block of text.
- L441 `_extract_literal_prefix(pattern: str)` (function) — Return the leading literal characters of a regex pattern.
- L461 `_has_known_prefix_substring(text: str)` (function) — Return True if ``text`` contains any known credential prefix substring.
- L482 `_has_http_method_substring(text: str)` (function) — Cheap pre-check before scanning for access-log request targets.
- L488 `RedactingFormatter` (class) — Log formatter that redacts secrets from all log messages.
- L491 `__init__(self, fmt=None, datefmt=None, style='%', **kwargs)` (method)
- L494 `format(self, record: logging.LogRecord)` (method)
