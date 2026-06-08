---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_curses_arrow_keys.py

Symbols in `tests/hermes_cli/test_curses_arrow_keys.py`.

- L22 `FakeStdscr` (class) — Minimal stdscr stand-in that replays a queue of getch() byte returns.
- L29 `__init__(self, keys)` (method)
- L33 `getch(self)` (method)
- L36 `timeout(self, ms)` (method)
- L40 `test_raw_csi_arrow_down_decodes_to_down()` (function)
- L45 `test_raw_csi_arrow_up_decodes_to_up()` (function)
- L50 `test_raw_ss3_arrow_keys_decode()` (function)
- L56 `test_translated_key_constants_still_work()` (function)
- L61 `test_vim_keys()` (function)
- L66 `test_lone_escape_is_cancel()` (function)
- L71 `test_q_is_cancel()` (function)
- L75 `test_enter_variants_select()` (function)
- L81 `test_unhandled_csi_sequence_is_consumed_and_ignored()` (function)
- L90 `test_home_end_csi_sequences_ignored()` (function)
- L96 `test_escape_uses_short_timeout_then_restores_blocking()` (function)
