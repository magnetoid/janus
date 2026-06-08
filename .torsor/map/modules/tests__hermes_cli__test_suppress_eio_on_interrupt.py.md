---
type: map
status: derived
tags:
- map
links: []
created: '2026-06-08T00:38:43'
updated: '2026-06-08T00:38:43'
---

# tests/hermes_cli/test_suppress_eio_on_interrupt.py

Symbols in `tests/hermes_cli/test_suppress_eio_on_interrupt.py`.

- L25 `_make_suppress_fn()` (function) — Build a standalone copy of ``_suppress_closed_loop_errors``.
- L44 `TestSuppressClosedLoopErrors` (class) — Verify the asyncio exception handler suppresses expected errors.
- L47 `test_suppresses_event_loop_closed(self)` (method)
- L53 `test_suppresses_key_not_registered(self)` (method)
- L59 `test_suppresses_oserror_eio(self)` (method) — OSError with errno.EIO must be suppressed (#13710).
- L67 `test_does_not_suppress_oserror_other_errno(self)` (method) — OSError with a different errno must still propagate.
- L75 `test_does_not_suppress_unrelated_exception(self)` (method) — Unrelated exceptions must still propagate.
- L82 `test_no_exception_key(self)` (method) — Context without 'exception' must propagate to default handler.
- L94 `TestOuterExceptEIO` (class) — Verify the outer ``except (KeyError, OSError)`` block logic.
- L97 `test_eio_does_not_reraise(self)` (method) — OSError with errno.EIO should be silently suppressed.
- L104 `test_bad_file_descriptor_matches(self)` (method) — 'Bad file descriptor' string should be caught.
- L109 `test_other_oserror_reraises(self)` (method) — Other OSError variants must not match the EIO guard.
- L137 `_make_signal_handler(logger, agent_state)` (function) — Build a standalone copy of ``_signal_handler``.
- L160 `TestSignalHandlerLoggingRace` (class) — #13710 regression — logger.debug in signal handler must not escape.
- L169 `test_keyboard_interrupt_raised_on_normal_path(self)` (method) — Sanity: handler raises KeyboardInterrupt when logging works.
- L177 `test_keyboard_interrupt_raised_when_logger_raises_keyerror(self)` (method) — logger.debug raising KeyError(10) must not escape — KeyboardInterrupt wins.
- L192 `test_keyboard_interrupt_raised_when_logger_raises_generic(self)` (method) — Any Exception from logger.debug must be swallowed by the guard.
- L200 `test_agent_interrupt_still_fires_when_logger_raises(self)` (method) — Even if logger.debug blows up, the agent interrupt must still run.
- L214 `test_agent_interrupt_failure_also_does_not_escape(self)` (method) — Defense-in-depth: agent.interrupt() raising must not escape either.
- L223 `test_base_exception_from_logger_is_not_swallowed(self)` (method) — BaseException (e.g. SystemExit) must still propagate — only Exception is caught.
