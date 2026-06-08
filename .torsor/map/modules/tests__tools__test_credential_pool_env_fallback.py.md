---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_credential_pool_env_fallback.py

Symbols in `tests/tools/test_credential_pool_env_fallback.py`.

- L17 `_make_pconfig(provider_id='deepseek', env_vars=None)` (function) — Create a minimal ProviderConfig for testing.
- L33 `isolated_hermes_home(tmp_path, monkeypatch)` (function) — Point HERMES_HOME at a temp dir and clear known API key env vars.
- L54 `_write_env_file(home: Path, **kwargs)` (function) — Write key=value pairs to ~/.hermes/.env.
- L60 `TestCredentialPoolSeedsFromDotEnv` (class) — _seed_from_env must read keys from ~/.hermes/.env, not just os.environ.
- L68 `test_deepseek_key_from_dotenv_only(self, isolated_hermes_home)` (method) — Key in .env but not os.environ → _seed_from_env adds a pool entry.
- L85 `test_openrouter_key_from_dotenv_only(self, isolated_hermes_home)` (method) — OpenRouter path has its own branch — verify it also reads .env.
- L100 `test_empty_dotenv_no_entries(self, isolated_hermes_home)` (method) — No .env file, no env vars → no entries seeded (and no crash).
- L111 `TestAuthResolvesFromDotEnv` (class) — _resolve_api_key_provider_secret must also read from ~/.hermes/.env.
- L114 `test_key_from_dotenv_only(self, isolated_hermes_home)` (method) — Key in .env but not os.environ → _resolve returns it with the env var source.
- L128 `TestAuthCredentialPoolFallback` (class) — _resolve_api_key_provider_secret falls back to credential pool when env + dotenv are empty.
- L131 `test_credential_pool_fallback_structure(self, isolated_hermes_home)` (method) — Empty env + empty .env → auth falls back to credential pool.
- L150 `test_credential_pool_empty_returns_empty(self, isolated_hermes_home)` (method) — Empty env + empty .env + empty pool → empty string.
- L163 `test_env_var_takes_priority_over_pool(self, isolated_hermes_home, monkeypatch)` (method) — os.environ key wins — credential pool is NEVER consulted.
- L181 `test_dotenv_takes_priority_over_pool(self, isolated_hermes_home)` (method) — Key in .env beats credential pool — pool only fires when both env sources are empty.
