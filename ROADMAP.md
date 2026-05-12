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
- [ ] Deep-read top 10 PDFs to upgrade key concept pages from `draft` to `validated`
- [ ] Periodic lint passes — first one before publishing

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

---

## Backlog

**Higher priority:**

- Deep-read 10 anchor PDFs to give concept pages real content (currently `draft` maturity)
- Add a `concepts/responsible-disclosure.md` page referenced from the ethics section of CLAUDE.md
- Add `concepts/exploration-graph-dead-ends.md`-style page for "techniques that no longer work" — defenders keep patching, exploits keep rotting

**Lower priority:**

- Bidirectional backlink scrubber — when the OSINT/SEO/etc wikis add backlinks to our pages, run a sweep to make sure `@cybersecurity-wiki/...` mentions resolve
- Per-certification cram-sheet briefs (OSCP, CRTO, eCPPT) staged in `briefs/`
- Threat-actor profile expansion (APT28 page is a stub; the corpus has one APT28 PDF; the broader threat-intel community has many more)
- Spanish / Portuguese page mirroring for the kid-safety subset (corpus is bilingual EN+PT-BR)
