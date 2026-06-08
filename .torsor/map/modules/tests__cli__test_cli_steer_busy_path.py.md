---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_cli_steer_busy_path.py

Symbols in `tests/cli/test_cli_steer_busy_path.py`.

- L29 `_make_cli()` (function) — Create a HermesCLI instance with prompt_toolkit stubbed out.
- L71 `TestSteerInlineDetector` (class) — _should_handle_steer_command_inline gates the busy-path fast dispatch.
- L74 `test_detects_steer_when_agent_running(self)` (method)
- L79 `test_ignores_steer_when_agent_idle(self)` (method) — Idle-path /steer should fall through to the normal process_loop
- L86 `test_ignores_non_slash_input(self)` (method)
- L92 `test_ignores_other_slash_commands(self)` (method)
- L99 `test_ignores_steer_with_attached_images(self)` (method) — Image payloads take the normal path; steer doesn't accept images.
- L106 `TestSteerBusyPathDispatch` (class) — When the detector fires, process_command('/steer ...') must call
- L110 `test_process_command_routes_to_agent_steer(self)` (method) — With _agent_running=True and agent.steer present, /steer reaches
- L125 `test_idle_path_queues_as_next_turn(self)` (method) — Control — when the agent is NOT running, /steer correctly falls
