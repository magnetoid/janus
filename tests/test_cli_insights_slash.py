"""The /insights slash parser extracts days/source/mode/json from the command string."""
from cli import _parse_insights_command


def test_parse_insights_defaults():
    opts = _parse_insights_command("/insights")
    assert opts == {"days": 30, "source": None, "mode": "both", "as_json": False}


def test_parse_insights_flags():
    opts = _parse_insights_command("/insights 7 --json --learning --source telegram")
    assert opts["days"] == 7
    assert opts["source"] == "telegram"
    assert opts["mode"] == "learning"
    assert opts["as_json"] is True
