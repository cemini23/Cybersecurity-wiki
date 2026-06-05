---
title: MCP security posture — admission, schema honesty, injection
type: concept
tags: [concept, mcp, security, k100, admission-control, spi, dci]
keywords: [mcp, attestation, prompt-injection, description-code, stored-spi, tool-allowlist]
related:
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/defenseclaw.md
  - entities/tools/chaincaps.md
  - entities/tools/nvidia-skillspector.md
  - "@ccc-wiki/concepts/skill-vetting.md"
maturity: validated
created: 2026-06-05
updated: 2026-05-31
---

## Relations

- @sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md — mcp-attested clearance + allowlist
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — cross-session stored SPI
- @sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md — DCI measurement (9.93%)
- @concepts/agent-runtime-guardrails.md — runtime enforcement stack
- @concepts/agent-skill-injection.md — installable skills/MCP as SPI source
- @concepts/llm-pentest-automation.md — ZERO-APT eval under live defense (separate source)
- @entities/tools/defenseclaw.md — MCP/skill scanners + optional admission sidecar
- @entities/tools/chaincaps.md — composition-safe MCP proxy
- @entities/tools/nvidia-skillspector.md — pre-install skill/MCP scan
- @ccc-wiki/concepts/skill-vetting.md — Phase-0 install gate

## Raw Concept

K100 deep-read batch (2026-05-31): four arXiv papers defining **MCP/tool-server trust boundaries** for agent harness engineering — synthesized after arXiv HTML deep pass + PDF archive.

## Narrative

MCP makes tool integration easy by exposing **metadata-only** interfaces to the LLM. Security fails when operators treat that metadata as ground truth. K100 maps three independent failure classes plus the evaluation gap:

### Layer model

| Layer | Threat | K100 source | Portable control |
|-------|--------|-------------|------------------|
| **Admission** | Host connects to wrong server or over-exposes tool surface | 2605.24248 attested admission | Per-server **closed allowlist**; optional Ed25519 clearance at `/.well-known/…`; hash-chained audit |
| **Semantic honesty** | Description/schema ≠ code behavior | 2606.04769 DCI (9.93% in wild) | mcp-scanner + DCIChecker-class description↔code cross-check before prod allowlist |
| **Persistence** | Injection survives session reset via memory/files/tool state | 2606.04425 SPI (32–42% E2E-ASR) | Write-path governance; treat `AGENTS.md`/memory/tool artifacts as strong-persistence channels |
| **Eval realism** | Pentest agents never face live defense | 2606.05567 ZERO-APT | Benchmark Tier-2 agents against configurable Defender — see @concepts/llm-pentest-automation.md |

### Confused deputy chain

```
Untrusted content → (write) persistent state / tool list
                 → (load) context constructor 𝒜
                 → LLM selects tool from description D
                 → implementation C executes (possibly ≠ D)
```

Attestation blocks **unauthorized tools** before `tools/call`. DCI asks whether **authorized tools lie**. SPI asks whether **past sessions poison future 𝒜**. No single product covers all three — @entities/tools/defenseclaw.md covers scan + optional admission; human GO still required for write MCPs on prod-mcp/lazy-tool.

### Cemini / lazy-tool checklist [TENTATIVE]

1. `defenseclaw mcp-scanner` / skillspector on manifest before catalog entry.
2. Closed tool allowlist per server (steal mcp-attested pattern even without crypto).
3. No auto-load of file-backed agent instructions from untrusted workspaces without review.
4. Session-reset tests for SPI on any harness storing memory across chats.
5. Re-scan on MCP version bump (DCI drift).

## Snippets

| Paper | Headline stat |
|-------|---------------|
| 2605.24248 | Additive extension — no MCP message changes |
| 2606.04769 | **9.93%** DCI rate / 19,200 pairs |
| 2606.04425 | **74–82%** fact-manipulation E2E-ASR |
| 2606.05567 | **79%** ASR vs adaptive Defender (Windows post-exploit lab) |

## Dead Ends

- **Attestation alone** — does not prove description–code alignment or block SPI writes to agent memory.
- **Scanner-only posture** — pre-connect scan misses runtime description drift until re-scan cadence enforced.
