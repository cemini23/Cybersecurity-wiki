#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = [sys.executable, str(ROOT / "scripts/k316_cua_ipi_precheck.py")]
KEYS = (
    "written_scope", "vm_sandbox", "deterministic_oracle", "joint_success", "no_wiki_payloads",
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
        json.dump({k: True for k in KEYS} | {"vm_sandbox": False}, f)
        path = f.name
    r = run("json", "--json", path)
    assert r.returncode == 2, r.stdout
    Path(path).unlink(missing_ok=True)


if __name__ == "__main__":
    test_selftest()
    test_json_ok()
    test_json_fail()
    print("OK test_k316_cua_ipi_precheck")
