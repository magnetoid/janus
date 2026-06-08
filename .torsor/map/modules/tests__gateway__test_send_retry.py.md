---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_send_retry.py

Symbols in `tests/gateway/test_send_retry.py`.

- L22 `_StubAdapter` (class)
- L23 `__init__(self)` (method)
- L29 `_next_result(self)` (method)
- L34 `send(self, chat_id, content, reply_to=None, metadata=None, **kwargs)` (method)
- L38 `connect(self)` (method)
- L41 `disconnect(self)` (method)
- L44 `send_typing(self, chat_id, metadata=None)` (method)
- L47 `get_chat_info(self, chat_id)` (method)
- L55 `TestIsRetryableError` (class)
- L56 `test_none_is_not_retryable(self)` (method)
- L59 `test_empty_string_is_not_retryable(self)` (method)
- L63 `test_known_pattern_is_retryable(self, pattern)` (method)
- L66 `test_permission_error_not_retryable(self)` (method)
- L69 `test_bad_request_not_retryable(self)` (method)
- L72 `test_case_insensitive(self)` (method)
- L75 `test_timeout_not_retryable(self)` (method)
- L78 `test_timed_out_not_retryable(self)` (method)
- L81 `test_connect_timeout_is_retryable(self)` (method)
- L89 `TestIsTimeoutError` (class)
- L90 `test_none_is_not_timeout(self)` (method)
- L93 `test_empty_is_not_timeout(self)` (method)
- L96 `test_timed_out(self)` (method)
- L99 `test_read_timeout(self)` (method)
- L102 `test_write_timeout(self)` (method)
- L105 `test_connect_timeout_not_flagged(self)` (method) — ConnectTimeout is a connection error, not a delivery-ambiguous timeout.
- L109 `test_connection_error_not_timeout(self)` (method)
- L117 `TestSendWithRetrySuccess` (class)
- L119 `test_success_first_attempt(self)` (method)
- L127 `test_returns_message_id(self)` (method)
- L138 `TestSendWithRetryNetworkRetry` (class)
- L140 `test_retries_on_connect_error_and_succeeds(self)` (method)
- L152 `test_timeout_not_retried_to_prevent_duplicates(self)` (method) — ReadTimeout is NOT retried because the request may have reached
- L168 `test_connect_timeout_still_retried(self)` (method) — ConnectTimeout is safe to retry — the connection was never established.
- L181 `test_retryable_flag_respected(self)` (method) — SendResult.retryable=True should trigger retry even if error string doesn't match.
- L194 `test_network_to_nonnetwork_transition_falls_back_to_plaintext(self)` (method) — If error switches from network to formatting mid-retry, fall through to plain-text fallback.
- L214 `TestSendWithRetryExhausted` (class)
- L216 `test_sends_user_notice_after_exhaustion(self)` (method)
- L232 `test_notice_send_exception_doesnt_propagate(self)` (method) — If the notice itself throws, _send_with_retry should not raise.
- L257 `TestSendWithRetryFallback` (class)
- L259 `test_non_network_error_falls_back_immediately(self)` (method)
- L275 `test_fallback_failure_logged_but_not_raised(self)` (method)
