---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_file_tools_cwd_resolution.py

Symbols in `tests/tools/test_file_tools_cwd_resolution.py`.

- L27 `_isolated_cwd(tmp_path, monkeypatch)` (function) — Two checkouts: workspace (intended) + decoy (process cwd).
- L43 `test_relative_terminal_cwd_anchors_to_absolute_not_process_cwd(_isolated_cwd, monkeypatch)` (function) — TERMINAL_CWD='.' must NOT silently mean 'the agent process cwd'.
- L65 `test_live_tracking_cwd_wins_over_relative_terminal_cwd(_isolated_cwd, monkeypatch)` (function) — When the terminal reports its absolute cwd, that is authoritative.
- L81 `test_absolute_terminal_cwd_used_verbatim(_isolated_cwd, monkeypatch)` (function) — An absolute TERMINAL_CWD is the resolution base (no live tracking).
- L91 `test_absolute_input_path_ignores_base(_isolated_cwd, monkeypatch)` (function) — An absolute input path is never re-anchored.
- L102 `test_resolution_base_always_absolute_no_terminal_cwd(_isolated_cwd, monkeypatch)` (function) — With TERMINAL_CWD unset, the base falls back to an ABSOLUTE process cwd.
- L116 `test_warning_fires_when_relative_path_escapes_workspace(_isolated_cwd, monkeypatch)` (function) — Relative path resolving outside the live workspace must warn.
- L133 `test_no_warning_when_relative_path_inside_workspace(_isolated_cwd, monkeypatch)` (function)
- L143 `test_no_warning_for_absolute_input(_isolated_cwd, monkeypatch)` (function)
- L152 `test_no_warning_when_no_live_cwd(_isolated_cwd, monkeypatch)` (function)
- L164 `test_write_file_reports_resolved_absolute_path(_isolated_cwd, monkeypatch)` (function) — write_file_tool must put the absolute on-disk path in files_modified.
- L178 `test_patch_reports_resolved_absolute_path(_isolated_cwd, monkeypatch)` (function) — patch_tool (replace mode) must put the absolute on-disk path in files_modified.
