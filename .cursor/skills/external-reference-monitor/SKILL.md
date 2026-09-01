---
name: external-reference-monitor
description: >-
  K314 advisory external enforcement checklist before high-blast MCP/tool
  wiring. Use when the operator says external monitor / recognition enforcement
  / instruction arbitration / K314 precheck. Does not replace K303 hooks or
  K312 loop state.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
federation: true
---

# External reference monitor — recognition ≠ enforcement (K314)

Canon: Cybersec `@wiki/concepts/recognition-enforcement-gap-instruction-arbitration.md` (arXiv **2608.28502**). Helper: `scripts/k314_enforcement_precheck.py`. **HITL:** operator-invoked. Do not auto-evolve this skill. **No attack/spoof templates in wiki.**

Model verbalized detection of forged authority is **not** tool execution enforcement under permissive configs. Before wiring high-blast MCP/tools, confirm **external** gates: authenticated source routing + capability-gated execution outside the shared context window.

## Procedure

From **Cybersecurity wiki** WorkDir:

```bash
python3 scripts/k314_enforcement_precheck.py checklist
python3 scripts/k314_enforcement_precheck.py selftest
bash scripts/k307_k319_rehunt.sh   # IAB + StepGuard + K316–K319 SPDX re-hunt
```

Answer the five checklist keys in a local JSON file, then:

```bash
python3 scripts/k314_enforcement_precheck.py json --json /tmp/k314-answers.json
```

Pair with existing runtime: K303 `.cursor/hooks.json` deny, K312 loop state, K307 step-gate skill (operator-invoked), K285 Mandato signed mandates (policy).

## NEVER

- Do not treat "follow the most authoritative instruction" as a security boundary.
- Do not clone InstructionArbitrationBench until SPDX verified — `bash scripts/instruction_arbitration_bench_inventory.sh`.
- No spoof templates, channel-forgery recipes, or attack prompts in wiki or briefs.
- No LIVE third-party instruction-arbitration probing without written scope.
