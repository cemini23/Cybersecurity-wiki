# Cybersecurity Wiki — ROADMAP

Active workstreams, open decisions, and the done log. Read at session start; update at session end.

---

## Active workstreams

### W1 — Seed corpus ingest (Joas A Santos PDFs)

**Status:** Initial scaffolding complete 2026-05-12. 227 PDFs from the `ebooks Joas` Google Drive folder catalogued as source stubs. Strategic deep-reads + entity/concept synthesis underway.

Steps:
- [x] Scaffold from `wiki-template/`
- [x] Adapt CLAUDE.md for cybersecurity vertical
- [x] Inventory 227 PDFs with file IDs (see `.scratch/drive_inventory.tsv`)
- [x] Generate 227 source stubs with frontmatter + Drive-link provenance
- [x] Seed entity pages for ~50 most-cited certs, tools, frameworks, vendors
- [x] Seed ~25 concept pages covering the wiki's main themes
- [x] Cross-link to OSINT / image-gen / SEO / 3d-printing wikis
- [x] Deep-read 7 PDFs to upgrade key concept pages from `draft` to `validated` (MITRE ATT&CK, Red Team Ops, AV/EDR Bypass, Web Pentest Checklist, Linux PrivEsc, IR Overview, INFOSEC Proficiency Colors)
- [x] Lint clean: 0 orphans, 0 bidirectional gaps, 0 dangling refs
- [x] Full maintenance pass 2026-05-12 evening — fixed CLAUDE.md OSINT path bug + `@@` typo + trailing-period regex boundary bug. All 8 lint checks now green; 4 cross-wiki refs resolve.
- [x] Phase-1 adoption of 4 K42-routed tools (2026-05-13) — entity + methodology pages for cua, fuzzyai, pentest-ai-agents, pydns-scanner; 6 new concept pages (agent-vm-sandboxing, llm-adversarial-fuzzing, pair-prompt-pattern, crescendo-multi-turn-jailbreak, llm-pentest-automation, dns-server-discovery-vs-subdomain-enumeration); 17 existing pages updated with bidirectional backlinks.
- [x] Continue deep-reads: Buffer Overflow series + eCPPT Notes + CTH intro PT.1 (2026-08-02/03) — OSINT Overview still open
- [ ] Phase-2 of the 4 adoptions: synthesize PAIR + Crescendo papers into `## Snippets`; lab-validate pentest-ai-agents Tier-2 mode (currently `[TENTATIVE]`); evaluate the remaining 11 K42-routed tools.

### W2 — Public-distribution polish

**Status:** Pre-publish. Repository scheduled for GitHub publish 2026-05-12.

Steps:
- [x] LICENSE (MIT)
- [x] README rewrite for public audience
- [x] Secret scan (no `.env`, no API keys in tracked files)
- [ ] Push to `Cybersecurity-wiki` GitHub repo

---

## Open decisions

- **Author attribution and Drive-folder permanence** — the seed corpus is a third-party share. If access changes or the author requests removal, the wiki keeps the synthesized pages (citations remain valid) but loses the ability to re-verify by re-reading the PDF.
- **PDF storage strategy** — `raw-sources/` is gitignored. Downloading the full 227-PDF corpus is ~2-3 GB. Decision deferred: only download PDFs on demand during deep-read sessions; for stubs, cite Drive file IDs.

---

## Done log

