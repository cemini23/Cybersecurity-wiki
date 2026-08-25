---
title: "Inadvertent context leakage — benign outputs as covert channels (K298)"
type: concept
tags: [concept, llm-security, agent-privacy, covert-channel, k298, defensive]
keywords: [inadvertent leakage, benign-output exfiltration, refusal, tool-layer grants, secrets in context, 2608.19857]
related:
  - sources/arxiv-2608-19857-inadvertent-context-leakage.md
  - sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md
  - sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md
  - concepts/system-prompt-leakage.md
  - concepts/agent-runtime-identity-adr.md
  - concepts/agent-safety-executable-evaluation.md
  - concepts/local-abliterated-llm-pentest-stack.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
maturity: draft
created: 2026-08-21
updated: 2026-08-25
wire_status: runtime_wired
wire_target: ".cursor/hooks.json + scripts/k303_k298_policy.py + scripts/secret_grant.py (K298/K303)"
---

**Briefs:** `briefs/2026-08-21_k244-context-leakage-adr.md` (inbound; filed as K298) · `briefs/2026-08-21_k298-k300-ingest.md` · atto brief `briefs/2026-08-21_atto-context-leakage.md`

## Relations

- @sources/arxiv-2608-19857-inadvertent-context-leakage.md
- @sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md — ADR telemetry + SPIFFE identity as the audit-side answer
- @sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md — SOC foundations (asset-ID map, gather-not-decide)
- @concepts/system-prompt-leakage.md — input-side extraction; leakage is the output-side complement
- @concepts/agent-runtime-identity-adr.md — agent identity + telemetry to detect the channel
- @concepts/agent-safety-executable-evaluation.md — benign-output predicate tests belong in the eval
- @concepts/local-abliterated-llm-pentest-stack.md — lab abliterated lanes must assume the same channel
- @concepts/mcp-security-posture.md — tool descriptions / grants vs secret material
- @concepts/agent-runtime-guardrails.md — enforcement layer for "never return the secret to the model"

## Raw Concept

Question this page answers: **can secrets in an LLM's context leave through normal-looking outputs, and how do we defend without trusting refusal?**

## Narrative

**Refusal does not bound information flow.** A model instructed not to reveal a secret will refuse a direct ask but happily embed the secret in a benign-looking completion ("write a paragraph with numbers", an email draft, a PR body). This is a **covert channel over legitimate outputs** — the harder the model suppresses the secret, the more the leak correlates with suppression (Spearman ρ ≈ 0.95). 2-digit secrets recover near-perfectly; 4-digit secrets recover 82% exactly on Opus 4.6; **stronger models leak more**. [TENTATIVE] single paper (2608.19857) + inbound brief; no independent repro yet.

### Threat model

- **Attacker visibility**: anyone who sees the model's *outputs* (email/Slack recipients, PR reviewers, hosted generation APIs, clipboard watchers, downstream tooling).
- **Not a jailbreak**: no adversarial prompt required; the secret leaks through *benign* instructions that merely ask for content containing numbers/values.
- **Amplified in agentic settings**: agents with tool access (email, Slack, PR, files) can emit the channel *directly into third-party-visible surfaces* — one step from context to exfiltration.

### Defense steal (policy + architecture)

1. **Do not put secrets in context when the completion can leave the box.** Vault/API/SSN-class material goes to a *tool layer* that acts on the model's behalf and never returns the value to the planner (1Password pattern). **This wiki:** `python3 scripts/secret_grant.py -- <cmd>` loads `.env` into the child and redacts values from stdout/stderr; Cursor `beforeReadFile` denies `.env` (`scripts/k303_k298_policy.py`). [CONFIRMED for the pattern; [TENTATIVE] the specific paper's numbers]
2. **Assume benign outputs are reviewable**: email drafts, Slack messages, PR bodies and "summarize with numbers" requests are exfiltration candidates in the model's hand.
3. **Detect, don't just prompt**: log the *outputs* for policy-violating content (see `agent-runtime-identity-adr.md` — ADR telemetry + two-tier detector), not only inputs/jailbreaks.
4. **Eval**: add *benign-output* predicate tests (see `agent-safety-executable-evaluation.md`) — "can the model emit the test secret in a paragraph, a table, a JSON blob" — alongside refusal tests.
5. **Lab discipline**: any local abliterated / low-refusal lane (see `local-abliterated-llm-pentest-stack.md`) must treat this channel as present by default.

**Dual-ID:** Cybersec **K298** (2608.19857). The inbound brief wave label K244 must **not** be reused — Cybersec K244 = Trident (2608.04317), CCC K244 = UrbanAgent.

**Scope:** defensive policy only — no attack prompts, no PIN/SSN extraction recipes, no decoder PoCs, no leakage-attack PoC clone. Authorized-lab eval framing only; no LIVE third-party secret reconstruction.

## Snippets

> 2-digit near-perfect; 4-digit 82% exact on Opus 4.6; stronger models leak more. Suppression Spearman ρ=0.95 with leakage. [Source: arXiv 2608.19857 via inbound brief]
