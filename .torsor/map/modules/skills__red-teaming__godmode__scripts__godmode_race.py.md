---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# skills/red-teaming/godmode/scripts/godmode_race.py

Symbols in `skills/red-teaming/godmode/scripts/godmode_race.py`.

- L168 `is_refusal(content)` (function) — Check if response is a refusal.
- L176 `count_hedges(content)` (function) — Count hedge/disclaimer patterns in content.
- L185 `score_response(content, query)` (function) — Score a response. Higher is better.
- L282 `_query_model(client, model, messages, timeout=60)` (function) — Query a single model. Returns (model, content, latency) or (model, None, error).
- L300 `race_models(query, tier='standard', api_key=None, system_prompt=None, max_workers=10, timeout=60, append_directive=True, jailbreak_system=None, prefill=None)` (function) — Race multiple models against a query, return the best unfiltered response.
- L400 `race_godmode_classic(query, api_key=None, timeout=60)` (function) — Race the 5 GODMODE CLASSIC combos — each with its own model + jailbreak template.
