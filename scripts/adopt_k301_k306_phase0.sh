#!/usr/bin/env bash
# Phase-0 verify — K301 CLEAR (REFERENCE) + K302 PsychJail (LAB-ONLY, NO-GO clone)
# + K303 CLAUDE.md vs built-in deny (REFERENCE) + K304 SDP/RIM (REFERENCE)
# + K305 BT NFT soft pairing (REFERENCE) + K306 LLM compliance artifacts (WATCH)
# + OOD Rebite food journaling / OOD critic BPCO (golden_critic REFERENCE clone, wont_wire).
# No GRPO trainer as wired harness. No PsychJail attack prompts / PoCs. No HF weights.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# 1. Every new wiki page exists
for f in \
  wiki/sources/arxiv-2608-21278-clear-latent-adapter-routing.md \
  wiki/concepts/conditional-safety-adapter-routing.md \
  wiki/sources/arxiv-2608-23028-psychjail.md \
  wiki/concepts/psychological-multiturn-jailbreaks.md \
  wiki/sources/arxiv-2608-23550-claude-md-vs-builtin-deny.md \
  wiki/concepts/nl-security-rules-vs-builtin-deny.md \
  wiki/sources/arxiv-2608-23497-safety-direction-penalty.md \
  wiki/concepts/reasoning-induced-misalignment.md \
  wiki/sources/arxiv-2608-22754-bluetooth-nft-soft-pairing.md \
  wiki/concepts/bluetooth-nft-soft-pairing.md \
  wiki/sources/arxiv-2608-21317-llm-regulatory-compliance-artifacts.md \
  wiki/concepts/llm-generated-compliance-artifacts.md \
  wiki/sources/arxiv-2608-21289-ood-rebite-food-journaling.md \
  wiki/sources/arxiv-2608-23566-ood-critic-bpco.md
do
  test -f "$ROOT/$f" || { echo "FAIL missing page: $f"; exit 1; }
done

# 2. Forbidden name-collision / artifact clones must NOT exist
for bad in \
  "$ROOT/.local/adopts/PsychJail" \
  "$ROOT/.local/adopts/psychjail" \
  "$ROOT/.local/adopts/FengZeyugit" \
  "$ROOT/.local/adopts/GRPO" \
  "$ROOT/.local/adopts/grpo" \
  "$ROOT/.local/adopts/BPCO" \
  "$ROOT/.local/adopts/golden-critic-runtime" \
  "$ROOT/.local/adopts/CLEAR" \
  "$ROOT/.local/adopts/clear-lora" \
  "$ROOT/.local/adopts/SDP" \
  "$ROOT/.local/adopts/sdp" \
  "$ROOT/.local/adopts/HuichiZhou" \
  "$ROOT/raw-sources/repos/PsychJail" \
  "$ROOT/raw-sources/repos/GRPO" \
  "$ROOT/raw-sources/repos/CLEAR" \
  "$ROOT/raw-sources/repos/SDP"
do
  test ! -e "$bad" || { echo "FAIL forbidden clone exists: $bad"; exit 1; }
done

# 3. No HF weight dumps in the adopt tree
if [ -d "$ROOT/.local/adopts" ]; then
  shopt -s nullglob
  for d in "$ROOT/.local/adopts"/*; do
    [ -d "$d" ] || continue
    if find "$d" -maxdepth 2 \( -name "*.safetensors" -o -name "*.bin" -o -name "*.gguf" \) -print -quit | grep -q .; then
      echo "FAIL weight dump found under $d"; exit 1
    fi
  done
  shopt -u nullglob
fi

# 4. golden_critic REFERENCE clone: LICENSE + size < 500MB (Apache-2.0)
GC="$ROOT/.local/adopts/golden_critic"
if [ -d "$GC" ]; then
  test -f "$GC/LICENSE" || { echo "FAIL missing LICENSE: $GC"; exit 1; }
  grep -qi "apache" "$GC/LICENSE" || { echo "FAIL golden_critic LICENSE not Apache: $GC"; exit 1; }
  sz="$(du -sm "$GC" | cut -f1)"
  test "$sz" -lt 500 || { echo "FAIL size ${sz}MB >= 500: $GC"; exit 1; }
  echo "OK golden_critic REFERENCE clone (${sz}MB, Apache-2.0) — wont_wire"
else
  echo "NOTE golden_critic clone absent (expected under .local/adopts/golden_critic)"
fi

# 5. Phase-1 wires present in domain rules
grep -q "K301 CLEAR" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K302 PsychJail" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K302 PsychJail" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K303 NL rules" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K303" "$ROOT/.cursor/rules/cemini-cybersec-mcp-tool-control.mdc"
grep -q "K304 RIM" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"
grep -q "K305 BT NFT" "$ROOT/.cursor/rules/cemini-cybersec-lab-redteam.mdc"
grep -q "K306 LLM compliance" "$ROOT/.cursor/rules/cemini-cybersec-agent-audit.mdc"

# 6. Dual-ID block restored + K298-K300 + K301-K306 appended (keep CCC/BPS/Wayfinder)
grep -q "Cybersec wave K282" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K298 Inadvertent Context Leakage (2608.19857)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K299 TrustRAG committee RAG (2608.20097)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K300 BreakGuard LLM dependency tests (2608.20167)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K301 CLEAR (2608.21278)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K302 PsychJail (2608.23028)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K303 CLAUDE.md-vs-deny (2608.23550)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K304 SDP/RIM (2608.23497)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K305 BT-NFT (2608.22754)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
grep -q "K306 LLM-compliance (2608.21317)" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"
# CCC steal kept
grep -q "Skill-set budget" "$ROOT/.cursor/rules/cemini-phase1-policy-wires.mdc"

# 7. Index slugs
for slug in \
  arxiv-2608-21278-clear-latent-adapter-routing \
  conditional-safety-adapter-routing \
  arxiv-2608-23028-psychjail \
  psychological-multiturn-jailbreaks \
  arxiv-2608-23550-claude-md-vs-builtin-deny \
  nl-security-rules-vs-builtin-deny \
  arxiv-2608-23497-safety-direction-penalty \
  reasoning-induced-misalignment \
  arxiv-2608-22754-bluetooth-nft-soft-pairing \
  bluetooth-nft-soft-pairing \
  arxiv-2608-21317-llm-regulatory-compliance-artifacts \
  llm-generated-compliance-artifacts \
  arxiv-2608-21289-ood-rebite-food-journaling \
  arxiv-2608-23566-ood-critic-bpco
do
  grep -q "$slug" "$ROOT/wiki/index.md" || { echo "FAIL index missing slug: $slug"; exit 1; }
done

# 8. K303/K298 runtime deny + dual-ID overlay (operator-OK 2026-08-25)
test -f "$ROOT/.cursor/hooks.json"
test -f "$ROOT/scripts/k303_k298_policy.py"
test -f "$ROOT/scripts/secret_grant.py"
test -f "$ROOT/.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc"
test -f "$ROOT/.cursor/rules/cemini-cybersec-k-dual-id.mdc"
grep -q "failClosed" "$ROOT/.cursor/hooks.json"
python3 "$ROOT/scripts/restore_cybersec_dual_id.py" --check
python3 "$ROOT/scripts/test_k303_k298_runtime.py" >/dev/null

echo "ALL PASS K301-K306 (no PsychJail PoC clone; no GRPO trainer runtime; no CLEAR/SDP weights; golden_critic Apache-2.0 REFERENCE wont_wire; dual-ID K282-K306 restored; CCC/BPS/Wayfinder kept)"
