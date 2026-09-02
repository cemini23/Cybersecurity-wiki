#!/usr/bin/env python3
"""K321 advisory precheck — guardrail construct validity before policy claims."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("incentive_validity", "Incentive manipulations move incentives in the expected direction?"),
    ("protocol_isolation", "Guarded vs unguarded agents share the same offer/choice interface?"),
    ("stochastic_stability", "Enough generations + uncertainty reported (bootstrap CIs)?"),
    ("welfare_accounting", "Scripted positive controls bound welfare interpretability?"),
    ("invalid_inconclusive_gate", "Return Invalid/Inconclusive when schema or chooser drift dominates?"),
    ("no_causal_claim_without_pass", "No causal guardrail efficacy claim without all checks passing?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist(
        {
            "incentive_validity": True,
            "protocol_isolation": False,
            "stochastic_stability": True,
            "welfare_accounting": True,
            "invalid_inconclusive_gate": True,
            "no_causal_claim_without_pass": True,
        }
    )
    assert not bad and "protocol_isolation" in miss
    print("OK k321_guardrail_construct_validity_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K321 guardrail construct validity advisory checklist")
    ap.add_argument("cmd", choices=("checklist", "selftest", "json"))
    ap.add_argument("--json", dest="json_path", help="JSON bool map for json subcommand")
    args = ap.parse_args()

    if args.cmd == "selftest":
        selftest()
        return 0

    if args.cmd == "json":
        if not args.json_path:
            print("FAIL --json required", file=sys.stderr)
            return 1
        try:
            data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
        except FileNotFoundError:
            print(f"FAIL file not found: {args.json_path}", file=sys.stderr)
            return 1
        except json.JSONDecodeError as exc:
            print(f"FAIL invalid JSON: {exc}", file=sys.stderr)
            return 1
        if not isinstance(data, dict):
            print("FAIL JSON must be an object", file=sys.stderr)
            return 1
        ok, missing = run_checklist({k: data.get(k) is True for k, _ in CHECKS})
        print(json.dumps({"ok": ok, "missing": missing}, indent=2))
        return 0 if ok else 2

    print("# K321 guardrail construct validity — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nRun: python3 scripts/k321_guardrail_construct_validity_precheck.py json --json path/to/answers.json")
    print("Canon: wiki/concepts/guardrail-construct-validity-agent-eval.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
