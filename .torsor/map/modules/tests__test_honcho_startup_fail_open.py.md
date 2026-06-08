---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_honcho_startup_fail_open.py

Symbols in `tests/test_honcho_startup_fail_open.py`.

- L13 `_FakeHonchoConfig` (class)
- L14 `resolve_session_name(self, **kwargs)` (method)
- L18 `_configured_hybrid_config()` (function)
- L35 `_configured_tools_config(*, init_on_session_start: bool=False)` (function)
- L42 `test_honcho_hybrid_initialize_returns_without_waiting_for_session_init(monkeypatch)` (function) — Slow Honcho session creation must not block agent startup.
- L76 `test_honcho_background_init_rechecks_state_after_lock_race()` (function) — Startup should not spawn/crash if init completes while waiting for lock.
- L100 `test_honcho_prefetch_returns_without_waiting_for_first_context_fetch()` (function) — First-turn context injection must fail open when Honcho is slow.
- L135 `test_honcho_sync_turn_does_not_start_network_write_before_session_init()` (function) — Session-end sync must not create a blocking writer before init finishes.
- L173 `test_honcho_sync_turn_waits_for_full_background_startup(monkeypatch)` (function) — Manager assignment alone is not readiness while background init continues.
- L230 `test_honcho_system_prompt_advertises_active_while_background_init_runs(monkeypatch)` (function) — Prompt metadata should not require a completed network session.
- L259 `test_honcho_tools_eager_init_still_ready_on_return(monkeypatch)` (function) — tools + initOnSessionStart=true keeps its ready-on-return contract.
- L283 `test_honcho_tools_eager_init_failure_does_not_leave_ready_manager(monkeypatch)` (function) — Failed eager tools startup must not leave hooks seeing a ready session.
- L317 `test_honcho_tools_lazy_hooks_do_not_prestart_background_init(monkeypatch)` (function) — tools lazy mode lets the first tool call own session initialization.
