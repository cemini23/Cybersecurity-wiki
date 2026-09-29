#!/usr/bin/env python3
"""K379 advisory precheck — curriculum prompt-injection red-team for frontier models."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written scope for owned-lab frontier prompt-injection red-team?"),
    ("curriculum_not_single_shot", "Use a multi-stage curriculum instead of single-shot RL?"),
    ("cold_start_documented", "Document the cold-start problem and curriculum design?"),
    ("frontier_owned_lab_only", "Frontier targets are owned or written-scope lab only?"),
    ("no_injection_payloads_wiki", "No injection payloads or attacker prompts in wiki?"),
    ("report_harness_judge", "Report the harness and judge used for ASR?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"curriculum_not_single_shot": False})
    assert not bad and "curriculum_not_single_shot" in miss
    print("OK k379_curriculum_pi_redteam_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K379 curriculum PI red-team advisory checklist")
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

    print("# K379 curriculum prompt-injection red-team — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/curriculum-prompt-injection-redteam-frontier-models.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
