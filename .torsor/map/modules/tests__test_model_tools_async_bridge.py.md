---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/test_model_tools_async_bridge.py

Symbols in `tests/test_model_tools_async_bridge.py`.

- L26 `_get_current_loop()` (function) — Return the running event loop from inside a coroutine.
- L31 `_create_and_return_transport()` (function) — Simulate an async client creating a transport on the current loop.
- L47 `TestRunAsyncLoopLifecycle` (class) — Verify _run_async() keeps the event loop alive after returning.
- L50 `test_loop_not_closed_after_run_async(self)` (method) — The loop used by _run_async must still be open after the call.
- L61 `test_same_loop_reused_across_calls(self)` (method) — Consecutive _run_async calls should reuse the same loop.
- L73 `test_cached_transport_survives_between_calls(self)` (method) — A transport/future created in call 1 must be valid in call 2.
- L87 `TestRunAsyncWorkerThread` (class) — Verify worker threads get persistent per-thread loops (delegate_task fix).
- L90 `test_worker_thread_loop_not_closed(self)` (method) — A worker thread's loop must stay open after _run_async returns,
- L109 `test_worker_thread_reuses_loop_across_calls(self)` (method) — Multiple _run_async calls on the same worker thread should
- L129 `test_parallel_workers_get_separate_loops(self)` (method) — Different worker threads must get their own loops to avoid
- L161 `test_worker_loop_separate_from_main_loop(self)` (method) — Worker thread loops must be different from the main thread's
- L182 `TestRunAsyncWithRunningLoop` (class) — When a loop is already running, _run_async falls back to a thread.
- L186 `test_run_async_from_async_context(self)` (method) — _run_async should still work when called from inside an
- L200 `test_timeout_uses_nonblocking_executor_shutdown(self, monkeypatch)` (method) — A timeout in the running-loop branch must not block the caller.
- L278 `test_timeout_cancels_coroutine_in_worker_loop(self, monkeypatch)` (method) — On timeout, the worker's event loop must receive a cancel request
- L343 `_mock_vision_response()` (function) — Build a fake LLM response matching async_call_llm's return shape.
- L350 `TestVisionDispatchLoopSafety` (class) — Simulate the full registry.dispatch('vision_analyze') chain and
- L355 `test_vision_dispatch_keeps_loop_alive(self, tmp_path)` (method) — After dispatching vision_analyze via the registry, the event
- L399 `test_two_consecutive_vision_dispatches(self, tmp_path)` (method) — Two back-to-back vision_analyze dispatches must both succeed
- L443 `_write_fake_image(dest)` (function) — Write minimal bytes so vision_analyze_tool thinks download succeeded.
