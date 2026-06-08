---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/stream_dispatch.py

Symbols in `gateway/stream_dispatch.py`.

- L40 `GatewayEventDispatcher` (class) — Route typed stream events through an adapter onto a delivery sink.
- L67 `__init__(self, adapter: Any, sink: Any=None, *, enqueue_tool_line: Optional[Callable[[Any], None]]=None, tool_mode: str='all', preview_max_len: int=40, on_long_tool: Optional[Callable[[LongToolHint], None]]=None, on_notice: Optional[Callable[[GatewayNotice], None]]=None)` (method)
- L88 `dispatch(self, event: StreamEvent)` (method) — Route a single event.  Never raises into the agent's worker thread.
- L95 `_dispatch(self, event: StreamEvent)` (method)
