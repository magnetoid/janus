---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_stage2_hook_toplevel_chown.py

Symbols in `tests/tools/test_stage2_hook_toplevel_chown.py`.

- L36 `stage2_text()` (function)
- L42 `_toplevel_chown_loop(text: str)` (function) — Extract the `for f in … chown hermes:hermes "$HERMES_HOME/$f" … done`
- L57 `test_toplevel_chown_loop_present(stage2_text: str)` (function)
- L66 `test_no_blanket_find_user_root_sweep(stage2_text: str)` (function) — The fix must NOT reintroduce a blanket `find … -user root` chown of
- L77 `_run_loop(text: str, present_files: list[str])` (function) — Run the extracted chown loop in a sandbox $HERMES_HOME, with `chown`
- L118 `test_loop_chowns_present_allowlisted_files(stage2_text: str)` (function)
- L125 `test_loop_skips_nonallowlisted_host_file(stage2_text: str)` (function) — A file NOT on the allowlist (e.g. a host-owned file in a bind mount) must
- L134 `test_loop_skips_absent_files(stage2_text: str)` (function) — Allowlisted files that don't exist are skipped (no spurious chown).
