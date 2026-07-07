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
  - entities/tools/ecc.md
  - entities/tools/skillgate.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md
  - concepts/agent-probabilistic-datalog-verification.md
  - sources/arxiv-2606-18673-prompt-leaking-attacks-area.md
  - concepts/system-prompt-leakage.md
  - entities/tools/leakbench-area.md
  - sources/arxiv-2606-22659-confidently-wrong-prompt-injection-calibration.md
  - concepts/prompt-injection-detector-calibration.md
  - sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md
  - concepts/self-evolving-agent-security.md
  - sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md
  - concepts/cross-tool-description-poisoning.md
  - entities/tools/tool-guard.md
  - sources/arxiv-2606-22504-portico-lingering-authority-coding-agents.md
  - concepts/lingering-authority-revocable-capabilities.md
  - sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md
  - concepts/intent-governed-tool-authorization.md
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
  - concepts/local-agent-runtime-audit.md
  - entities/tools/clawaudit.md
  - sources/arxiv-2606-24496-red-teaming-the-agentic-red-team.md
  - concepts/agentic-offensive-security-kill-chain.md
  - sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md
  - concepts/multi-tool-threshold-mcp-poisoning.md
  - sources/arxiv-2606-25819-toolbench-x-tool-environment-unreliability.md
  - concepts/tool-environment-unreliability-eval.md
  - entities/tools/toolbench-x.md
  - sources/arxiv-2606-23449-aohp-os-level-agent-harness.md
  - entities/tools/aohp.md
  - entities/tools/reverse-skill.md
  - sources/arxiv-2606-31227-ai-infra-guard-technical-report.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - entities/tools/ai-infra-guard.md
  - sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md
  - concepts/confidence-aware-tool-orchestration.md
  - sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
  - concepts/mcp-execution-control-invariants.md
  - entities/tools/handle-capability-protocol.md
  - sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - concepts/security-tool-orchestration-determinants.md
  - sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md
maturity: validated
created: 2026-06-05
updated: 2026-07-07
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
| **Execution control** | Connection-layer approvals insufficient; metadata grants hidden invokes | 2606.29073 HCP | Eight invariants (I1–I8): grant-backed approval, principal binding, data-pipe auth, deny-path audit |

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

**Pre-install scan stack (2026-06-20 digest)** — three new triage surfaces: **Skillgate** (Mitiga SaaS, Reference), **ecc-agentshield** (MIT npm, CONDITIONAL-GO), layered with SkillSpector + DefenseClaw. Scanner disagreement remains expected — no single allow/block. See `briefs/2026-06-20_agent-config-scan-stack-phase0.md`.

**Probabilistic runtime verification (2606.20510)** — MCP intercept paths that rely on **noisy content classifiers** (PII/secret scan) need distributionally robust bounds when failures correlate across batched tool responses — deterministic Boolean taint + naive P(violation) thresholds under-bound leak risk. Complements admission/DCI/SPI; Phase-0 **Reference**. See @concepts/agent-probabilistic-datalog-verification.md and `briefs/2026-06-21_probabilistic-agent-guardrail-dro-handoff.md`.

**System prompt leakage (2606.18673)** — custom GPT/copilot **hidden instructions** (including skill preambles and MCP routing rules) leak in **>80%** of measured commercial apps; prompt-append defenses fail via **attention drift**. Orthogonal to SPI/DCI but same assessment window — add LeakBench-style exfil probes. See @concepts/system-prompt-leakage.md and `briefs/2026-06-22_system-prompt-leak-redteam-checklist.md`.

**Guard calibration under shift (2606.22659)** — ProtectAI / Prompt-Guard-2 can miss **indirect behavior-hijack** with **severity S ≈ 1.0** on false negatives. Shift-test on MCP tool-return channel; never deploy on pooled ECE alone. See @concepts/prompt-injection-detector-calibration.md and `briefs/2026-06-23_prompt-guard-severity-calibration-handoff.md`.

**Self-evolving agents (2606.23075)** — MLAS matrix: evolution removes immutable anchors; Hermes case **100% attack persistence**, scanners **2.5%** on evolution path. Default deny self-modifying agents on prod-mcp. See @concepts/self-evolving-agent-security.md.

**Cross-tool description poisoning (2606.20922)** — poisoned metadata on tool A steers planner toward tool B without invoking A; PI defenses leave **19–43%** ASR on AgentDojo vs **2.06%** under Tool-Guard **isolated planning** (influenced-list quarantine). Orthogonal to DCI/MSTI. Phase-0 **CONDITIONAL-GO** on `shishishi123/Tool-Guard` (MIT). See @concepts/cross-tool-description-poisoning.md and `briefs/2026-06-24_tool-guard-isolated-planning-prod-mcp-handoff.md`.

