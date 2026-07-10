"""Classic-skin verbatim guards.

`classic` preserves the pre-redesign default look EXACTLY — these tests
intentionally pin exact strings (that pinning IS the feature: it guards the
"/skin classic restores the old look" promise, not implementation drift).
"""
from janus_cli.skin_engine import load_skin


def test_classic_exists_and_is_panel_layout_with_emoji():
    s = load_skin("classic")
    assert s.name == "classic"
    assert s.layout == "panel"
    assert s.emoji_tools is True


def test_classic_branding_matches_old_default_verbatim():
    s = load_skin("classic")
    assert s.get_branding("goodbye") == "Until next time. ⟡"
    assert s.get_branding("response_label") == " ⟡ Janus "
    assert s.get_branding("help_header") == "(^_^)? Available Commands"
    assert s.get_branding("prompt_symbol") == "❯"
    assert s.tool_prefix == "┊"


def test_classic_colors_match_old_default_verbatim():
    s = load_skin("classic")
    assert s.get_color("banner_title") == "#FFD700"
    assert s.get_color("banner_border") == "#CD7F32"
    assert s.get_color("ui_accent") == "#FFBF00"
    assert s.get_color("banner_text") == "#FFF8DC"


def test_classic_carries_the_kawaii_spinner():
    """The kawaii faces move INTO classic data so the display.py fallback can
    go minimal later without changing classic behavior."""
    s = load_skin("classic")
    assert "(⌐■_■)" in s.spinner.get("thinking_faces", [])
    assert "(｡◕‿◕｡)" in s.spinner.get("waiting_faces", [])
    assert "pondering" in s.spinner.get("thinking_verbs", [])
