---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tests/tools/test_modal_sandbox_fixes.py

Symbols in `tests/tools/test_modal_sandbox_fixes.py`.

- L33 `TestToolResolution` (class) — Verify get_tool_definitions returns all expected tools for eval.
- L36 `test_terminal_and_file_toolsets_resolve_all_tools(self)` (method) — enabled_toolsets=['terminal', 'file'] should produce 6 tools.
- L47 `test_terminal_tool_present(self)` (method) — The terminal tool must be present (not silently dropped).
- L62 `TestCwdHandling` (class) — Verify host paths are sanitized for container backends.
- L65 `test_home_path_replaced_for_modal(self, monkeypatch)` (method) — TERMINAL_CWD=/home/user/... should be replaced with /root for modal.
- L75 `test_users_path_replaced_for_docker_by_default(self, monkeypatch)` (method) — Docker should keep host paths out of the sandbox unless explicitly enabled.
- L87 `test_users_path_maps_to_workspace_for_docker_when_enabled(self, monkeypatch)` (method) — Docker should map the host cwd into /workspace only when explicitly enabled.
- L97 `test_windows_path_replaced_for_modal(self, monkeypatch)` (method) — TERMINAL_CWD=C:\Users\... should be replaced for modal.
- L105 `test_default_cwd_is_root_for_container_backends(self, backend, monkeypatch)` (method) — Container backends should default to /root, not ~.
- L115 `test_docker_default_cwd_maps_current_directory_when_enabled(self, monkeypatch)` (method) — Docker should use /workspace when cwd mounting is explicitly enabled.
- L125 `test_local_backend_uses_getcwd(self, monkeypatch)` (method) — Local backend should use os.getcwd(), not /root.
- L132 `test_create_environment_passes_docker_host_cwd_and_flag(self, monkeypatch)` (method) — Docker host cwd and mount flag should reach DockerEnvironment.
- L157 `test_ssh_preserves_home_paths(self, monkeypatch)` (method) — SSH backend should NOT replace /home/ paths (they're valid remotely).
- L173 `TestEphemeralDiskCheck` (class) — Verify ephemeral_disk is only passed when modal supports it.
- L176 `test_ephemeral_disk_skipped_when_unsupported(self, monkeypatch)` (method) — If modal.Sandbox.create doesn't have ephemeral_disk param, skip it.
- L211 `TestModalEnvironmentDefaults` (class) — Verify ModalEnvironment has correct defaults.
- L214 `test_default_cwd_is_root(self)` (method) — ModalEnvironment default cwd should be /root, not ~.
- L230 `TestEnsurepipFix` (class) — Verify the pip fix is applied in the ModalEnvironment init.
- L233 `test_modal_environment_creates_image_with_setup_commands(self)` (method) — _resolve_modal_image should create a modal.Image with pip fix.
- L251 `test_modal_environment_uses_native_sdk(self)` (method) — ModalEnvironment should use Modal SDK directly, not swe-rex.
- L276 `TestHostPrefixList` (class) — Verify the host prefix list catches common host-only paths.
- L279 `test_all_common_host_prefixes_caught(self)` (method) — The host prefix check should catch /Users/, /home/, C:\, C:/.
