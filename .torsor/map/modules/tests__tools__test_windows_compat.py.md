---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_windows_compat.py

Symbols in `tests/tools/test_windows_compat.py`.

- L22 `_get_preexec_fn_values(filepath: Path)` (function) — Find all preexec_fn= keyword arguments in Popen calls.
- L33 `TestNoUnconditionalSetsid` (class) — preexec_fn must never be a bare os.setsid reference.
- L37 `test_preexec_fn_is_guarded(self, relpath)` (method)
- L49 `TestIsWindowsConstant` (class) — Each guarded file must define _IS_WINDOWS.
- L53 `test_has_is_windows(self, relpath)` (method)
- L63 `TestKillpgGuarded` (class) — os.killpg must always be behind a platform check.
- L67 `test_no_unguarded_killpg(self, relpath)` (method)
