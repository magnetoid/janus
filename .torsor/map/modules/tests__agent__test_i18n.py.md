---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:41'
updated: '2026-06-08T00:38:41'
---

# tests/agent/test_i18n.py

Symbols in `tests/agent/test_i18n.py`.

- L16 `_load_raw(lang: str)` (function)
- L21 `_flatten(d, prefix='')` (function)
- L38 `test_all_locales_exist()` (function) — Every supported language must have a catalog file on disk.
- L45 `test_catalog_keys_match_english(lang: str)` (function) — Every non-English catalog must have exactly the same key set as English.
- L56 `test_catalog_placeholders_match_english(lang: str)` (function) — Every translated value must use the same {placeholder} tokens as English.
- L81 `test_normalize_lang_accepts_supported()` (function)
- L86 `test_normalize_lang_accepts_aliases()` (function)
- L100 `test_normalize_lang_unknown_falls_back()` (function)
- L106 `test_env_var_override(monkeypatch)` (function) — HERMES_LANGUAGE wins over config.
- L113 `test_env_var_normalized(monkeypatch)` (function)
- L119 `test_default_when_nothing_set(monkeypatch)` (function) — With no env var and no config override, falls back to English.
- L132 `test_t_explicit_lang()` (function)
- L139 `test_t_formats_placeholders()` (function)
- L144 `test_t_missing_key_returns_key()` (function) — A missing key returns its own path -- ugly but never crashes.
- L150 `test_t_missing_key_in_non_english_falls_back_to_english(tmp_path, monkeypatch)` (function) — If a key exists in English but not in the target locale, fall back.
- L167 `test_t_unknown_language_uses_english()` (function) — Unknown lang codes normalize to English, not to a key-path fallback.
- L178 `test_locales_dir_env_override_used_when_dir_exists(tmp_path, monkeypatch)` (function) — HERMES_BUNDLED_LOCALES wins when it points at a real directory.
- L186 `test_locales_dir_env_override_ignored_when_missing(tmp_path, monkeypatch)` (function) — A bogus HERMES_BUNDLED_LOCALES falls through to source/wheel resolution
- L196 `test_locales_dir_falls_back_to_data_scheme(tmp_path, monkeypatch)` (function) — When neither the env override nor a source-adjacent locales/ exists,
- L224 `test_t_resolves_real_string_in_source_checkout()` (function) — Sanity: in the test environment (a source checkout) t() must return a
