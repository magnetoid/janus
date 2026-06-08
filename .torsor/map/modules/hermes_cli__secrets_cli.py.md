---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/secrets_cli.py

Symbols in `hermes_cli/secrets_cli.py`.

- L40 `register_cli(parent_parser: argparse.ArgumentParser)` (function) — Attach the ``bitwarden`` subcommand tree to a parent parser.
- L102 `cmd_setup(args: argparse.Namespace)` (function)
- L291 `cmd_status(args: argparse.Namespace)` (function)
- L340 `cmd_sync(args: argparse.Namespace)` (function)
- L414 `cmd_disable(args: argparse.Namespace)` (function)
- L430 `cmd_install(args: argparse.Namespace)` (function)
- L446 `_yn(b: bool)` (function)
- L450 `_bws_version(binary: Path)` (function)
- L465 `_list_projects(binary: Path, token: str, console: Console, *, server_url: str='')` (function) — Call ``bws project list`` and return the parsed list, or None on failure.
- L524 `_resolve_server_url(args: argparse.Namespace, secrets_cfg: dict, console: Console)` (function) — Pick a Bitwarden server URL for setup.
