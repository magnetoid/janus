---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/fallback_cmd.py

Symbols in `hermes_cli/fallback_cmd.py`.

- L31 `_read_chain(config: Dict[str, Any])` (function) — Return the normalized fallback chain as a list of dicts.
- L42 `_write_chain(config: Dict[str, Any], chain: List[Dict[str, Any]])` (function) — Persist the chain to ``fallback_providers`` and clear legacy key.
- L50 `_format_entry(entry: Dict[str, Any])` (function) — One-line human-readable rendering of a fallback entry.
- L59 `_extract_fallback_from_model_cfg(model_cfg: Any)` (function) — Pull the ``{provider, model, base_url?, api_mode?}`` dict from a ``config["model"]`` snapshot.
- L78 `_snapshot_auth_active_provider()` (function) — Return the current ``active_provider`` in auth.json, or a sentinel if unavailable.
- L88 `_restore_auth_active_provider(value: Any)` (function) — Write back a previously snapshotted ``active_provider`` value.
- L107 `cmd_fallback_list(args)` (function) — Print the current fallback chain.
- L135 `_describe_primary(config: Dict[str, Any])` (function) — One-line description of the primary model for display purposes.
- L147 `cmd_fallback_add(args)` (function) — Launch the same picker as `hermes model`, then append the selection to the chain.
- L227 `_restore_model_cfg(model_before: Any)` (function) — Restore ``config["model"]`` to a previously-captured snapshot.
- L239 `cmd_fallback_remove(args)` (function) — Pick an entry from the chain and remove it.
- L279 `cmd_fallback_clear(args)` (function) — Remove all fallback entries (with confirmation).
- L314 `_numbered_pick(question: str, choices: List[str])` (function) — Fallback numbered-list picker when curses is unavailable.
- L340 `cmd_fallback(args)` (function) — Top-level dispatcher for ``hermes fallback [subcommand]``.
