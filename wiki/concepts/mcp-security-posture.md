---
title: MCP security posture — admission, schema honesty, injection
type: concept
tags: [concept, mcp, security, k100, admission-control, spi, dci]
keywords: [mcp, attestation, prompt-injection, description-code, stored-spi, tool-allowlist]
related:
  - sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
  - concepts/agent-runtime-guardrails.md
  - concepts/agent-skill-injection.md
  - concepts/llm-pentest-automation.md
  - concepts/ai-for-cybersecurity.md
  - entities/tools/defenseclaw.md
  - entities/tools/chaincaps.md
  - entities/tools/nvidia-skillspector.md
  - "@ccc-wiki/concepts/skill-vetting.md"
  - sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - concepts/context-fractured-decomposition-attacks.md
  - concepts/enterprise-mcp-adoption-interviews.md
  - entities/tools/ai-research-skills.md
  - sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
  - concepts/agentic-containment-principles.md
  - sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md
  - concepts/trajectory-context-control.md
  - sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md
  - concepts/llm-code-review-agent-security.md
  - entities/tools/sevra-bench.md
  - sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md
  - concepts/internet-of-agentic-ai-ioai.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/agent-least-privilege-tool-selection.md
  - entities/tools/toolprivbench.md
maturity: validated
created: 2026-06-05
updated: 2026-06-19
---

## Relations

- @sources/arxiv-attested-tool-server-admission-2605.24248-2026-06-05.md — mcp-attested clearance + allowlist
- @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md — cross-session stored SPI
- @sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md — DCI measurement (9.93%)
- @sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md — WebMCP MSTI (mid-session tool registry)
- @sources/arxiv-2606-04990-agent-traces-evidence-provenance.md — provenance survey (2606.04990)
- @concepts/agent-execution-provenance.md — process accountability layer
- @concepts/agent-runtime-guardrails.md — runtime enforcement stack
- @concepts/agent-skill-injection.md — installable skills/MCP as SPI source
- @concepts/llm-pentest-automation.md — ZERO-APT eval under live defense (separate source)
- @entities/tools/defenseclaw.md — MCP/skill scanners + optional admission sidecar
- @entities/tools/chaincaps.md — composition-safe MCP proxy
- @entities/tools/nvidia-skillspector.md — pre-install skill/MCP scan
- @ccc-wiki/concepts/skill-vetting.md — Phase-0 install gate
- @sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md — error-path implicit authority (K114)
- @sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md — framework containment gap (K114)
- @concepts/agentic-containment-principles.md — P1–P6 audit matrix
- @sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md — GT-MCP trajectory layer (Reference)
- @concepts/trajectory-context-control.md — memory-commit gate above MCP transport

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
| **Runtime surface** | Mid-session tool list mutation in browser WebMCP | 2606.06387 MSTI | OBAC + origin-bound registration; freeze tool catalog after task start; log registration events |
| **Error-path IPI** | Tool **error** responses trigger corrective mode; implicit authority bypasses skepticism | 2606.07992 VATS | Split error code vs help text; verify error provenance; red-team error-path mutations; human gate on error-triggered writes |
| **Trajectory evolution** | Accepted tool/RAG/agent outputs merge into persistent context without drift gate | 2606.10322 GT-MCP | Multi-model probe + CCI/AGR/CDS trust gate before memory commit; checkpoint rollback on high drift |

### Confused deputy chain

```
Untrusted content → (write) persistent state / tool list
                 → (load) context constructor 𝒜
                 → LLM selects tool from description D
                 → implementation C executes (possibly ≠ D)
```

Attestation blocks **unauthorized tools** before `tools/call`. DCI asks whether **authorized tools lie**. SPI asks whether **past sessions poison future 𝒜**. MSTI asks whether **the tool catalog itself changes mid-task** (WebMCP registry hijack/framing — up to 100% exfil ASR on registration race, 85% task completion on framing attacks). No single product covers all four — @entities/tools/defenseclaw.md covers scan + optional admission; human GO still required for write MCPs on prod-mcp/lazy-tool.

### Cemini / lazy-tool checklist [TENTATIVE]

1. `defenseclaw mcp-scanner` / skillspector on manifest before catalog entry.
2. Closed tool allowlist per server (steal mcp-attested pattern even without crypto).
3. No auto-load of file-backed agent instructions from untrusted workspaces without review.
4. Session-reset tests for SPI on any harness storing memory across chats.
5. Re-scan on MCP version bump (DCI drift).
6. For browser WebMCP: treat dynamic tool registration as untrusted; require origin binding + registration audit log (2606.06387 MSTI).
7. Log tool-call provenance (params + source labels) for audit — untrusted MCP metadata is not ground truth (2606.04990).

## Snippets

| Paper | Headline stat |
|-------|---------------|
| 2605.24248 | Additive extension — no MCP message changes |
| 2606.04769 | **9.93%** DCI rate / 19,200 pairs |
| 2606.04425 | **74–82%** fact-manipulation E2E-ASR |
| 2606.05567 | **79%** ASR vs adaptive Defender (Windows post-exploit lab) |
| 2606.06387 | **100%** MSTI registration-race ASR; **85%** task completion on framing attacks |

## Dead Ends

- **Attestation alone** — does not prove description–code alignment or block SPI writes to agent memory.
- **Scanner-only posture** — pre-connect scan misses runtime description drift until re-scan cadence enforced.

### K114 addendum (2026-06-13)

**VATS (2606.07992)** isolates the MCP **error-handling loop** as a distinct injection channel: error-path IPI achieves **3×** baseline tool-response IPI ACR; one mutation generation reaches **100% ACR** on four frontier models. **$M_4 \rightarrow$ middle** (instruction sandwiched in error context) is the only universal exploit. Production CLI frameworks (Gemini CLI, Codex) blocked exfil via repo guardrails + functional redundancy — raw API layer remains fully vulnerable. Add error-path cases to lazy-tool / prod-mcp red-team alongside DCI and MSTI.

**Containment gap (2606.12797)** complements MCP-layer controls with **architectural P1–P6 audit**: zero native ✓ on any principle across LangChain / AutoGPT / OpenAI Agents SDK; universal P3 (memory integrity) failure. See @concepts/agentic-containment-principles.md.

**GT-MCP (2606.10322)** adds a **trajectory layer** above passive MCP routing: trust-weighted multi-agent selection + causal graph + drift-triggered rollback before persistent context merge (0.0% controller ISR vs 17.8% single-agent in paper eval). Reference only until code ships — see @concepts/trajectory-context-control.md and `briefs/2026-06-15_gt-mcp-trajectory-context-control-harness.md`. Re-audit 2026-06-17: still no public GT-MCP repo.

**IoAI (2606.12835)** positions MCP as an emerging **interoperability layer** for Internet-scale agent federation. Our prod-mcp stack is a **closed IoAI cell** — Table 4 threat taxonomy maps to K100 + K114 controls; federated identity/incentive rows remain open gaps. See @concepts/internet-of-agentic-ai-ioai.md and `briefs/2026-06-17_ioai-threat-taxonomy-prod-mcp-handoff.md`.

**Over-privileged tool selection (2606.20023)** — even with closed allowlists, agents may pick the **broadest authorized tool** when a narrow one suffices; OPUR spikes after transient narrow-tool failures (503/timeout). Admission/DCI/SPI do not measure this — add TOOLPRIVBENCH-style paired-tool eval + runtime authority narrowing (AIRGuard). AgentHarm/refusal benchmarks are **not** a proxy. See @concepts/agent-least-privilege-tool-selection.md and `briefs/2026-06-19_toolprivbench-prod-mcp-eval-checklist.md`.
