#!/usr/bin/env bash
# K316–K319 artifact re-hunt: SIR HF space, EvoSkill benches, BLOOM-WILT repo.
# No attack templates. No clone until SPDX verified + operator OK.
# Exit 1 if forbidden clone exists on disk; otherwise exit 0.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "== K316 SIR / TrustSafeAI =="
for repo in TrustSafeAI/SIR; do
  if gh api "repos/${repo}" --jq '.full_name' >/dev/null 2>&1; then
    spdx="$(gh api "repos/${repo}" --jq '.license.spdx_id // "null"' 2>/dev/null || echo "null")"
    echo "  WATCH ${repo} spdx=${spdx}"
  else
    echo "  SIR GitHub repo: not found — HF space TrustSafeAI/SIR WATCH only"
  fi
done
SIR_HITS="$(gh search repos "2608.30207 SIR red-teaming computer use" --limit 3 --json nameWithOwner 2>/dev/null || true)"
if [[ -z "$SIR_HITS" ]]; then
  echo "  arXiv hunt: skipped"
else
  echo "$SIR_HITS" | python3 -c "
import sys, json
raw = sys.stdin.read().strip()
if not raw:
    print('  arXiv hunt: none')
else:
    d = json.loads(raw)
    print('  arXiv hunt:', [r['nameWithOwner'] for r in d] or 'none')
" 2>/dev/null || echo "  arXiv hunt: skipped"
fi

echo "== K317 EvoSkill Injection / SARGE =="
EVO_HITS="$(gh search repos "EvoSkillBench OR EvoSkillSafetyBench OR SARGE evoskill in:name,description,readme" --limit 8 --json nameWithOwner 2>/dev/null || echo '[]')"
if [[ "$EVO_HITS" == "[]" || -z "$EVO_HITS" ]]; then
  echo "  EvoSkillBench/SARGE repo: not found (expected — paper promises release at arXiv 2608.30429)"
else
  echo "$EVO_HITS" | python3 -c "import sys,json; [print('  candidate', r.get('nameWithOwner')) for r in json.load(sys.stdin)]"
fi
echo "HOLD EvoSkill clone — no SPDX-verified bench $(date +%F)"

echo "== K319 BLOOM-WILT =="
BW_REPO="AdrSkapars/bloom-wilt"
if gh api "repos/${BW_REPO}" --jq '.full_name' >/dev/null 2>&1; then
  spdx="$(gh api "repos/${BW_REPO}" --jq '.license.spdx_id // "null"' 2>/dev/null || echo "null")"
  echo "  ${BW_REPO} spdx=${spdx}"
  if [[ "$spdx" != "null" && -n "$spdx" ]]; then
    echo "  ACTION: SPDX present — operator may run Phase-0 clone review (still no auto-clone)"
  else
    echo "  HOLD BLOOM-WILT clone — license null $(date +%F)"
  fi
else
  echo "  ${BW_REPO}: not found"
fi

for bad in \
  "$ROOT/.local/adopts/bloom-wilt" \
  "$ROOT/.local/adopts/SIR" \
  "$ROOT/.local/adopts/EvoSkillBench" \
  "$ROOT/raw-sources/repos/bloom-wilt" \
  "$ROOT/raw-sources/repos/AdrSkapars-bloom-wilt"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

exit 0
