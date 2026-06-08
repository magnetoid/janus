---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_status_command.py

Symbols in `tests/gateway/test_status_command.py`.

- L15 `_make_source(platform: Platform=Platform.TELEGRAM)` (function)
- L25 `_make_event(text: str, *, platform: Platform=Platform.TELEGRAM)` (function)
- L33 `_make_runner(session_entry: SessionEntry, *, platform: Platform=Platform.TELEGRAM)` (function)
- L75 `test_status_command_reports_running_agent_without_interrupt(monkeypatch)` (function)
- L108 `test_status_command_includes_session_title_when_present()` (function)
- L128 `test_status_command_reads_token_totals_from_session_db()` (function) — Regression test for #17158: /status must source token totals from the
- L157 `test_status_command_tokens_zero_when_session_db_row_missing()` (function) — When the SessionDB has no row for the current session yet (fresh
- L178 `test_agents_command_reports_active_agents_and_processes(monkeypatch)` (function)
- L222 `test_tasks_alias_routes_to_agents_command(monkeypatch)` (function)
- L247 `test_handle_message_persists_agent_token_counts(monkeypatch)` (function)
- L289 `test_first_run_slack_home_channel_onboarding_uses_parent_command(monkeypatch)` (function)
- L333 `test_first_run_non_slack_home_channel_onboarding_keeps_direct_command(monkeypatch)` (function)
- L376 `test_handle_message_discards_stale_result_after_session_invalidation(monkeypatch)` (function)
- L422 `test_handle_message_stale_result_keeps_newer_generation_callback(monkeypatch)` (function)
- L492 `test_status_command_bypasses_active_session_guard()` (function) — When an agent is running, /status must be dispatched immediately via
- L549 `test_profile_command_reports_custom_root_profile(monkeypatch, tmp_path)` (function) — Gateway /profile detects custom-root profiles (not under ~/.hermes).
- L574 `test_post_delivery_callback_generation_snapshot_happens_after_bind()` (function) — Regression: the callback_generation snapshot in _process_message_background
