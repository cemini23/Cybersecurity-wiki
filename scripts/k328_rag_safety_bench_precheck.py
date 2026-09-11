#!/usr/bin/env python3
"""K328 advisory precheck — RAG-Safety-Bench eval discipline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("corpus_conditions", "Report retrieval corpus conditions and harmful-query set?"),
    ("base_vs_rag", "Separate base-model refusal from retrieval-conditioned outcomes?"),
    ("judge_named", "Name judge / rubric configuration explicitly?"),
    ("pairs_k323", "Consider upstream poisoning boundary (pairs K323 CodePoisonRAG)?"),
    ("no_scalar_certificate", "Do not treat one scalar as a fleet safety certificate?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"judge_named": False})
    assert not bad and "judge_named" in miss
    print("OK k328_rag_safety_bench_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K328 RAG-Safety-Bench advisory checklist")
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

    print("# K328 RAG-Safety-Bench — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/rag-safety-bench-evaluation.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
