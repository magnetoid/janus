---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_kanban_per_profile_cap.py

Symbols in `tests/hermes_cli/test_kanban_per_profile_cap.py`.

- L18 `isolated_kanban_home_with_profiles(monkeypatch)` (function) — Spin up a fresh HERMES_HOME with kanban DB + alpha/beta profiles.
- L31 `_fake_spawn(*args, **kwargs)` (function)
- L35 `test_no_cap_all_tasks_dispatched(isolated_kanban_home_with_profiles)` (function) — Baseline: with no per-profile cap, all ready tasks dispatch.
- L50 `test_cap_2_balances_two_profiles(isolated_kanban_home_with_profiles)` (function) — With cap=2: 2 alpha + 2 beta dispatched; remaining 3 alpha + 1 beta
- L73 `test_pre_existing_running_counts_against_cap(isolated_kanban_home_with_profiles)` (function) — A task already in 'running' status when dispatch_once starts counts
- L104 `test_invalid_cap_treated_as_no_cap(isolated_kanban_home_with_profiles, cap)` (function) — Cap values that don't represent a positive int should be treated as
- L121 `test_capped_tasks_dispatched_on_subsequent_tick(isolated_kanban_home_with_profiles)` (function) — A task deferred this tick because its profile was at cap should be
- L160 `test_dispatch_result_has_skipped_per_profile_capped_field()` (function) — Schema-level invariant: DispatchResult exposes the
