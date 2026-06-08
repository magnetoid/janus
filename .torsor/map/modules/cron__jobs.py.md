---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# cron/jobs.py

Symbols in `cron/jobs.py`.

- L55 `_job_output_dir(job_id: str)` (function) — Resolve a job's output directory, rejecting any path-escape attempt.
- L71 `_normalize_skill_list(skill: Optional[str]=None, skills: Optional[Any]=None)` (function) — Normalize legacy/single-skill and multi-skill inputs into a unique ordered list.
- L88 `_apply_skill_fields(job: Dict[str, Any])` (function) — Return a job dict with canonical `skills` and legacy `skill` fields aligned.
- L97 `_coerce_job_text(value: Any, fallback: str='')` (function) — Coerce legacy/hand-edited nullable cron fields to strings for readers.
- L104 `_schedule_display_for_job(job: Dict[str, Any])` (function)
- L121 `_normalize_job_record(job: Dict[str, Any])` (function) — Return a read-safe cron job shape for UI/API/tool/scheduler consumers.
- L159 `_secure_dir(path: Path)` (function) — Set directory to owner-only access (0700). No-op on Windows.
- L167 `_secure_file(path: Path)` (function) — Set file to owner-only read/write (0600). No-op on Windows.
- L176 `ensure_dirs()` (function) — Ensure cron directories exist with secure permissions.
- L188 `parse_duration(s: str)` (function) — Parse duration string into minutes.
- L209 `parse_schedule(schedule: str)` (function) — Parse schedule string into structured format.
- L298 `_ensure_aware(dt: datetime)` (function) — Return a timezone-aware datetime in Hermes configured timezone.
- L317 `_recoverable_oneshot_run_at(schedule: Dict[str, Any], now: datetime, *, last_run_at: Optional[str]=None)` (function) — Return a one-shot run time if it is still eligible to fire.
- L344 `_compute_grace_seconds(schedule: dict)` (function) — Compute how late a job can be and still catch up instead of fast-forwarding.
- L376 `compute_next_run(schedule: Dict[str, Any], last_run_at: Optional[str]=None)` (function) — Compute the next run time for a schedule.
- L426 `load_jobs()` (function) — Load all jobs from storage.
- L474 `save_jobs(jobs: List[Dict[str, Any]])` (function) — Save all jobs to storage.
- L493 `_normalize_workdir(workdir: Optional[str])` (function) — Normalize and validate a cron job workdir.
- L526 `_normalize_profile(profile: Optional[str])` (function) — Normalize and validate an optional cron job profile name.
- L550 `create_job(prompt: Optional[str], schedule: str, name: Optional[str]=None, repeat: Optional[int]=None, deliver: Optional[str]=None, origin: Optional[Dict[str, Any]]=None, skill: Optional[str]=None, skills: Optional[List[str]]=None, model: Optional[str]=None, provider: Optional[str]=None, base_url: Optional[str]=None, script: Optional[str]=None, context_from: Optional[Union[str, List[str]]]=None, enabled_toolsets: Optional[List[str]]=None, workdir: Optional[str]=None, profile: Optional[str]=None, no_agent: bool=False)` (function) — Create a new cron job.
- L715 `get_job(job_id: str)` (function) — Get a job by ID.
- L724 `AmbiguousJobReference` (class) — Raised when a job name matches more than one job.
- L727 `__init__(self, ref: str, matches: List[Dict[str, Any]])` (method)
- L737 `resolve_job_ref(ref: str)` (function) — Resolve a job reference (ID or name) to a job record.
- L762 `list_jobs(include_disabled: bool=False)` (function) — List all jobs, optionally including disabled ones.
- L770 `update_job(job_id: str, updates: Dict[str, Any])` (function) — Update a job by ID, refreshing derived schedule fields when needed.
- L836 `pause_job(job_id: str, reason: Optional[str]=None)` (function) — Pause a job without deleting it. Accepts a job ID or name.
- L852 `resume_job(job_id: str)` (function) — Resume a paused job and compute the next future run from now. Accepts a job ID or name.
- L871 `trigger_job(job_id: str)` (function) — Schedule a job to run on the next scheduler tick. Accepts a job ID or name.
- L888 `remove_job(job_id: str)` (function) — Remove a job by ID or name.
- L910 `mark_job_run(job_id: str, success: bool, error: Optional[str]=None, delivery_error: Optional[str]=None)` (function) — Mark a job as having been run.
- L983 `advance_next_run(job_id: str)` (function) — Preemptively advance next_run_at for a recurring job before execution.
- L1012 `get_due_jobs()` (function) — Get all jobs that are due to run now.
- L1024 `_get_due_jobs_locked()` (function) — Inner implementation of get_due_jobs(); must be called with _jobs_file_lock held.
- L1114 `save_job_output(job_id: str, output: str)` (function) — Save job output to file.
- L1146 `rewrite_skill_refs(consolidated: Optional[Dict[str, str]]=None, pruned: Optional[List[str]]=None)` (function) — Rewrite cron job skill references after a curator consolidation pass.
