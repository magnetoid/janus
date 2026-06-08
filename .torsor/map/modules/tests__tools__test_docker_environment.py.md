---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/tools/test_docker_environment.py

Symbols in `tests/tools/test_docker_environment.py`.

- L10 `_mock_subprocess_run(monkeypatch)` (function) — Mock subprocess.run to intercept docker run -d and docker version calls.
- L30 `_make_dummy_env(**kwargs)` (function) — Helper to construct DockerEnvironment with minimal required args.
- L51 `test_ensure_docker_available_logs_and_raises_when_not_found(monkeypatch, caplog)` (function) — When docker cannot be found, raise a clear error before container setup.
- L73 `test_ensure_docker_available_logs_and_raises_on_timeout(monkeypatch, caplog)` (function) — When docker version times out, surface a helpful error instead of hanging.
- L93 `test_ensure_docker_available_uses_resolved_executable(monkeypatch)` (function) — When docker is found outside PATH, preflight should use that resolved path.
- L116 `test_auto_mount_host_cwd_adds_volume(monkeypatch, tmp_path)` (function) — Opt-in docker cwd mounting should bind the host cwd to /workspace.
- L137 `test_auto_mount_disabled_by_default(monkeypatch, tmp_path)` (function) — Host cwd should not be mounted unless the caller explicitly opts in.
- L157 `test_auto_mount_skipped_when_workspace_already_mounted(monkeypatch, tmp_path)` (function) — Explicit user volumes for /workspace should take precedence over cwd mount.
- L181 `test_auto_mount_replaces_persistent_workspace_bind(monkeypatch, tmp_path)` (function) — Persistent mode should still prefer the configured host cwd at /workspace.
- L204 `test_non_persistent_cleanup_removes_container(monkeypatch)` (function) — When persist_across_processes=false, cleanup() must docker stop AND
- L244 `_FakePopen` (class)
- L245 `__init__(self, cmd, **kwargs)` (method)
- L252 `poll(self)` (method)
- L256 `_make_execute_only_env(forward_env=None)` (function)
- L277 `test_init_env_args_uses_hermes_dotenv_for_allowlisted_env(monkeypatch)` (function) — _build_init_env_args picks up forwarded env vars from .env file at init time.
- L292 `test_init_env_args_prefers_shell_env_over_hermes_dotenv(monkeypatch)` (function) — Shell env vars take priority over .env file values in init env args.
- L306 `test_init_env_args_uses_hermes_dotenv_for_empty_shell_env(monkeypatch)` (function) — A transient empty-string in the live env must fall back to .env, not win.
- L326 `test_init_env_args_never_forwards_blank_secret(monkeypatch)` (function) — A legitimately-empty key with no disk value is not forwarded as -e KEY=.
- L343 `test_docker_env_appears_in_run_command(monkeypatch)` (function) — Explicit docker_env values should be passed via -e at docker run time.
- L358 `test_docker_env_appears_in_init_env_args(monkeypatch)` (function) — Explicit docker_env values should appear in _build_init_env_args.
- L369 `test_forward_env_overrides_docker_env_in_init_args(monkeypatch)` (function) — docker_forward_env should override docker_env for the same key.
- L384 `test_docker_env_and_forward_env_merge_in_init_args(monkeypatch)` (function) — docker_env and docker_forward_env with different keys should both appear.
- L400 `test_normalize_env_dict_filters_invalid_keys()` (function) — _normalize_env_dict should reject invalid variable names.
- L412 `test_normalize_env_dict_coerces_scalars()` (function) — _normalize_env_dict should coerce int/float/bool to str.
- L422 `test_normalize_env_dict_rejects_non_dict()` (function) — _normalize_env_dict should return empty dict for non-dict input.
- L429 `test_normalize_env_dict_rejects_complex_values()` (function) — _normalize_env_dict should reject list/dict values.
- L439 `test_security_args_include_setuid_setgid_for_privdrop(monkeypatch)` (function) — The default (run_as_host_user=False) invocation must include SETUID and
- L474 `test_run_as_host_user_passes_uid_gid(monkeypatch)` (function) — With run_as_host_user=True, --user <uid>:<gid> is added to docker run.
- L495 `test_run_as_host_user_drops_setuid_setgid_caps(monkeypatch)` (function) — When --user is passed, the container already starts unprivileged and
- L526 `test_run_as_host_user_default_off(monkeypatch)` (function) — Without the opt-in, no --user flag is emitted — preserving existing behavior.
- L540 `test_run_as_host_user_warns_and_skips_when_no_posix_ids(monkeypatch, caplog)` (function) — On platforms without POSIX getuid/getgid, log a warning and leave the
- L573 `_run_args_from_calls(calls)` (function) — Pull the argv list passed to the first ``docker run`` invocation.
- L583 `_labels_in_run_args(run_args)` (function) — Return the set of ``key=value`` strings passed via ``--label``.
- L592 `test_run_command_tags_hermes_agent_label(monkeypatch)` (function) — Every container hermes-agent starts must carry the hermes-agent=1 label
- L608 `test_run_command_tags_task_and_profile_labels(monkeypatch)` (function) — task_id and the active profile name are surfaced as labels so future
- L628 `test_label_sanitizer_rejects_invalid_characters()` (function) — Docker label values must be alnum + ``_.-`` and ≤63 chars. Profile or
- L644 `test_run_command_sanitizes_unsafe_task_id(monkeypatch)` (function) — A task_id containing characters Docker rejects in label values must be
- L661 `test_labels_attribute_populated_after_init(monkeypatch)` (function) — ``self._labels`` must be set to the same key/value pairs that went onto
- L681 `_mock_subprocess_run_with_reuse(monkeypatch, ps_state: str | None, start_succeeds: bool=True)` (function) — Reuse-aware subprocess.run mock.
- L723 `test_reuse_attaches_to_running_container_without_docker_run(monkeypatch)` (function) — When a labeled container is already ``running``, the reuse probe
- L750 `test_reuse_starts_stopped_container_before_attaching(monkeypatch)` (function) — A labeled container in ``exited`` state must be restarted via
- L768 `test_reuse_falls_back_to_fresh_run_when_start_fails(monkeypatch)` (function) — If ``docker start`` on the matched container fails (container was
- L790 `test_failed_docker_run_cleans_up_orphaned_container(monkeypatch)` (function) — When ``docker run`` fails (e.g. exit 125), the partially-created
- L833 `test_docker_run_timeout_cleans_up_orphaned_container(monkeypatch)` (function) — When ``docker run`` times out (e.g. slow image pull), the
- L868 `test_no_reuse_when_persist_across_processes_disabled(monkeypatch)` (function) — Opt-out path: ``persist_across_processes=False`` skips the ps probe
- L891 `test_find_reusable_container_prefers_running_over_stopped(monkeypatch)` (function) — When the probe returns multiple matches (shouldn't normally happen,
- L923 `_FakeThread` (class) — Stand-in for threading.Thread that captures target/args and calls
- L928 `__init__(self, target=None, daemon=None, name=None)` (method)
- L934 `start(self)` (method)
- L939 `is_alive(self)` (method)
- L942 `join(self, timeout=None)` (method)
- L946 `_install_fake_thread(monkeypatch)` (function)
- L951 `test_cleanup_with_persist_is_noop_for_container(monkeypatch)` (function) — ``persist_across_processes=True`` (default) cleanup must NEITHER stop
- L1000 `test_cleanup_force_remove_stops_and_rms_even_in_persist_mode(monkeypatch)` (function) — ``cleanup(force_remove=True)`` must stop AND rm the container even
- L1035 `test_cleanup_vm_default_honors_persist_mode(monkeypatch)` (function) — ``cleanup_vm(task_id)`` without ``force_remove=True`` must be a no-op
- L1083 `test_cleanup_vm_force_remove_tears_down_persist_container(monkeypatch)` (function) — ``cleanup_vm(task_id, force_remove=True)`` tears down a persist-mode
- L1120 `test_cleanup_with_persist_disabled_stops_and_rms(monkeypatch)` (function) — ``persist_across_processes=False`` cleanup must docker stop AND docker
- L1160 `test_cleanup_uses_subprocess_run_not_detached_shell(monkeypatch)` (function) — The pre-fix code used ``subprocess.Popen("... &", shell=True)`` which
- L1188 `test_wait_for_cleanup_returns_true_when_no_thread_started()` (function) — ``wait_for_cleanup`` must be a no-op when ``cleanup`` was never called
- L1198 `test_wait_for_cleanup_after_cleanup_returns_true(monkeypatch)` (function) — End-to-end: cleanup() starts a thread, wait_for_cleanup() joins it
- L1218 `test_cleanup_on_env_with_no_container_id_does_not_raise(monkeypatch)` (function) — A DockerEnvironment whose ``__init__`` failed before the container_id
- L1236 `_now_iso(offset_seconds: int=0)` (function) — Return an RFC3339 timestamp ``offset_seconds`` in the past.
- L1244 `_reaper_run_mock(monkeypatch, ps_ids: list[str], inspect_responses: dict[str, str], rm_succeeds: bool=True)` (function) — Build a subprocess.run mock for reaper tests.
- L1283 `test_reap_orphan_returns_zero_when_no_matches(monkeypatch)` (function) — No labeled containers → no rm calls, returns 0. Establishes the
- L1297 `test_reap_orphan_removes_stale_exited_container(monkeypatch)` (function) — An Exited container older than max_age_seconds must be removed.
- L1316 `test_reap_orphan_spares_recently_exited_container(monkeypatch)` (function) — A container exited within max_age_seconds must NOT be reaped — that
- L1335 `test_reap_orphan_scopes_to_profile_filter_via_label(monkeypatch)` (function) — The reaper must pass ``--filter label=hermes-profile=<profile>`` to
- L1360 `test_reap_orphan_skips_container_with_unparseable_finished_at(monkeypatch)` (function) — If docker inspect returns the zero-value ``0001-01-01T00:00:00Z`` (no
- L1385 `test_reap_orphan_handles_docker_ps_failure_gracefully(monkeypatch)` (function) — If docker ps itself fails (daemon down, permission denied), the
- L1403 `test_reap_orphan_continues_after_individual_rm_failure(monkeypatch)` (function) — If ``docker rm -f`` fails on one container (already removed by a
- L1441 `test_container_finished_at_parses_nanosecond_timestamp(monkeypatch)` (function) — Docker emits FinishedAt with nanosecond precision (RFC3339 with up to
- L1463 `test_container_finished_at_returns_none_on_zero_value()` (function) — Docker's zero-value ``0001-01-01T00:00:00Z`` (never finished) must
- L1484 `test_credential_mount_skipped_when_source_is_directory(monkeypatch, tmp_path, caplog)` (function) — Credential mount should be skipped when source path is a directory.
- L1531 `test_credential_mount_skipped_when_source_missing(monkeypatch, tmp_path, caplog)` (function) — Credential mount should be skipped when source file no longer exists.
- L1569 `test_credential_mount_works_when_source_is_valid_file(monkeypatch, tmp_path)` (function) — Credential mount should proceed normally when source is a valid file.
- L1604 `_mock_subprocess_run_with_entrypoint(monkeypatch, entrypoint_json)` (function) — Like _mock_subprocess_run, but `docker image inspect` returns the given
- L1625 `test_image_uses_init_entrypoint_detects_s6_init(monkeypatch)` (function) — An image whose entrypoint is /init is detected as an s6-overlay image.
- L1634 `test_image_uses_init_entrypoint_false_for_plain_image(monkeypatch)` (function) — A normal image (no /init entrypoint) is not treated as s6-overlay.
- L1643 `test_image_uses_init_entrypoint_false_for_null_entrypoint(monkeypatch)` (function) — Images with no declared entrypoint (null) keep hardened defaults.
- L1652 `test_image_uses_init_entrypoint_false_on_inspect_failure(monkeypatch)` (function) — An inspect failure (e.g. image not pulled) is best-effort -> defaults kept.
- L1661 `test_image_uses_init_entrypoint_false_on_exception(monkeypatch)` (function) — A subprocess error never raises out of detection — defaults kept.
- L1670 `test_s6_image_skips_docker_init_and_mounts_run_exec(monkeypatch)` (function) — For an s6-overlay /init image, docker run must omit --init and mount
- L1692 `test_plain_image_keeps_docker_init_and_run_noexec(monkeypatch)` (function) — A non-s6 image keeps the hardened defaults: Docker --init and noexec /run.
- L1718 `test_is_container_gone_matches_removal_errors(monkeypatch)` (function) — ``_is_container_gone`` recognizes the docker errors that mean the
- L1744 `test_execute_recovers_from_out_of_band_removal(monkeypatch)` (function) — When a persistent container is removed out-of-band, ``execute`` detects
- L1784 `test_execute_does_not_recover_when_not_persistent(monkeypatch)` (function) — A non-persistent session must NOT trigger container recreation on a
- L1811 `test_execute_does_not_recover_on_ordinary_failure(monkeypatch)` (function) — A genuine non-zero exit that is NOT a container-gone error must pass
