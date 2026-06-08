---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/computer_use/tool.py

Symbols in `tools/computer_use/tool.py`.

- L60 `set_approval_callback(cb)` (function) — Register a callback for computer_use approval prompts (used by CLI).
- L93 `_canon_key_combo(keys: str)` (function)
- L110 `_is_blocked_type(text: str)` (function)
- L129 `_get_backend()` (function)
- L145 `reset_backend_for_tests()` (function) — Test helper — tear down the cached backend.
- L159 `_NoopBackend` (class) — Test/CI stub. Records calls; returns trivial results.
- L162 `__init__(self)` (method)
- L166 `start(self)` (method)
- L167 `stop(self)` (method)
- L168 `is_available(self)` (method)
- L170 `capture(self, mode: str='som', app: Optional[str]=None)` (method)
- L175 `click(self, **kw)` (method)
- L179 `drag(self, **kw)` (method)
- L183 `scroll(self, **kw)` (method)
- L187 `type_text(self, text: str)` (method)
- L191 `key(self, keys: str)` (method)
- L195 `list_apps(self)` (method)
- L199 `focus_app(self, app: str, raise_window: bool=False)` (method)
- L203 `set_value(self, value: str, element: Optional[int]=None)` (method)
- L212 `handle_computer_use(args: Dict[str, Any], **kwargs)` (function) — Main entry point — dispatched by tools.registry.
- L264 `_request_approval(action: str, args: Dict[str, Any])` (function) — Return None if approved, or a JSON error string if denied.
- L292 `_summarize_action(action: str, args: Dict[str, Any])` (function)
- L316 `_dispatch(backend: ComputerUseBackend, action: str, args: Dict[str, Any])` (function)
- L414 `_text_response(res: ActionResult)` (function)
- L434 `_coerce_max_elements(value: Any)` (function) — Validate the caller-supplied ``max_elements``.
- L456 `_capture_response(cap: CaptureResult, max_elements: int=_DEFAULT_MAX_ELEMENTS)` (function)
- L543 `_should_route_through_aux_vision()` (function) — Return True when ``_capture_response`` should hand the PNG to aux vision.
- L575 `_route_capture_through_aux_vision(cap: CaptureResult, summary: str)` (function) — Pre-analyse the captured PNG via ``vision_analyze`` and return a text result.
- L674 `_maybe_follow_capture(backend: ComputerUseBackend, res: ActionResult, do_capture: bool)` (function)
- L712 `_format_elements(elements: List[UIElement], max_lines: int=40)` (function)
- L723 `_element_to_dict(e: UIElement)` (function)
- L737 `check_computer_use_requirements()` (function) — Return True iff computer_use can run on this host.
- L748 `get_computer_use_schema()` (function)
