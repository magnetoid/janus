---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_mcp_add_command_dest.py

Symbols in `tests/hermes_cli/test_mcp_add_command_dest.py`.

- L27 `_build_parser()` (function) — Minimal replica of the slice of the hermes parser that exhibits
- L48 `TestMcpAddCommandDest` (class)
- L49 `test_url_invocation_preserves_top_level_command(self)` (method) — `hermes mcp add foo --url ...` must keep args.command == "mcp".
- L66 `test_command_flag_writes_to_mcp_command_dest(self)` (method) — `--command npx` must populate args.mcp_command, not args.command.
- L76 `test_bare_mcp_add_does_not_clobber_command(self)` (method) — Even without --url or --command, args.command stays "mcp".
