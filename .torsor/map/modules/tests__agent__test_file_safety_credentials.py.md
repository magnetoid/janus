---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_file_safety_credentials.py

Symbols in `tests/agent/test_file_safety_credentials.py`.

- L23 `fake_home(tmp_path, monkeypatch)` (function) — Point ``_hermes_home_path()`` at a tmp dir for isolated checks.
- L33 `_create(home: Path, rel: str | Path)` (function) — Create the file (with parents) so realpath() resolves it.
- L41 `test_auth_json_blocked(fake_home)` (function)
- L51 `test_auth_lock_blocked(fake_home)` (function)
- L60 `test_anthropic_oauth_json_blocked(fake_home)` (function)
- L69 `test_google_oauth_json_blocked(fake_home)` (function) — Gemini OAuth tokens live under auth/google_oauth.json — blocked.
- L79 `test_arbitrary_hermes_home_file_not_blocked(fake_home)` (function) — Non-credential files inside HERMES_HOME stay readable.
- L87 `test_subdirectory_named_auth_json_not_blocked(fake_home)` (function) — Only the top-level auth.json is the credential store; a file with the
- L96 `test_skills_hub_block_still_applies(fake_home)` (function) — Regression guard: the original skills/.hub deny must keep working.
- L106 `test_path_traversal_resolves_to_blocked(fake_home, tmp_path)` (function) — A path that traverses through a sibling dir back into HERMES_HOME's
- L120 `test_symlink_to_auth_json_blocked(fake_home, tmp_path)` (function) — A symlink pointing at HERMES_HOME/auth.json from outside the home
- L136 `test_read_file_tool_blocks_relative_path_under_terminal_cwd(fake_home, tmp_path, monkeypatch)` (function) — Bypass guard: a relative path like ``"auth.json"`` resolved by
- L162 `test_read_file_tool_blocks_nested_google_oauth_path(fake_home, tmp_path, monkeypatch)` (function) — The real read_file tool must not return Gemini OAuth token material.
- L198 `test_dotenv_blocked(fake_home)` (function) — .env in HERMES_HOME holds API keys — blocked.
- L208 `test_webhook_subscriptions_blocked(fake_home)` (function) — webhook_subscriptions.json holds per-route HMAC secrets — blocked.
- L218 `test_mcp_tokens_file_blocked(fake_home)` (function) — Files under mcp-tokens/ hold OAuth tokens — blocked.
- L228 `test_mcp_tokens_nested_blocked(fake_home)` (function) — Nested files inside mcp-tokens/ are also blocked.
- L238 `test_mcp_tokens_dir_itself_blocked(fake_home)` (function) — The mcp-tokens directory itself is blocked (listing is exfiltrating).
- L249 `test_identically_named_hermes_files_outside_home_not_blocked(fake_home, tmp_path)` (function) — Hermes-specific filenames (``auth.json``, ``mcp-tokens/``, ``google_oauth.json``)
- L280 `test_non_secret_auth_subtree_file_not_blocked(fake_home)` (function) — Only the known Google OAuth token path is blocked, not all auth/*.
- L288 `test_config_yaml_not_blocked(fake_home)` (function) — config.yaml is NOT a credential file — agent should still be
- L298 `test_profile_mode_blocks_root_credentials(tmp_path, monkeypatch)` (function) — Under a profile, HERMES_HOME = <root>/profiles/<name>, but
