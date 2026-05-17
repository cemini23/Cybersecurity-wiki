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
  1. **CLAUDE.md OSINT-wiki path was wrong** — `../../Desktop/OSINT WORKSPACE/wiki/` resolved to `/Users/claudiobarone/Desktop/Desktop/OSINT WORKSPACE/wiki/` (extra `Desktop/`). Corrected to `../../OSINT WORKSPACE/wiki/`. This unblocks the lint's cross-wiki resolver for every `@osint-wiki/...` reference.
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
