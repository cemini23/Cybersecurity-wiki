#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = [sys.executable, str(ROOT / "scripts/k314_enforcement_precheck.py")]


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(PY + list(args), capture_output=True, text=True, check=False)


def test_selftest() -> None:
    r = run("selftest")
    assert r.returncode == 0, r.stderr or r.stdout


def test_json_ok() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({k: True for k in (
            "external_pep", "authenticated_routing", "capability_gated",
            "no_model_arbitration_only", "model_clustered_metrics",
        )}, f)
        path = f.name
    r = run("json", "--json", path)
    assert r.returncode == 0, r.stdout
    Path(path).unlink(missing_ok=True)


def test_json_fail_missing_pep() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({"external_pep": False, "authenticated_routing": True,
                   "capability_gated": True, "no_model_arbitration_only": True,
                   "model_clustered_metrics": True}, f)
        path = f.name
    r = run("json", "--json", path)
    assert r.returncode == 2, r.stdout
    Path(path).unlink(missing_ok=True)


def test_json_string_false_not_true() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({"external_pep": "false", "authenticated_routing": True,
                   "capability_gated": True, "no_model_arbitration_only": True,
                   "model_clustered_metrics": True}, f)
        path = f.name
    r = run("json", "--json", path)
    assert r.returncode == 2, r.stdout
    Path(path).unlink(missing_ok=True)


def test_json_missing_file() -> None:
    r = run("json", "--json", "/tmp/k314-nonexistent-answers.json")
    assert r.returncode == 1
    assert "FAIL" in r.stderr


if __name__ == "__main__":
    test_selftest()
    test_json_ok()
    test_json_fail_missing_pep()
    test_json_string_false_not_true()
    test_json_missing_file()
    print("OK test_k314_enforcement_precheck")
