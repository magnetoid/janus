---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_profile_export_credentials.py

Symbols in `tests/hermes_cli/test_profile_export_credentials.py`.

- L13 `TestCredentialExclusion` (class)
- L15 `test_auth_json_in_default_exclude_set(self)` (method) — auth.json must be in the default export exclusion set.
- L19 `test_dotenv_in_default_exclude_set(self)` (method) — .env must be in the default export exclusion set.
- L23 `test_named_profile_export_excludes_auth(self, tmp_path, monkeypatch)` (method) — Named profile export must not contain auth.json or .env.
