---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_banner.py

Symbols in `tests/hermes_cli/test_banner.py`.

- L12 `test_display_toolset_name_strips_legacy_suffix()` (function)
- L18 `test_display_toolset_name_preserves_clean_names()` (function)
- L24 `test_display_toolset_name_handles_empty()` (function)
- L29 `test_build_welcome_banner_uses_normalized_toolset_names()` (function) — Unavailable toolsets should not have '_tools' appended in banner output.
- L73 `test_build_welcome_banner_title_is_hyperlinked_to_release()` (function) — Panel title (version label) is wrapped in an OSC-8 hyperlink to the GitHub release.
- L108 `test_build_welcome_banner_title_falls_back_when_no_tag()` (function) — Without a resolvable tag, the panel title renders as plain text (no hyperlink escape).
- L138 `test_build_welcome_banner_disabled_mcp_shows_disabled_not_failed()` (function) — A disabled MCP server renders '— disabled' (dim), not '— failed' (red).
