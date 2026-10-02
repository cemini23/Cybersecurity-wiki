#!/usr/bin/env bash
# Phase-0 verify — K387-K391 (2026-10-02).
# K387/K388/K389/K390: REFERENCE, no public artifact adopted.
# K391 KaliBench: repo exists (github.com/RISys-Lab/KaliBench) but returns null SPDX with no LICENSE
# file and no README licence text, so the paper's CC BY-NC 4.0 claim is unverified — NO-GO on clone.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2610-00590-hierarchical-llm-cyber-defense.md \
  wiki/concepts/hierarchical-llm-cyber-defense-planner-executor.md \
  wiki/sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md \
  wiki/concepts/benchmark-shortcut-attack-pyramid-audit.md \
  wiki/sources/arxiv-2610-01058-momat-quantized-llm-jailbreak-defense.md \
  wiki/concepts/quantized-llm-jailbreak-defense-atlas.md \
  wiki/sources/arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood.md \
  wiki/concepts/cross-task-no-regression-skill-promotion-gate.md \
  wiki/sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md \
  wiki/concepts/kalibench-nl-to-cli-tool-use-eval.md \
  wiki/concepts/k277-security-wave.md \
  wiki/concepts/k278-security-wave.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# K391 KaliBench: unverified licence -> no clone, and no dataset copied into the tree.
for bad in \
  "$ROOT/.local/adopts/KaliBench" \
  "$ROOT/raw-sources/repos/KaliBench" \
  "$ROOT/raw-sources/repos/RISys-Lab-KaliBench"
do
  test ! -e "$bad" || { echo "FAIL KaliBench clone exists with unverified licence: $bad"; exit 1; }
done
# The bundled dataset must not have been copied either.
test ! -d "$ROOT/raw-sources/KaliBench_data" \
  || { echo "FAIL KaliBench_data present — dataset is unlicensed"; exit 1; }

grep -q "K387" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K387" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K391" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K387" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K391" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "K387" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
grep -q "K300–K3" "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/k391_kalibench_precheck.py" selftest
test -f "$ROOT/.cursor/skills/kalibench-tooluse-precheck/SKILL.md"

echo "ALL PASS K387-K391 Phase-0"
