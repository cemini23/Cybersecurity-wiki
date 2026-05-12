#!/usr/bin/env python3
"""Generate entity + concept pages from a curated dict of metadata.

Pages with bodies that synthesize from the Joas A Santos PDF corpus are
written here with real content. Stubs (one-paragraph narratives) are also
emitted for sub-topics that appear in the corpus but don't warrant a long
hand-written page yet — they'll fill in over future ingests.

Run from repo root:
    python3 scripts/build_entity_concept_pages.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

TODAY = "2026-05-12"


def write_page(rel_path: str, title: str, page_type: str, tags: list[str],
               keywords: list[str], related: list[str], maturity: str,
               raw_concept: str, narrative: str, snippets: str = "",
               extra_frontmatter: dict | None = None) -> None:
    out = WIKI / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    tags_str = ", ".join(tags)
    keywords_str = ", ".join(keywords)
    related_block = "\n".join(f"  - {r}" for r in related) if related else "  []"
    relations_inline = "\n".join(f"- @{r}" for r in related) if related else "_(none yet)_"
    extra = ""
    if extra_frontmatter:
        extra = "\n".join(f"{k}: {v}" for k, v in extra_frontmatter.items()) + "\n"
    snippets_block = f"\n## Snippets\n\n{snippets}\n" if snippets else ""
    body = f"""---
title: {title}
type: {page_type}
tags: [{tags_str}]
keywords: [{keywords_str}]
related:
{related_block}
maturity: {maturity}
{extra}created: {TODAY}
updated: {TODAY}
---

## Relations

{relations_inline}

## Raw Concept

{raw_concept}

## Narrative

