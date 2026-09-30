#!/usr/bin/env python3
"""K384 advisory precheck — Frontier Autolab temporal-leakage audit for multi-agent firm evals."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Simulated / owned harness only — no live market or real-firm targets?"),
    ("leakage_measure", "Report a hindsight-leakage measure and a briefing-selection-leakage measure?"),
    ("separate_briefer_from_scorer", "Briefing author and scorer are separate roles?"),
    ("code_computed_totals", "Era totals computed in code, not written by the judge in prose?"),
    ("caution_treatment_fixed", "Rubric treatment of caution fixed in advance (avoid the caution attractor)?"),
    ("independence_disclosed", "Run independence and model reuse disclosed (not treated as replications)?"),
    ("no_self_judging", "Self-judging avoided, or its bias disclosed in the report?"),
    ("no_wiki_payloads", "No briefing bodies, judge prompts, or leakage recipes in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"leakage_measure": False})
    assert not bad and "leakage_measure" in miss
    print("OK k384_frontier_autolab_leakage_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K384 Frontier Autolab leakage advisory checklist")
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

    print("# K384 Frontier Autolab temporal-leakage audit — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/frontier-autolab-organizational-memory-leakage.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
