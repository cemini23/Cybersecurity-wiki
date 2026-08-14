#!/usr/bin/env bash
# Phase-0 verify — K278 ATOBench (REFERENCE) + K279 MARC-v1 (GO clone) + K280 YAVIN (REFERENCE) + K281 ente (NO clone)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/sources/arxiv-2608-12996-atobench-deceptive-observations.md \
  wiki/concepts/atobench-verification-chain-deception.md \
  wiki/entities/tools/atobench.md \
  wiki/sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md \
  wiki/entities/tools/marc-v1.md \
  wiki/concepts/deterministic-multi-agent-orchestration-failure-attribution.md \
  wiki/sources/arxiv-2608-13496-yavin-secure-edge-pim-tee.md \
  wiki/concepts/pim-tee-untrusted-memory-bus.md \
  wiki/entities/tools/ente.md \
  wiki/concepts/e2ee-consumer-cloud-threat-model.md \
  wiki/sources/arxiv-2608-13463-ood-mllm-routed-ensembles.md
do
  test -f "$ROOT/$f"
done
# MARC clone exists (GO, MIT, shallow)
test -d "$ROOT/raw-sources/repos/MARC-v1"
test -f "$ROOT/raw-sources/repos/MARC-v1/LICENSE"
grep -q "MIT License" "$ROOT/raw-sources/repos/MARC-v1/LICENSE"
# MARC size < 500MB
du_size="$(du -sm "$ROOT/raw-sources/repos/MARC-v1" | cut -f1)"
test "$du_size" -lt 500
# ente must NOT be cloned (AGPL ~704MB > cap)
test ! -d "$ROOT/raw-sources/repos/ente" -a ! -d "$ROOT/.local/adopts/ente"
# ATOBench must NOT be cloned (placeholder)
test ! -d "$ROOT/raw-sources/repos/ATOBench"
# K279 clinical runtime wont_wire; K281 no-clone note present
grep -q "wont_wire" "$ROOT/wiki/sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md"
grep -q "NO clone" "$ROOT/wiki/entities/tools/ente.md"
# Phase-1 wires landed in rule files
grep -q "K278 ATOBench" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K279 MARC" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K280 YAVIN" "$ROOT/.cursor/rules/cemini-cybersec-agent-containment.mdc"
grep -q "K281 ente" "$ROOT/.cursor/rules/cemini-cybersec-agent-containment.mdc"
# index coverage
grep -q "atobench-verification-chain-deception" "$ROOT/wiki/index.md"
grep -q "deterministic-multi-agent-orchestration-failure-attribution" "$ROOT/wiki/index.md"
grep -q "pim-tee-untrusted-memory-bus" "$ROOT/wiki/index.md"
grep -q "e2ee-consumer-cloud-threat-model" "$ROOT/wiki/index.md"
grep -q "marc-v1.md" "$ROOT/wiki/index.md"
echo "ALL PASS K278-K281 (ATOBench REFERENCE; MARC-v1 GO clone ${du_size}MB; YAVIN REFERENCE; ente NO clone; wires lab-redteam+agent-audit/mcp-tool-control/agent-containment)"
