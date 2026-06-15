"""The measurable-self-improvement feature flags exist with safe defaults."""
from janus_cli.config import DEFAULT_CONFIG


def test_evals_trend_defaults_off():
    evals = DEFAULT_CONFIG["evals"]
    assert evals["trend"]["enabled"] is False
    assert evals["trend"]["interval_hours"] == 24
    assert evals["autopin"] is False


def test_write_time_reconcile_default_off():
    assert DEFAULT_CONFIG["memory"]["write_time_reconcile"] is False
