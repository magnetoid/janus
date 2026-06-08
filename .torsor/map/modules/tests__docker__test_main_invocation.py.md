---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/docker/test_main_invocation.py

Symbols in `tests/docker/test_main_invocation.py`.

- L15 `test_no_args_starts_hermes(built_image: str)` (function) — ``docker run <image>`` should start hermes cleanly.
- L32 `test_chat_subcommand_passthrough(built_image: str)` (function) — ``docker run <image> chat --help`` should exec ``hermes chat --help``.
- L46 `test_bare_executable_passthrough(built_image: str)` (function) — ``docker run <image> sleep 1`` should exec ``sleep`` directly.
- L59 `test_bash_pattern(built_image: str)` (function) — ``docker run <image> bash -c 'echo ok'`` should exec bash directly.
- L69 `test_container_exit_code_matches_inner_exit(built_image: str)` (function) — The container exit code must match the inner process's exit code.
