---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_api_max_retries_config.py

Symbols in `tests/run_agent/test_api_max_retries_config.py`.

- L12 `_make_agent(api_max_retries=None)` (function) — Build an AIAgent with a mocked config.load_config that returns a
- L31 `test_default_api_max_retries_is_three()` (function) — No config override → legacy default of 3 retries preserved.
- L37 `test_api_max_retries_honors_config_override()` (function) — Setting agent.api_max_retries in config propagates to the agent.
- L46 `test_api_max_retries_clamps_below_one_to_one()` (function) — 0 or negative values would disable the retry loop entirely
- L57 `test_api_max_retries_falls_back_on_invalid_value()` (function) — Garbage values in config don't crash agent init — fall back to 3.
