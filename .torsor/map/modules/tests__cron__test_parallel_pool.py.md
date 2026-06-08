---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_parallel_pool.py

Symbols in `tests/cron/test_parallel_pool.py`.

- L15 `TestPersistentPool` (class) — _get_parallel_pool returns a persistent ThreadPoolExecutor.
- L18 `test_pool_is_reused(self, monkeypatch)` (method) — Same pool instance returned when max_workers doesn't change.
- L33 `test_pool_is_recreated_on_worker_change(self, monkeypatch)` (method) — New pool when max_workers changes.
- L46 `test_shutdown_clears_pool(self, monkeypatch)` (method) — _shutdown_parallel_pool resets state.
- L59 `TestRunningJobGuard` (class) — _running_job_ids prevents double-dispatch of active jobs.
- L62 `test_running_set_prevents_double_dispatch(self, tmp_path, monkeypatch)` (method) — A job already in _running_job_ids is skipped on the next tick.
- L100 `TestSyncMode` (class) — tick() blocks by default (sync=True); tick(sync=False) returns immediately.
- L103 `test_sync_true_blocks_and_returns_correct_count(self, tmp_path, monkeypatch)` (method) — sync=True waits for jobs and returns actual results.
- L130 `test_sync_false_returns_immediately(self, tmp_path, monkeypatch)` (method) — sync=False returns before parallel jobs finish (optimistic count).
- L174 `TestSequentialPool` (class) — Sequential (workdir/profile) jobs use the persistent cron-seq pool.
- L182 `test_sequential_job_does_not_block_ticker(self, tmp_path, monkeypatch)` (method) — sync=False returns immediately even when a workdir job is slow.
- L226 `test_sequential_running_guard_prevents_double_dispatch(self, tmp_path, monkeypatch)` (method) — A workdir job already in _running_job_ids is skipped on next tick.
- L264 `test_get_sequential_pool_is_persistent(self)` (method) — _get_sequential_pool returns the same single-thread pool.
