---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/send_cmd.py

Symbols in `hermes_cli/send_cmd.py`.

- L41 `_read_message_body(positional: Optional[str], file_path: Optional[str])` (function) — Resolve the message body from (in order):
- L77 `_resolve_target(arg_to: Optional[str])` (function) — Return a cleaned ``--to`` value, or ``None`` when nothing is set.
- L84 `_emit_result(result_json: str, *, json_mode: bool, quiet: bool)` (function) — Print the tool result in the requested format and return the exit code.
- L129 `_list_targets(platform_filter: Optional[str], *, json_mode: bool)` (function) — Print the channel directory (all configured targets across platforms).
- L198 `_load_hermes_env()` (function) — Populate ``os.environ`` from ``~/.hermes/.env`` AND bridge top-level
- L277 `cmd_send(args: argparse.Namespace)` (function) — Entry point wired into the top-level argparse dispatcher.
- L347 `register_send_subparser(subparsers)` (function) — Create the ``send`` subparser and return it.
