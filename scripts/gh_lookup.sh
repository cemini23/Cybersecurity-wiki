#!/usr/bin/env bash
# gh_lookup.sh — shared GitHub lookups that never swallow errors.
#
# Why this file exists: three Cybersec inventory scripts called `gh search repos` with
# `--json nameWithOwner`, a field the installed gh rejects, and ended the call in
# `2>/dev/null || echo '[]'`. The non-zero exit fired the fallback, so a hard failure
# was reported as "no repo found" — indistinguishable from a true negative. See
# briefs/2026-09-30_ccc-gh-inventory-scripts-broken.md (reported by the CCC wiki).
#
# Contract: every function prints a result on stdout. On failure it prints
# GH_FAIL_SENTINEL instead of a result and writes the gh error to stderr. A caller
# must test for the sentinel; it must never treat it as data.
#
#   . "$(dirname "$0")/gh_lookup.sh"
#   GH_LOOKUP_FAILED=0
#   hits="$(gh_search_repos 5 fullName "foo in:name,description")"
#   [[ "$hits" == "$GH_FAIL_SENTINEL" ]] && GH_LOOKUP_FAILED=1
#   ...
#   [[ "$GH_LOOKUP_FAILED" -eq 0 ]] || { echo "FAIL: gh lookup(s) failed"; exit 3; }
#
# Notes on gh fields (verified 2026-09-30):
#   - `gh search repos --json` accepts `fullName` (owner/repo), NOT `nameWithOwner`.
#   - `gh search repos` exposes `license.key`. Only `gh api repos/<slug>` exposes
#     `license.spdx_id`. Mixing the two prints NOASSERTION on every hit.
#   - `gh search repos` matches name and description only. An arXiv id or a title
#     phrase cannot match. Use an exact slug with `gh api` when the paper names one.

GH_LOOKUP_FAILED="${GH_LOOKUP_FAILED:-0}"
GH_FAIL_SENTINEL="__GH_LOOKUP_FAILED__"
GH_MISSING_SENTINEL="__GH_REPO_MISSING__"

# Capture stderr to a scratch file. Falls back if TMPDIR is not writable, so an
# empty path can never turn a real gh error into a confusing "ambiguous redirect".
_gh_tmp() {
  mktemp "${TMPDIR:-/tmp}/gh-err.XXXXXX" 2>/dev/null \
    || mktemp "/tmp/gh-err.XXXXXX" 2>/dev/null \
    || mktemp "./gh-err.XXXXXX"
}

# Classify a gh error file: 1 = HTTP 404 (the thing is absent), 2 = any other error.
_gh_err_is_404() { grep -qiE "HTTP 404|Not Found" "$1"; }

# gh_search_repos <limit> <fields> <query>  → JSON array, or the sentinel.
gh_search_repos() {
  local limit="$1" fields="$2" query="$3" err out
  err="$(_gh_tmp)"
  if out="$(gh search repos "$query" --limit "$limit" --json "$fields" 2>"$err")"; then
    rm -f "$err"
    printf '%s' "$out"
  else
    {
      echo "  LOOKUP FAILED (not an empty result): gh search repos \"$query\""
      sed 's/^/    /' "$err"
    } >&2
    rm -f "$err"
    printf '%s' "$GH_FAIL_SENTINEL"
  fi
}

# gh_repo_field <slug> <jq-expr>  → value, GH_MISSING_SENTINEL on 404, or GH_FAIL_SENTINEL.
gh_repo_field() {
  local slug="$1" jq_expr="$2" err out
  err="$(_gh_tmp)"
  if out="$(gh api "repos/${slug}" --jq "$jq_expr" 2>"$err")"; then
    rm -f "$err"
    printf '%s' "$out"
    return 0
  fi
  if _gh_err_is_404 "$err"; then
    rm -f "$err"
    printf '%s' "$GH_MISSING_SENTINEL"
    return 0
  fi
  {
    echo "  LOOKUP FAILED for ${slug}:"
    sed 's/^/    /' "$err"
  } >&2
  rm -f "$err"
  printf '%s' "$GH_FAIL_SENTINEL"
}

# gh_repo_spdx <slug> → spdx id, or "null" when the repo has no license file.
gh_repo_spdx() { gh_repo_field "$1" '.license.spdx_id // "null"'; }

# gh_repo_path_exists <slug> <path> → exit 0 present, 1 absent, 2 lookup failed.
gh_repo_path_exists() {
  local slug="$1" path="$2" err
  err="$(_gh_tmp)"
  if gh api "repos/${slug}/contents/${path}" >/dev/null 2>"$err"; then
    rm -f "$err"
    return 0
  fi
  if _gh_err_is_404 "$err"; then
    rm -f "$err"
    return 1
  fi
  {
    echo "  LOOKUP FAILED for ${slug}/${path}:"
    sed 's/^/    /' "$err"
  } >&2
  rm -f "$err"
  return 2
}

# gh_repo_exists <slug> → exit 0 exists, 1 not found, 2 lookup failed.
# Safe in an `if`; not a subshell, so it reports failure through its exit code.
gh_repo_exists() {
  local slug="$1" err
  err="$(_gh_tmp)"
  if gh api "repos/${slug}" --jq '.full_name' >/dev/null 2>"$err"; then
    rm -f "$err"
    return 0
  fi
  if _gh_err_is_404 "$err"; then
    rm -f "$err"
    return 1
  fi
  {
    echo "  LOOKUP FAILED for ${slug}:"
    sed 's/^/    /' "$err"
  } >&2
  rm -f "$err"
  return 2
}
