#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
test -f "$ROOT/wiki/concepts/agent-reconnaissance-ipi-pentesting.md"
test -f "$ROOT/wiki/concepts/ethics-autonomous-offensive-ai-agents.md"
test -f "$ROOT/wiki/concepts/llm-schwartz-value-recognition.md"
test -f "$ROOT/wiki/concepts/llm-probabilistic-safety-bounds.md"
test -f "$ROOT/wiki/concepts/experiential-abstraction-memory.md"
test -d "$ROOT/raw-sources/repos/Notes-to-self"
test -f "$ROOT/raw-sources/repos/Notes-to-self/verl/LICENSE"
rg -q 'Apache' "$ROOT/raw-sources/repos/Notes-to-self/verl/LICENSE"
SZ=$(du -sk "$ROOT/raw-sources/repos/Notes-to-self" | awk '{print $1}')
test "$SZ" -lt 512000
test -f "$ROOT/wiki/entities/tools/notes-to-self.md"
echo "ALL PASS notes-to-self=${SZ}KB"
