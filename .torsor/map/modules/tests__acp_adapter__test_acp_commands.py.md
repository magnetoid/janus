---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/acp_adapter/test_acp_commands.py

Symbols in `tests/acp_adapter/test_acp_commands.py`.

- L11 `FakeAgent` (class)
- L12 `__init__(self)` (method)
- L22 `steer(self, text)` (method)
- L26 `run_conversation(self, *, user_message, conversation_history, task_id, **kwargs)` (method)
- L35 `CaptureConn` (class)
- L36 `__init__(self)` (method)
- L39 `session_update(self, *args, **kwargs)` (method)
- L45 `request_permission(self, *args, **kwargs)` (method)
- L49 `NoopDb` (class)
- L50 `get_session(self, *_args, **_kwargs)` (method)
- L53 `create_session(self, *_args, **_kwargs)` (method)
- L56 `update_session(self, *_args, **_kwargs)` (method)
- L60 `make_agent_and_state()` (function)
- L70 `test_acp_real_agent_gets_session_db_for_recall(monkeypatch)` (function) — ACP sessions persist to SessionDB; recall must receive the same DB handle.
- L118 `test_acp_steer_slash_command_injects_into_running_agent()` (function)
- L133 `test_acp_steer_after_zed_interrupt_replays_interrupted_prompt_with_guidance()` (function)
- L151 `test_acp_steer_on_idle_session_runs_as_regular_prompt()` (function)
- L171 `test_acp_queue_slash_command_adds_next_turn_without_running_now()` (function)
- L185 `test_acp_prompt_drains_queued_turns_after_current_run()` (function)
