---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/config.py

Symbols in `hermes_cli/config.py`.

- L41 `_backup_corrupt_config(config_path: Path)` (function) — Preserve a corrupted ``config.yaml`` by copying it to a timestamped ``.bak``.
- L95 `_warn_config_parse_failure(config_path: Path, exc: Exception)` (function) — Surface a config.yaml parse failure to user, log, and stderr.
- L201 `_reject_denylisted_env_var(key: str)` (function) — Raise if ``key`` is in :data:`_ENV_VAR_NAME_DENYLIST`.
- L309 `get_managed_system()` (function) — Return the package manager owning this install, if any.
- L324 `is_managed()` (function) — Check if Hermes is running in package-manager-managed mode.
- L337 `get_managed_update_command()` (function) — Return the preferred upgrade command for a managed install.
- L347 `detect_install_method(project_root: Optional[Path]=None)` (function) — Detect how Hermes was installed: 'docker', 'nixos', 'homebrew', 'git', or 'pip'.
- L387 `stamp_install_method(method: str)` (function) — Write the install method to ~/.hermes/.install_method.
- L397 `is_uv_tool_install()` (function) — Return True when the *running* Hermes lives in a ``uv tool`` layout.
- L425 `recommended_update_command_for_method(method: str)` (function) — Return the update command or guidance for a given install method.
- L443 `recommended_update_command()` (function) — Return the best update command for the current installation.
- L494 `format_docker_update_message()` (function) — Return the user-facing message for ``hermes update`` inside Docker.
- L504 `format_managed_message(action: str='modify this Hermes installation')` (function) — Build a user-facing error for managed installs.
- L532 `managed_error(action: str='modify configuration')` (function) — Print user-friendly error for managed mode.
- L541 `get_container_exec_info()` (function) — Read container mode metadata from HERMES_HOME/.container-mode.
- L594 `get_config_path()` (function) — Get the main config file path.
- L598 `get_env_path()` (function) — Get the .env file path (for API keys).
- L602 `get_project_root()` (function) — Get the project installation directory.
- L606 `_resolve_hermes_uid_gid()` (function) — Read the HERMES_UID / HERMES_GID env vars set by Docker deployments.
- L636 `_chown_to_hermes_uid(path)` (function) — Chown ``path`` to ``HERMES_UID:HERMES_GID`` if those env vars are set.
- L665 `_secure_dir(path)` (function) — Set directory to owner-only access (0700 by default). No-op on Windows.
- L697 `_is_container()` (function) — Detect if we're running inside a Docker/Podman/LXC container.
- L722 `_secure_file(path)` (function) — Set file to owner-only read/write (0600). No-op on Windows.
- L740 `_ensure_default_soul_md(home: Path)` (function) — Seed a default SOUL.md into HERMES_HOME if the user doesn't have one yet.
- L749 `ensure_hermes_home()` (function) — Ensure ~/.hermes directory structure exists with secure permissions.
- L776 `_ensure_hermes_home_managed(home: Path)` (function) — Managed-mode variant: verify dirs exist (activation creates them), seed SOUL.md.
- L3532 `get_missing_env_vars(required_only: bool=False)` (function) — Check which environment variables are missing.
- L3554 `_set_nested(config, dotted_key: str, value)` (function) — Set a value at an arbitrarily nested dotted key path.
- L3605 `get_missing_config_fields()` (function) — Check which config fields are missing or outdated (recursive).
- L3633 `get_missing_skill_config_vars()` (function) — Return skill-declared config vars that are missing or empty in config.yaml.
- L3680 `_normalize_custom_provider_entry(entry: Any, *, provider_key: str='')` (function) — Return a runtime-compatible custom provider entry or ``None``.
- L3812 `_custom_provider_entry_to_provider_config(entry: Any, *, provider_key: str='')` (function) — Translate a legacy custom provider entry to the v12 providers shape.
- L3848 `providers_dict_to_custom_providers(providers_dict: Any)` (function) — Normalize ``providers`` config entries into the legacy custom-provider shape.
- L3862 `get_compatible_custom_providers(config: Optional[Dict[str, Any]]=None)` (function) — Return a deduplicated custom-provider view across legacy and v12+ config.
- L3912 `get_custom_provider_context_length(model: str, base_url: str, custom_providers: Optional[List[Dict[str, Any]]]=None, config: Optional[Dict[str, Any]]=None)` (function) — Look up a per-model ``context_length`` override from ``custom_providers``.
- L3977 `_coerce_config_version(value: Any)` (function) — Return a safe integer config version, treating invalid values as legacy.
- L3988 `check_config_version()` (function) — Check the raw on-disk config schema version.
- L4047 `ConfigIssue` (class) — A detected config structure problem.
- L4055 `validate_config_structure(config: Optional[Dict[str, Any]]=None)` (function) — Validate config.yaml structure and return a list of detected issues.
- L4199 `print_config_warnings(config: Optional[Dict[str, Any]]=None)` (function) — Print config structure warnings to stderr at startup.
- L4221 `warn_deprecated_cwd_env_vars(config: Optional[Dict[str, Any]]=None)` (function) — Warn if MESSAGING_CWD or TERMINAL_CWD is set in .env instead of config.yaml.
- L4266 `migrate_config(interactive: bool=True, quiet: bool=False)` (function) — Migrate config to latest version, prompting for new required fields.
- L4862 `_deep_merge(base: dict, override: dict)` (function) — Recursively merge *override* into *base*, preserving nested defaults.
- L4882 `_expand_env_vars(obj)` (function) — Recursively expand ``${VAR}`` references in config values.
- L4902 `_items_by_unique_name(items)` (function) — Return a name-indexed dict only when all items have unique string names.
- L4917 `_preserve_env_ref_templates(current, raw, loaded_expanded=None)` (function) — Restore raw ``${VAR}`` templates when a value is otherwise unchanged.
- L4981 `_normalize_root_model_keys(config: Dict[str, Any])` (function) — Move stale root-level provider/base_url/context_length into model section.
- L5011 `_normalize_max_turns_config(config: Dict[str, Any])` (function) — Normalize legacy root-level max_turns into agent.max_turns.
- L5027 `cfg_get(cfg: Optional[Dict[str, Any]], *keys: str, default: Any=None)` (function) — Traverse nested dict keys safely, returning ``default`` on any miss.
- L5074 `read_raw_config()` (function) — Read ~/.hermes/config.yaml as-is, without merging defaults or migrating.
- L5112 `load_config()` (function) — Load configuration from ~/.hermes/config.yaml.
- L5129 `load_config_readonly()` (function) — Fast-path variant of ``load_config()`` for callers that ONLY READ.
- L5152 `_load_config_impl(*, want_deepcopy: bool)` (function)
- L5286 `save_config(config: Dict[str, Any])` (function) — Save configuration to ~/.hermes/config.yaml.
- L5330 `load_env()` (function) — Load environment variables from ~/.hermes/.env.
- L5395 `invalidate_env_cache()` (function) — Clear the load_env() process-level memo.
- L5407 `_sanitize_env_lines(lines: list)` (function) — Fix corrupted .env lines before reading or writing.
- L5467 `sanitize_env_file()` (function) — Read, sanitize, and rewrite ~/.hermes/.env in place.
- L5513 `_check_non_ascii_credential(key: str, value: str)` (function) — Warn and strip non-ASCII characters from credential values.
- L5553 `save_env_value(key: str, value: str)` (function) — Save or update a value in ~/.hermes/.env.
- L5625 `remove_env_value(key: str)` (function) — Remove a key from ~/.hermes/.env and os.environ.
- L5682 `save_anthropic_oauth_token(value: str, save_fn=None)` (function) — Persist an Anthropic OAuth/setup token and clear the API-key slot.
- L5689 `use_anthropic_claude_code_credentials(save_fn=None)` (function) — Use Claude Code's own credential files instead of persisting env tokens.
- L5696 `save_anthropic_api_key(value: str, save_fn=None)` (function) — Persist an Anthropic API key and clear the OAuth/setup-token slot.
- L5703 `save_env_value_secure(key: str, value: str)` (function)
- L5713 `reload_env()` (function) — Re-read ~/.hermes/.env into os.environ. Returns count of vars updated.
- L5735 `get_env_value(key: str)` (function) — Get a value from ~/.hermes/.env or environment.
- L5750 `redact_key(key: str)` (function) — Redact an API key for display.
- L5760 `show_config()` (function) — Display current configuration.
- L5941 `edit_config()` (function) — Open config file in user's editor.
- L5981 `set_config_value(key: str, value: str)` (function) — Set a configuration value.
- L6078 `config_command(args)` (function) — Handle config subcommands.
- L6223 `_inject_profile_env_vars()` (function) — Populate OPTIONAL_ENV_VARS from provider profiles not already listed.
- L6280 `_inject_platform_plugin_env_vars()` (function) — Populate OPTIONAL_ENV_VARS from bundled platform plugin manifests.
