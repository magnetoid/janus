---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_unsupported_temperature_retry.py

Symbols in `tests/agent/test_unsupported_temperature_retry.py`.

- L37 `TestIsUnsupportedTemperatureError` (class) — The detector must match the phrasings providers actually return.
- L54 `test_matches_real_provider_messages(self, message)` (method)
- L66 `test_does_not_match_unrelated_errors(self, message)` (method)
- L70 `_dummy_response()` (function)
- L77 `TestCallLlmUnsupportedTemperatureRetry` (class) — ``call_llm`` retries once without temperature and returns on success.
- L80 `_setup(self, first_exc)` (method)
- L91 `test_retries_once_without_temperature(self, error_message)` (method)
- L123 `test_non_temperature_400_does_not_retry_as_temperature(self)` (method) — Unrelated 400s (e.g. bad tool role) must not silently drop temp.
- L152 `test_no_retry_when_temperature_not_in_kwargs(self)` (method) — If caller didn't send temperature, don't invent a temperature-retry.
- L182 `TestAsyncCallLlmUnsupportedTemperatureRetry` (class) — ``async_call_llm`` mirror of the sync retry semantics.
- L186 `test_async_retries_once_without_temperature(self)` (method)
- L222 `test_async_non_temperature_400_does_not_retry(self)` (method)
