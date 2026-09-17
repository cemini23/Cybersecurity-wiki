#!/usr/bin/env python3
"""CI smoke tests for federation helper scripts copied from CCC."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable

SCRIPTS = (
    "harness_eval_checklist.py",
    "delegation_broker_precheck.py",
    "agent_queue_labels.py",
)


def _run(script: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [PY, str(ROOT / "scripts" / script), *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_selftests() -> None:
    for script in SCRIPTS:
        cp = _run(script, "selftest")
        assert cp.returncode == 0, f"{script} selftest failed: {cp.stderr}"


def test_checklist_commands() -> None:
    for script in ("harness_eval_checklist.py", "delegation_broker_precheck.py"):
        cp = _run(script, "checklist")
        assert cp.returncode == 0, f"{script} checklist failed: {cp.stderr}"
        assert cp.stdout.strip(), f"{script} checklist empty"


if __name__ == "__main__":
    test_selftests()
    test_checklist_commands()
    print("OK test_federation_helper_scripts")
