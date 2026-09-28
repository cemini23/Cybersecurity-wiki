#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
CHECKS = [('written_scope', 'Written scope for skill-interaction eval on owned lab?'), ('skill_graph', 'Inventory skills+order+shared tools?'), ('no_auto_evolve', 'No auto-evolve skills from red-team runs?'), ('preflight', 'cursor-security-preflight before third-party skills?'), ('no_wiki_payloads', 'No cascade recipes in wiki?')]

def run_checklist(a):
    m=[k for k,_ in CHECKS if not a.get(k)]
    return len(m)==0,m

def selftest():
    ok,_=run_checklist({k:True for k,_ in CHECKS})
    assert ok
    print('OK k374 selftest')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('cmd',choices=('checklist','selftest','json'))
    ap.add_argument('--json',dest='jp')
    args=ap.parse_args()
    if args.cmd=='selftest':
        selftest(); return 0
    if args.cmd=='json':
        d=json.loads(Path(args.jp).read_text())
        ok,m=run_checklist({k:d.get(k)is True for k,_ in CHECKS})
        print(json.dumps({'ok':ok,'missing':m})); return 0 if ok else 2
    for k, label in CHECKS:
        print(f"- [ ] {label}  (`{k}`)")
    print("\nCanon: wiki/concepts/skill-cascading-attacks-skill-based-agents.md")
    return 0
if __name__=='__main__': raise SystemExit(main())
