"""Tests for agent/evals.py — eval spec loading, checks, and the runner."""

import json

import pytest

from agent.evals import (
    EvalSpec,
    evaluate_checks,
    evals_dir,
    load_eval_specs,
    results_dir,
    run_evals,
    scaffold_example,
)


def _spec(**overrides):
    base = dict(
        name="t",
        prompt="say hi",
        checks=[{"type": "contains", "value": "hi"}],
    )
    base.update(overrides)
    return EvalSpec(**base)


class TestLoadSpecs:
    def test_single_spec_file(self, tmp_path):
        f = tmp_path / "one.yaml"
        f.write_text(
            "name: greet\nprompt: say hi\nchecks:\n  - type: contains\n    value: hi\n",
            encoding="utf-8",
        )
        specs = load_eval_specs(f)
        assert len(specs) == 1
        assert specs[0].name == "greet"
        assert specs[0].source_file == str(f)

    def test_evals_list_and_directory_scan(self, tmp_path):
        (tmp_path / "a.yaml").write_text(
            "evals:\n"
            "  - name: one\n    prompt: p1\n    checks: [{type: contains, value: x}]\n"
            "  - name: two\n    prompt: p2\n    checks: [{type: regex, value: y}]\n",
            encoding="utf-8",
        )
        (tmp_path / "b.yml").write_text(
            "name: three\nprompt: p3\nchecks: [{type: min_length, value: 1}]\n",
            encoding="utf-8",
        )
        specs = load_eval_specs(tmp_path)
        assert {s.name for s in specs} == {"one", "two", "three"}

    def test_missing_path_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            load_eval_specs(tmp_path / "nope")

    def test_invalid_check_type_rejected(self, tmp_path):
        f = tmp_path / "bad.yaml"
        f.write_text(
            "name: bad\nprompt: p\nchecks: [{type: llm_vibes, value: x}]\n",
            encoding="utf-8",
        )
        with pytest.raises(ValueError, match="llm_vibes"):
            load_eval_specs(f)

    def test_missing_fields_rejected(self, tmp_path):
        f = tmp_path / "bad.yaml"
        f.write_text("name: bad\nchecks: [{type: contains, value: x}]\n", encoding="utf-8")
        with pytest.raises(ValueError, match="prompt"):
            load_eval_specs(f)

    def test_duplicate_names_rejected(self, tmp_path):
        f = tmp_path / "dup.yaml"
        f.write_text(
            "evals:\n"
            "  - name: same\n    prompt: p\n    checks: [{type: contains, value: x}]\n"
            "  - name: same\n    prompt: p\n    checks: [{type: contains, value: x}]\n",
            encoding="utf-8",
        )
        with pytest.raises(ValueError, match="duplicate"):
            load_eval_specs(f)

    def test_default_dir_is_profile_aware(self):
        # evals_dir derives from get_janus_home(), which tests isolate
        assert "evals" in str(evals_dir())


class TestEvaluateChecks:
    def test_contains_case_insensitive_default(self):
        out = evaluate_checks([{"type": "contains", "value": "PyTest"}], "we use pytest")
        assert out[0]["passed"] is True

    def test_contains_case_sensitive_opt_in(self):
        out = evaluate_checks(
            [{"type": "contains", "value": "PyTest", "case_sensitive": True}],
            "we use pytest",
        )
        assert out[0]["passed"] is False
        assert out[0]["detail"]

    def test_not_contains(self):
        out = evaluate_checks([{"type": "not_contains", "value": "error"}], "all good")
        assert out[0]["passed"] is True

    def test_regex(self):
        out = evaluate_checks([{"type": "regex", "value": r"\d+ passed"}], "12 passed")
        assert out[0]["passed"] is True

    def test_length_bounds(self):
        out = evaluate_checks(
            [{"type": "min_length", "value": 3}, {"type": "max_length", "value": 5}],
            "abcd",
        )
        assert all(c["passed"] for c in out)

    def test_tool_called_and_not_called(self):
        messages = [
            {"role": "user", "content": "q"},
            {
                "role": "assistant",
                "tool_calls": [
                    {"id": "1", "function": {"name": "web_search", "arguments": "{}"}}
                ],
            },
        ]
        out = evaluate_checks(
            [
                {"type": "tool_called", "value": "web_search"},
                {"type": "tool_not_called", "value": "terminal"},
                {"type": "tool_called", "value": "terminal"},
            ],
            "answer",
            messages,
        )
        assert out[0]["passed"] is True
        assert out[1]["passed"] is True
        assert out[2]["passed"] is False

    def test_bad_check_never_raises(self):
        out = evaluate_checks([{"type": "regex", "value": "("}], "text")
        assert out[0]["passed"] is False
        assert "error" in out[0]["detail"]


