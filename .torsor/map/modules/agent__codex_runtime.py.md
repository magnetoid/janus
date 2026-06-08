---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/codex_runtime.py

Symbols in `agent/codex_runtime.py`.

- L28 `run_codex_app_server_turn(agent, *, user_message: str, original_user_message: Any, messages: List[Dict[str, Any]], effective_task_id: str, should_review_memory: bool=False)` (function) — Codex app-server runtime path. Hands the entire turn to a `codex
- L206 `_event_field(event: Any, name: str, default: Any=None)` (function) — Field access that handles both attr-style (SDK objects) and dict (raw JSON) events.
- L214 `_raise_stream_error(event: Any)` (function) — Raise a ``_StreamErrorEvent`` from a ``type=error`` SSE frame.
- L229 `_consume_codex_event_stream(event_iter: Any, *, model: str, on_text_delta=None, on_reasoning_delta=None, on_first_delta=None, on_event=None, interrupt_check=None)` (function) — Consume a Codex Responses SSE event stream and return a final response.
- L422 `run_codex_stream(agent, api_kwargs: dict, client: Any=None, on_first_delta=None)` (function) — Execute one streaming Responses API request and return the final response.
- L518 `run_codex_create_stream_fallback(agent, api_kwargs: dict, client: Any=None)` (function) — Backward-compatible alias for the unified event-driven path.
