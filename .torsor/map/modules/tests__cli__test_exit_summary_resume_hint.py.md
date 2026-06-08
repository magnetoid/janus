---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_exit_summary_resume_hint.py

Symbols in `tests/cli/test_exit_summary_resume_hint.py`.

- L9 `_make_cli(session_id='20260524_000001_abc123')` (function)
- L21 `TestExitSummaryResumeHint` (class) — The exit-line ``Resume this session with:`` hint must include the
- L29 `test_resume_hint_no_profile_flag_on_default(self, capsys)` (method)
- L38 `test_resume_hint_no_profile_flag_on_custom(self, capsys)` (method)
- L47 `test_resume_hint_includes_profile_flag_for_named_profile(self, capsys)` (method)
- L54 `test_resume_hint_includes_profile_flag_on_title_hint_too(self, capsys, tmp_path)` (method) — When a session title is available, the `hermes -c "title"` hint
- L69 `test_resume_hint_falls_back_when_profile_lookup_fails(self, capsys)` (method) — If `get_active_profile_name` raises (e.g. profiles module