| Date | What | Why it mattered |
|------|------|-----------------|
| 2026-08-26 | Full ingest K307 StepGuard / K308 decorative CoT / K309 prompt security redistribution | Daily sweep 3 PDFs; pre-execution step guard policy; CoT cdr audit; codegen prompt redistributes CWE mix; StepGuard NO LICENSE — no clone; friend add-on 34 |
| 2026-08-25 | K303 fail-closed Cursor deny + K298 secret_grant + Cybersec dual-ID restore after CCC sync | Operator OK: `.env` no longer returned to planner; federation overwrite of dual-ID is auto-restored; SPDX re-hunt still no CLEAR/SDP/BT-NFT/TrustRAG/BreakGuard clones |
| 2026-08-25 | Full ingest K301 CLEAR / K302 PsychJail / K303 CLAUDE.md-deny / K304 SDP / K305 BT-NFT / K306 LLM-compliance + OOD Rebite/critic | Inbox 8 NEW PDFs (rainfall+travel archive-only); restored Cybersec dual-ID K282–K306 after BPS/EnvHarness/Wayfinder overwrite (CCC steal kept); golden_critic Apache-2.0 REFERENCE clone wont_wire; PsychJail NO-GO (null SPDX, 2GB); friend add-on 32 |
| 2026-08-21 | Full ingest K298 Inadvertent Context Leakage / K299 TrustRAG committee RAG / K300 BreakGuard LLM dependency tests + OOD rainfall CSI / travel agents | Inbox 4 PDFs (rainfall+travel OOD); inbound leakage brief filed as K298 not K244 (Trident); no name-collision clones (all REFERENCE); friend add-on 31 |
| 2026-08-20 | Full ingest K295 Fool's Gold / K296 Trusted Workflow Relays / K297 TI→detection + BloodBash/bbot/rule-blindness/excess-authority brief-sync | Inbox 5 PDFs (DiSCO+self-prompt OOD); restored Cybersec dual-ID after CCC K290–K294 overwrite; BloodBash/bbot OSINT Extract pointers |
| 2026-08-18 | Full ingest K282 ARENA-audio / K283 JailbreakSkill / K288 ESTI / K290 CHIVE + Tripwire/SVP/RA-Bench/DFI brief-sync | Inbox 5 PDFs; CHIVE MIT ~11MB REFERENCE; JailbreakSkill null SPDX no clone; Grok credits-out then parent takeover |
| 2026-08-12 | Ingest endpoint-encryption/deniable-storage classes + SLSA/sigstore build integrity + Secure Boot vs device ownership (3 concepts + 7 sources); all REFERENCE vendor HTML; no kits | FDE ≠ anonymity / deniability limits; release-artifact integrity (SLSA L0–L3, Sigstore, reproducible builds) pairs with npm dependency layer; attestation-vs-ownership tension for product policy + operator boxes |
| 2026-08-12 | Ingest license-bind / anti-tamper / Windows CI stack / Joas / mobile attestation (3 concepts + 10 sources + 1 entity); Joas Game Hacking 1 read + archived; no kits | License design for owned products (bind ≥2 layers, re-bind paths); protection classes not kits; HVCI/ELAM/IOMMU/WDAC trust stack; Play Integrity + App Attest server-side verification |
| 2026-08-12 | Ingest anti-cheat/licensing hardware-bound identity (1 concept + 11 sources + 3 entities); ARES 2408.00500 PDF to egress-fi; DeepSeek citation hunt for filtered URLs; no spoof clones | Identifier map for authorized product/lab RE; Vanguard On-Demand + TPM EK; OA3 field inventory; Epic HWID spoof as DMCA |
| 2026-08-12 | Ingest hardware-ID masking OPSEC (11 new pages: 1 concept + 10 sources); friend playbook + checklist brief; 7 PDFs to egress-fi; no clones | Closed wiki gap for anonymity/OPSEC; MAC rand ≠ unlinkability evidenced 2016–2026 |
| 2026-08-11 | Full ingest K267–K269 (ILL / SHE / Taboo) + OOD DoDTrack + OOD TTS-eval; SHE GO clone ~4.4MB Apache-2.0; Phase-1 K267/K268/K269 (lab-redteam + policy-wires + agent-audit); SHE renumbered off duplicate K265; prod+atto+GW+poker+CCC briefs | Inbox cleared; inaudible-LF audio attack+DRG, harness-evolution, decoding-time robustness coverage. Follow-ups: SHE headline ASR pending local repro; ILL/Taboo REFERENCE — re-check for public code before adopting as lab tools |
| 2026-08-10 | Full ingest K265–K266 (Blast Radius / ShieldAI) + OOD QNLP 07439; ShieldAI ~896KB; Phase-1 K265/K266; prod+atto+poker+GW briefs | Inbox cleared; reversible context eviction + OSS AI-risk taxonomy coverage |
| 2026-08-07 | Full ingest K249–K252 (ARIA / post-training taxonomy / NL→LTL / HarnessOpt-Bench); all REFERENCE; Phase-1 cybersec bullets restored | Inbox cleared; instruction-backdoor + harness-opt + adaptation governance coverage |
| 2026-08-06 | Full ingest K244–K248 (Trident / HoRFFI / Gradient Immunity / chiplet / PIMiner); PIMiner MIT lab clone ~28MB; Phase-1 cybersec bullets restored after federation sync | Inbox cleared; agent PI RT + malicious-FT gate + DRL/RFFI/chiplet coverage |
| 2026-08-05 | Full ingest K241–K243 (Wi-Fi broadcast / AirKey / adaptive TTS) + UniEvo/SIDPP OOD stubs; Phase-1 cybersec bullets restored after federation sync | Inbox cleared; wireless side-channel + TTS budget coverage |
| 2026-08-04 | Full ingest K236–K240 (ART-PDDL / OpenART / Salami / MedPRESS / GradCuit); OpenART AGPL lab clone; collusive-memory Phase-1 | Inbox cleared; agent RT + memory coalition coverage |
| 2026-08-03 | Full ingest K233–K235 (CWEEP / STAIR / TokTier) + Joas PDF egress archive; buffer-overflow → validated; eCPPT cram brief | Inbox cleared; RTL CWE lint clone; hierarchical repair + exact tokenize policy wires |
| 2026-07-31 | Phase-1 full sweep — 4 alwaysApply agent-security rules + CLAUDE Phase-1; stamps policy≈65 / wont≈113 / deferred≈16; zero unwired | Agent-security harness wired; REFERENCE/trainers explicitly wont_wire |
| 2026-07-31 | Full ingest K230–K232 (TCA-SIR, CoGate, AISPA) — all REFERENCE; SystemPromptIndex LICENSE watch; prod+poker+TipDrop+Atto briefs | Inbox cleared; secure codegen + system-prompt governance |
| 2026-07-30 | Full ingest K225–K229 (RFFI temperature, GPT-Red, InferScale, KAMR, ByDeWay-V2) — InferScale GO ~1.4MB; prod+poker+TipDrop+Atto briefs | Inbox cleared; wireless auth + self-play red-team + KV-injection security |
| 2026-07-29 | Full ingest K220–K224 (evidential ceiling, Concept2Scenario, agent containment, IH-B, KuTIE/VulnCare) — 5 sources, 5 concepts, 3 entities; GO clones ~6MB; prod+poker+TipDrop+Atto briefs | Inbox cleared; agent-eval + K8s remediation coverage |
| 2026-05-12 | Workspace forked from `wiki-template/` (SEO wiki) | Reused proven schema instead of re-deriving |
| 2026-05-12 | Inventoried 227 PDFs from `ebooks Joas` Drive folder via Playwright DOM scrape | Drive API search did not return contents of shared folders; Playwright extraction got every file ID |
| 2026-05-12 | Cross-linked to 4 sibling wikis (OSINT, image-gen, SEO, 3d-printing) | Cybersecurity intersects all four — OSINT tradecraft, deepfakes, web-app sec, physical-pentest hardware |
| 2026-05-12 | Full maintenance lint pass — wiki green across all 8 checks | Fixed CLAUDE.md OSINT path (extra `Desktop/`), `@@` typo, and trailing-period regex bug. Future sessions can trust the lint as a green-light gate. |
| 2026-05-13 | Phase-1 deep-dive adoptions for 4 K42-routed tools (cua, fuzzyai, pentest-ai-agents, pydns-scanner) — 10 new pages + 17 existing pages updated | Wiki now has structured coverage of agent-VM sandboxing, LLM adversarial fuzzing (PAIR + Crescendo), LLM-pentest automation (Tier 1/2 model), and DNS server discovery as a distinct recon discipline. Cross-wiki backlinks to @osint-wiki/entities/tools/cua.md + @osint-wiki/entities/tools/fuzzyai.md established. |

