---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/memory_setup.py

Symbols in `hermes_cli/memory_setup.py`.

- L23 `_curses_select(title: str, items: list[tuple[str, str]], default: int=0)` (function) — Interactive single-select with arrow keys.
- L38 `_prompt(label: str, default: str | None=None, secret: bool=False)` (function) — Prompt for a value with optional default and secret masking.
- L54 `_install_dependencies(provider_name: str)` (function) — Install pip dependencies declared in plugin.yaml.
- L150 `_get_available_providers()` (function) — Discover memory providers from plugins/memory/.
- L190 `cmd_setup_provider(provider_name: str)` (function) — Run memory setup for a specific provider, skipping the picker.
- L226 `cmd_setup(args)` (function) — Interactive memory provider setup wizard.
- L363 `_write_env_vars(env_path: Path, env_writes: dict)` (function) — Append or update env vars in .env file.
- L398 `cmd_status(args)` (function) — Show current memory provider config.
- L460 `memory_command(args)` (function) — Route memory subcommands.
