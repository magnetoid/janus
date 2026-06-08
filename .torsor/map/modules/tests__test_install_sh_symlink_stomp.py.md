---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_install_sh_symlink_stomp.py

Symbols in `tests/test_install_sh_symlink_stomp.py`.

- L29 `_extract_setup_path_shim_block()` (function) — Return the install.sh shim-write block used by setup_path().
- L43 `test_setup_path_shim_block_removes_old_link_before_writing()` (function) — Static guard: the rm must precede the cat heredoc, not follow it.
- L60 `test_re_running_setup_path_block_preserves_pip_entry_point(tmp_path: Path)` (function) — Behavioral repro: simulate prior-install symlink + new-install heredoc.
