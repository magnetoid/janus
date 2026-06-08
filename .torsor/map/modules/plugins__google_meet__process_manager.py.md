---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/process_manager.py

Symbols in `plugins/google_meet/process_manager.py`.

- L39 `_root()` (function)
- L43 `_active_file()` (function)
- L47 `_read_active()` (function)
- L57 `_write_active(data: Dict[str, Any])` (function)
- L65 `_clear_active()` (function)
- L72 `_pid_alive(pid: int)` (function)
- L84 `start(url: str, *, out_dir: Optional[Path]=None, headed: bool=False, auth_state: Optional[str]=None, guest_name: str='Hermes Agent', duration: Optional[str]=None, session_id: Optional[str]=None, mode: str='transcribe', realtime_model: Optional[str]=None, realtime_voice: Optional[str]=None, realtime_instructions: Optional[str]=None, realtime_api_key: Optional[str]=None)` (function) — Spawn the meet_bot subprocess for *url*.
- L190 `status()` (function) — Return the current meeting state, or ``{"ok": False, "reason": ...}``.
- L219 `transcript(last: Optional[int]=None)` (function) — Read the current transcript file. Returns ok=False if none exists.
- L246 `enqueue_say(text: str)` (function) — Append a ``say`` request to the active bot's JSONL queue.
- L288 `stop(*, reason: str='requested')` (function) — Signal the active bot to leave cleanly, then clear the active pointer.
