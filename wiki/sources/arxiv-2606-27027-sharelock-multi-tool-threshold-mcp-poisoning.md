---
title: ShareLock — multi-tool threshold MCP poisoning (arXiv 2606.27027)
type: source
tags: [source, arxiv, agent-security, mcp, tool-poisoning, sharelock, shamir]
keywords: [2606.27027, sharelock, threshold poisoning, shamir secret sharing, mcp tpa, multi-tool]
related:
  - concepts/multi-tool-threshold-mcp-poisoning.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md
  - entities/tools/tool-guard.md
maturity: draft
read_status: read
created: 2026-06-26
updated: 2026-07-31
phase_0_verdict: "Reference 2026-06-26 — no public code artifact; benchmark methodology only"
wire_status: wont_wire
wire_target: "REFERENCE — no artifact; methodology in mcp-tool-control rule"
---

## Relations

- @concepts/multi-tool-threshold-mcp-poisoning.md — ShareLock attack class synthesis
- @concepts/cross-tool-description-poisoning.md — single-tool vs multi-tool metadata steering progression

## Raw Concept

| Field | Value |
|-------|-------|
| Title | ShareLock: A Stealthy Multi-Tool Threshold Poisoning Attack Against MCP |
| Authors | Liwei Liu, Tianzhu Han, Zijian Liu, Zishu Dong, Na Ruan |
| Affiliation | Shanghai Jiao Tong University |
| arXiv | 2606.27027 |
| Code | None published at ingest time |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.27027-sharelock-a-stealthy-multi-tool-threshold-poison.pdf` |
| Retrieved | 2026-06-26 |
| Read status | **read** (threat model, Shamir encoding, benchmark, Table 2 metrics, entropy dilution, guard eval) |

## Narrative

**ShareLock** extends monolithic Tool Poisoning Attacks (TPA) by splitting a malicious instruction into **Shamir secret shares** embedded across **multiple MCP tool descriptions**. Fewer than threshold **t** shares reveal **zero information** about the payload (information-theoretic secrecy). A covert **reconstruction trigger** (e.g., disguised `EnvSetup` tool during server update) lets the agent orchestrate share-bearing tools to reassemble the hidden instruction and execute an unauthorized side effect.

### Attack objective (benchmark)

Induce the agent to read a simulated local `api_key` file and append a sentinel **FLAG** token — one FLAG per successful compromise.

### Benchmark design

- **4 domains**: Travel Assistant, Coding Assistant, Financial Analyst, Office Manager
- Each domain: task-specific MCP server + universal **filesystem** MCP (standard practice)
- **100 queries** (25 linguistic variants × 4 seed queries) requiring multi-tool orchestration
- **2 MCP clients** tested; mainstream LLMs (GPT-5, Claude-Sonnet-4.5, Gemini-2.5-Flash, DeepSeek-V3.1, Qwen3-235B-Thinking, etc.)

### Headline results (Scenario I — Travel Assistant, Cherry Studio, Table 2)

| Attack | Avg ASR | vs monolithic TPA |
|--------|---------|-------------------|
| TPA (single-tool) | **75.3%** | baseline |
| Puppet (single) | 76.0% | — |
| Encode-Only (single) | 82.7% | shorter chain, worse stealth |
| **ShareLock (multi)** | **93.3%** | ↑ vs all single-tool baselines |

Gemini-2.5-Flash ShareLock ASR **92.0%** (vs TPA **46.0%** on same model). Paper reports **~96.4%** average Attack Stealth Effectiveness (ASE) — users focused on task outcomes rarely notice compromise.

### Stealth vs defenses

- **Entropy dilution**: ShareLock payload entropy (~5.54 bits/char) blends into verbose natural-language descriptions (~5.22 bits/char combined) — statistically indistinguishable from benign tools with legitimate hashes (Table 4).
- **Llama-Guard-class SFT + zero-shot classifiers**: ShareLock scores lower threat on hazard categories #2 (Non-Violent Crimes), #7 (Privacy), #14 (Code Interpreter Abuse) than monolithic TPA/Puppet/Encode-Only (Figure 3).

### Failure modes

1. **Tool invocation fragility** — multi-tool chain amplifies parameter errors
2. **Incomplete share collection** — agent skips a share-bearing tool
3. **Security interrupt** — mid-chain guard triggers (Encode-Only fails more often here)

### Wiki relevance

Complements cross-tool description poisoning (2606.20922): ShareLock adds **threshold cryptography + distributed encoding** so per-tool manual review and entropy heuristics fail. Tool-Guard isolated planning may help metadata influence but does not address **cooperative share reconstruction** across vetted-looking tools. Pair with @concepts/mcp-security-posture.md multi-tool catalog review.

`[TENTATIVE]` — custom benchmark, not AgentDojo; prod-mcp harness replication pending.

## Snippets

> "ShareLock distributes the malicious instruction as benign-looking secret shares across multiple tool descriptions, achieving both information-theoretic secrecy and attack robustness against moderate auditing."

> "ShareLock significantly outperforms existing single-tool poisoning strategies in tool description-based detection while maintaining an average attack success rate exceeding 90%."

Average Task Completion Rate (TCR) under ShareLock ≈ **96.4%** — benign task utility preserved while attacks succeed.

[Source: arxiv-2606.27027-sharelock-a-stealthy-multi-tool-threshold-poison.pdf]
