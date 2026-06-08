---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_system_prompt_restore.py

Symbols in `tests/agent/test_system_prompt_restore.py`.

- L26 `_make_agent(session_db=None, prebuilt_prompt: str='BUILT_PROMPT')` (function) — Construct the minimal agent fake the helper needs.
- L43 `TestStoredPromptReuse` (class)
- L44 `test_present_row_is_reused_verbatim(self, caplog)` (method) — Continuing session with a stored prompt → reuse byte-for-byte.
- L60 `test_present_row_with_unicode_preserved(self)` (method) — Non-ASCII bytes in the stored prompt are not mangled.
- L76 `TestLegitimateFreshBuild` (class)
- L77 `test_no_history_skips_db_and_builds_fresh(self, caplog)` (method) — First turn with empty history → build fresh, don't touch the DB.
- L93 `test_no_db_skips_persistence(self)` (method) — When session DB is None, build and skip persistence silently.
- L106 `TestSilentFailureWarnings` (class)
- L107 `test_db_read_exception_warns_and_rebuilds(self, caplog)` (method) — DB read raising → WARNING + fall through to fresh build.
- L125 `test_null_system_prompt_warns_about_unusable_stored_state(self, caplog)` (method) — Row exists but system_prompt is NULL → WARNING + fresh build.
- L139 `test_empty_system_prompt_warns_about_silent_persistence_bug(self, caplog)` (method) — Row exists but system_prompt is '' → WARNING about silent write bug.
- L153 `test_db_write_failure_warns_loudly(self, caplog)` (method) — update_system_prompt raising → WARNING (was DEBUG before).
- L174 `test_no_history_with_null_row_does_not_warn(self, caplog)` (method) — First turn (no history) hitting a null row is not surprising — no warn.
- L195 `TestPromptStabilityInvariant` (class)
- L196 `test_restored_prompt_is_byte_identical_to_stored(self)` (method) — The restored prompt must equal the stored bytes exactly — no
