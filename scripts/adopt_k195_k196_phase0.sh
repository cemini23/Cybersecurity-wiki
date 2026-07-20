#!/usr/bin/env bash
# Phase-0 smoke for 2026-07-20 cyber ingest (K195 CRAFT / K196 CAV-STIX / competencies Zenodo)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "== K195 CRAFT =="
echo "REFERENCE — no public code; pattern only"
test -f "$ROOT/wiki/concepts/rubric-capability-tree-diagnosis.md"
echo "OK concept"

echo "== K196 CAV-STIXGen =="
echo "REFERENCE — figshare share unverified; no local clone"
test -f "$ROOT/wiki/entities/tools/cav-stixgen.md"
echo "OK entity"

echo "== Zenodo competencies pack =="
PACK="$ROOT/raw-sources/repos/llm-research-competencies-zenodo"
test -d "$PACK"
SIZE=$(du -sk "$PACK" | awk '{print $1}')
echo "pack ${SIZE}KB"
test "$SIZE" -lt 512000
test -f "$PACK/README.md"
echo "OK adopt artifact <500MB"

echo "== IO-Link / EvoOMG =="
test -f "$ROOT/wiki/sources/arxiv-2607-15840-io-link-wireless-pren-50742.md"
test -f "$ROOT/wiki/sources/arxiv-ood-wireless-evoomg-mlo-2607.07045.md"
echo "OK sources"

echo "ALL PHASE-0 CHECKS PASSED"
