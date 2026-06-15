from typing import Any, Dict, List, Optional, Set, Tuple
from dataclasses import dataclass
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class ConfigIssue:
    """A detected config structure problem."""

    severity: str  # "error", "warning"
    message: str
    hint: str


def validate_config_structure(config: Optional[Dict[str, Any]] = None) -> List["ConfigIssue"]:
    """Validate config.yaml structure and return a list of detected issues.

    Catches common YAML formatting mistakes that produce confusing runtime
    errors (like "Unknown provider") instead of clear diagnostics.

    Can be called with a pre-loaded config dict, or will load from disk.
    """
    if config is None:
        try:
            config = load_config()
        except Exception:
            return [ConfigIssue("error", "Could not load config.yaml", "Run 'janus setup' to create a valid config")]

    issues: List[ConfigIssue] = []

    # ── custom_providers must be a list, not a dict ──────────────────────
    cp = config.get("custom_providers")
    if cp is not None:
        if isinstance(cp, dict):
            issues.append(ConfigIssue(
                "error",
                "custom_providers is a dict — it must be a YAML list (items prefixed with '-')",
                "Change to:\n"
                "  custom_providers:\n"
                "    - name: my-provider\n"
                "      base_url: https://...\n"
                "      api_key: ...",
            ))
            # Check if dict keys look like they should be list-entry fields
            cp_keys = set(cp.keys()) if isinstance(cp, dict) else set()
            suspicious = cp_keys & _CUSTOM_PROVIDER_LIKE_FIELDS
            if suspicious:
                issues.append(ConfigIssue(
                    "warning",
                    f"Root-level keys {sorted(suspicious)} look like custom_providers entry fields",
                    "These should be indented under a '- name: ...' list entry, not at root level",
                ))
        elif isinstance(cp, list):
            # Validate each entry in the list
            for i, entry in enumerate(cp):
                if not isinstance(entry, dict):
                    issues.append(ConfigIssue(
                        "warning",
                        f"custom_providers[{i}] is not a dict (got {type(entry).__name__})",
                        "Each entry should have at minimum: name, base_url",
                    ))
                    continue
                if not entry.get("name"):
                    issues.append(ConfigIssue(
                        "warning",
                        f"custom_providers[{i}] is missing 'name' field",
                        "Add a name, e.g.: name: my-provider",
                    ))
                if not entry.get("base_url"):
                    issues.append(ConfigIssue(
                        "warning",
                        f"custom_providers[{i}] is missing 'base_url' field",
                        "Add the API endpoint URL, e.g.: base_url: https://api.example.com/v1",
                    ))

    # ── fallback_model: single dict OR list of dicts (chain) ─────────────
    fb = config.get("fallback_model")
    if fb is not None:
        if isinstance(fb, list):
            # Chain fallback — validate each entry
            for i, entry in enumerate(fb):
                if not isinstance(entry, dict):
                    issues.append(ConfigIssue(
                        "error",
                        f"fallback_model[{i}] should be a dict, got {type(entry).__name__}",
                        "Each entry needs provider + model",
                    ))
                else:
                    if not entry.get("provider"):
                        issues.append(ConfigIssue(
                            "warning",
                            f"fallback_model[{i}] is missing 'provider' field",
                            "Add: provider: openrouter (or another provider)",
                        ))
                    if not entry.get("model"):
                        issues.append(ConfigIssue(
                            "warning",
                            f"fallback_model[{i}] is missing 'model' field",
                            "Add: model: <model-name>",
                        ))
        elif not isinstance(fb, dict):
            issues.append(ConfigIssue(
                "error",
                f"fallback_model should be a dict with 'provider' and 'model', got {type(fb).__name__}",
                "Change to:\n"
                "  fallback_model:\n"
                "    provider: openrouter\n"
                "    model: anthropic/claude-sonnet-4",
            ))
        elif fb:
            if not fb.get("provider"):
                issues.append(ConfigIssue(
                    "warning",
                    "fallback_model is missing 'provider' field — fallback will be disabled",
                    "Add: provider: openrouter (or another provider)",
                ))
            if not fb.get("model"):
                issues.append(ConfigIssue(
                    "warning",
                    "fallback_model is missing 'model' field — fallback will be disabled",
                    "Add: model: anthropic/claude-sonnet-4 (or another model)",
                ))

    # ── Check for fallback_model accidentally nested inside custom_providers ──
    if isinstance(cp, dict) and "fallback_model" not in config and "fallback_model" in (cp or {}):
        issues.append(ConfigIssue(
            "error",
            "fallback_model appears inside custom_providers instead of at root level",
            "Move fallback_model to the top level of config.yaml (no indentation)",
        ))

    # ── model section: should exist when custom_providers is configured ──
    model_cfg = config.get("model")
    if cp and not model_cfg:
        issues.append(ConfigIssue(
            "warning",
            "custom_providers defined but no 'model' section — Janus won't know which provider to use",
            "Add a model section:\n"
            "  model:\n"
            "    provider: custom\n"
            "    default: your-model-name\n"
            "    base_url: https://...",
        ))

    # ── Root-level keys that look misplaced ──────────────────────────────
    for key in config:
        if key.startswith("_"):
            continue
        if key not in _KNOWN_ROOT_KEYS and key in _CUSTOM_PROVIDER_LIKE_FIELDS:
            issues.append(ConfigIssue(
                "warning",
                f"Root-level key '{key}' looks misplaced — should it be under 'model:' or inside a 'custom_providers' entry?",
                f"Move '{key}' under the appropriate section",
            ))

    return issues


