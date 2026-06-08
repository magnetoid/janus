---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_prompt_text_input_thread_safety.py

Symbols in `tests/cli/test_prompt_text_input_thread_safety.py`.

- L13 `_make_cli()` (function) — Minimal HermesCLI shell exposing prompt fallback helpers.
- L23 `TestPromptTextInputThreadSafety` (class)
- L24 `test_main_thread_uses_run_in_terminal(self)` (method) — On the main thread with an active app, route through run_in_terminal.
- L37 `test_background_thread_falls_back_to_direct_input(self)` (method) — On a daemon thread, skip run_in_terminal and call input() directly.
- L69 `test_no_app_uses_direct_input(self)` (method) — Without an active prompt_toolkit app, always call input() directly.
- L80 `test_run_in_terminal_exception_falls_back(self)` (method) — If run_in_terminal raises (WSL / Warp edge cases), fall back to input().
- L93 `test_eof_returns_none(self)` (method) — EOFError from input() yields None, not an unhandled exception.
