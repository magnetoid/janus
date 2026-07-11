"""Minimal tool lines (default skin): emoji-free aligned ledger.
Classic keeps the legacy emoji format byte-for-byte."""
import re

from agent.display import get_cute_tool_message
from janus_cli.skin_engine import set_active_skin


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
