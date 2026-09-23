#!/usr/bin/env python3
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = [sys.executable, str(ROOT / "scripts/k358_rrsi_harness_precheck.py")]
KEYS = (
    "written_scope", "hitl_gate", "regularization_claim",
    "rollback_path", "validation_ratchet", "no_wiki_payloads",
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


if __name__ == "__main__":
    test_selftest()
    test_json_ok()
    print("OK test_k358_rrsi_harness_precheck")
