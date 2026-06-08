---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_curator_status.py

Symbols in `tests/hermes_cli/test_curator_status.py`.

- L20 `test_status_uses_last_activity_not_only_last_used(monkeypatch, capsys)` (function)
- L61 `curator_status_env(tmp_path, monkeypatch)` (function) — Isolated HERMES_HOME with real agent-created skills on disk.
- L104 `_capture_status(curator_cli)` (function)
- L112 `test_status_shows_most_and_least_used_sections(curator_status_env)` (function)
- L153 `test_status_hides_most_active_when_all_zero(curator_status_env)` (function) — If no skills have any activity, skip the most-active block — it's noise.
- L171 `test_status_no_skills_produces_clean_empty_output(curator_status_env)` (function)
- L180 `test_status_marks_missing_last_report_path(monkeypatch, capsys, tmp_path)` (function)
