#!/usr/bin/env python3
"""Verify Cybersec dual-ID overlay matches the owned fragment.

Federation rules now sync to ~/.cursor/rules/ only (2026-09-02). The Cybersec
dual-ID list lives in `.cursor/rules/cemini-cybersec-k-dual-id.mdc`; this script
checks it stays in sync with `.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc`.

  python3 scripts/restore_cybersec_dual_id.py --check
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OWNED_RULE = ROOT / ".cursor/rules/cemini-cybersec-k-dual-id.mdc"
FRAGMENT = ROOT / ".cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
START = "## Cybersec wave K282"


def check() -> list[str]:
    errs: list[str] = []
    if not FRAGMENT.is_file():
        errs.append(f"missing overlay {FRAGMENT}")
    if not OWNED_RULE.is_file():
        errs.append(f"missing {OWNED_RULE}")
        return errs
    body = OWNED_RULE.read_text(encoding="utf-8")
    frag = FRAGMENT.read_text(encoding="utf-8") if FRAGMENT.is_file() else ""
    if START not in body and START not in frag:
        errs.append(f"{OWNED_RULE} missing dual-ID heading {START!r}")
    for needle in (
        "K298 Inadvertent Context Leakage (2608.19857)",
        "K303 CLAUDE.md-vs-deny (2608.23550)",
        "K306 LLM-compliance (2608.21317)",
        "K307 StepGuard (2608.24777)",
        "K310 RTLGuard (2608.26049)",
        "K313 RedEvoAgent (2608.27439)",
        "K314 Recognition–enforcement gap (2608.28502)",
        "K315 Security-agent SLR (2608.28490)",
        "K319 BLOOM-WILT (2608.31105)",
        "K320 EvoFlint (2609.00487)",
        "K323 CodePoisonRAG (2609.02774)",
        "K324 SafeEvolve (2609.02786)",
        "K325 Linguistic illegibility (2609.02852)",
        "K300–K306, K307–K309, and K310–K326 Cybersec entries",
    ):
        if needle not in body and needle not in frag:
            errs.append(f"dual-ID map missing {needle!r}")
    legacy = ROOT / ".cursor/rules/cemini-phase1-policy-wires.mdc"
    if legacy.is_file():
        errs.append(
            f"retire project copy {legacy} — federation phase1 catalog is global-only"
        )
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="verify owned rule + fragment")
    ap.add_argument("--file", type=Path, help="deprecated; ignored")
    args = ap.parse_args()
    if not args.check:
        print(
            "restore mode retired — dual-ID lives in cemini-cybersec-k-dual-id.mdc. "
            "Use --check only.",
            file=sys.stderr,
        )
        return 0
    errs = check()
    if errs:
        print("FAIL dual-ID:\n  " + "\n  ".join(errs), file=sys.stderr)
        return 1
    print("OK dual-ID owned rule + fragment")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
