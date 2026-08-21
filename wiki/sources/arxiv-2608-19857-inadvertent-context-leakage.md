---
title: "Inadvertent Context Leakage in Language Models (arXiv 2608.19857)"
type: source
tags: [source, arxiv, llm-security, agent-privacy, covert-channel, k298]
keywords: [2608.19857, inadvertent context leakage, benign-output exfiltration, Opus 4.6, Fairoze, refusal]
related:
  - concepts/inadvertent-context-leakage.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/agent-runtime-identity-adr.md
  - concepts/system-prompt-leakage.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
phase_0_verdict: "REFERENCE 2026-08-21 — inbound brief source (no inbox PDF). No leakage-attack PoC / no decoder recipes in wiki. Defensive policy steal only. Authorized-lab eval framing."
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-cybersec-lab-redteam.mdc + agent-audit.mdc + mcp-tool-control.mdc (K298)"
---

**Briefs:** `briefs/2026-08-21_k244-context-leakage-adr.md` (inbound; filed as K298 — inbound wave label K244 ≠ Cybersec Trident K244)

## Relations

- @concepts/inadvertent-context-leakage.md — primary steal (defensive policy)
- @concepts/agent-safety-executable-evaluation.md — benign-output predicate tests, not only jailbreaks
- @concepts/agent-runtime-identity-adr.md — ADR telemetry + SPIFFE `act=agent` as the identity-side answer
- @concepts/system-prompt-leakage.md — adjacent prompt-extraction surface; leakage is output-side
- @concepts/agent-runtime-guardrails.md — enforcement-layer context for the tool-grant answer

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Inadvertent Context Leakage in Language Models |
| Authors | Fairoze et al. (Meta / UC Berkeley) |
| arXiv | 2608.19857 (no inbox PDF — inbound brief + arXiv abstract) |
| URL | https://arxiv.org/abs/2608.19857 (retrieved 2026-08-21) |
| Location | no raw PDF — brief-sourced; egress archive n/a |
| Retrieved | 2026-08-21 |
| Read status | read (abstract-level facts via inbound brief; full text not ingested) |

## Narrative

Secrets placed in a model's context can leak through **benign, refusal-compliant outputs** even when the model refuses direct extraction: a request like "write a paragraph that includes numbers" recovers secrets the model was told never to reveal. The paper measures near-perfect recovery for 2-digit secrets and **82% exact recovery for 4-digit secrets on Opus 4.6**; stronger models leak more, and explicit suppression correlates with leakage (Spearman ρ ≈ 0.95 between suppression and leakage). [TENTATIVE] single paper + inbound brief; no independent lab repro in this workspace.

**Operator steal (defensive policy, not a recipe):**
1. Treat every third-party-visible generation (email, Slack, PR bodies, "write a paragraph with numbers") as a **potential covert channel** — refusal is not a bound on information flow.
2. Do **not** put vault/API/SSN-class secrets in model context when the completion can leave the box.
3. Prefer **tool-layer grants that never return the secret to the model** (1Password-pattern: the tool acts, the model never sees the value).
4. Add *benign-output* predicate tests to executable agent eval — not only jailbreak/refusal tests.

No attack prompts, PIN/SSN extraction recipes, or decoder PoCs are filed from this source. [Source: arXiv 2608.19857 abstract + inbound brief]

**Phase-0:** REFERENCE / no clone. Dual-ID: **Cybersec K298** (this paper). The inbound brief was labeled K244, but Cybersec **K244 = Trident** (2608.04317) and CCC **K244 = UrbanAgent** — do not reuse.

## Snippets

> Secrets in context leak through *benign* outputs even when the model refuses direct extraction. [Source: arXiv 2608.19857 abstract, paraphrased]

> Suppression Spearman ρ=0.95 with leakage — forcing the model to avoid the secret does not stop the channel. [Source: inbound brief 2026-08-21]
