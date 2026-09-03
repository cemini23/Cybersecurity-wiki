#!/usr/bin/env python3
"""K323 advisory precheck — CodePoisonRAG / RACG poisoning eval discipline."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("written_scope", "Written authorization for owned-lab RACG / code-gen eval target?"),
    ("corpus_ratio_reported", "Report corpus poisoning ratio and Top-k retrieval rank?"),
    ("asr_with_defense", "Report ASR with and without stated context-only defense?"),
    ("no_wiki_poison_bodies", "No poison artifact bodies or CWE injection templates in wiki?"),
    ("ingest_provenance", "Treat retrieved code/docs as supply-chain — provenance + allowlist?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist(
        {k: True for k, _ in CHECKS} | {"no_wiki_poison_bodies": False}
    )
    assert not bad and "no_wiki_poison_bodies" in miss
    print("OK k323_codepoisonrag_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K323 CodePoisonRAG advisory checklist")
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

    print("# K323 CodePoisonRAG — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/codepoisonrag-racg-knowledge-poisoning.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
