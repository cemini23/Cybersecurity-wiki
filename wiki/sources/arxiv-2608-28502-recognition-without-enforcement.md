---
title: "Recognition Without Enforcement — configuration-dependent instruction arbitration failures (arXiv 2608.28502)"
type: source
tags: [source, arxiv, agent-security, guardrails, instruction-arbitration, k314]
keywords: [2608.28502, recognition-enforcement gap, instruction arbitration, authority spoofing, external reference monitor, InstructionArbitrationBench, capability-gated execution]
related:
  - concepts/recognition-enforcement-gap-instruction-arbitration.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
read_status: read
created: 2026-08-31
updated: 2026-08-31
phase_0_verdict: "REFERENCE 2026-08-31 — InstructionArbitrationBench + middleware at release; no attack templates in wiki. External enforcement pattern steal."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-agent-audit.mdc + mcp-tool-control.mdc (K314)"
---

## Relations

- @concepts/recognition-enforcement-gap-instruction-arbitration.md — primary steal (recognition ≠ enforcement)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Recognition Without Enforcement: Configuration-Dependent Failures in LLM Agent Instruction Arbitration and External Control |
| Authors | Jun Wen Leong (Independent Researcher) |
| arXiv | 2608.28502 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2608.28502-recognition-without-enforcement-configuration-de.pdf |
| Retrieved | 2026-08-31 |
| Read status | read (abstract + central claims) |
| Public code | InstructionArbitrationBench + middleware promised at release; **no attack templates in wiki** |

## Narrative

LLM agents arbitrate among instructions from system prompts, users, memory, and tools — but **arbitration cannot be assumed to enforce trust boundaries**. The paper identifies a **recognition–enforcement gap**: source-format features (role-template position, channel metadata) are linearly decodable from activations, and models can **verbalize** forged authority when prompted, yet some configurations still execute the conflicting tool call.

**Key results:**
- Under permissive prompts, GPT-4.1-mini detects fabricated authority in **98.7%** of trials yet executes in **99.3%** — recognition and action dissociate.
- Fleet evaluation (46 endpoints authority spoofing; 48 models memory conflict): fleet-mean execution under diverse novel attacks **1.21%** [0.5–2.1%] (model-clustered bootstrap), but vulnerability concentrates in **reproducible prompt–model cells** (40–100% deterministic on specific pairs) and shifts across deployment windows (up to **47 pp** within-window).
- Prompt-layer defenses do **not** generalize across the model fleet; adaptive attacker achieves **100%** bypass on tested defenses.
- **External reference monitor** (authenticated source routing + HMAC-SHA256 + capability-gated tool execution) rejects tested channel-forgery variants; residual boundary is **semantic authorization** through authenticated channels.

**Why filed (K314):** model self-arbitration is a **capability**, not a security boundary — pairs K303 (NL prose ≠ deny), K276 withhold contract, K277 measurement integrity (model-clustered CIs), K307 StepGuard (step gate without composition). Authorized-lab eval only when InstructionArbitrationBench ships; **no attack prompts or spoof templates in wiki**.

## Snippets

> Models encode source-format features … and can verbalize detection, yet do not condition tool execution on that recognition under permissive configurations. [Source: arXiv 2608.28502 abstract]

> Secure agents require external enforcement, not merely better recognition. [Source: arXiv 2608.28502 abstract]
