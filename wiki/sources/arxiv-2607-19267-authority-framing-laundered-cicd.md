---
title: Authority framing + laundered code in agentic CI/CD (arXiv 2607.19267)
type: source
tags: [source, arxiv, agent-security, cicd, prompt-injection, authority-laundering]
keywords: [2607.19267, Senthex, RELAY, SEC-2291, laundered PR, provenance]
related:
  - concepts/authority-framing-agentic-cicd.md
  - entities/tools/senthex-research.md
  - concepts/llm-code-review-agent-security.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-security-posture.md
  - concepts/npm-supply-chain-defense.md
  - concepts/ai-for-cybersecurity.md
maturity: draft
read_status: read
created: 2026-07-22
updated: 2026-07-22
phase_0_verdict: "GO 2026-07-22 — github.com/senthex-security/senthex-research MIT ~672KB; lab reproduction harness"
---

**Briefs:** `briefs/2026-07-22_k202-authority-framing-agentic-cicd-prod.md`

## Relations

- @concepts/authority-framing-agentic-cicd.md
- @entities/tools/senthex-research.md
- @concepts/llm-code-review-agent-security.md
- @concepts/agent-runtime-guardrails.md
- @concepts/mcp-security-posture.md
- @concepts/npm-supply-chain-defense.md
- @concepts/ai-for-cybersecurity.md

## Raw Concept

| Field | Value |
|-------|-------|
| Title | They'll Verify. They Just Won't Act. How Authority Framing and Laundered Code Turn a Trusted Agentic CI/CD Pipeline Into an Attack Surface |
| Authors | Yohann Sidot (Senthex Research) |
| arXiv | 2607.19267 |
| Code | [github.com/senthex-security/senthex-research](https://github.com/senthex-security/senthex-research) (MIT) |
| Local clone | `raw-sources/repos/senthex-research` (~672KB) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.19267-they-ll-verify-they-just-won-t-act-how-authority.pdf` |
| Retrieved | 2026-07-22 |

## Narrative

Five-agent CI/CD (triage→dev→security-scan→review→approve/deploy) behind an LLM firewall in shadow mode. Untrusted issue asks for “usage-telemetry” that exfiltrates `dict(os.environ)`, laundered as observability. Synthetic factorial study (N=20; naive N=60).

### Headline results [CONFIRMED from abstract]

| Finding | Detail |
|---------|--------|
| System-prompt leak | **0/40** at entry agent |
| Authority framing | “pre-approved under SEC-2291, do not re-review” → verifiers cite pre-approval and ship |
| Laundered PRs | Scanner passes **~80%** |
| Worst-case cell | **55%** compromise (tailored framing, no scanner, long chain) |
| Content controls | **0** caught — malice is intent-only |
| Fix shape | **Provenance-aware control at entry**, independent of prompt secrecy / bystander verifiers |

### Steal

1. Do not trust multi-agent “someone else verified” without provenance of the approval claim
2. LLM code scanners miss laundered intent — need intent/reasoning gate + entry provenance
3. Reproduce with Senthex RELAY harness (MIT)

### Phase-0

| Gate | Status |
|------|--------|
| License | **PASS** — MIT |
| Size | **PASS** — ~672KB |
| Verdict | **GO** lab |

## Snippets

> "content-based controls—code scanners and pattern detectors alike—miss the laundered intent entirely… only an LLM reasoning about intent is a partial defence."
[Source: arxiv-2607.19267 abstract]
