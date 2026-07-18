#!/usr/bin/env bash
# Run adopted local security tools against this wiki's agent surfaces.
# Agent-side: call before ingesting third-party skills / MCP configs, and
# after any local adoption batch.
# User-side actions: briefs/2026-07-18_adopted-tools-use-it-checklist.md
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_DIR="${ROOT}/.scratch/adopted-tool-preflight"
mkdir -p "${REPORT_DIR}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
FAIL=0

need() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "MISSING: $1 not on PATH — see adoption brief"
    FAIL=1
    return 1
  fi
}

echo "== adopted security preflight (${STAMP}) =="
echo "reports → ${REPORT_DIR}"

# --- agentshield: harness config audit ---
if need agentshield; then
  for label_path in "claude:${HOME}/.claude" "cursor:${ROOT}/.cursor"; do
    label="${label_path%%:*}"
    path="${label_path#*:}"
    [[ -d "$path" ]] || continue
    echo ""
    echo "-- agentshield: ${path} --"
    out_md="${REPORT_DIR}/agentshield-${label}-${STAMP}.md"
    out_log="${REPORT_DIR}/agentshield-${label}-${STAMP}.ndjson"
    if ! agentshield scan -p "$path" -f markdown \
      --min-severity medium \
      --supply-chain \
      --log "$out_log" \
      >"$out_md" 2>"${REPORT_DIR}/agentshield-${label}-${STAMP}.err"; then
      echo "agentshield exited non-zero for ${label} (see ${out_md})"
      FAIL=1
    else
      echo "wrote ${out_md}"
    fi
  done
fi

# --- skillspector: static skill scan (no LLM) ---
if need skillspector; then
  SKILL_TARGETS=()
  [[ -d "${ROOT}/.cursor/skills" ]] && SKILL_TARGETS+=("${ROOT}/.cursor/skills")
  for t in "${SKILL_TARGETS[@]}"; do
    echo ""
    echo "-- skillspector --no-llm: ${t} --"
    base="$(basename "$t")"
    if ! skillspector scan "$t" --no-llm --recursive \
      --format markdown \
      --output "${REPORT_DIR}/skillspector-${base}-${STAMP}.md" 2>&1 \
      | tee "${REPORT_DIR}/skillspector-${base}-${STAMP}.log"; then
      FAIL=1
    fi
  done
  # reverse-skill is a multi-skill offensive pack — never treat repo-root as one skill
  if [[ -d "${ROOT}/raw-sources/repos/reverse-skill" ]]; then
    echo ""
    echo "-- skillspector note: reverse-skill is a pack; sample one CTF skill only --"
    sample="$(find "${ROOT}/raw-sources/repos/reverse-skill" -name SKILL.md -type f | head -1 | xargs -I{} dirname "{}")"
    if [[ -n "$sample" && -d "$sample" ]]; then
      if ! skillspector scan "$sample" --no-llm --format markdown \
        --output "${REPORT_DIR}/skillspector-reverse-skill-sample-${STAMP}.md" 2>&1 \
        | tee "${REPORT_DIR}/skillspector-reverse-skill-sample-${STAMP}.log"; then
        FAIL=1
      fi
    fi
  fi
fi

# --- defenseclaw skill-scanner (per skill directory) ---
if need skill-scanner; then
  if [[ -d "${ROOT}/.cursor/skills" ]]; then
    echo ""
    echo "-- skill-scanner: ${ROOT}/.cursor/skills/* --"
    shopt -s nullglob
    for skill_dir in "${ROOT}/.cursor/skills"/*/; do
      name="$(basename "$skill_dir")"
      [[ -f "${skill_dir}/SKILL.md" ]] || continue
      echo "  scanning ${name}"
      if ! skill-scanner scan "$skill_dir" --format summary \
        --fail-on-severity critical \
        >"${REPORT_DIR}/skill-scanner-${name}-${STAMP}.log" 2>&1; then
        echo "  FAIL ${name} (see log)"
        FAIL=1
      else
        echo "  OK ${name}"
      fi
    done
    shopt -u nullglob
  fi
fi

if command -v defenseclaw >/dev/null 2>&1; then
  echo ""
  echo "-- defenseclaw version --"
  defenseclaw version 2>&1 | tee "${REPORT_DIR}/defenseclaw-version-${STAMP}.log" || true
fi

echo ""
if [[ "${FAIL}" -ne 0 ]]; then
  echo "PREFLIGHT finished with failures (see ${REPORT_DIR})"
  exit 1
fi
echo "PREFLIGHT OK — reports in ${REPORT_DIR}"
exit 0
