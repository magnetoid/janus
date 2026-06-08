---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_tls_fd_recycle_corruption.py

Symbols in `tests/run_agent/test_tls_fd_recycle_corruption.py`.

- L38 `_FakeSocket` (class) — Records shutdown/close calls without touching real FDs.
- L41 `__init__(self)` (method)
- L45 `shutdown(self, _how)` (method)
- L48 `close(self)` (method)
- L52 `_build_fake_client(sock)` (function) — Mimic the httpcore-1 layout that ``_iter_pool_sockets`` walks.
- L63 `test_force_close_tcp_sockets_shutdown_only_no_close()` (function) — The smoking-gun guarantee: shutdown is called, close is NOT.
- L85 `test_force_close_tcp_sockets_uses_shut_rdwr()` (function) — Both directions must be shut down so the SSL state machine fully unwinds.
- L110 `test_force_close_tcp_sockets_swallows_oserror_on_shutdown()` (function) — A socket already shut down / not connected raises ``OSError`` — benign.
- L127 `test_force_close_tcp_sockets_handles_multiple_pool_entries()` (function) — Walk every pool connection — the bug equally applies to all of them.
- L152 `_make_agent_mock()` (function) — Minimal agent with the two close primitives stubbed for spy-style checks.
- L161 `_call_inside_owner_thread(callable_)` (function) — Run callable_ on a separate thread so its ``threading.get_ident()``
- L180 `test_close_from_stranger_thread_aborts_only_no_close()` (function) — Stranger-thread close → ``_abort_request_openai_client``, holder NOT popped.
- L242 `test_close_from_owner_thread_pops_and_full_close()` (function) — Worker-thread close → ``_close_request_openai_client``, holder popped.
- L284 `test_stranger_then_owner_close_sequence_runs_full_close_exactly_once()` (function) — Stranger abort followed by owner close → full close runs once.
- L353 `test_agent_abort_request_openai_client_does_not_call_client_close(caplog)` (function) — ``_abort_request_openai_client`` must shutdown sockets but NEVER close().
- L395 `test_agent_abort_request_openai_client_null_client_is_noop()` (function) — A ``None`` client must short-circuit cleanly (defensive).
- L412 `test_fd_recycle_window_closed_by_shutdown_only()` (function) — Construct the exact race the reporter saw — abort from a stranger
