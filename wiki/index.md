# Cybersecurity Wiki — Index

> Content-oriented catalog of every page in this wiki. Keep this curated by hand — it's the human-readable map.

---

## How to use this index

- **Concepts** are the *answers* (synthesized understanding of a topic). Start here when you ask "what is X?"
- **Entities** are the *nouns* (tools, certs, threat actors, people, vendors, programming languages, frameworks, platforms). Start here when you ask "tell me about X"
- **Sources** are the *raw inputs* (one page per PDF/article/repo). Mostly anchored from corresponding entity/concept pages — only browse them directly when you need provenance

---

## Concepts

### Doctrine + methodology

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/red-team-operations.md | validated | Red Team vs Pentest distinction; engagement model |
| @concepts/adversary-emulation.md | validated | APT-emulation plan + AutoSUT environment gap + LLM persona convergence |
| @concepts/threat-intelligence.md | validated | CTI 3-tier model + STIX SUT limits + TTP attribution under AI emulation |
| @concepts/purple-team-operations.md | draft | Red + blue collaborative engagements |
| @concepts/soc-operations.md | validated | Security Operations Center tooling + tiers + 5 pillars |
| @concepts/incident-response.md | validated | NIST / SANS IR lifecycle |
| @concepts/ransomware.md | validated | Ransomware defensive ops + investigation runbook (T1486) |
| @concepts/threat-hunting.md | validated | Hypothesis-driven proactive detection |
| @concepts/phishing-investigation.md | validated | SOC-analyst phishing triage (Yahia 5-step workflow + SPF/DKIM/DMARC) |
| @concepts/responsible-disclosure.md | draft | Coordinated Vulnerability Disclosure + CVE process |
| @concepts/bug-bounty.md | draft | Public bounty programs + career path |
| @concepts/cybersecurity-careers.md | validated | Career map + certification ladder |
| @concepts/agent-execution-provenance.md | draft | Evidence tracing + execution provenance — CFD artifact gap (2606.09084) |
| @concepts/agent-vm-sandboxing.md | validated | LLM-driven agent-VM sandboxing; pairs with Docker allowlist proxy (K102) |
| @concepts/docker-agent-sandbox-allowlist-proxy.md | draft | Docker/gVisor agent sandbox + vp-internal egress allowlist (K102) |

### Offensive technique categories

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/web-pentest-methodology.md | validated | Web-app pentest checklist (Joas) |
| @concepts/windows-pentest.md | draft | Windows + Active Directory + O365 |
| @concepts/cloud-pentest.md | draft | AWS / Azure / GCP / O365 pentest |
| @concepts/mobile-pentest.md | draft | Android + iOS app pentest |
| @concepts/network-security.md | draft | Network / firewall / wireless / IoT / OT / 6G CPS closed-loop |
| @concepts/6g-cps-closed-loop-security.md | draft | 6G CPS edge-to-network AI-native security loop (2606.08173) |
| @concepts/exploit-development.md | draft | Buffer overflow → ROP → kernel exploits |
| @concepts/buffer-overflow.md | draft | Stack/heap overflow fundamentals + shellcode |
| @concepts/av-edr-bypass.md | validated | AV/EDR evasion tradecraft |
| @concepts/privilege-escalation.md | validated | Linux + Windows privesc |
| @concepts/credential-access.md | draft | Credential dumping + password cracking (TA0006) |
| @concepts/pivoting.md | draft | Lateral movement + tunneling + port forwarding |
| @concepts/social-engineering.md | draft | Phishing + vishing + pretexting |
| @concepts/phishing.md | draft | Spear phishing + MFA bypass + infrastructure |
| @concepts/osint-for-cybersecurity.md | validated | Pre-engagement + threat-intel OSINT |
| @concepts/linux-pentest.md | draft | Linux enumeration + privesc (GTFOBins, SUID, capabilities) |
| @concepts/wireless-pentest.md | draft | WiFi / WPS / Bluetooth / RFID attacks |
| @concepts/container-security.md | draft | Docker + Kubernetes attack/defense |
| @concepts/dns-server-discovery-vs-subdomain-enumeration.md | draft | DNS recon distinction (server discovery vs subdomain enum) |

### Defensive + analytical

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/malware-analysis.md | draft | Static + dynamic malware RE |
| @concepts/defense-in-depth.md | draft | Layered security architecture |
| @concepts/system-hardening.md | draft | OS + network + application hardening |
| @concepts/linux-security.md | draft | RHEL security, SELinux, auditd, SSH hardening |
| @concepts/siem.md | draft | SIEM platform layer — log collection, correlation, alerting; BAS→Sigma detection-as-code (2606.05252) |
| @concepts/endpoint-detection-response.md | draft | EDR/XDR — endpoint telemetry, detection + response |

