---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# utils.py

Symbols in `utils.py`.

- L20 `is_truthy_value(value: Any, default: bool=False)` (function) — Coerce bool-ish values using the project's shared truthy string set.
- L31 `env_var_enabled(name: str, default: str='')` (function) — Return True when an environment variable is set to a truthy value.
- L36 `_preserve_file_mode(path: Path)` (function) — Capture the permission bits of *path* if it exists, else ``None``.
- L44 `_restore_file_mode(path: Path, mode: 'int | None')` (function) — Re-apply *mode* to *path* after an atomic replace.
- L61 `atomic_replace(tmp_path: Union[str, Path], target: Union[str, Path])` (function) — Atomically move *tmp_path* onto *target*, preserving symlinks.
- L85 `atomic_json_write(path: Union[str, Path], data: Any, *, indent: int=2, mode: int | None=None, **dump_kwargs: Any)` (function) — Write JSON data to a file atomically.
- L154 `atomic_yaml_write(path: Union[str, Path], data: Any, *, default_flow_style: bool=False, sort_keys: bool=False, extra_content: str | None=None)` (function) — Write YAML data to a file atomically.
- L206 `atomic_roundtrip_yaml_update(path: Union[str, Path], key_path: str, value: Any)` (function) — Update one dotted YAML key while preserving comments and readable text.
- L273 `safe_json_loads(text: str, default: Any=None)` (function) — Parse JSON, returning *default* on any parse error.
- L289 `env_int(key: str, default: int=0)` (function) — Read an environment variable as an integer, with fallback.
- L300 `env_bool(key: str, default: bool=False)` (function) — Read an environment variable as a boolean.
- L314 `normalize_proxy_url(proxy_url: str | None)` (function) — Normalize proxy URLs for httpx/aiohttp compatibility.
- L329 `normalize_proxy_env_vars()` (function) — Rewrite supported proxy env vars to canonical URL forms in-place.
- L341 `base_url_hostname(base_url: str)` (function) — Return the lowercased hostname for a base URL, or ``""`` if absent.
- L358 `base_url_host_matches(base_url: str, domain: str)` (function) — Return True when the base URL's hostname is ``domain`` or a subdomain.
