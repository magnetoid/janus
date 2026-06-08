---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_memory_session_switch.py

Symbols in `tests/agent/test_memory_session_switch.py`.

- L17 `_RecordingProvider` (class) — Provider that records every lifecycle call for assertion.
- L20 `__init__(self, name='rec')` (method)
- L28 `name(self)` (method)
- L31 `is_available(self)` (method)
- L34 `initialize(self, session_id, **kwargs)` (method)
- L37 `get_tool_schemas(self)` (method)
- L40 `sync_turn(self, user_content, assistant_content, *, session_id='')` (method)
- L45 `queue_prefetch(self, query, *, session_id='')` (method)
- L48 `on_session_switch(self, new_session_id, *, parent_session_id='', reset=False, **kwargs)` (method)
- L71 `_MinimalProvider` (class) — Provider that does NOT override on_session_switch — ABC default must no-op.
- L75 `name(self)` (method)
- L78 `is_available(self)` (method)
- L81 `initialize(self, session_id, **kwargs)` (method)
- L84 `get_tool_schemas(self)` (method)
- L88 `test_abc_default_on_session_switch_is_noop()` (function) — Providers that don't override the hook must not raise.
- L103 `test_manager_fans_out_to_all_providers()` (function)
- L122 `test_manager_ignores_empty_session_id()` (function) — Empty string session_id must not trigger provider hooks.
- L136 `test_manager_isolates_provider_failures()` (function) — A provider that raises must not block other providers.
- L157 `test_manager_reset_flag_preserved()` (function)
- L171 `test_sync_all_propagates_session_id_to_providers()` (function) — run_agent.py's sync_all call must pass session_id through to providers.
- L187 `test_queue_prefetch_all_propagates_session_id_to_providers()` (function)
- L200 `_make_hindsight_provider()` (function) — Build a bare HindsightMemoryProvider that skips network setup.
- L264 `test_hindsight_on_session_switch_updates_session_id_and_mints_fresh_doc()` (function)
- L279 `test_hindsight_on_session_switch_clears_turn_buffers()` (function) — Accumulated _session_turns must not leak into the next session.
- L293 `test_hindsight_on_session_switch_clears_on_reset_true()` (function) — reset=True (from /new, /reset) must also flush buffers.
- L302 `test_hindsight_on_session_switch_ignores_empty_id()` (function) — Empty new_session_id must be a no-op to avoid corrupting state.
- L322 `test_hindsight_preserves_parent_across_empty_parent_arg()` (function) — Omitting parent_session_id must NOT overwrite an existing one.
