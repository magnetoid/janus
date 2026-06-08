---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/setup.py

Symbols in `hermes_cli/setup.py`.

- L36 `_model_config_dict(config: Dict[str, Any])` (function)
- L45 `_get_credential_pool_strategies(config: Dict[str, Any])` (function)
- L50 `_set_credential_pool_strategy(config: Dict[str, Any], provider: str, strategy: str)` (function)
- L58 `_supports_same_provider_pool_setup(provider: str)` (function)
- L114 `_current_reasoning_effort(config: Dict[str, Any])` (function)
- L121 `_set_reasoning_effort(config: Dict[str, Any], effort: str)` (function)
- L150 `print_header(title: str)` (function) — Print a section header.
- L165 `is_interactive_stdin()` (function) — Return True when stdin looks like a usable interactive TTY.
- L176 `print_noninteractive_setup_guidance(reason: str | None=None)` (function) — Print guidance for headless/non-interactive setup flows.
- L195 `prompt(question: str, default: str=None, password: bool=False)` (function) — Prompt for input with optional default.
- L218 `_sanitize_pasted_input(value: str)` (function) — Strip terminal bracketed-paste control markers from pasted text.
- L225 `_curses_prompt_choice(question: str, choices: list, default: int=0, description: str | None=None)` (function) — Single-select menu using curses. Delegates to curses_radiolist.
- L232 `prompt_choice(question: str, choices: list, default: int=0, description: str | None=None)` (function) — Prompt for a choice from a list with arrow key navigation.
- L275 `prompt_yes_no(question: str, default: bool=True)` (function) — Prompt for yes/no. Ctrl+C exits, empty input returns default.
- L299 `prompt_checklist(title: str, items: list, pre_selected: list=None)` (function) — Display a multi-select checklist and return the indices of selected items.
- L328 `_prompt_api_key(var: dict)` (function) — Display a nicely formatted API key input screen for a single env var.
- L356 `_print_setup_summary(config: dict, hermes_home)` (function) — Print the setup completion summary.
- L642 `_prompt_container_resources(config: dict)` (function) — Prompt for container resource settings (Docker, Singularity, Modal, Daytona).
- L694 `setup_model_provider(config: dict, *, quick: bool=False)` (function) — Configure the inference provider and default model.
- L756 `_check_espeak_ng()` (function) — Check if espeak-ng is installed.
- L761 `_install_neutts_deps()` (function) — Install NeuTTS dependencies with user approval. Returns True on success.
- L811 `_install_kittentts_deps()` (function) — Install KittenTTS dependencies with user approval. Returns True on success.
- L836 `_xai_oauth_logged_in_for_setup()` (function) — True iff xAI Grok OAuth credentials are already stored locally.
- L850 `_run_xai_oauth_login_from_setup()` (function) — Run the xAI Grok OAuth loopback login from inside the setup wizard.
- L888 `_setup_tts_provider(config: dict)` (function) — Interactive TTS provider selection with install flow for NeuTTS.
- L1124 `setup_tts(config: dict)` (function) — Standalone TTS setup (for 'hermes setup tts').
- L1134 `setup_terminal_backend(config: dict)` (function) — Configure the terminal execution backend.
- L1437 `_apply_default_agent_settings(config: dict)` (function) — Apply recommended defaults for all agent settings without prompting.
- L1465 `setup_agent_settings(config: dict)` (function) — Configure agent behavior: iterations, progress display, compression, session reset.
- L1645 `_is_valid_telegram_bot_token(token: str)` (function)
- L1649 `_setup_telegram_auto_result()` (function) — Attempt automatic Telegram bot creation via managed QR onboarding.
- L1667 `_setup_telegram_auto()` (function) — Attempt automatic Telegram bot creation and return only the token.
- L1673 `_prompt_telegram_bot_token()` (function)
- L1688 `_setup_telegram()` (function) — Configure Telegram bot credentials and allowlist.
- L1798 `_setup_slack()` (function) — Configure Slack bot credentials.
- L1866 `_write_slack_manifest_and_instruct()` (function) — Generate the Slack manifest, write it under HERMES_HOME, and print
- L1909 `_setup_matrix()` (function) — Configure Matrix credentials.
- L2025 `_setup_bluebubbles()` (function) — Configure BlueBubbles iMessage gateway.
- L2090 `_setup_qqbot()` (function) — Configure QQ Bot (Official API v2) via gateway setup.
- L2096 `_setup_webhooks()` (function) — Configure webhook integration.
- L2143 `setup_gateway(config: dict)` (function) — Configure messaging platform integrations.
- L2383 `setup_tools(config: dict, first_install: bool=False)` (function) — Configure tools — delegates to the unified tools_command() in tools_config.py.
- L2403 `_model_section_has_credentials(config: dict)` (function) — Return True when any known inference provider has usable credentials.
- L2465 `_gateway_platform_short_label(label: str)` (function) — Strip trailing parenthetical qualifiers from a gateway platform label.
- L2471 `_get_section_config_summary(config: dict, section_key: str)` (function) — Return a short summary if a setup section is already configured, else None.
- L2526 `_skip_configured_section(config: dict, section_key: str, label: str)` (function) — Show an already-configured section summary and offer to skip.
- L2555 `_load_openclaw_migration_module()` (function) — Load the openclaw_to_hermes migration script as a module.
- L2599 `_print_migration_preview(report: dict)` (function) — Print a detailed dry-run preview of what migration would do.
- L2663 `_offer_openclaw_migration(hermes_home: Path)` (function) — Detect ~/.openclaw and offer to migrate during first-time setup.
- L2810 `_run_portal_one_shot(config: dict)` (function) — One-shot Nous Portal setup — OAuth + model pick + provider + Tool Gateway.
- L2894 `run_setup_wizard(args)` (function) — Run the interactive setup wizard.
- L3125 `_run_first_time_quick_setup(config: dict, hermes_home, is_existing: bool)` (function) — Streamlined first-time setup via Nous Portal: OAuth, model, terminal & messaging.
- L3198 `_run_quick_setup(config: dict, hermes_home)` (function) — Quick setup — only configure items that are missing.
