#!/usr/bin/env python3
"""K320 advisory precheck — EvoFlint multi-turn evolutionary red-team discipline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned-lab / in-scope victim models?"),
    ("asr_and_severity", "Report ASR and peak severity (not scalar ASR alone)?"),
    ("harness_judge_named", "Name harness, judge backbone, split, and severity metric?"),
    ("archive_coverage", "Archive/category coverage reported with results?"),
    ("no_wiki_plan_payloads", "No conversation-plan payloads in wiki, briefs, or git?"),
    ("no_live_third_party", "No LIVE third-party targets without written scope?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist(
        {
            "written_scope": True,
            "asr_and_severity": False,
            "harness_judge_named": True,
            "archive_coverage": True,
            "no_wiki_plan_payloads": True,
            "no_live_third_party": True,
        }
    )
    assert not bad and "asr_and_severity" in miss
    print("OK k320_evoflint_redteam_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K320 EvoFlint red-team advisory checklist")
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

    print("# K320 EvoFlint multi-turn red-team — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nRun: python3 scripts/k320_evoflint_redteam_precheck.py json --json path/to/answers.json")
    print("Canon: wiki/concepts/evoflint-multi-turn-redteam-atlas.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
