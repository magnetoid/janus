---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# cron/scheduler.py

Symbols in `cron/scheduler.py`.

- L49 `CronPromptInjectionBlocked` (class) — Raised by _build_job_prompt when the fully-assembled prompt trips the
- L62 `_resolve_cron_disabled_toolsets(cfg: dict)` (function) — Toolsets a cron-spawned agent must never receive.
- L85 `_resolve_cron_enabled_toolsets(job: dict, cfg: dict)` (function) — Resolve the toolset list for a cron job.
- L176 `_get_parallel_pool(max_workers: Optional[int])` (function) — Return (or create) the persistent parallel pool.
- L190 `_get_sequential_pool()` (function) — Return (or create) the persistent single-thread sequential pool.
- L207 `_shutdown_parallel_pool()` (function) — Shut down the persistent pools on process exit.
- L226 `_get_hermes_home()` (function) — Resolve Hermes home dynamically while preserving test monkeypatch hooks.
- L231 `_get_lock_paths()` (function) — Resolve cron lock paths at call time so profile/env changes are honored.
- L239 `_job_profile_context(job_id: str, profile: Optional[str])` (function) — Temporarily run a job under a specific Hermes profile.
- L303 `_resolve_origin(job: dict)` (function) — Extract origin info from a job, preserving any extra routing metadata.
- L325 `_cron_job_origin_log_suffix(job: dict)` (function) — Return safe provenance details for security warnings about a cron job.
- L349 `_plugin_cron_env_var(platform_name: str)` (function) — Return the cron home-channel env var registered by a plugin platform.
- L368 `_is_known_delivery_platform(platform_name: str)` (function) — Whether ``platform_name`` is a valid cron delivery target.
- L381 `_resolve_home_env_var(platform_name: str)` (function) — Return the env var name for a platform's cron home channel.
- L394 `_get_home_target_chat_id(platform_name: str)` (function) — Return the configured home target chat/room ID for a delivery platform.
- L407 `_get_home_target_thread_id(platform_name: str)` (function) — Return the optional thread/topic ID for a platform home target.
- L433 `_iter_home_target_platforms()` (function) — Iterate built-in + plugin platform names that expose a home channel.
- L451 `cron_delivery_targets()` (function) — Return the platforms a cron job can auto-deliver to.
- L492 `_resolve_single_delivery_target(job: dict, deliver_value: str)` (function) — Resolve one concrete auto-delivery target for a cron job.
- L578 `_normalize_deliver_value(deliver)` (function) — Normalize a stored/submitted ``deliver`` value to its canonical string form.
- L605 `_expand_routing_tokens(part: str)` (function) — Expand a routing-intent token to concrete platform names.
- L623 `_resolve_delivery_targets(job: dict)` (function) — Resolve all concrete auto-delivery targets for a cron job.
- L656 `_resolve_delivery_target(job: dict)` (function) — Resolve the concrete auto-delivery target for a cron job, if any.
- L668 `_send_media_via_adapter(adapter, chat_id: str, media_files: list, metadata: dict | None, loop, job: dict, platform=None)` (function) — Send extracted MEDIA files as native platform attachments via a live adapter.
- L724 `_deliver_result(job: dict, content: str, adapters=None, loop=None)` (function) — Deliver job output to the configured target(s) (origin chat, specific platform, etc.).
- L924 `_get_script_timeout()` (function) — Resolve cron pre-run script timeout from module/env/config with a safe default.
- L957 `_run_job_script(script_path: str)` (function) — Execute a cron job's data-collection script and capture its output.
- L1084 `_parse_wake_gate(script_output: str)` (function) — Parse the last non-empty stdout line of a cron job's pre-check script
- L1110 `_build_job_prompt(job: dict, prerun_script: Optional[tuple]=None)` (function) — Build the effective prompt for a cron job, optionally loading one or more skills first.
- L1297 `_scan_assembled_cron_prompt(assembled: str, job: dict, *, has_skills: bool=False)` (function) — Scan the fully-assembled cron prompt for injection patterns. Raises
- L1344 `run_job(job: dict)` (function) — Execute a single cron job, applying any per-job profile override.
- L1351 `_run_job_impl(job: dict)` (function) — Execute a single cron job.
- L2016 `tick(verbose: bool=True, adapters=None, loop=None, sync: bool=True)` (function) — Check and run all due jobs.
