#!/usr/bin/env bash
# K316–K319 artifact re-hunt: SIR HF space, EvoSkill benches, BLOOM-WILT repo.
# No attack templates. No clone until SPDX verified + operator OK.
# Exit 1 if a forbidden clone exists on disk, 3 if a gh lookup failed; otherwise 0.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
. "$ROOT/scripts/gh_lookup.sh"
GH_LOOKUP_FAILED=0

echo "== K316 SIR / TrustSafeAI =="
for repo in TrustSafeAI/SIR; do
  if gh_repo_exists "$repo"; then
    spdx="$(gh_repo_spdx "$repo")"
    case "$spdx" in
      "$GH_MISSING_SENTINEL") spdx="repo-vanished" ;;
      "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; spdx="unknown" ;;
    esac
    echo "  WATCH ${repo} spdx=${spdx}"
  else
    case "$?" in
      1) echo "  SIR GitHub repo: not found — HF space TrustSafeAI/SIR WATCH only" ;;
      *) GH_LOOKUP_FAILED=1; echo "  SIR repo: lookup failed — see error above" ;;
    esac
  fi
done

# Name-shaped fallback. The old query was the arXiv id plus a title fragment
# ("2608.30207 SIR red-teaming computer use"); gh search matches name and
# description only, so it could never hit. The exact-slug check above is the
# authoritative lookup — this only catches a repo named after the technique.
SIR_HITS="$(gh_search_repos 3 fullName,description "SIR red-teaming in:name,description")"
if [[ "$SIR_HITS" == "$GH_FAIL_SENTINEL" ]]; then
  GH_LOOKUP_FAILED=1
  echo "  arXiv hunt: lookup failed — result unknown, not 'none'"
elif [[ -z "$SIR_HITS" || "$SIR_HITS" == "[]" ]]; then
  echo "  arXiv hunt: no name/description match"
else
  echo "$SIR_HITS" | python3 -c "
import sys, json
for r in json.load(sys.stdin):
    print('  candidate', r.get('fullName'))
"
fi

echo "== K317 EvoSkill Injection / SARGE =="
EVO_HITS="$(gh_search_repos 8 fullName,description,license "EvoSkillBench OR EvoSkillSafetyBench OR SARGE evoskill in:name,description,readme")"
if [[ "$EVO_HITS" == "$GH_FAIL_SENTINEL" ]]; then
  GH_LOOKUP_FAILED=1
  echo "  EvoSkillBench/SARGE: lookup failed — result unknown, not 'not found'"
elif [[ -z "$EVO_HITS" || "$EVO_HITS" == "[]" ]]; then
  echo "  EvoSkillBench/SARGE repo: not found (expected — paper promises release at arXiv 2608.30429)"
else
  # gh search exposes license.key, not license.spdx_id. Confirm with gh api before any adopt.
  echo "$EVO_HITS" | python3 -c "
import sys, json
for r in json.load(sys.stdin):
    lic = (r.get('license') or {}).get('key') or 'none'
    print('  candidate', r.get('fullName'), '| license:', lic)
"
fi
echo "HOLD EvoSkill clone — no SPDX-verified bench $(date +%F)"

echo "== K319 BLOOM-WILT =="
BW_REPO="AdrSkapars/bloom-wilt"
if gh_repo_exists "$BW_REPO"; then
  spdx="$(gh_repo_spdx "$BW_REPO")"
  case "$spdx" in
    "$GH_MISSING_SENTINEL") spdx="repo-vanished" ;;
    "$GH_FAIL_SENTINEL") GH_LOOKUP_FAILED=1; spdx="unknown" ;;
  esac
  if [[ "$spdx" == "unknown" ]]; then
    echo "  ${BW_REPO}: license lookup failed — SPDX unknown"
  else
    echo "  ${BW_REPO} spdx=${spdx}"
    if [[ "$spdx" != "null" && -n "$spdx" ]]; then
      echo "  ACTION: SPDX present — operator may run Phase-0 clone review (still no auto-clone)"
    else
      echo "  HOLD BLOOM-WILT clone — license null $(date +%F)"
    fi
  fi
else
  case "$?" in
    1) echo "  ${BW_REPO}: not found" ;;
    *) GH_LOOKUP_FAILED=1; echo "  ${BW_REPO}: lookup failed — see error above" ;;
  esac
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

if [[ "$GH_LOOKUP_FAILED" -ne 0 ]]; then
  echo "FAIL: at least one gh lookup failed — results above are incomplete, not empty"
  exit 3
fi

exit 0
