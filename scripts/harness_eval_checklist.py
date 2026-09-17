#!/usr/bin/env python3
"""K334 harness-as-eval-artifact checklist — before accepting a harness version.

Operator-invoked gate aligned with HarnessDev: evaluate runnable infrastructure,
not only task outputs. Does not auto-evolve skills or rewrite pass criteria.

Usage:
  python3 scripts/harness_eval_checklist.py checklist
  python3 scripts/harness_eval_checklist.py json --json answers.json
  python3 scripts/harness_eval_checklist.py selftest
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKLIST: list[tuple[str, str]] = [
    (
        "hidden_held_out",
        "Hidden held-out tasks exist and were not used during harness development.",
    ),
    (
        "executor_swap",
        "Gains were checked under at least one alternate executor model (swap test).",
    ),
    (
        "state_fires",
        "State/memory/checkpoint hooks fired in formal runs (not only defined in code).",
    ),
    (
        "external_eval",
        "Pass criteria are external — agent did not rewrite ## Verify / lint rules.",
    ),
    (
        "no_skill_autowrite",
        "No unattended .cursor/skills auto-evolution from this harness iteration.",
    ),
]

REQUIRED_YES = {k for k, _ in CHECKLIST}


def checklist_text() -> str:
    lines = ["K334 harness eval artifact checklist", ""]
    for key, prompt in CHECKLIST:
        lines.append(f"  [{key}] {prompt}")
    lines.append("")
    lines.append("All keys must be true for SHIP. Partial visible feedback without held-out → HOLD.")
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
    return "SHIP", ["harness version cleared for persist"]


def selftest() -> int:
    good = {k: True for k in REQUIRED_YES}
    if score_answers(good)[0] != "SHIP":
        print("FAIL good case", file=sys.stderr)
        return 1
    bad = dict(good)
    bad["hidden_held_out"] = False
    if score_answers(bad)[0] != "HOLD":
        print("FAIL bad case", file=sys.stderr)
        return 1
    print("harness_eval_checklist selftest: 2 pass, 0 fail")
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