def print_config_warnings(config: Optional[Dict[str, Any]] = None) -> None:
    """Print config structure warnings to stderr at startup.

    Called early in CLI and gateway init so users see problems before
    they hit cryptic "Unknown provider" errors.  Prints nothing if
    config is healthy.
    """
    try:
        issues = validate_config_structure(config)
    except Exception:
        return
    if not issues:
        return

    lines = ["\033[33m⚠ Config issues detected in config.yaml:\033[0m"]
    for ci in issues:
        marker = "\033[31m✗\033[0m" if ci.severity == "error" else "\033[33m⚠\033[0m"
        lines.append(f"  {marker} {ci.message}")
    lines.append("  \033[2mRun 'janus doctor' for fix suggestions.\033[0m")
    sys.stderr.write("\n".join(lines) + "\n\n")


def warn_deprecated_cwd_env_vars(config: Optional[Dict[str, Any]] = None) -> None:
    """Warn if MESSAGING_CWD or TERMINAL_CWD is set in .env instead of config.yaml.

    These env vars are deprecated — the canonical setting is terminal.cwd
    in config.yaml.  Prints a migration hint to stderr.
    """
    messaging_cwd = os.environ.get("MESSAGING_CWD")
    terminal_cwd_env = os.environ.get("TERMINAL_CWD")

    if config is None:
        try:
            config = load_config()
        except Exception:
            return

    terminal_cfg = config.get("terminal", {})
    config_cwd = terminal_cfg.get("cwd", ".") if isinstance(terminal_cfg, dict) else "."
    # Only warn if config.yaml doesn't have an explicit path
    config_has_explicit_cwd = config_cwd not in {".", "auto", "cwd", ""}

    lines: list[str] = []
    if messaging_cwd:
        lines.append(
            f"  \033[33m⚠\033[0m MESSAGING_CWD={messaging_cwd} found in .env — "
            f"this is deprecated."
        )
    if terminal_cwd_env and not config_has_explicit_cwd:
        # TERMINAL_CWD in env but not from config bridge — likely from .env
        lines.append(
            f"  \033[33m⚠\033[0m TERMINAL_CWD={terminal_cwd_env} found in .env — "
            f"this is deprecated."
        )
    if lines:
        hint_path = os.environ.get("JANUS_HOME", "~/.janus")
        lines.insert(0, "\033[33m⚠ Deprecated .env settings detected:\033[0m")
        lines.append(
            f"  \033[2mMove to config.yaml instead:  "
            f"terminal:\\n    cwd: /your/project/path\033[0m"
        )
        lines.append(
            f"  \033[2mThen remove the old entries from {hint_path}/.env\033[0m"
        )
        sys.stderr.write("\n".join(lines) + "\n\n")


