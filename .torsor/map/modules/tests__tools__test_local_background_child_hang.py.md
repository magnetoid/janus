---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_local_background_child_hang.py

Symbols in `tests/tools/test_local_background_child_hang.py`.

- L21 `_pkill(pattern: str)` (function)
- L26 `local_env()` (function)
- L34 `TestBackgroundChildDoesNotHang` (class) — Regression guard for issue #8340.
- L37 `test_plain_background_returns_promptly(self, local_env)` (method) — ``cmd &`` with no output redirection must not hang on pipe inherit.
- L55 `test_setsid_disown_pattern_returns_promptly(self, local_env)` (method) — The exact pattern from the issue: setsid ... & disown.
- L72 `test_foreground_streaming_output_still_captured(self, local_env)` (method) — Sanity: incremental output over time must still be captured in full.
- L85 `test_high_volume_output_complete(self, local_env)` (method) — Sanity: select-based drain must not drop lines under load.
- L94 `test_timeout_path_still_works(self, local_env)` (method) — Foreground command exceeding timeout must still be killed.
- L104 `test_utf8_output_decoded_correctly(self, local_env)` (method) — Multibyte UTF-8 chunks must decode cleanly under select-based reads.
- L112 `test_utf8_multibyte_across_read_boundary(self, local_env)` (method) — Multibyte UTF-8 characters straddling a 4096-byte ``os.read()`` boundary
- L137 `test_invalid_utf8_uses_replacement_not_fallback(self, local_env)` (method) — Truly invalid byte sequences must be substituted with U+FFFD (matching
