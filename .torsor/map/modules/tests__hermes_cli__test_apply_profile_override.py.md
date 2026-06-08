---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_apply_profile_override.py

Symbols in `tests/hermes_cli/test_apply_profile_override.py`.

- L20 `_run_apply_profile_override(tmp_path, monkeypatch, *, hermes_home: str | None, active_profile: str | None, argv: list[str] | None=None)` (function) — Run _apply_profile_override in isolation.
- L52 `TestApplyProfileOverrideHermesHomeGuard` (class) — Regression guard for issue #22502.
- L60 `test_hermes_home_at_root_with_active_profile_is_redirected(self, tmp_path, monkeypatch)` (method) — HERMES_HOME=/root/.hermes + active_profile=coder must redirect
- L88 `test_hermes_home_already_profile_dir_is_trusted(self, tmp_path, monkeypatch)` (method) — HERMES_HOME=.../profiles/coder must not be overridden even when
- L113 `test_hermes_home_unset_reads_active_profile(self, tmp_path, monkeypatch)` (method) — Classic case: HERMES_HOME unset + active_profile=coder must set
- L127 `test_hermes_home_unset_default_profile_no_redirect(self, tmp_path, monkeypatch)` (method) — active_profile=default must not redirect HERMES_HOME.
