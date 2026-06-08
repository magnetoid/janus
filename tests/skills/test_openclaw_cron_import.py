"""Tests for OpenClaw cron auto-import in the migration script."""
import importlib.util
import json
from pathlib import Path

import pytest

SCRIPT = (
    Path(__file__).resolve().parents[2]
    / "optional-skills/migration/openclaw-migration/scripts/openclaw_to_janus.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location("openclaw_to_janus", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    import sys
    sys.modules["openclaw_to_janus"] = mod  # dataclass introspection needs this
    spec.loader.exec_module(mod)
    return mod


def _migrate(mod, tmp_path, cron_value):
    source = tmp_path / ".openclaw"
    target = tmp_path / ".janus"
    source.mkdir()
    target.mkdir()
    (source / "openclaw.json").write_text(
        json.dumps({"cron": cron_value}), encoding="utf-8"
    )
    migrator = mod.Migrator(
        source_root=source, target_root=target, execute=True,
        workspace_target=None, overwrite=False, migrate_secrets=False, output_dir=None,
        selected_options={"cron-jobs"},
    )
    migrator.migrate()
    jobs_file = target / "cron" / "jobs.json"
    jobs = json.loads(jobs_file.read_text(encoding="utf-8")) if jobs_file.exists() else {}
    # jobs.json is a dict {id: job} or {"jobs":[...]}; normalize to a list
    if isinstance(jobs, dict):
        jobs = list(jobs.get("jobs", jobs.values())) if "jobs" in jobs else list(jobs.values())
    return target, jobs


def test_imports_jobs_list_shape(tmp_path):
    mod = load_module()
    cron = {"jobs": [
        {"name": "daily report", "schedule": "0 9 * * *", "prompt": "Summarize yesterday"},
        {"name": "hourly ping", "schedule": "1h", "prompt": "Check the queue"},
    ]}
    target, jobs = _migrate(mod, tmp_path, cron)
    prompts = " ".join(str(j.get("prompt", "")) for j in jobs)
    names = " ".join(str(j.get("name", "")) for j in jobs)
    assert len(jobs) == 2
    assert "Summarize yesterday" in prompts and "Check the queue" in prompts
    assert "daily report" in names


def test_imports_dict_of_id_shape_and_rebrands(tmp_path):
    mod = load_module()
    cron = {
        "weekly-audit": {"cron": "0 0 * * 0", "message": "Audit the OpenClaw setup"},
    }
    target, jobs = _migrate(mod, tmp_path, cron)
    assert len(jobs) == 1
    # 'OpenClaw' rebranded to 'Janus' in the prompt
    assert "Janus" in jobs[0]["prompt"]
    assert "OpenClaw" not in jobs[0]["prompt"]
    assert jobs[0]["name"] == "weekly-audit"


def test_skips_jobs_missing_schedule_or_prompt(tmp_path):
    mod = load_module()
    cron = {"jobs": [
        {"name": "good", "schedule": "0 9 * * *", "prompt": "Do the thing"},
        {"name": "no-prompt", "schedule": "0 9 * * *"},
        {"name": "no-schedule", "prompt": "orphan"},
    ]}
    target, jobs = _migrate(mod, tmp_path, cron)
    names = [j.get("name") for j in jobs]
    assert "good" in names
    assert "no-prompt" not in names and "no-schedule" not in names


def test_no_cron_is_noop(tmp_path):
    mod = load_module()
    target, jobs = _migrate(mod, tmp_path, {})
    assert jobs == []
