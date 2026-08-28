#!/usr/bin/env bash
# Phase-0 verify — K310 RTLGuard + K311 CTF-ABACUS + K312 LoopHarness + K313 RedEvoAgent + 5 OOD.
# All in-scope are REFERENCE (no public paper repo at hunt). No clones. No attack-skill payloads.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# 1. Every page listed in the ingest plan (C) exists.
for f in \
  wiki/sources/arxiv-2608-26049-rtlguard.md \
  wiki/concepts/rtl-codegen-poison-defense.md \
  wiki/sources/arxiv-2608-26237-ctf-abacus.md \
  wiki/concepts/trace-verified-ctf-agent-eval.md \
  wiki/sources/arxiv-2608-27141-safety-does-not-compose.md \
  wiki/concepts/non-decaying-loop-safety-state.md \
  wiki/sources/arxiv-2608-27439-redevoagent.md \
  wiki/concepts/experience-driven-redteam-skill-evolution.md \
  wiki/sources/arxiv-2608-25612-ood-wifi-respiratory-csi.md \
  wiki/sources/arxiv-2608-26086-ood-traceml.md \
  wiki/sources/arxiv-2608-26103-ood-zero-wam.md \
  wiki/sources/arxiv-2608-27417-ood-vlm-retrieval-heads.md \
  wiki/sources/arxiv-2608-27420-ood-weak-model-rlvr.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# 2. Forbidden clones (name-collision repos are NOT these papers). No clone this batch.
for bad in \
  "$ROOT/.local/adopts/RTLGuard" \
  "$ROOT/.local/adopts/RTLGuardai" \
  "$ROOT/.local/adopts/ctf-abacus" \
  "$ROOT/.local/adopts/AbacusCTF" \
  "$ROOT/.local/adopts/LoopHarness" \
  "$ROOT/.local/adopts/loopharness" \
  "$ROOT/.local/adopts/RedEvoAgent" \
  "$ROOT/.local/adopts/TraceML" \
  "$ROOT/raw-sources/repos/RTLGuardai" \
  "$ROOT/raw-sources/repos/ctf-abacus" \
  "$ROOT/raw-sources/repos/AbacusCTF" \
  "$ROOT/raw-sources/repos/LoopHarness" \
  "$ROOT/raw-sources/repos/loopharness" \
  "$ROOT/raw-sources/repos/RedEvoAgent" \
  "$ROOT/raw-sources/repos/TraceML"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

# 3. K310–K313 wired into Phase-1 rules.
grep -q "K310 RTLGuard" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K311" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K312" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K313 RedEvoAgent" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K310 RTLGuard" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

# 4. Dual-ID restore check.
python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

# 5. Index slugs present.
for slug in \
  arxiv-2608-26049-rtlguard \
  rtl-codegen-poison-defense \
  arxiv-2608-26237-ctf-abacus \
  trace-verified-ctf-agent-eval \
  arxiv-2608-27141-safety-does-not-compose \
  non-decaying-loop-safety-state \
  arxiv-2608-27439-redevoagent \
  experience-driven-redteam-skill-evolution \
  arxiv-2608-25612-ood-wifi-respiratory-csi \
  arxiv-2608-26086-ood-traceml \
  arxiv-2608-26103-ood-zero-wam \
  arxiv-2608-27417-ood-vlm-retrieval-heads \
  arxiv-2608-27420-ood-weak-model-rlvr
do
  grep -q "$slug" "$ROOT/wiki/index.md" || { echo "FAIL index missing slug: $slug"; exit 1; }
done

# 6. K312 runtime (local accumulator; paper artifact still uncloned).
test -f "$ROOT/scripts/k312_loop_state.py" || { echo "FAIL missing k312_loop_state.py"; exit 1; }
test -f "$ROOT/scripts/test_k312_loop_state.py" || { echo "FAIL missing test_k312_loop_state.py"; exit 1; }
grep -q "k312_loop_state.py --hook" "$ROOT/.cursor/hooks.json" || { echo "FAIL hooks.json missing K312"; exit 1; }
grep -q "k312_loop_state.py" "$ROOT/wiki/concepts/non-decaying-loop-safety-state.md" || { echo "FAIL concept missing runtime path"; exit 1; }
python3 "$ROOT/scripts/test_k312_loop_state.py" >/dev/null

echo "ALL PASS K310-K313 Phase-0 + K312 runtime"
