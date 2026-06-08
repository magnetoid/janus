---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/commands.py

Symbols in `hermes_cli/commands.py`.

- L46 `CommandDef` (class) — Definition of a single slash command.
- L232 `_build_command_lookup()` (function) — Map every name and alias to its CommandDef.
- L245 `resolve_command(name: str)` (function) — Resolve a command name or alias to its CommandDef.
- L253 `_build_description(cmd: CommandDef)` (function) — Build a CLI-facing description string including usage hint.
- L313 `is_gateway_known_command(name: str | None)` (function) — Return True if ``name`` resolves to a gateway-dispatchable slash command.
- L358 `should_bypass_active_session(command_name: str | None)` (function) — Return True for any resolvable slash command.
- L381 `_resolve_config_gates()` (function) — Return canonical names of commands whose ``gateway_config_gate`` is truthy.
- L410 `_is_gateway_available(cmd: CommandDef, config_overrides: set[str] | None=None)` (function) — Check if *cmd* should appear in gateway surfaces (help, menus, mappings).
- L426 `_requires_argument(args_hint: str)` (function) — Return True when selecting a command without text would be incomplete.
- L431 `gateway_help_lines()` (function) — Generate gateway help text lines from the registry.
- L450 `_iter_plugin_command_entries()` (function) — Yield (name, description, args_hint) tuples for all plugin slash commands.
- L482 `telegram_bot_commands()` (function) — Return (command_name, description) pairs for Telegram setMyCommands.
- L553 `_prioritize_telegram_menu_commands(commands: list[tuple[str, str]])` (function)
- L590 `_sanitize_telegram_name(raw: str)` (function) — Convert a command/skill/plugin name to a valid Telegram command name.
- L604 `_clamp_command_names(entries: list[tuple[str, ...]], reserved: set[str])` (function) — Enforce 32-char command name limit with collision avoidance.
- L651 `_collect_gateway_skill_entries(platform: str, max_slots: int, reserved_names: set[str], desc_limit: int=100, sanitize_name: 'Callable[[str], str] | None'=None)` (function) — Collect plugin + skill entries for a gateway platform.
- L776 `telegram_menu_commands(max_commands: int=100)` (function) — Return Telegram menu commands capped to the Bot API limit.
- L811 `discord_skill_commands(max_slots: int, reserved_names: set[str])` (function) — Return skill entries for Discord slash command registration.
- L841 `discord_skill_commands_by_category(reserved_names: set[str])` (function) — Return skill entries organized by category for Discord ``/skill`` autocomplete.
- L1023 `_sanitize_slack_name(raw: str)` (function) — Convert a command name to a valid Slack slash command name.
- L1035 `slack_native_slashes()` (function) — Return (slash_name, description, usage_hint) triples for Slack.
- L1098 `slack_app_manifest(request_url: str='https://hermes-agent.local/slack/commands')` (function) — Generate a Slack app manifest with all gateway commands as slashes.
- L1125 `slack_subcommand_map()` (function) — Return subcommand -> /command mapping for Slack /hermes handler.
- L1153 `SlashCommandCompleter` (class) — Autocomplete for built-in slash commands, subcommands, and skill commands.
- L1156 `__init__(self, skill_commands_provider: Callable[[], Mapping[str, dict[str, Any]]] | None=None, command_filter: Callable[[str], bool] | None=None, skill_bundles_provider: Callable[[], Mapping[str, dict[str, Any]]] | None=None)` (method)
- L1170 `_command_allowed(self, slash_command: str)` (method)
- L1178 `_iter_skill_commands(self)` (method)
- L1186 `_iter_skill_bundles(self)` (method)
- L1201 `_completion_text(cmd_name: str, word: str)` (method) — Return replacement text for a completion.
- L1221 `_extract_path_word(text: str)` (method) — Extract the current word if it looks like a file path.
- L1245 `_path_completions(word: str, limit: int=30)` (method) — Yield Completion objects for file paths matching *word*.
- L1296 `_extract_context_word(text: str)` (method) — Extract a bare ``@`` token for context reference completions.
- L1309 `_context_completions(self, word: str, limit: int=30)` (method) — Yield Claude Code-style @ context completions.
- L1395 `_get_project_files(self)` (method) — Return cached list of project files (refreshed every 5s).
- L1437 `_score_path(filepath: str, query: str)` (method) — Score a file path against a fuzzy query. Higher = better match.
- L1481 `_fuzzy_file_completions(self, word: str, query: str, limit: int=20)` (method) — Yield fuzzy file completions for bare @query.
- L1525 `_skin_completions(sub_text: str, sub_lower: str)` (method) — Yield completions for /skin from available skins.
- L1542 `_personality_completions(sub_text: str, sub_lower: str)` (method) — Yield completions for /personality from configured personalities.
- L1569 `get_completions(self, document, complete_event)` (method)
- L1670 `SlashCommandAutoSuggest` (class) — Inline ghost-text suggestions for slash commands and their subcommands.
- L1677 `__init__(self, history_suggest: AutoSuggest | None=None, completer: SlashCommandCompleter | None=None)` (method)
- L1685 `get_suggestion(self, buffer, document)` (method)
- L1728 `_file_size_label(path: str)` (function) — Return a compact human-readable file size, or '' on error.
