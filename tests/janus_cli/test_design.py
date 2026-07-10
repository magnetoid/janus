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
    assert design.tok("accent") == "#FFBF00"   # old default ui_accent (pre-flip)
    assert design.tok("ok") == "#4caf50"


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
    assert design.layout() == "panel"          # pre-flip default
    set_active_skin("classic")
    assert design.layout() == "panel"


def test_styled_wraps_markup_only_when_colored(monkeypatch):
    monkeypatch.setattr(design, "_color_on", lambda: True)
    assert design.styled("hi", "accent") == "[#FFBF00]hi[/]"
    assert design.styled("hi", "accent", bold=True) == "[bold #FFBF00]hi[/]"
    monkeypatch.setattr(design, "_color_on", lambda: False)
    assert design.styled("hi", "accent") == "hi"
