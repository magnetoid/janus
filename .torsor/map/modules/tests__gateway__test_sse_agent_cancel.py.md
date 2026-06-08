---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_sse_agent_cancel.py

Symbols in `tests/gateway/test_sse_agent_cancel.py`.

- L19 `_make_adapter()` (function) — Build a minimal APIServerAdapter with mocked internals.
- L29 `_make_request()` (function) — Build a mock aiohttp request.
- L40 `TestSSEAgentCancelOnDisconnect` (class) — gateway/platforms/api_server.py — _write_sse_chat_completion()
- L43 `test_agent_task_cancelled_on_client_disconnect(self)` (method) — When response.write raises ConnectionResetError (client dropped),
- L93 `test_agent_task_not_cancelled_on_normal_completion(self)` (method) — On normal stream completion, agent task should NOT be cancelled.
- L127 `test_broken_pipe_also_cancels_agent(self)` (method) — BrokenPipeError (another disconnect variant) also cancels the task.
- L157 `test_already_done_task_not_cancelled_on_disconnect(self)` (method) — If agent already finished before disconnect, don't try to cancel.
- L198 `test_agent_interrupt_called_on_disconnect(self)` (method) — When the client disconnects, agent.interrupt() must be called
- L248 `test_agent_ref_none_still_cancels_task(self)` (method) — When agent_ref is not provided (None), the task is still cancelled
