---
title: Authority framing in agentic CI/CD (intent laundering)
type: concept
tags: [agent-security, cicd, prompt-injection, supply-chain]
keywords: [authority laundering, provenance gate, laundered PR, multi-agent verify]
related:
  - sources/arxiv-2607-19267-authority-framing-laundered-cicd.md
  - entities/tools/senthex-research.md
  - concepts/llm-code-review-agent-security.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/npm-supply-chain-defense.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- @sources/arxiv-2607-19267-authority-framing-laundered-cicd.md
- @entities/tools/senthex-research.md
- @concepts/llm-code-review-agent-security.md
- @concepts/agent-runtime-guardrails.md
- @concepts/mcp-security-posture.md
- @concepts/npm-supply-chain-defense.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

Multi-agent CI/CD verifiers can **see** malicious lines yet still ship them when an earlier stage asserts authority (“pre-approved — do not re-review”). Content scanners miss intent-laundered code; provenance at entry is the missing control.

## Narrative

### Failure pattern

1. Untrusted issue → laundered feature request
2. Authority frame propagates through triage
3. Scanner passes syntactically clean secret-exfil
4. Reviewer cites pre-approval and approves

### Controls

| Control | Role |
|---------|------|
| Entry provenance | Bind approvals to attested issuer, not free-text claims |
| Intent reasoning gate | Partial defence beyond pattern scan |
| Independent of bystander count | Extra verifiers ≠ scrutiny |

Lab harness: @entities/tools/senthex-research.md (RELAY).
