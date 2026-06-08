---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_curses_color_compat.py

Symbols in `tests/hermes_cli/test_curses_color_compat.py`.

- L23 `TestInitPairClampingBehavior` (class) — Simulate curses color initialization on low-color terminals.
- L30 `_collect_init_pair_calls(self, draw_fn, colors_value)` (method) — Run a curses draw function with a mock stdscr and patched COLORS.
- L58 `test_8_color_terminal_no_color_exceeds_limit(self)` (method) — On an 8-color terminal (Docker), no init_pair fg color >= 8.
- L77 `test_256_color_terminal_uses_color_8(self)` (method) — On a 256-color terminal, color 8 (dim gray) should be used.
- L90 `test_16_color_terminal_uses_color_8(self)` (method) — On a 16-color terminal, color 8 should be available.
- L102 `TestSourceCodeGuardrails` (class) — Regression guardrails: raw color 8 must not reappear in source.
- L111 `test_no_raw_color_8_in_plugins_cmd(self)` (method)
- L118 `test_no_raw_color_8_in_main(self)` (method)
- L125 `test_no_raw_color_8_in_curses_ui(self)` (method)
