---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_prompt_size.py

Symbols in `tests/hermes_cli/test_prompt_size.py`.

- L14 `_seed_memory(hermes_home, memory_text='', user_text='')` (function)
- L23 `_seed_skill(hermes_home, name, description)` (function)
- L33 `isolated_home(tmp_path, monkeypatch)` (function)
- L41 `test_breakdown_keys_and_shape(isolated_home)` (function) — The breakdown exposes every documented key with int byte/char counts.
- L64 `test_runs_offline_without_credentials(isolated_home, monkeypatch)` (function) — No provider credentials configured → still produces a breakdown.
- L73 `test_skills_index_reflects_installed_skills(isolated_home)` (function) — Installing a skill makes the skills-index block non-empty.
- L85 `test_memory_and_profile_are_attributed(isolated_home)` (function) — Memory and user-profile blocks are measured separately.
- L97 `test_skills_block_regex_matches_tagged_block()` (function)
- L105 `test_render_breakdown_is_plain_text(isolated_home)` (function)
- L115 `test_json_serializable(isolated_home)` (function)
