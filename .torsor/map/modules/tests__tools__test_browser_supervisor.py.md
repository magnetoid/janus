---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_supervisor.py

Symbols in `tests/tools/test_browser_supervisor.py`.

- L34 `_find_chrome()` (function)
- L43 `chrome_cdp(request)` (function) — Start a headless Chrome with --remote-debugging-port, yield its WS URL.
- L132 `_test_page_url()` (function)
- L141 `_fire_on_page(cdp_url: str, expression: str)` (function) — Navigate the first page target to a data URL and fire `expression`.
- L182 `supervisor_registry()` (function) — Yield the global registry and tear down any supervisors after the test.
- L190 `_wait_for_dialog(supervisor, timeout: float=5.0)` (function)
- L200 `test_supervisor_start_and_snapshot(chrome_cdp, supervisor_registry)` (function) — Supervisor attaches, exposes an active snapshot with a top frame.
- L218 `test_main_frame_alert_detection_and_dismiss(chrome_cdp, supervisor_registry)` (function) — alert() in the main frame surfaces and can be dismissed via the sync API.
- L237 `test_iframe_contentwindow_alert(chrome_cdp, supervisor_registry)` (function) — alert() fired from inside a same-origin iframe surfaces too.
- L254 `test_prompt_dialog_with_response_text(chrome_cdp, supervisor_registry)` (function) — prompt() gets our prompt_text back inside the page.
- L274 `test_respond_with_no_pending_dialog_errors_cleanly(chrome_cdp, supervisor_registry)` (function) — Calling respond_to_dialog when nothing is pending returns a clean error, not an exception.
- L284 `test_auto_dismiss_policy(chrome_cdp, supervisor_registry)` (function) — auto_dismiss policy clears dialogs without the agent responding.
- L303 `test_registry_idempotent_get_or_start(chrome_cdp, supervisor_registry)` (function) — Calling get_or_start twice with the same (task, url) returns the same instance.
- L311 `test_registry_stop(chrome_cdp, supervisor_registry)` (function) — stop() tears down the supervisor and snapshot reports inactive.
- L321 `test_browser_dialog_tool_no_supervisor()` (function) — browser_dialog returns a clear error when no supervisor is attached.
- L330 `test_browser_dialog_invalid_action(chrome_cdp, supervisor_registry)` (function) — browser_dialog rejects actions that aren't accept/dismiss.
- L342 `test_recent_dialogs_ring_buffer(chrome_cdp, supervisor_registry)` (function) — Closed dialogs show up in recent_dialogs with a closed_by tag.
- L371 `test_browser_dialog_tool_end_to_end(chrome_cdp, supervisor_registry)` (function) — Full agent-path check: fire an alert, call the tool handler directly.
- L387 `test_browser_cdp_frame_id_routes_via_supervisor(chrome_cdp, supervisor_registry, monkeypatch)` (function) — browser_cdp(frame_id=...) routes Runtime.evaluate through supervisor.
- L431 `test_browser_cdp_frame_id_real_oopif_smoke_documented()` (function) — Document that real-OOPIF E2E was manually verified — see PR #14540.
- L462 `test_browser_cdp_frame_id_missing_supervisor()` (function) — browser_cdp(frame_id=...) errors cleanly when no supervisor is attached.
- L476 `test_browser_cdp_frame_id_not_in_frame_tree(chrome_cdp, supervisor_registry)` (function) — browser_cdp(frame_id=...) errors when the frame_id isn't known.
- L494 `test_bridge_captures_prompt_and_returns_reply_text(chrome_cdp, supervisor_registry)` (function) — End-to-end: agent's prompt_text round-trips INTO the page's JS.
- L594 `test_evaluate_runtime_primitive(chrome_cdp, supervisor_registry)` (function) — evaluate_runtime returns primitive values via the supervisor's live WS.
- L609 `test_evaluate_runtime_object(chrome_cdp, supervisor_registry)` (function) — Plain objects come back JSON-serialized via returnByValue=True.
- L623 `test_evaluate_runtime_js_exception(chrome_cdp, supervisor_registry)` (function) — JS exceptions surface as ok=False with the exception message.
- L636 `test_evaluate_runtime_dom_node_returns_empty_object(chrome_cdp, supervisor_registry)` (function) — DOM nodes with returnByValue=true serialize to ``{}`` (Chrome quirk).
- L658 `test_evaluate_runtime_unserializable_value(chrome_cdp, supervisor_registry)` (function) — ``Infinity``/``NaN``/``BigInt`` come back via ``unserializableValue``.
