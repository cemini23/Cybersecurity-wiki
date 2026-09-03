#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = [sys.executable, str(ROOT / "scripts/k324_safeevolve_precheck.py")]
KEYS = (
    "hitl_harness_write", "bounded_reversible", "no_unattended_skills",
    "external_eval_contract", "utility_and_asr", "retrieval_lineage",
)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(PY + list(args), capture_output=True, text=True, check=False)


def test_selftest() -> None:
    assert run("selftest").returncode == 0


def test_json_ok() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({k: True for k in KEYS}, f)
        path = f.name
    assert run("json", "--json", path).returncode == 0
    Path(path).unlink(missing_ok=True)


def test_json_fail() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({k: True for k in KEYS} | {"hitl_harness_write": False}, f)
        path = f.name
    assert run("json", "--json", path).returncode == 2
    Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    test_selftest()
    test_json_ok()
    test_json_fail()
    print("OK test_k324_safeevolve_precheck")
