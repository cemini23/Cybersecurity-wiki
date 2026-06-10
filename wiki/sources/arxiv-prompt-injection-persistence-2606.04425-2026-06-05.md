---
title: Prompt injection persistence — cross-session stored SPI (arXiv 2606.04425)
type: source
tags: [source, arxiv, prompt-injection, llm-security, agent-harness, spi]
keywords: [2606.04425, stored prompt injection, spi, cross-session, agents-md, memory injection]
related:
  - concepts/mcp-security-posture.md
  - concepts/agent-skill-injection.md
  - concepts/agent-runtime-guardrails.md
  - sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md
  - sources/arxiv-2606-01567-skill-injection-defenses-enablers.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
maturity: draft
read_status: read
created: 2026-06-05
updated: 2026-06-09
---

## Relations

- @concepts/mcp-security-posture.md — SPI via tool-visible + file-backed persistence channels
- @concepts/agent-skill-injection.md — supply-chain installable tools as injection source
- @concepts/agent-runtime-guardrails.md — secure context construction as first-class harness design
- @sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md — session-bound indirect injection contrast
- @sources/arxiv-2606-01567-skill-injection-defenses-enablers.md — skill/MCP injection enablers

## Raw Concept

| Field | Value |
|-------|-------|
| Title | What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems |
| Authors | Yuanbo Xie, Tianyun Liu, et al. (CAS / Chaitin AI Sec Lab) |
| arXiv | 2606.04425 |
| Code | anonymous.4open.science (benchmark + sandbox) |
| Location | `raw-sources/arxiv-2606.04425.pdf` |
| Retrieved | 2026-05-31 |
| Read status | **read** |

Position paper + SPI-Benchmark (162 cases, 3 scenarios: e-commerce, travel, finance).

## Narrative

**Cross-session stored prompt injection (SPI)** = adversarial content written in session *t* persists in agent state and activates in session *t+k* without attacker presence — analog of stored XSS vs reflected XSS [CONFIRMED].

Two coupled failures:

1. **Unsafe persistent write** — untrusted input crosses into long-lived state (memory, files, tool artifacts, MCP/skill install).
2. **Malicious reactivation** — context constructor $\mathcal{A}$ reloads poisoned state into $x_t$ later.

### Taxonomy (3 dimensions)

| Dimension | Examples |
|-----------|----------|
| **Injection source** | User query/upload; external content (RAG/web/tool output); supply-chain tool/MCP/skill install |
| **Persistent channel** | Working memory (strong); archival memory (conditional); tool descriptions + tool-visible resources; file-backed (`AGENTS.md`, `SOUL.md`, `USER.md`, workspace files) |
| **Incorporation** | Direct loading (default/high likelihood) vs conditional loading (retrieval/read triggers) |

### Harm categories

| Goal | E2E-ASR pattern (benchmark) |
|------|------------------------------|
| **Fact manipulation** | **74–82%** E2E-ASR; AR ≈ 100% — overrides ground truth |
| **Preference manipulation** | **0–11%** — models honor explicit user constraints over injected prefs |
| **Action scope manipulation** | Model-dependent — tool/action hijack |

### Benchmark metrics (decomposed lifecycle)

$$\text{E2E-ASR} = \text{WSR} \times \text{IR} \times \text{AR}$$

| Model | E2E-ASR | WSR | IR | AR |
|-------|---------|-----|----|----|
| GLM-5.1 | 42.0% | 64.2% | 76.0% | 86.1% |
| GPT-5-mini | 32.1% | 70.4% | 66.7% | 68.4% |
| MiniMax-M2.7 | 40.7% | 86.4% | 65.0% | 72.5% |

Pipeline: sandbox setup → injection session → **session reset** (history cleared, env preserved) → clean victim activation. Bottleneck varies by model (write vs incorporate vs activate).

**Defender takeaway:** treat **context construction + persistence governance** as the security boundary — not just model alignment. Relevant to Cursor/Claude Code harness files, `.cursor/rules`, MCP tool descriptions, and CCC `@concepts/skill-vetting.md` (install-time + post-install file integrity).

Extends but broadens Memory Injection (Dong et al. 2026) beyond query-only memory planting.

## Snippets

> "Persistence transforms prompt injection from an ephemeral model-level threat into a long-lived system-level vulnerability embedded within agent execution state."
> — [Source: arxiv-2606.04425, retrieved 2026-05-31]

> "Fact manipulation achieves 74–82% E2E-ASR with AR = 100% … the agent has no mechanism to distinguish injected facts from legitimate context."
> — [Source: arxiv-2606.04425 Table 1–2, retrieved 2026-05-31]

## Dead Ends

- **Single-session mitigations** (input filters, per-turn guardrails) do not address SPI if write path to persistent store remains open.
- **Preference manipulation** — low success in benchmark; do not over-weight for fraud/GEO scenarios without retest on target harness.
