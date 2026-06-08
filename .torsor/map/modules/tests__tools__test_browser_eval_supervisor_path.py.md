---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_browser_eval_supervisor_path.py

Symbols in `tests/tools/test_browser_eval_supervisor_path.py`.

- L22 `_disable_camofox(monkeypatch)` (function) — Force the non-camofox path so our supervisor branch is reached.
- L30 `_patch_supervisor(monkeypatch, supervisor)` (function) — Wire SUPERVISOR_REGISTRY.get to return ``supervisor`` for any task_id.
- L40 `TestBrowserEvalSupervisorPath` (class) — The supervisor fast path replaces the agent-browser subprocess hop.
- L43 `test_primitive_result_routes_through_supervisor(self, monkeypatch)` (method)
- L65 `test_json_string_result_is_parsed(self, monkeypatch)` (method) — Match agent-browser semantics: JSON-string results get parsed.
- L87 `test_non_json_string_result_kept_as_string(self, monkeypatch)` (method)
- L103 `test_js_exception_surfaces_without_subprocess_fallthrough(self, monkeypatch)` (method) — A JS-side error must NOT trigger a (slow + redundant) subprocess retry.
- L127 `test_supervisor_loop_down_falls_through_to_subprocess(self, monkeypatch)` (method) — When the supervisor itself is unavailable, fall back to the subprocess.
- L154 `test_no_active_supervisor_falls_through_to_subprocess(self, monkeypatch)` (method) — When SUPERVISOR_REGISTRY.get returns None, subprocess path runs.
- L172 `test_supervisor_no_session_falls_through(self, monkeypatch)` (method) — A supervisor without an attached page session must fall through cleanly.
- L192 `test_subprocess_reference_chain_error_becomes_guidance(self, monkeypatch)` (method) — The CLI subprocess can't retry with returnByValue=False, so the
- L224 `_make_supervisor_with_cdp(cdp_response)` (function) — Build a CDPSupervisor instance that mocks ``_cdp`` to return ``cdp_response``.
- L260 `_stop_supervisor(sup)` (function)
- L265 `TestEvaluateRuntimeResponseShaping` (class) — CDPSupervisor.evaluate_runtime decodes the Runtime.evaluate response correctly.
- L268 `test_primitive_value(self)` (method)
- L279 `test_object_value_returned_by_value(self)` (method)
- L297 `test_undefined_value(self)` (method)
- L308 `test_dom_node_returns_description(self)` (method) — Non-serializable values (DOM nodes, functions) come back as description strings.
- L329 `test_js_exception_returns_error(self)` (method)
- L349 `test_inactive_supervisor_returns_error_without_dispatch(self)` (method) — Inactive supervisor short-circuits before even touching the loop.
- L366 `test_no_session_attached_returns_error(self)` (method)
- L392 `_make_supervisor_with_cdp_fn(cdp_fn)` (function) — Like ``_make_supervisor_with_cdp`` but lets the test supply a coroutine
- L421 `TestEvaluateRuntimeDomNodeCrashRetry` (class) — returnByValue=True on a DOM node fails CDP serialization with 'Object
- L427 `test_reference_chain_crash_retries_without_by_value(self)` (method)
- L462 `test_unrelated_error_does_not_retry(self)` (method)