### Emerging / cross-domain

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/ai-for-cybersecurity.md | draft | LLM use in red + blue workflows |
| @concepts/llm-vulnerability-discovery.md | draft | LLM-driven vuln-discovery pipeline (Detect→Attack); defending-code ASAN verify |
| @concepts/llm-adversarial-fuzzing.md | draft | Adversarial LLM testing methodology (FuzzyAI umbrella) |
| @concepts/pair-prompt-pattern.md | draft | PAIR — single-turn LLM jailbreak (arXiv 2310.08419) |
| @concepts/crescendo-multi-turn-jailbreak.md | draft | Multi-turn LLM escalation attack (arXiv 2404.01833) |
| @concepts/llm-pentest-automation.md | draft | Tier 1/2 LLM pentest automation + scope-enforcement model |
| @concepts/agent-runtime-guardrails.md | draft | Agent side-effect attacks + runtime guards; GT-MCP trajectory layer (2606.10322) |
| @concepts/llm-code-review-agent-security.md | draft | SEVRA merge-gate robustness — reversed CVE PR + framing attacks (2606.13757) |
| @concepts/trajectory-context-control.md | draft | GT-MCP — multi-agent memory-commit gate + drift rollback (2606.10322) |
| @concepts/internet-of-agentic-ai-ioai.md | draft | IoAI vision — federated agent ecosystems + Table 4 threat taxonomy (2606.12835) |
| @concepts/exceptional-access-risk-quantification.md | draft | EA architecture risk framework — T-EA vs OTT-EA, deep uncertainty (2606.19106) |
| @concepts/agent-least-privilege-tool-selection.md | draft | Over-privileged tool selection — OPUR/PED, TOOLPRIVBENCH (2606.20023) |
| @concepts/agent-probabilistic-datalog-verification.md | draft | DRO probabilistic Datalog runtime verification — noisy classifiers (2606.20510) |
| @concepts/system-prompt-leakage.md | draft | System prompt exfiltration — attention drift, LeakBench, AREA (2606.18673) |
| @concepts/prompt-injection-detector-calibration.md | draft | Guard-model severity S under shift — confident FN on indirect hijack (2606.22659) |
| @concepts/self-evolving-agent-security.md | draft | MLAS matrix — self-evolving agents, attack persistence (2606.23075) |
| @concepts/ai-loss-of-control-osint-monitoring.md | draft | OSINT vectors for AI loss-of-control detection (2606.20610) |
| @concepts/cross-tool-description-poisoning.md | draft | Cross-tool MCP metadata steering + Tool-Guard isolated planning (2606.20922) |
| @concepts/local-agent-runtime-audit.md | draft | CLAWAUDIT static runtime audit — OpenClaw source (2606.21071) |
| @concepts/autonomous-defense-agent-transferability.md | draft | ARENA — SOC agent transferability gap (2606.21377) |
| @concepts/lingering-authority-revocable-capabilities.md | draft | PORTICO revocable planner capabilities (2606.22504) |
| @concepts/intent-governed-tool-authorization.md | draft | IGAC — session intent narrowing (2606.22916) |
| @concepts/agentic-offensive-security-kill-chain.md | draft | Agentic pentest agent kill chain + agent-phishing (2606.24496) |
| @concepts/multi-tool-threshold-mcp-poisoning.md | draft | ShareLock Shamir multi-tool MCP poisoning (2606.27027) |
| @concepts/tool-environment-unreliability-eval.md | draft | ToolBench-X recoverable tool hazards + diagnosis gap (2606.25819) |
| @concepts/confidence-aware-tool-orchestration.md | draft | Robust-TO Blind Trust + (result, confidence) tool routing (2606.26904) |
| @concepts/cognitive-heuristics-llm-vuln-detection.md | draft | Halo/framing/anchoring bias in LLM vuln scanners (2606.30587) |
| @concepts/mcp-execution-control-invariants.md | draft | HCP eight invariants — execution control beyond MCP connection (2606.29073) |
| @concepts/crypter-as-a-service.md | draft | CraaS underground market — exploit.in longitudinal study (2606.24226) |
| @concepts/seclaw-agent-security-evaluation.md | draft | Trajectory-aware agent security eval — SeClaw methodology (Reference until code ships) |
| @concepts/agent-skill-injection.md | draft | K95 — skill injection + MalSkillBench/POISE + SPI + P3 memory gap (K114) |
| @concepts/context-fractured-decomposition-attacks.md | draft | CFD — artifact provenance gap jailbreaks across sessions/instances (2606.09084) |
| @concepts/mcp-security-posture.md | validated | K100 — MCP admission, DCI, SPI, WebMCP MSTI, VATS, GT-MCP trajectory (2606.10322) |
| @concepts/agentic-containment-principles.md | draft | K114 — P1–P6 containment matrix; LangChain/AutoGPT/OpenAI SDK audit |
| @concepts/neuro-symbolic-auditable-reasoning.md | validated | K100 — NeuroLog-style Datalog+SMT auditable vuln chains |
| @concepts/blockchain-security.md | draft | Smart-contract + DeFi security |
| @concepts/metaverse-security.md | draft | VR / AR / immersive platform risk |
| @concepts/game-hacking.md | draft | Anti-cheat bypass as RE practice |
| @concepts/zero-trust.md | draft | Identity-centric defense architecture |
| @concepts/cyberwarfare.md | draft | Nation-state cyber operations |
| @concepts/anonymity-networks.md | draft | Tor + I2P |

