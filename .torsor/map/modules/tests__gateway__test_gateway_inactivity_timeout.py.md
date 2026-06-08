---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_gateway_inactivity_timeout.py

Symbols in `tests/gateway/test_gateway_inactivity_timeout.py`.

- L22 `FakeAgent` (class) — Mock agent with controllable activity summary for timeout tests.
- L25 `__init__(self, idle_seconds=0.0, activity_desc='tool_call', current_tool=None, api_call_count=5, max_iterations=90)` (method)
- L35 `get_activity_summary(self)` (method)
- L45 `interrupt(self, msg)` (method)
- L49 `run_conversation(self, prompt)` (method)
- L53 `SlowFakeAgent` (class) — Agent that runs for a while, then goes idle.
- L56 `__init__(self, run_duration=0.5, idle_after=None, **kwargs)` (method)
- L62 `get_activity_summary(self)` (method)
- L74 `run_conversation(self, prompt)` (method)
- L80 `TestStagedInactivityWarning` (class) — Test the staged inactivity warning before full timeout.
- L83 `test_warning_fires_once_before_timeout(self)` (method) — Warning fires when inactivity reaches warning threshold.
- L127 `test_warning_disabled_when_zero(self)` (method) — No warning fires when gateway_timeout_warning is 0.
- L163 `test_warning_fires_only_once(self)` (method) — Warning fires exactly once even if agent remains idle.
- L199 `test_full_timeout_still_fires_after_warning(self)` (method) — Full timeout fires even after warning was sent.
- L239 `test_warning_env_var_respected(self, monkeypatch)` (method) — HERMES_AGENT_TIMEOUT_WARNING env var is parsed correctly.
- L245 `test_warning_zero_means_disabled(self, monkeypatch)` (method) — HERMES_AGENT_TIMEOUT_WARNING=0 disables the warning.
- L252 `test_unlimited_timeout_no_warning(self)` (method) — When timeout is unlimited (0), no warning fires either.
- L272 `TestWarningThresholdBelowTimeout` (class) — Test that warning threshold must be less than timeout threshold.
- L275 `test_warning_at_half_timeout(self)` (method) — Warning fires at half the timeout duration.
