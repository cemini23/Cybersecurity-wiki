#!/usr/bin/env python3
"""K376 advisory precheck — noncanonical token inference-cost audit."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("owned_or_procured", "Eval only owned or contractually procured models (no third-party attack training)?"),
    ("tir_vs_visible", "Report token count against visible response length (TIR-style)?"),
    ("model_provenance", "Record model source, fine-tune lineage, and tokenizer identity?"),
    ("canonical_tokenizer", "Keep tokenizer and decode path vendor-canonical during serving?"),
    ("no_fragtoken_training", "Do not train or fine-tune a FragToken-style fragmentation model?"),
    ("no_wiki_payloads", "No fragmentation recipes, token-split tables, or attack code in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"no_fragtoken_training": False})
    assert not bad and "no_fragtoken_training" in miss
    print("OK k376_fragtoken_cost_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K376 FragToken cost-audit advisory checklist")
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

    print("# K376 FragToken noncanonical token cost — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/fragtoken-noncanonical-token-cost-audit.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
