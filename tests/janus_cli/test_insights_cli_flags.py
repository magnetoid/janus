"""The insights subcommand resolves the learning/usage flags to a render mode."""
import janus_cli.main as m


def test_resolve_insights_mode_helper():
    assert m._resolve_insights_mode(learning=False, usage=False) == "both"
    assert m._resolve_insights_mode(learning=True, usage=False) == "learning"
    assert m._resolve_insights_mode(learning=False, usage=True) == "usage"
    # both flags -> both
    assert m._resolve_insights_mode(learning=True, usage=True) == "both"
