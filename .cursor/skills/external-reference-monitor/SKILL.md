---
name: external-reference-monitor
description: >-
  K326 advisory external enforcement checklist before high-blast MCP/tool
  wiring. Pairs K333 untrusted-model delegation precheck. Use when the
  operator says external monitor / recognition enforcement / instruction
  arbitration / K326 precheck. Does not replace step-gate or install products.
license: MIT
metadata.author: cemini23
metadata.version: "1.1.0"
disable-model-invocation: true
federation: true
---

# External reference monitor — recognition ≠ enforcement (K326 · pairs K333)

Canon: `@wiki/concepts/recognition-vs-enforcement-instruction-arbitration.md` (arXiv **2608.28502**) · `@wiki/concepts/untrusted-model-delegation-governance.md` (K333). Helpers: `scripts/k314_enforcement_precheck.py` (Cybersec), `scripts/delegation_broker_precheck.py` (CCC K333). **HITL:** operator-invoked. **No attack/spoof templates in wiki.**

Model verbalized detection of forged authority is **not** tool execution enforcement under permissive configs. Treat the model as **untrusted** (K333): a fully prompt-injected agent must still not exceed delegated authority. Before wiring high-blast MCP/tools, confirm **external** gates: authenticated source routing + capability-gated execution outside the shared context window + scoped credentials via an authorization broker.

## Procedure

From **Cybersecurity wiki** WorkDir (K326 checklist):

```bash
python3 scripts/k314_enforcement_precheck.py checklist
python3 scripts/k314_enforcement_precheck.py selftest
python3 scripts/k314_enforcement_precheck.py json --json /tmp/k314-answers.json
bash scripts/instruction_arbitration_bench_inventory.sh   # SPDX watch only
```

From **CCC** WorkDir (K333 pairing + harness-wave SPDX watch):

```bash
python3 scripts/delegation_broker_precheck.py checklist
python3 scripts/delegation_broker_precheck.py selftest
python3 scripts/delegation_broker_precheck.py json --json /tmp/k333-answers.json
bash scripts/spdx_watch_harness_wave.sh
```

Pair with existing runtime: K312 step-gate skill + PreToolUse hook (operator-invoked), K285 Mandato signed mandates (policy), `untrusted-delegation-precheck` skill.

## NEVER

- Do not treat "follow the most authoritative instruction" as a security boundary.
- Do not clone InstructionArbitrationBench until SPDX verified — `bash scripts/instruction_arbitration_bench_inventory.sh`.
- No spoof templates, channel-forgery recipes, or attack prompts in wiki or briefs.
- No LIVE third-party instruction-arbitration probing without written scope.
