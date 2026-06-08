---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/middleware.py

Symbols in `hermes_cli/middleware.py`.

- L38 `RequestMiddlewareResult` (class) — Result of applying request middleware to a mutable payload.
- L47 `observer_payload(**kwargs: Any)` (function)
- L52 `middleware_payload(**kwargs: Any)` (function)
- L58 `_safe_copy(payload: Any)` (function) — Deep-copy a request payload, tolerating non-deepcopyable members.
- L77 `apply_llm_request_middleware(request: Dict[str, Any], **context: Any)` (function) — Apply registered LLM request middleware.
- L120 `apply_tool_request_middleware(tool_name: str, args: Dict[str, Any], **context: Any)` (function) — Apply registered tool request middleware.
- L165 `apply_api_request_middleware(request: Dict[str, Any], **context: Any)` (function) — Compatibility wrapper for older ``api_request`` naming.
- L173 `run_llm_execution_middleware(request: Dict[str, Any], next_call: Callable[[Dict[str, Any]], Any], **context: Any)` (function) — Run provider execution through registered LLM execution middleware.
- L192 `run_tool_execution_middleware(tool_name: str, args: Dict[str, Any], next_call: Callable[[Dict[str, Any]], Any], **context: Any)` (function) — Run tool execution through registered tool execution middleware.
- L213 `run_api_execution_middleware(request: Dict[str, Any], next_call: Callable[[Dict[str, Any]], Any], **context: Any)` (function) — Compatibility wrapper for older ``api_execution`` naming.
- L222 `_invoke_middleware(kind: str, **kwargs: Any)` (function)
- L228 `_has_middleware(kind: str)` (function)
- L234 `_get_middleware_callbacks(kind: str)` (function)
- L240 `_run_execution_chain(kind: str, callbacks: List[Callable], terminal_call: Callable[[Any], Any], **kwargs: Any)` (function)
- L305 `_trace_entry(result: Dict[str, Any])` (function)
