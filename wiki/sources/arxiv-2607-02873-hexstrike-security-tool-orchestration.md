---
title: Determinants and Limits of LLM Security-Tool Orchestration — HexStrike-AI study (arXiv 2607.02873)
type: source
tags: [source, arxiv, llm-agents, pentest, ctf, tool-orchestration, mcp, hexstrike]
keywords: [2607.02873, hexstrike-ai, picoCTF, tool orchestration, driving client, MCP, penetration testing, empirical eval]
related:
  - concepts/security-tool-orchestration-determinants.md
  - concepts/agentic-offensive-security-kill-chain.md
  - concepts/agent-least-privilege-tool-selection.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/mcp-security-posture.md
  - concepts/tool-environment-unreliability-eval.md
  - "@ccc-wiki/concepts/client-as-first-order-harness-factor.md"
  - entities/tools/hexstrike-ai.md
  - sources/github-hexstrike-ai.md
  - concepts/ai-pentest-harness-landscape.md
maturity: draft
read_status: read
created: 2026-07-07
updated: 2026-07-31
phase_0_verdict: "REFERENCE 2026-07-07 — HexStrike-AI repo MIT, 10k★; methodology + client-effect finding adopt; fixes tuned on eval set (limit)"
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

**Briefs:** `briefs/2026-07-07_hexstrike-client-first-order-orchestration-checklist.md`

## Relations

- @concepts/security-tool-orchestration-determinants.md — synthesis page
- @concepts/agentic-offensive-security-kill-chain.md — where orchestrators sit in the offensive flow
- @concepts/mcp-execution-control-invariants.md — MCP tool-call authority complement

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Determinants and Limits of LLM Security-Tool Orchestration: A Study with HexStrike-AI |
| Authors | Romain Gerard, Assmaa Zeghaider, Yan Guo (USTC) |
| arXiv | 2607.02873 |
| Testbed | HexStrike-AI (`github.com/0x4m4/hexstrike-ai`, MIT, 10k★, 150+ tools over MCP) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.02873-determinants-and-limits-of-llm-security-tool-orc.pdf` |
| Retrieved | 2026-07-07 |
| Read status | read (methodology, 774-trial matrix, client effect, residual-failure taxonomy) |

## Narrative

Empirical study of what bounds an LLM security orchestrator's capability: **model vs client**, whether **constraining to the orchestrator's own tools** helps, and where failures are **reasoning-bound** vs missing-tool.

### Experiment

- **86 picoCTF** challenges × 7 categories × 3 difficulty tiers
- **3 tool-access regimes** × **3 model/client configs** = **774 trials**
- Configs: **Claude Sonnet 4.6**; **DeepSeek (deepseek-chat) via RooCode**; **DeepSeek via 5ire** — same model, two clients isolates the **client effect**
- Then: corrections to existing tools + agent-behavior changes + **11 new capability tools**; re-run failures

### Headline findings

| Finding | Value |
|---------|-------|
| **Driving client is first-order** | 2.1× gap between two DeepSeek clients (RooCode 76.4% vs 5ire 49.6% post-fix) |
| Overall solve rate | **55.4% → 72.0%** after fixes (McNemar p < 0.001) |
| Residual failures | **Reasoning- / environment-bound**, not missing-tool |
| Difficulty | Monotonic gradient; largest gains in **mid tier** |
| Stability | 60-run sub-study: 17/20 unanimous single-run verdicts |

### Methodological implication

> A model's solve rate is meaningful **only when the client that produced it is named**; a benchmark that varies the model while fixing an **unnamed harness may be measuring the harness as much as the model**.

### Limits

Single benchmark; fixes tuned on the same challenges evaluated; client effect shown for one model only.

### Adoption posture

| Verdict | **REFERENCE** — adopt eval methodology + client-naming discipline; HexStrike-AI MIT if trialed in authorized lab |

## Snippets

> "The diagnosis isolates the driving client as a first-order factor for a fixed model (a 2.1× gap between two DeepSeek clients)."
> — [Source: arxiv-2607.02873 abstract, retrieved 2026-07-07]

> "A benchmark that varies the model while fixing an unnamed harness may be measuring the harness as much as the model."
> — [Source: arxiv-2607.02873 §5.1, retrieved 2026-07-07]
