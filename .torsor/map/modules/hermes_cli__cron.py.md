---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/cron.py

Symbols in `hermes_cli/cron.py`.

- L33 `_contains_gateway_lifecycle_command(text: str)` (function) — Return True if *text* contains a gateway lifecycle command pattern.
- L38 `_normalize_skills(single_skill=None, skills: Optional[Iterable[str]]=None)` (function)
- L54 `_cron_api(**kwargs)` (function)
- L60 `cron_list(show_all: bool=False)` (function) — List all scheduled jobs.
- L151 `cron_tick()` (function) — Run due jobs once and exit.
- L157 `cron_status()` (function) — Show cron execution status.
- L190 `cron_create(args)` (function)
- L248 `cron_edit(args)` (function)
- L315 `_job_action(action: str, job_id: str, success_verb: str)` (function)
- L329 `cron_command(args)` (function) — Handle cron subcommands.
