---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_file_permissions.py

Symbols in `tests/cron/test_file_permissions.py`.

- L11 `TestCronFilePermissions` (class) — Verify cron files get secure permissions.
- L14 `setUp(self)` (method)
- L19 `tearDown(self)` (method)
- L26 `test_ensure_dirs_sets_0700(self, mock_jobs_file, mock_output, mock_cron)` (method)
- L45 `test_save_jobs_sets_0600(self, mock_jobs_file, mock_output, mock_cron)` (method)
- L59 `test_save_job_output_sets_0600(self)` (method)
- L77 `TestConfigFilePermissions` (class) — Verify config files get secure permissions.
- L80 `setUp(self)` (method)
- L83 `tearDown(self)` (method)
- L87 `test_save_config_sets_0600(self)` (method)
- L97 `test_save_env_value_sets_0600(self)` (method)
- L107 `test_ensure_hermes_home_sets_0700(self)` (method)
- L121 `TestSecureHelpers` (class) — Test the _secure_file and _secure_dir helpers.
- L124 `test_secure_file_nonexistent_no_error(self)` (method)
- L128 `test_secure_dir_nonexistent_no_error(self)` (method)
