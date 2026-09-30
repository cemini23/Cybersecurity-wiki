#!/usr/bin/env python3
"""Offline tests for scripts/gh_lookup.sh. No network: `gh` is stubbed on PATH.

Guards the regression described in briefs/2026-09-30_ccc-gh-inventory-scripts-broken.md:
a failing lookup must never read as an empty or absent result.
"""
from __future__ import annotations

import os
import stat
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIB = ROOT / "scripts/gh_lookup.sh"

FAKE_GH = """#!/usr/bin/env bash
case "${GH_FAKE_MODE:-ok}" in
  ok)      echo "Apache-2.0"; exit 0 ;;
  empty)   echo "[]"; exit 0 ;;
  missing) echo "gh: Not Found (HTTP 404)" >&2; exit 1 ;;
  fail)    echo "gh: API rate limit exceeded" >&2; exit 1 ;;
esac
exit 1
"""


def _run(snippet: str, mode: str = "ok") -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as d:
        gh = Path(d) / "gh"
        gh.write_text(FAKE_GH, encoding="utf-8")
        gh.chmod(gh.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        env = dict(os.environ)
        env["PATH"] = f"{d}:{env['PATH']}"
        env["GH_FAKE_MODE"] = mode
        body = f'. "{LIB}"\n{snippet}\n'
        return subprocess.run(["bash", "-c", body], capture_output=True, text=True, env=env)


def sentinels() -> dict[str, str]:
    r = _run('printf "FAIL=%s\\nMISSING=%s\\n" "$GH_FAIL_SENTINEL" "$GH_MISSING_SENTINEL"')
    assert r.returncode == 0, r.stderr
    out = {}
    for line in r.stdout.strip().splitlines():
        k, _, v = line.partition("=")
        out[k] = v
    return out


S = sentinels()


def test_spdx_success() -> None:
    r = _run('printf "VAL=%s\\n" "$(gh_repo_spdx owner/repo)"', "ok")
    assert r.stdout.strip() == "VAL=Apache-2.0", r.stdout
    assert "LOOKUP FAILED" not in r.stderr


def test_spdx_missing_repo_is_not_a_failure() -> None:
    r = _run('printf "VAL=%s\\n" "$(gh_repo_spdx owner/repo)"', "missing")
    assert r.stdout.strip() == f"VAL={S['MISSING']}", r.stdout
    assert "LOOKUP FAILED" not in r.stderr, "a 404 must not be reported as a lookup failure"


def test_spdx_hard_failure_is_the_sentinel_not_a_value() -> None:
    r = _run('printf "VAL=%s\\n" "$(gh_repo_spdx owner/repo)"', "fail")
    assert r.stdout.strip() == f"VAL={S['FAIL']}", r.stdout
    assert "LOOKUP FAILED" in r.stderr, "a real failure must be announced on stderr"


def test_search_empty_is_a_true_negative() -> None:
    r = _run('printf "VAL=%s\\n" "$(gh_search_repos 5 fullName "x in:name")"', "empty")
    assert r.stdout.strip() == "VAL=[]", r.stdout
    assert "LOOKUP FAILED" not in r.stderr


def test_search_failure_is_not_an_empty_result() -> None:
    r = _run('printf "VAL=%s\\n" "$(gh_search_repos 5 fullName "x in:name")"', "fail")
    assert r.stdout.strip() == f"VAL={S['FAIL']}", r.stdout
    assert "LOOKUP FAILED" in r.stderr


def test_repo_exists_exit_codes() -> None:
    ok = _run('gh_repo_exists owner/repo; echo "RC=$?"', "ok")
    assert ok.stdout.strip() == "RC=0", ok.stdout
    missing = _run('gh_repo_exists owner/repo; echo "RC=$?"', "missing")
    assert missing.stdout.strip() == "RC=1", missing.stdout
    fail = _run('gh_repo_exists owner/repo; echo "RC=$?"', "fail")
    assert fail.stdout.strip() == "RC=2", fail.stdout
    assert "LOOKUP FAILED" in fail.stderr


def test_repo_path_exists_exit_codes() -> None:
    ok = _run('gh_repo_path_exists owner/repo LICENSE; echo "RC=$?"', "ok")
    assert ok.stdout.strip() == "RC=0", ok.stdout
    missing = _run('gh_repo_path_exists owner/repo LICENSE; echo "RC=$?"', "missing")
    assert missing.stdout.strip() == "RC=1", missing.stdout
    fail = _run('gh_repo_path_exists owner/repo LICENSE; echo "RC=$?"', "fail")
    assert fail.stdout.strip() == "RC=2", fail.stdout


if __name__ == "__main__":
    test_spdx_success()
    test_spdx_missing_repo_is_not_a_failure()
    test_spdx_hard_failure_is_the_sentinel_not_a_value()
    test_search_empty_is_a_true_negative()
    test_search_failure_is_not_an_empty_result()
    test_repo_exists_exit_codes()
    test_repo_path_exists_exit_codes()
    print("OK test_gh_lookup")
