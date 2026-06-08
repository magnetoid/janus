---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/gateway/test_api_server_jobs.py

Symbols in `tests/gateway/test_api_server_jobs.py`.

- L42 `_make_adapter(api_key: str='')` (function) — Create an adapter with optional API key.
- L51 `_create_app(adapter: APIServerAdapter)` (function) — Create the aiohttp app with jobs routes registered.
- L69 `adapter()` (function)
- L74 `auth_adapter()` (function)
- L82 `TestListJobs` (class)
- L84 `test_list_jobs(self, adapter)` (method) — GET /api/jobs returns job list.
- L104 `test_list_jobs_include_disabled(self, adapter)` (method) — GET /api/jobs?include_disabled=true passes the flag.
- L119 `test_list_jobs_default_excludes_disabled(self, adapter)` (method) — GET /api/jobs without flag passes include_disabled=False.
- L138 `TestCreateJob` (class)
- L140 `test_create_job(self, adapter)` (method) — POST /api/jobs with valid body returns created job.
- L172 `test_create_job_missing_name(self, adapter)` (method) — POST /api/jobs without name returns 400.
- L186 `test_create_job_name_too_long(self, adapter)` (method) — POST /api/jobs with name > 200 chars returns 400.
- L200 `test_create_job_prompt_too_long(self, adapter)` (method) — POST /api/jobs with prompt > 5000 chars returns 400.
- L215 `test_create_job_invalid_repeat(self, adapter)` (method) — POST /api/jobs with repeat=0 returns 400.
- L230 `test_create_job_missing_schedule(self, adapter)` (method) — POST /api/jobs without schedule returns 400.
- L247 `TestGetJob` (class)
- L249 `test_get_job(self, adapter)` (method) — GET /api/jobs/{id} returns job.
- L266 `test_get_job_not_found(self, adapter)` (method) — GET /api/jobs/{id} returns 404 when job doesn't exist.
- L280 `test_get_job_invalid_id(self, adapter)` (method) — GET /api/jobs/{id} with non-hex id returns 400.
- L291 `test_invalid_job_id_logs_source_context(self, adapter, caplog)` (method) — Invalid job-id probes log source metadata for later investigation.
- L318 `TestUpdateJob` (class)
- L320 `test_update_job(self, adapter)` (method) — PATCH /api/jobs/{id} updates with whitelisted fields.
- L346 `test_update_job_rejects_unknown_fields(self, adapter)` (method) — PATCH /api/jobs/{id} — only allowed fields pass through.
- L373 `test_update_job_no_valid_fields(self, adapter)` (method) — PATCH /api/jobs/{id} with only unknown fields returns 400.
- L391 `TestDeleteJob` (class)
- L393 `test_delete_job(self, adapter)` (method) — DELETE /api/jobs/{id} returns ok.
- L410 `test_delete_job_not_found(self, adapter)` (method) — DELETE /api/jobs/{id} returns 404 when job doesn't exist.
- L428 `TestPauseJob` (class)
- L430 `test_pause_job(self, adapter)` (method) — POST /api/jobs/{id}/pause returns updated job.
- L453 `TestResumeJob` (class)
- L455 `test_resume_job(self, adapter)` (method) — POST /api/jobs/{id}/resume returns updated job.
- L478 `TestRunJob` (class)
- L480 `test_run_job(self, adapter)` (method) — POST /api/jobs/{id}/run returns triggered job.
- L502 `TestAuthRequired` (class)
- L504 `test_auth_required_list_jobs(self, auth_adapter)` (method) — GET /api/jobs without API key returns 401 when key is set.
- L513 `test_auth_required_create_job(self, auth_adapter)` (method) — POST /api/jobs without API key returns 401 when key is set.
- L524 `test_auth_required_get_job(self, auth_adapter)` (method) — GET /api/jobs/{id} without API key returns 401 when key is set.
- L533 `test_auth_required_delete_job(self, auth_adapter)` (method) — DELETE /api/jobs/{id} without API key returns 401.
- L542 `test_auth_passes_with_valid_key(self, auth_adapter)` (method) — GET /api/jobs with correct API key succeeds.
- L563 `TestCronUnavailable` (class)
- L565 `test_cron_unavailable_list(self, adapter)` (method) — GET /api/jobs returns 501 when _CRON_AVAILABLE is False.
- L576 `test_pause_handler_no_self_binding(self, adapter)` (method) — Pause must not inject ``self`` into the cron helper call.
- L596 `test_list_handler_no_self_binding(self, adapter)` (method) — List must preserve keyword arguments without injecting ``self``.
- L616 `test_update_handler_no_self_binding(self, adapter)` (method) — Update must pass positional arguments correctly without ``self``.
- L642 `test_cron_unavailable_create(self, adapter)` (method) — POST /api/jobs returns 501 when _CRON_AVAILABLE is False.
- L653 `test_cron_unavailable_get(self, adapter)` (method) — GET /api/jobs/{id} returns 501 when _CRON_AVAILABLE is False.
- L662 `test_cron_unavailable_delete(self, adapter)` (method) — DELETE /api/jobs/{id} returns 501 when _CRON_AVAILABLE is False.
- L671 `test_cron_unavailable_pause(self, adapter)` (method) — POST /api/jobs/{id}/pause returns 501 when _CRON_AVAILABLE is False.
- L680 `test_cron_unavailable_resume(self, adapter)` (method) — POST /api/jobs/{id}/resume returns 501 when _CRON_AVAILABLE is False.
- L689 `test_cron_unavailable_run(self, adapter)` (method) — POST /api/jobs/{id}/run returns 501 when _CRON_AVAILABLE is False.
- L702 `TestCronPromptScanParity` (class) — The REST cron endpoints must reject exfiltration/injection prompts the
- L719 `test_create_job_rejects_malicious_prompt(self, adapter)` (method) — POST /api/jobs with an exfiltration prompt returns 400 and never
- L739 `test_create_job_allows_benign_prompt(self, adapter)` (method) — POST /api/jobs with a benign prompt still succeeds (no regression).
- L757 `test_update_job_rejects_malicious_prompt(self, adapter)` (method) — PATCH /api/jobs/{id} with an exfiltration prompt returns 400 and
- L775 `test_update_job_allows_benign_prompt(self, adapter)` (method) — PATCH /api/jobs/{id} with a benign prompt still succeeds.
