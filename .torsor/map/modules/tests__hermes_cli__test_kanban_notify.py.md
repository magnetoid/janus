---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_notify.py

Symbols in `tests/hermes_cli/test_kanban_notify.py`.

- L15 `kanban_home(tmp_path, monkeypatch)` (function)
- L30 `test_notifier_unsubs_after_completed_event(kanban_home)` (function) — Subscription should be remove after completed event
- L83 `test_notifier_unsubs_after_abnormal_events(kind, kanban_home)` (function) — Event kinds gave_up / crashed / timed_out send a notification but DO
- L153 `test_notifier_second_blocked_delivers(kanban_home)` (function) — After the first blocked, should receive second blocked notification.
- L246 `test_notifier_does_not_call_init_db(kanban_home)` (function) — Notifier watcher path must not invoke `_kb.init_db` (issue #21378).
- L292 `test_dispatcher_tick_does_not_call_init_db(kanban_home, monkeypatch)` (function) — `_tick_once_for_board` must not invoke `_kb.init_db` (issue #21378).
- L330 `test_notifier_skips_subscription_owned_by_other_profile(kanban_home)` (function) — Each gateway keeps its watcher on, but only the subscribing profile claims.
- L386 `test_notifier_delivers_subscription_owned_by_current_profile(kanban_home)` (function) — The gateway for the profile that created/subscribed the task reports it.
- L440 `test_gateway_create_autosubscribes_on_explicit_board(kanban_home)` (function) — `/kanban --board <slug> create ...` must subscribe on that board.
- L489 `test_notifier_uploads_artifacts_on_completion(kanban_home, tmp_path, monkeypatch)` (function) — When a completed event carries ``artifacts`` in its payload, the
- L586 `test_notifier_artifact_delivery_skips_missing_files(kanban_home, tmp_path, monkeypatch)` (function) — Missing artifact paths are silently skipped — they may have been
