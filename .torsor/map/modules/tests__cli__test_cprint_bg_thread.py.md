---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cprint_bg_thread.py

Symbols in `tests/cli/test_cprint_bg_thread.py`.

- L25 `reset_output_history()` (function)
- L31 `test_cprint_no_app_direct_print(monkeypatch)` (function) — No active app → direct _pt_print, no run_in_terminal involvement.
- L48 `test_cprint_app_not_running_direct_print(monkeypatch)` (function) — App exists but not running (e.g. teardown) → direct print.
- L65 `test_cprint_bg_thread_schedules_on_app_loop(monkeypatch)` (function) — App running + different thread → schedules via call_soon_threadsafe.
- L123 `test_cprint_same_thread_as_app_loop_direct_print(monkeypatch)` (function) — App running on same thread → direct print (no scheduling).
- L159 `test_cprint_swallows_app_loop_attr_error(monkeypatch)` (function) — Loop missing on app → fall back to direct print, no crash.
- L182 `test_cprint_swallows_prompt_toolkit_import_error(monkeypatch)` (function) — If prompt_toolkit.application itself fails to import, fall back.
- L218 `test_output_history_preserves_ansi_and_keeps_recent_lines()` (function)
- L229 `test_replay_output_history_does_not_record_replayed_lines(monkeypatch)` (function)
- L247 `test_replay_output_history_rerenders_callable_entries(monkeypatch)` (function)
- L267 `test_replay_output_history_batches_rendered_lines_into_one_print(monkeypatch)` (function)
- L282 `test_chat_console_records_rich_ansi_for_resize_replay(monkeypatch)` (function)
- L292 `test_suspend_output_history_blocks_recording()` (function)
- L302 `test_clear_output_history_removes_replayable_lines()` (function)
