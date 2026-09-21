#!/usr/bin/env bash
# Phase-0 verify — K351–K354 batch + OOD stub (2026-09-21 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-20909-tpm-attest-hardware-rooted-integrity-attestation.md \
  wiki/concepts/tpm-attest-linux-integrity-attestation.md \
  wiki/sources/arxiv-2609-21996-lie-detector-probe-internal-recognition.md \
  wiki/concepts/probe-internal-recognition-sandbagging-audit.md \
  wiki/sources/arxiv-2609-22048-available-guardrails-selective-prediction.md \
  wiki/concepts/certified-selective-prediction-guardrails.md \
  wiki/sources/arxiv-2609-22024-pv-care-ood.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K351 TPM-Attest" "$ROOT/.cursor/rules/cemini-cybersec-agent-containment.mdc"
grep -q "K352 PIR" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K352 PIR" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K354 Available Guardrails" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K351 TPM-Attest" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k352_pir_sandbagging_precheck.py" >/dev/null

echo "ALL PASS K351-K354 Phase-0"
