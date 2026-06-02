---
title: "ClawHub Security Signals — scanner disagreement on agent skills (arXiv:2606.01494)"
type: source
tags: [arxiv, agent-security, skill-supply-chain, skillspector, openclaw, research-paper]
keywords: [clawhub, skillspector, virustotal, scanner disagreement, agent skills, openclaw foundation]
related:
  - concepts/agent-runtime-guardrails.md
  - concepts/npm-supply-chain-defense.md
  - entities/tools/nvidia-skillspector.md
  - entities/tools/claude-code-ultimate-guide.md
  - sources/arxiv-2605-29251-provably-secure-agent-guardrail.md
maturity: draft
read_status: read
created: 2026-06-02
updated: 2026-06-02
---

## Relations

- @concepts/agent-runtime-guardrails.md — layered skill governance vs single-scanner allow/block
- @concepts/npm-supply-chain-defense.md — skill supply chain analogous to package malware scanning
- @entities/tools/nvidia-skillspector.md — SkillSpector as semantic agentic-risk scanner in study
- @entities/tools/claude-code-ultimate-guide.md — static pattern DB vs VT vs SkillSpector disagreement
- @sources/arxiv-2605-29251-provably-secure-agent-guardrail.md — formal guardrail complement to empirical scanner stack

## Raw Concept

- **Title**: ClawHub Security Signals: When VirusTotal, Static Analysis, and SkillSpector Disagree
- **Authors**: Vincent Koc, Patrick Erichsen (OpenClaw Foundation); Jacob Tomlinson, Agustin Rivera, Michael Appel, Nir Paz (NVIDIA)
- **Type**: arXiv preprint
- **Location**: `raw-sources/arxiv-2606.01494-clawhub-security-signals-when-virustotal-static.pdf`
- **URL**: https://arxiv.org/abs/2606.01494
- **Dataset**: https://huggingface.co/datasets/OpenClaw/clawhub-security-signals
- **Retrieved**: 2026-06-02
- **Read-status**: read

## Narrative

Sanitized dataset of **67,453** public OpenClaw skill versions with ClawScan registry verdicts from three scanner families: **VirusTotal**, static heuristics, and **NVIDIA SkillSpector**. Core finding: scanners **rarely agree** — max pair overlap 10.4% of combined positives; only **0.69%** flagged by all three; **81.9%** of flagged skills hit by a single scanner only.

**SkillSpector** catches semantic agentic-risk (75.3% of suspicious rows) but only **6.8%** of rows labeled malicious (VT better on bundled-code malware: 72.8% of malicious rows). Implication for cybersec wiki: **layered governance** (static + reputation + semantic skill audit) — aligns with @entities/tools/nvidia-skillspector.md + static skill pattern lists — not one allow/block gate.

Labels are automated registry verdicts, not human ground truth `[TENTATIVE]`.

## Snippets

> "Agent skills function as an execution layer that determines what agents do with tools, rather than merely specifying which tools are available." — OWASP Agentic Skills Top 10 cited

> "These results show that agent-skill security requires layered governance, not single-scanner allow/block decisions."
