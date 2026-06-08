---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_stage2_hook_user_flag_guard.py

Symbols in `tests/tools/test_stage2_hook_user_flag_guard.py`.

- L38 `_read(p: Path)` (function)
- L44 `_guard_block(text: str)` (function) — Extract the `cur_uid=...; if [ ... ]; then ... exit 1; fi` guard.
- L55 `test_guard_present_and_mentions_remediation(path: Path)` (function)
- L67 `_run_guard(text: str, *, cur_uid: int, hermes_uid: int=10000)` (function) — Run the extracted guard with `id` stubbed. Returns the completed process
- L87 `test_arbitrary_user_uid_is_rejected()` (function) — An arbitrary host UID (1000), neither root nor hermes, is rejected.
- L96 `test_root_start_passes()` (function) — Root start (uid 0) is never blocked.
- L104 `test_user_pinned_to_hermes_uid_passes()` (function) — `--user 10000:10000` (the hermes UID itself) is the supported non-root
- L113 `test_user_pinned_to_remapped_hermes_uid_passes()` (function) — After a HERMES_UID remap the hermes UID is e.g. 4242; a container pinned