### Education + ethics

| Page | Maturity | Topic |
|------|----------|-------|
| @concepts/cyber-for-kids.md | draft | Parent + teacher + LE-facing kid-safety material |

---
- [chekusu/mails — AI email parsing, dual-use phishing-domain enumeration](concepts/2026-05-13_chekusu-mails-dual-use.md) — cross-wiki stub routed from ingest — `cross-wiki`

## Entities

### Frameworks

| Page | Maturity |
|------|----------|
| @entities/frameworks/mitre-attack.md | validated |
| @entities/frameworks/cyber-kill-chain.md | validated |

### Certifications

| Page | Maturity | Vendor |
|------|----------|--------|
| @entities/certifications/oscp.md | draft | Offensive Security |
| @entities/certifications/oswa.md | draft | Offensive Security |
| @entities/certifications/oswe.md | draft | Offensive Security |
| @entities/certifications/crto.md | draft | Zero-Point Security |
| @entities/certifications/ceh.md | draft | EC-Council |
| @entities/certifications/comptia-security-plus.md | draft | CompTIA |
| @entities/certifications/comptia-pentest-plus.md | draft | CompTIA |
| @entities/certifications/ecppt.md | draft | eLearnSecurity / INE |
| @entities/certifications/ecptx.md | draft | eLearnSecurity / INE |
| @entities/certifications/ewpt.md | draft | eLearnSecurity / INE |

### Tools

