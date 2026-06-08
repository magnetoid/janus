---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/skills_hub.py

Symbols in `hermes_cli/skills_hub.py`.

- L35 `_resolve_short_name(name: str, sources, console: Console)` (function) — Resolve a short skill name (e.g. 'pptx') to a full identifier by searching
- L84 `_format_extra_metadata_lines(extra: Dict[str, Any])` (function)
- L112 `_resolve_source_meta_and_bundle(identifier: str, sources)` (function) — Resolve metadata and bundle for a specific identifier.
- L142 `_derive_category_from_install_path(install_path: str)` (function)
- L156 `_is_valid_installed_skill_name(name: str)` (function) — Accept identifier-shaped names, reject empty / sentinel-y values.
- L166 `_existing_categories()` (function) — Return sorted subdirectory names under ``~/.hermes/skills/`` that look
- L198 `_prompt_for_skill_name(c: Console, url: str, default: str='')` (function) — Prompt interactively for a skill name. Returns None on cancel/EOF.
- L223 `_prompt_for_category(c: Console, existing: List[str])` (function) — Prompt interactively for a category. Empty/None input means flat install.
- L248 `do_search(query: str, source: str='all', limit: int=10, console: Optional[Console]=None, as_json: bool=False)` (function) — Search registries and display results as a Rich table.
- L317 `do_browse(page: int=1, page_size: int=20, source: str='all', console: Optional[Console]=None)` (function) — Browse all available skills across registries, paginated.
- L462 `do_install(identifier: str, category: str='', force: bool=False, console: Optional[Console]=None, skip_confirm: bool=False, invalidate_cache: bool=True, name_override: str='')` (function) — Fetch, quarantine, scan, confirm, and install a skill.
- L690 `do_inspect(identifier: str, console: Optional[Console]=None)` (function) — Preview a skill's SKILL.md content without installing.
- L740 `browse_skills(page: int=1, page_size: int=20, source: str='all')` (function) — Paginated hub browse for programmatic callers (e.g. TUI gateway).
- L789 `inspect_skill(identifier: str)` (function) — Skill metadata (+ SKILL.md preview) for programmatic callers.
- L827 `do_list(source_filter: str='all', enabled_only: bool=False, console: Optional[Console]=None)` (function) — List installed skills, distinguishing hub, builtin, and local skills.
- L926 `do_check(name: Optional[str]=None, console: Optional[Console]=None)` (function) — Check hub-installed skills for upstream updates.
- L949 `do_update(name: Optional[str]=None, console: Optional[Console]=None)` (function) — Update hub-installed skills with upstream changes.
- L969 `do_audit(name: Optional[str]=None, console: Optional[Console]=None, deep: bool=False)` (function) — Re-run security scan on installed hub skills.
- L1015 `do_uninstall(name: str, console: Optional[Console]=None, skip_confirm: bool=False, invalidate_cache: bool=True)` (function) — Remove a hub-installed skill with confirmation.
- L1050 `do_reset(name: str, restore: bool=False, console: Optional[Console]=None, skip_confirm: bool=False, invalidate_cache: bool=True)` (function) — Reset a bundled skill's manifest tracking (+ optionally restore from bundled).
- L1095 `do_opt_out(remove: bool=False, console: Optional[Console]=None, skip_confirm: bool=False, invalidate_cache: bool=True)` (function) — Opt the active profile out of bundled-skill seeding.
- L1165 `do_opt_in(sync: bool=False, console: Optional[Console]=None, invalidate_cache: bool=True)` (function) — Remove the opt-out marker so bundled-skill seeding resumes.
- L1196 `do_repair_official(name: str, restore: bool=False, console: Optional[Console]=None, skip_confirm: bool=False, invalidate_cache: bool=True)` (function) — Backfill or restore official optional skills from repo source.
- L1238 `do_tap(action: str, repo: str='', console: Optional[Console]=None)` (function) — Manage taps (custom GitHub repo sources).
- L1281 `do_publish(skill_path: str, target: str='github', repo: str='', console: Optional[Console]=None)` (function) — Publish a local skill to a registry (GitHub PR or ClawHub submission).
- L1350 `_github_publish(skill_path: Path, skill_name: str, target_repo: str, auth)` (function) — Create a PR to a GitHub repo with the skill. Returns (success, message).
- L1447 `do_snapshot_export(output_path: str, console: Optional[Console]=None)` (function) — Export current hub skill configuration to a portable JSON file.
- L1487 `do_snapshot_import(input_path: str, force: bool=False, console: Optional[Console]=None)` (function) — Re-install skills from a snapshot file.
- L1538 `skills_command(args)` (function) — Router for `hermes skills <subcommand>` — called from hermes_cli/main.py.
- L1608 `handle_skills_slash(cmd: str, console: Optional[Console]=None)` (function) — Parse and dispatch `/skills <subcommand> [args]` from the chat interface.
- L1815 `_print_skills_help(console: Console)` (function) — Print help for the /skills slash command.
