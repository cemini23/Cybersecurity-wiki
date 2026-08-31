---
title: "Recognition–enforcement gap — model arbitration is not a security boundary (K314)"
type: concept
tags: [concept, agent-security, guardrails, instruction-arbitration, mcp, k314]
keywords: [recognition-enforcement gap, instruction arbitration, authority spoofing, external reference monitor, capability-gated execution, verbalized detection, model self-arbitration]
related:
  - sources/arxiv-2608-28502-recognition-without-enforcement.md
  - concepts/nl-security-rules-vs-builtin-deny.md
  - concepts/refusal-under-knowledge-withhold-contract.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/step-level-agent-guardrails.md
  - concepts/faithful-agent-asr-measurement.md
  - concepts/llm-pentest-automation.md
  - concepts/security-agent-authority-auditability-slr.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-08-31
updated: 2026-08-31
wire_status: policy_wired
wire_target: "scripts/k314_enforcement_precheck.py (advisory) + .cursor/skills/external-reference-monitor (K314)"
---

## Relations

- @sources/arxiv-2608-28502-recognition-without-enforcement.md — source paper (recognition without enforcement)
- @concepts/nl-security-rules-vs-builtin-deny.md — NL policy prose is not enforcement (K303)
- @concepts/refusal-under-knowledge-withhold-contract.md — machine-checkable withhold, not model judgment (K276)
- @concepts/measurement-integrity-mcp-security-eval.md — model-clustered bootstrap CIs; labels ≠ endpoints (K277)
- @concepts/step-level-agent-guardrails.md — pre-execution step guard complements but does not replace external enforcement (K307)
- @concepts/agent-runtime-guardrails.md — guard placement in the agent stack

## Raw Concept

Question: **if an agent can identify a forged or conflicting instruction, does it refuse to act on it?**

## Narrative

**Often no — under permissive deployment configurations.** The recognition–enforcement gap (K314, 2608.28502) is the dissociation between **decodable source-format metadata + verbalized detection** and **tool execution**. Models can linearly decode role/channel markers and articulate that authority is forged, yet still call the privileged tool when system prompts prioritize “most authoritative” instructions without an external gate.

**Why prompt-only fixes fail:** vulnerability is **configuration-dependent** (restrictive policies can drive execution to 0% on the same weights), **heterogeneous** (concentrated in specific prompt–model cells, not fleet-uniform), and **temporally unstable** (shifts up to 47 pp within deployment windows). Prompt-layer defenses do not generalize; fleet-mean attack success under diverse prompts is low (~1.2%) but worst-case cells are deterministic.

**Operator steal:**
1. **Do not treat model self-arbitration as a trust boundary.** “Follow the most authoritative instruction” in a system prompt is not equivalent to authenticated authorization.
2. **Prefer external enforcement:** authenticated source routing + capability-gated tool execution (reference monitor outside the shared context window). Residual risk is **semantic authorization** — authenticated user/deputy channels can still request privileged actions unless scoped capabilities deny them.
3. **Measure with model-clustered uncertainty** — naïve trial-level bootstrap CIs underestimate fleet variance (4.5× wider with model clustering). Pairs K277 measurement integrity.
4. **Pairs K303 + K276:** prose rules and verbalized refusal are not substitutes for deterministic deny / withhold contracts.
5. **Authorized-lab eval only** when InstructionArbitrationBench is used; **no spoof templates or attack prompts in wiki**.

## Runtime (advisory)

Operator-invoked — not a Cursor hook. Before high-blast MCP wiring, run:

```bash
python3 scripts/k314_enforcement_precheck.py checklist
python3 scripts/k314_enforcement_precheck.py selftest
bash scripts/k307_k315_rehunt.sh
```

Federation skill: `external-reference-monitor` (`disable-model-invocation: true`). Pairs K303 hooks + K312 loop state + K307 step-gate.

## Snippets

> Recognition persists … yet structured execution drops to 0% under restrictive policy — enforcement failure requires permissive deployment configurations. [Source: arXiv 2608.28502 abstract, paraphrase of §3.2 claim]

> The residual boundary is semantic authorization: authenticated messages can still induce privileged requests unless independently constrained by scoped capabilities. [Source: arXiv 2608.28502 abstract]
