---
title: "NVIDIA SkillSpector — agent/MCP skill supply-chain scanner"
type: entity
tags: [tool, ai-security, mcp, skill-audit, supply-chain, langgraph, apache-2.0, adopt]
keywords: [skillspector, nvidia, agent skills, mcp security, prompt injection, tool poisoning, langgraph, osv]
related:
  - concepts/ai-for-cybersecurity.md
  - concepts/npm-supply-chain-defense.md
  - concepts/llm-pentest-automation.md
  - concepts/responsible-disclosure.md
  - entities/tools/defenseclaw.md
  - entities/tools/claude-code-ultimate-guide.md
  - entities/tools/src-hunter-skill.md
  - entities/tools/airguard.md
  - entities/tools/chaincaps.md
  - concepts/agent-runtime-guardrails.md
  - concepts/seclaw-agent-security-evaluation.md
  - sources/arxiv-2605-26542-chaincaps-composition-safe-tool-using-agents.md
  - sources/arxiv-2605-28201-plant-persist-trigger-sleeper-attack.md
  - sources/arxiv-2605-28914-airguard-guarding-agent-actions.md
  - sources/arxiv-2606-01494-clawhub-security-signals.md
  - concepts/mcp-security-posture.md
  - sources/arxiv-mcp-description-code-inconsistency-2606.04769-2026-06-05.md
  - entities/tools/seclaw-eval.md
  - sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md
  - "@osint-wiki/entities/tools/nvidia-skillspector.md"
  - sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md
  - sources/arxiv-2606-07943-poise-position-aware-skill-injection.md
  - entities/tools/malskillbench.md
  - entities/tools/ai-research-skills.md
  - entities/tools/ecc.md
  - entities/tools/skillgate.md
  - sources/openreview-openclaw-real-world-safety-analysis.md
  - concepts/self-evolving-agent-security.md
  - sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md
  - concepts/local-agent-runtime-audit.md
  - entities/tools/clawaudit.md
  - sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md
  - sources/arxiv-2606-31227-ai-infra-guard-technical-report.md
  - concepts/layer-paradigm-agent-red-teaming.md
  - entities/tools/ai-infra-guard.md

maturity: draft
created: 2026-05-31
updated: 2026-07-18
phase_0_verdict: CONDITIONAL-GO 2026-05-31 — mirrors OSINT Phase-0; static `--no-llm` laptop preingest; OSV air-gap probe pending on lab VLAN
---

# NVIDIA SkillSpector — agent/MCP skill supply-chain scanner

## Relations

- @concepts/ai-for-cybersecurity.md — defensive layer for LLM agent deployments
- @concepts/npm-supply-chain-defense.md — analogous supply-chain discipline for agent skills/MCP packages
- @concepts/llm-pentest-automation.md — pentest agents install third-party skills; scan before Tier 2 execution
- @concepts/responsible-disclosure.md — report skill-poisoning findings through vendor timelines
- @entities/tools/defenseclaw.md — complementary MCP/skill governance at enterprise scale
- @entities/tools/claude-code-ultimate-guide.md — static malicious-skill pattern DB vs SkillSpector dynamic scan
- @entities/tools/airguard.md — runtime action-time enforcement after skills pass static scan
- @entities/tools/chaincaps.md — composition IFC for MCP tool chains
- @concepts/agent-runtime-guardrails.md — full agent attack/defense cluster
- @sources/arxiv-2606-01494-clawhub-security-signals.md — empirical scanner disagreement on 67k+ skills (SkillSpector vs VT vs static)
- @entities/tools/src-hunter-skill.md — example high-risk skill surface to vet before install
- @osint-wiki/entities/tools/nvidia-skillspector.md — cross-wiki mirror; OSINT wires into `skill_audit.py` after Phase-0

## Raw Concept

Routed from K88 brief (`briefs/2026-05-31_k88-skillspector-cybersec-from-osint.md`, 2026-05-31). `nvidia/skillspector` — Apache-2.0, ~429 stars, Python. Security scanner for AI agent skills: prompt injection, tool poisoning, malicious patterns.

## Narrative

**Local adoption (2026-07-18):** clone `raw-sources/repos/SkillSpector` (~3.9MB); CLI `skillspector` v2.3.13 via `uv tool install` → `~/.local/bin/skillspector`.


SkillSpector is the **Adopt-tier** defensive tool for auditing agent/MCP skill supply chains before they enter a pentest or SOC copilot workflow. It targets the gap between "we installed a Claude Code skill" and "we verified what that skill can actually do."

**Integration surface**: LangGraph `skillspector.graph` API — embed scans into pre-flight skill onboarding pipelines.

**Import boundary (K88)**:
- **In scope**: cybersec-wiki workstation skill vetting, pentest-agent pre-install checks, blue-team governance workflows.
- **Out of scope**: direct integration into trading-stack / IP-sale-bearing production automation until Phase-0 lab validation completes.
- **Cross-wiki**: OSINT wiki owns `skill_audit.py` wiring post-Phase-0; this page is the cybersec-wiki canonical entity.

**ClawHub empirical note (2026-06-02)**: OpenClaw Foundation + NVIDIA study of 67,453 public skill versions — SkillSpector flags **75.3%** of registry “suspicious” rows but only **6.8%** of “malicious”; VirusTotal leads on bundled-code malware (**72.8%** of malicious rows). Pairwise scanner overlap ≤10.4%. Layer SkillSpector with static + reputation scanners; see @sources/arxiv-2606-01494-clawhub-security-signals.md. `[TENTATIVE]`

**Failure modes**:
- Air-gapped subnets without OSV.dev reachability degrade SC4 supply-chain checks to a small static fallback list. `[CONFIRMED 2026-05-31]` per OSINT Phase-0 source audit — probe on isolated lab VLAN before relying on scans there.
- Default CLI requires LLM API key; automated pipelines must pass **`--no-llm`** (static-only). LLM semantic pass is operator-opt-in.
- Not on PyPI — pin Git SHA; Python **≥3.12**; isolated venv ~228 MB.

## Snippets

```bash
# license verification (K88)
gh api repos/nvidia/skillspector --jq '.license.spdx_id'   # Apache-2.0
```

## Dead Ends

- **Installing unaudited third-party skills because "it's just markdown"** — skills are executable policy; SkillSpector exists because prompt injection and tool-poisoning payloads hide in skill files.
- **Treating static pattern lists (claude-code-ultimate-guide) as sufficient** — signature DBs complement but do not replace dynamic skill-structure analysis.
- **Assuming strong CI recall generalizes to PI** — MalSkillBench reports 98.4% CI recall for best skill-specific tool with collapse on PI/agent-control; pair with runtime verification (@entities/tools/malskillbench.md) and body-line stealth tests (POISE ASR metric). [Source: arXiv:2606.07131, 2606.07943]
