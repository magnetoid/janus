---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/cli/test_personality_none.py

Symbols in `tests/cli/test_personality_none.py`.

- L9 `TestCLIPersonalityNone` (class)
- L11 `_make_cli(self, personalities=None)` (method)
- L23 `test_none_clears_system_prompt(self)` (method)
- L29 `test_default_clears_system_prompt(self)` (method)
- L35 `test_neutral_clears_system_prompt(self)` (method)
- L41 `test_none_forces_agent_reinit(self)` (method)
- L47 `test_none_saves_to_config(self)` (method)
- L53 `test_known_personality_still_works(self)` (method)
- L59 `test_unknown_personality_shows_none_in_available(self, capsys)` (method)
- L65 `test_list_shows_none_option(self)` (method)
- L75 `TestGatewayPersonalityNone` (class)
- L77 `_make_event(self, args='')` (method)
- L83 `_make_runner(self, personalities=None)` (method)
- L95 `test_none_clears_ephemeral_prompt(self, tmp_path)` (method)
- L109 `test_default_clears_ephemeral_prompt(self, tmp_path)` (method)
- L122 `test_list_includes_none(self, tmp_path)` (method)
- L135 `test_unknown_shows_none_in_available(self, tmp_path)` (method)
- L148 `test_empty_personality_list_uses_profile_display_path(self, tmp_path)` (method)
- L160 `TestPersonalityDictFormat` (class) — Test dict-format custom personalities with description, tone, style.
- L163 `_make_cli(self, personalities)` (method)
- L172 `test_dict_personality_uses_system_prompt(self)` (method)
- L185 `test_dict_personality_includes_tone(self)` (method)
- L196 `test_dict_personality_includes_style(self)` (method)
- L207 `test_string_personality_still_works(self)` (method)
- L213 `test_resolve_prompt_dict_no_tone_no_style(self)` (method)
- L221 `test_resolve_prompt_string(self)` (method)
