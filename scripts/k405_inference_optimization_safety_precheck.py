#!/usr/bin/env python3
"""K405 advisory precheck — safety review before adding an inference optimisation.

Speculative decoding adds a draft model to the token path. That model enters the
trusted computing base: a weak draft raised jailbreak / prompt-injection ASR while
utility barely moved (arXiv 2610.08678). Run this before any such change ships.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CHECKS = (
    ("measures_safety", "Is the safety eval re-run, not just the quality/utility eval?"),
    ("draft_in_tcb", "Is the draft / auxiliary model treated as part of the trusted computing base?"),
    ("swap_tested", "Was a weaker or substituted draft model tested for ASR movement?"),
    ("early_positions", "Are early decoding positions verified more strictly than later ones?"),
    ("utility_and_safety", "Are security and utility reported on the SAME run (asymmetry is invisible otherwise)?"),
    ("owned_or_procured", "Owned or procured models only (no third-party attack training)?"),
    ("no_wiki_payloads", "No jailbreak payloads or decoding exploits in wiki?"),
)


def run_checklist(answers: dict[str, bool]) -> tuple[bool, list[str]]:
    missing = [key for key, _ in CHECKS if not answers.get(key)]
    return len(missing) == 0, missing


def selftest() -> None:
    ok, miss = run_checklist({k: True for k, _ in CHECKS})
    assert ok and not miss
    bad, miss = run_checklist({k: True for k, _ in CHECKS} | {"measures_safety": False})
    assert not bad and "measures_safety" in miss
    print("OK k405_inference_optimization_safety_precheck selftest")


def main() -> int:
    ap = argparse.ArgumentParser(description="K405 inference-optimisation safety checklist")
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

    print("# K405 inference-optimisation safety — advisory checklist\n")
    for key, label in CHECKS:
        print(f"- [ ] {label}  (`{key}`)")
    print("\nCanon: wiki/concepts/speculative-decoding-safety-asymmetry.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
