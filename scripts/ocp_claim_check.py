#!/usr/bin/env python3
"""Overclaiming propensity (OCP) claim check — K371 leftover.

Compare agent completion claims to on-disk locators and verify_ran flag.
Status labels are not endpoints (K277). Does not write watches or wiki.

Usage:
  python3 scripts/ocp_claim_check.py json --json claim.json
  python3 scripts/ocp_claim_check.py selftest
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

_DONE_WORDS = re.compile(r"\b(done|complete|finished|shipped|success)\b", re.I)
_SCOPE_OUT = re.compile(r"\.\./|\bnode_modules\b|\b\.git\b")


def _resolve(path_str: str) -> Path:
    p = Path(path_str)
    if not p.is_absolute():
        p = REPO_ROOT / p
    return p.resolve()


def classify(data: dict) -> tuple[str, list[str]]:
    if not isinstance(data, dict):
        return "OVERCLAIM", ["input must be a JSON object"]

    claim_text = str(data.get("claim_text") or "")
    status = str(data.get("claimed_status") or "").strip().lower()
    evidence = data.get("evidence_paths") or []
    verify_ran = data.get("verify_ran")

    if status not in {"done", "partial", "blocked"}:
        return "OVERCLAIM", [f"invalid claimed_status: {status!r}"]

    if not isinstance(evidence, list):
        return "OVERCLAIM", ["evidence_paths must be a list"]

    missing = []
    for raw in evidence:
        p = _resolve(str(raw))
        if not p.is_file() and not p.is_dir():
            missing.append(str(raw))

    if status == "done" and not verify_ran:
        return "OVERCLAIM", ["done claimed without verify_ran=true"]

    if missing:
        return "OVERCLAIM", [f"missing evidence path: {p}" for p in missing]

    for raw in evidence:
        if _SCOPE_OUT.search(str(raw)):
            return "DRIFT_EXPERIMENTAL", [f"evidence outside claimed scope: {raw}"]

    claim_l = claim_text.lower()
    if status == "done" and evidence:
        basename_hits = sum(
            1 for raw in evidence if Path(str(raw)).stem.lower() in claim_l
        )
        if basename_hits == 0 and _DONE_WORDS.search(claim_text):
            return "DRIFT_SEMANTIC", ["claim keywords do not match evidence paths (K122)"]

    if status == "done" and _DONE_WORDS.search(claim_text):
        if not any(
            re.search(r"(planning|action|context|component|harness)", str(raw), re.I)
            for raw in evidence
        ):
            return "DRIFT_MECHANISTIC", ["success claimed with no component locator (pairs K370)"]

    if status == "done" and verify_ran and not missing:
        return "OK", ["claim matches locators and verify_ran"]

    if status in {"partial", "blocked"}:
        return "OK", [f"status {status} with locators present"]

    return "OK", ["claim check passed"]


def selftest() -> int:
    wiki = "wiki/index.md"
    cases = [
        (
            {
                "claim_text": "Ingest done",
                "claimed_status": "done",
                "evidence_paths": [wiki],
                "verify_ran": False,
            },
            "OVERCLAIM",
        ),
        (
            {
                "claim_text": "Ingest done",
                "claimed_status": "done",
                "evidence_paths": ["wiki/no-such-file-xyz.md"],
                "verify_ran": True,
            },
            "OVERCLAIM",
        ),
        (
            {
                "claim_text": f"Updated {wiki}",
                "claimed_status": "done",
                "evidence_paths": [wiki],
                "verify_ran": True,
            },
            "OK",
        ),
        (
            {
                "claim_text": "Blocked on archive",
                "claimed_status": "blocked",
                "evidence_paths": [wiki],
                "verify_ran": False,
            },
            "OK",
        ),
    ]
    for data, want in cases:
        got, _ = classify(data)
        if got != want:
            print(f"FAIL expected {want}, got {got} for {data}", file=sys.stderr)
            return 1
    print(f"ocp_claim_check selftest: {len(cases)} pass, 0 fail")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p_json = sub.add_parser("json")
    p_json.add_argument("--json", required=True)
    sub.add_parser("selftest")
    args = ap.parse_args()

    if args.cmd == "selftest":
        return selftest()

    data = json.loads(Path(args.json).read_text())
    verdict, reasons = classify(data)
    print(json.dumps({"verdict": verdict, "reasons": reasons}, indent=2))
    return 0 if verdict == "OK" else 2


if __name__ == "__main__":
    raise SystemExit(main())
