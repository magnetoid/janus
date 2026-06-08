---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_hidden_dir_filter.py

Symbols in `tests/tools/test_hidden_dir_filter.py`.

- L13 `_old_filter_matches(path_str: str)` (function) — The BROKEN filter that used hardcoded forward slashes.
- L21 `_new_filter_matches(path: Path)` (function) — The FIXED filter using Path.parts.
- L29 `TestOldFilterBrokenOnWindows` (class) — Demonstrate the bug: hardcoded '/' never matches Windows backslash paths.
- L32 `test_old_filter_misses_hub_on_windows_path(self)` (method) — Old filter fails to catch .hub in a Windows-style path string.
- L37 `test_old_filter_misses_git_on_windows_path(self)` (method) — Old filter fails to catch .git in a Windows-style path string.
- L42 `test_old_filter_works_on_unix_path(self)` (method) — Old filter works fine on Unix paths (the original platform).
- L48 `TestNewFilterCrossPlatform` (class) — The fixed filter works on both Windows and Unix paths.
- L51 `test_hub_quarantine_filtered(self, tmp_path)` (method) — A SKILL.md inside .hub/quarantine/ must be filtered out.
- L56 `test_git_dir_filtered(self, tmp_path)` (method) — A SKILL.md inside .git/ must be filtered out.
- L61 `test_github_dir_filtered(self, tmp_path)` (method) — A SKILL.md inside .github/ must be filtered out.
- L66 `test_normal_skill_not_filtered(self, tmp_path)` (method) — A regular skill SKILL.md must NOT be filtered out.
- L71 `test_nested_skill_not_filtered(self, tmp_path)` (method) — A deeply nested regular skill must NOT be filtered out.
- L76 `test_dot_prefix_not_false_positive(self, tmp_path)` (method) — A skill dir starting with dot but not in the filter list passes.
- L82 `TestWindowsPathParts` (class) — Verify Path.parts correctly splits on the native separator.
- L85 `test_parts_contains_hidden_dir(self, tmp_path)` (method) — Path.parts includes each directory component individually.
- L90 `test_parts_does_not_contain_combined_string(self, tmp_path)` (method) — Path.parts splits by separator, not by substring.
