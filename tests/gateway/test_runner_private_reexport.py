"""Guard the gateway-runner extraction regression.

`from gateway.core import *` does NOT re-export underscore-prefixed names, so the
runner extraction silently dropped ~50 private helpers gateway.runner depends on,
crashing `janus gateway` with NameError at GatewayRunner construction. runner.py
re-exports them; these tests ensure they stay bound.
"""
import ast

import gateway.core as core
import gateway.runner as runner


def test_runner_reexports_core_private_helpers():
    # A few of the names the crash surfaced, plus the broad invariant below.
    for name in (
        "_weakref",
        "_gateway_runner_ref",
        "_resolve_gateway_model",
        "_load_gateway_runtime_config",
        "_load_gateway_config",
    ):
        assert hasattr(runner, name), f"gateway.runner is missing private helper {name!r}"


def test_no_private_core_name_used_by_runner_is_unbound():
    """Every private core symbol the runner references must resolve in runner."""
    core_private = {n for n in dir(core) if n.startswith("_") and not n.startswith("__")}
    src = open(runner.__file__, encoding="utf-8").read()
    used = {n.id for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Name)}
    missing = sorted(n for n in core_private if n in used and not hasattr(runner, n))
    assert missing == [], f"gateway.runner references unbound private core names: {missing}"


def test_gateway_runner_constructs_without_nameerror():
    try:
        gr = runner.GatewayRunner()
    except NameError as exc:  # the exact failure class this fix addresses
        raise AssertionError(f"GatewayRunner __init__ hit NameError: {exc}") from exc
    assert runner._gateway_runner_ref() is gr
