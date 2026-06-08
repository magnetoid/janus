---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:42'
updated: '2026-06-08T00:38:42'
---

# tests/hermes_cli/test_config_env_expansion.py

Symbols in `tests/hermes_cli/test_config_env_expansion.py`.

- L7 `TestExpandEnvVars` (class)
- L8 `test_simple_substitution(self)` (method)
- L13 `test_missing_var_kept_verbatim(self)` (method)
- L18 `test_no_placeholder_unchanged(self)` (method)
- L21 `test_dict_recursive(self)` (method)
- L27 `test_nested_dict(self)` (method)
- L33 `test_list_items(self)` (method)
- L39 `test_non_string_values_untouched(self)` (method)
- L45 `test_multiple_placeholders_in_one_string(self)` (method)
- L51 `test_dict_keys_not_expanded(self)` (method)
- L58 `TestLoadConfigExpansion` (class)
- L59 `test_load_config_expands_env_vars(self, tmp_path, monkeypatch)` (method)
- L84 `test_load_config_unresolved_kept_verbatim(self, tmp_path, monkeypatch)` (method)
- L97 `TestLoadCliConfigExpansion` (class) — Verify that load_cli_config() also expands ${VAR} references.
- L100 `test_cli_config_expands_auxiliary_api_key(self, tmp_path, monkeypatch)` (method)
- L118 `test_cli_config_unresolved_kept_verbatim(self, tmp_path, monkeypatch)` (method)
