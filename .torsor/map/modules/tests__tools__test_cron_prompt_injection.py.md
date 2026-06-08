---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_cron_prompt_injection.py

Symbols in `tests/tools/test_cron_prompt_injection.py`.

- L13 `TestMultiWordInjectionBypass` (class) — Multi-word variants that previously bypassed the scanner.
- L16 `test_ignore_all_prior_instructions(self)` (method)
- L19 `test_ignore_all_previous_instructions(self)` (method)
- L22 `test_ignore_every_prior_instructions(self)` (method)
- L27 `test_ignore_your_all_instructions(self)` (method)
- L30 `test_ignore_the_above_instructions(self)` (method)
- L33 `test_case_insensitive(self)` (method)
- L36 `test_single_word_still_works(self)` (method) — Original single-word patterns must still be caught.
- L43 `test_clean_prompts_not_blocked(self)` (method) — Ensure the broader regex doesn't create false positives.
