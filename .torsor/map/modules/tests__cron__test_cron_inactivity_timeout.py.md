---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cron/test_cron_inactivity_timeout.py

Symbols in `tests/cron/test_cron_inactivity_timeout.py`.

- L22 `FakeAgent` (class) — Mock agent with controllable activity summary for timeout tests.
- L25 `__init__(self, idle_seconds=0.0, activity_desc='tool_call', current_tool=None, api_call_count=5, max_iterations=90)` (method)
- L35 `get_activity_summary(self)` (method)
- L45 `interrupt(self, msg)` (method)
- L49 `run_conversation(self, prompt)` (method) — Simulate a quick agent run that finishes immediately.
- L54 `SlowFakeAgent` (class) — Agent that runs for a while, simulating active work then going idle.
- L57 `__init__(self, run_duration=0.5, idle_after=None, **kwargs)` (method)
- L63 `get_activity_summary(self)` (method)
- L76 `run_conversation(self, prompt)` (method)
- L82 `TestInactivityTimeout` (class) — Test the inactivity-based timeout polling loop in cron scheduler.
- L85 `test_active_agent_completes_normally(self)` (method) — An agent that finishes quickly should return its result.
- L115 `test_idle_agent_triggers_timeout(self)` (method) — An agent that goes idle should be detected and interrupted.
- L155 `test_unlimited_timeout(self)` (method) — HERMES_CRON_TIMEOUT=0 means no timeout at all.
- L169 `_parse_cron_timeout(self, raw_value)` (method) — Mirror the defensive parsing logic from cron/scheduler.py run_job().
- L178 `test_timeout_env_var_parsing(self, monkeypatch)` (method) — HERMES_CRON_TIMEOUT env var is respected.
- L188 `test_timeout_zero_means_unlimited(self, monkeypatch)` (method) — HERMES_CRON_TIMEOUT=0 yields None (unlimited).
- L196 `test_timeout_invalid_value_falls_back_to_default(self, monkeypatch)` (method) — HERMES_CRON_TIMEOUT=abc should fall back to 600s, not raise ValueError.
- L205 `test_timeout_empty_string_uses_default(self, monkeypatch)` (method) — HERMES_CRON_TIMEOUT='' (empty) should use the 600s default.
- L212 `test_timeout_error_includes_diagnostics(self)` (method) — The TimeoutError message should include last activity info.
- L261 `test_agent_without_activity_summary_uses_wallclock_fallback(self)` (method) — If agent lacks get_activity_summary, idle_secs stays 0 (never times out).
- L301 `TestSysPathOrdering` (class) — Test that sys.path is set before repo-level imports.
- L304 `test_hermes_time_importable(self)` (method) — hermes_time should be importable when cron.scheduler loads.
- L310 `test_hermes_constants_importable(self)` (method) — hermes_constants should be importable from cron context.