def migrate_config(interactive: bool = True, quiet: bool = False) -> Dict[str, Any]:
    """
    Migrate config to latest version, prompting for new required fields.
    
    Args:
        interactive: If True, prompt user for missing values
        quiet: If True, suppress output
        
    Returns:
        Dict with migration results: {"env_added": [...], "config_added": [...], "warnings": [...]}
    """
    results = {"env_added": [], "config_added": [], "warnings": []}

    # ── Always: sanitize .env (split concatenated keys) ──
    try:
        fixes = sanitize_env_file()
        if fixes and not quiet:
            print(f"  ✓ Repaired .env file ({fixes} corrupted entries fixed)")
    except Exception:
        pass  # best-effort; don't block migration on sanitize failure

    # Check config version
    current_ver, latest_ver = check_config_version()
    
    # ── Version 3 → 4: migrate tool progress from .env to config.yaml ──
    if current_ver < 4:
        config = load_config()
        display = config.get("display", {})
        if not isinstance(display, dict):
            display = {}
        if "tool_progress" not in display:
            old_enabled = get_env_value("JANUS_TOOL_PROGRESS")
            old_mode = get_env_value("JANUS_TOOL_PROGRESS_MODE")
            if old_enabled and old_enabled.lower() in {"false", "0", "no"}:
                display["tool_progress"] = "off"
                results["config_added"].append("display.tool_progress=off (from JANUS_TOOL_PROGRESS=false)")
            elif old_mode and old_mode.lower() in {"new", "all"}:
                display["tool_progress"] = old_mode.lower()
                results["config_added"].append(f"display.tool_progress={old_mode.lower()} (from JANUS_TOOL_PROGRESS_MODE)")
            else:
                display["tool_progress"] = "all"
                results["config_added"].append("display.tool_progress=all (default)")
            config["display"] = display
            save_config(config)
            if not quiet:
                print(f"  ✓ Migrated tool progress to config.yaml: {display['tool_progress']}")
    
    # ── Version 4 → 5: add timezone field ──
    if current_ver < 5:
        config = load_config()
        if "timezone" not in config:
            old_tz = os.getenv("JANUS_TIMEZONE", "")
            if old_tz and old_tz.strip():
                config["timezone"] = old_tz.strip()
                results["config_added"].append(f"timezone={old_tz.strip()} (from JANUS_TIMEZONE)")
            else:
                config["timezone"] = ""
                results["config_added"].append("timezone= (empty, uses server-local)")
            save_config(config)
            if not quiet:
                tz_display = config["timezone"] or "(server-local)"
                print(f"  ✓ Added timezone to config.yaml: {tz_display}")

    # ── Version 8 → 9: clear ANTHROPIC_TOKEN from .env ──
    # The new Anthropic auth flow no longer uses this env var.
    if current_ver < 9:
        try:
            old_token = get_env_value("ANTHROPIC_TOKEN")
            if old_token:
                save_env_value("ANTHROPIC_TOKEN", "")
                if not quiet:
                    print("  ✓ Cleared ANTHROPIC_TOKEN from .env (no longer used)")
        except Exception:
            pass

    # ── Version 11 → 12: migrate custom_providers list → providers dict ──
    if current_ver < 12:
        config = load_config()
        custom_list = config.get("custom_providers")
        if isinstance(custom_list, list) and custom_list:
            providers_dict = config.get("providers", {})
            if not isinstance(providers_dict, dict):
                providers_dict = {}
            migrated_count = 0
            for entry in custom_list:
                if not isinstance(entry, dict):
                    continue
                old_name = entry.get("name", "")
                old_url = entry.get("base_url", "") or entry.get("url", "") or entry.get("api", "") or ""
                if not old_url:
                    continue  # skip entries with no URL

                # Generate a kebab-case key from the display name
                key = old_name.strip().lower().replace(" ", "-").replace("(", "").replace(")", "")
                # Remove consecutive hyphens and trailing hyphens
                while "--" in key:
                    key = key.replace("--", "-")
                key = key.strip("-")
                if not key:
                    # Fallback: derive from URL hostname
                    try:
                        from urllib.parse import urlparse
                        parsed = urlparse(old_url)
                        key = (parsed.hostname or "endpoint").replace(".", "-")
                    except Exception:
                        key = f"endpoint-{migrated_count}"

                # Don't overwrite existing entries
                base_key = key
                suffix = migrated_count
                while key in providers_dict:
                    key = f"{base_key}-{suffix}"
                    suffix += 1

                new_entry = _custom_provider_entry_to_provider_config(
                    entry,
                    provider_key=key,
                )
                if new_entry is None:
                    continue
                if not old_name:
                    new_entry.pop("name", None)
                if new_entry.get("api_key") in {"no-key", "no-key-required", ""}:
                    new_entry.pop("api_key", None)

                providers_dict[key] = new_entry
                migrated_count += 1

            if migrated_count > 0:
                config["providers"] = providers_dict
                # Remove the old list — runtime reads via get_compatible_custom_providers()
                config.pop("custom_providers", None)
                save_config(config)
                if not quiet:
                    print(f"  ✓ Migrated {migrated_count} custom provider(s) to providers: section")
                    for key in list(providers_dict.keys())[-migrated_count:]:
                        ep = providers_dict[key]
                        print(f"    → {key}: {ep.get('api', '')}")

    # ── Version 12 → 13: clear dead LLM_MODEL / OPENAI_MODEL from .env ──
    # These env vars were written by the old setup wizard but nothing reads
    # them anymore (config.yaml is the sole source of truth since March 2026).
    # Stale entries cause user confusion — see issue report.
    if current_ver < 13:
        for dead_var in ("LLM_MODEL", "OPENAI_MODEL"):
            try:
                old_val = get_env_value(dead_var)
                if old_val:
                    save_env_value(dead_var, "")
                    if not quiet:
                        print(f"  ✓ Cleared {dead_var} from .env (no longer used — config.yaml is source of truth)")
            except Exception:
                pass

    # ── Version 13 → 14: migrate legacy flat stt.model to provider section ──
    # Old configs (and cli-config.yaml.example) had a flat `stt.model` key
    # that was provider-agnostic.  When the provider was "local" this caused
    # OpenAI model names (e.g. "whisper-1") to be fed to faster-whisper,
    # crashing with "Invalid model size".  Move the value into the correct
    # provider-specific section and remove the flat key.
    if current_ver < 14:
        # Read raw config (no defaults merged) to check what the user actually
        # wrote, then apply changes to the merged config for saving.
        raw = read_raw_config()
        raw_stt = raw.get("stt", {})
        if isinstance(raw_stt, dict) and "model" in raw_stt:
            legacy_model = raw_stt["model"]
            provider = raw_stt.get("provider", "local")
            config = load_config()
            stt = config.get("stt", {})
            # Remove the legacy flat key
            stt.pop("model", None)
            # Place it in the appropriate provider section only if the
            # user didn't already set a model there
            if provider in {"local", "local_command"}:
                # Don't migrate an OpenAI model name into the local section
                _local_models = {
                    "tiny.en", "tiny", "base.en", "base", "small.en", "small",
                    "medium.en", "medium", "large-v1", "large-v2", "large-v3",
                    "large", "distil-large-v2", "distil-medium.en",
                    "distil-small.en", "distil-large-v3", "distil-large-v3.5",
                    "large-v3-turbo", "turbo",
                }
                if legacy_model in _local_models:
                    # Check raw config — only set if user didn't already
                    # have a nested local.model
                    raw_local = raw_stt.get("local", {})
                    if not isinstance(raw_local, dict) or "model" not in raw_local:
                        local_cfg = stt.setdefault("local", {})
                        local_cfg["model"] = legacy_model
                # else: drop it — it was an OpenAI model name, local section
                # already defaults to "base" via DEFAULT_CONFIG
            else:
                # Cloud provider — put it in that provider's section only
                # if user didn't already set a nested model
                raw_provider = raw_stt.get(provider, {})
                if not isinstance(raw_provider, dict) or "model" not in raw_provider:
                    provider_cfg = stt.setdefault(provider, {})
                    provider_cfg["model"] = legacy_model
            config["stt"] = stt
            save_config(config)
            if not quiet:
                print(f"  ✓ Migrated legacy stt.model to provider-specific config")

    # ── Version 14 → 15: add explicit gateway interim-message gate ──
    if current_ver < 15:
        config = read_raw_config()
        display = config.get("display", {})
        if not isinstance(display, dict):
            display = {}
        if "interim_assistant_messages" not in display:
            display["interim_assistant_messages"] = True
            config["display"] = display
            results["config_added"].append("display.interim_assistant_messages=true (default)")
            save_config(config)
            if not quiet:
                print("  ✓ Added display.interim_assistant_messages=true")

    # ── Version 15 → 16: migrate tool_progress_overrides into display.platforms ──
    if current_ver < 16:
        config = read_raw_config()
        display = config.get("display", {})
        if not isinstance(display, dict):
            display = {}
        old_overrides = display.get("tool_progress_overrides")
        if isinstance(old_overrides, dict) and old_overrides:
            platforms = display.get("platforms", {})
            if not isinstance(platforms, dict):
                platforms = {}
            for plat, mode in old_overrides.items():
                if plat not in platforms:
                    platforms[plat] = {}
                if "tool_progress" not in platforms[plat]:
                    platforms[plat]["tool_progress"] = mode
            display["platforms"] = platforms
            config["display"] = display
            save_config(config)
            if not quiet:
                migrated = ", ".join(f"{p}={m}" for p, m in old_overrides.items())
                print(f"  ✓ Migrated tool_progress_overrides → display.platforms: {migrated}")
            results["config_added"].append("display.platforms (migrated from tool_progress_overrides)")

    # ── Version 16 → 17: remove legacy compression.summary_* keys ──
    if current_ver < 17:
        config = read_raw_config()
        comp = config.get("compression", {})
        if isinstance(comp, dict):
            s_model = comp.pop("summary_model", None)
            s_provider = comp.pop("summary_provider", None)
            s_base_url = comp.pop("summary_base_url", None)
            migrated_keys = []
            # Migrate non-empty, non-default values to auxiliary.compression
            if s_model and str(s_model).strip():
                aux = config.setdefault("auxiliary", {})
                aux_comp = aux.setdefault("compression", {})
                if not aux_comp.get("model"):
                    aux_comp["model"] = str(s_model).strip()
                    migrated_keys.append(f"model={s_model}")
            if s_provider and str(s_provider).strip() not in {"", "auto"}:
                aux = config.setdefault("auxiliary", {})
                aux_comp = aux.setdefault("compression", {})
                if not aux_comp.get("provider") or aux_comp.get("provider") == "auto":
                    aux_comp["provider"] = str(s_provider).strip()
                    migrated_keys.append(f"provider={s_provider}")
            if s_base_url and str(s_base_url).strip():
                aux = config.setdefault("auxiliary", {})
                aux_comp = aux.setdefault("compression", {})
                if not aux_comp.get("base_url"):
                    aux_comp["base_url"] = str(s_base_url).strip()
                    migrated_keys.append(f"base_url={s_base_url}")
            if migrated_keys or s_model is not None or s_provider is not None or s_base_url is not None:
                config["compression"] = comp
                save_config(config)
                if not quiet:
                    if migrated_keys:
                        print(f"  ✓ Migrated compression.summary_* → auxiliary.compression: {', '.join(migrated_keys)}")
                    else:
                        print("  ✓ Removed unused compression.summary_* keys")

    # ── Version 20 → 21: plugins are now opt-in; grandfather existing user plugins ──
    # The loader now requires plugins to appear in ``plugins.enabled`` before
    # loading. Existing installs had all discovered plugins loading by default
    # (minus anything in ``plugins.disabled``). To avoid silently breaking
    # those setups on upgrade, populate ``plugins.enabled`` with the set of
    # currently-installed user plugins that aren't already disabled.
    #
    # Bundled plugins (shipped in the repo itself) are NOT grandfathered —
    # they ship off for everyone, including existing users, so any user who
    # wants one has to opt in explicitly.
    if current_ver < 21:
        config = read_raw_config()
        plugins_cfg = config.get("plugins")
        if not isinstance(plugins_cfg, dict):
            plugins_cfg = {}
        # Only migrate if the enabled allow-list hasn't been set yet.
        if "enabled" not in plugins_cfg:
            disabled = plugins_cfg.get("disabled", []) or []
            if not isinstance(disabled, list):
                disabled = []
            disabled_set = set(disabled)

            # Scan ``$JANUS_HOME/plugins/`` for currently installed user plugins.
            grandfathered: List[str] = []
            try:
                user_plugins_dir = get_janus_home() / "plugins"
                if user_plugins_dir.is_dir():
                    for child in sorted(user_plugins_dir.iterdir()):
                        if not child.is_dir():
                            continue
                        manifest_file = child / "plugin.yaml"
                        if not manifest_file.exists():
                            manifest_file = child / "plugin.yml"
                        if not manifest_file.exists():
                            continue
                        try:
                            with open(manifest_file, encoding="utf-8") as _mf:
                                manifest = yaml.safe_load(_mf) or {}
                        except Exception:
                            manifest = {}
                        name = manifest.get("name") or child.name
                        if name in disabled_set:
                            continue
                        grandfathered.append(name)
            except Exception:
                grandfathered = []

            plugins_cfg["enabled"] = grandfathered
            config["plugins"] = plugins_cfg
            save_config(config)
            results["config_added"].append(
                f"plugins.enabled (opt-in allow-list, {len(grandfathered)} grandfathered)"
            )
            if not quiet:
                if grandfathered:
                    print(
                        f"  ✓ Plugins now opt-in: grandfathered "
                        f"{len(grandfathered)} existing plugin(s) into plugins.enabled"
                    )
                else:
                    print(
                        "  ✓ Plugins now opt-in: no existing plugins to grandfather. "
                        "Use `janus plugins enable <name>` to activate."
                    )

    # ── Version 22 → 23: seed curator defaults + create logs/curator/ ──
    # The curator (background skill maintenance) was added in PR #16049, but
    # existing configs from before that PR (or before the April 2026
    # unification under `auxiliary.curator`) never wrote the curator section
    # to disk. The runtime deep-merge in `load_config()` fills defaults at
    # read time, so the curator *functions*; but users can't see/edit the
    # settings in their `config.yaml`, and `janus curator status` has no
    # stable logs dir to point at until the first run mkdir's it.
    #
    # This migration:
    #   1. Writes the `curator` top-level section to config.yaml (enabled,
    #      interval_hours, min_idle_hours, stale_after_days, archive_after_days)
    #      — only keys the user hasn't already overridden.
    #   2. Writes the `auxiliary.curator` aux-task slot (provider, model,
    #      base_url, api_key, timeout, extra_body) — canonical slot for
    #      routing the curator fork to a cheaper aux model.
    #   3. Creates `~/.janus/logs/curator/` if missing (belt-and-suspenders
    #      on top of ensure_janus_home() — old profiles that predate this
    #      migration still benefit).
    if current_ver < 23:
        try:
            curator_dir = get_janus_home() / "logs" / "curator"
            curator_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            results["warnings"].append(f"Could not create {curator_dir}: {e}")

        config = read_raw_config()
        touched = False

        # (1) Top-level curator section — only add missing keys
        _curator_defaults = DEFAULT_CONFIG.get("curator", {})
        raw_curator = config.get("curator")
        if not isinstance(raw_curator, dict):
            raw_curator = {}
        added_curator: List[str] = []
        for k, v in _curator_defaults.items():
            if k not in raw_curator:
                raw_curator[k] = copy.deepcopy(v)
                added_curator.append(k)
        if added_curator:
            config["curator"] = raw_curator
            touched = True

        # (2) auxiliary.curator task slot
        _aux_curator_defaults = (
            DEFAULT_CONFIG.get("auxiliary", {}).get("curator", {})
        )
        raw_aux = config.get("auxiliary")
        if not isinstance(raw_aux, dict):
            raw_aux = {}
        raw_aux_curator = raw_aux.get("curator")
        if not isinstance(raw_aux_curator, dict):
            raw_aux_curator = {}
        added_aux: List[str] = []
        for k, v in _aux_curator_defaults.items():
            if k not in raw_aux_curator:
                raw_aux_curator[k] = copy.deepcopy(v)
                added_aux.append(k)
        if added_aux:
            raw_aux["curator"] = raw_aux_curator
            config["auxiliary"] = raw_aux
            touched = True

        if touched:
            save_config(config)
            if added_curator:
                results["config_added"].append(
                    f"curator ({len(added_curator)} default key(s))"
                )
                if not quiet:
                    print(
                        "  ✓ Seeded curator defaults in config.yaml: "
                        f"{', '.join(added_curator)}"
                    )
            if added_aux:
                results["config_added"].append(
                    f"auxiliary.curator ({len(added_aux)} default key(s))"
                )
                if not quiet:
                    print(
                        "  ✓ Seeded auxiliary.curator defaults in config.yaml: "
                        f"{', '.join(added_aux)}"
                    )

    # ── Version 24 → 25: lower model_catalog TTL 24h → 1h ──
    # The model picker now refreshes its curated list hourly so freshly
    # published model-catalog.json deploys reach users without a day-long
    # stale window. Only rewrite the OLD default (24) — never clobber a
    # value the user deliberately customized.
    if current_ver < 25:
        config = read_raw_config()
        raw_mc = config.get("model_catalog")
        if isinstance(raw_mc, dict) and raw_mc.get("ttl_hours") == 24:
            raw_mc["ttl_hours"] = 1
            config["model_catalog"] = raw_mc
            save_config(config)
            results["config_added"].append("model_catalog.ttl_hours 24→1")
            if not quiet:
                print("  ✓ Lowered model_catalog.ttl_hours to 1 (hourly picker refresh)")

    if current_ver < latest_ver and not quiet:
        print(f"Config version: {current_ver} → {latest_ver}")
    
    # Check for missing required env vars
    missing_env = get_missing_env_vars(required_only=True)
    
    if missing_env and not quiet:
        print("\n⚠️  Missing required environment variables:")
        for var in missing_env:
            print(f"   • {var['name']}: {var['description']}")
    
    if interactive and missing_env:
        print("\nLet's configure them now:\n")
        for var in missing_env:
            if var.get("url"):
                print(f"  Get your key at: {var['url']}")
            
            if var.get("password"):
                value = masked_secret_prompt(f"  {var['prompt']}: ")
            else:
                value = input(f"  {var['prompt']}: ").strip()
            
            if value:
                save_env_value(var["name"], value)
                results["env_added"].append(var["name"])
                print(f"  ✓ Saved {var['name']}")
            else:
                results["warnings"].append(f"Skipped {var['name']} - some features may not work")
            print()
    
    # Check for missing optional env vars and offer to configure interactively
    # Skip "advanced" vars (like OPENAI_BASE_URL) -- those are for power users
    missing_optional = get_missing_env_vars(required_only=False)
    required_names = {v["name"] for v in missing_env} if missing_env else set()
    missing_optional = [
        v for v in missing_optional
        if v["name"] not in required_names and not v.get("advanced")
    ]
    
    # Only offer to configure env vars that are NEW since the user's previous version
    new_var_names = set()
    for ver in range(current_ver + 1, latest_ver + 1):
        new_var_names.update(ENV_VARS_BY_VERSION.get(ver, []))

    if new_var_names and interactive and not quiet:
        new_and_unset = [
            (name, OPTIONAL_ENV_VARS[name])
            for name in sorted(new_var_names)
            if not get_env_value(name) and name in OPTIONAL_ENV_VARS
        ]
        if new_and_unset:
            print(f"\n  {len(new_and_unset)} new optional key(s) in this update:")
            for name, info in new_and_unset:
                print(f"    • {name} — {info.get('description', '')}")
            print()
            try:
                answer = input("  Configure new keys? [y/N]: ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                answer = "n"

            if answer in {"y", "yes"}:
                print()
                for name, info in new_and_unset:
                    if info.get("url"):
                        print(f"  {info.get('description', name)}")
                        print(f"  Get your key at: {info['url']}")
                    else:
                        print(f"  {info.get('description', name)}")
                    if info.get("password"):
                        value = masked_secret_prompt(
                            f"  {info.get('prompt', name)} (Enter to skip): "
                        )
                    else:
                        value = input(f"  {info.get('prompt', name)} (Enter to skip): ").strip()
                    if value:
                        save_env_value(name, value)
                        results["env_added"].append(name)
                        print(f"  ✓ Saved {name}")
                    print()
            else:
                print("  Set later with: janus config set <key> <value>")
    
    # Check for missing config fields
    missing_config = get_missing_config_fields()
    
    if missing_config:
        config = load_config()
        
        for field in missing_config:
            key = field["key"]
            default = field["default"]
            
            _set_nested(config, key, default)
            results["config_added"].append(key)
            if not quiet:
                print(f"  ✓ Added {key} = {default}")
        
        # Update version and save
        config["_config_version"] = latest_ver
        save_config(config)
    elif current_ver < latest_ver:
        # Just update version
        config = load_config()
        config["_config_version"] = latest_ver
        save_config(config)

    # ── Skill-declared config vars ──────────────────────────────────────
    # Skills can declare config.yaml settings they need via
    # metadata.janus.config in their SKILL.md frontmatter.
    # Prompt for any that are missing/empty.
    missing_skill_config = get_missing_skill_config_vars()
    if missing_skill_config and interactive and not quiet:
        print(f"\n  {len(missing_skill_config)} skill setting(s) not configured:")
        for var in missing_skill_config:
            skill_name = var.get("skill", "unknown")
            print(f"    • {var['key']} — {var['description']} (from skill: {skill_name})")
        print()
        try:
            answer = input("  Configure skill settings? [y/N]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            answer = "n"

        if answer in {"y", "yes"}:
            print()
            config = load_config()
            try:
                from agent.skill_utils import SKILL_CONFIG_PREFIX
            except Exception:
                SKILL_CONFIG_PREFIX = "skills.config"
            for var in missing_skill_config:
                default = var.get("default", "")
                default_hint = f" (default: {default})" if default else ""
                value = input(f"  {var['prompt']}{default_hint}: ").strip()
                if not value and default:
                    value = str(default)
                if value:
                    storage_key = f"{SKILL_CONFIG_PREFIX}.{var['key']}"
                    _set_nested(config, storage_key, value)
                    results["config_added"].append(var["key"])
                    print(f"  ✓ Saved {var['key']} = {value}")
                else:
                    results["warnings"].append(
                        f"Skipped {var['key']} — skill '{var.get('skill', '?')}' may ask for it later"
                    )
                print()
            save_config(config)
        else:
            print("  Set later with: janus config set <key> <value>")

    return results


def _deep_merge(base: dict, override: dict) -> dict:
    """Recursively merge *override* into *base*, preserving nested defaults.

    Keys in *override* take precedence. If both values are dicts the merge
    recurses, so a user who overrides only ``tts.elevenlabs.voice_id`` will
    keep the default ``tts.elevenlabs.model_id`` intact.
    """
    result = base.copy()
    for key, value in override.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def _expand_env_vars(obj):
    """Recursively expand ``${VAR}`` references in config values.

    Only string values are processed; dict keys, numbers, booleans, and
    None are left untouched.  Unresolved references (variable not in
    ``os.environ``) are kept verbatim so callers can detect them.
    """
    if isinstance(obj, str):
        return re.sub(
            r"\${([^}]+)}",
            lambda m: os.environ.get(m.group(1), m.group(0)),
            obj,
        )
    if isinstance(obj, dict):
        return {k: _expand_env_vars(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_expand_env_vars(item) for item in obj]
    return obj


def _items_by_unique_name(items):
    """Return a name-indexed dict only when all items have unique string names."""
    if not isinstance(items, list):
        return None
    indexed = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("name"), str):
            return None
        name = item["name"]
        if name in indexed:
            return None
        indexed[name] = item
    return indexed