**Lingering authority (2606.22504)** — planner-interface exposure after subgoal closure; PORTICO revokes epoch-bound handles (**10/10** post-closure replay blocked). Complements OPUR/AIRGuard temporal gap. **Reference** until artifact ships. See @concepts/lingering-authority-revocable-capabilities.md and `briefs/2026-06-24_portico-lingering-authority-coding-agent-handoff.md`.

**IGAC (2606.22916)** — server-side intent certificates + manifest narrowing; static OpenPort still allowed **85.71%** of high-risk requests. Sits above admission, before planner. **Reference**. See @concepts/intent-governed-tool-authorization.md and `briefs/2026-06-24_igac-intent-governed-tool-auth-handoff.md`.

**Local runtime audit (2606.21071)** — CLAWAUDIT Semgrep/CodeQL on OpenClaw source (**66.8% / 75.1%** recall vs baselines); complements scanner-only posture. Phase-0 **CONDITIONAL-GO** (`SRestLabUB/ClawAudit`, no LICENSE file). See @concepts/local-agent-runtime-audit.md and `briefs/2026-06-24_clawaudit-openclaw-runtime-audit-checklist.md`.

**Agentic red-team reverse-audit (2606.24496)** — 10/12 OSS pentest agents compromised via **agent-phishing** (97.8% honeypot success, no prompt injection). Worker-as-malicious architecture required: secrets on orchestrator, no docker.sock/`--network=host`. See @concepts/agentic-offensive-security-kill-chain.md and `briefs/2026-06-25_agentic-red-team-secure-architecture-handoff.md`.

**Multi-tool threshold poisoning (2606.27027)** — ShareLock splits malicious MCP instructions via **Shamir shares** across tool descriptions; **93.3%** avg ASR vs **75.3%** monolithic TPA; entropy dilution defeats per-tool Shannon heuristics; Llama-Guard-class detectors score lower hazard than TPA. Per-tool review insufficient — audit **catalog as a set**. Phase-0 **Reference** (no artifact). See @concepts/multi-tool-threshold-mcp-poisoning.md and `briefs/2026-06-26_sharelock-multi-tool-threshold-mcp-redteam-checklist.md`.

**Layer-paradigm red teaming (2606.31227)** — AI-Infra-Guard **MCP-Scan** (protocol/tool layer) complements admission + DCI gates here; does not replace attested allowlists or closed tool catalogs. Use as **breadth audit** after admission, before runtime agent probes. External Docker only (@entities/tools/ai-infra-guard.md). See @concepts/layer-paradigm-agent-red-teaming.md and `briefs/2026-07-01_ai-infra-guard-layer-paradigm-red-team-handoff.md`.

**Tool-environment unreliability (2606.25819)** — ToolBench-X: agents scoring well on clean **P₀** tools drop to **<0.51** under recoverable hazards (spec drift, invocation errors, output drift, cross-source conflict). **Hint-after-failure recovers 60–80%** of lost accuracy — diagnosis bottleneck for prod MCP. Phase-0 **Reference** until repo ships. See @concepts/tool-environment-unreliability-eval.md and `briefs/2026-06-27_toolbench-x-prod-mcp-reliability-eval-checklist.md`.

**Confidence-aware orchestration (2606.26904)** — Robust-TO **Blind Trust Problem**: agents act on degraded tool/perception outputs without downgrading confidence. Steal `(result, confidence)` MCP wrappers + tiered evidence fusion before high-impact tool chains. Phase-0 **Reference** (CV paper; code pending). See @concepts/confidence-aware-tool-orchestration.md and `briefs/2026-07-02_prod-mcp-tool-confidence-contract-checklist.md`.

**Execution-control invariants (2606.29073)** — HCP: connection-layer mitigations (metadata lint + per-call approval) permit **6/10** modeled attacks; execution-control runtime blocks **10/10** with deny-path audit. Eight invariants I1–I8 cover metadata non-authority, grant-backed approval, data-pipe auth. Phase-0 **CONDITIONAL-GO** (MIT, 0★). See @concepts/mcp-execution-control-invariants.md and `briefs/2026-07-04_prod-mcp-eight-invariants-checklist.md`.

**Substrate oversight (2607.02389)** — For **local owned code**, MCP-mediated retrieval can saturate reviewer context; ~200 LoC AST `docs` CLI + enforceable substrate (linters/types/contracts) lifts small-reviewer backdoor recall **54.5% → 90.9%**. Complements connection/execution layers — does not replace untrusted MCP admission. Phase-0 **Reference**. See @concepts/substrate-constraints-coding-agent-oversight.md and `briefs/2026-07-07_harness-substrate-constraints-checklist.md`.

**Batch handoff index (2026-06-24)** — CCC routing for Tool-Guard / CLAWAUDIT / PORTICO / IGAC ingest: `briefs/2026-06-24_ccc-handoff-agent-security-ingest-batch.md`.
