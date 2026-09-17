#!/usr/bin/env python3
"""K333 delegation broker precheck — untrusted-model property checklist.

Operator-invoked closed checklist before wiring multi-agent delegation or
sub-agent tool credentials. Policy only — not a VotalAI/LLM Shield install.

Usage:
  python3 scripts/delegation_broker_precheck.py checklist
  python3 scripts/delegation_broker_precheck.py json --json answers.json
  python3 scripts/delegation_broker_precheck.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKLIST: list[tuple[str, str]] = [
    (
        "external_broker",
        "Authority is enforced outside model reasoning (broker/PEP), not by prompt refusal.",
    ),
    (
        "scoped_credentials",
        "Credentials are workload-scoped; the model never holds long-lived bearer tokens.",
    ),
    (
        "subagent_attenuation",
        "Sub-agent delegation narrows scope (monotone attenuation); parent cannot widen silently.",
    ),
    (
        "audit_trail",
        "Permit/deny decisions are append-only and attributable (principal + workload + tool).",
    ),
    (
        "fail_closed",
        "Missing/expired/revoked mandate → DENY (no silent-default allow).",
    ),
]

REQUIRED_YES = {k for k, _ in CHECKLIST}


def checklist_text() -> str:
    lines = ["K333 untrusted-model delegation precheck", ""]
    for key, prompt in CHECKLIST:
        lines.append(f"  [{key}] {prompt}")
    lines.append("")
    lines.append("All keys must be true (yes) for SHIP. Any false → HOLD for HITL.")
    return "\n".join(lines)


def _truthy(v: object) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in {"yes", "true", "1", "y"}
    return False


def score_answers(data: dict) -> tuple[str, list[str]]:
    if not isinstance(data, dict):
        return "HOLD", ["answers must be a JSON object"]
    missing = [k for k in REQUIRED_YES if k not in data]
    if missing:
        return "HOLD", [f"missing key: {k}" for k in missing]
    fails = [k for k in REQUIRED_YES if not _truthy(data[k])]
    if fails:
        return "HOLD", [f"failed: {k}" for k in fails]
    return "SHIP", ["all five checks pass"]


def selftest() -> int:
    ok, fail = 0, 0
    good = {k: True for k in REQUIRED_YES}
    verdict, _ = score_answers(good)
    if verdict == "SHIP":
        ok += 1
    else:
        fail += 1
        print("FAIL good case", file=sys.stderr)
    bad = dict(good)
    bad["external_broker"] = False
    verdict, reasons = score_answers(bad)
    if verdict == "HOLD" and any("external_broker" in r for r in reasons):
        ok += 1
    else:
        fail += 1
        print("FAIL bad case", file=sys.stderr)
    print(f"delegation_broker_precheck selftest: {ok} pass, {fail} fail")
    return 0 if fail == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("checklist")
    p_json = sub.add_parser("json")
    p_json.add_argument("--json", required=True)
    sub.add_parser("selftest")
    args = ap.parse_args()

    if args.cmd == "checklist":
        print(checklist_text())
        return 0
    if args.cmd == "selftest":
        return selftest()
    path = Path(args.json)
    data = json.loads(path.read_text())
    verdict, reasons = score_answers(data)
    print(json.dumps({"verdict": verdict, "reasons": reasons}, indent=2))
    return 0 if verdict == "SHIP" else 2


if __name__ == "__main__":
    raise SystemExit(main())
