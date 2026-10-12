#!/usr/bin/env bash
# Phase-0 verify — K418-K424 (2026-10-12) + K288 NOMOS inbound. All REFERENCE; no clones.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

# Every source page this batch must exist.
for f in \
  wiki/sources/arxiv-2610-05007-aerial-5g-gnb-arm-testbed.md \
  wiki/sources/arxiv-2610-05979-holistic-rffi-vector-quantization.md \
  wiki/sources/arxiv-2610-13307-sustainable-cloud-fog-edge-smart-buildings.md \
  wiki/sources/arxiv-2610-13367-secrets-in-preamble-phy-wifi.md \
  wiki/sources/arxiv-2610-13811-qtestbench-llm-quantum-code-tests.md \
  wiki/sources/arxiv-2610-13886-x-agentred-cross-service-redteam.md \
  wiki/sources/arxiv-2610-13895-task-context-component-roles.md \
  wiki/sources/arxiv-2610-11030-nomos-compiled-policy-tool-gate.md
do
  test -f "$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# No doubled .md extensions anywhere (a repeat emit-script bug).
test -z "$(find wiki -name '*.md.md' -print -quit)" \
  || { echo "FAIL a page has a doubled .md extension"; exit 1; }

# No clone of any tool this batch; all are REFERENCE.
for bad in \
  .local/adopts/RFFI-VQVAE .local/adopts/QTestBench .local/adopts/X-AgentRed \
  raw-sources/repos/RFFI-with-GCD-via-VQVAE raw-sources/repos/QTestBench \
  raw-sources/repos/x-agentred
do
  test ! -e "$bad" || { echo "FAIL clone present for a REFERENCE-only paper: $bad"; exit 1; }
done

# Lane wires.
grep -q "K418 aerial RAN" .cursor/rules/cemini-cybersec-lab-redteam.mdc
grep -q "K419 holistic RFFI" .cursor/rules/cemini-cybersec-lab-redteam.mdc
grep -q "K421 PHY info hiding" .cursor/rules/cemini-cybersec-lab-redteam.mdc
grep -q "K423 X-AgentRed" .cursor/rules/cemini-cybersec-lab-redteam.mdc
grep -q "K422 QTestBench" .cursor/rules/cemini-cybersec-agent-audit.mdc
grep -q "K424 task-context component roles" .cursor/rules/cemini-cybersec-agent-audit.mdc
grep -q "K288 NOMOS" .cursor/rules/cemini-cybersec-agent-audit.mdc

# Dual-ID.
grep -q "K418 Aerial 5G" .cursor/rules/cemini-cybersec-k-dual-id.mdc
grep -q "K424 Task-context component roles" .cursor/rules/cemini-cybersec-k-dual-id.mdc
grep -q "K300–K4" .cursor/rules/cemini-cybersec-k-dual-id.mdc
grep -q "K418 Aerial 5G" .cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc
grep -q "K300–K4" .cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc

python3 scripts/restore_cybersec_dual_id.py --check
echo "ALL PASS K418-K424 Phase-0"