---

## Backlog

**Higher priority:**

- Friend operator lab playbook shipped 2026-08-02 (`operator-lab-playbook` + pillars + tracked brief `briefs/2026-08-02_friend-operator-lab-playbook.md`) — **keep brief current after every relevant ingest** (CLAUDE.md step 9b). Next: Phase-0 Ollama/vLLM local install stamps only if friend adopts on a named box
- CyberStrike Phase-0 CONDITIONAL-GO 2026-08-02 — clone only; human VM install + lab validation before promoting maturity; no host npm -g / MCP until asked
- Continue deep-reads — OSINT Overview PT.1 (chunked); Buffer Overflow / eCPPT / CTH intro closed 2026-08-03
- Add `concepts/exploration-graph-dead-ends.md`-style page for "techniques that no longer work" — defenders keep patching, exploits keep rotting (responsible-disclosure already done)
- Stub @concepts/web-vitals.md in @seo-wiki/ so the cross-wiki ref resolves both ways (currently using @seo-wiki/concepts/local-seo-foundations.md as the anchor)

**Lower priority:**

- Bidirectional cross-wiki backlink scrubber — when the OSINT/SEO/etc wikis add backlinks to our pages, run a sweep to make sure `@cybersecurity-wiki/...` mentions resolve
- Per-certification cram-sheet briefs (OSCP, CRTO, eCPPT) staged in `briefs/`
- Threat-actor profile expansion beyond the current 4 — APT41 (China-attributed), FIN7 (criminal), Volt Typhoon (China — critical-infrastructure focus), Scattered Spider (criminal social-eng specialist)
- Spanish / Portuguese page mirroring for the kid-safety subset (corpus is bilingual EN+PT-BR — currently treated as siblings, could be elevated)
- Per-tool deep-reads: BloodHound + Cobalt Strike + Caldera entity pages currently `draft`; ingest the canonical SpecterOps / Fortra / MITRE docs to upgrade them
