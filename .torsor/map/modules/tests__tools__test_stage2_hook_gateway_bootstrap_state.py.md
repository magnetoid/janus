---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_stage2_hook_gateway_bootstrap_state.py

Symbols in `tests/tools/test_stage2_hook_gateway_bootstrap_state.py`.

- L39 `stage2_text()` (function)
- L45 `_seed_block(text: str)` (function) — Extract the ``if [ ! -f "$HERMES_HOME/gateway_state.json" ] && … fi``
- L60 `test_seed_block_present_and_guarded(stage2_text: str)` (function)
- L70 `_run_seed(text: str, *, env_value: str | None, preexisting: str | None)` (function) — Run the extracted seed block in a sandbox $HERMES_HOME.
- L121 `test_seeds_running_state_on_blank_volume(stage2_text: str)` (function) — env=running + no pre-existing file -> writes a valid running state.
- L128 `test_does_not_clobber_existing_state(stage2_text: str)` (function) — The [ ! -f ] guard: an existing state file is never overwritten, even
- L137 `test_no_seed_when_env_unset(stage2_text: str)` (function) — No env var -> no file written (preserves the default down-on-first-boot
- L144 `test_non_running_value_ignored(stage2_text: str)` (function) — Only a literal "running" is honoured; any other value is ignored so a
