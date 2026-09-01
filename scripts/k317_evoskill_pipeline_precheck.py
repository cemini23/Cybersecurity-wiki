#!/usr/bin/env python3
"""K317 advisory precheck — EvoSkill / skill-generation pipeline red-team discipline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned-lab self-evolving agent target?"),
    ("persistence_metric", "Measure stored → retrieved → activated (not single-turn ASR)?"),
    ("no_cursor_skills_copy", "Do not copy evolved/malicious skills into .cursor/skills?"),
    ("hitl_on_skill_write", "HITL on any skill bank write; retrieval-time harm is separate?"),
    ("no_wiki_trajectories", "No malicious trajectory bodies in wiki or briefs?"),
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
            "persistence_metric": True,
            "no_cursor_skills_copy": False,
            "hitl_on_skill_write": True,
            "no_wiki_trajectories": True,
        }
    )
    assert not bad and "no_cursor_skills_copy" in miss
    print("OK k317_evoskill_pipeline_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K317 EvoSkill pipeline advisory checklist")
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

    print("# K317 EvoSkill pipeline — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nRun: python3 scripts/k317_evoskill_pipeline_precheck.py json --json path/to/answers.json")
    print("Canon: wiki/concepts/evoskill-injection-self-evolving-agents.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