| Page | Maturity | Role |
|------|----------|------|
| @entities/tools/cobalt-strike.md | draft | Commercial C2 |
| @entities/tools/metasploit.md | draft | FOSS exploitation framework |
| @entities/tools/burp-suite.md | draft | Web-app testing proxy |
| @entities/tools/caldera.md | draft | Adversary emulation automation |
| @entities/tools/maltego.md | draft | OSINT graph analysis |
| @entities/tools/wazuh.md | draft | FOSS SIEM / host-IDS |
| @entities/tools/nmap.md | draft | Network scanner |
| @entities/tools/bloodhound.md | draft | AD attack-path graph |
| @entities/tools/kali-linux.md | draft | Pentest Linux distribution (OffSec, 600+ tools) |
| @entities/tools/multi-cloud-red-team.md | draft | Multi-cloud red team operations (AWS/Azure/GCP) |
| @entities/tools/cua.md | validated | Agent-VM sandbox (Apple Virtualization + Lume) |
| @entities/tools/fuzzyai.md | validated | LLM adversarial fuzz framework (CyberArk, Apache-2.0) |
| @entities/tools/ifixai.md | draft | Agent deception/manipulation diagnostic harness — Adopt (K142) |
| @entities/tools/pentest-ai-agents.md | validated | LLM-driven red-team automation (MIT) |
| @entities/tools/pydns-scanner.md | validated | DNS server discovery (ethical-use addendum) |
| @entities/tools/jadx-mcp-server.md | draft | Android RE + live debugging via MCP (JADX decompiler) |
| @entities/tools/osmedeus.md | draft | Orchestration engine for security scanning (recon/scan YAML workflows) |
| @entities/tools/splunk.md | validated | Commercial SIEM / SPL — 110-query detection catalog + SPL command reference + 24 SOC-2 use cases |
| @entities/tools/qradar.md | validated | IBM commercial SIEM — architecture/components/databases/EPS+FPM licensing/coalescing/CRE/superflows (Kothekar 2023 Ch 1-4 deep-read; Ch 5-12 deferred) |
| @entities/tools/sysmon.md | draft | Microsoft Sysinternals — high-fidelity Windows event log (process/network/registry/WMI) |
| @entities/tools/gau.md | draft | Multi-provider known-URL discovery — OTX / Wayback / Common Crawl (MIT, Go; Adopt) |
| @entities/tools/katana.md | draft | Scriptable web crawler with headless-browser mode (MIT, Go; ProjectDiscovery; Adopt) |
| @entities/tools/gopacket.md | draft | Go packet-decoding library for network analysis (Apache-2.0, Mandiant; Steal-from) |
| @entities/tools/openvpn-install.md | draft | Bash OpenVPN deployment automation — NAT / IPv6-routing logic (Unlicense; Steal-from) |
| @entities/tools/vpn-self-hosted.md | draft | VPN hub page — WireGuard, OpenVPN, wg-easy, PiVPN, Tailscale catalog + decision matrix |
| @entities/tools/defenseclaw.md | draft | Enterprise AI security governance — MCP/skill scanners + Codex sidecar observe (Apache-2.0; ADOPTED laptop) |
| @entities/tools/deepzero.md | draft | Windows kernel-driver vuln research pipeline — PE→Ghidra→Semgrep→LLM (MIT) |
| @entities/tools/grex.md | draft | Regex generation from test cases — SOC/IR log parsing (Apache-2.0) |
| @entities/tools/vanguard.md | draft | Single-binary DFIR toolkit — Velociraptor+Volatility+KAPE+YARA, 28 MITRE-mapped (MIT) |
| @entities/tools/raptor.md | draft | Claude Code offensive/defensive agent — Semgrep+CodeQL (Steal-from, no license) |
| @entities/tools/src-hunter-skill.md | draft | Claude Code bug-bounty/pentest skill — 305 payloads, 19 playbooks, 263 WAF bypasses (MIT) |
| @entities/tools/bluehood.md | draft | Bluetooth telemetry monitoring — BLE MAC correlation (MIT, Steal-from) |
| @entities/tools/super-spr.md | draft | Zero-trust networking — per-device DNS, VLAN segregation in Go (BSD-3-Clause) |
| @entities/tools/reconftw.md | draft | Apex recon automation — subdomain+web+vulns+osint+Axiom fleet distribution (MIT, 7.5k stars) |
| @entities/tools/evilsocket-audit.md | draft | 8-stage vuln-discovery agent — Glasswing pattern, reachability gating (MIT) |
| @entities/tools/offensive-claude.md | draft | Offensive-security Claude Code workstation — 25 skill modules, 8 classifications |
| @entities/tools/reverse-skill.md | draft | MIT skill router pack for authorized pentest methodology routing (K129) |
| @entities/tools/cf-hero.md | draft | Cloudflare origin-IP discovery via DNS + Shodan hashing (Go, ~2.4k stars) — Defer pending LICENSE audit |
| @entities/tools/pentest-ai.md | draft | MCP offensive-security server — 205 tools, 17 agents, MIT (`ptai` CLI; distinct from pentest-ai-agents) |
| @entities/tools/nidhogg.md | draft | Windows kernel rootkit reference — DKOM/ActiveProcessLinks tradecraft (GPL-3.0; Steal-from, no deploy) |
| @entities/tools/iron-proxy.md | draft | Egress firewall for untrusted workloads (Apache-2.0; Adopt-eligible Phase-0) |
| @entities/tools/cryptex-oss.md | draft | LLM red-teaming transforms/mutators toolkit — 162 transforms (MIT; Adopt-eligible Phase-0) |
| @entities/tools/cve-mcp-server.md | draft | Security-intel MCP server — CVE/EPSS/KEV/ATT&CK enrichment (Apache-2.0; CONDITIONAL-GO) |
| @entities/tools/autosut.md | draft | STIX environment-semantics gap measurement for adversary emulation (Reference) |
| @entities/tools/malskillbench.md | draft | Runtime-verified malicious agent skills benchmark — CI/PI detector eval (Reference) |
| @entities/tools/sevra-bench.md | draft | Malicious PR benchmark for LLM review agents — inspect_ai + Gitea (Reference) |
| @entities/tools/nvidia-skillspector.md | draft | Agent/MCP skill supply-chain scanner — prompt injection + tool poisoning (Apache-2.0; Adopt) |
| @entities/tools/netviz.md | draft | Browser network-architecture graph visualizer — D3.js + Socket.IO (MIT; Adopt, K93) |
| @entities/tools/airguard.md | draft | Runtime authority control for tool/MCP agents (MIT; CONDITIONAL-GO) |
| @entities/tools/chaincaps.md | draft | MCP proxy — composition-safe tool chains via monotonic capability budgets (Reference) |
| @entities/tools/handle-capability-protocol.md | draft | HCP reference runtime — MCP execution-control invariants + 10-case benchmark (MIT; CONDITIONAL-GO) |
| @entities/tools/agentredguard.md | draft | Integration-aware guard for SaaS LLM agents — AgentRedBench paper (Reference) |
| @entities/tools/seclaw-eval.md | draft | Trajectory-aware agent security benchmark — SeClaw Docker testbed (Reference, K98) |
| @entities/tools/ai-research-skills.md | draft | Orchestra ML skills library — cybersec cherry-pick subset (K113 CONDITIONAL-GO) |
| @sources/brief-k113-cybersec-ai-research-skills-2026-06-12.md | deep-read | K113 cross-wiki brief ingest |
| @entities/tools/llm-defense-lattice.md | draft | OWASP LLM Top 10 defense attribution — BAS lattice + 17-probe corpus (Reference) |
| @entities/tools/defending-code-reference-harness.md | draft | Anthropic Docker/gVisor vuln-discovery reference harness — K102 CONDITIONAL-GO |

