"""Minimal tool lines (default skin): emoji-free aligned ledger.
Classic keeps the legacy emoji format byte-for-byte."""
import re
from unittest.mock import patch as mock_patch

from agent.display import get_cute_tool_message
from janus_cli.skin_engine import SkinConfig, set_active_skin


def teardown_function():
    set_active_skin("default")


def test_minimal_line_is_emoji_free_and_aligned():
    set_active_skin("default")
    line = get_cute_tool_message("terminal", {"command": "git status"}, 0.21)
    assert line.startswith("▸ ")
    assert "$" in line                       # verb preserved
    assert "git status" in line
    assert line.rstrip().endswith("0.2s")
    assert "💻" not in line and "┊" not in line


def test_minimal_failure_line_uses_fail_mark():
    set_active_skin("default")
    line = get_cute_tool_message(
        "terminal", {"command": "boom"}, 0.10,
        result='{"error": "exit 1"}')
    assert line.startswith("✗ ")


def test_minimal_line_never_contains_emoji_for_any_known_tool():
    set_active_skin("default")
    emoji_re = re.compile(r"[\U0001F000-\U0001FAFF☀-➿️]")
    cases = [
        ("web_search", {"query": "rust"}), ("read_file", {"path": "/a/b.py"}),
        ("write_file", {"path": "/a/b.py"}), ("patch", {"path": "/a/b.py"}),
        ("search_files", {"pattern": "TODO"}), ("browser_navigate", {"url": "https://x.io"}),
        ("memory", {"action": "add", "target": "user", "content": "c"}),
        ("execute_code", {"code": "print(1)"}), ("delegate_task", {"goal": "g"}),
        ("unknown_tool_xyz", {}),
    ]
    for name, args in cases:
        line = get_cute_tool_message(name, args, 0.5)
        assert not emoji_re.search(line), f"{name}: {line!r}"


def test_classic_line_is_byte_identical_to_legacy():
    set_active_skin("classic")
    line = get_cute_tool_message("terminal", {"command": "git status"}, 0.21)
    assert line == "┊ 💻 $         git status  0.2s"


def test_classic_search_line_verbatim():
    set_active_skin("classic")
    line = get_cute_tool_message("web_search", {"query": "rust"}, 1.0)
    assert line == "┊ 🔍 search    rust  1.0s"


def test_emoji_skin_with_custom_prefix_substitutes_it():
    """The legacy branch's skin-prefix substitution (skin_prefix != "┊")
    must stay covered: no built-in emoji_tools skin ships a non-┊ prefix
    (classic uses "┊"; ares moved to the minimal branch), so exercise it
    with a fabricated skin, same _get_skin mocking pattern as
    tests/agent/test_display_emoji.py."""
    skin = SkinConfig(name="x", emoji_tools=True, tool_prefix="╎")
    with mock_patch("agent.display._get_skin", return_value=skin):
        line = get_cute_tool_message("terminal", {"command": "ls"}, 0.1)
    assert line.startswith("╎ ")
    assert "💻" in line                      # legacy emoji shape preserved
    assert "$" in line and "ls" in line
    assert line.rstrip().endswith("0.1s")
    assert "┊" not in line                   # prefix was substituted, not kept


def test_spinner_faces_minimal_under_default_skin():
    from agent.display import KawaiiSpinner
    set_active_skin("default")
    assert KawaiiSpinner.get_waiting_faces() == [""]
    assert KawaiiSpinner.get_thinking_faces() == [""]
    assert KawaiiSpinner.get_thinking_verbs() == ["thinking"]


def test_spinner_faces_kawaii_under_classic_skin():
    from agent.display import KawaiiSpinner
    set_active_skin("classic")
    assert "(⌐■_■)" in KawaiiSpinner.get_thinking_faces()
    assert "pondering" in KawaiiSpinner.get_thinking_verbs()


def test_compose_spinner_message_skips_empty_face():
    from agent.display import compose_spinner_message
    assert compose_spinner_message("", "running 3 tools") == "running 3 tools"
    assert compose_spinner_message("(◕‿◕)", "running 3 tools") == "(◕‿◕) ⚡ running 3 tools"
    assert compose_spinner_message("", "thinking...") == "thinking..."
