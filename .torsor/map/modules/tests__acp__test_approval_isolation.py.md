---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp/test_approval_isolation.py

Symbols in `tests/acp/test_approval_isolation.py`.

- L20 `TestThreadLocalApprovalCallback` (class) — GHSA-qg5c-hvr5-hjgr: set_approval_callback must be per-thread so
- L24 `test_set_and_get_in_same_thread(self)` (method)
- L34 `test_callback_not_visible_in_different_thread(self)` (method) — Thread A's callback is NOT visible to Thread B.
- L71 `test_main_thread_callback_not_leaked_to_worker(self)` (method) — A callback set in the main thread does NOT leak into a
- L96 `test_sudo_password_callback_also_thread_local(self)` (method) — Same protection applies to the sudo password callback.
- L118 `test_sudo_password_cache_does_not_leak_across_threads(self)` (method) — Interactive sudo cache must not bleed into another executor thread.
- L141 `test_sudo_password_cache_isolated_across_acp_sessions_on_same_pool_thread(self)` (method) — ACP's ThreadPoolExecutor reuses threads. Two ACP sessions that land
- L195 `TestAcpExecAskGate` (class) — GHSA-96vc-wcxf-jjff: ACP's _run_agent must set HERMES_INTERACTIVE so
- L205 `test_interactive_env_var_routes_to_callback(self, monkeypatch)` (method) — When HERMES_INTERACTIVE is set and an approval callback is
