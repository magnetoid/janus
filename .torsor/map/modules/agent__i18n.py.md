---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:40'
updated: '2026-06-08T00:38:40'
---

# agent/i18n.py

Symbols in `agent/i18n.py`.

- L88 `_locales_dir()` (function) — Return the directory containing locale YAML files.
- L141 `_normalize_lang(value: Any)` (function) — Normalize a user-supplied language value to a supported code.
- L165 `_load_catalog(lang: str)` (function) — Load and flatten one locale YAML file into a dotted-key dict.
- L200 `_flatten_into(node: Any, prefix: str, out: dict[str, str])` (function)
- L211 `_config_language_cached()` (function) — Read ``display.language`` from config.yaml once per process.
- L230 `reset_language_cache()` (function) — Invalidate cached language resolution and catalogs.
- L241 `get_language()` (function) — Resolve the active language using env > config > default order.
- L252 `t(key: str, lang: str | None=None, **format_kwargs: Any)` (function) — Translate a dotted key to the active language.
