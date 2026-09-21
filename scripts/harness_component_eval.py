#!/usr/bin/env python3
"""K370 harness component eval checklist — decompose before persist gate.

Operator-invoked: score planning / action space / context management under a
fixed execution loop. Run before harness-eval-gate (K334).

Usage:
  python3 scripts/harness_component_eval.py checklist
  python3 scripts/harness_component_eval.py json --json answers.json
  python3 scripts/harness_component_eval.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKLIST: list[tuple[str, str]] = [
    ("fixed_execution_loop", "Execution loop stayed constant across component ablations."),
    ("planning_evidence", "Planning component has its own artifact or locator."),
    ("action_space_evidence", "Action space component has its own artifact or locator."),
    ("context_management_evidence", "Context management has its own artifact or locator."),
    ("not_monolithic", "Result is not a single end-to-end harness score only."),
    ("no_skill_autowrite", "No unattended .cursor/skills write from this iteration."),
]

REQUIRED_YES = {k for k, _ in CHECKLIST}


def checklist_text() -> str:
    lines = ["K370 harness component eval checklist", ""]
    for key, prompt in CHECKLIST:
        lines.append(f"  [{key}] {prompt}")
    lines.append("")
    lines.append("All keys must be true for SHIP. Run before harness-eval-gate (K334).")
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
    return "SHIP", ["component-level harness eval cleared"]


def selftest() -> int:
    good = {k: True for k in REQUIRED_YES}
    if score_answers(good)[0] != "SHIP":
        print("FAIL good case", file=sys.stderr)
        return 1
    bad = dict(good)
    bad["not_monolithic"] = False
    if score_answers(bad)[0] != "HOLD":
        print("FAIL bad case", file=sys.stderr)
        return 1
    print("harness_component_eval selftest: 2 pass, 0 fail")
    return 0


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
    data = json.loads(Path(args.json).read_text())
    verdict, reasons = score_answers(data)
    print(json.dumps({"verdict": verdict, "reasons": reasons}, indent=2))
    return 0 if verdict == "SHIP" else 2


if __name__ == "__main__":
    raise SystemExit(main())
