---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/run_agent/test_callable_api_key.py

Symbols in `tests/run_agent/test_callable_api_key.py`.

- L40 `TestCreateOpenAIClientCallable` (class) — ``AIAgent._create_openai_client`` must pass the callable through
- L44 `test_callable_api_key_passed_to_openai_constructor(self, monkeypatch)` (method) — Construct the smallest possible AIAgent surface and verify
- L91 `TestNormalizeMainRuntimePreservesCallable` (class) — The aux client orchestrator must keep the callable on the
- L96 `test_callable_api_key_survives_normalization(self)` (method)
- L113 `test_string_api_key_still_works(self)` (method)
- L121 `test_normalization_drops_empty_string_but_preserves_callable(self)` (method)
- L138 `test_unknown_field_dropped(self)` (method)
- L155 `TestTruncateTokenCallable` (class)
- L156 `test_callable_returns_placeholder(self)` (method) — Dashboard preview must render the Entra placeholder, NOT
- L172 `test_string_jwt_still_truncated_to_signature_tail(self)` (method)
- L178 `test_empty_returns_empty(self)` (method)
- L190 `TestRuntimeDictSerializationGuard` (class)
- L191 `test_json_dumps_default_str_does_not_silently_stringify_callable(self)` (method) — Sanity check: a runtime dict with a callable api_key must
- L218 `TestBatchRunnerCallableHandling` (class)
- L219 `test_callable_api_key_stripped_from_worker_config(self, capsys, monkeypatch, tmp_path)` (method) — ``BatchRunner._run_batches`` (or the equivalent code path)
- L244 `test_batch_runner_source_uses_the_correct_predicate(self)` (method) — Pin the predicate string in batch_runner so refactors that
- L263 `TestCliEnsureRuntimeCredentialsCallable` (class) — Regression: ``cli.py:_ensure_runtime_credentials`` previously
- L276 `test_callable_predicate_present_in_cli_runtime_validation(self)` (method)
- L289 `TestInlinedDisplayMasks` (class) — The masked-credential display sites are now inlined per-site (no
- L298 `test_run_agent_banner_uses_is_token_provider_guard(self)` (method) — The masked-banner sites live in ``agent/agent_init.py``
- L319 `test_cli_show_config_handles_callable(self)` (method) — ``cli.HermesCLI.show_config`` previously did
- L339 `test_mask_api_key_for_logs_handles_callable(self)` (method) — ``run_agent._mask_api_key_for_logs`` is called from the
- L359 `test_anthropic_401_diagnostic_handles_callable(self)` (method) — The Anthropic 401 diagnostic path lives in
