---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# optional-skills/creative/kanban-video-orchestrator/scripts/bootstrap_pipeline.py

Symbols in `optional-skills/creative/kanban-video-orchestrator/scripts/bootstrap_pipeline.py`.

- L70 `load_template(name: str)` (function)
- L78 `validate_plan(plan: dict)` (function) — Return a list of validation error strings; empty list = valid.
- L132 `render_brief(plan: dict)` (function) — Render brief.md from the plan.
- L204 `render_team_md(plan: dict)` (function) — Render TEAM.md from the team list + scene → tool mapping.
- L324 `render_setup_sh(plan: dict, brief_md: str, team_md: str)` (function) — Render setup.sh from the plan.
- L403 `render_soul_md(team_member: dict, plan: dict)` (function) — Render a profile's SOUL.md from a team member dict + plan context.
- L464 `main()` (function)
