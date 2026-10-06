#!/usr/bin/env bash
# Phase-0 verify — K398-K402 (2026-10-06 B).
# K398/K400/K402: no artifact adopted -> REFERENCE.
# K399: repo SaFo-Lab/Red-TTT exists; attack tooling -> REFERENCE, never clone.
# K401: OOD (diffusion interpretability) -> stub only, routed to image-gen.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2610-04693-penumbra-regulatory-obligation-adversarial-search.md \
  wiki/concepts/compliance-boundary-adjacent-pair-search.md \
  wiki/sources/arxiv-2610-05282-red-ttt-test-time-training-jailbreak.md \
  wiki/concepts/test-time-training-redteam-attacker.md \
  wiki/sources/arxiv-2610-05346-mosaic-attacks-sequential-fragment-defense.md \
  wiki/concepts/mosaic-attack-bounded-window-insufficiency.md \
  wiki/sources/arxiv-2610-06844-contextual-reader-diffusion-transformers-ood.md \
  wiki/sources/arxiv-2610-06848-transcope-hardware-membership-inference.md \
  wiki/concepts/hardware-membership-inference-microarchitecture.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

test -z "$(find "$ROOT/wiki" -name '*.md.md' -print -quit)" \
  || { echo "FAIL a page has a doubled .md extension"; exit 1; }

# No clones: Red-TTT is attack tooling; the rest have no artifact.
for bad in \
  "$ROOT/.local/adopts/Red-TTT" \
  "$ROOT/.local/adopts/RedTTT" \
  "$ROOT/.local/adopts/mosaic" \
  "$ROOT/.local/adopts/TransScope" \
  "$ROOT/raw-sources/repos/Red-TTT" \
  "$ROOT/raw-sources/repos/TransScope"
do
  test ! -e "$bad" || { echo "FAIL clone present for a REFERENCE-only paper: $bad"; exit 1; }
done

grep -q "K400 mosaic" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K398 Penumbra" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K402 TransScope" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K398" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K402" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K398" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k400_mosaic_session_guard_precheck.py" selftest
test -f "$ROOT/.cursor/skills/mosaic-session-guard-precheck/SKILL.md"

echo "ALL PASS K398-K402 Phase-0"
