---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# gateway/stream_events.py

Symbols in `gateway/stream_events.py`.

- L44 `MessageChunk` (class) — A delta of streamed assistant text.
- L56 `MessageStop` (class) — The current assistant message segment is complete.
- L72 `Commentary` (class) — A complete interim assistant message emitted between tool iterations.
- L85 `ToolCallChunk` (class) — A tool invocation has started (or its in-progress state changed).
- L104 `ToolCallFinished` (class) — A tool invocation completed.
- L122 `LongToolHint` (class) — One-shot onboarding nudge when a tool runs longer than the threshold.
- L135 `GatewayNotice` (class) — A gateway-originated control message (restart, online, long-run notice).
