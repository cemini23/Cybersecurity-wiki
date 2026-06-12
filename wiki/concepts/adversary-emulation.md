---
title: Adversary Emulation
type: concept
tags: [red-team, methodology, mitre]
keywords: [adversary emulation, apt emulation, emulation plan, ttp]
related:
  - concepts/cyberwarfare.md
  - concepts/purple-team-operations.md
  - concepts/red-team-operations.md
  - entities/certifications/crto.md
  - entities/frameworks/cyber-kill-chain.md
  - entities/frameworks/mitre-attack.md
  - entities/people/joas-a-santos.md
  - entities/threat-actors/apt28.md
  - entities/threat-actors/apt29.md
  - entities/threat-actors/lazarus.md
  - entities/tools/caldera.md
  - entities/tools/cobalt-strike.md
  - sources/adversary-emulation-and-cracking-the-bridge-overview.md
  - sources/adversary-emulation-com-cobalt-strike.md
  - sources/adversary-emulation-matrix-by-joas.md
  - sources/adversary-emulation-services.md
  - sources/adversary-simulation-with-caldera-and-mitre.md
  - sources/red-team-operations-simulando-um-grupo-apt-na-pratica.md
  - sources/red-team-operations-simulating-an-apt-group-in-practice.md
  - sources/for-red-team-operation.md
  - sources/practical-redteaming.md
  - sources/red-team-guides.md
  - sources/the-hacker-playbook-3-practical.md
  - entities/tools/red-run.md
  - sources/mitre-attack-framework-soc.md
  - concepts/threat-intelligence.md
  - sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md
  - sources/arxiv-zero-apt-llm-pentest-2606.05567-2026-06-05.md
  - sources/arxiv-2606-08700-autosut-environment-semantics-gap.md
  - entities/tools/autosut.md
maturity: validated
created: 2026-05-12
updated: 2026-06-11
---

## Relations

- @concepts/cyberwarfare.md
- @concepts/purple-team-operations.md
- @concepts/red-team-operations.md
- @entities/certifications/crto.md
- @entities/frameworks/cyber-kill-chain.md
- @entities/frameworks/mitre-attack.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/apt28.md
- @entities/threat-actors/apt29.md
- @entities/threat-actors/lazarus.md
- @entities/tools/caldera.md
- @entities/tools/cobalt-strike.md
- @sources/adversary-emulation-and-cracking-the-bridge-overview.md
- @sources/adversary-emulation-com-cobalt-strike.md
- @sources/adversary-emulation-matrix-by-joas.md
- @sources/adversary-emulation-services.md
- @sources/adversary-simulation-with-caldera-and-mitre.md
- @sources/red-team-operations-simulando-um-grupo-apt-na-pratica.md
- @sources/red-team-operations-simulating-an-apt-group-in-practice.md


- @sources/for-red-team-operation.md
- @sources/practical-redteaming.md
- @sources/red-team-guides.md
- @sources/the-hacker-playbook-3-practical.md
- @entities/tools/red-run.md — autonomous pentest-agent + Sliver C2 orchestrator (reference-only)
- @sources/mitre-attack-framework-soc.md
- @concepts/threat-intelligence.md

## Raw Concept

Corpus has 7+ PDFs that scope explicitly into adversary emulation (Adversary Emulation com Cobalt Strike, Adversary Emulation Matrix, Adversary Emulation Services, Adversary Simulation with Caldera and Mitre, Red Team Operations – Simulando um grupo APT na prática, etc.).

## Narrative

Adversary Emulation is a proactive cybersecurity practice in which an organization simulates real-world attack scenarios — modeled on a chosen APT's TTPs — to identify vulnerabilities in systems, processes, and defenses, and to evaluate the security posture by *thinking like* a potential attacker. [Source: Red Team Operations – Concepts #1.pdf]

**Emulation plan structure** [CONFIRMED]

1. **Scope Definition** — objectives, constraints, boundaries. Which systems/networks/assets are in scope. Rules of engagement.
2. **Reconnaissance** — preliminary OSINT, network discovery, attack-surface mapping.
3. **Threat Modeling** — analyze target infra + apps; map architecture; identify weak points + attack paths.
4. **Tactic Selection** — which APT-style TTPs the emulation will use (social engineering / network exploitation / privilege escalation / lateral movement, etc.).
5. **Planning** — detailed step sequence, timeline, resources, contingency plans, stakeholder approvals.
6. **Execution** — deploy specialized tools, exploit vulnerabilities, attempt unauthorized access, exfiltrate sensitive (test) data per the chosen profile.
7. **Detection Evasion** — APT-style — bypass IDS/AV/EDR, leverage 0-days where in scope.
8. **Post-Exploitation + Persistence** — establish footholds (backdoors, persistent malware, privileged accounts) to test long-term-access scenarios.
9. **Reporting** — findings, observations, recommendations. Each finding ties back to a TTP and to detection gaps.
10. **Remediation** — work with the blue team to address findings.
11. **Follow-Up Testing** — verify remediation closed the actual technique, not just the symptom.

[Source: Red Team Operations – Concepts #1.pdf]

**Public emulation plans** to start from rather than design from scratch:
- [MITRE APT3 Adversary Emulation Plan](https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf)
- [MITRE Engenuity Center for Threat-Informed Defense](https://github.com/center-for-threat-informed-defense) — FIN6, menuPass, Carbanak+FIN7 plans
- [SCYTHE Community Threats](https://github.com/scythe-io/community-threats)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) — atomic tests keyed to ATT&CK techniques

**Threat Intelligence pre-work** is what separates good emulation from theater. The TTPs you pick must come from real threat-intel reports about the threat actor you're emulating — otherwise you're testing against fiction. See @concepts/threat-hunting.md and @entities/threat-actors/apt28.md.

### LLM-driven emulation fidelity vs distinguishability (2606.07158)

Alias Robotics CSI agents emulating APT28/29/41/44 and Lazarus on CYBER RANGES showed **55–80% MITRE ATT&CK precision** vs official profiles when enterprise domains fell — but **identical Recon + Initial Access** across all personas regardless of assigned APT. In 8/10 enterprise runs, every persona independently weaponized defender **Velociraptor** as C2 (not in any profile). **Topology dominated outcomes** (enterprise 10/10 compromised; military 10/10 defended) more than persona choice.

**Purple-team implication:** emulation plans must test **convergent AI tradecraft** and defender-tool abuse — not only catalog TTP replay. Attribution exercises built on early-phase TTPs alone will mis-fire when the attacker is a generic LLM stack. See @sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md and @concepts/threat-intelligence.md.

### Environment semantics gap (AutoSUT — 2606.08700)

Public ATT&CK STIX narrows platform/backend family but **does not uniquely determine** replay-ready SUTs: **97.6%** of Enterprise software objects lack version+CPE; holding corpus-fixed elements, varying analyst-authored region yields multiple campaign-compatible environments (witness: CVE-2021-41773). Emulation plans must label **corpus-supported** vs **analyst-authored** environment commitments. See @entities/tools/autosut.md and @sources/arxiv-2606-08700-autosut-environment-semantics-gap.md.
