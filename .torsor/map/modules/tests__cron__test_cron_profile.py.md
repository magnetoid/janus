---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_cron_profile.py

Symbols in `tests/cron/test_cron_profile.py`.

- L16 `isolated_cron_profile_home(tmp_path, monkeypatch)` (function) — Create an isolated Hermes root with a named profile and temp cron store.
- L31 `TestNormalizeProfile` (class)
- L32 `test_none_and_empty_return_none(self, isolated_cron_profile_home)` (method)
- L39 `test_default_profile_is_valid_and_normalized(self, isolated_cron_profile_home)` (method)
- L44 `test_named_profile_must_exist_and_is_normalized(self, isolated_cron_profile_home)` (method)
- L49 `test_invalid_profile_name_is_rejected(self, isolated_cron_profile_home)` (method)
- L55 `test_missing_named_profile_is_rejected(self, isolated_cron_profile_home)` (method)
- L62 `TestCreateAndUpdateJobProfile` (class)
- L63 `test_create_stores_profile_id(self, isolated_cron_profile_home)` (method)
- L72 `test_create_without_profile_preserves_old_behaviour(self, isolated_cron_profile_home)` (method)
- L81 `test_create_accepts_explicit_default(self, isolated_cron_profile_home)` (method)
- L90 `test_update_sets_and_clears_profile(self, isolated_cron_profile_home)` (method)
- L104 `test_update_rejects_missing_profile(self, isolated_cron_profile_home)` (method)
- L112 `TestCronjobToolProfile` (class)
- L113 `test_create_and_list_with_profile(self, isolated_cron_profile_home)` (method)
- L130 `test_update_clears_profile_with_empty_string(self, isolated_cron_profile_home)` (method)
- L148 `test_schema_advertises_profile(self)` (method)
- L160 `TestRunJobProfileContext` (class)
- L162 `_install_agent_stubs(monkeypatch, observed: dict)` (method)
- L233 `test_run_job_sets_and_restores_profile_home(self, isolated_cron_profile_home, monkeypatch)` (method)
- L263 `test_profile_dotenv_environment_is_restored(self, isolated_cron_profile_home, monkeypatch)` (method)
- L305 `test_no_agent_profile_uses_profile_scripts_dir_and_restores_env(self, isolated_cron_profile_home, monkeypatch)` (method)
- L334 `test_run_job_without_profile_leaves_hermes_home_untouched(self, isolated_cron_profile_home, monkeypatch)` (method)
- L356 `test_run_job_falls_back_on_missing_runtime_profile(self, isolated_cron_profile_home, monkeypatch)` (method)
- L381 `TestTickProfilePartition` (class)
- L382 `test_profile_and_workdir_combined(self, isolated_cron_profile_home, monkeypatch)` (method) — Both profile and workdir set — verify both are applied and restored.
- L409 `test_profile_jobs_run_sequentially(self, isolated_cron_profile_home, monkeypatch)` (method)
