---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_kanban_notifier.py

Symbols in `tests/gateway/test_kanban_notifier.py`.

- L10 `RecordingAdapter` (class)
- L11 `__init__(self)` (method)
- L14 `send(self, chat_id, text, metadata=None)` (method)
- L18 `DisconnectedAdapters` (class) — Expose a platform during collection, then simulate disconnect on get().
- L21 `get(self, key, default=None)` (method)
- L25 `_run_one_notifier_tick(monkeypatch, runner)` (function)
- L38 `_make_runner(adapter)` (function)
- L46 `_create_completed_subscription(summary='done once')` (function)
- L57 `_unseen_terminal_events(tid)` (function)
- L72 `test_kanban_notifier_dedupes_board_slugs_pointing_to_same_db(tmp_path, monkeypatch)` (function)
- L91 `test_kanban_notifier_claim_prevents_second_watcher_send(tmp_path, monkeypatch)` (function)
- L108 `test_kanban_notifier_rewinds_claim_if_adapter_disconnects(tmp_path, monkeypatch)` (function)
- L124 `test_kanban_db_path_is_test_isolated_from_real_home()` (function)
- L140 `FailingAdapter` (class) — Adapter whose send() always raises, simulating a transient send error.
- L143 `__init__(self)` (method)
- L146 `send(self, chat_id, text, metadata=None)` (method)
- L151 `test_kanban_notifier_rewinds_claim_on_send_exception(tmp_path, monkeypatch)` (function) — A raising adapter rewinds the claim so the next tick can retry.
- L176 `test_notifier_redelivers_same_kind_on_dispatch_cycle(tmp_path, monkeypatch)` (function) — A retry cycle (crashed → reclaimed → crashed) notifies the user twice.
