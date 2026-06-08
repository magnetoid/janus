---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_curator_archive_prune.py

Symbols in `tests/hermes_cli/test_curator_archive_prune.py`.

- L19 `_ns(**kwargs)` (function)
- L26 `test_archive_refuses_pinned(monkeypatch, capsys)` (function)
- L45 `test_archive_calls_archive_skill(monkeypatch, capsys)` (function)
- L59 `test_archive_reports_failure(monkeypatch, capsys)` (function)
- L76 `_mk_record(name, *, idle_days=0, pinned=False, state='active', created_idle_days=None)` (function)
- L92 `test_prune_days_validation(monkeypatch, capsys)` (function)
- L100 `test_prune_nothing_to_do(monkeypatch, capsys)` (function)
- L110 `test_prune_filters_pinned_and_archived(monkeypatch, capsys)` (function)
- L138 `test_prune_falls_back_to_created_at_when_never_used(monkeypatch, capsys)` (function) — Never-used skills must be prunable via created_at — otherwise immortal.
- L158 `test_prune_dry_run_makes_no_changes(monkeypatch, capsys)` (function)
- L177 `test_prune_prompts_without_yes(monkeypatch, capsys)` (function)
- L195 `test_prune_confirms_with_y(monkeypatch, capsys)` (function)
- L212 `test_prune_reports_partial_failure(monkeypatch, capsys)` (function)
- L238 `test_archive_and_prune_registered()` (function)
- L256 `test_prune_defaults()` (function)
