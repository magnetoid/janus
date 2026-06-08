---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_ctrl_enter_newline.py

Symbols in `tests/cli/test_ctrl_enter_newline.py`.

- L19 `test_native_windows_preserves_newline()` (function)
- L25 `test_ssh_session_preserves_newline_on_linux()` (function)
- L32 `test_ssh_tty_alone_preserves_newline()` (function)
- L40 `test_wsl_distro_name_preserves_newline()` (function)
- L47 `test_windows_terminal_session_preserves_newline()` (function)
- L54 `test_ghostty_tmux_session_preserves_ctrl_j_newline()` (function) — Ghostty-inherited env survives tmux even when TERM_PROGRAM becomes tmux.
- L66 `test_pure_local_linux_does_not_preserve()` (function) — A bare local Linux TTY (no SSH/WSL/WT/Ghostty) keeps c-j → submit so docker exec
- L77 `test_proc_version_microsoft_marker_preserves_newline()` (function) — WSL detection via /proc when env vars are scrubbed (sudo etc.).
- L97 `test_install_ctrl_enter_alias_maps_csi_u_sequences()` (function) — Kitty / xterm modifyOtherKeys / mintty Ctrl+Enter sequences alias to
- L112 `test_install_ctrl_enter_alias_idempotent()` (function) — Running it twice doesn't double-count or break.
