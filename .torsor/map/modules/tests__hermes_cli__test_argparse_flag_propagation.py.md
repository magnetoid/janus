---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_argparse_flag_propagation.py

Symbols in `tests/hermes_cli/test_argparse_flag_propagation.py`.

- L21 `_build_parser()` (function) — Build the hermes argument parser from the real code.
- L59 `TestChatVerboseArg` (class) — Verify chat --verbose preserves config fallback when absent.
- L62 `test_chat_without_verbose_leaves_attribute_unset(self)` (method)
- L70 `test_chat_verbose_sets_attribute_true(self)` (method)
- L78 `test_cmd_chat_forwards_none_when_verbose_is_absent(self, monkeypatch)` (method)
- L112 `TestYoloEnvVar` (class) — Verify --yolo sets HERMES_YOLO_MODE regardless of flag position.
- L119 `_clean_env(self)` (method)
- L124 `_simulate_cmd_chat_yolo_check(self, args)` (method) — Replicate the exact check from cmd_chat in main.py.
- L129 `test_yolo_before_chat_sets_env(self)` (method)
- L135 `test_yolo_after_chat_sets_env(self)` (method)
- L141 `test_no_yolo_no_env(self)` (method)
- L148 `TestAcceptHooksOnAgentSubparsers` (class) — Verify --accept-hooks is accepted at every agent-subcommand
- L169 `test_accepted_at_every_position(self, argv)` (method) — Invoking `hermes <argv>` must exit 0 (help) rather than
