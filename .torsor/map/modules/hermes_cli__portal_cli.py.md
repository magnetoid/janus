---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/portal_cli.py

Symbols in `hermes_cli/portal_cli.py`.

- L34 `_cmd_status(args)` (function) — Show Portal auth + Tool Gateway routing summary.
- L106 `_cmd_open(args)` (function) — Open the Portal subscription page in the default browser.
- L121 `_cmd_tools(args)` (function) — List the Tool Gateway catalog + current routing.
- L170 `_cmd_login(args)` (function) — Run the one-shot Nous Portal onboarding (login + model + provider + tools).
- L191 `portal_command(args)` (function) — Top-level dispatch for `hermes portal <subcommand>`.
- L211 `add_parser(subparsers)` (function) — Register `hermes portal` on the given argparse subparsers object.
