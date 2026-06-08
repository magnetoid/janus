---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_background_status_indicator.py

Symbols in `tests/cli/test_cli_background_status_indicator.py`.

- L15 `_stub_thread()` (function) — Return a Thread instance that's never started — pure dict-value stand-in.
- L20 `_make_cli()` (function) — Bare-metal HermesCLI for snapshot/build tests (no __init__ side effects).
- L31 `test_snapshot_reports_zero_when_no_background_tasks()` (function)
- L37 `test_snapshot_counts_live_background_tasks()` (function)
- L44 `test_snapshot_safe_when_background_tasks_attr_missing()` (function) — Older HermesCLI instances (tests with __new__, etc.) may lack the attr.
- L55 `test_plain_text_status_omits_indicator_when_idle()` (function)
- L61 `test_plain_text_status_shows_indicator_when_active()` (function)
- L68 `test_plain_text_status_shows_higher_count()` (function)
- L79 `test_narrow_width_omits_bg_indicator()` (function) — The narrow tier (<52) is already cramped — bg is secondary, drop it.
- L87 `test_fragments_include_bg_segment_when_active()` (function)
- L98 `test_fragments_omit_bg_segment_when_idle()` (function)
- L114 `_FakeRunningRegistry` (class) — Minimal stand-in for process_registry; exposes count_running().
- L117 `__init__(self, count: int)` (method)
- L120 `count_running(self)` (method)
- L124 `_patch_process_registry(monkeypatch, count: int)` (function)
- L129 `test_snapshot_reports_zero_when_no_background_processes(monkeypatch)` (function)
- L136 `test_snapshot_counts_live_background_processes(monkeypatch)` (function)
- L143 `test_snapshot_safe_when_process_registry_raises(monkeypatch)` (function) — If count_running() raises the snapshot stays at 0; no propagate.
- L157 `test_plain_text_status_shows_proc_indicator_when_active(monkeypatch)` (function)
- L164 `test_plain_text_status_omits_proc_indicator_when_idle(monkeypatch)` (function)
- L171 `test_fragments_include_proc_segment_when_active(monkeypatch)` (function)
- L181 `test_indicators_independent_agents_and_processes(monkeypatch)` (function) — ▶ (agent tasks) and ⚙ (shell processes) render side-by-side.
