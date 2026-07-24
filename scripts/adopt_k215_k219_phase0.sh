#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/concepts/drone-fl-chained-deauth-impersonation.md \
  wiki/concepts/code-monitor-red-teaming-public-tests.md \
  wiki/concepts/pats-policy-aware-agent-rl-scaffold.md \
  wiki/concepts/thinkink-ink-native-llm-canvas.md \
  wiki/concepts/rf-fingerprint-probe-point-benchmark.md \
  wiki/sources/arxiv-2607-20280-drone-fl-chained-attacks.md \
  wiki/sources/arxiv-2607-20852-code-monitor-red-teaming.md \
  wiki/sources/arxiv-2607-21419-pats-agentic-rl.md \
  wiki/sources/arxiv-2607-21468-thinkink.md \
  wiki/sources/arxiv-2607-21564-rf-fingerprint-probe.md
do
  test -f "$ROOT/$f"
done
echo "ALL PASS k215-k219 pages present (REFERENCE — no local clones)"
