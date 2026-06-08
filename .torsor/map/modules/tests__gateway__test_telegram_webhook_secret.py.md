---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_webhook_secret.py

Symbols in `tests/gateway/test_telegram_webhook_secret.py`.

- L22 `TestTelegramWebhookSecretRequired` (class) — Direct source-level check of the webhook-secret guard.
- L33 `_get_source(self)` (method)
- L37 `test_webhook_branch_checks_secret(self)` (method) — The webhook-mode branch of connect() must read
- L50 `test_guard_raises_runtime_error(self)` (method) — The guard raises RuntimeError (not a silent log) so operators
- L65 `test_guard_message_includes_advisory_link(self)` (method) — The RuntimeError message should reference the advisory so
- L73 `test_guard_message_explains_remediation(self)` (method) — The error should tell the operator how to fix it.
- L82 `test_polling_branch_has_no_secret_guard(self)` (method) — Polling mode (else-branch) must NOT require the webhook secret —
