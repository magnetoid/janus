---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_stream_events.py

Symbols in `tests/gateway/test_stream_events.py`.

- L26 `_base_adapter()` (function) — A real BasePlatformAdapter instance (abstractmethods cleared) so we
- L36 `_FakeSink` (class)
- L37 `__init__(self)` (method)
- L42 `on_delta(self, text)` (method)
- L45 `on_commentary(self, text)` (method)
- L48 `on_segment_break(self)` (method)
- L54 `test_message_chunk_flows_to_sink_on_delta()` (function)
- L62 `test_intermediate_message_stop_breaks_segment_but_final_does_not()` (function)
- L70 `test_commentary_flows_to_sink()` (function)
- L77 `test_message_events_dropped_when_no_sink()` (function)
- L85 `test_tool_call_chunk_renders_default_chrome()` (function)
- L97 `test_tool_preview_truncated_to_cap()` (function)
- L109 `test_new_mode_dedups_same_tool()` (function)
- L121 `test_off_mode_emits_nothing()` (function)
- L131 `test_adapter_can_eat_tool_chrome()` (function) — An adapter that returns None from format_tool_event drops the event —
- L144 `test_tool_finished_emits_no_chrome()` (function)
- L156 `test_long_tool_hint_routes_to_hook()` (function)
- L166 `test_gateway_notice_routes_to_hook()` (function)
- L175 `test_dispatch_swallows_render_errors()` (function) — A render error must never propagate into the agent worker thread.
