---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_web_server_cron_profiles.py

Symbols in `tests/hermes_cli/test_web_server_cron_profiles.py`.

- L8 `isolated_profiles(tmp_path, monkeypatch)` (function) — Give profile discovery an isolated default home with one named profile.
- L25 `test_call_cron_for_profile_routes_storage_and_restores_globals(isolated_profiles)` (function)
- L54 `test_list_cron_jobs_all_includes_default_and_named_profiles(isolated_profiles)` (function)
- L85 `test_list_cron_jobs_specific_profile_filters_results(isolated_profiles)` (function)
- L110 `test_cron_mutation_without_profile_finds_named_profile_job(isolated_profiles)` (function)
- L135 `test_update_cron_job_rejects_id_mutation(isolated_profiles)` (function) — Dashboard surfaces a 400 (not a 500 or silent rename) when an
- L162 `test_cron_delete_with_profile_deletes_only_target_profile(isolated_profiles)` (function)
- L190 `test_cron_profile_validation_errors(isolated_profiles)` (function)
