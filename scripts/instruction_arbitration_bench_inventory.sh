#!/usr/bin/env bash
# K314 InstructionArbitrationBench + author-repo re-hunt. No attack templates in wiki. No clone until IAB SPDX verified.
# Exit 1 if a forbidden clone exists on disk, 3 if a gh lookup failed; otherwise 0.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/gh_lookup.sh"
GH_LOOKUP_FAILED=0

echo "== K314 InstructionArbitrationBench hunt =="
IAB_HITS="$(gh_search_repos 5 fullName,description "InstructionArbitrationBench in:name,description,readme")"
if [[ "$IAB_HITS" == "$GH_FAIL_SENTINEL" ]]; then
  GH_LOOKUP_FAILED=1
  echo "  IAB repo: lookup failed — result unknown, not 'not found'"
elif [[ -z "$IAB_HITS" || "$IAB_HITS" == "[]" ]]; then
  echo "  IAB repo: not found (expected — paper promises release at arXiv 2608.28502)"
  echo "HOLD IAB clone — bench not public $(date +%F); re-hunt via k307_k315_rehunt.sh"
else
  echo "$IAB_HITS" | python3 -c "import sys,json; [print('  candidate', r.get('fullName')) for r in json.load(sys.stdin)]"
  echo "HOLD IAB clone — verify SPDX + paper match before any adopt $(date +%F)"
fi

echo "== Author adjacent repos (WATCH — not auto-adopt) =="
for repo in junwenleong/stateful-agent-security-eval; do
  if gh_repo_exists "$repo"; then
    spdx="$(gh_repo_spdx "$repo")"
    case "$spdx" in
      "$GH_MISSING_SENTINEL") spdx="repo-vanished" ;;
      "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; spdx="unknown" ;;
    esac
    desc="$(gh_repo_field "$repo" '.description // ""')"
    case "$desc" in
      "$GH_MISSING_SENTINEL") desc="" ;;
      "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; desc="" ;;
    esac
    echo "  WATCH ${repo} spdx=${spdx} — $(printf '%s' "$desc" | head -c 80)"
  else
    case "$?" in
      1) echo "  WATCH ${repo}: not found" ;;
      *) GH_LOOKUP_FAILED=1; echo "  WATCH ${repo}: lookup failed — see error above" ;;
    esac
  fi
done

for bad in \
  "$ROOT/.local/adopts/InstructionArbitrationBench" \
  "$ROOT/raw-sources/repos/InstructionArbitrationBench"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

if [[ "$GH_LOOKUP_FAILED" -ne 0 ]]; then
  echo "FAIL: at least one gh lookup failed — results above are incomplete, not empty"
  exit 3
fi

exit 0
