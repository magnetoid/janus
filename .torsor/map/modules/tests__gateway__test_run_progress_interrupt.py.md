---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_run_progress_interrupt.py

Symbols in `tests/gateway/test_run_progress_interrupt.py`.

- L24 `ProgressCaptureAdapter` (class)
- L25 `__init__(self, platform=Platform.TELEGRAM)` (method)
- L31 `connect(self)` (method)
- L34 `disconnect(self)` (method)
- L37 `send(self, chat_id, content, reply_to=None, metadata=None)` (method)
- L41 `edit_message(self, chat_id, message_id, content)` (method)
- L45 `send_typing(self, chat_id, metadata=None)` (method)
- L48 `stop_typing(self, chat_id)` (method)
- L51 `get_chat_info(self, chat_id: str)` (method)
- L55 `PreInterruptAgent` (class) — Fires tool-progress events BEFORE the interrupt lands.
- L63 `__init__(self, **kwargs)` (method)
- L69 `is_interrupted(self)` (method)
- L72 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L78 `InterruptedAgent` (class) — Fires tool.started events AFTER interrupt — all should be suppressed.
- L86 `__init__(self, **kwargs)` (method)
- L94 `is_interrupted(self)` (method)
- L97 `run_conversation(self, message, conversation_history=None, task_id=None)` (method)
- L109 `_make_runner(adapter)` (function)
- L133 `_run_once(monkeypatch, tmp_path, agent_cls, session_id)` (function)
- L171 `test_baseline_non_interrupted_agent_renders_progress(monkeypatch, tmp_path)` (function) — Sanity check: when is_interrupted is False, tool-progress renders normally.
- L185 `test_progress_suppressed_when_agent_is_interrupted(monkeypatch, tmp_path)` (function) — Post-interrupt tool.started events must not render as bubbles.
