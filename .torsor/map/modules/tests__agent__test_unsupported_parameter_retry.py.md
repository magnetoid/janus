---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_unsupported_parameter_retry.py

Symbols in `tests/agent/test_unsupported_parameter_retry.py`.

- L31 `TestIsUnsupportedParameterError` (class) — The generic detector must match real provider phrasings for any param.
- L47 `test_matches_real_provider_messages(self, param, message)` (method)
- L60 `test_does_not_match_unrelated_errors(self, param, message)` (method)
- L63 `test_empty_param_returns_false(self)` (method)
- L68 `test_temperature_wrapper_delegates_to_generic(self)` (method) — Back-compat: ``_is_unsupported_temperature_error`` still routes through.
- L77 `_dummy_response()` (function) — Sentinel — real code calls ``_validate_llm_response`` which we patch out.
- L82 `TestMaxTokensRetryHardening` (class) — The max_tokens retry branch now (a) gates on ``max_tokens is not None``
- L87 `test_sync_max_tokens_retry_skipped_when_max_tokens_is_none(self)` (method) — No max_tokens kwarg → must not pop/retry even if the error mentions it.
- L120 `test_async_max_tokens_retry_skipped_when_max_tokens_is_none(self)` (method)
