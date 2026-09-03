#!/usr/bin/env python3
"""K324 advisory precheck — SafeEvolve harness-policy co-evolution discipline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("hitl_harness_write", "HITL before any prod harness/skill/policy write?"),
    ("bounded_reversible", "Harness updates are component-level, auditable, reversible?"),
    ("no_unattended_skills", "No unattended auto-evolve of .cursor/skills?"),
    ("external_eval_contract", "Policy/harness gains scored on held-out external eval?"),
    ("utility_and_asr", "Report safety ASR and benign utility jointly?"),
    ("retrieval_lineage", "Retrieval-time harm tracked separately from write-time HITL?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist(
        {k: True for k, _ in CHECKS} | {"no_unattended_skills": False}
    )
    assert not bad and "no_unattended_skills" in miss
    print("OK k324_safeevolve_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K324 SafeEvolve advisory checklist")
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
        if not isinstance(data, dict):
            print("FAIL JSON must be an object", file=sys.stderr)
            return 1
        ok, missing = run_checklist({k: data.get(k) is True for k, _ in CHECKS})
        print(json.dumps({"ok": ok, "missing": missing}, indent=2))
        return 0 if ok else 2

    print("# K324 SafeEvolve — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/safeevolve-harness-policy-co-evolution.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
