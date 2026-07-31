#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/concepts/tca-sir-target-conditioned-inspiration-retrieval.md \
  wiki/concepts/cogate-confidence-gated-secure-code.md \
  wiki/concepts/aispa-system-prompt-assurance-audit.md \
  wiki/sources/arxiv-2607-28498-tca-sir-scientific-inspiration.md \
  wiki/sources/arxiv-2607-28529-cogate-secure-code-codecoding.md \
  wiki/sources/arxiv-2607-28617-aispa-system-prompt-auditing.md \
  wiki/entities/tools/system-prompt-index.md
do
  test -f "$ROOT/$f"
done
# Ensure we did NOT clone unlicensed SystemPromptIndex
if [ -d "$ROOT/raw-sources/repos/SystemPromptIndex" ]; then
  echo "FAIL: SystemPromptIndex cloned without LICENSE — remove" >&2
  exit 1
fi
echo "ALL PASS k230-k232 REFERENCE (no local clones; SystemPromptIndex LICENSE watch)"
