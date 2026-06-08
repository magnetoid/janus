---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_noise_filter.py

Symbols in `tests/gateway/test_telegram_noise_filter.py`.

- L10 `test_telegram_status_suppresses_auxiliary_and_retry_noise()` (function) — Auxiliary failures and retry backoff chatter should not hit Telegram.
- L26 `test_non_telegram_status_is_unchanged()` (function) — The Telegram quieting policy must not hide CLI/Discord diagnostics.
- L34 `test_telegram_status_sanitizes_raw_provider_security_errors()` (function) — Provider policy/security bodies should be replaced before chat delivery.
- L50 `test_telegram_final_response_sanitizes_raw_provider_errors()` (function) — Final Telegram replies should not expose raw provider/security details.
- L65 `test_telegram_final_response_redacts_auth_secrets()` (function) — Authentication errors should be useful without leaking key material.
- L79 `test_telegram_final_response_keeps_normal_answers()` (function) — Normal assistant content should not be rewritten.
