---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_usage_command.py

Symbols in `tests/gateway/test_usage_command.py`.

- L9 `_make_mock_agent(**overrides)` (function) — Create a mock AIAgent with realistic session counters.
- L44 `_make_runner(session_key, agent=None, cached_agent=None)` (function) — Build a bare GatewayRunner with just the fields _handle_usage_command needs.
- L70 `TestUsageCachedAgent` (class) — The main fix: /usage should find agents in _agent_cache between turns.
- L74 `test_cached_agent_shows_detailed_usage(self)` (method)
- L95 `test_running_agent_preferred_over_cache(self)` (method) — When agent is in both dicts, the running one wins.
- L111 `test_sentinel_skipped_uses_cache(self)` (method) — PENDING sentinel in _running_agents should fall through to cache.
- L129 `test_no_agent_anywhere_falls_to_history(self)` (method) — No running or cached agent → rough estimate from transcript.
- L150 `test_cache_read_write_hidden_when_zero(self)` (method) — Cache token lines should be omitted when zero.
- L165 `test_cost_included_status(self)` (method) — Subscription-included providers show 'included' instead of dollar amount.
- L179 `TestUsageAccountSection` (class) — Account-limits section appended to /usage output (PR #2486).
- L183 `test_usage_command_includes_account_section(self, monkeypatch)` (method)
- L212 `test_usage_command_uses_persisted_provider_when_agent_not_running(self, monkeypatch)` (method)
