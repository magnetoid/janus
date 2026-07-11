"""Tests for janus_cli.skin_engine — the data-driven skin/theme system."""

import pytest


@pytest.fixture(autouse=True)
def reset_skin_state():
    """Reset skin engine state between tests."""
    from janus_cli import skin_engine
    skin_engine._active_skin = None
    skin_engine._active_skin_name = "default"
    yield
    skin_engine._active_skin = None
    skin_engine._active_skin_name = "default"


class TestSkinConfig:
    def test_default_skin_has_required_fields(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("default")
        assert skin.name == "default"
        assert skin.tool_prefix == "▸"
        assert "banner_title" in skin.colors
        assert "banner_border" in skin.colors
        assert "agent_name" in skin.branding

    def test_get_color_with_fallback(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("default")
        assert skin.get_color("banner_title") == "#E3A857"
        assert skin.get_color("nonexistent", "#000") == "#000"

    def test_get_branding_with_fallback(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("default")
        assert skin.get_branding("agent_name") == "janus"
        assert skin.get_branding("nonexistent", "fallback") == "fallback"

    def test_get_spinner_wings_empty_for_default(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("default")
        assert skin.get_spinner_wings() == []


class TestBuiltinSkins:
    def test_ares_skin_loads(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("ares")
        assert skin.name == "ares"
        assert skin.tool_prefix == "╎"
        assert skin.get_color("banner_border") == "#9F1C1C"
        assert skin.get_color("response_border") == "#C7A96B"
        assert skin.get_color("session_label") == "#C7A96B"
        assert skin.get_color("session_border") == "#6E584B"
        assert skin.get_branding("agent_name") == "Ares Agent"

    def test_ares_has_spinner_customization(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("ares")
        wings = skin.get_spinner_wings()
        assert len(wings) > 0
        assert isinstance(wings[0], tuple)
        assert len(wings[0]) == 2

    def test_mono_skin_loads(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("mono")
        assert skin.name == "mono"
        assert skin.get_color("banner_title") == "#e6edf3"

    def test_slate_skin_loads(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("slate")
        assert skin.name == "slate"
        assert skin.get_color("banner_title") == "#7eb8f6"

    def test_daylight_skin_loads(self):
        from janus_cli.skin_engine import load_skin

        skin = load_skin("daylight")
        assert skin.name == "daylight"
        assert skin.tool_prefix == "│"
        assert skin.get_color("banner_title") == "#0F172A"
        assert skin.get_color("status_bar_bg") == "#E5EDF8"
        assert skin.get_color("voice_status_bg") == "#E5EDF8"
        assert skin.get_color("completion_menu_bg") == "#F8FAFC"
        assert skin.get_color("completion_menu_current_bg") == "#DBEAFE"
        assert skin.get_color("completion_menu_meta_bg") == "#EEF2FF"
        assert skin.get_color("completion_menu_meta_current_bg") == "#BFDBFE"

    def test_warm_lightmode_skin_loads(self):
        from janus_cli.skin_engine import load_skin

        skin = load_skin("warm-lightmode")
        assert skin.name == "warm-lightmode"
        assert skin.get_color("banner_text") == "#2C1810"
        assert skin.get_color("completion_menu_bg") == "#F5EFE0"

    @pytest.mark.parametrize(
        "skin_name,expected_status_bar_text",
        [
            ("daylight", "#111827"),
            ("warm-lightmode", "#2C1810"),
        ],
    )
    def test_light_skins_define_own_status_bar_text(self, skin_name, expected_status_bar_text):
        """Light skins must not inherit the default skin's dark status-bar text.

        The default skin's status_bar_text (#B8B8B8) is tuned for a dark
        (#1C1C1C) status bar background and is unreadable on light
        backgrounds. Light skins must define their own explicit value.
        """
        from janus_cli.skin_engine import load_skin

        default_skin = load_skin("default")
        assert default_skin.get_color("status_bar_text") == "#B8B8B8"

        skin = load_skin(skin_name)
        assert skin.get_color("status_bar_text") != default_skin.get_color("status_bar_text")
        assert skin.get_color("status_bar_text") == expected_status_bar_text

    def test_charizard_skin_has_dark_ember_completion_menu(self):
        from janus_cli.skin_engine import load_skin

        skin = load_skin("charizard")
        assert skin.name == "charizard"
        assert skin.get_color("banner_dim") == "#C58A45"
        assert skin.get_color("completion_menu_bg") == "#0B0503"
        assert skin.get_color("completion_menu_current_bg") == "#4A1B07"
        assert skin.get_color("completion_menu_meta_bg") == "#120806"
        assert skin.get_color("completion_menu_meta_current_bg") == "#5A260D"
        assert skin.get_color("selection_bg") == "#5A260D"

    def test_unknown_skin_falls_back_to_default(self):
        from janus_cli.skin_engine import load_skin
        skin = load_skin("nonexistent_skin_xyz")
        assert skin.name == "default"

    def test_all_builtin_skins_have_complete_colors(self):
        from janus_cli.skin_engine import _BUILTIN_SKINS, _build_skin_config
        required_keys = ["banner_border", "banner_title", "banner_accent",
                         "banner_dim", "banner_text", "ui_accent"]
        for name, data in _BUILTIN_SKINS.items():
            skin = _build_skin_config(data)
            for key in required_keys:
                assert key in skin.colors, f"Skin '{name}' missing color '{key}'"


class TestSkinManagement:
    def test_set_active_skin(self):
        from janus_cli.skin_engine import set_active_skin, get_active_skin, get_active_skin_name
        skin = set_active_skin("ares")
        assert skin.name == "ares"
        assert get_active_skin_name() == "ares"
        assert get_active_skin().name == "ares"

    def test_get_active_skin_defaults(self):
        from janus_cli.skin_engine import get_active_skin
        skin = get_active_skin()
        assert skin.name == "default"

    def test_list_skins_includes_builtins(self):
        from janus_cli.skin_engine import list_skins
        skins = list_skins()
        names = [s["name"] for s in skins]
        assert "default" in names
        assert "ares" in names
        assert "mono" in names
        assert "slate" in names
        assert "daylight" in names
        assert "warm-lightmode" in names
        for s in skins:
            assert "source" in s
            assert s["source"] == "builtin"

    def test_init_skin_from_config(self):
        from janus_cli.skin_engine import init_skin_from_config, get_active_skin_name
        init_skin_from_config({"display": {"skin": "ares"}})
        assert get_active_skin_name() == "ares"

    def test_init_skin_from_empty_config(self):
        from janus_cli.skin_engine import init_skin_from_config, get_active_skin_name
        init_skin_from_config({})
        assert get_active_skin_name() == "default"

    def test_init_skin_from_null_display(self):
        """display: null should fall back to default, not crash."""
        from janus_cli.skin_engine import init_skin_from_config, get_active_skin_name
        init_skin_from_config({"display": None})
        assert get_active_skin_name() == "default"

    def test_init_skin_from_non_dict_display(self):
        """display: <non-dict> should fall back to default."""
        from janus_cli.skin_engine import init_skin_from_config, get_active_skin_name
        init_skin_from_config({"display": "invalid"})
        assert get_active_skin_name() == "default"

        init_skin_from_config({"display": 42})
        assert get_active_skin_name() == "default"

        init_skin_from_config({"display": []})
        assert get_active_skin_name() == "default"


class TestUserSkins:
    def test_load_user_skin_from_yaml(self, tmp_path, monkeypatch):
        from janus_cli.skin_engine import load_skin
        # Create a user skin YAML
        skins_dir = tmp_path / "skins"
        skins_dir.mkdir()
        skin_file = skins_dir / "custom.yaml"
        skin_data = {
            "name": "custom",
            "description": "A custom test skin",
            "colors": {"banner_title": "#FF0000"},
            "branding": {"agent_name": "Custom Agent"},
            "tool_prefix": "▸",
        }
        import yaml
        skin_file.write_text(yaml.dump(skin_data))

        # Patch skins dir
        monkeypatch.setattr("janus_cli.skin_engine._skins_dir", lambda: skins_dir)

        skin = load_skin("custom")
        assert skin.name == "custom"
        assert skin.get_color("banner_title") == "#FF0000"
        assert skin.get_branding("agent_name") == "Custom Agent"
        assert skin.tool_prefix == "▸"
        # Should inherit defaults for unspecified colors
        assert skin.get_color("banner_border") == "#5C5C5C"  # from default

    def test_load_user_skin_invalid_section_types_fall_back_to_defaults(self, tmp_path, monkeypatch):
        from janus_cli.skin_engine import load_skin

        skins_dir = tmp_path / "skins"
        skins_dir.mkdir()
        import yaml

        (skins_dir / "broken.yaml").write_text(
            yaml.dump(
                {
                    "name": "broken",
                    "colors": ["not", "a", "mapping"],
                    "spinner": "invalid",
                    "branding": ["also", "invalid"],
                    "tool_emojis": ["invalid"],
                    "tool_prefix": "!",
                }
            ),
            encoding="utf-8",
        )
        monkeypatch.setattr("janus_cli.skin_engine._skins_dir", lambda: skins_dir)

        skin = load_skin("broken")

        assert skin.name == "broken"
        assert skin.get_color("banner_title") == "#E3A857"
        assert skin.get_branding("agent_name") == "janus"
        assert skin.spinner.get("waiting_faces", []) == []
        assert skin.tool_emojis == {}
        assert skin.tool_prefix == "!"

    def test_list_skins_includes_user_skins(self, tmp_path, monkeypatch):
        from janus_cli.skin_engine import list_skins
        skins_dir = tmp_path / "skins"
        skins_dir.mkdir()
        import yaml
        (skins_dir / "pirate.yaml").write_text(yaml.dump({
            "name": "pirate",
            "description": "Arr matey",
        }))
        monkeypatch.setattr("janus_cli.skin_engine._skins_dir", lambda: skins_dir)

        skins = list_skins()
        names = [s["name"] for s in skins]
        assert "pirate" in names
        pirate = [s for s in skins if s["name"] == "pirate"][0]
        assert pirate["source"] == "user"


class TestDisplayIntegration:
    def test_get_skin_tool_prefix_default(self):
        from agent.display import get_skin_tool_prefix
        assert get_skin_tool_prefix() == "▸"

    def test_get_skin_tool_prefix_custom(self):
        from janus_cli.skin_engine import set_active_skin
        from agent.display import get_skin_tool_prefix
        set_active_skin("ares")
        assert get_skin_tool_prefix() == "╎"

    def test_tool_message_uses_skin_prefix_classic(self):
        """``tool_prefix`` substitution is a classic-only (emoji_tools=True)
        mechanism [redesign 3.1]: pin to a classic-family skin so this stays
        a guard on that legacy substitution, not on ares's minimal-mode mark."""
        from janus_cli.skin_engine import set_active_skin
        from agent.display import get_cute_tool_message
        set_active_skin("classic")
        msg = get_cute_tool_message("terminal", {"command": "ls"}, 0.5)
        assert msg.startswith("┊")

    def test_tool_message_minimal_mode_ignores_custom_tool_prefix(self):
        """ares has emoji_tools=False (inherited from default), so its tool
        lines use the uniform minimal mark, not its custom tool_prefix
        [redesign 3.1]. ``get_skin_tool_prefix()`` itself still returns the
        skin's own prefix (see test_get_skin_tool_prefix_custom above); it's
        just no longer consulted for minimal-mode tool lines."""
        from janus_cli.skin_engine import set_active_skin
        from agent.display import get_cute_tool_message
        set_active_skin("ares")
        msg = get_cute_tool_message("terminal", {"command": "ls"}, 0.5)
        assert msg.startswith("▸")
        assert "╎" not in msg
        assert "┊" not in msg

    def test_tool_message_default_prefix(self):
        from agent.display import get_cute_tool_message
        msg = get_cute_tool_message("terminal", {"command": "ls"}, 0.5)
        assert msg.startswith("▸")


class TestCliBrandingHelpers:
    def test_active_prompt_symbol_default(self):
        from janus_cli.skin_engine import get_active_prompt_symbol

        assert get_active_prompt_symbol() == "❯ "

    def test_active_prompt_symbol_ares(self):
        from janus_cli.skin_engine import set_active_skin, get_active_prompt_symbol

        set_active_skin("ares")
        assert get_active_prompt_symbol() == "⚔ "

    def test_active_help_header_ares(self):
        from janus_cli.skin_engine import set_active_skin, get_active_help_header

        set_active_skin("ares")
        assert get_active_help_header() == "(⚔) Available Commands"

    def test_active_goodbye_ares(self):
        from janus_cli.skin_engine import set_active_skin, get_active_goodbye

        set_active_skin("ares")
        assert get_active_goodbye() == "Farewell, warrior! ⚔"

    def test_prompt_toolkit_style_overrides_cover_tui_classes(self):
        from janus_cli.skin_engine import set_active_skin, get_prompt_toolkit_style_overrides
        set_active_skin("ares")
        overrides = get_prompt_toolkit_style_overrides()
        required = {
            "input-area",
            "placeholder",
            "prompt",
            "prompt-working",
            "hint",
            "status-bar",
            "status-bar-strong",
            "status-bar-dim",
            "status-bar-good",
            "status-bar-warn",
            "status-bar-bad",
            "status-bar-critical",
            "input-rule",
            "image-badge",
            "completion-menu",
            "completion-menu.completion",
            "completion-menu.completion.current",
            "completion-menu.meta.completion",
            "completion-menu.meta.completion.current",
            "status-bar",
            "status-bar-strong",
            "status-bar-dim",
            "status-bar-good",
            "status-bar-warn",
            "status-bar-bad",
            "status-bar-critical",
            "voice-status",
            "voice-status-recording",
            "clarify-border",
            "clarify-title",
            "clarify-question",
            "clarify-choice",
            "clarify-selected",
            "clarify-active-other",
            "clarify-countdown",
            "sudo-prompt",
            "sudo-border",
            "sudo-title",
            "sudo-text",
            "approval-border",
            "approval-title",
            "approval-desc",
            "approval-cmd",
            "approval-choice",
            "approval-selected",
        }
        assert required.issubset(overrides.keys())

    def test_prompt_toolkit_style_overrides_use_skin_colors(self):
        from janus_cli.skin_engine import (
            set_active_skin,
            get_active_skin,
            get_prompt_toolkit_style_overrides,
        )

        set_active_skin("ares")
        skin = get_active_skin()
        overrides = get_prompt_toolkit_style_overrides()
        assert overrides["prompt"] == skin.get_color("prompt")
        assert overrides["input-rule"] == skin.get_color("input_rule")
        assert overrides["status-bar"] == (
            f"bg:{skin.get_color('status_bar_bg')} {skin.get_color('status_bar_text')}"
        )
        assert overrides["status-bar-strong"] == (
            f"bg:{skin.get_color('status_bar_bg')} {skin.get_color('status_bar_strong')} bold"
        )
        assert overrides["status-bar-critical"] == (
            f"bg:{skin.get_color('status_bar_bg')} {skin.get_color('status_bar_critical')} bold"
        )
        assert overrides["clarify-title"] == f"{skin.get_color('banner_title')} bold"
        assert overrides["sudo-prompt"] == f"{skin.get_color('ui_error')} bold"
        assert overrides["approval-title"] == f"{skin.get_color('ui_warn')} bold"

        set_active_skin("daylight")
        skin = get_active_skin()
        overrides = get_prompt_toolkit_style_overrides()
        # daylight defines its own light-appropriate status_bar_text so it no
        # longer inherits the minimal default's dark-background value.
        assert overrides["status-bar"] == f"bg:{skin.get_color('status_bar_bg')} {skin.get_color('status_bar_text')}"
        assert overrides["voice-status"] == f"bg:{skin.get_color('voice_status_bg')} {skin.get_color('ui_label')}"


class TestSchemaAdditions:
    """Increment-1 schema fields: symbols / layout / emoji_tools (all optional)."""

    def test_new_fields_have_safe_defaults(self):
        from janus_cli.skin_engine import SkinConfig
        s = SkinConfig(name="x")
        assert s.symbols == {}
        assert s.layout == "panel"          # behavior-preserving until the flip
        assert s.emoji_tools is True
        assert s.get_symbol("activity", "▸") == "▸"

    def test_build_config_passes_fields_through(self):
        from janus_cli.skin_engine import _build_skin_config
        cfg = _build_skin_config({
            "name": "t", "symbols": {"activity": "→"},
            "layout": "open", "emoji_tools": False,
        })
        assert cfg.get_symbol("activity", "x") == "→"
        assert cfg.layout == "open"
        assert cfg.emoji_tools is False

    def test_fields_inherit_from_default_when_missing(self):
        from janus_cli.skin_engine import _BUILTIN_SKINS, _build_skin_config
        cfg = _build_skin_config({"name": "bare"})
        d = _BUILTIN_SKINS["default"]
        assert cfg.layout == d.get("layout", "panel")
        assert cfg.emoji_tools is d.get("emoji_tools", True)

    def test_invalid_symbols_section_ignored(self):
        from janus_cli.skin_engine import _build_skin_config
        cfg = _build_skin_config({"name": "t", "symbols": "not-a-dict"})
        assert cfg.symbols == {}


class TestMinimalDefault:
    def test_default_is_open_layout_no_emoji(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        assert s.layout == "open"
        assert s.emoji_tools is False

    def test_default_accent_is_refined_gold(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        assert s.get_color("ui_accent") == "#E3A857"
        assert s.get_color("banner_title") == "#E3A857"

    def test_default_branding_is_lowercase_calm(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        for key in ("welcome", "goodbye", "help_header", "response_label"):
            v = s.get_branding(key)
            assert v == v.lower(), f"{key} not lowercase: {v!r}"
            assert "!" not in v
        # no emoji / kaomoji in default branding
        assert "⚕" not in s.get_branding("response_label")
        assert "(^_^)" not in s.get_branding("help_header")

    def test_default_supplies_no_spinner_faces(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("default")
        assert s.spinner.get("waiting_faces", []) == []
        assert s.spinner.get("thinking_faces", []) == []

    def test_classic_unaffected_by_the_flip(self):
        from janus_cli.skin_engine import load_skin
        s = load_skin("classic")
        assert s.get_color("ui_accent") == "#FFBF00"
        assert s.layout == "panel"
