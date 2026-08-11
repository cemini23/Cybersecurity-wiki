#!/usr/bin/env bash
# Phase-0 verify — K267 ILL (REFERENCE) + K268 SHE (GO clone) + K269 Taboo (REFERENCE) + OOD routes
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md \
  wiki/concepts/inaudible-low-frequency-audio-attacks.md \
  wiki/entities/tools/ill-inaudible-low-frequency-lockout.md \
  wiki/sources/arxiv-2608-09885-she-safety-harness-evolution.md \
  wiki/concepts/safety-harness-evolution.md \
  wiki/entities/tools/she-safety-harness-evolution.md \
  wiki/sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md \
  wiki/concepts/decoding-level-taboo-diagnostic.md \
  wiki/sources/arxiv-2608-06866-ood-dodtrack-wifi-doppler-tracking.md \
  wiki/sources/arxiv-2608-09930-ood-beyond-naturalness-tts-eval.md
do
  test -f "$ROOT/$f"
done
test -d "$ROOT/raw-sources/repos/SHE"
test -f "$ROOT/raw-sources/repos/SHE/LICENSE"
rg -q 'Apache' "$ROOT/raw-sources/repos/SHE/LICENSE"
test "$(git -C "$ROOT/raw-sources/repos/SHE" rev-parse HEAD)" = "0c656460d9d8acdf406a2271d657f7a7b60bb255"
SZ=$(du -sk "$ROOT/raw-sources/repos/SHE" | awk '{print $1}')
test "$SZ" -lt 512000
rg -q 'SHE / K268' "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
rg -q 'K267 ILL' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
rg -q 'K269 Taboo' "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
rg -q 'K269 Taboo' "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
echo "ALL PASS SHE=${SZ}KB @0c656460 (K267 REFERENCE no clone; K268 GO ~${SZ}KB; K269 REFERENCE Zenodo; 06866/09930 OOD stubbed)"
