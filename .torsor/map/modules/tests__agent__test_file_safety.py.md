---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_file_safety.py

Symbols in `tests/agent/test_file_safety.py`.

- L22 `TestEnvFileReadBlocking` (class) — Secret-bearing .env files must be blocked by get_read_block_error.
- L34 `test_blocked_env_basenames(self, basename)` (method) — All secret-bearing .env basenames are blocked regardless of directory.
- L42 `test_blocked_env_in_subdirectory(self)` (method) — Nested .env files are also blocked.
- L47 `test_blocked_env_absolute_path(self)` (method) — Absolute paths to .env files are blocked.
- L52 `test_allowed_env_example(self)` (method) — "The .env.example file is explicitly allowed — it's documentation, not a secret.
- L57 `test_allowed_env_sample(self)` (method) — Other .env variants like .env.sample are allowed.
- L62 `test_allowed_non_env_files(self)` (method) — Regular files are not affected by the env guard.
- L69 `test_allowed_hermes_env(self)` (method) — Hermes' own .env inside HERMES_HOME is NOT blocked by this rule
- L78 `test_blocked_set_is_lowercase(self)` (method) — All entries in the blocked set are lowercase for case-insensitive matching.
- L89 `TestCacheFileReadBlocking` (class) — Internal Hermes cache files must remain blocked.
- L92 `test_hub_index_cache_blocked(self, tmp_path)` (method) — Hub index-cache reads are blocked.
- L104 `test_hub_directory_blocked(self, tmp_path)` (method) — Hub directory reads are blocked.
- L121 `TestCombinedGuards` (class) — Both guards should work independently without interference.
- L124 `test_env_guard_works_regardless_of_hermes_home(self, tmp_path)` (method) — The env basename guard does not depend on HERMES_HOME resolution.
- L138 `test_cache_guard_still_works_with_env_guard(self, tmp_path)` (method) — Cache file blocking still works when env guard is active.
