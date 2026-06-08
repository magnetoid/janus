---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_shift_enter_newline.py

Symbols in `tests/cli/test_cli_shift_enter_newline.py`.

- L26 `_ensure_alias_installed()` (function) — Make every test idempotent — install the alias once per test run.
- L31 `_parse(byte_seq: str)` (function)
- L40 `test_install_registers_all_three_sequences()` (function)
- L46 `test_install_overwrites_stock_modifyotherkeys_shift_enter()` (function) — Stock prompt_toolkit maps `\x1b[27;2;13~` to plain Keys.ControlM —
- L57 `test_install_returns_zero_when_already_correct()` (function) — Idempotency — running install twice should not report a second change.
- L63 `test_csi_u_shift_enter_parses_as_alt_enter()` (function) — Kitty keyboard protocol Shift+Enter must parse to the same key tuple
- L74 `test_modify_other_keys_shift_enter_parses_as_alt_enter()` (function) — xterm modifyOtherKeys=2 Shift+Enter must parse identically to Alt+Enter.
- L81 `test_plain_enter_remains_distinct_from_alt_enter()` (function) — Plain Enter must keep emitting a single key (submit), not a two-key
