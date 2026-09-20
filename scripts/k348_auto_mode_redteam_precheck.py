#!/usr/bin/env python3
"""K348 advisory precheck — Auto Mode blocking classifier red-team eval."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned-lab blocking-monitor red-team?"),
    ("monitor_named", "Name blocking monitor product/stage and tool coverage under test?"),
    ("multi_context_axis", "Report multi-context malign-agent attacks separately from single-turn ASR?"),
    ("no_wiki_payloads", "No attack transcripts or malign replay payloads in wiki?"),
    ("external_enforcement", "Treat monitor as pre-execution gate — not model self-arbitration alone (pairs K314)?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"multi_context_axis": False})
    assert not bad and "multi_context_axis" in miss
    print("OK k348_auto_mode_redteam_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K348 Auto Mode red-team advisory checklist")
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

    print("# K348 Auto Mode blocking classifier red-team — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/auto-mode-blocking-classifier-redteam.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
