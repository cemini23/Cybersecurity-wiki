---
title: MITRE ATT&CK
type: entity
tags: [framework, threat-intel, tactics-techniques-procedures]
keywords: [mitre, att&ck, attack matrix, ttps, tactics, techniques, procedures, navigator]
related:
  - concepts/adversary-emulation.md
  - concepts/av-edr-bypass.md
  - concepts/red-team-operations.md
  - concepts/threat-hunting.md
  - entities/frameworks/cyber-kill-chain.md
  - entities/people/joas-a-santos.md
  - entities/threat-actors/apt28.md
  - entities/threat-actors/apt29.md
  - entities/threat-actors/lazarus.md
  - entities/threat-actors/lockbit.md
  - entities/tools/caldera.md
  - sources/adversary-emulation-matrix-by-joas.md
  - sources/adversary-simulation-with-caldera-and-mitre.md
  - sources/introducao-ao-mitre-att-ck-e-ao-cyber-kill-chain.md
  - sources/mitre-att-ck-study-overview.md
  - sources/red-team-macos-att-ck-overview.md
  - sources/red-team-operations-concepts-1.md
  - sources/tdc2021-mitre-att-ck.md
  - concepts/credential-access.md
  - sources/mitre-attack-framework-soc.md
  - entities/tools/sysmon.md
  - concepts/ransomware.md
  - sources/ransomware-investigation-runbook.md
  - concepts/threat-intelligence.md
  - sources/open-source-soc-guide.md
  - entities/tools/splunk.md
  - sources/100-splunk-queries-soc-analyst.md
  - entities/tools/nidhogg.md
  - sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md
  - sources/arxiv-2606-08700-autosut-environment-semantics-gap.md
  - entities/tools/autosut.md
  - sources/arxiv-2606-08173-ai-native-closed-loop-6g-cps-security.md
  - concepts/6g-cps-closed-loop-security.md
  - concepts/autonomous-defense-agent-transferability.md
  - sources/arxiv-2606-21377-arena-autonomous-defense-transferability.md
  - concepts/llm-cve-to-stix-generation.md
  - entities/tools/cav-stixgen.md
  - sources/arxiv-2607-16175-cav-stixgen-open-weight-stix.md
  - concepts/symbolic-art-attack-chain-granularity.md
  - sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md

maturity: validated
created: 2026-05-12
updated: 2026-08-04
---

## Relations

- @concepts/adversary-emulation.md
- @concepts/av-edr-bypass.md
- @concepts/red-team-operations.md
- @concepts/threat-hunting.md
- @entities/frameworks/cyber-kill-chain.md
- @entities/people/joas-a-santos.md
- @entities/threat-actors/apt28.md
- @entities/threat-actors/apt29.md
- @entities/threat-actors/lazarus.md
- @entities/threat-actors/lockbit.md
- @entities/tools/caldera.md
- @sources/adversary-emulation-matrix-by-joas.md
- @sources/adversary-simulation-with-caldera-and-mitre.md
- @sources/introducao-ao-mitre-att-ck-e-ao-cyber-kill-chain.md
- @sources/mitre-att-ck-study-overview.md
- @sources/red-team-macos-att-ck-overview.md
- @sources/red-team-operations-concepts-1.md
- @sources/tdc2021-mitre-att-ck.md


- @concepts/credential-access.md
- @sources/mitre-attack-framework-soc.md
- @entities/tools/sysmon.md
- @concepts/ransomware.md
- @sources/ransomware-investigation-runbook.md
- @concepts/threat-intelligence.md
- @sources/open-source-soc-guide.md
- @entities/tools/splunk.md
- @sources/100-splunk-queries-soc-analyst.md
- @entities/tools/nidhogg.md — T1014 rootkit / DKOM tradecraft reference (GPL-3.0; defensive mapping)
- @concepts/llm-cve-to-stix-generation.md — LLM ATT&CK mapping from CVE text remains hard (Match@All)
- @entities/tools/cav-stixgen.md
- @sources/arxiv-2607-16175-cav-stixgen-open-weight-stix.md
- @concepts/symbolic-art-attack-chain-granularity.md
- @sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md

