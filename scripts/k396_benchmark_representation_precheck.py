#!/usr/bin/env python3
"""K396 advisory precheck — benchmark representation sensitivity (TPRS) review.

Run before quoting an agent-security ASR as a robustness claim. An ASR is a
property of the agent PLUS the agent-visible representation, not the agent alone.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("representation_stated", "Is the exact agent-visible representation (tool names/descriptions) stated?"),
    ("success_defined", "Is it stated when an attack counts as success (invocation vs committed)?"),
    ("sensitivity_measured", "Was at least one threat-preserving transformation run and reported?"),
    ("utility_under_transform", "Is benign utility measured under the SAME transformations?"),
    ("max_asr_reported", "Is the maximum ASR across representations reported, not just one?"),
    ("attacker_chooses_name", "If the attacker picks the tool name, is that reflected in the claim?"),
    ("no_single_number_cert", "Is the claim free of treating one ASR as a robustness certificate?"),
    ("no_wiki_payloads", "No attack payloads, tool-name lists, or evasion recipes in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"sensitivity_measured": False})
    assert not bad and "sensitivity_measured" in miss
    print("OK k396_benchmark_representation_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K396 benchmark representation sensitivity checklist")
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
        data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
        ok, missing = run_checklist({k: data.get(k) is True for k, _ in CHECKS})
        print(json.dumps({"ok": ok, "missing": missing}, indent=2))
        return 0 if ok else 2

    print("# K396 benchmark representation sensitivity (TPRS) — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/threat-preserving-representation-sensitivity.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
