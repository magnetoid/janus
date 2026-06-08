---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/browser_supervisor.py

Symbols in `tools/browser_supervisor.py`.

- L131 `PendingDialog` (class) — A JS dialog currently open on some frame's session.
- L146 `to_dict(self)` (method)
- L158 `DialogRecord` (class) — A historical record of a dialog that was opened and then handled.
- L174 `to_dict(self)` (method)
- L187 `FrameInfo` (class) — One frame in the page's frame tree.
- L203 `to_dict(self)` (method)
- L220 `ConsoleEvent` (class) — Ring buffer entry for console + exception traffic.
- L230 `SupervisorSnapshot` (class) — Read-only snapshot of supervisor state.
- L245 `to_dict(self)` (method) — Serialize for inclusion in ``browser_snapshot`` output.
- L259 `CDPSupervisor` (class) — One supervisor per (task_id, cdp_url) pair.
- L276 `__init__(self, task_id: str, cdp_url: str, *, dialog_policy: str=DEFAULT_DIALOG_POLICY, dialog_timeout_s: float=DEFAULT_DIALOG_TIMEOUT_S)` (method)
- L323 `start(self, timeout: float=15.0)` (method) — Launch the background loop and wait until attachment is complete.
- L353 `stop(self, timeout: float=5.0)` (method) — Cancel the supervisor task and join the thread.
- L385 `snapshot(self)` (method) — Return an immutable snapshot of current state.
- L403 `respond_to_dialog(self, action: str, *, prompt_text: Optional[str]=None, dialog_id: Optional[str]=None, timeout: float=10.0)` (method) — Accept/dismiss a pending dialog. Sync bridge onto the supervisor loop.
- L465 `evaluate_runtime(self, expression: str, *, return_by_value: bool=True, await_promise: bool=True, timeout: float=10.0)` (method) — Evaluate ``expression`` in the page's Runtime context over the live WS.
- L571 `_thread_main(self)` (method) — Entry point for the supervisor's dedicated thread.
- L602 `_run(self)` (method) — Top-level supervisor coroutine.
- L698 `_attach_initial_page(self)` (method) — Find a page target, attach flattened session, enable domains, install dialog bridge.
- L727 `_install_dialog_bridge(self, session_id: str)` (method) — Install the dialog-bridge init script + Fetch interceptor on a session.
- L785 `_cdp(self, method: str, params: Optional[Dict[str, Any]]=None, *, session_id: Optional[str]=None, timeout: float=10.0)` (method) — Send a CDP command and await its response.
- L811 `_read_loop(self)` (method) — Continuously dispatch incoming CDP frames.
- L839 `_on_event(self, method: str, params: Dict[str, Any], session_id: Optional[str])` (method)
- L863 `_on_dialog_opening(self, params: Dict[str, Any], session_id: Optional[str])` (method)
- L905 `_auto_handle_dialog(self, dialog: PendingDialog, *, accept: bool, prompt_text: str)` (method) — Send handleJavaScriptDialog for auto_dismiss/auto_accept.
- L926 `_dialog_timeout_expired(self, dialog_id: str)` (method)
- L958 `_archive_dialog_locked(self, dialog: PendingDialog, closed_by: str)` (method) — Move a pending dialog to the recent_dialogs ring buffer. Must hold state_lock.
- L973 `_handle_dialog_cdp(self, dialog: PendingDialog, *, accept: bool, prompt_text: str)` (method) — Send the Page.handleJavaScriptDialog CDP command (agent path only).
- L1017 `_on_dialog_closed(self, params: Dict[str, Any], session_id: Optional[str])` (method)
- L1046 `_on_fetch_paused(self, params: Dict[str, Any], session_id: Optional[str])` (method) — Bridge XHR captured mid-flight — materialize as a pending dialog.
- L1125 `_fulfill_bridge_request(self, dialog: PendingDialog, *, accept: bool, prompt_text: str)` (method) — Resolve a bridge XHR via Fetch.fulfillRequest so the page unblocks.
- L1158 `_on_frame_attached(self, params: Dict[str, Any], session_id: Optional[str])` (method)
- L1174 `_on_frame_navigated(self, params: Dict[str, Any], session_id: Optional[str])` (method)
- L1194 `_on_frame_detached(self, params: Dict[str, Any], session_id: Optional[str])` (method) — Remove a frame from our state only when it's truly gone.
- L1231 `_on_target_attached(self, params: Dict[str, Any])` (method)
- L1259 `_enable_child_domains(self, sid: str)` (method) — Enable Page+Runtime (+nested setAutoAttach) on a child CDP session.
- L1279 `_on_target_detached(self, params: Dict[str, Any])` (method) — Handle a child CDP session detaching.
- L1311 `_on_console(self, params: Dict[str, Any], *, level_from: str)` (method)
- L1336 `_build_frame_tree_locked(self)` (method) — Build the capped frame_tree payload. Must be called under state lock.
- L1382 `_SupervisorRegistry` (class) — Process-global (task_id → supervisor) map with idempotent start/stop.
- L1389 `__init__(self)` (method)
- L1393 `get(self, task_id: str)` (method) — Return the supervisor for ``task_id`` if running, else ``None``.
- L1398 `get_or_start(self, task_id: str, cdp_url: str, *, dialog_policy: str=DEFAULT_DIALOG_POLICY, dialog_timeout_s: float=DEFAULT_DIALOG_TIMEOUT_S, start_timeout: float=15.0)` (method) — Idempotently ensure a supervisor is running for ``(task_id, cdp_url)``.
- L1442 `stop(self, task_id: str)` (method) — Stop and discard the supervisor for ``task_id`` if it exists.
- L1449 `stop_all(self)` (method) — Stop every running supervisor. For shutdown / test teardown.
