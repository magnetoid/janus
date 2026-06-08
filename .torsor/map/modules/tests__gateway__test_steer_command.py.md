---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/gateway/test_steer_command.py

Symbols in `tests/gateway/test_steer_command.py`.

- L26 `_make_source()` (function)
- L36 `_make_event(text: str)` (function)
- L44 `_make_runner(session_entry: SessionEntry)` (function)
- L80 `_session_entry()` (function)
- L93 `test_steer_calls_agent_steer_and_does_not_interrupt()` (function) — When an agent is running, /steer must call agent.steer(text) and
- L119 `test_steer_without_payload_returns_usage()` (function)
- L134 `test_steer_with_pending_sentinel_falls_back_to_queue()` (function) — When the agent hasn't finished booting (sentinel), /steer should
- L153 `test_steer_agent_without_steer_method_falls_back()` (function) — If the running agent somehow lacks the steer() method (older build,
- L174 `test_steer_rejected_payload_returns_rejection_message()` (function) — If agent.steer() returns False (e.g. empty after strip — though
