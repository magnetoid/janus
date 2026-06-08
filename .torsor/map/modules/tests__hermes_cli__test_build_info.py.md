---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_build_info.py

Symbols in `tests/hermes_cli/test_build_info.py`.

- L12 `test_get_build_sha_returns_none_when_file_absent(tmp_path)` (function) — Source installs: no file present → None, callers fall back to git.
- L22 `test_get_build_sha_reads_baked_file(tmp_path)` (function) — Docker image case: file exists with full 40-char SHA → truncated to 8.
- L33 `test_get_build_sha_respects_short_argument(tmp_path)` (function) — ``short=N`` truncates to N chars; ``short<=0`` returns full SHA.
- L47 `test_get_build_sha_strips_whitespace(tmp_path)` (function) — The Dockerfile uses ``printf '%s\n'`` — strip the trailing newline.
- L58 `test_get_build_sha_returns_none_for_empty_file(tmp_path)` (function) — A whitespace-only file is treated as absent.
- L69 `test_get_build_sha_swallows_read_errors(tmp_path)` (function) — Any IO exception from the read returns None — never raises.
