---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/google_meet/cli.py

Symbols in `plugins/google_meet/cli.py`.

- L26 `_auth_state_path()` (function)
- L34 `register_cli(subparser: argparse.ArgumentParser)` (function) — Build the ``hermes meet`` argparse tree.
- L107 `meet_command(args: argparse.Namespace)` (function)
- L154 `_cmd_setup()` (function)
- L214 `_cmd_install(*, realtime: bool, assume_yes: bool)` (function) — Install the plugin's prerequisites.
- L336 `_cmd_auth()` (function) — Open a headed Chromium, let the user sign in, save storage_state.
- L371 `_cmd_join(url: str, *, guest_name: str, duration: Optional[str], headed: bool, mode: str='transcribe', node: Optional[str]=None)` (function)
- L421 `_cmd_say(text: str, node: Optional[str]=None)` (function)
- L451 `_cmd_status()` (function)
- L457 `_cmd_transcript(last: Optional[int])` (function)
- L467 `_cmd_stop()` (function)
