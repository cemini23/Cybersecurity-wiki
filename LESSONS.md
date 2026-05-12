# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## [2026-05-12] Bootstrapping the wiki from a 227-PDF Drive folder

- Google Drive API's `parentId = '<id>'` query returns empty for folders that are shared-with-me (only the folder metadata itself shows up, not the contents). Workaround: Playwright over the `drive.google.com/drive/folders/<id>` URL, then `document.querySelectorAll('[data-id]')` to extract file IDs + tooltip-derived titles. 227 files in ~3 scrolls.
- For a corpus this size, deep-reading every source is not viable in a session. Strategy: generate one source stub per file (frontmatter + Drive link + provenance), then deep-read a curated subset (~10) to anchor real content in the most-cited concept pages. The rest stays `read_status: unread-stub` until an actual query needs that page.
- Many corpus titles are bilingual (English + Portuguese) duplicates of the same content. Treat the PT-BR version as the canonical source-page and link the EN as `## Related translations` rather than maintain parallel pages.
- The `Related Wikis` cross-link table is most valuable when each row spells out the **shared territory** between the two wikis — not just a path. Without that, the LLM treats all sister-wiki references the same. With it, it knows when an OSINT query genuinely needs OSINT-wiki vs cybersecurity-wiki context.
