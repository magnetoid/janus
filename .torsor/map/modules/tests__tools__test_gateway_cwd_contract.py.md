---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_gateway_cwd_contract.py

Symbols in `tests/tools/test_gateway_cwd_contract.py`.

- L20 `test_terminal_env_config_uses_terminal_cwd(monkeypatch, tmp_path)` (function) — The terminal tool's default cwd should come from TERMINAL_CWD.
- L33 `test_file_tool_relative_paths_use_terminal_cwd(monkeypatch, tmp_path)` (function) — Relative file/search/patch paths resolve under TERMINAL_CWD.
- L45 `test_execute_code_project_mode_uses_terminal_cwd(monkeypatch, tmp_path)` (function) — Project-mode execute_code should run scripts from TERMINAL_CWD.
- L59 `test_execute_code_project_mode_falls_back_when_terminal_cwd_missing(monkeypatch, tmp_path)` (function) — Invalid TERMINAL_CWD should not break execute_code project mode startup.
