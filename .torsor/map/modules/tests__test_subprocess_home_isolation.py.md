---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_subprocess_home_isolation.py

Symbols in `tests/test_subprocess_home_isolation.py`.

- L20 `TestGetSubprocessHome` (class) — Unit tests for hermes_constants.get_subprocess_home().
- L23 `test_returns_none_when_hermes_home_unset(self, monkeypatch)` (method)
- L28 `test_returns_none_when_home_dir_missing(self, tmp_path, monkeypatch)` (method)
- L36 `test_returns_path_when_home_dir_exists(self, tmp_path, monkeypatch)` (method)
- L45 `test_returns_profile_specific_path(self, tmp_path, monkeypatch)` (method) — Named profiles get their own isolated HOME.
- L55 `test_two_profiles_get_different_homes(self, tmp_path, monkeypatch)` (method)
- L76 `test_context_override_is_thread_local(self, tmp_path, monkeypatch)` (method)
- L119 `TestMakeRunEnvHomeInjection` (class) — Verify _make_run_env() injects HOME into subprocess envs.
- L122 `test_injects_home_when_profile_home_exists(self, tmp_path, monkeypatch)` (method)
- L135 `test_no_injection_when_home_dir_missing(self, tmp_path, monkeypatch)` (method)
- L148 `test_no_injection_when_hermes_home_unset(self, monkeypatch)` (method)
- L158 `test_context_override_bridges_to_subprocess_env(self, tmp_path, monkeypatch)` (method)
- L185 `TestSanitizeSubprocessEnvHomeInjection` (class) — Verify _sanitize_subprocess_env() injects HOME for background procs.
- L188 `test_injects_home_when_profile_home_exists(self, tmp_path, monkeypatch)` (method)
- L200 `test_no_injection_when_home_dir_missing(self, tmp_path, monkeypatch)` (method)
- L211 `test_context_override_bridges_to_background_env(self, tmp_path, monkeypatch)` (method)
- L237 `TestProfileBootstrap` (class) — Verify new profiles get a home/ subdirectory.
- L240 `test_profile_dirs_includes_home(self)` (method)
- L244 `test_create_profile_bootstraps_home_dir(self, tmp_path, monkeypatch)` (method) — create_profile() should create home/ inside the profile dir.
- L260 `TestPythonProcessUnchanged` (class) — Confirm the Python process's own HOME is never modified.
- L263 `test_path_home_unchanged_after_subprocess_home_resolved(self, tmp_path, monkeypatch)` (method)