### Vendors

| Page | Maturity |
|------|----------|
| @entities/vendors/offensive-security.md | draft |
| @entities/vendors/elearnsecurity.md | draft |
| @entities/vendors/comptia.md | draft |
| @entities/vendors/ec-council.md | draft |
| @entities/vendors/zeropoint-security.md | draft |

### Platforms (labs / CTF)

| Page | Maturity |
|------|----------|
| @entities/platforms/hackthebox.md | draft |

### Programming languages

| Page | Maturity | Role |
|------|----------|------|
| @entities/programming-languages/python.md | draft | Scripting + automation |
| @entities/programming-languages/c.md | draft | Exploit dev + AV/EDR bypass |
| @entities/programming-languages/javascript.md | draft | Web exploitation + Node.js |
| @entities/programming-languages/powershell.md | draft | Windows post-exploitation |

### Threat actors

| Page | Maturity | Region |
|------|----------|--------|
| @entities/threat-actors/apt28.md | draft | Russia-attributed (GRU) |
| @entities/threat-actors/apt29.md | draft | Russia-attributed (SVR) |
| @entities/threat-actors/lazarus.md | draft | DPRK-attributed (RGB) |
| @entities/threat-actors/lockbit.md | draft | Criminal RaaS (Russian-language) |

### People

| Page | Maturity | Role |
|------|----------|------|
| @entities/people/joas-a-santos.md | validated | Corpus author |
| @entities/people/mostafa-yahia.md | draft | SOC analyst author (Yahia Packt 2023) |
| @entities/people/rajneesh-gupta.md | draft | SIEM / SOC 2 use-case author (@rajneeshcyber) |
| @entities/people/ashish-m-kothekar.md | draft | IBM SWAT/SME — author of *Building a Next-Gen SOC with IBM QRadar* (Packt 2023) |

