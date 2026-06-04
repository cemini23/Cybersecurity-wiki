# Cybersecurity Wiki — Operations Log

Append-only chronological log of ingests, queries, and lint passes. Newest entries at the bottom.

---

## [2026-05-12] scaffold | Workspace bootstrapped from SEO wiki-template

- Forked `wiki-template/` to `~/Desktop/projects/Cybersecurity wiki/`
- Adapted `CLAUDE.md` for cybersecurity-vertical scope: offensive security + defensive operations + career/education
- Created entity subfolders: certifications, tools, frameworks, threat-actors, platforms, people, vendors, programming-languages
- Wrote README, ROADMAP, LESSONS, LICENSE, hot.md
- Added `Related Wikis` table linking `osint-wiki`, `image-gen-wiki`, `seo-wiki`, `3d-printing-wiki`
- Added cybersecurity-specific `Hands-on rules — ethics + legality` block (authorization, responsible disclosure, dual-use tools, kid-safety framing)

## [2026-05-12] ingest | Joas A Santos cybersecurity PDF corpus (227 PDFs)

- **Source**: shared Google Drive folder `ebooks Joas` (folder ID `12Mvq6kE2HJDwN2CZhEGWizyWt87YunkU`, owner joasantonio108@gmail.com)
- **Author**: Joas A Santos (Brazilian cybersecurity educator, Red Team Leader). LinkedIn: [joas-antonio-dos-santos](https://www.linkedin.com/in/joas-antonio-dos-santos/). GitHub: [CyberSecurityUP](https://github.com/CyberSecurityUP).
- **Method**: Drive API `parentId` query returned empty for shared folders, so contents were enumerated via Playwright DOM scrape (`[data-id]` attributes + tooltip-derived titles). Full inventory persisted to `.scratch/drive_inventory.tsv`
- **Pages touched** — 50+ entities/concepts + 226 source stubs:
  - **226 source stubs** generated via `scripts/build_source_stubs.py` (frontmatter + Drive file-ID provenance + read_status=unread-stub)
  - **2 validated frameworks**: MITRE ATT&CK (full deep-read from `Mitre Att&ck Study Overview.pdf`), Cyber Kill Chain (Unified Cyber Kill Chain content from `Red Team Operations – Concepts #1.pdf`)
  - **8 tool entities**: Cobalt Strike, Metasploit, Burp Suite, Caldera, Maltego, Wazuh, Nmap, BloodHound
  - **10 certification entities**: OSCP, OSWA, OSWE, CRTO, CEH, CompTIA Security+/PenTest+, eCPPT/eCPTX/eWPT
  - **5 vendor entities**: Offensive Security, eLearnSecurity, CompTIA, EC-Council, Zero-Point Security
  - **1 platform**: HackTheBox
  - **1 person**: Joas A Santos (anchor for the entire source corpus)
  - **1 threat actor**: APT28 (only named APT in the corpus)
  - **4 programming language entities**: Python, C/C++, JavaScript, PowerShell — all security-focused
  - **5 validated concepts**: Red Team Operations, Adversary Emulation, AV/EDR Bypass, Web Pentest Methodology, OSINT for Cybersecurity
  - **20+ draft concepts**: SOC Operations, Incident Response, Threat Hunting, Malware Analysis, Exploit Development, Cyber for Kids, Social Engineering, Windows Pentest, Privilege Escalation, Cloud Pentest, Mobile Pentest, Network Security, Container Security, Bug Bounty, Responsible Disclosure, Cybersecurity Careers, Anonymity Networks, Cyberwarfare, AI for Cybersecurity, Blockchain Security, Metaverse Security, Game Hacking, Zero Trust, Purple Team Operations
- **Deep-reads (anchor pages)**: 4 PDFs fully ingested:
  1. `Mitre Att&ck Study Overview.pdf` → @entities/frameworks/mitre-attack.md
  2. `Red Team Operations – Concepts #1.pdf` → @concepts/red-team-operations.md + @entities/frameworks/cyber-kill-chain.md + @concepts/adversary-emulation.md
  3. `AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf` → @concepts/av-edr-bypass.md
  4. `Web PenTesting Checklist by Joas.pdf` → @concepts/web-pentest-methodology.md
- **Cross-wiki backlinks** added: web-pentest-methodology references `@seo-wiki/concepts/web-vitals.md`; osint-for-cybersecurity references `@osint-wiki/concepts/typed-relation-dependencies.md`
- **Read status**: 4 sources `deep-read`, 222 sources `unread-stub` (titles + provenance only; deep-read deferred to future sessions per the ROADMAP)
- **Maturity at write time**: 8 pages `validated` (5 concept + 2 framework + 1 person), 47 pages `draft` (will mature with future ingests + corpus deep-reads)

## [2026-05-12] cross-link | added cybersecurity-wiki backlinks to 4 sibling wikis

- Updated `osint-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `image-gen-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `seo-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `3d-printing-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row

## [2026-05-12] follow-ups | post-publication fixes + content expansion

- **Lint orphan fix**: improved `scripts/fix_wiki_refs.py` (3 passes, idempotent) — fixed the bidirectional-fix bug where `set_related()` failed to recognize one-space-indented `- foo` YAML list items. Result: orphans went 41 → 0, bidirectional gaps 0, dangling refs 0.
- **Deep-reads (3 more PDFs)** — upgraded the following from `draft` → `validated`:
  - `Linux Privilege Escalation – Overview.pdf` → @concepts/privilege-escalation.md (11 Linux privesc technique categories + enumeration script inventory + Windows privesc + community references)
  - `Incident response - overview.pdf` → @concepts/incident-response.md (NIST SP 800-61r2 + SANS PICERL + SOC-vs-CSIRT + DFIR tooling)
  - `INFOSEC PROEFICIENCY COLORS.pdf` → @concepts/cybersecurity-careers.md (the color taxonomy — Red/Blue/Purple/Yellow/Green/White/Orange teams, lane→role mapping, cert ladder by lane)
- **New threat-actor pages** (3): @entities/threat-actors/apt29.md (Cozy Bear / SVR), @entities/threat-actors/lazarus.md (DPRK), @entities/threat-actors/lockbit.md (RaaS criminal). Threat-actor coverage now 4 pages, spans state + criminal axes.
- **Cross-wiki fix**: replaced dangling `@seo-wiki/concepts/web-vitals.md` (page doesn't exist in SEO wiki) with `@seo-wiki/concepts/local-seo-foundations.md` (verified to exist). Cross-wiki dangling: 0.
- **Maturity counts after follow-up**: 11 pages `validated` (5 + 3 upgraded concepts + 2 framework + 1 person), 50 pages `draft`, 226 source stubs `draft + unread-stub`.
- Updated `image-gen-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `seo-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `3d-printing-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row

## [2026-05-12] lint | full maintenance pass — wiki green across all 8 checks

- Ran `scripts/wiki_lint.py` against the 290-page corpus. Three latent issues surfaced:
  1. **CLAUDE.md OSINT-wiki path was wrong** — `../../Desktop/OSINT WORKSPACE/wiki/` resolved with an extra `Desktop/` segment. Corrected to `../../OSINT WORKSPACE/wiki/`. This unblocks the lint's cross-wiki resolver for every `@osint-wiki/...` reference.
  2. **Double-`@` typo** in @concepts/osint-for-cybersecurity.md `## Relations` block — `@@osint-wiki/concepts/typed-relation-dependencies.md` corrected to `@osint-wiki/...`. The lint regex was matching at offset 1, dropping the cross-wiki alias context.
  3. **Trailing-period boundary bug** in @concepts/osint-for-cybersecurity.md narrative — a sentence ended with `...typed-relation-dependencies.md.`, and the cross-wiki regex greedily captured the trailing dot. Rewrote the sentence so the reference sits mid-sentence.
- **Lint result (all 8 checks clean):** 0 orphans, 0 bidirectional gaps, 0 dangling related links, 0 missing @path body mentions, 0 frontmatter quality issues, 0 stale `[NEEDS VERIFICATION]` tags, 0 dangling cross-wiki refs (4 cross-wiki refs all resolve).
- **Remaining "issues" that are by design**, not bugs: 226 cited unread-stub source pages (the deep-read pipeline backlog) and 20 thin concept pages (<100 narrative words) awaiting source-driven expansion. Both tracked in `ROADMAP.md`.

## [2026-05-13] adoption | Phase-1 deep-dives — 4 K42-routed tools + LLM-security concept buildout

Adopted the 4 GO / CONDITIONAL-GO tools that the 2026-05-13 K42 multi-wiki cross-routing audit identified as cybersecurity-wiki-relevant. The 4 corresponding briefs in `briefs/` (cua, fuzzyai, pentest-ai-agents, pydns-scanner) have been actioned with full Phase-1 implementation.

**10 new pages created:**

Entity pages (4):
- @entities/tools/cua.md — Apple Virtualization.Framework + Lume agent-VM sandbox (FOSS, agent-action tracing). Cross-wiki backlink to @osint-wiki/entities/tools/cua.md.
- @entities/tools/fuzzyai.md — CyberArk's LLM adversarial fuzz framework (Apache-2.0, 18 attack methods including PAIR + Crescendo). Cross-wiki backlink to @osint-wiki/entities/tools/fuzzyai.md.
- @entities/tools/pentest-ai-agents.md — 0xSteph LLM-driven red-team automation (MIT, 1100+ stars, v3.2). Documents the Tier 1 / Tier 2 scope-enforcement model.
- @entities/tools/pydns-scanner.md — xullexer DNS server discovery tool (MIT, 337 stars). Includes mandatory `## Ethical use` section (Phase-1 conditional-GO requirement from K42 evaluation).

Concept pages (6):
- @concepts/agent-vm-sandboxing.md — 3-property methodology (disposable VM substrate / agent-action tracing / explicit isolation boundary). Anchors cua.
- @concepts/llm-adversarial-fuzzing.md — Umbrella methodology distinguishing prompt injection / jailbreak / adversarial fuzzing.
- @concepts/pair-prompt-pattern.md — PAIR single-turn jailbreak (arXiv 2310.08419, Chao et al. 2023).
- @concepts/crescendo-multi-turn-jailbreak.md — Multi-turn escalation attack (arXiv 2404.01833, Russinovich et al. 2024).
- @concepts/llm-pentest-automation.md — Tier 1/2 model + scope-enforcement + findings JSON schema. Anchors pentest-ai-agents.
- @concepts/dns-server-discovery-vs-subdomain-enumeration.md — Recon-discipline distinction. Prevents pydns-scanner misuse (it does *not* enumerate subdomains; it discovers DNS servers).

**17 existing pages updated with bidirectional backlinks** — frontmatter `related:` + body `## Relations` block edits to maintain the wiki's bidirectional invariant. Pages touched: red-team-operations, exploit-development, incident-response, malware-analysis, av-edr-bypass, ai-for-cybersecurity, llm-vulnerability-discovery, social-engineering, responsible-disclosure, bug-bounty, cybersecurity-careers, network-security, osint-for-cybersecurity, web-pentest-methodology, bloodhound, metasploit, nmap. All bumped `updated:` to 2026-05-13.

**Source memory anchors** (from 2026-05-13 K42 audit and follow-up evaluations):
- Obs #507 — K42 multi-wiki cross-routing audit (15 tools flagged for cybersec ingest, 4 prioritized here)
- Obs #502, #506, #508, #509 — individual GO/CONDITIONAL-GO decisions for cua / fuzzyai / pentest-ai-agents / pydns-scanner
- Obs #519, #521, #525, #527 — entity page creation events
- Obs #531, #532, #537, #541, #542 — methodology concept page creation events

**Out of scope (Phase-2 candidates):**
- Per-CVE deep-reads of PAIR + Crescendo academic papers — currently we cite arXiv IDs but haven't synthesized the full method descriptions into snippets.
- Lab-validation of pentest-ai-agents Tier-2 mode against a test target — currently `[TENTATIVE]` on the actual operational claims.
- Tooling-stack briefs for Caldera + Atomic Red Team comparisons against pentest-ai-agents — both are LLM-pentest adjacent but not yet evaluated.

## [2026-05-13] cross-wiki route | xullexer/PYDNS-Scanner — async DNS recon (Slipstream + SlipNet)

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/entities/pydns-scanner-xullexer.md (stub)

## [2026-05-13] cross-wiki route | 0xSteph/pentest-ai-agents — shell-only Claude Code subagents for pentest workflows

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/entities/pentest-ai-agents-0xsteph.md (stub)

## [2026-05-14] cross-wiki route | apktool-mcp-server — Android Reverse Engineering via MCP

Cross-wiki stub routed from `@osint-wiki/entities/tools/apktool-mcp-server.md`.
- Created wiki/entities/apktool-mcp-server.md (stub)

## [2026-05-14] cross-wiki route | T-Pot — Multi-Honeypot Deception Framework

Cross-wiki stub routed from `@osint-wiki/entities/tools/tpotce.md`.
- Created wiki/entities/tpotce.md (stub)

## [2026-05-14] cross-wiki route | Decepticon — Autonomous Red-Team Multi-Agent Framework

Cross-wiki stub routed from `@osint-wiki/entities/tools/decepticon.md`.
- Created wiki/entities/decepticon.md (stub)

## [2026-05-15] cross-wiki route | Claude-Red — Offensive Security Skills Library for Claude Code

Cross-wiki stub routed from `@osint-wiki/entities/tools/claude-red-offensive-skills.md`.
- Created wiki/entities/claude-red-offensive-skills.md (stub)

## [2026-05-15] ingest | Redteam Kit — 22 PDFs (shared Drive folder)

- **Source**: Google Drive shared folder [Redteam Kit](https://drive.google.com/drive/folders/1_UR7Kns9v3vIUyPPP0dTGBKdD1JOZupx) (owner hidden, shared 2026-05-15)
- **Contents**: 22 English-language cybersecurity PDFs — books, playbooks, field manuals, and technique references. Distinct corpus from the Joas A Santos (PT-BR/EN) seed corpus.
- **Method**: Enumerated via Playwright DOM snapshot (Drive API search doesn't return shared-folder children). File IDs not captured — Drive API search by title also returns empty for shared files.
- **Pages touched** — 22 source stubs:
  1. `2025-cybersecurity-attacks-playbooks` — SOC/IR playbooks
  2. `cloud-hacking-playbook` — Cloud offensive playbook
  3. `cloud-attack-vectors` — Cloud attack surface reference
  4. `for-red-team-operation` — Red team operations guide
  5. `hacking-the-art-of-exploitation-2nd-edition` — Jon Erickson classic (exploit dev)
  6. `hacking-computer-hacking-security-testing` — Pentest fundamentals
  7. `hacking-mastery-with-kali-linux` — Kali Linux mastery
  8. `hacking-multifactor-authentication` — MFA bypass techniques (new topic area)
  9. `hands-on-hacking` — Practical hacking guide
  10. `network-attacks-and-exploitation` — Network attack/exploitation
  11. `no-starch-press-hacking-apis` — Web API hacking (new topic area)
  12. `offline-bruteforce-wps` — WPS brute-force attacks
  13. `password-cracking-techniques` — Hash cracking techniques
  14. `penetration-testing-with-kali-linux` — Kali pentest guide
  15. `phishing-dark-waters` — Advanced phishing techniques
  16. `practical-redteaming` — Practical red team operations
  17. `red-team-guides` — Red team guides collection
  18. `red-hat-linux-security-and-optimization` — RHEL hardening
  19. `rtfm-red-team-field-manual-v2` — RTFM v2 quick reference
  20. `ssh-hardening-and-offensive-mastery` — SSH hardening + tunneling (new topic area)
  21. `the-hacker-playbook-3-practical` — Peter Kim's Hacker Playbook 3
  22. `window-privilege-escalation-automated-script` — Windows privesc automation
- **Genuine topic gaps filled**: MFA hacking (#8), web API hacking (#11), SSH hardening (#20) — these seed entirely new topic areas with no prior source coverage
- **Kali Linux gap filled**: two Kali-specific sources (#7, #14) — first dedicated Kali source pages despite it being a core pentest platform
- **Read status**: all 22 sources `unread-stub`; deep-read deferred
- **Total wiki size**: 249 source stubs (227 Joas + 22 Redteam Kit), ~54 entity pages, ~31 concept pages, 4 threat-actor pages
- **New concept pages** created to anchor the ingest:
  - `concepts/buffer-overflow.md` — Stack/heap overflow + shellcode fundamentals
  - `concepts/credential-access.md` — MITRE TA0006 credential dumping + password cracking
  - `concepts/linux-pentest.md` — Linux enumeration + privilege escalation
  - `concepts/linux-security.md` — RHEL hardening, SELinux, SSH defense
  - `concepts/phishing.md` — Spear phishing + MFA bypass + infrastructure
  - `concepts/pivoting.md` — Lateral movement + tunneling + port forwarding
  - `concepts/system-hardening.md` — CIS/STIG system hardening frameworks
  - `concepts/wireless-pentest.md` — WiFi/WPS/Bluetooth/RFID attacks
  - `concepts/defense-in-depth.md` — Layered security architecture
- **New entity pages**: `entities/tools/kali-linux.md` (pentest distro), `entities/tools/multi-cloud-red-team.md` (multi-cloud red team ops)
- **Backlinks**: 26 existing pages updated (11 concept + 15 entity/source) to maintain bidirectional invariant
- **Lint state**: 0 new orphans, 0 new bidirectional gaps, 0 new dangling links from this ingest

## [2026-05-15] cross-wiki route | chekusu/mails — AI email parsing, dual-use phishing-domain enumeration

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/concepts/2026-05-13_chekusu-mails-dual-use.md (stub)

## [2026-05-16] cross-wiki route | jadx-mcp-server + osmedeus (OSINT v3 tool-eval)

Two new tool pages cross-routed from the OSINT workspace tool-evaluation ingest (`@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md`), both rated Adopt tier with cybersec as primary-fit wiki.
- New pages: `entities/tools/jadx-mcp-server.md` (Android RE + live debugging via MCP, JADX decompiler), `entities/tools/osmedeus.md` (orchestration engine for security scanning).
- **Backlink wiring** — reciprocal `related:` + Relations entries added to maintain bidirectional invariant:
  - jadx-mcp-server: `concepts/mobile-pentest.md`, `concepts/malware-analysis.md`, `entities/apktool-mcp-server.md` (sibling Android-RE MCP server)
  - osmedeus: `concepts/red-team-operations.md`, `concepts/bug-bounty.md`, `concepts/web-pentest-methodology.md`, `entities/tools/nmap.md` (Osmedeus integrates nmap)
- **Cross-wiki concept backlinks** — two pages now referenced by sibling-wiki tool pages:
  - `concepts/osint-for-cybersecurity.md` → `@osint-wiki/entities/tools/socid-extractor.md` (cross-platform social-account identifier-extraction; threat-actor correlation)
  - `concepts/blockchain-security.md` → `@osint-wiki/entities/tools/polymarket-insider-tracker.md` (Polymarket funding-chain analysis; threat-actor financial profiling)
- **av-edr-bypass reading list** — one catalog-reference line added (APC-routine remote write primitive write-up; Reference-only tier, ETW/telemetry tamper-detection awareness).
- Index updated: 2 new Tools rows. All modified pages bumped to `updated: 2026-05-16`.

## [2026-05-16] phase-0 | K49 Adopt-tier tool audits (jadx-mcp-server, Osmedeus)

Phase-0 clone audits of the 2 cybersec K49 Adopt-tier tools. Verdicts in each entity page's `## Phase-0 Audit` section.

- **jadx-mcp-server → GO.** Apache-2.0 confirmed (verbatim LICENSE). 510 stars, 5 open issues, multi-contributor. No GPL contamination — Python deps permissive; JADX not vendored (talks over MCP to a separate plugin). Mseep.ai audit badge confirmed real.
- **Osmedeus → GO.** MIT confirmed. 6,314 stars, ~8-year project, active multi-contributor (last push 2026-05-11). Go `go.mod` deps all permissive, no copyleft. The cloud runaway-compute concern is resolved — `docs/cloud/` documents `--auto-destroy`, orphan detection, and `max_hourly_spend`/`max_total_spend` ceilings (av-edr-bypass-class concern → `[CONFIRMED]`).

## [2026-05-16] ingest | BlueTeam Kit (26 PDFs) + KALI For 2023 video course

Two shared Google Drive folders ingested. The Drive API still cannot enumerate shared-folder children — the BlueTeam Kit folder was scraped via Playwright for `data-id`s, then each file's title/metadata fetched via `get_file_metadata`.

- **BlueTeam Kit** (`drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs`, owner `cipherphantomofficials@gmail.com`) — 26 PDFs, all defensive / blue-team scope: SOC analyst material (Splunk, QRadar, EDR, threat hunting, IR runbooks), 4 full books (*Next-Gen SOC with IBM QRadar*, *Cybersecurity Blue Team Strategies*, *Effective Threat Investigation for SOC Analysts*, *Open-Source SOC*), and networking/crypto primers (CCNA, Cisco SD-WAN ×2, networking essentials, encryption & hashing). 26 source stubs created (`unread-stub`).
- **2. KALI For 2023** (`drive/folders/1GTheDOkj1I70zzW4CXOZk8ctwIb3dyHN`) — a 50-part Kali Linux video course (`Chapter 1.mp4` … `Chapter 50.mp4`, ~1.8 GB). No per-chapter titles or transcripts; video is not synthesizable into prose. Catalogued as **one** source page (`sources/kali-for-2023-video-course.md`) per user decision — not 50 content-free stubs.
- **4 new entity/concept pages**: `entities/tools/splunk.md`, `entities/tools/qradar.md` (commercial SIEMs — 3 + 2 corpus PDFs respectively); `concepts/siem.md` (no dedicated SIEM page existed despite a SIEM-heavy corpus); `concepts/endpoint-detection-response.md` (defensive counterpart to the existing offensive `av-edr-bypass.md`).
- **Backlinks** — 15 existing pages patched to hold the bidirectional invariant: `soc-operations` (+25), `threat-hunting` (+10), `incident-response` (+9), `network-security` (+7), `defense-in-depth`, `malware-analysis`, `linux-security`, `purple-team-operations`, `adversary-emulation`, `cybersecurity-careers`, `osint-for-cybersecurity`, `av-edr-bypass`, `entities/tools/wazuh`, `entities/tools/kali-linux`, `entities/frameworks/mitre-attack`. All bumped to `updated: 2026-05-16`.
- Index updated: 2 new Defensive-concept rows, 2 new Tools rows, Sources count 249→275 (and the prior Joas miscount 227→226 corrected per `hot.md`).
- Source total: 248 → 275.

## [2026-05-17] deep-read | Threat Hunting 101 (LogRhythm, R. F. Smith) — promoted concepts/threat-hunting.md draft → validated

First BlueTeam Kit deep-read. The LogRhythm white paper provides an 8-hunt structural skeleton (process / behavior / scripting / AV-follow-up / persistence / lateral-movement / DNS / honeypot), each anchored to specific Windows Event IDs or Sysmon event classes — exactly the scaffolding the existing one-paragraph threat-hunting concept page was missing.

- **`sources/threat-hunting-101.md`**: `unread-stub` → `read`; full Narrative with the 8-hunt summary + per-hunt log-source mapping; `## Snippets` extracting the Lucene/SQL baseline queries + Windows Event ID tables + DNS-rebinding mechanism; `## Dead Ends` for hash-only whitelisting + WSH auditing.
- **`concepts/threat-hunting.md`**: `draft` → `validated`. Added Pyramid-of-Pain mental model, log-substrate prerequisites, full 8-hunt catalog with MITRE ATT&CK tactic mapping, hunt-program maturity ladder, Snippets, Dead Ends.
- **NEW `entities/tools/sysmon.md`** (draft): no Sysmon page existed despite every BlueTeam Kit threat-hunt source assuming Sysmon is deployed. Documents the 10 highest-value event IDs (1, 3, 7, 8, 10, 11, 12-14, 19-21, 22, 25), SwiftOnSecurity + sysmon-modular configs (last-validated marked `[NEEDS VERIFICATION 2026-05-17]`), defense-stack positioning (above default Security Log, below commercial EDR, default FOSS-SOC sensor), and operational pitfalls (config noise, no self-tamper-protection).
- **Backlinks** (bidirectional invariant held): added `sysmon.md` ↔ `concepts/siem.md`, `concepts/soc-operations.md`, `concepts/endpoint-detection-response.md`, `entities/frameworks/mitre-attack.md`, `sources/effective-threat-investigation-soc-analysts.md`, `sources/blue-team-handbook.md`, `sources/open-source-soc-guide.md`. Added `concepts/threat-hunting.md` ↔ `concepts/endpoint-detection-response.md` (was missing).
- **Index updated**: new Tools row for Sysmon; `concepts/threat-hunting.md` maturity bumped draft → validated.
- Source `read-status`: `unread-stub` count: 275 → 274 (`threat-hunting-101.md` now `read`).

## [2026-05-17] deep-read | Ransomware Investigation Runbook (Kumar Bineet Ranjan) — new concepts/ransomware.md (validated)

Second BlueTeam Kit deep-read. 15-section SOC playbook (triage → collect → query → process review → TP/FP score → contain + recover); concrete enough to warrant a dedicated concept page rather than just inlining the takeaways into `incident-response.md`.

- **`sources/ransomware-investigation-runbook.md`**: `unread-stub` → `read`; full Narrative (15-section summary), `## Snippets` (TP/FP scoring rubric, VSS-deletion commands, Splunk mass-write + encoded-PowerShell queries, ransom-note filename catalog, certutil LOLBin pattern, encrypted-extension catalog), Dead Ends (entropy as sole signal, power-off destroys evidence, PowerShell-alone false-positive rate).
- **NEW `concepts/ransomware.md`** (validated): defensive-operations synthesis. Kill-chain → defender-signal mapping table, RaaS + double/triple/quad extortion landscape, the canonical VSS-deletion detection, full TP/FP scoring rubric, 10-step play sequence, recovery rules (no-pay default, backup hygiene, krbtgt double-rotation, breach-notification clock), LOLBin reference table (12 binaries × normal/misuse/detection-cue).
- **Backlinks** (bidirectional invariant held): added `concepts/ransomware.md` ↔ `incident-response`, `malware-analysis`, `soc-operations`, `threat-hunting`, `endpoint-detection-response`, `entities/tools/sysmon`, `entities/threat-actors/lockbit`, `entities/frameworks/mitre-attack`, `sources/ransomware-investigation-runbook`, `sources/ransomware-investigation-osint-and-hunting-overview-pt1`, `sources/2025-cybersecurity-attacks-playbooks`.
- **Index updated**: new Doctrine + methodology row for `concepts/ransomware.md` (validated).
- Source `read-status`: `unread-stub` count: 274 → 273 (`ransomware-investigation-runbook.md` now `read`).

## [2026-05-17] partial-ingest | Open-Source SOC (Basta et al., Wiley 2025) — Ch 1-2 extracted, Ch 4-15 deferred

Third BlueTeam Kit deep-read attempt — and a partial. The 6.2 MB PDF exceeds direct-read token limits; subagent extraction surfaced Ch 1-2 + partial Ch 3 only. Ch 4-15 body text was not extractable in the response stream. Honest path: ingest what was readable, document the gap, defer the rest.

- **`sources/open-source-soc-guide.md`**: `unread-stub` → `skimmed` (NOT `read`); Narrative expanded with Ch 1-2 content (5 pillars, 3 SOC operating models, alert-volume math, Cyber Kill Chain 7-stage, three-tier threat-intel typology, 76% zero-trust adoption stat), 7 verbatim Snippets quotes from Basta et al., Dead Ends section documenting the extraction gap + `[NEEDS VERIFICATION 2026-05-17]` flag for Ch 4-15. Pages estimated ~400+; author Basta/Basta/Anwar/Essar, Wiley 2025.
- **NEW `concepts/threat-intelligence.md`** (validated): the wiki had no dedicated CTI page despite >15 pages referencing CTI concepts. Sourced from Ch 2 of the Basta book. Three-tier (strategic/tactical/operational) typology + source taxonomy (OSINT / commercial / ISAC / gov / internal) + 5-step intel lifecycle + tooling stack (MISP / OpenCTI / TheHive / Cortex / Yeti / TAXII) + CTI-in-the-SOC integration points + 4 common pitfalls. Links to all four corpus threat-actor pages (APT28, APT29, Lazarus, LockBit) + MITRE ATT&CK + Cyber Kill Chain.
- **`concepts/soc-operations.md`** promoted `draft` → `validated`: extended Narrative with the 5-pillar framework table (people/processes/technology/governance/data), 3 SOC operating models (in-house/co-managed/MSSP) + 7 decision criteria, alert-volume reality (20k endpoints → 500k alerts/day; 1k/analyst/day → 10 real), Cyber Kill Chain 7-stage defender-signal mapping table, zero-trust adoption signal.
- **Backlinks** (bidirectional invariant held — lint passed 0 gaps): added `concepts/threat-intelligence.md` ↔ `soc-operations`, `threat-hunting`, `incident-response`, `osint-for-cybersecurity`, `adversary-emulation`, `ransomware`, `entities/frameworks/mitre-attack`, `entities/frameworks/cyber-kill-chain`, `entities/threat-actors/apt28`, `entities/threat-actors/apt29`, `entities/threat-actors/lazarus`, `entities/threat-actors/lockbit`. Added `cyber-kill-chain` ↔ `soc-operations`, `open-source-soc-guide`. Added `zero-trust` ↔ `open-source-soc-guide`. Added `mitre-attack` ↔ `open-source-soc-guide`.
- **Index updated**: new Doctrine + methodology row for `concepts/threat-intelligence.md` (validated); `concepts/soc-operations.md` maturity bumped draft → validated.
- Source `read-status`: `unread-stub` count: 273 → 272 (`open-source-soc-guide.md` now `skimmed`).

## [2026-05-17] partial-ingest | Effective Threat Investigation for SOC Analysts (Yahia, Packt 2023) — Ch 1-3 extracted, Ch 4-15 deferred

Fourth BlueTeam Kit deep-read — second partial. The 13.3 MB PDF (~280 pages, file ID `19kYHrfybBmTgrwUrPlUjcNdByhD0AGq9`) was delegated to a general-purpose subagent for chunked extraction; subagent confirmed Ch 1-3 extractable, Ch 4-15 body text (Windows Event ID tables, NTLM/Kerberos Event IDs pp. 71-72, firewall/proxy/DNS field tables) collapsed into a bare hyperlink/index dump beyond Ch 4 paragraph 1. Honest path: same partial-ingest pattern as the Basta SOC guide — promote source to `skimmed`, create only the concept pages whose chapter content was readable, defer the Windows-event-log / firewall / proxy / DNS tunneling / C2 / WAF / sandbox concept pages until re-extraction via `pdftotext -layout`.

- **`sources/effective-threat-investigation-soc-analysts.md`**: `unread-stub` → `skimmed` (NOT `read`); Narrative expanded with Ch 1-3 content (email phishing taxonomy + sandbox evasion + 5-sub-investigation workflow + SPF/DKIM/DMARC trio + Windows event-log defaults + Windows 11 336-log-file count + 6 Security event categories). 12 verbatim Snippets quotes from Yahia (Ch 1 phishing-prevalence stat, ISO-file evasion, sandbox sleep tactic, Yahia keyword catalog; Ch 2 MUA/MSA/MTA flow, Return-Path validation; Ch 3 default log path, 336-log count). Dead Ends section documenting the extraction gap + `[NEEDS VERIFICATION 2026-05-17]` flag for Ch 4-15. Adoption-decisions section lists 4 changes adopted now + 9 concept pages deferred.
- **NEW `concepts/phishing-investigation.md`** (validated): SOC-analyst phishing-triage workflow — the wiki had `concepts/phishing.md` (offensive perspective) but no defensive-investigation counterpart despite Yahia Ch 1-2 dedicating ~50 pages to it. Email-threat taxonomy table (spearphishing-attachment / spearphishing-link / BEC / blackmail), attacker email-security evasion tradecraft table, common phishing subject/filename keyword catalog, Yahia's 5-sub-investigation workflow (sender reputation → spoofing validation → sender behavior → subject/filename → content/URL/attachment), SPF qualifier table + DKIM field table + DMARC field table, investigation tool stack (MxToolbox, Talos, URLscan, VirusTotal, ANY.RUN, CyberChef, AbuseIPDB), triage-outcome handoff table, 5 defender priorities.
- **NEW `entities/people/mostafa-yahia.md`** (draft): author-entity for Mostafa Yahia (Egyptian MSSP SOC lead, GCFA/GCIH/IBM QRadar/CCNA per Packt 2023 front matter — `[NEEDS VERIFICATION 2026-05-17]` for employer / LinkedIn). Mirrors the @entities/people/joas-a-santos.md pattern — defensive-investigation-side anchor (where Joas anchors offensive-side concept pages, Yahia anchors defensive-investigation pages).
- **`concepts/incident-response.md`** extended: added Ch 3 Windows event-log triage toolchain (Event Viewer, PsLogList, Event Log Explorer, EvtxECmd, HELK, Mordor datasets) with cost/use-case table; documented default log path `C:\Windows\System32\winevt\Logs`, registry-relocation key, Windows 11 336-default-log count, 6 Security-log event categories. Added `phishing-investigation` + `mostafa-yahia` backlinks.
- **`concepts/threat-intelligence.md`** extended: added "Canonical SOC-analyst pivot stack" section with the 4 named OSINT-TI pivots from Yahia Ch 14 (VirusTotal / IBM X-Force Exchange / AbuseIPDB / Google) as the Tier-1 first-touch stack before commercial feeds.
- **Backlinks** (bidirectional invariant held): added `concepts/phishing-investigation.md` ↔ `phishing`, `social-engineering`, `incident-response`, `threat-intelligence`, `soc-operations`, `threat-hunting`, `osint-for-cybersecurity`, `entities/people/mostafa-yahia`, `sources/effective-threat-investigation-soc-analysts`. Added `entities/people/mostafa-yahia` ↔ `phishing-investigation`, `soc-operations`, `threat-hunting`, `incident-response`, `effective-threat-investigation-soc-analysts`.
- **Index updated**: new Doctrine + methodology row for `concepts/phishing-investigation.md` (validated); new People row for `entities/people/mostafa-yahia.md` (draft).
- Source `read-status`: `unread-stub` count: 272 → 271 (`effective-threat-investigation-soc-analysts.md` now `skimmed`).
- **Deferred** (extraction-gap follow-up): `concepts/windows-event-log-investigation.md`, `concepts/powershell-attack-detection.md`, `concepts/lateral-movement-detection.md`, `concepts/firewall-log-investigation.md`, `concepts/proxy-log-investigation.md`, `concepts/dns-tunneling.md`, `concepts/c2-detection.md`, `concepts/waf-investigation.md`, `concepts/malware-sandboxing.md` — chapters exist in Yahia's TOC but body text + tables were not extractable.
- **Follow-up tracked**: re-extract Ch 4-15 of Basta et al. via pdftotext + page-range read; only then can `open-source-soc-guide.md` move to `read` + the deferred concept pages (`log-analysis`, `network-traffic-analysis`, `security-analytics-ml`, `insider-threat`) be created.

## [2026-05-17] cross-wiki route | gau + katana + gopacket + openvpn-install (OSINT 56-repo tool eval)

Cross-routed 4 security tools into this wiki from the OSINT-workspace 56-repo multi-wiki tool-evaluation ingest (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). All 4 are cybersec-primary fit; verdicts are doc-level (Phase-0 clone audits still owed before production adoption). All 4 licenses are permissive — clean for the IP sale.

- **NEW `entities/tools/gau.md`** (draft): gau (getallurls), lc/gau, MIT, Go. Multi-provider known-URL discovery — fetches a domain's known URLs from AlienVault OTX, the Wayback Machine, and Common Crawl simultaneously. Passive recon / attack-surface mapping; established in Kali Linux. Tier: **Adopt**.
- **NEW `entities/tools/katana.md`** (draft): katana, projectdiscovery/katana, MIT, Go. Scriptable web crawler with standard HTTP + headless-browser modes; extracts URLs / JS paths / API endpoints from SPA frameworks; Go API (`NewCrawlerOptions`, `ClassifyPage`). ~1,567 commits, enterprise-grade lifecycle controls. Tier: **Adopt**. Fills the headless-browser (G5) gap noted in the cariddi audit.
- **NEW `entities/tools/gopacket.md`** (draft): gopacket, mandiant/gopacket, Apache-2.0, Go. High-performance packet-decoding library (decoding routines in `layers_decoder.go`); ~630 stars, 0 open issues. Tier: **Steal-from** — extract specific decoding logic into bespoke defensive tooling, not deploy whole.
- **NEW `entities/tools/openvpn-install.md`** (draft): openvpn-install, angristan/openvpn-install, Unlicense (public domain), Bash. Single-script secure OpenVPN deployment automation; notable for refined NAT detection + dual-stack DNS resolver handling (`resolvePublicIP()`) + extensive IPv6-routing edge-case handling. Tier: **Steal-from** — extract the IPv6-detection / routing shell snippets, not the monolithic installer.
- **Backlinks** (bidirectional invariant held): `gau` ↔ `concepts/bug-bounty`, `concepts/web-pentest-methodology`, `concepts/osint-for-cybersecurity`, `entities/tools/cariddi`, `entities/tools/katana`. `katana` ↔ `concepts/web-pentest-methodology`, `concepts/bug-bounty`, `entities/tools/cariddi`, `entities/tools/gau`, `entities/tools/osmedeus`. `gopacket` ↔ `concepts/network-security`, `concepts/threat-hunting`, `entities/tools/nmap`. `openvpn-install` ↔ `concepts/network-security`, `concepts/system-hardening`. All 4 backlink `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`.
- **`updated:` bumped** on pre-existing pages touched: `entities/tools/cariddi.md`, `entities/tools/nmap.md`, `concepts/web-pentest-methodology.md`, `concepts/bug-bounty.md`, `concepts/network-security.md`, `concepts/threat-hunting.md`, `concepts/system-hardening.md` (and `osint-for-cybersecurity.md` already at 2026-05-17).
- **Index updated**: 4 new Tools rows.

## [2026-05-17] deep-read | Splunk trio (110-query SPL catalog + SPL command reference + 24 SOC-2 use cases) — full extraction, splunk entity promoted to validated

Fifth BlueTeam Kit deep-read — first **full** extraction (not partial). Three small Splunk PDFs from the BlueTeam Kit Drive folder were read in full via `mcp__claude_ai_Google_Drive__read_file_content`: a community-curated 110-query SPL detection catalog, an alphabetical SPL command reference, and Rajneesh Gupta's 24 SOC-2-mapped SPL use cases. No extraction gap this time — the PDFs are small + structurally repetitive (cheatsheet format), so they fit within the read-stream budget. The `entities/tools/splunk.md` stub gets promoted from 1-paragraph draft to validated entity page with full SPL primer + catalog tables + SOC-2 mapping.

- **`sources/100-splunk-queries-soc-analyst.md`**: `unread-stub` → `read` (validated). Narrative restructured into 9 hunt-class categories (auth 28 / process 18 / lateral 8 / network+C2+exfil 15 / web-app 6 / ransomware 5 / recon+CVE 8 / phishing 3 / data+DDoS+ATO remainder). 5 verbatim Snippets (failed-logins, PowerShell encoded, RDP lateral, DNS tunneling, ransomware shadow-copy deletion).
- **`sources/splunk-commands-reference.md`**: `unread-stub` → `read` (validated). Narrative documents the high-value SPL command subset (search/stats/eval/where/rex/table/sort/dedup/top/timechart/chart/lookup/iplocation/transaction/streamstats/eventstats/join/append/makeresults/inputlookup) and the canonical SPL pipeline shape. 4 Snippets (pipeline canonical, rex named-capture, eventstats annotate, transaction caveat).
- **`sources/splunk-siem-soc2-use-cases.md`**: `unread-stub` → `read` (validated). Narrative maps Gupta's 24 use cases to Trust Service Criteria (CC6.1 Logical Access 13 use cases / CC6.6 Change Management 1 / CC6.7 System Operations 8 / CC6.8 Risk Mitigation 2). 3 Snippets (UC2 brute-force, UC9 exfil, UC21 config-change). Author Gupta noted as named-entity.
- **`entities/tools/splunk.md`**: 1-paragraph stub → validated entity page. Sections: SPL primer with pipeline mental model; Detection-query catalog with 9 hunt-class tables (~50 queries quoted across the rows); SPL command reference (the 20-command high-value subset); SOC 2 use-case mapping table (24 use cases by TSC); Pitfalls + cost discipline; Comparison vs QRadar + Wazuh. 6 verbatim Snippets. Dead Ends section (hash-based detection, join at scale, CVE-string-match, encoded-PowerShell on 4688 alone). Maturity: draft → validated.
- **NEW `entities/people/rajneesh-gupta.md`** (draft): author-entity stub for Rajneesh Gupta (@rajneeshcyber), author of the SOC 2 use-cases PDF. `[NEEDS VERIFICATION 2026-05-17]` for LinkedIn / employer / credentials.
- **Backlinks** (bidirectional invariant held — lint passed 0 gaps): added `entities/tools/splunk.md` ↔ `concepts/threat-hunting`, `concepts/incident-response`, `concepts/endpoint-detection-response`, `concepts/ransomware`, `concepts/phishing-investigation`, `concepts/threat-intelligence`, `entities/frameworks/mitre-attack`, `entities/tools/sysmon`, `sources/effective-threat-investigation-soc-analysts`, `sources/open-source-soc-guide`, `sources/soc-analyst-book`, `entities/people/rajneesh-gupta`. Added `sources/100-splunk-queries-soc-analyst.md` ↔ `incident-response`, `ransomware`, `phishing-investigation`, `mitre-attack`, `sysmon`. Added `sources/splunk-commands-reference.md` ↔ `threat-hunting`. Added `sources/splunk-siem-soc2-use-cases.md` ↔ `incident-response`, `threat-hunting`, `rajneesh-gupta`. Added `rajneesh-gupta` ↔ `siem`, `soc-operations`, `splunk`.
- **Index updated**: `entities/tools/splunk.md` maturity row bumped draft → validated with detailed description. New People row for `entities/people/rajneesh-gupta.md` (draft).
- Source `read-status`: `unread-stub` count: 271 → 268 (3 Splunk source pages now `read`).

## [2026-05-17] partial-ingest | Building a Next-Gen SOC with IBM QRadar (Kothekar, Packt 2023) — Ch 1-4 extracted, Ch 5-12 deferred. Final BlueTeam Kit queue item.

Sixth BlueTeam Kit deep-read — second partial-extraction pattern (matches Basta SOC guide + Yahia SOC textbook). The 126,426-character PDF (file ID `1F6E53JLQJcB88lGcrfa7Q9s68o46bM7j`, located via past-transcript JSONL `tool_use_id` match because Drive `search_files` returns empty for the shared folder) exceeds inline read budget. Subagent delegation surfaced Ch 1-4 in full (~36% body coverage); Ch 5-12 are TOC-summary only. Honest path: write what's extracted, flag what isn't, defer the rest.

- **`sources/next-gen-soc-ibm-qradar.md`**: `unread-stub` → `skimmed` (NOT `read`); Narrative expanded with full author/publisher/ISBN/page-count metadata (Kothekar, Packt 2023, ISBN 978-1-80107-602-9, 12 chapters / 3 parts / ~165 body pages), TOC structure (Part I Foundations / Part II Detection+tuning / Part III Apps+ops), extraction-coverage table marking ✅ vs ⚠️ TOC-only per topic. Next-extraction priority: WinCollect (Ch 12) > rule-wizard+AQL (Ch 5-7).
- **`entities/tools/qradar.md`**: 6-line draft stub → validated entity page. Sections: Architecture overview (Console + N managed-host taxonomy table: EP, EC, FP, QFlow, Data Node, QNI, QRIF, QPCAP, QVM, QRM, App Host, DLC); Console + EP subservices (Tomcat, hostcontext, hostservices, ecs-ec-ingress, ecs-ec, ecs-ep, qflow, accumulator, ariel-proxy/query); Two-database split (Ariel time-series local + Postgres config replicated) with operator-implication framing; Core concepts table (event, flow, log source, DSM, offense, BB, rule, reference set, coalescing, traffic analysis); Ingestion protocols (active vs passive); Flow capture + 64-byte payload foot-gun + Superflow types A/B/C with detection use; Custom Rule Engine kinds (event/flow/common/offense/anomaly/behavioral); One end-to-end CRE example (Linux SSH brute force from Ch 4); EPS/FPM licensing model + 7.4 single-capacity-license transition + sizing math (2 TB/day ≈ 46,296 EPS); Deployment topologies (all-in-one / distributed / HA / DR / Community Edition); Upgrade pitfalls (GlusterFS→DRBD, Patch All UI button); Operator foot-guns (JDBC marker-file, time-zone drift, UDP-514 syslog, App Host mandate for UBA/Watson); Apps + extensions section (TOC-only with `[NEEDS VERIFICATION 2026-05-17]`); Comparison table vs Splunk + Wazuh. 3 verbatim Snippets. Dead Ends section explicitly cataloging the 4 extraction gaps (AQL syntax, rule-writing patterns, UBA/Watson/UCM, WinCollect). Maturity: draft → validated.
- **NEW `entities/people/ashish-m-kothekar.md`** (draft): author-entity stub for Ashish M Kothekar (IBM SWAT/SME path, 16+ years IBM Security threat-management products per book front matter). `[NEEDS VERIFICATION 2026-05-17]` for current employer / LinkedIn / additional publications.
- **Backlinks** (bidirectional invariant held — lint passed 0 gaps): added `entities/tools/qradar.md` ↔ `concepts/threat-hunting`, `concepts/incident-response`, `concepts/endpoint-detection-response`, `entities/tools/sysmon`, `sources/open-source-soc-guide`, `entities/people/ashish-m-kothekar`. Added `sources/next-gen-soc-ibm-qradar.md` ↔ `concepts/threat-hunting`, `concepts/incident-response`, `concepts/endpoint-detection-response`, `entities/tools/splunk`, `entities/tools/wazuh`, `entities/tools/sysmon`. Added `entities/people/ashish-m-kothekar.md` ↔ `concepts/siem`, `concepts/soc-operations`.
- **Index updated**: `entities/tools/qradar.md` maturity row bumped draft → validated with detailed description. New People row for `entities/people/ashish-m-kothekar.md` (draft).
- Source `read-status`: `unread-stub` count: 268 → 267 (`next-gen-soc-ibm-qradar.md` now `skimmed`).
- **BlueTeam Kit deep-read queue: CLEARED.** All 26 BlueTeam Kit PDFs are now either `read` (Splunk trio: 3 PDFs), `skimmed` with extraction-gap documented (Basta SOC, Yahia SOC textbook, Kothekar QRadar: 3 PDFs), or remain at `unread-stub` (20 lower-priority PDFs that weren't part of the targeted deep-read pass for SIEM / threat-hunting / EDR / IR / phishing / SOC-architecture). Next-extraction priorities recorded per partial-ingest entry (Basta Ch 4-15; Yahia Ch 4-15 Windows event tables; Kothekar Ch 12 WinCollect + Ch 5-7 AQL/rule-wizard).

## [2026-05-19] ingest | Python Ethical Hacking MASTERCLASS — Zero to Mastery (video course)

User dropped a Google Drive folder link with no instructions; established pattern → ingest. Folder `1Uc1I973Cg7Mo6j_KYgsHReC0kR9Jq-OM` ("SaleWebDesign.Com-Python-Ethical-Hacking-MASTERCLASS-Zero-Mastery", owner `horahibarish@gmail.com`, created 2023-04-26). Drive API cannot enumerate shared-folder children (known trap) → Playwright scrape of `[data-id]` nodes returned 19 titled section subfolders + 4 marketing `.txt` junk files. Second video course in the corpus (after Kali For 2023) → same handling: video has no transcripts, not synthesizable into prose, catalogued as **one** `unread-stub` source page (per user decision, KALI precedent).

- **NEW `sources/python-ethical-hacking-masterclass.md`** (draft, `unread-stub`): source page for the 19-section video course. Curriculum table — sections 1–11 generic Python language (setup → essentials → control flow → loops → data structures → functions/modules → classes → exceptions → network programming → file I/O); sections 12–19 entry-level ethical hacking (testing lab → Linux CLI → anonymity → information gathering → port scanning → gaining access → maintaining access → wrap-up). Follows the standard recon→scan→exploit→persist kill-chain arc paired with a from-scratch Python primer. Provenance note: folder carries `GET 100% OFF COUPONS.txt` / `SaleWebDesign.Com` marketing artefacts characteristic of a repackaged/pirated paid course — noted for honesty, not endorsed.
- **Backlinks** (bidirectional invariant held): added `sources/python-ethical-hacking-masterclass.md` ↔ `entities/programming-languages/python.md`, `entities/tools/kali-linux.md`, `entities/tools/nmap.md`, `entities/tools/metasploit.md`, `concepts/osint-for-cybersecurity.md`, `concepts/anonymity-networks.md`. 6 pages patched (frontmatter `related:` + body `## Relations`), `updated:` bumped to 2026-05-19 on each.
- **Index updated**: Sources count 275 → 276; the video-course line now reads "**2** video courses" (Kali Linux 2023 + Python Ethical Hacking MASTERCLASS).
- No raw source moved — Drive-only, consistent with the four-folder corpus storage decision.

## [2026-05-21] ingest | Cross-wiki brief triage — 15 briefs inventoried, 11 entity stubs + 31 index entries created

All 15 briefs in `briefs/` triaged: 5 already-ingested (content previously folded into wiki during K42 Phase-1 adoption) + 10 unprocessed cross-wiki routing briefs from OSINT wiki tool evaluations.

**11 new entity stub pages** (Adopt/Steal-from tier):
- `entities/tools/defenseclaw.md` — Cisco AI Defense (Apache-2.0, 654 stars)
- `entities/tools/deepzero.md` — Windows kernel-driver vuln research (MIT, 425 stars)
- `entities/tools/grex.md` — Regex generation for SOC/IR (Apache-2.0, ~8,129 stars)
- `entities/tools/vanguard.md` — Single-binary DFIR toolkit (MIT, ~118 stars)
- `entities/tools/raptor.md` — Claude Code offensive/defensive agent (Steal-from)
- `entities/tools/src-hunter-skill.md` — Claude Code bug-bounty skill (MIT, 305 payloads)
- `entities/tools/bluehood.md` — Bluetooth telemetry monitoring (MIT, 977 stars)
- `entities/tools/super-spr.md` — Zero-trust networking (BSD-3-Clause, 565 stars)
- `entities/tools/reconftw.md` — Apex recon automation (MIT, 7.5k+ stars)
- `entities/tools/evilsocket-audit.md` — 8-stage vuln-discovery agent, Glasswing pattern (MIT, 388 stars)
- `entities/tools/offensive-claude.md` — Claude Code offensive workstation, 25 skill modules

**~31 index-only catalog entries** (Steal-from/Defer/Reference tier) added to `wiki/index.md` under new "Cross-wiki routed tool evaluations" subsection, covering K42 (9 items), K15 (2), K53 (2), K51 (5), K54 (6), K55 (3), K56 (2).

**~18 Reject-tier items** dropped (not catalogued).

**Bidirectional invariant**: 18 existing concept/tool pages received backlinks for new entity stubs. Lint verified: 0 orphans, 0 bidirectional gaps across 422 pages.

**All 15 briefs** marked `processed: 2026-05-21`.

## [2026-05-22] ingest | Cross-wiki brief triage — K55-2 + K57 (2 new briefs)

**K55-2** (`briefs/2026-05-21_k55-2-cybersec-toolset-from-osint-tool-eval.md`): Ran `gh api` license verification on 6 primary-fit entries. Results: `Awesome-Hacking` CC0-1.0, `open-source-web-scanners` Apache-2.0, `jadx-ai-mcp` Apache-2.0, `reconftw` MIT (already `@entities/tools/reconftw.md`), `CF-Hero` and `LLM4Pentest` still no SPDX license.

- **NEW** `@entities/tools/cf-hero.md` (draft, Defer) — Cloudflare origin-IP discovery stub; adoption gated on manual LICENSE audit
- **Updated** `@entities/tools/jadx-mcp-server.md` — K55-2 sibling note for `jadx-ai-mcp`
- **Index**: 5 K55-2 rows in cross-wiki eval table; `cf-hero` row in main Tools table; `LLM4Pentest` tier bumped Reference → Defer with K55-2 cross-ref
- **Backlinks**: `cf-hero` ↔ `web-pentest-methodology`, `osint-for-cybersecurity`, `reconftw`

**K57** (`briefs/2026-05-22_k57-cybersec-tool-eval-rejects-from-osint.md`): Reject-tier methodology reference only — no entity stubs. **4 index rows** added (Galaxy-Bugbounty-Checklist, BugBounty-Recon-Methodology, sqlmap, NoSQLMap). `open-source-web-scanners` already indexed from K55-2 with verified Apache-2.0.

Both briefs marked `processed: 2026-05-22`.

## [2026-05-23] ingest | Cross-wiki brief triage — K60 (1 new brief)

**K60** (`briefs/2026-05-23_k60-cybersec-tool-eval-from-osint.md`): 20-URL OSINT eval; four cybersec-routed items.

- **NEW** `@entities/tools/pentest-ai.md` (draft, CONDITIONAL-GO Phase-0) — `0xSteph/pentest-ai` MCP + `ptai` CLI; MIT verified; distinct from validated `pentest-ai-agents`
- **Updated** `@entities/tools/pentest-ai-agents.md` — sibling cross-link; removed stale "out of scope" wording
- **Index**: 4 K60 rows (KaliGPT Reject/NC, h4cker Reference, pentest-ai entity, NVISO catalog Defer) + main Tools table row for `pentest-ai`
- **Backlinks**: `pentest-ai` ↔ `llm-pentest-automation`, `ai-for-cybersecurity`, `pentest-ai-agents`

No entity stubs for KaliGPT (commercial NC), h4cker (reference catalog), or NVISO catalog (no SPDX).

Brief marked `processed: 2026-05-23`.

## [2026-05-24] ingest | Cross-wiki brief triage — K63 Nidhogg (1 new brief)

**K63** (`briefs/2026-05-24_k63-cybersec-nidhogg-from-osint.md`): `Idov31/Nidhogg` — GPL-3.0 Windows kernel rootkit (~2.4k★). Steal-from tier: DKOM / `ActiveProcessLinks` process-hiding tradecraft for blue-team MITRE mapping; **no binary import**.

- **NEW** `@entities/tools/nidhogg.md` (draft, Steal-from) — defensive tradecraft table + T1014/T1562 anchors; GPL deployment boundary documented
- **Index**: K63 row in cross-wiki eval table + main Tools table row
- **Backlinks**: `nidhogg` ↔ `av-edr-bypass`, `endpoint-detection-response`, `malware-analysis`, `privilege-escalation`, `red-team-operations`, `mitre-attack`

Brief marked `processed: 2026-05-24`.

## [2026-05-26] ingest | Cross-wiki brief triage — K68 (1 new brief)

**K68** (`briefs/2026-05-26_k68-cybersec-tool-eval-from-osint.md`): 22-URL OSINT eval; five cybersec-routed repos.

- **NEW** `@entities/tools/iron-proxy.md` (draft, Adopt-eligible) — egress firewall for untrusted workloads (Apache-2.0)
- **NEW** `@entities/tools/cryptex-oss.md` (draft, Adopt-eligible) — LLM red-team transform/mutator toolkit (MIT, 162 transforms)
- **Index**: 3 Steal-from/Reject rows (facex, centaur, ZishanAdThandar/pentest GPL-3.0)
- **Backlinks**: `iron-proxy` ↔ zero-trust, network-security, defense-in-depth, container-security, agent-vm-sandboxing; `cryptex-oss` ↔ llm-adversarial-fuzzing, ai-for-cybersecurity, fuzzyai

Brief marked `processed: 2026-05-26`.

## [2026-05-27] ingest | Cross-wiki brief triage — K71 (1 new brief)

**K71** (`briefs/2026-05-27_k71-cybersec-tooling-from-osint.md`): 27-URL OSINT eval; two cybersec-routed items — both **index-only**, no entity stubs.

- **Reference**: Hackers-Arise AI enumeration article (methodology only, no code) — complements existing K54 Hackers-Arise MCP log index row
- **Reject**: `blacklanternsecurity/bbot` — AGPL-3.0 confirmed via `gh api`; copyleft poison pill for IP-sale surfaces (same posture as TruffleHog/gitGraber)

**Index**: 2 K71 rows added to cross-wiki eval table.

Brief marked `processed: 2026-05-27`.

## [2026-05-28] ingest | Cross-wiki brief triage — K73 (1 new brief)

**K73** (`briefs/2026-05-28_k73-security-tool-phase0-outcomes.md`): security-tool Phase-0 outcome routing from OSINT wiki.

- **NEW** `@entities/tools/cve-mcp-server.md` (draft, CONDITIONAL-GO) — Apache-2.0 security-intel MCP server for CVE/EPSS/KEV/ATT&CK enrichment in cybersec workstation workflows
- **Reject reiterated**: `blacklanternsecurity/bbot` AGPL-3.0 copyleft posture remains reject for IP-sale-bearing production surfaces (already indexed under K71; now annotated K71,K73)
- **Index**: 1 new K73 row (`cve-mcp-server`) + bbot brief provenance widened to `K71, K73`
- **Backlinks**: `cve-mcp-server` ↔ `threat-intelligence`, `threat-hunting`, `osint-for-cybersecurity`, `incident-response`, `pentest-ai`

Brief marked `processed: 2026-05-28`.

## [2026-05-31] ingest | Cross-wiki brief triage — K88 (1 new brief)

**K88** (`briefs/2026-05-31_k88-skillspector-cybersec-from-osint.md`): skill/MCP supply-chain eval from OSINT wiki.

- **NEW** `@entities/tools/nvidia-skillspector.md` (draft, Adopt) — Apache-2.0 agent/MCP skill supply-chain scanner; LangGraph `skillspector.graph` API; import boundary: cybersec workstation vetting only, no trading-stack integration until Phase-0 lab validation
- **Reference**: `FareedKhan-dev/train-llm-from-scratch` (MIT) — index-only
- **Reject**: `ahegazy0/linux-basics-for-hackers-notes` (no LICENSE); `LHRLAB/Graph-R1` (NC-SA per eval; gh api MIT 2026-05-31 — verify before override)
- **Index**: 1 Tools row + 4 cross-wiki eval rows (Adopt + Reference + 2 Reject)
- **Backlinks**: `nvidia-skillspector` ↔ `ai-for-cybersecurity`, `npm-supply-chain-defense`, `llm-pentest-automation`, `defenseclaw`, `claude-code-ultimate-guide`, `src-hunter-skill`

Brief marked `processed: 2026-05-31`.

## [2026-06-01] ingest | Cross-wiki brief triage — K93 (1 new brief)

**K93** (`briefs/2026-06-01_k93-cybersec-digest-netviz-from-osint.md`): federated daily digest install + netviz Adopt upgrade.

- **Structural**: federated daily digest installed (`scripts/daily_research_digest_run.py`, `daily_research_fetch.py`, `daily_research_config.yaml`, `wiki/sweeps/`, `wiki/meta/daily-research-digest-cadence.md`); LaunchAgent `com.cemini.daily-research-digest.cybersec` written to `~/Library/LaunchAgents/` (not tracked)
- **NEW** `@entities/tools/netviz.md` (draft, Adopt) — `ShadowArcanist/netviz` MIT; upgraded from K53 Steal-from; Phase-0 analyst-laptop only
- **Index**: netviz cross-wiki row upgraded `Steal-from K53` → `Adopt K53, K93` + Tools table row
- **Backlinks**: `netviz` ↔ `osint-for-cybersecurity`, `threat-intelligence`, `red-team-operations`, `maltego`, `bloodhound`, `reconftw`

Brief marked `processed: 2026-06-01`.

## [2026-06-01] ingest | Agent security arXiv cluster (5 PDFs)

**Source**: daily digest inbox — five May 2026 arXiv papers on tool-using agent security.

- **NEW** `@concepts/agent-runtime-guardrails.md` (draft) — synthesizes failure modes (authority confusion, permission laundering, sleeper attack, dual-surface injection) + defenses (ePCA, AIRGuard, ChainCaps) + eval hygiene (AAR, per-surface ASR)
- **NEW** `@entities/tools/airguard.md` (draft, CONDITIONAL-GO) — MIT runtime authority guard; paper arXiv:2605.28914
- **NEW** `@entities/tools/chaincaps.md` (draft, Reference) — MCP composition IFC pattern; paper arXiv:2605.26542
- **5 source pages** (1 deep-read anchor 2605.29251 ePCA guardrail + 4 read): 28914, 26542, 28201, 30454
- **Backlinks**: `agent-runtime-guardrails` ↔ `ai-for-cybersecurity`, `llm-adversarial-fuzzing`, `llm-pentest-automation`, `agent-vm-sandboxing`, `crescendo-multi-turn-jailbreak`, `defenseclaw`, `nvidia-skillspector`, `iron-proxy`, `airguard`, `chaincaps`
- **Raw sources** moved to `raw-sources/`

## [2026-06-02] ingest | Daily digest inbox — 2 agent-security papers

**Source**: AM digest run (`wiki/sweeps/2026-06-02-daily.md`) — ClawHub scanner study + AgentRedBench.

- **NEW** `@sources/arxiv-2606-01494-clawhub-security-signals.md` — VT vs static vs SkillSpector on 67k+ OpenClaw skills
- **NEW** `@sources/arxiv-2606-02240-agentredbench.md` — dynamic redteam + AgentRedGuard for SaaS integrations
- **NEW** `@entities/tools/agentredguard.md` (draft, Reference)
- **Updated** `@concepts/agent-runtime-guardrails.md` — layered skill governance + integration-aware guards
- **Backlinks** `nvidia-skillspector`, `airguard`, `llm-adversarial-fuzzing`, `index.md`
- **Sweep** `2026-06-02-daily.md` marked ingested; PDFs → `raw-sources/`
- **Ops** `~/bin/cemini-daily-research-digest-cybersec` loads `~/.cemini/exa-api-key` + `.env` for LaunchAgent (fixes exit 2 when key missing under launchd)

## [2026-06-04] ingest | Cross-wiki brief K98 — SeClaw agent security eval

**K98** (`briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md`): arXiv:2606.02302 trajectory-aware agent security benchmark.

- **NEW** `@sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md` (read)
- **NEW** `@entities/tools/seclaw-eval.md` (draft, Reference — no LICENSE on GitHub API at Phase-0)
- **Updated** `agent-runtime-guardrails`, `llm-pentest-automation`, `llm-adversarial-fuzzing`, `index.md`
- **Backlinks** OSINT `@osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md` + `@osint-wiki/concepts/seclaw-agent-security-evaluation.md`
- **PDF** → `raw-sources/arxiv-2606.02302-seclaw-spec-driven-security-task-synthesis-for-e.pdf`
- Brief marked processed 2026-06-04

## [2026-06-04] ingest | Daily digest — OWASP LLM defense attribution (arXiv:2606.02822)

**Source**: `research to be indexed/` — daily digest fetch.

- **NEW** `@sources/arxiv-2606-02822-owasp-llm-defense-attribution.md` (read)
- **NEW** `@entities/tools/llm-defense-lattice.md` (draft, Reference — GitHub license NOASSERTION)
- **Updated** `agent-runtime-guardrails`, `llm-adversarial-fuzzing`, `llm-pentest-automation`, `ai-for-cybersecurity`, `defenseclaw`, `cryptex-oss`, `seclaw-eval`, `index.md`
- **PDF** → `raw-sources/arxiv-2606.02822-which-defense-closes-which-threat-attributing-ow.pdf`
- **Sweep** `2026-06-04-daily.md` marked ingested

## [2026-06-03] ingest | K95 — skill injection cluster (3 arXiv)

- **Sources** — 2606.00485 Confused ChatGPT, 2606.01567 defenses/enablers, 2606.03024 SkillGuard
- **Concept** — `agent-skill-injection.md`
- **Cross-wiki** — steal permission model → `@ccc-wiki/concepts/skill-vetting.md`; OSINT prod brief `2026-06-03_k95-skillguard-permission-steal-cemini-prod`
- **PDFs** → librarian; inbox cleared
