#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/concepts/ai-redteam-evidential-ceiling.md \
  wiki/concepts/concept2scenario-refusal-suppression.md \
  wiki/concepts/cyber-capable-agent-evaluation-containment.md \
  wiki/concepts/instruction-hierarchy-conflict-benchmark.md \
  wiki/concepts/topology-aware-k8s-llm-remediation.md \
  wiki/sources/arxiv-2607-21735-ai-redteam-evidential-ceiling.md \
  wiki/sources/arxiv-2607-23496-concept2scenario-vulnerable-scenarios.md \
  wiki/sources/arxiv-2607-25379-cyber-capable-agent-containment.md \
  wiki/sources/arxiv-2607-25987-ih-benchmark-instruction-hierarchy.md \
  wiki/sources/arxiv-2607-25995-kutie-topology-k8s-patches.md \
  wiki/entities/tools/ai-redteam-evidential-limits.md \
  wiki/entities/tools/kutie-artifacts.md \
  wiki/entities/tools/vulncare.md
do
  test -f "$ROOT/$f"
done
test -d "$ROOT/raw-sources/repos/ai-redteam-evidential-limits"
test -f "$ROOT/raw-sources/repos/ai-redteam-evidential-limits/LICENSE"
rg -q 'MIT' "$ROOT/raw-sources/repos/ai-redteam-evidential-limits/LICENSE"
SZ1=$(du -sk "$ROOT/raw-sources/repos/ai-redteam-evidential-limits" | awk '{print $1}'); test "$SZ1" -lt 512000
test -d "$ROOT/raw-sources/repos/vulncare"
test -f "$ROOT/raw-sources/repos/vulncare/LICENSE"
rg -q 'Apache' "$ROOT/raw-sources/repos/vulncare/LICENSE"
SZ2=$(du -sk "$ROOT/raw-sources/repos/vulncare" | awk '{print $1}'); test "$SZ2" -lt 512000
test -d "$ROOT/raw-sources/repos/kutie-artifacts"
test -f "$ROOT/raw-sources/repos/kutie-artifacts/LICENSE"
rg -q 'Dynatrace' "$ROOT/raw-sources/repos/kutie-artifacts/LICENSE"
SZ3=$(du -sk "$ROOT/raw-sources/repos/kutie-artifacts" | awk '{print $1}'); test "$SZ3" -lt 512000
echo "ALL PASS evidential=${SZ1}KB vulncare=${SZ2}KB kutie=${SZ3}KB (kutie CONDITIONAL lab-only)"
