#!/usr/bin/env bash
# Phase-0 verify — K327–K339 batch + OOD stubs (2026-09-11 ingest).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

for f in \
  wiki/sources/arxiv-2609-09647-black-box-agentic-redteam-taxonomy.md \
  wiki/concepts/black-box-agentic-redteam-taxonomy.md \
  wiki/sources/arxiv-2609-11758-rag-safety-bench.md \
  wiki/concepts/rag-safety-bench-evaluation.md \
  wiki/sources/arxiv-2609-11799-specguard-backdoor-detection.md \
  wiki/concepts/specguard-inference-time-backdoor-detection.md \
  wiki/sources/arxiv-2609-11852-bluestar-tiered-cyber-defense.md \
  wiki/concepts/bluestar-tiered-agentic-cyber-defense.md \
  wiki/sources/arxiv-2609-09087-privescalate-llm-linux-privesc.md \
  wiki/concepts/privescalate-llm-linux-privilege-escalation.md \
  wiki/sources/arxiv-2609-05165-conformal-prediction-offensive-security.md \
  wiki/concepts/conformal-prediction-offensive-security.md \
  wiki/sources/arxiv-2609-05370-llm-decompiler-fidelity.md \
  wiki/concepts/llm-decompiler-recompilability-fidelity.md \
  wiki/sources/arxiv-2609-04159-sentinel-rl-soc-topology.md \
  wiki/concepts/sentinel-rl-soc-topological-reasoning.md \
  wiki/sources/arxiv-2609-05385-llm-explanation-necessary-sufficient.md \
  wiki/concepts/llm-explanation-necessary-sufficient-audit.md \
  wiki/sources/arxiv-2609-06271-side-sensor-impersonation-edge.md \
  wiki/concepts/side-sensor-impersonation-edge-detection.md \
  wiki/sources/arxiv-2609-05741-zero-trust-robotic-fleets.md \
  wiki/concepts/zero-trust-mission-critical-robotic-fleets.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

grep -q "K327 Black-box agentic red-team" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K328 RAG-Safety-Bench" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K331 PrivEscalate" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K327 Black-box agentic red-team" "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"

python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check

python3 "$ROOT/scripts/test_k327_agentic_redteam_precheck.py" >/dev/null
python3 "$ROOT/scripts/test_k328_rag_safety_bench_precheck.py" >/dev/null
python3 "$ROOT/scripts/test_k331_privescalate_precheck.py" >/dev/null

echo "ALL PASS K327-K339 Phase-0"
