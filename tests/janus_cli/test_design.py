"""Design-token layer (janus_cli/design.py) — the single home of styling."""
import pytest

from janus_cli import design
from janus_cli.skin_engine import set_active_skin


@pytest.fixture(autouse=True)
def _reset_skin():
    set_active_skin("default")
    yield
    set_active_skin("default")


def test_tokens_resolve_from_active_skin(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    assert design.tok("accent") == "#E3A857"   # minimal default ui_accent
    assert design.tok("ok") == "#7CB87C"       # minimal default ui_ok


def test_tokens_empty_when_color_off(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: False)
    assert design.tok("accent") == ""
    assert design.tok("error") == ""


def test_unknown_token_is_empty_not_a_crash(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    assert design.tok("nonsense") == ""


def test_symbols_default_to_minimal_set(monkeypatch):
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.sym("activity") == "▸"
    assert design.sym("fail") == "✗"
    assert design.sym("gutter") == "▍"


def test_symbols_ascii_fallback(monkeypatch):
    monkeypatch.setattr(design, "_unicode_ok", lambda: False)
    assert design.sym("activity") == ">"
    assert design.sym("ok") == "ok"
    assert design.sym("rule") == "-"


def test_skin_can_override_symbols(monkeypatch):
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    from janus_cli.skin_engine import get_active_skin
    get_active_skin().symbols["activity"] = "→"
    assert design.sym("activity") == "→"


def test_layout_reads_active_skin():
    assert design.layout() == "open"
    set_active_skin("classic")
    assert design.layout() == "panel"


def test_styled_wraps_markup_only_when_colored(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    assert design.styled("hi", "accent") == "[#E3A857]hi[/]"
    assert design.styled("hi", "accent", bold=True) == "[bold #E3A857]hi[/]"
    monkeypatch.setattr(design, "_color_on", lambda: False)
    assert design.styled("hi", "accent") == "hi"


class _FakeStdout:
    def __init__(self, encoding):
        self.encoding = encoding


def test_unicode_ok_true_for_utf8(monkeypatch):
    monkeypatch.setattr(design.sys, "stdout", _FakeStdout("utf-8"))
    assert design._unicode_ok() is True


def test_unicode_ok_none_encoding_falls_back_to_utf8(monkeypatch):
    monkeypatch.setattr(design.sys, "stdout", _FakeStdout(None))
    assert design._unicode_ok() is True


def test_unicode_ok_false_for_cp1252(monkeypatch):
    monkeypatch.setattr(design.sys, "stdout", _FakeStdout("cp1252"))
    assert design._unicode_ok() is False


def test_unicode_ok_false_for_bogus_codec(monkeypatch):
    monkeypatch.setattr(design.sys, "stdout", _FakeStdout("not-a-codec"))
    assert design._unicode_ok() is False


def test_notices_carry_semantic_symbols(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.ok("saved").startswith("[#")          # colored
    assert "✓" in design.ok("saved") and "saved" in design.ok("saved")
    assert "!" in design.warn("careful")
    assert "✗" in design.error("broke")
    assert "●" in design.note("fyi")


def test_notices_plain_when_color_off(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: False)
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.error("broke") == "✗ broke"


def test_rule_and_header(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: False)
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    assert design.rule(10) == "─" * 10
    assert design.header("commands") == "commands"


def test_response_block_panel_layout_returns_panel():
    from rich.panel import Panel
    set_active_skin("classic")
    block = design.response_block(
        "body", label=" ⟡ Janus ", border_hex="#FFD700",
        text_hex="#FFF8DC", width=80)
    assert isinstance(block, Panel)
    assert block.title == "[#FFD700 bold] ⟡ Janus [/]"


def test_response_block_panel_layout_merges_attribution():
    from rich.panel import Panel
    set_active_skin("classic")
    block = design.response_block(
        "body", label=" ⟡ Janus ", border_hex="#FFD700",
        text_hex="#FFF8DC", width=80, attribution="(background #3)")
    assert isinstance(block, Panel)
    assert "(background #3)" in str(block.title)


def test_response_block_open_layout_uses_gutter(monkeypatch):
    from rich.console import Console
    monkeypatch.setattr(design, "layout", lambda: "open")
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    block = design.response_block(
        "hello world", label=" janus ", border_hex="#E3A857",
        text_hex="", width=60)
    con = Console(record=True, width=60, force_terminal=False)
    con.print(block)
    out = con.export_text()
    assert "▍" in out
    assert "hello world" in out
    assert "╭" not in out and "─" * 10 not in out   # no box frame


def test_gutter_block_prefixes_every_line(monkeypatch):
    from rich.console import Console
    monkeypatch.setattr(design, "_unicode_ok", lambda: True)
    con = Console(record=True, width=40, force_terminal=False)
    con.print(design.GutterBlock("line one\nline two"))
    out = con.export_text()
    lines = [l for l in out.splitlines() if l.strip()]
    assert all("▍" in l for l in lines)
