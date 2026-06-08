---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_dashboard_auth_audit.py

Symbols in `tests/hermes_cli/test_dashboard_auth_audit.py`.

- L16 `profile_home(tmp_path, monkeypatch)` (function) — Redirect $HERMES_HOME and ~ to a tmp dir for the duration of the test.
- L26 `test_audit_writes_jsonlines(profile_home)` (function)
- L47 `test_audit_redacts_token_like_fields(profile_home)` (function)
- L58 `test_audit_all_event_types_have_string_values()` (function)
- L64 `test_audit_write_failure_does_not_raise(monkeypatch, tmp_path)` (function) — A broken audit log must not crash auth.
- L74 `test_audit_creates_logs_dir_if_missing(tmp_path, monkeypatch)` (function)