## Raw Concept

MITRE ATT&CK is the lingua franca for describing adversary behavior in modern cybersecurity. Appears in dozens of corpus titles (Mitre Att&ck Study Overview, Adversary Emulation Matrix, Red Team Operations — Concepts, MULTI-CLOUD RED TEAM, Red Team MacOS Att&ck, TDC2021 — Mitre Att&ck, etc.). Anchor page for every corpus source that maps techniques to T-numbers.

## Narrative

MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a globally accessible knowledge base of adversary behaviors based on real-world observations, maintained by the MITRE Corporation at [attack.mitre.org](https://attack.mitre.org/). It's used by defenders (blue team) to understand and classify threat actions and by attackers (red team) to plan adversary-emulation exercises that map to known APT TTPs. [Source: Mitre Att&ck Study Overview.pdf]

**Structure — three levels of abstraction:** [CONFIRMED]

- **Tactics** — the *why* of an attack. Goals an adversary tries to achieve: Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command & Control, Exfiltration, Impact. [Source: Red Team Operations – Concepts #1.pdf]
- **Techniques** — the *how*. Specific methods (e.g., under Initial Access: "Spearphishing Attachment" T1566.001). Subtechniques add another layer of specificity.
- **Procedures** — the *what was actually done*. Detailed variants observed in real attacks, often tied to a named APT group.

**Matrices:** Enterprise (Windows/macOS/Linux/cloud/containers/network/SaaS), Mobile (iOS/Android), ICS (industrial control systems). Each matrix has its own tactic + technique tree.

**Adjacent products:** ATT&CK Navigator (web UI for layering coverage), CAR (Cyber Analytics Repository — defender analytics keyed to techniques), STIX/TAXII (structured threat-intel exchange), and the adversary-emulation plans published by MITRE Engenuity's Center for Threat-Informed Defense ([github.com/center-for-threat-informed-defense](https://github.com/center-for-threat-informed-defense)).

**Relation to other frameworks:** ATT&CK is **not** a kill chain — it's an unordered matrix. When ordering matters (e.g., for narrative incident write-ups), defenders typically pair ATT&CK with the Cyber Kill Chain (see @entities/frameworks/cyber-kill-chain.md). The Diamond Model is a complementary intrusion-analysis framework (adversary / capability / infrastructure / victim). [Sources: Mitre Att&ck Study Overview.pdf, Introdução ao Mitre Att&ck e ao Cyber Kill Chain.pdf]

**STIX environment semantics (AutoSUT — 2606.08700):** Public ATT&CK STIX bundles excel at TTP cataloging but leave replay-ready SUT detail underspecified — 97.6% of Enterprise software objects lack version+CPE in structured fields. Emulation consumers must enrich beyond corpus. See @sources/arxiv-2606-08700-autosut-environment-semantics-gap.md.

**LLM CVE→ATT&CK (CAV-STIXGen — 2607.16175):** Open-weight models often hit Match@1 but fail Match@All on multi-technique CVEs; pair auto-mapping with analyst review. See @concepts/llm-cve-to-stix-generation.md.

## Snippets

> Each APT group profile is linked to a set of TTPs that the group is known to use. These are categorized according to the ATT&CK framework, which includes: Tactics (objectives an adversary may try to achieve, such as Initial Access, Execution, Persistence), Techniques (specific methods to achieve those tactical objectives — e.g., Spearphishing Attachment under Initial Access), and Procedures (more detailed or specific variants of techniques, often including information about how a particular group applied that technique in real attacks).
>
> — Red Team Operations — Concepts #1, Joas A Santos [Source: Red Team Operations – Concepts #1.pdf]
