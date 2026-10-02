#!/usr/bin/env python3
"""K391 advisory precheck — KaliBench NL-to-CLI tool-use evaluation."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("fixed_reference", "Score tool invocations against a fixed reference command, not the model's own account?"),
    ("split_selection_arguments", "Report tool-selection and argument-construction separately, not one figure?"),
    ("alias_aware", "Normalise aliases before comparing flags/arg order?"),
    ("no_execution_of_model_output", "Verify against a pre-validated reference rather than executing model output?"),
    ("licence_verified", "Dataset/repo licence verified via gh api before any use? (KaliBench repo: null SPDX, no LICENSE file)"),
    ("no_clone_unlicensed", "No clone / no dataset download while the licence stays unverified?"),
    ("manual_drift_noted", "Note that ground truth comes from build-time manuals and flags drift?"),
    ("no_wiki_payloads", "No executable command lists or attack payloads in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"licence_verified": False})
    assert not bad and "licence_verified" in miss
    print("OK k391_kalibench_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K391 KaliBench advisory checklist")
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

    print("# K391 KaliBench NL-to-CLI tool-use eval — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/kalibench-nl-to-cli-tool-use-eval.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
