#!/usr/bin/env bash
# Pre-commit hook for OSINT WORKSPACE — blocks accidental leaks.
#
# Versioned at scripts/pre-commit.sh; install via scripts/install-hooks.sh
# (which symlinks .git/hooks/pre-commit to this file).
#
# Blocks:
#   - Filenames matching .env / .DS_Store
#   - Staged content additions matching:
#       * the literal Hetzner server IP (from .local/server.md)
#       * sk-... API key prefix (catches OpenAI/DeepSeek/Anthropic-style keys)
#
# Only ADDED lines are scanned (`git diff --cached -U0` filtered to ^+),
# so historical occurrences in untouched parts of files don't trip the hook.
# The hook itself is excluded from content scanning so its own regex strings
# don't false-positive.
#
# To bypass intentionally (e.g. a documented test pattern):
#   git commit --no-verify

set -euo pipefail

violations=()

# --- Filename-based blocks ---------------------------------------------------

while IFS= read -r f; do
    [[ -z "$f" ]] && continue
    # .env at any path depth, with or without a suffix (.env, .env.local, etc.)
    if [[ "$(basename "$f")" =~ ^\.env(\..*)?$ ]]; then
        violations+=("FILENAME — $f (matches .env*)")
    fi
    # .DS_Store at any path depth
    if [[ "$(basename "$f")" == ".DS_Store" ]]; then
        violations+=("FILENAME — $f (.DS_Store)")
    fi
done < <(git diff --cached --name-only --diff-filter=AM)

# --- Content-based blocks (added lines only) ---------------------------------

# Build pattern from parts so this hook script's source doesn't itself contain
# the literal IP it's blocking (would otherwise trip on its own initial commit).
SERVER_IP_RE='5\.16'"1"'\.53\.103'
# API-key regex requires a non-word char (or start-of-line) immediately before
# 'sk-' so URL fragments like '.../Risk-Premiums-of-Equity-...' don't match
# at the 'sk-Premiums-...' substring (false-positive seen during ingest N on
# 2026-04-27 in a CME Group URL inside the SPY Gemini DR baseline). Real
# OpenAI / DeepSeek / Anthropic keys are always surrounded by whitespace,
# quotes, or start-of-string when staged, so this remains safe.
API_KEY_RE='(^|[^A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}'

# Extract added lines from staged diff, excluding the hook itself.
added_lines=$(
    git diff --cached --diff-filter=AM -U0 -- ':(exclude)scripts/pre-commit.sh' \
        | grep -E '^\+[^+]' \
        || true
)

if [[ -n "$added_lines" ]]; then
    if echo "$added_lines" | grep -E -q "$SERVER_IP_RE"; then
        violations+=("CONTENT — server IP found in staged additions")
    fi
    if echo "$added_lines" | grep -E -q "$API_KEY_RE"; then
        violations+=("CONTENT — API key pattern (sk-…) found in staged additions")
    fi
fi

# --- Report and exit ---------------------------------------------------------

if (( ${#violations[@]} > 0 )); then
    echo ""
    echo "================================================================"
    echo "  pre-commit hook BLOCKED commit"
    echo "================================================================"
    printf '  • %s\n' "${violations[@]}"
    echo ""
    echo "  If this is a documented test pattern or you have reviewed and"
    echo "  understand the risk, bypass with: git commit --no-verify"
    echo "================================================================"
    echo ""
    exit 1
fi

exit 0
