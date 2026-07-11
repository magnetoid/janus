"""/help rendering: open layout is grouped/scannable; classic keeps its box."""
import pytest

from janus_cli.skin_engine import set_active_skin


@pytest.fixture()
def cli(monkeypatch):
    """A JanusCLI with output captured. Uses the real COMMAND registry."""
    import cli as cli_mod
    inst = object.__new__(cli_mod.JanusCLI)   # skip heavy __init__
    inst.enabled_toolsets = []
    monkeypatch.setattr(cli_mod.JanusCLI, "_command_available",
                        lambda self, c: True, raising=False)
    lines = []
    monkeypatch.setattr(cli_mod, "_cprint", lambda *a, **k: lines.append(" ".join(str(x) for x in a)))

    class _FakeConsole:
        def print(self, *a, **k):
            lines.append(" ".join(str(x) for x in a))
    monkeypatch.setattr(cli_mod, "ChatConsole", lambda *a, **k: _FakeConsole())
    return inst, lines


def test_open_help_has_no_ascii_box_and_lists_commands(cli):
    inst, lines = cli
    set_active_skin("default")
    inst.show_help()
    out = "\n".join(lines)
    assert "/help" in out
    assert "+----" not in out and "+-" not in out     # no ASCII box header
    assert "(^_^)?" not in out


def test_classic_help_keeps_the_boxed_header(cli):
    inst, lines = cli
    set_active_skin("classic")
    try:
        inst.show_help()
    finally:
        set_active_skin("default")
    out = "\n".join(lines)
    assert "(^_^)? Available Commands" in out


def test_open_show_tools_header_is_calm(cli, monkeypatch):
    import builtins
    import cli as cli_mod
    inst, lines = cli
    set_active_skin("default")
    monkeypatch.setattr(cli_mod, "get_tool_definitions",
                        lambda **k: [{"function": {"name": "terminal", "description": "Run a command."}}])
    monkeypatch.setattr(cli_mod, "get_toolset_for_tool", lambda n: "core", raising=False)
    monkeypatch.setattr(builtins, "print", lambda *a, **k: lines.append(" ".join(str(x) for x in a)))
    inst.show_tools()
    out = "\n".join(lines)
    assert "(^_^)/" not in out
    assert "terminal" in out