---
- [xullexer/PYDNS-Scanner — async DNS recon (Slipstream + SlipNet)](entities/pydns-scanner-xullexer.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [0xSteph/pentest-ai-agents — shell-only Claude Code subagents for pentest workflows](entities/pentest-ai-agents-0xsteph.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [apktool-mcp-server — Android Reverse Engineering via MCP](entities/apktool-mcp-server.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [T-Pot — Multi-Honeypot Deception Framework](entities/tpotce.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Decepticon — Autonomous Red-Team Multi-Agent Framework](entities/decepticon.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Claude-Red — Offensive Security Skills Library for Claude Code](entities/claude-red-offensive-skills.md) — cross-wiki stub routed from ingest — `cross-wiki`

### Cross-wiki routed tool evaluations (index-only, no entity pages)

These tools surfaced from OSINT-wiki K-batch evaluations. Verdicts below reflect the eval tier at routing time. Re-verify license + maturity before adopting.

| Tool | License | Tier | Brief | Note |
|------|---------|------|-------|------|
| YellowKey | MIT | Steal-from | K42 | Exploit PoC harness — methodology reference |
| GreenPlasma | MIT | Steal-from | K42 | Exploit PoC harness — methodology reference |
| witr | — | Steal-from | K42 | Webhook + telemetry replay harness |
| autoharness | — | Steal-from | K42 | Fuzz-harness auto-generation pattern reference |
| cypht | — | Steal-from | K42 | Secure webmail — IR inbox isolation reference |
| awesome-codex-subagents | — | Reference | K42 | Curated subagent prompt list |
| claude-code-telegram | — | Steal-from | K42 | Sandbox-hardening pattern for chatops |
| frona | BSL-1.1 | Reject (until 2029) | K42 | Policy-driven syscall filtering — methodology reference only |
| Threat-Intel SaaS cluster (9) | closed-source | Reject | K42 | Shodan/FullHunt/ONYPHE/SOCRadar/Pulsedive/IntelX/Hunter.io/PublicWWW/Coalitioninc — batch-rejected |
| Claude Code Agent Farm | MIT | Steal-from | K15 | Parallel tmux orchestration — lock-based concurrency + heartbeat for network enumeration |
| MyIP DNS Leak Detection | MIT | Steal-from | K15 | WebRTC STUN leak detection, DNS exit endpoint identification — VPN/tunnel validation |
| fingerprint-suite | Apache-2.0 | Cross-ref | K15 | Browser fingerprint generation/injection — primary fit osint-wiki. Red-team browser evasion reference |
| netviz | MIT | Adopt | K53, K93 | @entities/tools/netviz.md — browser network graph visualizer (upgraded from Steal-from) |
| iOS-pentest-list | — | Reference | K53 | Curated Markdown list of iOS pentest tools |
| opendrop | TBD | Defer | K51 | Reverse-engineered Apple AirDrop (Python, 9.6k stars, SEEMOO lab) — license audit pending |
| Shells-X | TBD | Defer | K51 | Modular single-file PHP web-shell framework — license audit pending |
| AgentGym-RL | TBD | Defer | K51 | RL framework for LLM agent training — academic, license unverified |
| Grafana-Final-Scanner | TBD | Defer | K51 | Multi-source Grafana version fingerprinting + CVE checking — license unverified |
| fd | MIT+Apache-2.0 | Adopt-eligible | K51 | Rust `find` replacement, 43k stars — eval wrongly rejected; license verified clean |
| TruffleHog | AGPL-3.0 | Reject (copyleft) | K54 | Credential scanner, 26k stars — reference-only due to AGPL poison pill |
| gitGraber | GPL-3.0 | Reject (copyleft) | K54 | Real-time GitHub credential-leak monitor — reference-only |
| H4X-Tools | GPL-3.0 | Reject (copyleft) | K54/K55 | OSINT/recon/scraping toolkit — reference-only |
| VulnWeb directory | — | Reference | K54 | Directory of OWASP initiatives (GenAI Security, AI Exchange, CycloneDX) |
| Hackers-Arise MCP log | — | Reference | K54 | Educational blueprint for AI-assisted blue-team / MCP server boundary patterns |
| Windows-Use | MIT | Reference | K54 | GUI-level Windows automation agent — lateral-movement logic reference (primary fit: CCC wiki) |
| tugarecon | GPL-3.0 | Steal-from | K55 | Subdomain recon + Temporal Intelligence & Asset Memory module — impact-scoring algorithm extractable |
| hackingtool-plugin | NO LICENSE | Defer | K55 | 183 pentest+OSINT utilities integrated into Claude Code via C#/Docker — license+maturity recheck |
| osint_stuff_tool_collection | NO LICENSE | Reference | K55 | 7,875-star markdown index of OSINT tools — threat-actor-profiling subset |
| jhalon/reverse-engineering-protocols | — | Reference | K56 | Instructional curriculum on dissecting undocumented network protocols |
| LLM4Pentest catalog | — | Defer | K56, K55-2 | `simon-p-j-r/LLM4Pentest` — academic LLM-pentest survey; gh api NO LICENSE (2026-05-22) |
| Awesome-Hacking | CC0-1.0 | Reference | K55-2 | Aggregate awesome-list — gh-api cleared NO LICENSE false negative |
| open-source-web-scanners | Apache-2.0 | Reference | K55-2 | ZAP-lead-dev curated web-scanner index (also K57 reject as aggregate — license verified) |
| CF-Hero | — | Defer | K55-2 | @entities/tools/cf-hero.md — Cloudflare origin-IP unmasking |
| jadx-ai-mcp | Apache-2.0 | Cross-ref | K55-2 | Sibling to @entities/tools/jadx-mcp-server.md (`zinja-coder`, same MCP family) |
| Galaxy-Bugbounty-Checklist | — | Reject | K57 | NO LICENSE FOUND — methodology reference only |
| BugBounty-Recon-Methodology | — | Reject | K57 | Verify license before any adoption |
| sqlmap | NOASSERTION | Reject | K57 | Confirm AGPL/GPL before use — already cited in methodology pages, no entity |
| NoSQLMap | GPL-3.0 | Reject (copyleft) | K57 | Reference-only — same copyleft posture as gitGraber/H4X-Tools |
| KaliGPT | Custom NC | Reject (commercial) | K60 | Ollama terminal harness — **do not install on prod**; eval overturned Adopt |
| h4cker | MIT | Reference | K60 | Omar Santos mega-repo — OSINT tradecraft in `osint/` subtree (~26k stars) |
| pentest-ai | MIT | CONDITIONAL-GO | K60 | @entities/tools/pentest-ai.md — MCP + 17 agents; compare vs pentest-ai-agents |
| cyber-security-llm-agents | — | Defer | K60 | NVISO catalog — gh api NO LICENSE; reference until SPDX filed |
| Nidhogg | GPL-3.0 | Steal-from | K63 | @entities/tools/nidhogg.md — DKOM/process-hiding tradecraft for MITRE mapping; **no binary import** |
| facex | Apache-2.0 | Steal-from | K68 | WASM in-browser face stack + anti-spoof — extract ideas only, no full import |
| iron-proxy | Apache-2.0 | Adopt-eligible | K68 | @entities/tools/iron-proxy.md — egress firewall for untrusted workloads |
| centaur | NOASSERTION | Steal-from | K68 | Paradigm secure multi-agent host — read LICENSE text before any code use |
| cryptex-oss | MIT | Adopt-eligible | K68 | @entities/tools/cryptex-oss.md — LLM red-team transform/mutator catalog |
| ZishanAdThandar/pentest | GPL-3.0 | Reject | K68 | Pentest/bounty notes cheatsheets — keep out of IP-sale surfaces |
| bbot | AGPL-3.0 | Reject (copyleft) | K71, K73 | `blacklanternsecurity/bbot` recursive scanner (~9.7k stars) — **do not route into IP-sale surfaces** |
| Hackers-Arise AI enumeration | — | Reference | K71 | AI-assisted enumeration article (no code); complements K54 Hackers-Arise MCP log row |
| cve-mcp-server | Apache-2.0 | CONDITIONAL-GO | K73 | @entities/tools/cve-mcp-server.md — workstation CVE/KEV/EPSS intel enrichment MCP |
| nvidia-skillspector | Apache-2.0 | Adopt | K88 | @entities/tools/nvidia-skillspector.md — agent/MCP skill supply-chain scanner |
| defenseclaw | Apache-2.0 | ADOPTED (observe) | K42, CCC | @entities/tools/defenseclaw.md — CLI scanners + Codex sidecar observe 2026-05-31; action/LLM judge optional |
| train-llm-from-scratch | MIT | Reference | K88 | LLM training reference only — not a security tool |
| linux-basics-for-hackers-notes | — | Reject | K88 | NO LICENSE FOUND — do not adopt |
| Graph-R1 | CC-BY-NC-SA (eval) | Reject | K88 | K88 eval reject; gh api reports MIT 2026-05-31 — verify LICENSE before override |
| seclaw-eval | — | Reference | K98 | @entities/tools/seclaw-eval.md — trajectory-aware agent security benchmark; **no LICENSE on GitHub API 2026-06-04** |
| sevra-bench | — | Reference | digest | @entities/tools/sevra-bench.md — LLM PR merge-gate eval; **no LICENSE on GitHub API 2026-06-16** |
| toolprivbench | — | Reference | digest | @entities/tools/toolprivbench.md — OPUR/PED least-privilege tool eval; **no LICENSE on GitHub API 2026-06-19** |
| leakbench-area | — | Reference | digest | @entities/tools/leakbench-area.md — LeakBench + AREA soft-prompt defense; **no LICENSE on GitHub API 2026-06-22** |
| clawaudit | — | CONDITIONAL-GO | digest | @entities/tools/clawaudit.md — OpenClaw runtime Semgrep/CodeQL audit; **no LICENSE on GitHub API 2026-06-24** |
| tool-guard | MIT | CONDITIONAL-GO | digest | @entities/tools/tool-guard.md — isolated planning vs cross-tool description poisoning (ICML 2026) |
| aohp | Apache-2.0 | CONDITIONAL-GO | digest | @entities/tools/aohp.md — AOSP agent-native OS harness (2606.23449) |
| toolbench-x | — | Reference | digest | @entities/tools/toolbench-x.md — tool-environment unreliability benchmark; **no LICENSE 2026-06-27** |
| defengraph | — | Reference | digest | @entities/tools/defengraph.md — KG+RAG blue-team assistant; no public repo 2026-06-23 |
| picalib-research | — | Reference | digest | @entities/tools/picalib-research.md — PI guard severity metric artifacts; **no LICENSE 2026-06-23** |
| ecc | MIT | Steal-from / CONDITIONAL-GO | digest | @entities/tools/ecc.md — cross-harness operator system; **ecc-agentshield** npm for config audit |
| skillgate | closed-source SaaS | Reference | digest | @entities/tools/skillgate.md — Mitiga free skill/hook/MCP config scanner |
| llm-defense-lattice | NOASSERTION | Reference | digest | @entities/tools/llm-defense-lattice.md — OWASP LLM Top 10 per-defense BAS lattice; license audit pending |
| defending-code-reference-harness | Apache-2.0 | Reference | K102 | @entities/tools/defending-code-reference-harness.md — Docker/gVisor agent vuln pipeline; laptop lab only |
| ai-infra-guard | Apache-2.0 + NOTICE §4(d) | CONDITIONAL-GO | digest | @entities/tools/ai-infra-guard.md — multi-layer agent red team (2606.31227); **external Docker only** |
| handle-capability-protocol | MIT | CONDITIONAL-GO | digest | @entities/tools/handle-capability-protocol.md — HCP execution-control invariants + benchmark (2606.29073); 0★ reference runtime |

## Meta

| Page | Maturity | Role |
|------|----------|------|
| @meta/daily-research-digest-cadence.md | draft | Federated daily research digest — K93 install; outputs to `wiki/sweeps/` |

## Sources

282 source pages live in `sources/`:

- **226** from the Joas A Santos seed corpus (shared Drive folder `ebooks Joas`)
- **22** from the Redteam Kit shared Drive folder (English-language security books + field manuals)
- **26** from the BlueTeam Kit shared Drive folder (SOC / blue-team PDFs — SIEM, threat hunting, IR, EDR)
- **2** video courses (Kali Linux 2023 50-chapter set; Python Ethical Hacking MASTERCLASS 19-section set) — `.mp4` only, each catalogued as a single page

Source pages are not individually catalogued here; each entity and concept page lists the sources that synthesize into it under `related:`. Browse `sources/` directly for provenance lookups.

The corpus inventory (file ID + title for every PDF) lives at `.scratch/drive_inventory.tsv` (gitignored — see `ROADMAP.md` for the storage decision).

**Catalog status (decided 2026-05-16):** the `sources/` layer is a deliberate *reference catalog* of the two shared Drive folders. Every source page carries `read_status: unread-stub` because the PDFs live in external Drive folders not synced to this workspace — `unread-stub` is the expected steady state here, not a defect. A page graduates to `deep-read` only when the underlying PDF is obtained and read. Tooling that scores wiki health (e.g. `wiki_scan_all.py`) should treat this wiki's cited-unread-stub count as informational, not as a backlog to burn down.

---
- [tl;dr sec — [tl;dr sec] #335 - Prompt Injection as Role Confusion, PHP Ecosystem Security, New MCP Spec](sources/newsletter-rss-tldrsec-2026-07-02-tldr-sec-335---prompt-injection-as-role-confusio.md) — cross-wiki stub routed from ingest — `cross-wiki`
- [Packt SecPro — Identity Became the New Perimeter](sources/substack-rss-secpro-2026-07-03-identity-became-the-new-perimeter.md) — cross-wiki stub routed from ingest — `cross-wiki`

## Cross-wiki anchors

When this wiki references a sibling wiki's page, the citation uses `@<alias>/path/to/page.md`. Aliases:

- `osint-wiki` — financial / quant / prediction-market research
- `image-gen-wiki` — uncensored image generation, ComfyUI, LoRA
- `seo-wiki` — local SEO, GBP, GEO/AEO, web design
- `3d-printing-wiki` — FDM/FFF, Bambu, slicers, print farms

Bidirectional invariant: if this wiki cites `@osint-wiki/...`, the matching page in the OSINT wiki should cite `@cybersecurity-wiki/...` back. Run `python3 scripts/wiki_lint.py` to check.

