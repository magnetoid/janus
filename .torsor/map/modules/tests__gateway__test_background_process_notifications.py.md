---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_background_process_notifications.py

Symbols in `tests/gateway/test_background_process_notifications.py`.

- L24 `_FakeRegistry` (class) — Return pre-canned sessions, then None once exhausted.
- L27 `__init__(self, sessions)` (method)
- L30 `get(self, session_id)` (method)
- L35 `is_completion_consumed(self, session_id)` (method)
- L39 `_build_runner(monkeypatch, tmp_path, mode: str)` (function) — Create a GatewayRunner with a fake config for the given mode.
- L56 `_watcher_dict(session_id='proc_test', thread_id='')` (function)
- L72 `TestLoadBackgroundNotificationsMode` (class)
- L74 `test_defaults_to_all(self, monkeypatch, tmp_path)` (method)
- L80 `test_reads_config_yaml(self, monkeypatch, tmp_path)` (method)
- L89 `test_env_var_overrides_config(self, monkeypatch, tmp_path)` (method)
- L98 `test_false_value_maps_to_off(self, monkeypatch, tmp_path)` (method)
- L107 `test_invalid_value_defaults_to_all(self, monkeypatch, tmp_path)` (method)
- L182 `test_run_process_watcher_respects_notification_mode(monkeypatch, tmp_path, mode, sessions, expected_calls, expected_fragment)` (function)
- L208 `test_thread_id_passed_to_send(monkeypatch, tmp_path)` (function) — thread_id from watcher dict is forwarded as metadata to adapter.send().
- L230 `test_no_thread_id_sends_no_metadata(monkeypatch, tmp_path)` (function) — When thread_id is empty, metadata should be None (general topic).
- L252 `test_inject_watch_notification_routes_from_session_store_origin(monkeypatch, tmp_path)` (function)
- L287 `test_agent_notification_carries_message_id_reply_anchor(monkeypatch, tmp_path)` (function) — notify_on_complete injection carries the triggering message_id so the
- L327 `test_agent_notification_no_message_id_is_tolerated(monkeypatch, tmp_path)` (function) — A watcher dict without message_id (CLI spawn, pre-upgrade checkpoint)
- L361 `test_inject_watch_notification_carries_message_id_reply_anchor(monkeypatch, tmp_path)` (function)
- L391 `test_build_process_event_source_falls_back_to_session_key_chat_type(monkeypatch, tmp_path)` (function)
- L415 `test_build_process_event_source_uses_cached_live_source_before_session_key_parse(monkeypatch, tmp_path)` (function)
- L450 `test_inject_watch_notification_ignores_foreground_event_source(monkeypatch, tmp_path)` (function) — Negative test: watch notification must NOT route to the foreground thread.
- L484 `test_build_process_event_source_returns_none_for_empty_evt(monkeypatch, tmp_path)` (function) — Missing session_key and no platform metadata → None (drop notification).
- L492 `test_build_process_event_source_returns_none_for_invalid_platform(monkeypatch, tmp_path)` (function) — Invalid platform string → None.
- L506 `test_build_process_event_source_returns_none_for_short_session_key(monkeypatch, tmp_path)` (function) — Session key with <5 parts doesn't parse, falls through to empty metadata → None.
- L522 `test_parse_session_key_valid()` (function)
- L527 `test_parse_session_key_with_extra_parts()` (function) — 6th part in a group key may be a user_id, not a thread_id — omit it.
- L533 `test_parse_session_key_with_user_id_part()` (function) — Group keys with per-user isolation have user_id as 6th part — don't return as thread_id.
- L539 `test_parse_session_key_dm_with_thread()` (function) — DM keys use parts[5] as thread_id unambiguously.
- L545 `test_parse_session_key_thread_chat_type()` (function) — Thread-typed keys use parts[5] as thread_id unambiguously.
- L551 `test_parse_session_key_too_short()` (function)
- L556 `test_parse_session_key_wrong_prefix()` (function)
