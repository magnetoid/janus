---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_7100_transient_failure_transcript.py

Symbols in `tests/gateway/test_7100_transient_failure_transcript.py`.

- L20 `_classify(agent_result: dict, history_len: int)` (function) — Replicate the gateway classifier from GatewayRunner._run_agent.
- L41 `TestContextOverflowStillSkipsTranscript` (class) — #1630 behavior must be preserved for real context-overflow cases.
- L44 `test_compression_exhausted_is_context_overflow(self)` (method)
- L54 `test_explicit_context_length_error_is_context_overflow(self)` (method)
- L63 `test_generic_400_on_large_session_is_context_overflow(self)` (method)
- L73 `TestTransientFailureKeepsUserMessage` (class) — Transient provider failures must NOT skip the transcript — doing so
- L77 `test_rate_limit_429_is_not_context_overflow(self)` (method)
- L89 `test_read_timeout_is_not_context_overflow(self)` (method)
- L98 `test_connection_reset_is_not_context_overflow(self)` (method)
- L107 `test_provider_500_is_not_context_overflow(self)` (method)
- L116 `test_generic_400_on_short_session_is_not_context_overflow(self)` (method) — A 400 on a short session is a real client error, not context
- L128 `TestSuccessfulResultUnaffected` (class)
- L129 `test_successful_result_neither_failed_nor_overflow(self)` (method)
