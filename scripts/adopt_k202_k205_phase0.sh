#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
test -f "$ROOT/wiki/concepts/authority-framing-agentic-cicd.md"
test -d "$ROOT/raw-sources/repos/senthex-research"
test -f "$ROOT/raw-sources/repos/senthex-research/LICENSE"
rg -q 'MIT' "$ROOT/raw-sources/repos/senthex-research/LICENSE"
SZ=$(du -sk "$ROOT/raw-sources/repos/senthex-research" | awk '{print $1}'); test "$SZ" -lt 512000
test -d "$ROOT/raw-sources/repos/OC-GRPO"
test -f "$ROOT/raw-sources/repos/OC-GRPO/LICENSE"
SZ2=$(du -sk "$ROOT/raw-sources/repos/OC-GRPO" | awk '{print $1}'); test "$SZ2" -lt 512000
test -f "$ROOT/wiki/concepts/quantum-vqe-adversarial-robustness.md"
test -f "$ROOT/wiki/concepts/evidence-aware-long-context-grounding.md"
echo "ALL PASS senthex=${SZ}KB ocgrpo=${SZ2}KB"