class TestRunEvals:
    def test_runner_injection_and_summary(self):
        specs = [
            _spec(name="pass-one"),
            _spec(name="fail-one", checks=[{"type": "contains", "value": "absent"}]),
        ]

        def fake_runner(spec):
            return {"final_response": "hi there", "messages": []}

        summary = run_evals(specs, agent_runner=fake_runner, save_results=False)
        assert summary["total"] == 2
        assert summary["passed"] == 1
        assert summary["failed"] == 1
        by_name = {r["name"]: r for r in summary["results"]}
        assert by_name["pass-one"]["passed"] is True
        assert by_name["fail-one"]["passed"] is False

    def test_runner_exception_marks_failed_and_continues(self):
        calls = []

        def flaky_runner(spec):
            calls.append(spec.name)
            if spec.name == "boom":
                raise RuntimeError("provider down")
            return {"final_response": "hi", "messages": []}

        specs = [_spec(name="boom"), _spec(name="ok")]
        summary = run_evals(specs, agent_runner=flaky_runner, save_results=False)
        assert calls == ["boom", "ok"]
        by_name = {r["name"]: r for r in summary["results"]}
        assert by_name["boom"]["passed"] is False
        assert "provider down" in by_name["boom"]["error"]
        assert by_name["ok"]["passed"] is True

    def test_results_saved_as_jsonl(self):
        summary = run_evals(
            [_spec(name="saved")],
            agent_runner=lambda s: {"final_response": "hi", "messages": []},
        )
        path = summary.get("results_path")
        assert path
        lines = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]
        assert lines[0]["name"] == "saved"
        assert str(results_dir()) in path


class TestScaffold:
    def test_scaffold_creates_loadable_spec(self):
        path = scaffold_example()
        specs = load_eval_specs(path)
        assert specs[0].name == "example-arithmetic"
        # idempotent without force
        assert scaffold_example() == path

    def test_starter_suite_all_load(self):
        from agent.evals import STARTER_SPECS, scaffold_starters

        written = scaffold_starters()
        assert len(written) == len(STARTER_SPECS)
        specs = load_eval_specs(evals_dir())
        names = {s.name for s in specs}
        assert "dialectic-frame-dependent-flags" in names
        assert "dialectic-frame-stable-does-not-flag" in names
        assert "instruction-following-brevity" in names
        # every starter spec passes full validation (checks well-formed)
        for s in specs:
            assert s.checks

    def test_starter_rerun_never_clobbers_edits(self):
        from agent.evals import scaffold_starters

        scaffold_starters()
        edited = evals_dir() / "basics.yaml"
        edited.write_text(
            "name: mine\nprompt: p\nchecks: [{type: contains, value: x}]\n",
            encoding="utf-8",
        )
        assert scaffold_starters() == []  # nothing rewritten
        assert "mine" in edited.read_text(encoding="utf-8")

    def test_dialectic_pair_targets_moa_toolset(self):
        from agent.evals import scaffold_starters

        scaffold_starters()
        specs = load_eval_specs(evals_dir() / "dialectic-validation.yaml")
        for s in specs:
            assert s.toolsets == ["moa"]
            assert any(
                c["type"] == "tool_called" and c["value"] == "deliberate"
                for c in s.checks
            )
