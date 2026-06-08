---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/auth_commands.py

Symbols in `hermes_cli/auth_commands.py`.

- L39 `_get_custom_provider_names()` (function) — Return list of (display_name, pool_key, provider_key) tuples.
- L60 `_resolve_custom_provider_input(raw: str)` (function) — If raw input matches a custom_providers entry name (case-insensitive), return its pool key.
- L76 `_normalize_provider(provider: str)` (function)
- L89 `_provider_base_url(provider: str)` (function)
- L103 `_oauth_default_label(provider: str, count: int)` (function)
- L107 `_api_key_default_label(count: int)` (function)
- L111 `_display_source(source: str)` (function)
- L115 `_classify_exhausted_status(entry)` (function)
- L134 `_format_exhausted_status(entry)` (function)
- L163 `auth_add_command(args)` (function)
- L416 `auth_list_command(args)` (function)
- L443 `auth_remove_command(args)` (function)
- L481 `auth_reset_command(args)` (function)
- L488 `auth_status_command(args)` (function)
- L508 `auth_logout_command(args)` (function)
- L512 `auth_spotify_command(args)` (function)
- L526 `_interactive_auth()` (function) — Interactive credential pool management when `hermes auth` is called bare.
- L634 `_pick_provider(prompt: str='Provider')` (function) — Prompt for a provider name with auto-complete hints.
- L651 `_interactive_add()` (function)
- L687 `_interactive_remove()` (function)
- L709 `_interactive_reset()` (function)
- L715 `_interactive_strategy()` (function)
- L757 `auth_command(args)` (function)
