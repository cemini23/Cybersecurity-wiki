#!/usr/bin/env python3
"""K378 advisory precheck — SkillDRE dual-stage skill evolution lab."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written scope for owned-lab dual-stage skill evolution eval?"),
    ("dual_stage_eval", "Evaluate both pre-execution scan and runtime defense feedback?"),
    ("no_clone_null_spdx", "SkillDRE repo remains REFERENCE (null SPDX) — no clone?"),
    ("hitl_skill_evolve", "HITL before evolving skills in the owned harness?"),
    ("preserve_benign_task_metric", "Report benign-task preservation alongside attack success?"),
    ("no_wiki_payloads", "No skill bodies, evolution recipes, or attack payloads in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"dual_stage_eval": False})
    assert not bad and "dual_stage_eval" in miss
    print("OK k378_skilldre_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K378 SkillDRE dual-stage advisory checklist")
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

    print("# K378 SkillDRE dual-stage skill evolution — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
