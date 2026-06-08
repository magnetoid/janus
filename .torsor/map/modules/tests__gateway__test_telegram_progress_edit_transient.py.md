---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_telegram_progress_edit_transient.py

Symbols in `tests/gateway/test_telegram_progress_edit_transient.py`.

- L53 `_is_transient(error_str: str)` (function) — Mirrors the classification logic added to TelegramAdapter.edit_message.
- L59 `_is_permanent(error_str: str)` (function)
- L79 `test_transient_errors_are_classified_as_transient(error_str)` (function) — Network / transient errors must be classified as retryable.
- L94 `test_permanent_errors_are_not_transient(error_str)` (function) — Permanent edit failures must NOT be classified as retryable.
- L105 `test_send_result_retryable_default_is_false()` (function)
- L110 `test_send_result_retryable_can_be_set_true()` (function)
- L115 `test_send_result_retryable_false_for_permanent()` (function)
- L132 `_simulate_progress_loop(edit_results)` (function) — Simulate the can_edit decision for a sequence of edit_message results.
- L149 `test_transient_failure_keeps_can_edit_true()` (function) — A single transient network error must not disable progress editing.
- L158 `test_permanent_failure_sets_can_edit_false()` (function) — A permanent edit failure must disable progress editing.
- L166 `test_multiple_transient_then_success_keeps_can_edit_true()` (function) — Multiple transient failures followed by success keep can_edit=True.
- L176 `test_flood_control_sets_can_edit_false()` (function) — Flood control (non-retryable) must disable progress editing.
