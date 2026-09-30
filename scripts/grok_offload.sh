#!/usr/bin/env bash
# grok_offload.sh — run a Grok CLI job detached, so a terminal-tab close cannot kill it.
#
# Why: headless `grok -p` / `grok --prompt-file` dies when its terminal tab closes
# mid-run. Long deep-reads (multi-minute, large prompts) then have to be restarted.
# This wrapper starts grok under `nohup` + `disown` with stdin detached, and records
# the result on disk so the caller polls instead of holding a tab open.
#
# macOS has no `setsid`, so `nohup` + `disown` is the detach path here.
#
# MUST run OUTSIDE the Claude Code sandbox: the sandbox denies cli-chat-proxy.grok.com
# and grok's session directory, so grok cannot start inside it.
#
# Invocation notes (see LESSONS.md):
#   - `--cwd` must stay inside the project. Pointing it outside stalls grok.
#   - `--prompt-file` avoids quoting problems on long prompts.
#   - `--output-format plain` writes the answer, not a TUI.
#   - Grok narrates: expect a short preamble line before the real answer.
#
# Usage:
#   bash scripts/grok_offload.sh run <prompt-file> [--name NAME] [--cwd DIR]
#   bash scripts/grok_offload.sh status <name>
#   bash scripts/grok_offload.sh wait <name> [timeout-seconds]
#   bash scripts/grok_offload.sh list
#
# Artifacts: ${GROK_OFFLOAD_DIR:-$PWD/.scratch/grok}/<name>/
#   prompt.txt  out.md  err.log  rc  started  finished  pid  run.sh

set -uo pipefail

BASE="${GROK_OFFLOAD_DIR:-$PWD/.scratch/grok}"

die() { echo "grok_offload: $*" >&2; exit 2; }

job_dir() { echo "$BASE/$1"; }

job_state() {
  local d; d="$(job_dir "$1")"
  [[ -d "$d" ]] || { echo "missing"; return; }
  if [[ -f "$d/rc" ]]; then
    echo "done:$(cat "$d/rc")"
  elif [[ -f "$d/pid" ]] && kill -0 "$(cat "$d/pid")" 2>/dev/null; then
    echo "running"
  else
    echo "stale"
  fi
}

cmd_run() {
  local prompt="" name="" cwd="$PWD"
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --name) name="${2:-}"; shift 2 ;;
      --cwd)  cwd="${2:-}";  shift 2 ;;
      *) if [[ -z "$prompt" ]]; then prompt="$1"; shift; else die "unexpected arg: $1"; fi ;;
    esac
  done
  [[ -n "$prompt" ]] || die "run needs a prompt file"
  [[ -f "$prompt" ]] || die "prompt file not found: $prompt"
  [[ -z "$name" ]] && name="$(basename "$prompt")"; name="${name%.*}"
  [[ -d "$cwd" ]] || die "cwd not a directory: $cwd"

  local d; d="$(job_dir "$name")"
  mkdir -p "$d"
  cp "$prompt" "$d/prompt.txt"

  cat > "$d/run.sh" <<EOS
#!/usr/bin/env bash
cd "$cwd" || exit 3
grok --cwd "$cwd" --always-approve --prompt-file "$d/prompt.txt" \\
     --output-format plain --disable-web-search > "$d/out.md" 2> "$d/err.log"
echo \$? > "$d/rc"
date +%s > "$d/finished"
EOS
  chmod +x "$d/run.sh"

  date +%s > "$d/started"
  rm -f "$d/rc" "$d/finished"
  nohup bash "$d/run.sh" </dev/null > "$d/nohup.log" 2>&1 &
  echo $! > "$d/pid"
  disown 2>/dev/null || true

  echo "grok_offload: launched name=$name pid=$(cat "$d/pid")"
  echo "grok_offload: dir=$d"
  echo "grok_offload: poll with: bash scripts/grok_offload.sh status $name"
}

cmd_status() {
  local name="${1:-}"; [[ -n "$name" ]] || die "status needs a job name"
  local d; d="$(job_dir "$name")"
  [[ -d "$d" ]] || die "no such job: $name"
  local st; st="$(job_state "$name")"
  local bytes=0
  [[ -f "$d/out.md" ]] && bytes="$(wc -c < "$d/out.md" | tr -d ' ')"
  echo "job:    $name"
  echo "state:  $st"
  echo "bytes:  $bytes"
  if [[ -f "$d/started" ]]; then
    local now; now="$(date +%s)"
    echo "elapsed: $(( now - $(cat "$d/started") ))s"
  fi
  [[ -f "$d/err.log" && -s "$d/err.log" ]] && { echo "--- err.log (tail) ---"; tail -5 "$d/err.log"; }
  [[ "$st" == done:* ]] && return "$(cat "$d/rc")"
  return 0
}

cmd_wait() {
  local name="${1:-}" timeout="${2:-0}"
  [[ -n "$name" ]] || die "wait needs a job name"
  local d; d="$(job_dir "$name")"
  [[ -d "$d" ]] || die "no such job: $name"
  local waited=0
  while [[ ! -f "$d/rc" ]]; do
    sleep 5; waited=$(( waited + 5 ))
    if [[ "$timeout" -gt 0 && "$waited" -ge "$timeout" ]]; then
      echo "grok_offload: timeout after ${timeout}s (job still running)" >&2
      return 3
    fi
  done
  cmd_status "$name"
}

cmd_list() {
  [[ -d "$BASE" ]] || { echo "(no jobs)"; return; }
  local d
  for d in "$BASE"/*/; do
    [[ -d "$d" ]] || continue
    local n; n="$(basename "$d")"
    printf '%-30s %s\n' "$n" "$(job_state "$n")"
  done
}

case "${1:-}" in
  run)    shift; cmd_run "$@" ;;
  status) shift; cmd_status "$@" ;;
  wait)   shift; cmd_wait "$@" ;;
  list)   cmd_list ;;
  *) sed -n '2,28p' "$0"; exit 2 ;;
esac