{narrative}
{snippets_block}"""
    out.write_text(body)


# ---------- people ----------

write_page(
    "entities/people/joas-a-santos.md",
    "Joas A Santos",
    "entity",
    tags=["person", "educator", "researcher"],
    keywords=["joas antonio dos santos", "c0d3cr4zy", "red team leader", "brazilian", "cybersecurity educator"],
    related=[
        "concepts/red-team-operations.md",
        "concepts/adversary-emulation.md",
        "concepts/av-edr-bypass.md",
        "concepts/web-pentest-methodology.md",
        "concepts/osint-for-cybersecurity.md",
        "concepts/cybersecurity-careers.md",
        "concepts/cyber-for-kids.md",
    ],
    maturity="validated",
    raw_concept=(
        "Author of the seed PDF corpus (227 PDFs in the `ebooks Joas` Google Drive folder, "
        "shared publicly). The author's name appears in titles and author lines across the corpus; "
        "this page is the canonical anchor that every source page links back to via `related:`."
    ),
    narrative=(
        "Brazilian cybersecurity educator, Red Team Leader, and prolific content creator. "
        "Self-described in the corpus as: \"Asperger, Red Team Leader, PenTester, Instructor, "
        "Cyber Security Mentor, Hacking is Not a Crime Advocate.\" [Source: AV and EDR Bypass "
        "Techniques for new Hackers - Update 2022.pdf, slide 2]\n\n"
        "Active on LinkedIn ([linkedin.com/in/joas-antonio-dos-santos](https://www.linkedin.com/in/joas-antonio-dos-santos/) — retrieved 2026-05-12) and GitHub "
        "([CyberSecurityUP](https://github.com/CyberSecurityUP)). Material spans offensive security "
        "(red team operations, adversary emulation, AV/EDR bypass, exploit development, web/mobile/cloud "
        "pentest), defensive operations (SOC tooling, incident response, threat hunting), career guidance "
        "(certification cram sheets for OSCP/CRTO/eCPPT/eCPTX/eWPT/CEH/Security+/PenTest+), and a "
        "secondary track on **cyber safety for kids + families** (cyberbullying, school-attack survival, "
        "child-grooming prevention, social-network safety).\n\n"
        "The corpus is bilingual (English + Portuguese) — many sources have parallel PT-BR and EN releases "
        "of the same material. The English versions are typically translations of the Portuguese originals; "
        "when both exist, this wiki treats them as siblings rather than separate sources.\n\n"
        "Distinctive style across the corpus: bullet-heavy slide decks, dense link lists pointing to "
        "primary references (vendor docs, MITRE pages, GitHub repos, conference talks), and a strong "
        "emphasis on **free / low-cost tooling** (multiple \"Low Cost Red Team Tools\" and \"Low Cost SOC "
        "Tools\" volumes). [CONFIRMED]"
    ),
)

# ---------- frameworks ----------

write_page(
    "entities/frameworks/mitre-attack.md",
    "MITRE ATT&CK",
    "entity",
    tags=["framework", "threat-intel", "tactics-techniques-procedures"],
    keywords=["mitre", "att&ck", "attack matrix", "ttps", "tactics", "techniques", "procedures", "navigator"],
    related=[
        "entities/frameworks/cyber-kill-chain.md",
        "concepts/adversary-emulation.md",
        "concepts/red-team-operations.md",
        "concepts/threat-hunting.md",
        "concepts/av-edr-bypass.md",
        "entities/threat-actors/apt28.md",
        "sources/mitre-att-ck-study-overview.md",
        "sources/introdu-o-ao-mitre-att-ck-e-ao-cyber-kill-chain.md",
        "sources/tdc2021-mitre-att-ck.md",
        "sources/red-team-operations-concepts-1.md",
        "sources/adversary-emulation-matrix-by-joas.md",
        "entities/people/joas-a-santos.md",
    ],
    maturity="validated",
    raw_concept=(
        "MITRE ATT&CK is the lingua franca for describing adversary behavior in modern cybersecurity. "
        "Appears in dozens of corpus titles (Mitre Att&ck Study Overview, Adversary Emulation Matrix, "
        "Red Team Operations — Concepts, MULTI-CLOUD RED TEAM, Red Team MacOS Att&ck, TDC2021 — Mitre Att&ck, etc.). "
        "Anchor page for every corpus source that maps techniques to T-numbers."
    ),
    narrative=(
        "MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) is a globally accessible "
        "knowledge base of adversary behaviors based on real-world observations, maintained by the MITRE "
        "Corporation at [attack.mitre.org](https://attack.mitre.org/). It's used by defenders (blue team) "
        "to understand and classify threat actions and by attackers (red team) to plan adversary-emulation "
        "exercises that map to known APT TTPs. [Source: Mitre Att&ck Study Overview.pdf]\n\n"
        "**Structure — three levels of abstraction:** [CONFIRMED]\n\n"
        "- **Tactics** — the *why* of an attack. Goals an adversary tries to achieve: Initial Access, "
        "Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, "
        "Lateral Movement, Collection, Command & Control, Exfiltration, Impact. [Source: Red Team "
        "Operations – Concepts #1.pdf]\n"
        "- **Techniques** — the *how*. Specific methods (e.g., under Initial Access: \"Spearphishing "
        "Attachment\" T1566.001). Subtechniques add another layer of specificity.\n"
        "- **Procedures** — the *what was actually done*. Detailed variants observed in real attacks, "
        "often tied to a named APT group.\n\n"
        "**Matrices:** Enterprise (Windows/macOS/Linux/cloud/containers/network/SaaS), Mobile (iOS/Android), "
        "ICS (industrial control systems). Each matrix has its own tactic + technique tree.\n\n"
        "**Adjacent products:** ATT&CK Navigator (web UI for layering coverage), CAR (Cyber Analytics "
        "Repository — defender analytics keyed to techniques), STIX/TAXII (structured threat-intel "
        "exchange), and the adversary-emulation plans published by MITRE Engenuity's Center for "
        "Threat-Informed Defense ([github.com/center-for-threat-informed-defense](https://github.com/center-for-threat-informed-defense)).\n\n"
        "**Relation to other frameworks:** ATT&CK is **not** a kill chain — it's an unordered matrix. "
        "When ordering matters (e.g., for narrative incident write-ups), defenders typically pair ATT&CK "
        "with the Cyber Kill Chain (see @entities/frameworks/cyber-kill-chain.md). The Diamond Model is "
        "a complementary intrusion-analysis framework (adversary / capability / infrastructure / victim). "
        "[Sources: Mitre Att&ck Study Overview.pdf, Introdução ao Mitre Att&ck e ao Cyber Kill Chain.pdf]"
    ),
    snippets=(
        "> Each APT group profile is linked to a set of TTPs that the group is known to use. These are "
        "categorized according to the ATT&CK framework, which includes: Tactics (objectives an adversary "
        "may try to achieve, such as Initial Access, Execution, Persistence), Techniques (specific methods "
        "to achieve those tactical objectives — e.g., Spearphishing Attachment under Initial Access), and "
        "Procedures (more detailed or specific variants of techniques, often including information about "
        "how a particular group applied that technique in real attacks).\n>\n> — Red Team Operations — Concepts #1, "
        "Joas A Santos [Source: Red Team Operations – Concepts #1.pdf]"
    ),
)

write_page(
    "entities/frameworks/cyber-kill-chain.md",
    "Cyber Kill Chain (Lockheed Martin) + Unified Cyber Kill Chain",
    "entity",
    tags=["framework", "intrusion-modelling", "ordered-phases"],
    keywords=["lockheed martin", "kill chain", "unified kill chain", "phases", "ordered"],
    related=[
        "entities/frameworks/mitre-attack.md",
        "concepts/red-team-operations.md",
        "concepts/adversary-emulation.md",
        "concepts/incident-response.md",
        "sources/introdu-o-ao-mitre-att-ck-e-ao-cyber-kill-chain.md",
        "sources/red-team-operations-concepts-1.md",
        "entities/people/joas-a-santos.md",
    ],
    maturity="validated",
    raw_concept=(
        "Companion framework to MITRE ATT&CK. Mentioned across the corpus when ordering matters in "
        "engagement / incident narratives. The Joas corpus uses the Unified Cyber Kill Chain (Paul Pols, "
        "2017), a 18-phase superset of the original Lockheed Martin chain plus elements of ATT&CK."
    ),
    narrative=(
        "Originally proposed by Lockheed Martin (Hutchins, Cloppert, Amin, 2011) as a 7-phase ordered "
        "model of network intrusion: Reconnaissance → Weaponization → Delivery → Exploitation → "
        "Installation → Command & Control → Actions on Objectives. The model's strength is its "
        "**ordered** nature — useful for narrating incidents — but it was criticized as too coarse for "
        "modern intrusions that loop through phases multiple times. [CONFIRMED]\n\n"
        "**Unified Cyber Kill Chain** (Paul Pols, 2017) extends Lockheed's chain into 18 ordered phases "
        "and explicitly maps each phase to MITRE ATT&CK tactics: [Source: Red Team Operations – Concepts #1.pdf]\n\n"
        "1. **Reconnaissance** — passive + active target identification\n"
        "2. **Weaponization** — preparing attack infrastructure\n"
        "3. **Delivery** — transmitting weaponized payload to target\n"
        "4. **Social Engineering** — manipulating people into unsafe actions\n"
        "5. **Exploitation** — vulnerability exploitation → code execution\n"
        "6. **Persistence** — establishing durable footholds\n"
        "7. **Defense Evasion** — avoiding detection (AV/EDR, monitoring)\n"
        "8. **Command & Control (C2)** — communicating with compromised hosts\n"
        "9. **Pivoting** — tunneling traffic through controlled hosts\n"
        "10. **Discovery** — local + network enumeration\n"
        "11. **Privilege Escalation** — gaining higher permissions\n"
        "12. **Execution** — running attacker-controlled code\n"
        "13. **Credential Access** — harvesting credentials\n"
        "14. **Lateral Movement** — moving horizontally across systems\n"
        "15. **Harvesting** — gathering target data prior to exfiltration\n"
        "16. **Exfiltration** — removing data from the target network\n"
        "17. **Impact** — manipulating, disrupting, or destroying systems/data\n"
        "18. **Objectives** — sociotechnical end-goals of the operation\n\n"
        "**ATT&CK vs Kill Chain — when to use which:** Use ATT&CK when the question is \"what technique "
        "could be used here?\" (technique-first). Use Kill Chain when the question is \"how did this "
        "intrusion unfold?\" (story-first). For red team reporting both are typically used together — "
        "phases give narrative structure, ATT&CK T-numbers give granular accountability."
    ),
)

# ---------- threat actors ----------

write_page(
    "entities/threat-actors/apt28.md",
    "APT28 (Fancy Bear / Sofacy)",
    "entity",
    tags=["threat-actor", "apt", "nation-state", "russia-attributed"],
    keywords=["apt28", "fancy bear", "sofacy", "strontium", "pawn storm", "gru", "russia"],
    related=[
        "entities/frameworks/mitre-attack.md",
        "concepts/adversary-emulation.md",
        "concepts/cyberwarfare.md",
        "sources/apt28-understanding-a-group-specialized-in-attacks-against-intelligence-sectors.md",
        "entities/people/joas-a-santos.md",
    ],
    maturity="draft",
    raw_concept=(
        "Sole named APT group in the corpus (APT28 — Understanding a group specialized in attacks against "
        "intelligence sectors.pdf). Stub upgraded with public threat-intel context; deeper expansion will "
        "come from the corpus PDF on next deep-read pass."
    ),
    narrative=(
        "APT28 — aliases Fancy Bear, Sofacy, Strontium, Pawn Storm, Sednit — is a Russian state-sponsored "
        "advanced persistent threat group widely attributed to the GRU (Russian military intelligence, "
        "Unit 26165) by Western government agencies and threat-intel vendors (CrowdStrike, Mandiant, "
        "Microsoft Threat Intelligence, US-CERT). [NEEDS VERIFICATION 2026-05-12]\n\n"
        "**Notable operations** (public attribution):\n"
        "- DNC + DCCC intrusions, 2016 US election interference\n"
        "- TV5Monde attack, 2015\n"
        "- German Bundestag intrusion, 2015\n"
        "- WADA / IAAF (anti-doping) intrusions, 2016\n"
        "- Long-running campaigns against NATO members, defense contractors, foreign ministries\n\n"
        "**TTPs (high-level, MITRE-keyed):** spear-phishing with credential-harvesting + zero-day "
        "exploits; custom malware families (X-Agent, X-Tunnel, Komplex, Zebrocy, Cannon, LoJax UEFI "
        "implant); use of 0day exploits when justified; aggressive operational tempo. MITRE ATT&CK "
        "[group page G0007](https://attack.mitre.org/groups/G0007/) is the canonical mapping. "
        "[Sources: attack.mitre.org/groups/G0007/, APT28 - Understanding a group specialized in attacks "
        "against intelligence sectors.pdf]\n\n"
        "**Adversary emulation:** the MITRE Engenuity Center for Threat-Informed Defense and various "
        "red-team teams (SCYTHE, AttackIQ) publish APT28 emulation plans. These are good starting points "
        "for Purple Team exercises (see @concepts/purple-team-operations.md)."
    ),
)

# ---------- tools ----------

TOOLS = [
    ("cobalt-strike.md", "Cobalt Strike",
        ["c2", "post-exploitation", "commercial", "red-team-standard"],
        ["cobalt strike", "beacon", "fortra", "c2 framework", "red team commercial tooling"],
        ["concepts/red-team-operations.md", "concepts/adversary-emulation.md", "concepts/av-edr-bypass.md",
         "sources/adversary-emulation-com-cobalt-strike.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Single most-cited commercial C2 in the corpus (Adversary Emulation com Cobalt Strike.pdf). "
        "Stub anchored to the corpus PDF; expand on next ingest pass.",
        ("Commercial command-and-control (C2) framework from Fortra (formerly Strategic Cyber LLC), "
         "originally written by Raphael Mudge. The de-facto standard for professional red team operations. "
         "[CONFIRMED]\n\n"
         "**Architecture:** Team server (Java) + client GUI + Beacon implants. Beacon is the workhorse — "
         "supports HTTP/HTTPS/DNS/SMB-pipe communication, sleep + jitter for stealth, malleable C2 "
         "profiles for traffic shaping, and Aggressor Script for automation.\n\n"
         "**Dual-use reality:** Cobalt Strike is licensed legitimately for red team consultancies but is "
         "**also one of the most-abused tools in criminal intrusions** — cracked Beacon builds are common "
         "in ransomware operator toolchains. As a result, vendor detections (CrowdStrike, Defender for "
         "Endpoint, etc.) signature heavily on default Beacon profiles. Operational red teams use "
         "malleable C2 profiles, [CobaltBus](https://github.com/Mr-Un1k0d3r/CobaltBus)-style transport "
         "switching, and process injection / sleep-mask techniques to stay ahead of signatures. See "
         "@concepts/av-edr-bypass.md for the broader evasion playbook."),
     ),
    ("metasploit.md", "Metasploit Framework",
        ["exploitation", "framework", "foss", "rapid7"],
        ["metasploit", "msf", "msfvenom", "meterpreter", "rapid7", "h.d. moore"],
        ["concepts/exploit-development.md", "concepts/red-team-operations.md", "concepts/av-edr-bypass.md",
         "sources/ebook-invadindo-com-metasploit-vl-1.md", "sources/pentest-with-metasploit-overview.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Cited across the corpus as the standard FOSS exploitation framework. Stub anchored to two "
        "corpus PDFs (ebook Invadindo com Metasploit VL 1 + Pentest with metasploit - overview).",
        ("Open-source exploitation framework maintained by Rapid7, originally created by H.D. Moore in "
         "2003. The default toolbox for opportunistic exploitation and post-exploitation. [CONFIRMED]\n\n"
         "**Core components:**\n"
         "- **msfconsole** — interactive console for selecting/configuring/running modules\n"
         "- **msfvenom** — payload generator (encoders, formats, templates). Cited in the corpus for "
         "AV-bypass workflows where stock payloads get signatured immediately\n"
         "- **Meterpreter** — interactive payload supporting in-memory operation, port forwarding, hash "
         "dumping, screenshot/keylogger, etc.\n\n"
         "**Module taxonomy:** exploit / auxiliary / post / encoder / nop / payload / evasion / "
         "post-exploitation. ~2000+ exploit modules; auxiliary scanners cover most enumeration tasks.\n\n"
         "**Where it falls short for modern engagements:** default Meterpreter/msfvenom payloads are "
         "signatured by every vendor. For red team / adversary-emulation work, Metasploit is most useful "
         "for *initial access* + lab scenarios — operators typically shift to Cobalt Strike, Sliver, or "
         "Mythic for the C2 / post-exploitation phase. See @entities/tools/cobalt-strike.md."),
     ),
    ("burp-suite.md", "Burp Suite",
        ["web-pentest", "proxy", "portswigger", "commercial-plus-free"],
        ["burp", "portswigger", "intercepting proxy", "repeater", "intruder", "scanner", "extender"],
        ["concepts/web-pentest-methodology.md", "concepts/bug-bounty.md",
         "sources/burp-suite-plugin-development.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Standard tool for web-app testing across the corpus. Anchored by Burp Suite Plugin Development.pdf.",
        ("PortSwigger's intercepting web proxy + integrated web-app testing toolkit. The de-facto standard "
         "across both pentest and bug-bounty workflows. [CONFIRMED]\n\n"
         "**Editions:** Community (free, limited Scanner), Professional ($449/yr, full Scanner + "
         "Intruder rate-unlimited), Enterprise (CI/CD-integrated DAST).\n\n"
         "**Key panes:** Proxy (intercept + history), Repeater (manual single-request iteration), Intruder "
         "(automated payload fuzzing — 4 attack types: sniper, battering ram, pitchfork, cluster bomb), "
         "Scanner (Pro-only DAST), Decoder, Comparer, Sequencer (session-token entropy analysis), "
         "Extender (BApp store + custom extensions in Java/Python/Ruby).\n\n"
         "**Notable extensions** (BApp store): Logger++, Autorize, JWT Editor, Param Miner, Turbo "
         "Intruder, AuthMatrix, Hackvertor, Bypass WAF, ActiveScan++. The corpus's *Burp Suite Plugin "
         "Development.pdf* covers building your own. See @concepts/web-pentest-methodology.md for the "
         "full web-pentest workflow this tool slots into."),
     ),
    ("caldera.md", "MITRE Caldera",
        ["adversary-emulation", "automation", "foss", "mitre"],
        ["caldera", "mitre", "adversary emulation", "automated", "atomic red team"],
        ["concepts/adversary-emulation.md", "concepts/purple-team-operations.md",
         "entities/frameworks/mitre-attack.md",
         "sources/adversary-simulation-with-caldera-and-mitre.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by Adversary Simulation with Caldera and Mitre.pdf.",
        ("MITRE's open-source adversary-emulation platform — automates the execution of "
         "ATT&CK-mapped TTPs against test environments. [CONFIRMED]\n\n"
         "**Architecture:** server (Python) + agents (sandcat — Go, manx — TCP/HTTP, ragdoll — Python). "
         "Operators define **adversary profiles** (ordered lists of abilities, each ability tied to one "
         "or more MITRE techniques), then run **operations** that execute those abilities against agents.\n\n"
         "**Distinguishing features vs Atomic Red Team:** Caldera is fully automated (it picks the next "
         "ability based on planner logic — atomic / batch / look-ahead); Atomic Red Team is a library of "
         "atomic tests you run manually. Caldera is better for unattended purple-team exercises; Atomic "
         "is better for focused detection-engineering work. See @concepts/purple-team-operations.md."),
     ),
    ("maltego.md", "Maltego",
        ["osint", "graph-analysis", "investigation"],
        ["maltego", "transforms", "osint", "link analysis", "paterva"],
        ["concepts/osint-for-cybersecurity.md",
         "sources/maltego-introduction-creating-a-simple-local-transform-en.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by two parallel corpus PDFs (EN + PT-BR) on Maltego local-transform development.",
        ("Graph-based OSINT + link-analysis tool from Maltego Technologies (formerly Paterva). The "
         "canonical tool for *investigation* — visualizing relationships between people, organizations, "
         "domains, IPs, social-media accounts, file hashes, leaked credentials, and more. [CONFIRMED]\n\n"
         "**Architecture:** entities (typed nodes) + transforms (functions that take an entity and return "
         "related entities). Transforms can be local (Python code on your machine) or hub-based (run on a "
         "vendor server, often paid).\n\n"
         "**Editions:** Community Edition (free, capped at 12 results per transform), Professional, "
         "Classic, XL. Cross-link: @osint-wiki/entities/tools/swarmvault.md and broader OSINT tradecraft "
         "lives in the sister wiki."),
     ),
    ("wazuh.md", "Wazuh",
        ["soc", "siem", "host-ids", "foss"],
        ["wazuh", "siem", "soc", "ossec fork", "elastic", "rule management"],
        ["concepts/soc-operations.md", "concepts/incident-response.md", "concepts/purple-team-operations.md",
         "sources/purple-team-lab-01-wazuh-and-win2016.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by Purple Team Lab 01 — Wazuh and Win2016.pdf — the corpus's hands-on lab.",
        ("Open-source security-monitoring platform — host-based IDS + log management + vulnerability "
         "assessment + cloud-workload protection in one stack. A fork of OSSEC, since rewritten with a "
         "modern API, Elastic-based dashboard, and an active vendor offering managed support. [CONFIRMED]\n\n"
         "**Architecture:** Wazuh agent (lightweight, on every endpoint) → Wazuh manager (aggregates, "
         "applies rules) → Wazuh indexer (formerly Open Distro Elasticsearch / OpenSearch) → Wazuh "
         "dashboard. Cited in the corpus as the centerpiece of a **low-cost SOC** stack (see also "
         "@concepts/soc-operations.md and the corpus's *Low Cost SOC Tools* PDFs)."),
     ),
    ("nmap.md", "Nmap + Nmap Scripting Engine",
        ["recon", "network-scanner", "foss", "industry-standard"],
        ["nmap", "nse", "scanning", "port scan", "service detection"],
        ["concepts/network-security.md", "concepts/web-pentest-methodology.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Cited implicitly across the pentest corpus. Stub for completeness.",
        ("De-facto network discovery + port-scanning tool. Default for the recon phase of every "
         "engagement. Notable subsystems: NSE (Nmap Scripting Engine, ~600+ Lua scripts for vuln-detection "
         "and service-specific enumeration), Ndiff (diffing two scans), Nping (packet crafting). "
         "[CONFIRMED]\n\n"
         "Standard recon-phase combinations: `-sV -sC -p- -T4` (all ports + service detection + default "
         "scripts), `--script vuln` (vulnerability NSE bundle), `-O` (OS fingerprinting). Output formats "
         "(`-oN/-oX/-oG/-oA`) feed cleanly into other tools like sqlmap, gobuster, BloodHound."),
     ),
    ("bloodhound.md", "BloodHound",
        ["ad-recon", "graph-analysis", "foss"],
        ["bloodhound", "active directory", "sharphound", "neo4j", "kingdom kerberos", "specter ops"],
        ["concepts/windows-pentest.md", "concepts/red-team-operations.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Implicit across Active Directory pentest sources. Stub for AD-attack-path enumeration.",
        ("AD relationship-mapping tool from SpecterOps — uses graph theory (Neo4j) to surface attack "
         "paths within Active Directory. Indispensable for Windows enterprise pentest + red team. "
         "[CONFIRMED]\n\n"
         "**Collector:** SharpHound (C# binary, or PowerShell equivalents) — enumerates AD users, groups, "
         "computers, sessions, ACLs. **Analyzer:** BloodHound (Electron app) loads the JSON output into "
         "Neo4j and presents pre-built Cypher queries like \"Shortest path to Domain Admins from owned "
         "user.\" Newer release: **BloodHound CE** (containerized, web UI) and **BloodHound Enterprise** "
         "(commercial, continuous monitoring). See @concepts/windows-pentest.md."),
     ),
]

for filename, title, tags, keywords, related, maturity, raw_concept, narrative in TOOLS:
    write_page(
        f"entities/tools/{filename}",
        title,
        "entity",
        tags=tags,
        keywords=keywords,
        related=related,
        maturity=maturity,
        raw_concept=raw_concept,
        narrative=narrative,
    )

# ---------- certifications ----------

CERTS = [
    ("oscp.md", "OSCP (Offensive Security Certified Professional)",
        ["entry-level", "hands-on", "offensive-security", "industry-standard"],
        ["oscp", "pen-200", "try harder", "offensive security", "24-hour exam"],
        ["entities/vendors/offensive-security.md", "concepts/web-pentest-methodology.md",
         "concepts/windows-pentest.md", "concepts/privilege-escalation.md",
         "sources/oscp-labs-to-practice-2023.md", "sources/oscp-like-vulns-machines.md",
         "entities/platforms/hackthebox.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Two corpus PDFs directly anchored: OSCP LABS TO PRACTICE 2023 + OSCP Like Vulns Machines.",
        ("Offensive Security's flagship entry-level offensive certification — paired with the PEN-200 "
         "course. The industry's most widely recognized hands-on pentest credential. [CONFIRMED]\n\n"
         "**Exam format:** 24-hour proctored hands-on lab → 24-hour reporting window. 5 machines "
         "(Standalone + Active Directory set worth 40 pts as of 2023 revamp). Passing threshold: 70/100.\n\n"
         "**Common prep loop:** PEN-200 course material → official OSCP labs → HackTheBox + VulnHub "
         "boxes matched to the official \"OSCP-like\" lists (TJ Null's list is the community standard, "
         "referenced explicitly by *OSCP Like Vulns Machines.pdf* in the corpus). Reporting practice is "
         "as important as exploitation: many exam failures are clean technical wins lost to incomplete "
         "reports. See @entities/platforms/hackthebox.md and @concepts/web-pentest-methodology.md."),
     ),
    ("crto.md", "CRTO (Certified Red Team Operator)",
        ["mid-level", "red-team", "zeropoint-security"],
        ["crto", "rto i", "rto ii", "zero-point security", "rastamouse", "cobalt strike"],
        ["entities/vendors/zeropoint-security.md", "concepts/red-team-operations.md",
         "concepts/adversary-emulation.md", "entities/tools/cobalt-strike.md",
         "sources/crto-notes-to-exam-preparation.md",
         "sources/certified-red-team-leader-rto-ii-overview-to-study.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Corpus has *CRTO — Notes to Exam Preparation* + *Certified Red Team Leader (RTO II) — Overview to Study* directly anchoring this entity.",
        ("Zero-Point Security's Red Team Operator certification (Daniel Duggan / Rastamouse). "
         "The default pivot certification for pentesters moving into red team work. RTO II "
         "(\"Certified Red Team Leader\") is the advanced follow-on. [CONFIRMED]\n\n"
         "**Exam format:** 4-day take-home with full lab access. Heavy on **Cobalt Strike** operation, "
         "Active Directory abuse, evasion tradecraft, and OPSEC. Less time-pressured than OSCP but the "
         "lab is larger and the techniques are more current.\n\n"
         "**Why it's well-regarded:** course content tracks closely with what working red teams actually "
         "do — malleable C2 profiles, AV/EDR-aware payload generation, AD attack paths, KRBTGT abuse. "
         "Pairs naturally with the *AV/EDR Bypass* + *Adversary Emulation* concept pages."),
     ),
    ("ceh.md", "CEH (Certified Ethical Hacker)",
        ["entry-level", "vendor-neutral", "ec-council"],
        ["ceh", "ec-council", "certified ethical hacker"],
        ["entities/vendors/ec-council.md", "concepts/cybersecurity-careers.md",
         "sources/ceh-fundamentals.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by CEH Fundamentals.pdf.",
        ("EC-Council's flagship offensive certification — historically the most recognized cert "
         "name in the cybersecurity job market, especially in compliance-driven hiring (defense, "
         "government, regulated industries). [CONFIRMED]\n\n"
         "**Format:** 125 multiple-choice questions, 4 hours. Optional CEH Practical adds a 6-hour "
         "hands-on lab.\n\n"
         "**Community view:** the credential's name recognition is strong, but the multiple-choice "
         "format means it doesn't validate hands-on capability the way OSCP/CRTO do. Common career "
         "pattern in the corpus: CEH first for HR keyword-match → OSCP for technical credibility. See "
         "@concepts/cybersecurity-careers.md."),
     ),
    ("comptia-security-plus.md", "CompTIA Security+",
        ["entry-level", "vendor-neutral", "foundational"],
        ["comptia", "security plus", "sy0-601", "sy0-701"],
        ["entities/vendors/comptia.md", "concepts/cybersecurity-careers.md",
         "sources/comptia-security-tips-and-tricks.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by CompTIA Security+ — Tips and Tricks.pdf.",
        ("Foundational vendor-neutral certification. Often the first cert recommended for cybersecurity "
         "career entrants. [CONFIRMED]\n\n"
         "**Format:** ~90 questions (MC + performance-based), 90 minutes. Current exam code SY0-701 "
         "(launched 2023). Validity: 3 years; renewable via continuing education.\n\n"
         "**Where it fits:** broad cybersecurity vocabulary — controls, risk management, cryptography, "
         "incident response basics, governance. Doesn't validate hands-on offensive or defensive skill; "
         "instead serves as a common baseline for Tier-1 SOC analyst roles and a stepping stone toward "
         "PenTest+ / CySA+ / OSCP. Required by DoD 8570 for many US government positions."),
     ),
    ("comptia-pentest-plus.md", "CompTIA PenTest+",
        ["entry-mid", "vendor-neutral", "pentest"],
        ["pentest+", "comptia", "pt0-002"],
        ["entities/vendors/comptia.md", "concepts/cybersecurity-careers.md",
         "sources/comptia-pentest-tips-and-tricks.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by CompTIA PenTest+ — Tips and Tricks.pdf.",
        ("CompTIA's hands-on pentest certification (current exam code PT0-002). Sits between Security+ "
         "and OSCP. [CONFIRMED]\n\n"
         "**Format:** ~85 questions, 165 minutes. Mix of multiple-choice and performance-based "
         "(scenario simulations). DoD 8570-approved. Less hands-on than OSCP but covers the *process* "
         "of an engagement — planning, scoping, reporting — more thoroughly. Good middle-ground for "
         "career switchers who need both vocabulary and methodology before OSCP."),
     ),
    ("ecppt.md", "eCPPT (eLearnSecurity Certified Professional Penetration Tester)",
        ["mid-level", "hands-on", "elearnsecurity"],
        ["ecppt", "elearnsecurity", "ine", "ptp"],
        ["entities/vendors/elearnsecurity.md", "concepts/red-team-operations.md",
         "sources/elearnsecurity-ecppt-notes-exam.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by eLearnSecurity eCPPT Notes Exam.pdf.",
        ("eLearnSecurity / INE's mid-level hands-on pentest cert. Paired with the PTP "
         "(Penetration Testing Professional) course. [CONFIRMED]\n\n"
         "**Format:** 7-day lab + 7-day reporting window. Less time-pressured than OSCP, but the "
         "report is weighted heavily and must be professional-grade. Strong on Active Directory + "
         "buffer overflow content. Sister cert: eCPTX (advanced)."),
     ),
    ("ecptx.md", "eCPTX (eLearnSecurity Certified Penetration Tester eXtreme)",
        ["advanced", "hands-on", "elearnsecurity"],
        ["ecptx", "elearnsecurity", "ine", "ptx"],
        ["entities/vendors/elearnsecurity.md", "concepts/red-team-operations.md",
         "concepts/av-edr-bypass.md", "concepts/windows-pentest.md",
         "sources/elearnsecurity-ecptxv2-notes.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by eLearnSecurity eCPTXv2 Notes.pdf.",
        ("eLearnSecurity / INE's advanced pentest cert — focused on Active Directory abuse, "
         "AV/EDR evasion, custom exploit development, post-exploitation tradecraft. [CONFIRMED]\n\n"
         "**Format:** 14-day take-home lab — emulates a real engagement. Reporting is the "
         "centerpiece — examiners weight quality of writeup heavily. Strong overlap with the "
         "CRTO scope but more focused on individual technique depth than red-team-operations "
         "doctrine. See @concepts/av-edr-bypass.md and @concepts/windows-pentest.md."),
     ),
    ("ewpt.md", "eWPT / eWPTX (eLearnSecurity Web App Pentest)",
        ["mid-level", "web-app", "elearnsecurity"],
        ["ewpt", "ewptx", "elearnsecurity", "wapt"],
        ["entities/vendors/elearnsecurity.md", "concepts/web-pentest-methodology.md",
         "concepts/bug-bounty.md", "sources/elearnsecurity-ewpt-notes.md",
         "sources/elearnsecurity-ewptx-notes-basic-by-joas.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Two corpus PDFs anchor this: eLearnSecurity eWPT Notes + eWPTX Notes Basic by Joas.",
        ("eLearnSecurity's web-app pentest cert. eWPT = mid-level (paired with the WAPT course); "
         "eWPTX = advanced (paired with WAPTX). [CONFIRMED]\n\n"
         "**Format:** 7-day lab + 7-day report (eWPT); 14-day lab + 7-day report (eWPTX). Strong "
         "coverage of OWASP Top 10 + advanced web techniques (XXE, SSRF, deserialization, NoSQL "
         "injection, SAML attacks). Closest equivalent: OffSec's OSWA / OSWE."),
     ),
    ("oswe.md", "OSWE (Offensive Security Web Expert)",
        ["advanced", "web-app", "offensive-security"],
        ["oswe", "awae", "offensive security", "white-box"],
        ["entities/vendors/offensive-security.md", "concepts/web-pentest-methodology.md",
         "concepts/bug-bounty.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Implicit across OffSec / web pentest corpus; cite as community-standard for white-box "
        "code review.",
        ("Offensive Security's web-app exploitation certification (paired with the AWAE / WEB-300 "
         "course). White-box focus — source-code review + custom exploit development. [CONFIRMED]\n\n"
         "**Format:** 48-hour proctored exam — 2 vulnerable web apps, expected to find + exploit + "
         "write exploit code from scratch. Distinguishes itself from eWPTX by heavily emphasizing "
         "code-review skills (PHP, Java, .NET, Node.js, Python source bases)."),
     ),
    ("oswa.md", "OSWA (Offensive Security Web Assessor)",
        ["mid-level", "web-app", "offensive-security"],
        ["oswa", "web-200", "offensive security"],
        ["entities/vendors/offensive-security.md", "concepts/web-pentest-methodology.md",
         "sources/oswa-offensive-security-web-attacks-study-overview-pt-1.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by OSWA Study Overview PT.1.pdf.",
        ("Offensive Security's web-app *assessment* cert (paired with WEB-200). Black-box focus — "
         "complementary to OSWE's white-box. Launched 2022. [CONFIRMED]\n\n"
         "**Format:** 24-hour proctored exam — black-box web exploitation across multiple targets. "
         "Bridges the gap between OSCP-level web content (single OWASP-style boxes) and OSWE-level "
         "custom-exploit work."),
     ),
]

for filename, title, tags, keywords, related, maturity, raw_concept, narrative in CERTS:
    write_page(
        f"entities/certifications/{filename}",
        title,
        "entity",
        tags=tags,
        keywords=keywords,
        related=related,
        maturity=maturity,
        raw_concept=raw_concept,
        narrative=narrative,
    )

# ---------- vendors ----------

VENDORS = [
    ("offensive-security.md", "Offensive Security (OffSec)",
        ["vendor", "training", "certifications"],
        ["offensive security", "offsec", "oscp", "kali linux"],
        ["entities/certifications/oscp.md", "entities/certifications/oswe.md",
         "entities/certifications/oswa.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Sponsor of OSCP / OSWE / OSWA / OSED / OSEP / OSDA / OSWP / OSEE — cited across the corpus.",
        ("Cybersecurity training + certification vendor founded 2007 by Mati Aharoni (muts). Steward "
         "of Kali Linux. Operates the OSCP, OSWE, OSWA, OSED, OSEP, OSDA, OSWP, OSEE certifications "
         "and the proving-grounds lab platform. [CONFIRMED]\n\n"
         "**Culture:** \"Try Harder\" mantra; minimal hand-holding; courses are written-text-heavy. "
         "Lab learning is the centerpiece — videos exist but the labs do the teaching."),
     ),
    ("elearnsecurity.md", "eLearnSecurity / INE Security",
        ["vendor", "training", "certifications"],
        ["elearnsecurity", "ine", "ine security", "ptp", "ptx", "wapt"],
        ["entities/certifications/ecppt.md", "entities/certifications/ecptx.md",
         "entities/certifications/ewpt.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Eight corpus PDFs reference eLearnSecurity certifications (eCPPT, eCPTXv2, eWPT, eWPTX, eCXD, eCIR, Mobile, ExploitDev).",
        ("Italian-founded cybersecurity training vendor (acquired by INE in 2020, now operates as INE "
         "Security). Offers a deep certification ladder — eJPT (entry) → eCPPT (mid) → eCPTX (advanced) "
         "for pentest; eWPT → eWPTX for web app; eMAPT for mobile; eCDFP / eCIR for DFIR / IR. "
         "[CONFIRMED]\n\n"
         "**Position vs OffSec:** more permissive lab access, longer take-home format, heavier emphasis "
         "on **reporting quality**. Often paired with OSCP in career paths (eCPPT first for foundation, "
         "OSCP second for credential weight)."),
     ),
    ("comptia.md", "CompTIA",
        ["vendor", "certifications", "vendor-neutral"],
        ["comptia", "security+", "pentest+", "cysa+", "casp+"],
        ["entities/certifications/comptia-security-plus.md", "entities/certifications/comptia-pentest-plus.md",
         "concepts/cybersecurity-careers.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Cited via Security+ + PenTest+ corpus PDFs.",
        ("US-based non-profit IT certification body. Vendor-neutral certs span IT generalist (A+ / "
         "Network+) → security (Security+ / PenTest+ / CySA+ / CASP+). Many CompTIA certs are "
         "DoD 8570 approved, driving heavy adoption in US federal + defense hiring. [CONFIRMED]"),
     ),
    ("ec-council.md", "EC-Council",
        ["vendor", "certifications"],
        ["ec-council", "ceh", "chfi", "ecsa"],
        ["entities/certifications/ceh.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Cited via CEH corpus content.",
        ("EC-Council (International Council of E-Commerce Consultants) operates the **CEH** "
         "(Certified Ethical Hacker), CHFI (computer forensics), ECSA (security analyst), and "
         "LPT (licensed pentester) certs. The CEH credential has high name recognition in HR + "
         "compliance hiring; community opinion varies on technical depth vs OSCP/OSWE. [CONFIRMED]"),
     ),
    ("zeropoint-security.md", "Zero-Point Security",
        ["vendor", "training", "red-team"],
        ["zero-point", "rastamouse", "crto", "rto"],
        ["entities/certifications/crto.md", "concepts/red-team-operations.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Sponsor of CRTO / RTO II — directly cited in two corpus PDFs.",
        ("UK-based red-team training vendor founded by Daniel Duggan (Rastamouse). Operates "
         "RTO (Red Team Operator) and RTO II (Certified Red Team Leader) certifications. "
         "[CONFIRMED]\n\n"
         "**Why it's well-regarded:** the courseware updates frequently (Cobalt Strike + AD tradecraft "
         "rotate as defenders evolve), and the lab is large enough to feel like a real engagement. "
         "See @entities/certifications/crto.md."),
     ),
]

for filename, title, tags, keywords, related, maturity, raw_concept, narrative in VENDORS:
    write_page(
        f"entities/vendors/{filename}",
        title,
        "entity",
        tags=tags,
        keywords=keywords,
        related=related,
        maturity=maturity,
        raw_concept=raw_concept,
        narrative=narrative,
    )

# ---------- platforms ----------

write_page(
    "entities/platforms/hackthebox.md",
    "HackTheBox (HTB)",
    "entity",
    tags=["lab-platform", "ctf", "training"],
    keywords=["hackthebox", "htb", "boxes", "pwnbox", "academy"],
    related=[
        "entities/certifications/oscp.md",
        "concepts/web-pentest-methodology.md",
        "concepts/windows-pentest.md",
        "sources/hackthebox-e-vulnhub-dicas-e-truques.md",
        "sources/red-team-and-blue-team-labs-and-ctf.md",
        "entities/people/joas-a-santos.md",
    ],
    maturity="draft",
    raw_concept="Corpus has Hackthebox e Vulnhub - Dicas e Truques.pdf and Red Team and Blue Team Labs and CTF.pdf anchoring this platform.",
    narrative=(
        "Online CTF + lab platform. Industry standard for hands-on pentest practice. [CONFIRMED]\n\n"
        "**Surfaces:**\n"
        "- **Machines** — individual hosts, retired weekly. Difficulty: Easy / Medium / Hard / Insane.\n"
        "- **Pro Labs** — multi-host enterprise environments. Dante / Offshore / RastaLabs / Cybernetics. "
        "Closest sim to a real engagement; expensive but worth it for AD + lateral-movement practice.\n"
        "- **HTB Academy** — structured paid courses + CPTS / CBBH / CWEE certifications, increasingly "
        "competitive with OffSec / eLearnSecurity offerings.\n"
        "- **Sherlocks** — defensive scenarios (forensics, IR).\n\n"
        "**OSCP prep:** the community-maintained TJ Null list of *OSCP-like* boxes is the standard "
        "warmup. The corpus's *OSCP Like Vulns Machines.pdf* extends + curates this list. See "
        "@entities/certifications/oscp.md."
    ),
)

# ---------- programming languages ----------

LANGS = [
    ("python.md", "Python (security-focused)",
        ["scripting", "automation", "tooling"],
        ["python", "scapy", "impacket", "pwntools"],
        ["concepts/exploit-development.md", "concepts/osint-for-cybersecurity.md",
         "sources/python-for-hackers-bootcamp.md", "sources/python-for-hackers-pt-1.md",
         "sources/python-libs-for-security-pt-1.md", "entities/people/joas-a-santos.md"],
        "draft",
        "Three corpus PDFs anchor this (Python for Hackers Bootcamp, PYTHON FOR HACKERS PT 1, Python Libs for Security PT.1).",
        ("De-facto scripting language for cybersecurity work. Used across nearly every offensive + "
         "defensive workflow. [CONFIRMED]\n\n"
         "**Notable security libraries (Joas corpus + community standard):**\n"
         "- **Scapy** — packet crafting, sniffing, dissection\n"
         "- **Impacket** — Windows protocols (SMB, MS-RPC, Kerberos) → smbexec, secretsdump, "
         "GetUserSPNs, ntlmrelayx\n"
         "- **pwntools** — CTF + exploit-development helpers\n"
         "- **requests** — HTTP — the foundation of web-pentest scripting\n"
         "- **paramiko** — SSH automation\n"
         "- **PyCryptodome / cryptography** — crypto primitives\n"
         "- **frida / pyfrida** — runtime instrumentation (mobile + Windows)"),
     ),
    ("c.md", "C / C++ (security-focused)",
        ["systems", "exploit-dev", "low-level"],
        ["c", "c++", "buffer overflow", "shellcode", "windows api"],
        ["concepts/exploit-development.md", "concepts/av-edr-bypass.md",
         "sources/c-for-hackers-overview-pt.md",
         "sources/programa-o-c-e-c-para-seguran-a-ofensiva-digital.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Two corpus PDFs anchor (C for Hackers - Overview PT + Programação C e C++ para Segurança Ofensiva).",
        ("Foundational for buffer overflow + exploit development + AV/EDR bypass tradecraft + "
         "shellcode + Windows API manipulation. [CONFIRMED]\n\n"
         "**Why it's central:** every modern OS kernel is C; the Windows API is C-callable; most "
         "EDR-evasion techniques (process injection, syscall stubs, indirect-syscall jump tables, DLL "
         "unhooking) ship as C/C++ proof-of-concept code. See @concepts/exploit-development.md and "
         "@concepts/av-edr-bypass.md."),
     ),
    ("javascript.md", "JavaScript (security-focused)",
        ["web", "client-side", "node"],
        ["javascript", "js", "xss", "prototype pollution", "node.js"],
        ["concepts/web-pentest-methodology.md", "concepts/bug-bounty.md",
         "sources/javascript-for-hackers.md", "sources/javascript-for-hackers-2.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by JavaScript for Hackers + JavaScript for Hackers 2.pdf.",
        ("Required for serious web-app testing — XSS payload crafting, DOM-based vulnerability "
         "analysis, prototype pollution, postMessage abuse, JWT manipulation, source-code review of "
         "Node.js backends. [CONFIRMED]"),
     ),
    ("powershell.md", "PowerShell (security-focused)",
        ["windows", "post-exploitation", "scripting"],
        ["powershell", "empire", "powerview", "amsi", "constrained language mode"],
        ["concepts/windows-pentest.md", "concepts/av-edr-bypass.md",
         "concepts/red-team-operations.md",
         "sources/pentest-com-powershell-overview.md",
         "entities/people/joas-a-santos.md"],
        "draft",
        "Anchored by Pentest com POWERSHELL - overview.pdf.",
        ("Windows-native scripting language. Central to Windows post-exploitation tradecraft. "
         "[CONFIRMED]\n\n"
         "**Standard offensive tooling:** PowerView (AD recon), PowerSploit, Empire (legacy C2), "
         "Nishang (offensive helpers), Invoke-Mimikatz. Defenders have raised the cost of "
         "naive PowerShell offense via AMSI, ScriptBlock Logging, Constrained Language Mode, "
         "and Just Enough Administration (JEA). Modern red-team practice: bypass AMSI, run "
         ".NET assemblies via execute-assembly (Cobalt Strike) rather than raw PowerShell. See "
         "@concepts/av-edr-bypass.md."),
     ),
]

for filename, title, tags, keywords, related, maturity, raw_concept, narrative in LANGS:
    write_page(
        f"entities/programming-languages/{filename}",
        title,
        "entity",
        tags=tags,
        keywords=keywords,
        related=related,
        maturity=maturity,
        raw_concept=raw_concept,
        narrative=narrative,
    )

# ---------- concepts ----------

write_page(
    "concepts/red-team-operations.md",
    "Red Team Operations",
    "concept",
    tags=["offensive-security", "doctrine", "operations"],
    keywords=["red team", "adversary simulation", "engagement", "ttp"],
    related=[
        "concepts/adversary-emulation.md",
        "concepts/av-edr-bypass.md",
        "concepts/purple-team-operations.md",
        "concepts/social-engineering.md",
        "entities/frameworks/mitre-attack.md",
        "entities/frameworks/cyber-kill-chain.md",
        "entities/tools/cobalt-strike.md",
        "entities/certifications/crto.md",
        "entities/certifications/ecptx.md",
        "sources/red-team-operations-concepts-1.md",
        "sources/red-team-tradecraft-complete-guide.md",
        "sources/what-it-takes-to-be-a-red-team.md",
        "sources/red-team-pentest-english.md",
        "entities/people/joas-a-santos.md",
    ],
    maturity="validated",
    raw_concept=(
        "Anchor concept for the largest single sub-collection in the corpus — 16+ PDFs explicitly "
        "scope-named Red Team (Red Team Operations Concepts/Development/Toolkit, Red Team Tradecraft, "
        "Red Team Career Tips, What it takes to be a Red Team, Red Team x Blue Team, Red_Team_x_Blue_Team, "
        "Cyber Security Complete Journey – Red Team #1, etc.)."
    ),
    narrative=(
        "**Red team ≠ pentest.** [CONFIRMED]\n\n"
        "A pentest's goal is *vulnerability discovery* — \"what are all the ways someone could get in?\" "
        "A red team operation's goal is *defender assessment* — \"how well does the blue team detect, "
        "respond to, and recover from a goal-driven adversary?\" The red team studies real adversaries "
        "and TTPs, then simulates or emulates them — typically with limited or no advance notice to the "
        "blue team. [Source: Red Team Operations – Concepts #1.pdf]\n\n"
        "**Key contrasts:**\n\n"
        "| Dimension | Pentest | Red Team |\n"
        "|-----------|---------|----------|\n"
        "| Goal | Enumerate vulns | Test detection + response |\n"
        "| Scope | Broad (find everything) | Narrow (achieve a stated objective) |\n"
        "| Notification | Defenders know | Defenders typically don't |\n"
        "| Duration | Days–weeks | Weeks–months |\n"
        "| Output | Vuln report | Adversary-narrative report + detection gaps |\n"
        "| Cost driver | Coverage | Stealth + objective realism |\n\n"
        "**Adversary Emulation vs Adversary Simulation:**\n"
        "- *Emulation* — pick a real APT, copy their TTPs end-to-end. Question: \"is our org ready for "
        "APT28 specifically?\"\n"
        "- *Simulation* — assemble a custom blend of TTPs designed to look novel. Question: \"can our "
        "blue team catch unusual but plausible behavior?\"\n"
        "Both are valid; both are used. The choice depends on the engagement's purpose. [Source: Red "
        "Team Operations – Concepts #1.pdf]\n\n"
        "**OPSEC for red teams.** OPSEC (Operational Security) on the red team side covers anything "
        "that could blow the operation: leaked infrastructure (C2 domains tied to obvious patterns), "
        "tool noise (Cobalt Strike default profile = instant detection), insider-clue leakage (test "
        "accounts named \"redteam01\"), uncontrolled blast radius (running an actual destructive "
        "payload on production). The corpus emphasizes: strict access controls, sandboxes for payload "
        "testing, anonymized infrastructure, post-engagement debriefs with blue team. See @concepts/adversary-emulation.md "
        "for the planning playbook.\n\n"
        "**Frameworks that govern formal red-team work (esp. financial sector):**\n"
        "- **TIBER-EU** (Threat Intelligence-Based Ethical Red Teaming, European Central Bank) — the "
        "EU-wide framework for testing significant financial institutions.\n"
        "- **CBEST** (Bank of England) — UK equivalent.\n"
        "- **ABS RTA** (Association of Banks in Singapore) — Singapore equivalent.\n"
        "- **GFMA** framework — global financial-industry guidelines.\n"
        "[Source: Red Team Operations – Concepts #1.pdf]"
    ),
)

write_page(
    "concepts/adversary-emulation.md",
    "Adversary Emulation",
    "concept",
    tags=["red-team", "methodology", "mitre"],
    keywords=["adversary emulation", "apt emulation", "emulation plan", "ttp"],
    related=[
        "concepts/red-team-operations.md",
        "concepts/purple-team-operations.md",
        "entities/frameworks/mitre-attack.md",
        "entities/tools/caldera.md",
        "entities/tools/cobalt-strike.md",
        "entities/threat-actors/apt28.md",
        "sources/adversary-emulation-com-cobalt-strike.md",
        "sources/adversary-emulation-and-cracking-the-bridge-overview.md",
        "sources/adversary-emulation-matrix-by-joas.md",
        "sources/adversary-emulation-services.md",
        "sources/adversary-simulation-with-caldera-and-mitre.md",
        "sources/red-team-operations-simulando-um-grupo-apt-na-pratica.md",
        "sources/red-team-operations-simulating-an-apt-group-in-practice.md",
        "entities/people/joas-a-santos.md",
    ],
    maturity="validated",
    raw_concept=(
        "Corpus has 7+ PDFs that scope explicitly into adversary emulation (Adversary Emulation com "
        "Cobalt Strike, Adversary Emulation Matrix, Adversary Emulation Services, Adversary Simulation "
        "with Caldera and Mitre, Red Team Operations – Simulando um grupo APT na prática, etc.)."
    ),
    narrative=(
        "Adversary Emulation is a proactive cybersecurity practice in which an organization simulates "
        "real-world attack scenarios — modeled on a chosen APT's TTPs — to identify vulnerabilities in "
        "systems, processes, and defenses, and to evaluate the security posture by *thinking like* a "
        "potential attacker. [Source: Red Team Operations – Concepts #1.pdf]\n\n"
        "**Emulation plan structure** [CONFIRMED]\n\n"
        "1. **Scope Definition** — objectives, constraints, boundaries. Which systems/networks/assets "
        "are in scope. Rules of engagement.\n"
        "2. **Reconnaissance** — preliminary OSINT, network discovery, attack-surface mapping.\n"
        "3. **Threat Modeling** — analyze target infra + apps; map architecture; identify weak points + "
        "attack paths.\n"
        "4. **Tactic Selection** — which APT-style TTPs the emulation will use (social engineering / "
        "network exploitation / privilege escalation / lateral movement, etc.).\n"
        "5. **Planning** — detailed step sequence, timeline, resources, contingency plans, stakeholder "
        "approvals.\n"
        "6. **Execution** — deploy specialized tools, exploit vulnerabilities, attempt unauthorized "
        "access, exfiltrate sensitive (test) data per the chosen profile.\n"
        "7. **Detection Evasion** — APT-style — bypass IDS/AV/EDR, leverage 0-days where in scope.\n"
        "8. **Post-Exploitation + Persistence** — establish footholds (backdoors, persistent malware, "
        "privileged accounts) to test long-term-access scenarios.\n"
        "9. **Reporting** — findings, observations, recommendations. Each finding ties back to a TTP and "
        "to detection gaps.\n"
        "10. **Remediation** — work with the blue team to address findings.\n"
        "11. **Follow-Up Testing** — verify remediation closed the actual technique, not just the symptom.\n\n"
        "[Source: Red Team Operations – Concepts #1.pdf]\n\n"
        "**Public emulation plans** to start from rather than design from scratch:\n"
        "- [MITRE APT3 Adversary Emulation Plan](https://attack.mitre.org/docs/APT3_Adversary_Emulation_Plan.pdf)\n"
        "- [MITRE Engenuity Center for Threat-Informed Defense](https://github.com/center-for-threat-informed-defense) — FIN6, "
        "menuPass, Carbanak+FIN7 plans\n"
        "- [SCYTHE Community Threats](https://github.com/scythe-io/community-threats)\n"
        "- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) — atomic tests keyed to ATT&CK techniques\n\n"
        "**Threat Intelligence pre-work** is what separates good emulation from theater. The TTPs you "
        "pick must come from real threat-intel reports about the threat actor you're emulating — "
        "otherwise you're testing against fiction. See @concepts/threat-hunting.md and "
        "@entities/threat-actors/apt28.md."
    ),
)

write_page(
    "concepts/av-edr-bypass.md",
    "AV / EDR Bypass",
    "concept",
    tags=["evasion", "offensive", "windows", "tradecraft"],
    keywords=["av bypass", "edr bypass", "evasion", "ntdll unhooking", "syscall", "shellcode"],
    related=[
        "concepts/red-team-operations.md",
        "concepts/exploit-development.md",
        "entities/frameworks/mitre-attack.md",
        "entities/tools/cobalt-strike.md",
        "entities/programming-languages/c.md",
        "entities/programming-languages/powershell.md",
        "sources/av-and-edr-bypass-techniques-for-new-hackers-update-2022.md",
        "sources/av-edr-bypass-red-team-village-pt-br.md",
        "sources/offensive-security-evasion-techniques-pt-1.md",
        "sources/bypassing-defenses-in-layers.md",
        "sources/dll-hijacking-overview.md",
        "entities/people/joas-a-santos.md",
    ],
    maturity="validated",
    raw_concept=(
        "Anchored by *AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf* (full deck deep-read). "
        "Additional anchors: AV/EDR Bypass Red Team Village, Offensive Security Evasion Techniques, "
        "Bypassing defenses in layers, DLL Hijacking Overview."
    ),
    narrative=(
        "**AV (Antivirus)** is a single program for scanning + detecting + removing viruses, originally "
        "signature-based. **EDR (Endpoint Detection and Response)** is a superset — antivirus *plus* "
        "firewall, whitelisting, monitoring, behavioral detection — operating on a client-server model "
        "centralized for an enterprise. EDR is detective + responsive where AV is preventive. [Source: "
        "AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf]\n\n"
        "Bypassing AV/EDR requires understanding (1) how the solution works, (2) the OS it runs on, "
        "(3) how the OS + solution behave together, (4) bypass technique categories, and (5) programming "
        "(Python/Go/Ruby/C# at high-level; C/C++ + assembly at low-level) + Windows API + Sysinternals.\n\n"
        "### Technique categories [CONFIRMED]\n\n"
        "**1. Obfuscation** — distort malware while preserving its function. Simple but surprisingly "
        "effective against signature-based detection. Examples: PowerShell case randomization, "
        "Invoke-Obfuscation, renaming all strings in Mimikatz to Mimidogz to dodge string signatures.\n\n"
        "**2. Encryption (crypters)** — encrypt the payload and ship a decryption stub. Two variants:\n"
        "- *Scantime crypters* — decrypt, drop to disk, execute. Naive — disk drop is detected.\n"
        "- *Runtime crypters* — decrypt + execute in memory, never touching disk. Standard for modern "
        "implants.\n\n"
        "**3. NTDLL Unhooking** — most EDRs hook ntdll.dll (the Windows API gateway) at process start. "
        "Unhooking replaces the in-memory hooked ntdll.dll with a fresh copy from disk → the EDR is blind. "
        "Re-hooking at end of op covers tracks. [Source: AV and EDR Bypass Techniques.pdf]\n\n"
        "**4. Direct + Indirect Syscalls** — high-level Windows APIs (kernel32, user32) call low-level "
        "APIs (ntdll), which finally invoke syscalls. EDR-hooked ntdll can be bypassed by:\n"
        "- *Direct syscall* — emit the `syscall` instruction directly, skipping ntdll entirely. "
        "Detection: \"Mark of the Syscall\" — syscalls from outside known modules look suspicious.\n"
        "- *Indirect syscall* — emit a `jmp` to a `syscall` instruction inside ntdll, so the syscall "
        "*originates* from a known module while still skipping the hook.\n"
        "- *Vectored syscall* — use Windows VEH (Vectored Exception Handler) to modify RIP, redirecting "
        "execution into ntdll's syscall instruction. Bypasses RIP-based instrumentation-callback detection.\n\n"
        "**5. Patching the patch** — EDRs that hook by patching specific function prologues (jmp to "
        "EDR inspection code) can be defeated by patching over the EDR's jmp with a no-op or by "
        "restoring the original prologue. Vendor-specific (see SpecialHoang + MDsec 2019 Cylance "
        "post). The disadvantage: every EDR vendor's hooks differ, so this approach needs per-vendor "
        "tuning.\n\n"
        "**6. Unmanaged code invocation (DInvoke)** — call native Windows API functions dynamically "
        "via .NET P/Invoke without exposing them in the binary's Import Address Table. Bypasses static "
        "IAT analysis.\n\n"
        "**7. UUID-encoded shellcode** — encode shellcode as UUIDs and reassemble at runtime via "
        "UuidFromStringA. Static analysis sees benign-looking UUID strings; no `syscall` instruction "
        "or recognizable shellcode in the binary opcode.\n\n"
        "**8. LSA / LSASS protection bypass** — to read LSASS for credential dumping when LSA "
        "Protection (RunAsPPL) is enabled, options are: remove RunAsPPL registry key (worst — reboots "
        "lose credentials), disable PPL flags via kernel memory patching (via a signed-but-vulnerable "
        "driver like RTCore64.sys; see [PPLKiller](https://github.com/RedCursorSecurityConsulting/PPLKiller)), "
        "or read LSASS process memory directly with kernel-level access. [Source: AV and EDR Bypass.pdf]\n\n"
        "### Mitigation (defender side)\n\n"
        "Effective EDR catches behavioral patterns regardless of the bypass technique used: process "
        "tree anomalies, unusual API call sequences, syscall origin tracking, in-memory hash matching "
        "of decrypted payloads, ETW (Event Tracing for Windows) for tamper detection. Bypasses age "
        "quickly — every technique above has a corresponding defender response. The wiki tracks "
        "techniques with `[NEEDS VERIFICATION YYYY-MM-DD]` so we know to retest annually."
    ),
    snippets=(
        "**Tooling lists from the corpus** [Source: AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf]\n\n"
        "Obfuscators + bypassers:\n"
        "- [AVIator](https://github.com/Ch0pin/AVIator) — AV bypass framework\n"
        "- [PyFuscation](https://github.com/CBHue/PyFuscation) — PowerShell obfuscation by variables, functions, parameters\n"
        "- [Veil-Evasion](https://github.com/Veil-Framework/Veil-Evasion) — payload obfuscation framework\n"
        "- [Shellter Project](https://www.shellterproject.com/) — PE injector with dynamic encoding\n"
        "- [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation) — PowerShell obfuscation (Daniel Bohannon, 2016)\n"
        "- [Amsi-Bypass-Powershell](https://github.com/S3cur3Th1sSh1t/Amsi-Bypass-Powershell)\n"
        "- [UnmanagedPowerShell](https://github.com/leechristensen/UnmanagedPowerShell)\n"
        "- [FilelessRemotePE](https://github.com/D1rkMtr/FilelessRemotePE)\n"
        "- [uuid-loader](https://github.com/pwn1sher/uuid-loader)\n"
        "- [IORI_Loader](https://github.com/D1rkMtr/IORI_Loader)\n"
        "- [VEH-PoC (Vectored Syscall)](https://github.com/RedTeamOperations/VEH-PoC/)\n"
        "- [Awesome Red-Teaming Defense Evasion list](https://github.com/yeyintminthuhtut/Awesome-Red-Teaming#-defense-evasion)\n\n"
        "Reading:\n"
        "- [ired.team / Defense Evasion](https://www.ired.team/offensive-security/defense-evasion/)\n"
        "- [MITRE ATT&CK Defense Evasion tactic (TA0005)](https://attack.mitre.org/tactics/TA0005/)\n"
        "- [F-Secure: AV bypass techniques through an EDR lens](https://blog.f-secure.com/av-bypass-techniques-through-an-edr-lens/)\n"
        "- [itm4n: Bypassing LSA Protection in userland](https://itm4n.github.io/bypassing-lsa-protection-userland/)\n"
        "- [NCC Group: RIFT - Lazarus shellcode execution method](https://research.nccgroup.com/2021/01/23/rift-analysing-a-lazarus-shellcode-execution-method/)\n"
        "- [DInvoke_rs by NVISO](https://github.com/NVISOsecurity/brown-bags/tree/main/DInvoke%20to%20defeat%20EDRs)"
    ),
)

write_page(
    "concepts/web-pentest-methodology.md",
    "Web Pentest Methodology",
    "concept",
    tags=["web-app", "owasp", "methodology"],
    keywords=["web pentest", "owasp", "wstg", "xxe", "sqli", "xss", "ssrf", "idor", "subdomain takeover"],
    related=[
        "entities/tools/burp-suite.md",
        "entities/certifications/oswa.md",
        "entities/certifications/oswe.md",
        "entities/certifications/ewpt.md",
        "concepts/bug-bounty.md",
        "entities/programming-languages/javascript.md",
        "sources/web-pentesting-checklist-by-joas.md",
        "sources/pentest-web-do-black-box-ao-white-box.md",
        "sources/wstg-web-application-security-testing-owasp-mind-map.md",
        "sources/communs-web-attack-reference-pt-1.md",
        "sources/complete-bug-bounty-cheat-sheet.md",
        "sources/offensive-security-web-exploitation.md",
        "sources/offensive-security-web-exploitation-2.md",
        "sources/apostila-ataques-web-basico.md",
        "sources/resume-web-pentest-by-joas.md",
        "sources/versao-final-atualizada-vulnerabilidades-comuns-em-aplica-es-web-roadsec-2023.md",
        "entities/people/joas-a-santos.md",
        "@seo-wiki/concepts/web-vitals.md",
    ],
    maturity="validated",
    raw_concept=(
        "Highest-volume topic in the corpus — 12+ PDFs scope into web pentest. Web PenTesting Checklist "
        "by Joas.pdf was deep-read to anchor real content; the comprehensive checklist there covers "
        "every major OWASP class plus operational edge cases."
    ),
    narrative=(
        "Web-app testing has been the highest-volume subdomain of pentest for two decades. The corpus's "
        "*Web PenTesting Checklist by Joas* organizes engagement workflow around 12+ attack classes "
        "plus configuration / header / cookie hardening. The checklist below is paraphrased from the "
        "deep-read source. [Source: Web PenTesting Checklist by Joas.pdf]\n\n"
        "### Mapping + recon\n\n"
        "- **Subdomain enumeration** — Sublist3r, Amass, dnsrecon for active discovery; crt.sh / Censys "
        "for certificate-derived subdomains.\n"
        "- **DNS records** — examine CNAME / A / AAAA / MX for subdomains pointing to external services "
        "or expired domains (subdomain takeover risk: AWS S3, GitHub Pages, Heroku CNAMEs are the "
        "classic stale-pointer attack surface).\n"
        "- **HTTP responses** — error codes and headers reveal stack, version, behind-the-scenes "
        "framework.\n\n"
        "### Attack classes\n\n"
        "**1. SQL Injection (SQLi)** — single-quote test → tautologies → UNION-based extraction → "
        "error-based → time-based (`SLEEP()` / `WAITFOR DELAY`) → out-of-band (DNS lookups, HTTP "
        "callbacks). Dialect-specific payloads (MySQL / PostgreSQL / Oracle / MSSQL). Test cookies + "
        "headers + content-type variants (JSON/XML/form). Use sqlmap once a candidate is identified.\n\n"
        "**2. Cross-Site Scripting (XSS)** — basic `<script>alert(1)</script>` → encoded variants (URL "
        "/ hex / HTML entity / null-byte / double-encoded) → attribute injection → SVG payloads → "
        "JavaScript event handlers (onmouseover/onfocus/onclick) → context-specific (HTML comment / "
        "inline JS / CSS). Reflected via error pages is a common-but-missed vector.\n\n"
        "**3. Cross-Site Request Forgery (CSRF)** — attempt state-changing actions without a valid "
        "CSRF token, or with another user's authenticated session. Check SameSite cookie attribute.\n\n"
        "**4. Server-Side Request Forgery (SSRF)** — user-controlled URLs → fetch internal IPs "
        "(127.0.0.1, 169.254.169.254 for cloud metadata, RFC1918 ranges) → URL schemas (file:// "
        "/ ftp:// / gopher://) → URL redirection chains → out-of-band data exfil → cloud metadata "
        "endpoint access (AWS IMDS, GCP metadata, Azure IMDS).\n\n"
        "**5. XML External Entity (XXE)** — basic external entity reference → external parameter "
        "entity → blind XXE via OOB → file inclusion via SYSTEM identifier → internal entity expansion "
        "(Billion Laughs DoS) → CDATA wrapping → custom-encoded XML. Test SOAP, XHTML, SVG, RSS, "
        "Office Open XML (.docx/.pptx/.xlsx), OpenDocument (.odt/.ods/.odp).\n\n"
        "**6. Insecure Direct Object Reference (IDOR)** — sequential IDs in URLs / hidden fields / API "
        "endpoints → modify to access another user's data. Multi-account testing (admin/user/guest "
        "roles) to find authorization gaps. Test password reset, email validation, file uploads.\n\n"
        "**7. File Upload** — file size limits, type restrictions, MIME validation, filename sanitization "
        "(`../`, `.htaccess`, double extensions), antivirus scanning, duplicate-name handling, upload "
        "directory permissions + access controls, image-processing library vulnerabilities (buffer "
        "overflows in ImageMagick etc.), embedded scripts in file contents/metadata.\n\n"
        "**8. Subdomain Takeover** — dangling CNAMEs to deleted/expired services. Tools: SubOver, Subjack, "
        "tko-subs. Common takeover targets: GitHub Pages, AWS S3, Heroku, Zendesk, Tumblr.\n\n"
        "### Configuration hardening checks\n\n"
        "**HTTP headers** — Strict-Transport-Security (HSTS), X-Content-Type-Options (no-sniff), "
        "X-Frame-Options (clickjacking), Content-Security-Policy (CSP), X-XSS-Protection (legacy), "
        "Referrer-Policy, Feature-Policy / Permissions-Policy, Public-Key-Pins (HPKP — deprecated but "
        "occasionally cited), CORS Access-Control-Allow-Origin (no `*` for authenticated endpoints), "
        "Expect-CT, X-Permitted-Cross-Domain-Policies. [Source: Web PenTesting Checklist by Joas.pdf]\n\n"
        "**Cookies** — Secure, HttpOnly, SameSite (Strict/Lax), Domain + Path scoping, sufficient "
        "lifetime limits, sufficient session-ID entropy, no sensitive data stored in cookies.\n\n"
        "**TLS** — disable SSL 2/3 + TLS 1.0; enable TLS 1.2 + 1.3 only; strong cipher suites "
        "(AES-GCM / ChaCha20-Poly1305 / ECDHE); valid certificate chain; OCSP stapling; forward "
        "secrecy; protection against POODLE / BEAST / CRIME / BREACH / Heartbleed.\n\n"
        "**CMS-specific (WordPress)** — keep core + plugins + themes patched; strong admin passwords "
        "(no default `admin` username); login attempt limiting (Wordfence / Login LockDown); user "
        "enumeration disabled; XML-RPC disabled if unused; file/folder permissions; SQLi + XSS in "
        "comments / search; wp-config.php hardening (disable error display, disable file editing).\n\n"
        "**WAF testing** — HTTP method coverage, malformed-request handling, evasion (encoding / "
        "case-variation), IP/UA blocking bypass via proxies, rate limiting, cookie manipulation "
        "detection, file-upload signatures, false positive / false negative balance.\n\n"
        "### Standards + frameworks\n\n"
        "- **OWASP WSTG** ([Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)) — "
        "the canonical test-by-test methodology. Anchored by *WSTG (Web Application Security Testing) "
        "OWASP - Mind Map.pdf* in the corpus.\n"
        "- **OWASP Top 10** — high-level vuln categories, refreshed every 3-4 years.\n"
        "- **OWASP ASVS** — Application Security Verification Standard. Three levels of assurance.\n"
        "- **NIST SP 800-115** — Technical Guide to Information Security Testing and Assessment.\n\n"
        "**Cross-wiki note:** for client-side web vital concerns (Core Web Vitals, page-speed signals "
        "in SEO), see @seo-wiki/concepts/web-vitals.md. Web pentest and SEO web-perf testing share the "
        "same proxy/devtools stack but the success metrics differ."
    ),
)

write_page(
    "concepts/osint-for-cybersecurity.md",
    "OSINT for Cybersecurity",
    "concept",
    tags=["osint", "recon", "reconnaissance", "intelligence"],
    keywords=["osint", "open source intelligence", "recon", "investigation", "shodan", "maltego"],
    related=[
        "entities/tools/maltego.md",
        "concepts/red-team-operations.md",
        "concepts/social-engineering.md",
        "concepts/threat-hunting.md",
        "sources/osint-overview-pt-1.md",
        "sources/apostila-a-arte-do-osint-para-pentesters.md",
        "sources/fundamentos-de-osint.md",
        "sources/investigation-using-osint-with-a-focus-on-intelligence-operations-and-dark-web-operations-training.md",
        "sources/using-osint-techniques-to-investigate-human-trafficking-and-missing-persons-pt-1.md",
        "sources/using-osint-to-investigate-human-trafficking-and-missing-persons.md",
        "sources/using-osint-to-investigate-school-shooters.md",
        "sources/ransomware-investigation-osint-and-hunting-overview-pt1.md",
        "entities/people/joas-a-santos.md",
        "@osint-wiki/concepts/typed-relation-dependencies.md",
    ],
    maturity="validated",
    raw_concept=(
        "7+ corpus PDFs explicitly scope to OSINT — pentest-side (APOSTILA A ARTE DO OSINT PARA "
        "PENTESTERS, OSINT Overview, FUNDAMENTOS DE OSINT) + investigative-side (human trafficking, "
        "missing persons, school shooters, ransomware investigation)."
    ),
    narrative=(
        "OSINT (Open-Source Intelligence) is the discipline of collecting + analyzing publicly available "
        "information to support an investigation or operation. In cybersecurity it appears in three "
        "distinct roles: [CONFIRMED]\n\n"
        "**1. Pentest / Red Team recon.** Pre-engagement OSINT establishes the target's external "
        "footprint without sending a single packet to their infrastructure: subdomain enumeration via "
        "crt.sh, dnsdumpster, Censys; corporate identity mapping via LinkedIn / GitHub / Twitter; "
        "leaked credentials via HaveIBeenPwned / Dehashed / IntelX; technology fingerprinting via Wappalyzer "
        "/ BuiltWith; certificate-transparency mining for shadow domains. The corpus's *APOSTILA A ARTE "
        "DO OSINT PARA PENTESTERS.pdf* anchors the pentest-side methodology.\n\n"
        "**2. Defensive / threat intelligence.** Threat-intel teams use OSINT to track threat actors — "
        "OPSEC mistakes in social media, infrastructure reuse across campaigns, public TTP write-ups, "
        "leaked builder kits on criminal forums. The corpus's *Ransomware Investigation (osint and "
        "hunting).pdf* anchors this use case.\n\n"
        "**3. Investigation (human-impact context).** Law enforcement + nonprofits use OSINT for human "
        "trafficking investigations, missing-persons searches, child-safety case work, threat assessments "
        "for school violence. Four corpus PDFs cover this niche specifically: human-trafficking (EN + "
        "PT-BR), missing persons, and school shooters. **This use case requires extra ethical care** — "
        "victim privacy + chain-of-custody for evidence + jurisdictional rules around what's admissible.\n\n"
        "### Tool families\n\n"
        "- **Domain + IP**: whois / dig / crt.sh / SecurityTrails / Shodan / Censys / DNSDumpster / "
        "DNS history sites\n"
        "- **People + accounts**: Sherlock, WhatsMyName, Maigret (cross-platform username lookups); "
        "Holehe, Epieos (email enumeration); LinkedIn / Twitter / Facebook / Instagram with proper OPSEC\n"
        "- **Leaked credentials**: HaveIBeenPwned, Dehashed, IntelX, ScyllaDB credential dumps\n"
        "- **Graph + linkage**: @entities/tools/maltego.md (commercial + community), SpiderFoot, "
        "Recon-ng (frameworks that orchestrate the smaller tools)\n"
        "- **Code search**: GitHub Dorking (`extension:env DB_PASSWORD`), GitLeaks, TruffleHog for repo "
        "secret discovery\n"
        "- **Image + geolocation**: reverse image search (TinEye, Yandex), EXIF tools, GeoSpy AI for "
        "image-derived geolocation\n"
        "- **Dark web** (caveat: needs Tor + OPSEC): Ahmia, OnionLand, Dread, exposed-credentials dumps "
        "on criminal forums. Use VMs + read-only browsing; never paste anything identifying.\n\n"
        "### Cross-wiki anchor\n\n"
        "The sibling **OSINT wiki** (@osint-wiki/) covers OSINT primarily through the financial-research "
        "lens (ticker due-diligence, congressional-trade tracking, prediction-market sentiment), with "
        "deeper coverage of source-evaluation methodology + exploration-graph dead-ends. When this wiki "
        "needs a methodology reference, prefer linking there rather than duplicating. Example: "
        "@osint-wiki/concepts/typed-relation-dependencies.md."
    ),
)

# Stubs for the rest — one paragraph each, linked to corpus sources.

STUBS: list[tuple[str, str, str, list[str], list[str], list[str], str, str]] = [
    ("concepts/purple-team-operations.md", "Purple Team Operations", "concept",
        ["purple-team", "collaboration", "detection-engineering"],
        ["purple team", "red blue collaboration", "detection engineering"],
        ["concepts/red-team-operations.md", "concepts/adversary-emulation.md", "concepts/soc-operations.md",
         "entities/tools/caldera.md", "entities/tools/wazuh.md",
         "sources/purple-team-lab-01-wazuh-and-win2016.md", "entities/people/joas-a-santos.md"],
        "Anchored by Purple Team Lab 01 - Wazuh and Win2016.pdf.",
        ("Purple team = red + blue working **together** in real time. Where red team operations test "
         "the blue team blindly, a purple-team engagement is collaborative: attackers fire a known TTP, "
         "defenders watch + tune detections, both sides iterate until coverage is achieved. The "
         "corpus's hands-on lab (Wazuh + Windows 2016) is a typical entry point — Wazuh as SIEM, a "
         "Windows victim, MITRE ATT&CK technique catalog as the test menu. See "
         "@concepts/adversary-emulation.md for the technique-selection side and "
         "@entities/tools/wazuh.md for the SIEM side. [CONFIRMED]"),
     ),
    ("concepts/soc-operations.md", "SOC Operations", "concept",
        ["soc", "blue-team", "siem", "detection"],
        ["soc", "siem", "monitoring", "wazuh", "elk", "splunk"],
        ["concepts/incident-response.md", "concepts/threat-hunting.md", "concepts/purple-team-operations.md",
         "entities/tools/wazuh.md", "sources/100-security-operation-center-tools.md",
         "sources/security-operation-center-open-source.md",
         "sources/security-operation-center-40-tools.md",
         "sources/security-operation-center-operations-development.md",
         "sources/security-operation-center-study-and-career-2022.md",
         "sources/security-operation-center-and-analysis.md",
         "sources/low-cost-soc.md", "sources/low-cost-soc-tools-2.md",
         "sources/soc-open-source-tools.md", "sources/soc-analyst-career.md",
         "entities/people/joas-a-santos.md"],
        "11+ corpus PDFs scope into SOC operations.",
        ("Security Operations Center = the people + processes + tooling that detect, triage, and "
         "respond to security events 24×7. Tiered model: Tier-1 (alert triage), Tier-2 (incident "
         "analysis), Tier-3 (threat hunting + IR + advanced reverse engineering). Tooling stack: "
         "SIEM (Wazuh / Splunk / Elastic / Sentinel / QRadar), SOAR (Cortex XSOAR / Tines), EDR "
         "(CrowdStrike / Defender for Endpoint / SentinelOne), threat-intel (MISP / OpenCTI). The "
         "corpus's *Low Cost SOC* PDFs explicitly cover the FOSS path: Wazuh + Elastic + TheHive + "
         "MISP + Velociraptor. See @entities/tools/wazuh.md and @concepts/threat-hunting.md."),
     ),
    ("concepts/incident-response.md", "Incident Response", "concept",
        ["dfir", "blue-team", "response"],
        ["incident response", "ir", "dfir", "ecir"],
        ["concepts/soc-operations.md", "concepts/threat-hunting.md", "concepts/malware-analysis.md",
         "sources/incident-response-overview.md", "sources/incident-response-simulation-1.md",
         "sources/elearnsecurity-certified-incident-response-ecir-guide-study-to-exam.md",
         "entities/people/joas-a-santos.md"],
        "Three corpus PDFs anchor (Incident response - overview, Incident Response Simulation 1, eCIR Guide).",
        ("Incident Response = the structured process for detecting → containing → eradicating → "
         "recovering from → learning from a security incident. NIST SP 800-61r2 is the canonical "
         "lifecycle (Preparation / Detection & Analysis / Containment, Eradication & Recovery / "
         "Post-Incident Activity). SANS uses the PICERL model (Preparation, Identification, Containment, "
         "Eradication, Recovery, Lessons Learned). The corpus's *Incident Response Simulation 1.pdf* is "
         "a hands-on tabletop exercise. Cross-link: @concepts/malware-analysis.md (for malware-driven "
         "incidents) and @concepts/soc-operations.md (where IR teams live organizationally)."),
     ),
    ("concepts/threat-hunting.md", "Threat Hunting", "concept",
        ["proactive", "blue-team", "detection"],
        ["threat hunting", "hunt", "kibana", "elastic", "splunk"],
        ["concepts/soc-operations.md", "concepts/incident-response.md", "entities/frameworks/mitre-attack.md",
         "sources/elearnsecurity-certified-threat-hunting-introduction-pt-1.md",
         "sources/malware-hunting-threat-hunter-overview-1.md",
         "entities/people/joas-a-santos.md"],
        "Two corpus PDFs anchor.",
        ("Threat Hunting = proactive search for adversary activity in environments where no alert has "
         "fired. Hypothesis-driven: \"if APT29 were already inside, what would I expect to see in "
         "scheduled tasks / WMI subscriptions / unusual parent-child process trees?\" Pyramid of Pain "
         "(David Bianco) is the canonical mental model — hash IOCs are easy to dodge, TTPs are not. "
         "Hunting workflows pair tightly with MITRE ATT&CK (the technique tree) and the SIEM "
         "(query substrate)."),
     ),
    ("concepts/malware-analysis.md", "Malware Analysis + Reverse Engineering", "concept",
        ["reverse-engineering", "malware", "static-analysis", "dynamic-analysis"],
        ["malware analysis", "reverse engineering", "ghidra", "ida", "x64dbg"],
        ["concepts/incident-response.md", "concepts/threat-hunting.md", "entities/programming-languages/c.md",
         "sources/introdu-o-b-sica-a-analise-de-malware-1.md",
         "sources/malware-and-reverse-engineering-complete-collection-by-joas.md",
         "sources/reverse-engineering-content-study-1.md",
         "sources/reverse-engineering-research-storm.md",
         "sources/overview-windows-api-s-and-internals-reverse-engineering.md",
         "entities/people/joas-a-santos.md"],
        "Five corpus PDFs anchor.",
        ("Malware Analysis splits into static (analyze the binary without running it — strings, "
         "imports, PE/ELF/Mach-O headers, disassembly with Ghidra / IDA / Cutter) and dynamic (detonate "
         "the binary in a controlled environment — sandboxed VM with Procmon, Wireshark, x64dbg, ProcDot, "
         "Cuckoo). Output: IOCs (hashes, domains, IPs, registry keys, file paths) + behavioral signature "
         "+ attribution hypothesis. The corpus's *Windows API's and Internals & Reverse Engineering* "
         "overview is the foundation for Windows-centric work."),
     ),
    ("concepts/exploit-development.md", "Exploit Development", "concept",
        ["binary-exploitation", "shellcode", "buffer-overflow", "advanced"],
        ["exploit development", "buffer overflow", "shellcode", "rop", "aslr", "dep"],
        ["entities/programming-languages/c.md", "concepts/av-edr-bypass.md",
         "entities/certifications/oswe.md",
         "sources/buffer-overflow-for-beginners-joas.md",
         "sources/buffer-overflow-guide-1.md",
         "sources/buffer-overflow-introduction.md",
         "sources/introdu-o-ao-buffer-overflow-1.md",
         "sources/introdu-o-ao-desenvolvimento-de-exploits.md",
         "sources/introdu-o-ao-desenvolvimento-de-exploits-2.md",
         "sources/fundamentos-de-desenvolvimento-de-exploits-overview.md",
         "sources/fundamentals-cracking-the-perimeter.md",
         "sources/shellcode-development.md", "sources/shellcode-development-2.md",
         "sources/offensive-security-exploit-development-windows-overview.md",
         "sources/elearnsecurity-exploit-development-student-notes-by-joas.md",
         "entities/people/joas-a-santos.md"],
        "13+ corpus PDFs anchor — this is one of the deepest subdomains.",
        ("Exploit Development = writing code that turns a memory-corruption bug into reliable arbitrary "
         "code execution. Pipeline: trigger crash → identify control (typically EIP/RIP overwrite) → "
         "find usable space → defeat mitigations (DEP via ROP, ASLR via info leak, stack canaries, "
         "CFG, ACG, CET) → land shellcode (or use msfvenom). Modern exploit dev is **harder than 2010** "
         "— ASLR + DEP + Control Flow Guard close many naive paths; today's targets are typically "
         "type confusion / use-after-free / heap grooming. Standard learning ladder: stack overflows "
         "(eg. SLMail / vulnserver) → SEH-based exploits → ROP → heap grooming → kernel exploits. "
         "Cert ladder: OSCP/OSED (Windows user-mode) → OSEE (kernel + advanced)."),
     ),
    ("concepts/cyber-for-kids.md", "Cyber Safety for Kids + Families", "concept",
        ["education", "child-safety", "parenting"],
        ["cyber for kids", "cyberbullying", "child safety", "internet safety"],
        ["concepts/social-engineering.md",
         "sources/cyber-security-career-for-children-pt-1.md",
         "sources/cyber-security-for-kids-2-1.md",
         "sources/cyber-security-for-kids-2.md",
         "sources/cyber-security-for-kids.md",
         "sources/cybersecurity-for-kids-english.md",
         "sources/cybersecurity-for-kids-pt-br.md",
         "sources/cybersecurity-and-cyberbullying-education-for-kids.md",
         "sources/cyberbullying-and-its-consequences.md",
         "sources/cyberbullying-e-as-consequ-ncias.md",
         "sources/seguran-a-infantil-um-problema-s-rio-mas-pouco-falado.md",
         "sources/child-safety-a-serious-problem-but-little-talked-about-english.md",
         "sources/seguran-a-na-internet-para-crian-as.md",
         "sources/sobrevivendo-a-um-ataque-escolar.md",
         "sources/surviving-a-school-attack.md",
         "sources/instagram-social-network-security.md",
         "sources/golpe-do-perfil-falso-no-whatsapp-medidas-preventivas.md",
         "sources/redes-sociais-o-lado-sombrio-do-discord.md",
         "sources/internet-safety-sexual-predators-and-stalkers-how-to-protect-yourself.md",
         "entities/people/joas-a-santos.md"],
        "20+ corpus PDFs scope into cyber safety for kids + families — second-largest sub-collection.",
        ("Sub-collection of the corpus dedicated to age-appropriate cyber-safety material for parents, "
         "teachers, school staff, and law-enforcement. Topics: cyberbullying recognition + response, "
         "fake-profile scams (WhatsApp / Instagram / Discord), sexual-predator + stalker awareness, "
         "school-attack survival (active-shooter pre-attack signal recognition + lockdown best "
         "practices). **Ethical framing matters:** these pages are written for *protective* context — "
         "parents talking with kids, teachers running classroom modules, LE officers building "
         "investigations. The pages should not be readable as a how-to for the inverse use case. "
         "Bilingual PT-BR + EN coverage across most topics. [CONFIRMED]"),
     ),
    ("concepts/social-engineering.md", "Social Engineering", "concept",
        ["offensive", "human-factor", "phishing"],
        ["social engineering", "phishing", "spear phishing", "vishing", "pretexting"],
        ["concepts/red-team-operations.md", "concepts/osint-for-cybersecurity.md",
         "concepts/cyber-for-kids.md",
         "sources/social-engineering-practical-overview.md",
         "sources/introdu-o-a-engenharia-social-pr-tica.md",
         "entities/people/joas-a-santos.md"],
        "Two corpus PDFs (PT-BR + EN) anchor.",
        ("Social engineering = manipulating people to perform actions that compromise security. "
         "Categories: phishing (email), vishing (voice / phone), smishing (SMS), pretexting (false "
         "identity), tailgating (physical), baiting (USB drops / lures). For red team work, social "
         "engineering is typically the cheapest path to initial access. The corpus pairs this concept "
         "with @concepts/cyber-for-kids.md — the same techniques used offensively against employees "
         "appear in fake-profile WhatsApp scams against teens."),
     ),
    ("concepts/windows-pentest.md", "Windows + Active Directory Pentest", "concept",
        ["windows", "active-directory", "post-exploitation"],
        ["active directory", "ad", "kerberos", "ntlm", "mimikatz", "bloodhound", "o365"],
        ["concepts/red-team-operations.md", "concepts/av-edr-bypass.md",
         "concepts/privilege-escalation.md",
         "entities/programming-languages/powershell.md", "entities/tools/bloodhound.md",
         "sources/windows-server-and-active-directory-pentest.md",
         "sources/windows-server-ad-and-o365-advanced-pentest.md",
         "sources/windows-enterprise-network-pentest.md",
         "sources/windows-persistence-techniques.md",
         "sources/windows-privilege-escalation-overview.md",
         "sources/windows-api-for-red-team-101-english.md",
         "sources/windows-api-for-red-team-101-portuguese.md",
         "sources/windows-api-for-red-team-102-english.md",
         "sources/windows-api-for-red-team-102-portugues.md",
         "sources/pentest-com-powershell-overview.md",
         "sources/pentest-in-office365-and-security.md",
         "entities/people/joas-a-santos.md"],
        "12+ corpus PDFs anchor.",
        ("Windows + AD pentest is one of the largest sub-domains in the corpus. Core attack surfaces: "
         "Kerberos abuse (Kerberoasting / AS-REP roasting / Golden Ticket / Silver Ticket / Skeleton "
         "Key), NTLM relay, ACL abuse, GPO abuse, DC sync (Mimikatz), DCShadow, Constrained / "
         "Unconstrained delegation abuse, Resource-Based Constrained Delegation (RBCD). Standard "
         "tooling: BloodHound (graph), Mimikatz / Rubeus (Kerberos), Impacket (Python protocol "
         "implementations), Certify (AD CS abuse), ADCSPwn / Certipy (ESC1-ESC14 paths against AD "
         "Certificate Services). For Office 365 attack: AADInternals, MFASweep, MicroBurst. See "
         "@concepts/privilege-escalation.md."),
     ),
    ("concepts/privilege-escalation.md", "Privilege Escalation", "concept",
        ["post-exploitation", "linux", "windows"],
        ["privilege escalation", "linpeas", "winpeas", "kernel exploit", "sudo abuse"],
        ["concepts/windows-pentest.md", "concepts/exploit-development.md",
         "sources/linux-privilege-escalation-overview.md",
         "sources/windows-privilege-escalation-overview.md",
         "sources/conceitos-b-sicos-de-p-s-explora-o-1.md",
         "sources/introdu-o-a-p-s-explora-o.md",
         "entities/people/joas-a-santos.md"],
        "Anchored by Linux + Windows privesc PDFs + two post-exploitation overviews.",
        ("Privilege Escalation = going from initial low-privilege foothold to higher privileges "
         "(typically root / SYSTEM / Domain Admin). Splits cleanly by OS: **Linux** — SUID binaries "
         "(GTFOBins reference), sudo misconfig, weak file permissions, kernel exploits, capability "
         "abuse, cron jobs, NFS no_root_squash, container escapes. **Windows** — service "
         "misconfigurations (AlwaysInstallElevated, modifiable service binaries, unquoted service "
         "paths), token impersonation (RoguePotato / PrintSpoofer family), DLL hijacking, kernel "
         "exploits, scheduled-task abuse. Standard enumeration: LinPEAS / WinPEAS, PowerUp, "
         "Seatbelt. See @concepts/windows-pentest.md."),
     ),
    ("concepts/cloud-pentest.md", "Cloud Pentest (AWS / Azure / GCP / O365)", "concept",
        ["cloud", "aws", "azure", "gcp", "office365"],
        ["cloud pentest", "aws", "azure", "gcp", "o365", "multi-cloud"],
        ["concepts/red-team-operations.md", "concepts/windows-pentest.md",
         "sources/pentest-em-ambientes-cloud-1.md",
         "sources/multi-cloud-red-team-pt-1.md",
         "sources/google-cloud-attack-overview-pt1.md",
         "sources/pentest-in-office365-and-security.md",
         "sources/windows-server-ad-and-o365-advanced-pentest.md",
         "entities/people/joas-a-santos.md"],
        "Five corpus PDFs anchor (Cloud, Multi-Cloud Red Team, Google Cloud Attack, O365 Pentest, AD+O365).",
        ("Cloud pentest extends the on-prem attack surface to provider-specific risk: misconfigured "
         "S3 buckets / Storage Accounts, IAM role-chaining abuse, metadata-endpoint SSRF (AWS IMDS "
         "v1/v2, GCP/Azure equivalents), serverless misconfig (Lambda / Azure Functions / Cloud "
         "Functions), cross-account assumeRole abuse, GitHub Actions / OIDC trust mistakes. Standard "
         "tools: ScoutSuite, Prowler, CloudSploit, Pacu (AWS), MicroBurst / ROADtools (Azure / Entra "
         "ID), GCPBucketBrute. Multi-cloud engagements add identity-federation seam exploitation."),
     ),
    ("concepts/mobile-pentest.md", "Mobile App Pentest", "concept",
        ["mobile", "android", "ios"],
        ["mobile pentest", "android", "ios", "frida", "objection", "emapt"],
        ["concepts/web-pentest-methodology.md",
         "sources/elearnsecurity-mobile-application-penetration-testing.md",
         "sources/introdu-o-ao-pentest-mobile-pt-1.md",
         "sources/carreira-em-desenvolvimento-mobile.md",
         "entities/people/joas-a-santos.md"],
        "Three corpus PDFs anchor.",
        ("Mobile pentest = static analysis of the app binary (APK / IPA) + dynamic analysis at "
         "runtime + backend API testing. Standard tools: MobSF (Mobile Security Framework — static "
         "+ initial dynamic), Frida + Objection (runtime instrumentation, hook / replace methods, "
         "bypass root/jailbreak detection + SSL pinning), apktool / jadx (decompile Android), Hopper "
         "/ Ghidra (iOS / Mach-O), Burp Suite (proxied traffic). OWASP MASVS + MASTG are the canonical "
         "methodology standards."),
     ),
    ("concepts/network-security.md", "Network Security + Firewall + Wireless + IoT/OT", "concept",
        ["network", "firewall", "wireless", "iot", "ot"],
        ["firewall", "network security", "wireless", "wifi", "iot", "ot", "ics"],
        ["concepts/red-team-operations.md", "entities/tools/nmap.md",
         "sources/fundamentos-de-firewall.md", "sources/introdu-o-a-network-security-1-0.md",
         "sources/introdu-o-a-network-security-e-firewall.md",
         "sources/offensive-security-wireless-fundamentals.md",
         "sources/offensive-security-wireless.md",
         "sources/hardware-hacking-introduction-overview.md",
         "sources/pentest-iot-and-ot-overview.md",
         "entities/people/joas-a-santos.md"],
        "Eight corpus PDFs anchor.",
        ("Network security = traditional network-layer + perimeter topics (firewalls, IDS/IPS, "
         "segmentation, VLANs, NAC) plus the wireless + IoT + OT extensions. Wireless: WPA2 attacks "
         "(PMKID, handshake capture + offline crack with hashcat), WPA3 (Dragonblood), Evil Twin / "
         "captive-portal phishing. IoT: firmware extraction (binwalk), hardware interfaces (UART, "
         "JTAG, SPI dumps via Bus Pirate / Saleae), default credential mining. OT/ICS: Modbus, "
         "PROFINET, DNP3 protocol attacks — context-specific because of real-world safety implications. "
         "See @concepts/red-team-operations.md."),
     ),
    ("concepts/bug-bounty.md", "Bug Bounty", "concept",
        ["responsible-disclosure", "vrp", "platform"],
        ["bug bounty", "hackerone", "bugcrowd", "intigriti", "vrp", "responsible disclosure"],
        ["concepts/web-pentest-methodology.md", "concepts/responsible-disclosure.md",
         "entities/tools/burp-suite.md",
         "sources/bug-bounty-career.md", "sources/bug-bounty-how-to-start.md",
         "sources/complete-bug-bounty-cheat-sheet.md",
         "sources/how-to-report-a-vulnerability-and-generate-its-cve.md",
         "sources/dicas-como-reportar-uma-falha.md",
         "entities/people/joas-a-santos.md"],
        "Five corpus PDFs anchor.",
        ("Bug bounty = formalized public disclosure programs that pay researchers for valid security "
         "findings. Major platforms: HackerOne, Bugcrowd, Intigriti, YesWeHack, Synack (invite-only). "
         "Career-vs-job framing: bounty income is rewarding but volatile; most full-time bounty hunters "
         "specialize (e.g., subdomain-takeover scaling, JS file mining, IDOR-heavy workflows). The "
         "corpus's *Complete Bug Bounty Cheat Sheet.pdf* + *How to report a vulnerability and generate "
         "its CVE.pdf* anchor the reporting-side discipline."),
     ),
    ("concepts/responsible-disclosure.md", "Responsible Disclosure + CVE Process", "concept",
        ["ethics", "disclosure", "cve"],
        ["responsible disclosure", "cvd", "cve", "mitre", "vendor"],
        ["concepts/bug-bounty.md",
         "sources/how-to-report-a-vulnerability-and-generate-its-cve.md",
         "sources/dicas-como-reportar-uma-falha.md",
         "entities/people/joas-a-santos.md"],
        "Anchored by How to report a vulnerability + Dicas como Reportar uma Falha.",
        ("Responsible Disclosure (now usually called Coordinated Vulnerability Disclosure, CVD) is the "
         "process of reporting a vulnerability to the vendor and giving them a reasonable window — "
         "typically 90 days, sometimes extended for complex fixes — before publishing details. CVE "
         "(Common Vulnerabilities and Exposures) IDs are assigned by MITRE or by CNAs (CVE Numbering "
         "Authorities, often the vendor itself). The corpus has a dedicated PDF on the CVE-request "
         "process. Industry norm: report → acknowledge → coordinated disclosure date → CVE assigned "
         "→ vendor patches → researcher publishes write-up. Reporting hygiene matters — PoC clarity, "
         "impact scoring (CVSS), reproduction steps."),
     ),
    ("concepts/cybersecurity-careers.md", "Cybersecurity Careers", "concept",
        ["career", "education"],
        ["career", "cybersecurity job", "certification path", "infosec proeficiency"],
        ["entities/certifications/oscp.md", "entities/certifications/ceh.md",
         "entities/certifications/comptia-security-plus.md", "entities/certifications/crto.md",
         "sources/12-best-career-in-cyber-security-2023.md",
         "sources/carreira-em-cyber-security-jr-ao-especialista.md",
         "sources/cyber-security-career-in-2024.md",
         "sources/cyber-security-career-for-children-pt-1.md",
         "sources/penetration-testing-career-jr-to-specialist.md",
         "sources/blue-e-red-team-mercado-de-trabalho.md",
         "sources/dicas-b-sicas-para-ingressar-no-mercado-de-seguran-a.md",
         "sources/iniciando-sua-carreira-em-pentest.md",
         "sources/red-team-career-tips-1.md",
         "sources/soc-analyst-career.md",
         "sources/starting-your-cybersecurity-career-complete-guide.md",
         "sources/the-complete-guide-for-cyber-security-career.md",
         "sources/the-complete-guide-for-cyber-security-career-english.md",
         "sources/resume-pentest-career-by-joas-a-santos.md",
         "sources/interview-question-tips-pentest-red-team-appsec-and-blue-team.md",
         "sources/infosec-proeficiency-colors.md",
         "sources/enumera-o-de-grupos-de-ti-e-seguran-a-para-tech-recruiters.md",
         "sources/competencias-essenciais-para-liderar-uma-equipe-de-pentest.md",
         "sources/como-gerenciar-um-red-team.md",
         "sources/cybersec-certifications-2023.md",
         "sources/certifications-preparation-guide.md",
         "sources/offsec-certification-and-courses-2024.md",
         "sources/offensive-security-materials-for-studies-and-certifications.md",
         "sources/offensive-security-professional-overview-survival.md",
         "sources/plano-de-estudos-cyber-security-parte-1-red-team.md",
         "sources/roadmap-seguran-a-da-informa-o-pt-1.md",
         "entities/people/joas-a-santos.md"],
        "30+ corpus PDFs explicitly scope into career / education / certification roadmaps — the largest single sub-collection alongside Red Team Ops.",
        ("Cybersecurity careers split coarsely into Red (offensive — pentest / red team / bug bounty / "
         "exploit-dev), Blue (defensive — SOC / IR / threat hunting / detection engineering), Purple "
         "(both), GRC (governance / risk / compliance), and adjacent (DevSecOps, AppSec, cloud security "
         "engineering, security architect). The *INFOSEC PROEFICIENCY COLORS.pdf* covers the color "
         "taxonomy. Typical entry paths: Tier-1 SOC analyst → Tier-2 SOC → IR → threat hunting (Blue "
         "lane); IT helpdesk → junior pentester → mid pentester → red team operator (Red lane). The "
         "corpus's strongest theme is **career mapping for Brazilian + Latin-American context** "
         "(employer expectations, R$-denominated salary baselines, local cert acceptance). See "
         "@entities/certifications/* for the cert ladder."),
     ),
    ("concepts/container-security.md", "Container + Kubernetes Security", "concept",
        ["container", "k8s", "cloud-native"],
        ["container", "docker", "kubernetes", "k8s", "escape"],
        ["concepts/cloud-pentest.md",
         "sources/container-security-overview-pt-1.md",
         "sources/kubernetes-exploitation-introduction-cheatsheet.md",
         "entities/people/joas-a-santos.md"],
        "Two corpus PDFs anchor (Container Security Overview + Kubernetes Exploitation Cheatsheet).",
        ("Container security = (1) hardening individual containers (image scanning, no privileged "
         "mode, non-root users, read-only FS, capabilities pruning, secrets handling), (2) container "
         "escape research (kernel CVEs, runc/containerd CVEs, namespace abuse, capability escalation), "
         "(3) Kubernetes-specific attacks (kubeconfig leakage, exposed kubelet, pod-spec abuse for "
         "lateral movement, namespace boundary breaks, RBAC misconfigurations, etcd access). "
         "Standard tools: kube-hunter, kube-bench, peirates, kubectl-who-can, Pacu (k8s extensions)."),
     ),
    ("concepts/anonymity-networks.md", "Anonymity Networks (Tor / I2P)", "concept",
        ["anonymity", "privacy", "tor"],
        ["tor", "onion routing", "anonymity", "dark web", "i2p"],
        ["concepts/osint-for-cybersecurity.md",
         "sources/the-onion-router-overview-pt-1.md",
         "entities/people/joas-a-santos.md"],
        "Anchored by The Onion Router - Overview PT 1.pdf.",
        ("Tor (The Onion Router) is the most widely used anonymity network. Each request is wrapped "
         "in three layers of encryption + routed through three relay nodes (entry / middle / exit), "
         "each peeling one layer — neither any single relay nor any single observer sees both source "
         "+ destination. **Tor is not magic anonymity**: traffic correlation attacks (NetFlow + "
         "timing) work against under-resourced attackers; misuse (logging in to identity-tied accounts "
         "over Tor) defeats the design; many onion services have been deanonymized through OPSEC "
         "mistakes by their operators (FBI v. Silk Road etc.). For cybersecurity investigators: Tor "
         "browser in a VM for dark-web OSINT, never copy-paste anything identifying."),
     ),
    ("concepts/cyberwarfare.md", "Cyberwarfare", "concept",
        ["nation-state", "geopolitics", "strategy"],
        ["cyberwarfare", "nation state", "apt", "cyber operations"],
        ["entities/threat-actors/apt28.md", "concepts/red-team-operations.md",
         "concepts/adversary-emulation.md",
         "sources/cyberwarfare-books-1.md",
         "entities/people/joas-a-santos.md"],
        "Anchored by cyberwarfare books #1.pdf.",
        ("Cyberwarfare = nation-state use of cyber operations as a strategic instrument. Covers "
         "espionage (intelligence collection — APTs), sabotage (Stuxnet, NotPetya, Industroyer), "
         "influence operations (information warfare overlapping with cybersecurity but distinct), "
         "and the doctrinal / legal questions (Tallinn Manual, application of LOAC to cyber, "
         "attribution challenges). Adjacent reading anchors live in the threat-actor profiles."),
     ),
    ("concepts/ai-for-cybersecurity.md", "AI / ChatGPT for Cybersecurity", "concept",
        ["ai", "llm", "chatgpt", "automation"],
        ["chatgpt", "ai", "llm", "security automation"],
        ["concepts/red-team-operations.md", "concepts/soc-operations.md",
         "sources/chatgpt-for-cybersecurity-1.md",
         "sources/chatgpt-for-cybersecurity-2.md",
         "sources/chatgpt-for-cybersecurity-3.md",
         "sources/chatgpt-for-cybersecurity-4.md",
         "entities/people/joas-a-santos.md"],
        "Four-PDF series anchors this.",
        ("LLMs (ChatGPT, Claude, Gemini, local Llama / Mistral) have become daily tools across both "
         "offensive + defensive workflows: payload obfuscation drafts, regex generation for SIEM "
         "rules, IR write-up first-drafts, vulnerability triage assistance, code review of "
         "newly-disclosed PoCs, OSINT pivot suggestion. Caveats: prompt-injection risk in agentic "
         "workflows (especially if the LLM is reading attacker-controlled content), hallucination "
         "in technical references (always verify CVE IDs / GitHub URLs), and confidentiality (don't "
         "paste customer data into hosted LLMs without contractual cover). [NEEDS VERIFICATION 2026-05-12]"),
     ),
    ("concepts/blockchain-security.md", "Blockchain + Smart Contract Security", "concept",
        ["blockchain", "smart-contract", "web3"],
        ["blockchain", "smart contract", "solidity", "evm", "defi"],
        ["concepts/web-pentest-methodology.md",
         "sources/blockchain-and-smart-contract-testing-security.md",
         "sources/smart-contract-security-overview-pt-1.md",
         "entities/people/joas-a-santos.md"],
        "Two corpus PDFs anchor.",
        ("Smart-contract security focuses on bytecode (typically EVM — Solidity / Vyper) deployed "
         "to public chains. Standard bug classes: reentrancy (DAO 2016), integer overflow/underflow "
         "(pre-Solidity 0.8 era), front-running / MEV, oracle manipulation, access-control "
         "mistakes (missing onlyOwner), upgradability proxy bugs, signature malleability. Tools: "
         "Slither, Mythril, Echidna (fuzzing), Foundry (test framework). Audit firms: OpenZeppelin, "
         "Trail of Bits, ConsenSys Diligence. DeFi-specific risks add: liquidity-pool drain via "
         "flash loans, governance-token capture."),
     ),
    ("concepts/game-hacking.md", "Game Hacking + Anti-Cheat Bypass", "concept",
        ["game-hacking", "reverse-engineering", "anti-cheat"],
        ["game hacking", "cheat engine", "anti-cheat", "anticheat", "vac", "battleye", "easy anticheat"],
        ["concepts/malware-analysis.md", "entities/programming-languages/c.md",
         "sources/game-hacking-1-anti-cheat-bypass.md", "entities/people/joas-a-santos.md"],
        "Anchored by Game Hacking 1 - Anti Cheat BYPASS.pdf.",
        ("Game-hacking is a niche but technically dense subdomain — overlaps heavily with reverse "
         "engineering + Windows internals + memory manipulation + driver development. Anti-cheats "
         "(BattlEye, Easy Anti-Cheat, Vanguard, FACEIT-AC, VAC) increasingly run as kernel-mode "
         "drivers, making naive user-mode cheats easy to detect; modern cheat developers respond "
         "with their own kernel drivers + DKOM techniques + hardware-level isolation (DMA cheats "
         "via PCIe FPGAs). Standard learning track: Cheat Engine + ReClass for first cheats → "
         "manual driver development → kernel-mode cheats. Legality varies by jurisdiction; this "
         "concept is most useful as **reverse-engineering practice**, not as a serious career path."),
     ),
    ("concepts/metaverse-security.md", "Metaverse Security", "concept",
        ["metaverse", "vr", "ar", "novel-surface"],
        ["metaverse", "vr", "ar", "horizon worlds", "vrchat"],
        ["concepts/web-pentest-methodology.md", "concepts/blockchain-security.md",
         "sources/cybersecurity-flaws-in-the-metaverse-1.md",
         "sources/metaverso-e-a-inova-o-tecnol-gica.md",
         "entities/people/joas-a-santos.md"],
        "Two corpus PDFs anchor.",
        ("Speculative-but-real attack surface as immersive platforms (Meta Horizon, VRChat, "
         "Roblox-as-platform, Decentraland) gain users. Risks: identity / avatar impersonation, "
         "voice-deepfake harassment, virtual-property theft (often via NFT bridges), "
         "child-safety incidents in unmoderated rooms (overlaps with @concepts/cyber-for-kids.md), "
         "novel payment/payment-fraud paths (overlapping with @concepts/blockchain-security.md). "
         "[NEEDS VERIFICATION 2026-05-12]"),
     ),
    ("concepts/zero-trust.md", "Zero Trust", "concept",
        ["architecture", "defense"],
        ["zero trust", "ztna", "beyondcorp", "microsegmentation"],
        ["concepts/network-security.md", "concepts/soc-operations.md",
         "sources/zero-trust-testing-checklist.md", "entities/people/joas-a-santos.md"],
        "Anchored by Zero Trust Testing Checklist.pdf.",
        ("Zero Trust = an architectural philosophy: **never trust, always verify** — every request "
         "is authenticated + authorized regardless of network position. Core tenets (per NIST "
         "SP 800-207): explicit verification, least privilege, assume breach. Implementations: "
         "BeyondCorp (Google's original), Zscaler ZTNA, Cloudflare Access, Tailscale (WireGuard-"
         "based). Testing a Zero Trust deployment: identity-spoofing attempts across federations, "
         "MFA-bypass attempts, conditional-access policy edge cases, posture-check evasion, "
         "service-mesh policy enforcement."),
     ),
]

for rel_path, title, page_type, tags, keywords, related, raw_concept, narrative in STUBS:
    write_page(
        rel_path,
        title,
        page_type,
        tags=tags,
        keywords=keywords,
        related=related,
        maturity="draft",
        raw_concept=raw_concept,
        narrative=narrative,
    )

print("All entity + concept pages written.")
