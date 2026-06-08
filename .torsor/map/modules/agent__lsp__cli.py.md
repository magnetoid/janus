---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/lsp/cli.py

Symbols in `agent/lsp/cli.py`.

- L21 `register_subparser(subparsers: argparse._SubParsersAction)` (function) — Wire the ``hermes lsp`` subcommand tree into the main argparse.
- L69 `run_lsp_command(args: argparse.Namespace)` (function) — Top-level dispatcher for ``hermes lsp <subcommand>``.
- L91 `_cmd_status(emit_json: bool)` (function)
- L176 `_cmd_list(installed_only: bool)` (function)
- L191 `_cmd_install(server_id: str)` (function)
- L215 `_cmd_install_all(include_manual: bool)` (function)
- L241 `_cmd_restart()` (function)
- L249 `_cmd_which(server_id: str)` (function)
- L262 `_recipe_pkg_for(server_id: str)` (function) — Map a registry ``server_id`` to its install-recipe package key.
- L277 `_backend_warnings()` (function) — Return human-readable notes about LSP backend tools that are missing
