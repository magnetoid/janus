---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/website_policy.py

Symbols in `tools/website_policy.py`.

- L40 `_get_default_config_path()` (function)
- L44 `WebsitePolicyError` (class) — Raised when a website policy file is malformed.
- L48 `_normalize_host(host: str)` (function)
- L52 `_normalize_rule(rule: Any)` (function)
- L67 `_iter_blocklist_file_rules(path: Path)` (function) — Load rules from a shared blocklist file.
- L93 `_load_policy_config(config_path: Optional[Path]=None)` (function)
- L131 `load_website_blocklist(config_path: Optional[Path]=None)` (function) — Load and return the parsed website blocklist policy.
- L202 `invalidate_cache()` (function) — Force the next ``check_website_access`` call to re-read config.
- L209 `_match_host_against_rule(host: str, pattern: str)` (function)
- L217 `_extract_host_from_urlish(url: str)` (function)
- L232 `check_website_access(url: str, config_path: Optional[Path]=None)` (function) — Check whether a URL is allowed by the website blocklist policy.
