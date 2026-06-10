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
  - "@ccc-wiki/concepts/skill-vetting.md"
maturity: draft
created: 2026-06-03
updated: 2026-06-09
---

## Relations

- @sources/arxiv-2606-00485-confused-chatgpt-cross-app-context-poisoning.md — cross-app context poisoning
- @sources/arxiv-2606-01567-skill-injection-defenses-enablers.md — defense/enabler taxonomy
- @sources/arxiv-2606-03024-skillguard-permission-framework.md — SkillGuard permissions
- @ccc-wiki/concepts/skill-vetting.md — Cemini Phase-0 skill audit (steal permission model)

## Narrative

K95 cluster (2026-06-03 daily digest): three papers on **agent skill / context injection** — platform-level confused-deputy poisoning (ChatGPT Apps), skill-file attack surfaces on coding agents, and **SkillGuard** permission framework.

| Paper | arXiv | Takeaway |
|-------|-------|----------|
| Confused ChatGPT | 2606.00485 | Flat shared context + first-party APIs → cross-app poisoning |
| Defenses & enablers | 2606.01567 | Taxonomy of mitigations vs attack enablers on skill injection |
| SkillGuard | 2606.03024 | Permission framework for agent skills — steal-for skill_audit |

**Cemini relevance:** extend `skill-vetting.md` + prod MCP governance (K94 brief) with permission metadata; no SkillGuard vendor install without Phase-0.

### Cross-session stored prompt injection (K100 — 2606.04425)

SPI extends skill/MCP injection across **sessions**: poisoned `AGENTS.md`, memory, or tool-visible state can activate after session reset (32–42% E2E-ASR on SPI-Benchmark). Install-time vetting is necessary but not sufficient — audit **write paths to persistent context** and post-reset activation. See @sources/arxiv-prompt-injection-persistence-2606.04425-2026-06-05.md and @concepts/mcp-security-posture.md.

### Runtime-verified benchmark (MalSkillBench — 2606.07131)

Hybrid skills need **joint** reasoning over code + instructions. MalSkillBench (3,944 verified malicious + 4,000 benign) shows best skill-specific detector at **98.4% CI recall** but collapse on PI and agent-control; wild-only eval swings rankings up to **66 recall points**. Supply-chain scanners and PI defenses each see half the artifact. See @entities/tools/malskillbench.md and @sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md.

### Stealth body injection (POISE — 2606.07943)

**Attack Success Rate** = payload executes **and** user task passes verifier — models hidden compromise. POISE achieves **89.3% ASR** on Skill-Inject (codex+gpt-5.2) via one benign-looking body line at a feasible numbered-step position; YAML-only placement still **86.7%**. LLM scanner panels false-flag **74.6%** of clean skills; POISE adds only **5.6%** new high-risk alerts. Install-time YAML review + static scanners miss this — add authorized **runtime canary + task verifier** tests. See @sources/arxiv-2606-07943-poise-position-aware-skill-injection.md.
