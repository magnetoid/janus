---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/profile_describer.py

Symbols in `hermes_cli/profile_describer.py`.

- L91 `DescribeOutcome` (class) — Result of describing a single profile.
- L100 `_collect_skills(profile_dir: Path)` (function) — Return a stable, capped list of skill names for the prompt.
- L138 `_extract_json_blob(raw: str)` (function)
- L156 `describe_profile(profile_name: str, *, overwrite: bool=False, timeout: Optional[int]=None)` (function) — Auto-generate a description for one profile.
- L287 `list_describable_profiles(*, missing_only: bool=True)` (function) — Return profile names that can be described.
