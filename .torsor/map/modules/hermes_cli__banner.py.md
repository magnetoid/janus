---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/banner.py

Symbols in `hermes_cli/banner.py`.

- L39 `cprint(text: str)` (function) — Print ANSI-colored text through prompt_toolkit's renderer.
- L50 `_skin_color(key: str, fallback: str)` (function) — Get a color from the active skin, or return fallback.
- L92 `get_available_skills()` (function) — Return skills grouped by category, filtered by platform and disabled state.
- L126 `_check_via_rev(local_rev: str)` (function) — Compare an embedded git revision to upstream main via ls-remote.
- L147 `_check_via_local_git(repo_dir: Path)` (function) — Count commits behind origin/main in a local checkout.
- L171 `_version_tuple(v: str)` (function) — Parse '0.13.0' into (0, 13, 0) for comparison. Non-numeric segments become 0.
- L182 `_fetch_pypi_latest(package: str='hermes-agent')` (function) — Fetch the latest version of a package from PyPI. Returns None on failure.
- L195 `check_via_pypi()` (function) — Compare installed version against PyPI latest.
- L213 `check_for_updates()` (function) — Check whether a Hermes update is available.
- L289 `_resolve_repo_dir()` (function) — Return the active Hermes git checkout, or None if this isn't a git install.
- L303 `_git_short_hash(repo_dir: Path, rev: str)` (function) — Resolve a git revision to an 8-character short hash.
- L321 `get_git_banner_state(repo_dir: Optional[Path]=None)` (function) — Return upstream/local git hashes for the startup banner.
- L381 `get_latest_release_tag(repo_dir: Optional[Path]=None)` (function) — Return ``(tag, release_url)`` for the latest git tag, or None.
- L423 `format_banner_version_label()` (function) — Return the version label shown in the startup banner title.
- L449 `prefetch_update_check()` (function) — Kick off update check in a background daemon thread.
- L459 `get_update_result(timeout: float=0.5)` (function) — Get result of prefetched check. Returns None if not ready.
- L469 `_format_context_length(tokens: int)` (function) — Format a token count for display (e.g. 128000 → '128K', 1048576 → '1M').
- L486 `_display_toolset_name(toolset_name: str)` (function) — Normalize internal/legacy toolset identifiers for banner display.
- L497 `build_welcome_banner(console: 'Console', model: str, cwd: str, tools: List[dict]=None, enabled_toolsets: List[str]=None, session_id: str=None, get_toolset_for_tool=None, context_length: int=None)` (function) — Build and print a welcome banner with caduceus on left and info on right.
