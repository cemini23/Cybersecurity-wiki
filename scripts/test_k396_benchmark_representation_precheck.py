#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = [sys.executable, str(ROOT / "scripts/k396_benchmark_representation_precheck.py")]
KEYS = (
    "representation_stated",
    "success_defined",
    "sensitivity_measured",
    "utility_under_transform",
    "max_asr_reported",
    "attacker_chooses_name",
    "no_single_number_cert",
    "no_wiki_payloads",
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


def test_json_missing_key_fails() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump({k: True for k in KEYS if k != "sensitivity_measured"}, f)
        path = f.name
    assert run("json", "--json", path).returncode == 2
    Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    test_selftest()
    test_json_ok()
    test_json_missing_key_fails()
    print("OK test_k396_benchmark_representation_precheck")
