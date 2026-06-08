---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_bracketed_paste_timeout.py

Symbols in `tests/cli/test_bracketed_paste_timeout.py`.

- L21 `_load_production_patch_helper()` (function) — Load cli._apply_bracketed_paste_timeout_patch without importing cli.
- L49 `_reset_and_apply_production_patch()` (function) — Reload prompt_toolkit's parser and apply Hermes' production patch.
- L63 `TestBracketedPasteTimeout` (class) — Verify the Vt100Parser monkey-patch prevents frozen bracketed-paste.
- L66 `_make_parser(self)` (method) — Create a Vt100Parser after applying the production patch.
- L73 `test_normal_bracketed_paste_works(self)` (method) — A complete bracketed-paste sequence should work normally.
- L81 `test_incomplete_paste_times_out(self)` (method) — If ESC[201~ is never received, parser should recover after timeout.
- L93 `test_timeout_preserves_buffered_content(self)` (method) — Auto-escape should flush buffered content, not lose it.
- L109 `test_normal_keys_after_timeout_recovery(self)` (method) — After timeout recovery, normal key processing should resume.
- L121 `test_no_timeout_when_end_mark_arrives_quickly(self)` (method) — No timeout should fire if end mark arrives within the window.
- L128 `test_subsequent_data_after_incomplete_paste(self)` (method) — Data arriving after a stuck paste should be processable.
- L138 `test_torn_end_mark_recovers(self)` (method) — If end mark arrives split across feeds within timeout, it still works.
- L149 `test_no_timeout_under_threshold(self)` (method) — Bracketed-paste mode should not timeout within the 2s window.
