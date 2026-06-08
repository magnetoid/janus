---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/error_classifier.py

Symbols in `agent/error_classifier.py`.

- L24 `FailoverReason` (class) — Why an API call failed — determines recovery strategy.
- L70 `ClassifiedError` (class) — Structured classification of an API error with recovery hints.
- L88 `is_auth(self)` (method)
- L441 `classify_api_error(error: Exception, *, provider: str='', model: str='', approx_tokens: int=0, context_length: int=200000, num_messages: int=0)` (function) — Classify an API error into a structured recovery recommendation.
- L728 `_classify_by_status(status_code: int, error_msg: str, error_code: str, body: dict, *, provider: str, model: str, approx_tokens: int, context_length: int, num_messages: int=0, result_fn)` (function) — Classify based on HTTP status code with message-aware refinement.
- L884 `_classify_402(error_msg: str, result_fn)` (function) — Disambiguate 402: billing exhaustion vs transient usage limit.
- L913 `_classify_400(error_msg: str, error_code: str, body: dict, *, provider: str, model: str, approx_tokens: int, context_length: int, num_messages: int=0, result_fn)` (function) — Classify 400 Bad Request — context overflow, format error, or generic.
- L1043 `_classify_by_error_code(error_code: str, error_msg: str, result_fn)` (function) — Classify by structured error codes from the response body.
- L1098 `_classify_by_message(error_msg: str, error_type: str, *, approx_tokens: int, context_length: int, result_fn)` (function) — Classify based on error message patterns when no status code is available.
- L1220 `_extract_status_code(error: Exception)` (function) — Walk the error and its cause chain to find an HTTP status code.
- L1239 `_extract_error_body(error: Exception)` (function) — Extract the structured error body from an SDK exception.
- L1256 `_extract_error_code(body: dict)` (function) — Extract an error code string from the response body.
- L1306 `_extract_message(error: Exception, body: dict)` (function) — Extract the most informative error message.
