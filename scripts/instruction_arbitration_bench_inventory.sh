#!/usr/bin/env bash
# K314 InstructionArbitrationBench + author-repo re-hunt. No attack templates in wiki. No clone until IAB SPDX verified.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "== K314 InstructionArbitrationBench hunt =="
IAB_HITS="$(gh search repos "InstructionArbitrationBench in:name,description,readme" --limit 5 --json nameWithOwner,description 2>/dev/null || echo '[]')"
if [[ "$IAB_HITS" == "[]" || -z "$IAB_HITS" ]]; then
  echo "  IAB repo: not found (expected — paper promises release at arXiv 2608.28502)"
  echo "HOLD IAB clone — bench not public $(date +%F); re-hunt via k307_k315_rehunt.sh"
else
  echo "$IAB_HITS" | python3 -c "import sys,json; [print('  candidate', r.get('nameWithOwner')) for r in json.load(sys.stdin)]"
  echo "HOLD IAB clone — verify SPDX + paper match before any adopt $(date +%F)"
fi

echo "== Author adjacent repos (WATCH — not auto-adopt) =="
for repo in junwenleong/stateful-agent-security-eval; do
  spdx="$(gh api "repos/${repo}" --jq '.license.spdx_id // "null"' 2>/dev/null || echo "missing")"
  desc="$(gh api "repos/${repo}" --jq '.description // ""' 2>/dev/null | head -c 80)"
  echo "  WATCH ${repo} spdx=${spdx} — ${desc}"
done

for bad in \
  "$ROOT/.local/adopts/InstructionArbitrationBench" \
  "$ROOT/raw-sources/repos/InstructionArbitrationBench"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

exit 0