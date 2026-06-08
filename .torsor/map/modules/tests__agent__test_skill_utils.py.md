---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_skill_utils.py

Symbols in `tests/agent/test_skill_utils.py`.

- L12 `test_metadata_as_dict_with_hermes()` (function) — Normal case: metadata is a dict containing hermes keys.
- L31 `test_metadata_as_string_does_not_crash()` (function) — Bug case: metadata is a non-dict truthy value (e.g. a YAML string).
- L43 `test_metadata_as_none()` (function) — metadata key is present but set to null/None.
- L55 `test_metadata_missing_entirely()` (function) — metadata key is absent from frontmatter.
- L67 `test_iter_skill_index_files_prunes_dependency_dirs(tmp_path)` (function)
- L108 `TestSkillMatchesPlatformTermux` (class) — Termux is Linux userland on Android. Skills tagged platforms:[linux]
- L117 `test_no_platforms_field_matches_everywhere(self)` (method)
- L126 `test_linux_skill_loads_on_termux_android_platform(self)` (method)
- L134 `test_linux_macos_windows_skill_loads_on_termux(self)` (method)
- L143 `test_linux_skill_loads_on_termux_linux_platform(self)` (method)
- L152 `test_macos_only_skill_still_excluded_on_termux(self)` (method)
- L161 `test_windows_only_skill_still_excluded_on_termux(self)` (method)
- L168 `test_explicit_termux_or_android_tag_matches(self)` (method)
- L177 `test_non_termux_android_does_not_widen(self)` (method)
- L186 `test_linux_skill_on_real_linux_unaffected(self)` (method)
- L194 `test_macos_skill_on_real_macos_unaffected(self)` (method)
