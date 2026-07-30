#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
for f in \
  wiki/concepts/rf-fingerprint-temperature-drift.md \
  wiki/concepts/gpt-red-self-play-red-teaming.md \
  wiki/concepts/inferscale-kv-injection-personalized-serving.md \
  wiki/concepts/kamr-knowledge-aligned-multihop-retrieval.md \
  wiki/concepts/bydeway-v2-explainable-spatial-reasoning.md \
  wiki/sources/arxiv-2607-25070-rffi-device-temperature.md \
  wiki/sources/arxiv-2607-26115-gpt-red-self-play.md \
  wiki/sources/arxiv-2607-27090-inferscale-kv-injection.md \
  wiki/sources/arxiv-2607-27136-kamr-multihop-retrieval.md \
  wiki/sources/arxiv-2607-27145-bydeway-v2-spatial.md \
  wiki/entities/tools/inferscale.md
do
  test -f "$ROOT/$f"
done
test -d "$ROOT/raw-sources/repos/InferScale"
test -f "$ROOT/raw-sources/repos/InferScale/LICENSE"
rg -q 'BSD' "$ROOT/raw-sources/repos/InferScale/LICENSE"
SZ=$(du -sk "$ROOT/raw-sources/repos/InferScale" | awk '{print $1}'); test "$SZ" -lt 512000
echo "ALL PASS InferScale=${SZ}KB (K225/K226/K228/K229 REFERENCE — no clones)"
