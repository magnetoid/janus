---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/skills/test_google_workspace_credential_files.py

Symbols in `tests/skills/test_google_workspace_credential_files.py`.

- L23 `_parse_frontmatter(content: str)` (function)
- L30 `TestGoogleWorkspaceCredentialFiles` (class)
- L31 `test_required_credential_files_present_in_skill_md(self)` (method)
- L45 `test_entries_are_registered_when_files_exist(self, tmp_path)` (method)
- L74 `test_missing_token_is_reported(self, tmp_path)` (method) — google_token.json absent (first-time setup) — reported as missing, client secret still mounts.
