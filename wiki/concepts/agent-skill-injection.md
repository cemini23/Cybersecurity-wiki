---
title: Agent skill injection — attack surface and defenses (K95 cluster)
type: concept
tags: [concept, agent-security, skill-injection, mcp, k95]
keywords: [skill injection, SkillGuard, context poisoning, confused deputy, agent skills]
related:
  - sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md
  - sources/arxiv-2606-01567-skill-injection-defenses-enablers.md
  - sources/arxiv-2606-03024-skillguard-permission-framework.md
  - sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md
  - sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md
  - concepts/mcp-security-posture.md
  - concepts/agent-runtime-guardrails.md
  - entities/tools/defending-code-reference-harness.md
  - concepts/docker-agent-sandbox-allowlist-proxy.md
  - sources/arxiv-2606-04990-agent-traces-evidence-provenance.md
  - concepts/agent-execution-provenance.md
  - sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - entities/tools/malskillbench.md
  - sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md
  - sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md
  - concepts/context-fractured-decomposition-attacks.md
  - "@ccc-wiki/concepts/skill-vetting.md"
  - sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md
  - concepts/agentic-containment-principles.md
  - sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md
  - sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md
  - concepts/agent-least-privilege-tool-selection.md
  - entities/tools/ecc.md
  - entities/tools/skillgate.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
  - concepts/local-agent-runtime-audit.md
  - entities/tools/clawaudit.md
  - sources/arxiv-2606-18673-prompt-leaking-attacks-area.md
  - concepts/system-prompt-leakage.md
  - sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md
  - concepts/self-evolving-agent-security.md
  - concepts/multi-tool-threshold-mcp-poisoning.md
  - sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md
  - entities/tools/reverse-skill.md
  - sources/arxiv-2606-31227-ai-infra-guard-technical-report.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - entities/tools/ai-infra-guard.md
  - sources/arxiv-2607-05120-agent-data-injection-attacks.md
  - concepts/agent-data-injection-attacks.md
  - concepts/skillsec-lifecycle-agent-skill-security.md
  - sources/arxiv-2607-13987-agent-skill-security-skillsec-eval.md
  - concepts/vulnerability-concept-graph-production-agent-red-teaming.md
  - sources/arxiv-2607-11698-agent-hacks-agent-autoresearch.md
  - sources/arxiv-2608-12292-tutor-withhold-refusal-contract.md
  - concepts/refusal-under-knowledge-withhold-contract.md
  - concepts/role-specialization-multi-tool-coordination.md
maturity: draft
created: 2026-06-03
updated: 2026-08-13
wire_status: wont_wire
wire_target: "REFERENCE / steal-from — paper or methodology only"
---

## Relations

- @sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md — cross-app context poisoning
- @sources/arxiv-2606-01567-skill-injection-defenses-enablers.md — defense/enabler taxonomy
- @sources/arxiv-2606-03024-skillguard-permission-framework.md — SkillGuard permissions
- @ccc-wiki/concepts/skill-vetting.md — Cemini Phase-0 skill audit (steal permission model)

- @sources/arxiv-2608-12292-tutor-withhold-refusal-contract.md
- @concepts/refusal-under-knowledge-withhold-contract.md
- @concepts/role-specialization-multi-tool-coordination.md
## Narrative

K95 cluster (2026-06-03 daily digest): three papers on **agent skill / context injection** — platform-level confused-deputy poisoning (ChatGPT Apps), skill-file attack surfaces on coding agents, and **SkillGuard** permission framework.

| Paper | arXiv | Takeaway |
|-------|-------|----------|
| Confused ChatGPT | 2606.00485 | Flat shared context + first-party APIs → cross-app poisoning |
| Defenses & enablers | 2606.01567 | Taxonomy of mitigations vs attack enablers on skill injection |
| SkillGuard | 2606.03024 | Permission framework for agent skills — steal-for skill_audit |

**Cemini relevance:** extend `skill-vetting.md` + prod MCP governance (K94 brief) with permission metadata; no SkillGuard vendor install without Phase-0.

**System prompt overlap (2606.18673):** skill files and `CLAUDE.md` act as **offline system prompts** — LeakBench-style exfiltration applies when users can chat against agents configured with those files. See @concepts/system-prompt-leakage.md.

### Cross-session stored prompt injection (K100 — 2606.04425)

SPI extends skill/MCP injection across **sessions**: poisoned `AGENTS.md`, memory, or tool-visible state can activate after session reset (32–42% E2E-ASR on SPI-Benchmark). Install-time vetting is necessary but not sufficient — audit **write paths to persistent context** and post-reset activation. See @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md and @concepts/mcp-security-posture.md.

