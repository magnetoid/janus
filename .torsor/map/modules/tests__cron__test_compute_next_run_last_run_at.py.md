---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_compute_next_run_last_run_at.py

Symbols in `tests/cron/test_compute_next_run_last_run_at.py`.

- L15 `TestCronComputeNextRunUsesLastRunAt` (class) — compute_next_run MUST use last_run_at as the croniter base for cron jobs,
- L19 `test_cron_uses_last_run_at_for_every_6h_schedule(self, monkeypatch)` (method) — For a schedule like 'every 6 hours', the base time matters.
- L48 `test_cron_without_last_run_at_uses_now(self, monkeypatch)` (method) — When last_run_at is NOT provided, compute_next_run falls back to
- L68 `test_cron_weekly_consistent_with_interval(self, monkeypatch)` (method) — Both cron and interval jobs should anchor to last_run_at when
