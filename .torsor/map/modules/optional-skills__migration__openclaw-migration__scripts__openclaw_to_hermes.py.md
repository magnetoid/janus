---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py

Symbols in `optional-skills/migration/openclaw-migration/scripts/openclaw_to_hermes.py`.

- L246 `ItemResult` (class)
- L256 `parse_selection_values(values: Optional[Sequence[str]])` (function)
- L266 `resolve_selected_options(include: Optional[Sequence[str]]=None, exclude: Optional[Sequence[str]]=None, preset: Optional[str]=None)` (function)
- L306 `sha256_file(path: Path)` (function)
- L314 `read_text(path: Path)` (function)
- L318 `normalize_text(text: str)` (function)
- L322 `ensure_parent(path: Path)` (function)
- L326 `resolve_secret_input(value: Any, env: Optional[Dict[str, str]]=None)` (function) — Resolve an OpenClaw SecretInput value to a plain string.
- L349 `load_yaml_file(path: Path)` (function)
- L356 `dump_yaml_file(path: Path, data: Dict[str, Any])` (function)
- L366 `parse_env_file(path: Path)` (function)
- L379 `save_env_file(path: Path, data: Dict[str, str])` (function)
- L385 `backup_existing(path: Path, backup_root: Path)` (function)
- L413 `_case_preserving_replacement(replacement: str)` (function) — Return a re.sub replacement fn that lowercases the result when the
- L430 `rebrand_text(text: str)` (function) — Replace OpenClaw / ClawdBot / MoltBot brand names with Hermes.
- L441 `parse_existing_memory_entries(path: Path)` (function)
- L452 `extract_markdown_entries(text: str)` (function)
- L528 `merge_entries(existing: Sequence[str], incoming: Sequence[str], limit: int)` (function)
- L562 `relative_label(path: Path, root: Path)` (function)
- L605 `_normalize_secret_key(key: str)` (function)
- L609 `_is_secret_key(key: str)` (function)
- L618 `_redact_string(value: str)` (function)
- L624 `redact_migration_value(value: Any)` (function) — Return a deep copy of ``value`` with secret-looking content replaced.
- L635 `_redact_internal(value: Any, seen: set)` (function)
- L655 `write_report(output_dir: Path, report: Dict[str, Any])` (function)
- L711 `Migrator` (class)
- L712 `__init__(self, source_root: Path, target_root: Path, execute: bool, workspace_target: Optional[Path], overwrite: bool, migrate_secrets: bool, output_dir: Optional[Path], selected_options: Optional[set[str]]=None, preset_name: str='', skill_conflict_mode: str='skip')` (method)
- L781 `is_selected(self, option_id: str)` (method)
- L810 `record(self, kind: str, source: Optional[Path], destination: Optional[Path], status: str, reason: str='', **details: Any)` (method)
- L839 `source_candidate(self, *relative_paths: str)` (method)
- L876 `resolve_skill_destination(self, destination: Path)` (method)
- L888 `migrate(self)` (method)
- L962 `run_if_selected(self, option_id: str, func)` (method)
- L988 `build_report(self)` (method)
- L1033 `_build_warnings(self, summary: Dict[str, int])` (method) — Structured warnings surfaced on the report for downstream consumers.
- L1069 `_build_next_steps(self, summary: Dict[str, int])` (method) — Human-readable next-step guidance baked into the report.
- L1094 `maybe_backup(self, path: Path)` (method)
- L1099 `write_overflow_entries(self, kind: str, entries: Sequence[str])` (method)
- L1108 `copy_file(self, source: Path, destination: Path, kind: str, transform: Optional[Any]=None)` (method)
- L1135 `migrate_soul(self)` (method)
- L1142 `migrate_workspace_agents(self)` (method)
- L1156 `migrate_memory(self, source: Optional[Path], destination: Path, limit: int, kind: str)` (method)
- L1200 `migrate_command_allowlist(self)` (method)
- L1259 `load_openclaw_config(self)` (method)
- L1271 `load_openclaw_env(self)` (method) — Load the OpenClaw .env file for secrets that live there instead of config.
- L1275 `merge_env_values(self, additions: Dict[str, str], kind: str, source: Path)` (method)
- L1321 `migrate_messaging_settings(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1361 `handle_secret_settings(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1387 `migrate_secret_settings(self, config: Dict[str, Any])` (method)
- L1407 `_resolve_channel_secret(self, value: Any)` (method) — Resolve a channel config value that may be a SecretRef.
- L1412 `_get_channel_field(ch_cfg: Dict[str, Any], field: str)` (method) — Get a field from channel config, checking both flat and accounts.default layout.
- L1424 `migrate_discord_settings(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1442 `migrate_slack_settings(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1463 `migrate_whatsapp_settings(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1478 `migrate_signal_settings(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1499 `handle_provider_keys(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1514 `migrate_provider_keys(self, config: Dict[str, Any])` (method)
- L1653 `migrate_model_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1722 `migrate_tts_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L1822 `migrate_shared_skills(self)` (method)
- L1839 `_import_skill_directory(self, source_root: Path, kind_label: str, desc: str)` (method) — Import skills from a single source directory into openclaw-imports.
- L1890 `migrate_daily_memory(self)` (method)
- L1946 `migrate_skills(self)` (method)
- L2000 `copy_tree_non_destructive(self, source_root: Optional[Path], destination_root: Path, kind: str, ignore_dir_names: Optional[set[str]]=None)` (method)
- L2053 `archive_docs(self)` (method)
- L2090 `archive_path(self, source: Path, reason: str)` (method)
- L2103 `migrate_mcp_servers(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2179 `migrate_plugins_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2217 `migrate_cron_jobs(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2249 `migrate_hooks_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2279 `migrate_agent_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2398 `migrate_gateway_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2419 `migrate_session_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2482 `migrate_full_providers(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2556 `migrate_deep_channels(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2644 `migrate_browser_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2684 `migrate_tools_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2728 `migrate_approvals_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2761 `migrate_memory_backend(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2776 `migrate_skills_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2792 `migrate_ui_identity(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2807 `migrate_logging_config(self, config: Optional[Dict[str, Any]]=None)` (method)
- L2828 `_set_env_var(self, key: str, value: str, source_label: str)` (method)
- L2841 `generate_migration_notes(self)` (method)
- L2960 `parse_args()` (function)
- L3011 `main()` (function)
