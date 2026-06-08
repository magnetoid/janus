---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/realtime/openai_client.py

Symbols in `plugins/google_meet/realtime/openai_client.py`.

- L27 `_require_websockets()` (function) — Import ``websockets.sync.client.connect`` or raise with hint.
- L39 `RealtimeSession` (class) — Minimal sync client for the OpenAI Realtime WebSocket API.
- L52 `__init__(self, api_key: str, model: str='gpt-realtime', voice: str='alloy', instructions: str='', audio_sink_path: Optional[Path]=None, sample_rate: int=24000)` (method)
- L77 `connect(self)` (method) — Open WS and send session.update with voice+instructions.
- L106 `close(self)` (method)
- L116 `speak(self, text: str, timeout: float=30.0)` (method) — Send ``text`` and accumulate the audio response.
- L207 `cancel_response(self)` (method) — Interrupt the in-flight response (barge-in).
- L223 `_send_json(self, payload: dict)` (method)
- L228 `_recv(self, timeout: Optional[float]=None)` (method)
- L239 `RealtimeSpeaker` (class) — File-based JSONL queue wrapper around :class:`RealtimeSession`.
- L249 `__init__(self, session: RealtimeSession, queue_path: Path, processed_path: Optional[Path]=None)` (method)
- L261 `_read_queue(self)` (method)
- L280 `_rewrite_queue(self, remaining: list[dict])` (method)
- L290 `_append_processed(self, entry: dict, result: dict)` (method)
- L300 `run_until_stopped(self, stop_fn: Callable[[], bool], poll_interval: float=0.5)` (method)
