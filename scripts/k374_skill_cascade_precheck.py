#!/usr/bin/env python3
"""K374 advisory precheck — skill cascading / joint-skill suite audit."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written scope for owned-lab joint-skill / suite eval?"),
    ("suite_as_unit", "Treat co-installed vendor skill suites as one review unit?"),
    ("shared_context_audit", "Audit what each skill writes into the shared context window?"),
    ("joint_skill_scan", "Run a joint-skill review in addition to per-skill SKILL.md scan?"),
    ("hitl_install", "HITL before installing third-party skill suites from a marketplace?"),
    ("no_wiki_payloads", "No cascade recipes, modified skills, or attack payloads in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"joint_skill_scan": False})
    assert not bad and "joint_skill_scan" in miss
    print("OK k374_skill_cascade_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K374 skill cascading advisory checklist")
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

    print("# K374 skill cascading — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/skill-cascading-attacks-cross-skill.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
