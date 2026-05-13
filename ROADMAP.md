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
- [ ] Continue deep-reads: next batch should target Buffer Overflow, eCPPT Notes, OSINT Overview, Threat Hunting
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
| 2026-05-12 | Workspace forked from `wiki-template/` (SEO wiki) | Reused proven schema instead of re-deriving |
| 2026-05-12 | Inventoried 227 PDFs from `ebooks Joas` Drive folder via Playwright DOM scrape | Drive API search did not return contents of shared folders; Playwright extraction got every file ID |
| 2026-05-12 | Cross-linked to 4 sibling wikis (OSINT, image-gen, SEO, 3d-printing) | Cybersecurity intersects all four — OSINT tradecraft, deepfakes, web-app sec, physical-pentest hardware |
| 2026-05-12 | Full maintenance lint pass — wiki green across all 8 checks | Fixed CLAUDE.md OSINT path (extra `Desktop/`), `@@` typo, and trailing-period regex bug. Future sessions can trust the lint as a green-light gate. |
| 2026-05-13 | Phase-1 deep-dive adoptions for 4 K42-routed tools (cua, fuzzyai, pentest-ai-agents, pydns-scanner) — 10 new pages + 17 existing pages updated | Wiki now has structured coverage of agent-VM sandboxing, LLM adversarial fuzzing (PAIR + Crescendo), LLM-pentest automation (Tier 1/2 model), and DNS server discovery as a distinct recon discipline. Cross-wiki backlinks to @osint-wiki/entities/tools/cua.md + @osint-wiki/entities/tools/fuzzyai.md established. |

---

## Backlog

**Higher priority:**

- Continue deep-reads — Buffer Overflow series (4 PDFs), eCPPT Exam Notes, OSINT Overview PT.1 (was too long for single read; need to chunk), Threat Hunting (eLearnSecurity intro PDF)
- Add `concepts/exploration-graph-dead-ends.md`-style page for "techniques that no longer work" — defenders keep patching, exploits keep rotting (responsible-disclosure already done)
- Stub @concepts/web-vitals.md in @seo-wiki/ so the cross-wiki ref resolves both ways (currently using @seo-wiki/concepts/local-seo-foundations.md as the anchor)

**Lower priority:**

- Bidirectional cross-wiki backlink scrubber — when the OSINT/SEO/etc wikis add backlinks to our pages, run a sweep to make sure `@cybersecurity-wiki/...` mentions resolve
- Per-certification cram-sheet briefs (OSCP, CRTO, eCPPT) staged in `briefs/`
- Threat-actor profile expansion beyond the current 4 — APT41 (China-attributed), FIN7 (criminal), Volt Typhoon (China — critical-infrastructure focus), Scattered Spider (criminal social-eng specialist)
- Spanish / Portuguese page mirroring for the kid-safety subset (corpus is bilingual EN+PT-BR — currently treated as siblings, could be elevated)
- Per-tool deep-reads: BloodHound + Cobalt Strike + Caldera entity pages currently `draft`; ingest the canonical SpecterOps / Fortra / MITRE docs to upgrade them
