---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_slash_confirm_windows.py

Symbols in `tests/cli/test_slash_confirm_windows.py`.

- L25 `_make_cli()` (function) — Minimal HermesCLI shell exposing prompt/modal helpers.
- L50 `TestModalWindowsFallback` (class) — Windows dead-lock regression tests for _prompt_text_input_modal.
- L53 `test_windows_falls_back_to_stdin(self)` (method) — On Windows, _prompt_text_input_modal should use _prompt_text_input.
- L69 `test_non_main_thread_uses_modal_via_app_loop(self)` (method) — Off the main thread on Linux, keep the modal path via app-loop setup.
- L111 `test_main_thread_non_windows_uses_modal(self)` (method) — On macOS/Linux main thread, the queue-based modal is still used.
- L161 `test_no_app_falls_back_to_stdin(self)` (method) — Without a prompt_toolkit app, always use stdin fallback.
- L176 `test_empty_choices_returns_none(self)` (method) — Empty choices list should return None without prompting.
- L190 `test_windows_fallback_does_not_set_modal_state(self)` (method) — Verify Windows fallback doesn't leave _slash_confirm_state set.
- L204 `test_non_main_thread_modal_clears_state(self)` (method) — Verify daemon-thread modal teardown does not leave state behind.
- L243 `TestConfirmDestructiveSlashWindows` (class) — Integration-level tests for _confirm_destructive_slash on Windows.
- L246 `test_confirm_destructive_slash_bypasses_modal_on_windows(self)` (method) — _confirm_destructive_slash should work on Windows via stdin fallback.
- L269 `test_confirm_destructive_slash_cancelled_on_windows(self)` (method) — Cancellation via stdin fallback works on Windows.
