---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_run_tool_media_re.py

Symbols in `tests/gateway/test_run_tool_media_re.py`.

- L45 `TestToolMediaReWindowsPaths` (class) — Issue #34632: _TOOL_MEDIA_RE must match Windows absolute paths.
- L66 `test_windows_paths_match(self, media_tag, expected_path)` (method) — Windows absolute paths with drive letters are matched.
- L82 `test_unix_paths_still_match(self, media_tag, expected_path)` (method) — Unix-style absolute and home-relative paths still match.
- L99 `test_invalid_paths_dont_match(self, text)` (method) — Non-MEDIA text, relative paths, and unsupported extensions are ignored.
- L111 `test_pre_fix_pattern_rejects_windows(self, media_tag)` (method) — The pre-fix pattern (without Windows anchor) does NOT match Windows paths.
- L119 `test_multiple_media_tags_in_content(self)` (method) — Multiple MEDIA tags in the same content are all found.
- L130 `test_case_insensitive_drive_letter(self)` (method) — Drive letters are case-insensitive due to re.IGNORECASE.
- L144 `test_case_insensitive_extensions(self, media_tag)` (method) — File extensions are matched case-insensitively.
