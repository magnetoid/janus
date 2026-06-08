---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# hermes_cli/env_loader.py

Symbols in `hermes_cli/env_loader.py`.

- L42 `get_secret_source(env_var: str)` (function) — Return the label of the secret source that supplied ``env_var``, if any.
- L55 `reset_secret_source_cache()` (function) — Forget which HERMES_HOME paths have already had external secrets applied.
- L68 `format_secret_source_suffix(env_var: str)` (function) — Return a human-readable suffix like ``" (from Bitwarden)"`` or ``""``.
- L87 `_format_offending_chars(value: str, limit: int=3)` (function) — Return a compact 'U+XXXX ('c'), ...' summary of non-ASCII codepoints.
- L102 `_sanitize_loaded_credentials()` (function) — Strip non-ASCII characters from credential env vars in os.environ.
- L146 `_load_dotenv_with_fallback(path: Path, *, override: bool)` (function)
- L159 `_sanitize_env_file_if_needed(path: Path)` (function) — Pre-sanitize a .env file before python-dotenv reads it.
- L212 `load_hermes_dotenv(*, hermes_home: str | os.PathLike | None=None, project_env: str | os.PathLike | None=None)` (function) — Load Hermes environment files with user config taking precedence.
- L250 `_apply_external_secret_sources(home_path: Path)` (function) — Pull secrets from external sources (currently Bitwarden) into env.
- L326 `_load_secrets_config(home_path: Path)` (function) — Read just the ``secrets:`` section out of config.yaml.
