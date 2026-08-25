#!/usr/bin/env python3
"""Re-insert the Cybersec dual-ID block after CCC federation overwrite.

CCC copies cemini-phase1-policy-wires.mdc from the CCC canon, which does not
carry Cybersec K282–K306 dual-IDs. Run this after that copy (and from CI).

  python3 scripts/restore_cybersec_dual_id.py
  python3 scripts/restore_cybersec_dual_id.py --check
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FILE = ROOT / ".cursor/rules/cemini-phase1-policy-wires.mdc"
FRAGMENT = ROOT / ".cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
START = "## Cybersec wave K282"
PHASE1 = "## Phase-1 meta"
BPS = "## Skill-set budget"


def _section_pattern() -> re.Pattern[str]:
    return re.compile(
        rf"^{re.escape(START)}.*?(?=^## |\Z)",
        re.M | re.S,
    )


def restore(path: Path, fragment: str) -> bool:
    text = path.read_text(encoding="utf-8")
    frag = fragment.strip() + "\n\n"
    text = _section_pattern().sub("", text)
    if PHASE1 in text:
        text = text.replace(PHASE1, frag + PHASE1, 1)
    elif BPS in text:
        text = text.rstrip() + "\n\n" + frag
    else:
        text = text.rstrip() + "\n\n" + frag
    text = re.sub(r"\n{3,}", "\n\n", text)
    path.write_text(text, encoding="utf-8")
    return START in path.read_text(encoding="utf-8")


def check(path: Path) -> list[str]:
    errs: list[str] = []
    if not FRAGMENT.is_file():
        errs.append(f"missing overlay {FRAGMENT}")
    if not path.is_file():
        errs.append(f"missing {path}")
        return errs
    body = path.read_text(encoding="utf-8")
    if START not in body:
        errs.append(f"{path} missing dual-ID heading {START!r}")
    for needle in (
        "K298 Inadvertent Context Leakage (2608.19857)",
        "K303 CLAUDE.md-vs-deny (2608.23550)",
        "K306 LLM-compliance (2608.21317)",
        "Skill-set budget",
        "K300–K306 in this block are Cybersec IDs",
    ):
        if needle not in body:
            errs.append(f"{path} missing {needle!r}")
    if BPS in body and START in body:
        if body.find(BPS) > body.find(START):
            errs.append("dual-ID block must come AFTER BPS/Wayfinder")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", type=Path, default=DEFAULT_FILE)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.check:
        errs = check(args.file)
        if errs:
            print("FAIL dual-ID:\n  " + "\n  ".join(errs), file=sys.stderr)
            return 1
        print("OK dual-ID present after BPS/Wayfinder")
        return 0
    if not FRAGMENT.is_file():
        print(f"FAIL missing {FRAGMENT}", file=sys.stderr)
        return 1
    fragment = FRAGMENT.read_text(encoding="utf-8")
    if not restore(args.file, fragment):
        print("FAIL restore did not insert heading", file=sys.stderr)
        return 1
    print(f"OK restored dual-ID into {args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
