---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# plugins/memory/honcho/cli.py

Symbols in `plugins/memory/honcho/cli.py`.

- L18 `clone_honcho_for_profile(profile_name: str)` (function) — Auto-clone Honcho config for a new profile from the default host block.
- L82 `_ensure_peer_exists(host_key: str | None=None)` (function) — Create the AI peer in Honcho if it doesn't already exist.
- L103 `cmd_enable(args)` (function) — Enable Honcho for the active profile.
- L146 `cmd_disable(args)` (function) — Disable Honcho for the active profile.
- L163 `cmd_sync(args)` (function) — Sync Honcho config to all existing profiles.
- L209 `sync_honcho_profiles_quiet()` (function) — Sync Honcho host blocks for all profiles. Returns count of newly created blocks.
- L241 `_host_key()` (function) — Return the active Honcho host key, derived from the current Hermes profile.
- L250 `_config_path()` (function) — Return the active Honcho config path for reading (instance-local or global).
- L255 `_local_config_path()` (function) — Return the instance-local Honcho config path for writing.
- L265 `_read_config()` (function)
- L275 `_write_config(cfg: dict, path: Path | None=None)` (function)
- L282 `_resolve_api_key(cfg: dict)` (function) — Resolve API key with host -> root -> env fallback.
- L325 `_resolve_effective_identity_mapping(cfg: dict, hermes_host: dict)` (function) — Resolve the effective identity-mapping state for the active host.
- L371 `_scrub_identity_mapping(hermes_host: dict)` (function) — Drop every peer-mapping key from the host block.
- L383 `_prompt(label: str, default: str | None=None, secret: bool=False)` (function)
- L399 `_ensure_sdk_installed()` (function) — Check honcho-ai is importable; offer to install if not. Returns True if ready.
- L429 `cmd_setup(args)` (function) — Interactive Honcho setup wizard.
- L822 `_active_profile_name()` (function) — Return the active Hermes profile name (respects --target-profile override).
- L833 `_all_profile_host_configs()` (function) — Return (profile_name, host_key, host_block) for every known profile.
- L861 `cmd_status(args)` (function) — Show current Honcho config and connection status.
- L956 `_show_peer_cards(hcfg, client)` (function) — Fetch and display peer cards for the active profile.
- L995 `_cmd_status_all()` (function) — Show Honcho config overview across all profiles.
- L1021 `cmd_peers(args)` (function) — Show peer identities across all profiles.
- L1038 `cmd_sessions(args)` (function) — List known directory → session name mappings.
- L1057 `cmd_map(args)` (function) — Map current directory to a Honcho session name.
- L1082 `cmd_peer(args)` (function) — Show or update peer names and dialectic reasoning level.
- L1138 `cmd_mode(args)` (function) — Show or set the recall mode.
- L1172 `cmd_strategy(args)` (function) — Show or set the session strategy.
- L1207 `cmd_tokens(args)` (function) — Show or set token budget settings.
- L1251 `cmd_identity(args)` (function) — Seed AI peer identity or show both peer representations.
- L1325 `cmd_migrate(args)` (function) — Step-by-step migration guide: OpenClaw native memory → Hermes + Honcho.
- L1554 `honcho_command(args)` (function) — Route honcho subcommands.
- L1600 `register_cli(subparser)` (function) — Build the ``hermes honcho`` argparse subcommand tree.
