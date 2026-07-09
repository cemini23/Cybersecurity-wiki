---
title: Agent data injection attacks (ADI) — arXiv 2607.05120
type: source
tags: [source, arxiv, agent-security, ipi, data-injection, trusted-untrusted]
keywords: [2607.05120, adi, agent data injection, probabilistic delimiter, instruction injection, compsec-snu]
related:
  - concepts/agent-data-injection-attacks.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - concepts/mcp-execution-control-invariants.md
  - concepts/cross-tool-description-poisoning.md
  - concepts/agent-execution-provenance.md
  - concepts/llm-code-review-agent-security.md
  - concepts/agent-skill-injection.md
  - concepts/ai-for-cybersecurity.md
  - sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md
  - concepts/mcp-taint-style-vulnerabilities.md
maturity: draft
read_status: read
created: 2026-07-09
updated: 2026-07-09
phase_0_verdict: "CONDITIONAL-GO 2026-07-09 — github.com/compsec-snu/adi artifacts + AgentDojo ADI benchmark; responsible disclosure to Anthropic/OpenAI/Google; adopt eval harness after license audit"
---

**Briefs:** `briefs/2026-07-09_adi-trusted-untrusted-data-handoff.md`, `briefs/2026-07-09_prod-mcp-trusted-untrusted-data-isolation-checklist.md`

## Relations

- @concepts/agent-data-injection-attacks.md — ADI synthesis
- @sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md — complementary MCP taint study (same ingest batch)

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Agent Data Injection Attacks are Realistic Threats to AI Agents |
| Authors | Woohyuk Choi, Juhee Kim, Taehyun Kang, Jihyeon Jeong, Luyi Xing, Byoungyoung Lee |
| Affiliation | Seoul National University; Largosoft; UIUC |
| arXiv | 2607.05120 |
| Code | [github.com/compsec-snu/adi](https://github.com/compsec-snu/adi) |
| Location | `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2607.05120-agent-data-injection-attacks-are-realistic-threa.pdf` |
| Retrieved | 2026-07-09 |
| Read status | **read** (ADI formalization, probabilistic delimiter injection, real-agent PoCs, defense eval) |

## Narrative

Introduces **agent data injection (ADI)** — IPI where attacker-controlled **untrusted data** is misinterpreted as **trusted data** (metadata, tool-call structure, security anchors), not as instructions.

### vs instruction injection (II)

| Attack | Misinterpretation | Defenses bypassed |
|--------|-------------------|-------------------|
| **II** | `DU` → instruction `I` | Dual-LLM, guardrails separating I/D |
| **ADI** | `DU` → trusted `DT` | Same defenses — they only split instruction vs data |

Agent data `D = (DT, DU)` mixes trusted anchors (sender, tool name, resource IDs) with attacker-controlled values in one block.

### Probabilistic delimiter injection

Exploits LLM misreading **inexact delimiters** (`\"`, smart quotes, alternate brackets) as valid structure — JSON ASR **31.3–43.3%**, web DOM **33.3–100%** across six models (GPT-5.2, Claude Opus/Sonnet 4.5, Gemini 3 Pro/Flash).

### Real-world PoCs [CONFIRMED disclosed]

| Target class | Examples | Impact |
|--------------|----------|--------|
| Web agents | Claude in Chrome, Antigravity, Nanobrowser | Arbitrary click (XSS-like) |
| Coding agents | Claude Code, Codex, Gemini CLI | RCE via spoofed maintainer GitHub comment; supply-chain via fake tool response |
| Assistants | ChatGPT, Claude email | Sender spoofing |

### Defense eval (AgentDojo + standalone)

- **II** ASR → **0.0–0.7%** under SOTA agent defenses
- **ADI** ASR up to **50.0%** on same defenses
- CaMeL Strict: **0%** ADI ASR but **36.5%** utility; Randomization: **28.7%** ADI ASR, **83.3%** utility
- Instruction-focused mitigations fail because they do not isolate **DT/DU within agent data**

### Phase-0 (2026-07-09)

| Gate | Status |
|------|--------|
| Artifact | **PARTIAL** — `compsec-snu/adi` benchmark release claimed; verify LICENSE on ingest |
| Domain fit | Core prod-mcp + Claude Code threat model |
| Verdict | **CONDITIONAL-GO** — adopt ADI benchmark for lazy-tool regression; not production runtime until vendor patches land |

## Snippets

> "ADI achieves up to 50.0% ASR while instruction injection achieved near-zero ASR (0.0%–0.7%) against state-of-the-art agent defenses."
[Source: arxiv-2607.05120 abstract — paraphrase anchor]
