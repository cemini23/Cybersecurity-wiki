#!/usr/bin/env bash
# Phase-0 verify — K403-K407 (2026-10-07).
# All five REFERENCE: no artifact adopted, no clone this batch.
# K407 is OOD (research ideation) -> stub only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2610-07323-atlas-al-adversarial-region-active-learning.md \
  wiki/concepts/adversarial-region-estimation-vs-single-example.md \
  wiki/sources/arxiv-2610-07870-post-quantum-ble-pairing-nfc-oob-implant.md \
  wiki/concepts/post-quantum-oob-pairing-medical-implants.md \
  wiki/sources/arxiv-2610-08678-secure-speculative-decoding.md \
  wiki/concepts/speculative-decoding-safety-asymmetry.md \
  wiki/sources/arxiv-2610-08739-bare-ai-bit-flip-resilience.md \
  wiki/concepts/dnn-bit-flip-detection-runtime-monitors.md \
  wiki/sources/arxiv-2610-08781-ideaanchor-research-ideation-ood.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

test -z "$(find "$ROOT/wiki" -name '*.md.md' -print -quit)" \
  || { echo "FAIL a page has a doubled .md extension"; exit 1; }

# No clones this batch.
for bad in \
  "$ROOT/.local/adopts/ATLAS-AL" \
  "$ROOT/.local/adopts/BARE-AI" \
  "$ROOT/.local/adopts/SecureSD" \
  "$ROOT/.local/adopts/IdeaAnchor" \
  "$ROOT/raw-sources/repos/BARE-AI" \
  "$ROOT/raw-sources/repos/IdeaAnchor"
do
  test ! -e "$bad" || { echo "FAIL clone present for a REFERENCE-only paper: $bad"; exit 1; }
done

grep -q "K405 SecureSD" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K403 ATLAS-AL" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K406 BARE-AI" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K407 IdeaAnchor" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K403" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K407" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K403" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k405_inference_optimization_safety_precheck.py" selftest
test -f "$ROOT/.cursor/skills/inference-optimization-safety-precheck/SKILL.md"

echo "ALL PASS K403-K407 Phase-0"