### Runtime-verified benchmark (MalSkillBench — 2606.07131)

Hybrid skills need **joint** reasoning over code + instructions. MalSkillBench (3,944 verified malicious + 4,000 benign) shows best skill-specific detector at **98.4% CI recall** but collapse on PI and agent-control; wild-only eval swings rankings up to **66 recall points**. Supply-chain scanners and PI defenses each see half the artifact. See @entities/tools/malskillbench.md and @sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md.

### Stealth body injection (POISE — 2606.07943)

**Attack Success Rate** = payload executes **and** user task passes verifier — models hidden compromise. POISE achieves **89.3% ASR** on Skill-Inject (codex+gpt-5.2) via one benign-looking body line at a feasible numbered-step position; YAML-only placement still **86.7%**. LLM scanner panels false-flag **74.6%** of clean skills; POISE adds only **5.6%** new high-risk alerts. Install-time YAML review + static scanners miss this — add authorized **runtime canary + task verifier** tests. See @sources/arxiv-2606-07943-poise-position-aware-skill-injection.md.

### K114 addendum — architectural memory gap (2606.12797)

Install-time skill vetting addresses **supply-chain SPI** but not **runtime memory integrity (P3)**. Containment-gap audit: LangChain, AutoGPT, and OpenAI Agents SDK all score ✗ on P3 — a single adversarial memory write (fake policy note, poisoned `AGENTS.md` fragment) achieves **100% corruption** on targeted decisions post-write, generalizing to GPT-4o and Claude Haiku. Under complex policies, aggregate accuracy can stay stable while targeted wrongful outcomes rise **3–3.5×** — evading monitors that only track headline accuracy.

**Mitigation pattern:** provenance-tagged memory validator (reject external policy overrides + demographic targeting patterns) + P1 tool policy gate — deterministic, sub-ms. Maps to Cemini: audit write paths to stash, session cache, and wiki-backed agent instructions, not only skill install. See @concepts/agentic-containment-principles.md.

**Adjacent channel — error-path IPI (2606.07992):** MCP tool **errors** (not skill files) can trigger exfil via corrective reasoning; complements skill/MCP description injection in red-team coverage. See @sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md.

### Supply-chain breadth scan (AI-Infra-Guard Agent-Scan — 2606.31227)

Technical report positions **Agent-Scan** as black-box runtime probing plus **agent-skill package** auditing — one of few open-source frameworks claiming end-to-end skill supply-chain coverage alongside MCP-Scan. Use as **external Docker breadth pass** after SkillSpector/SkillGuard static review; does not replace MalSkillBench-style verified eval or POISE runtime canaries. See @entities/tools/ai-infra-guard.md and `briefs/2026-07-01_ai-infra-guard-external-scanner-lab-checklist.md`.

### Over-privileged tool selection among authorized skills (2606.20023)

SkillGuard and install-time vetting bound **which** tools/skills enter the catalog; TOOLPRIVBENCH shows agents still prefer **higher-privilege authorized tools** when lower-privilege ones suffice — especially after transient failures on narrow tools. Skill permission metadata should tag **privilege tier** and harnesses should enforce retry-at-same-tier before escalate. See @concepts/agent-least-privilege-tool-selection.md.

### Pre-install scanner expansion (2026-06-20)

| Scanner | Verdict | Notes |
|---------|---------|-------|
| **Skillgate** (Mitiga SaaS) | Reference | 80+ rules, OWASP Agentic AI mapping; closed source — triage public repos only |
| **ecc-agentshield** (ECC npm) | CONDITIONAL-GO | MIT; config/hook/injection audit — official npm/github only |

Layer with @entities/tools/nvidia-skillspector.md + @entities/tools/defenseclaw.md; see `briefs/2026-06-20_agent-config-scan-stack-phase0.md`. **OpenClaw** runtime source audit: @concepts/local-agent-runtime-audit.md (CLAWAUDIT 2606.21071). Real-world safety paper stubbed: @sources/openreview-openclaw-real-world-safety-analysis.md.

### SkillSec lifecycle (2607.13987 — 2026-07-16)

SkillSec-Eval extends skill security past execution into **admission → retrieval → selection → execution → evolution**. See @concepts/skillsec-lifecycle-agent-skill-security.md. Install-time MalSkillBench scans are necessary but not sufficient. [Source: arXiv 2607.13987]
