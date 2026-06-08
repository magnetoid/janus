---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:44'
updated: '2026-06-08T00:38:44'
---

# tools/environments/modal_utils.py

Symbols in `tools/environments/modal_utils.py`.

- L28 `PreparedModalExec` (class) — Normalized command data passed to a transport-specific exec runner.
- L38 `ModalExecStart` (class) — Transport response after starting an exec.
- L45 `wrap_modal_stdin_heredoc(command: str, stdin_data: str)` (function) — Append stdin as a shell heredoc for transports without stdin piping.
- L53 `wrap_modal_sudo_pipe(command: str, sudo_stdin: str)` (function) — Feed sudo via a shell pipe for transports without direct stdin piping.
- L58 `BaseModalExecutionEnvironment` (class) — Execution flow for the *managed* Modal transport (gateway-owned sandbox).
- L75 `execute(self, command: str, cwd: str='', *, timeout: int | None=None, stdin_data: str | None=None, rewrite_compound_background: bool=True)` (method)
- L151 `_before_execute(self)` (method) — Hook for backends that need pre-exec sync or validation.
- L155 `_prepare_modal_exec(self, command: str, *, cwd: str='', timeout: int | None=None, stdin_data: str | None=None)` (method)
- L182 `_result(self, output: str, returncode: int)` (method)
- L188 `_error_result(self, output: str)` (method)
- L191 `_timeout_result_for_modal(self, timeout: int)` (method)
- L195 `_start_modal_exec(self, prepared: PreparedModalExec)` (method) — Begin a transport-specific exec.
- L199 `_poll_modal_exec(self, handle: Any)` (method) — Return a final result dict when complete, else ``None``.
- L203 `_cancel_modal_exec(self, handle: Any)` (method) — Cancel or terminate the active transport exec.
