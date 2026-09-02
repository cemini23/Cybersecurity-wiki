#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = [sys.executable, str(ROOT / "scripts/k320_evoflint_redteam_precheck.py")]
KEYS = (
    "written_scope",
    "asr_and_severity",
    "harness_judge_named",
    "archive_coverage",
    "no_wiki_plan_payloads",
    "no_live_third_party",
)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(PY + list(args), capture_output=True, text=True, check=False)


def test_selftest() -> None:
    r = run("selftest")
    assert r.returncode == 0, r.stderr or r.stdout


def test_json_ok() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({k: True for k in KEYS}, f)
        path = f.name
    r = run("json", "--json", path)
    assert r.returncode == 0, r.stdout
    Path(path).unlink(missing_ok=True)


def test_json_fail() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({k: True for k in KEYS} | {"asr_and_severity": False}, f)
        path = f.name
    r = run("json", "--json", path)
    assert r.returncode == 2, r.stdout
    Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    test_selftest()
    test_json_ok()
    test_json_fail()
    print("OK test_k320_evoflint_redteam_precheck")
