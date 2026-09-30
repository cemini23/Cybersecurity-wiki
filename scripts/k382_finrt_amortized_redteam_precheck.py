#!/usr/bin/env python3
"""K382 advisory precheck — FinRT amortized adversarial-generator red-team lab."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("authorized_scope", "Written scope for the models under red-team test (owned or procured)?"),
    ("joint_objectives", "Report attack success, severity, coverage, and diversity jointly?"),
    ("realism_constrained_coverage", "Use realism-constrained coverage, not raw prompt count?"),
    ("amortization_accounting", "State the offline generator cost and what it is amortized over?"),
    ("separate_generator_from_target", "Keep the reusable generator separate from target-facing calls?"),
    ("human_audit_judge", "Human-audit a sample of judge labels and report agreement?"),
    ("no_wiki_payloads", "No high-severity prompts, target adapters, or attack recipes in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"joint_objectives": False})
    assert not bad and "joint_objectives" in miss
    print("OK k382_finrt_amortized_redteam_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K382 FinRT amortized red-team advisory checklist")
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

    print("# K382 FinRT amortized adversarial-generator red-team — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/finrt-amortized-redteam-generator.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
