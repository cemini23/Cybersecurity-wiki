# Lessons

A running log of lessons learned while managing this workspace. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## [2026-10-02] Run grok jobs one at a time — concurrent headless sessions kill each other

- Launching **five** `grok-offload run` jobs at once lost **two** of them mid-read: each died after printing only its preamble, with an empty error log. `ps` showed the survivors still working, so the losses were silent.
- Cause: grok coordinates headless sessions through one **leader socket** (`~/.grok/leader.sock`). Parallel launches contend for it and some sessions lose.
- `scripts/grok_offload.sh` now **queues by default**: each job takes a `mkdir` lock before starting grok and releases it on exit, so runs serialize. A job waiting on the lock reports state `queued`, not `running`. `--no-lock` opts out.
- Stale locks are stolen automatically (holder pid no longer alive), so a killed tab cannot wedge the queue.
- Verified: three concurrent jobs → one `running`, two `queued` → all three completed. Previously two of five died.
- If you genuinely need throughput, prefer `--no-lock` with **two** jobs rather than five; the ceiling was not measured, only the failure.

---

## [2026-09-30] Offload long grok runs — a terminal tab close kills them

- Headless `grok -p` / `grok --prompt-file` dies when its terminal tab closes mid-run. Three deep-read restarts happened in one session before this was diagnosed.
- **Run it detached.** `scripts/grok_offload.sh` (also on PATH as `grok-offload`) starts grok under `nohup` with stdin detached, writes `out.md` / `err.log` / `rc` into `.scratch/grok/<name>/`, and gives `status` / `wait` / `list` to poll without holding a tab open.
- macOS has **no `setsid`** (it is util-linux, not BSD). `nohup` + `disown` + `</dev/null` is the detach path here.
- Grok must run **outside the Claude Code sandbox**: the sandbox denies `cli-chat-proxy.grok.com` and grok's session directory, so grok cannot start inside it.
- Keep `--cwd` inside the project. Pointing it outside stalls grok. Use `--prompt-file` for long prompts, and pass the text as a **file path grok reads itself** — inlining a 100 KB paper into `-p` makes grok think the message was truncated.
- Grok narrates: expect one preamble line ("I'll read the file and ...") before the answer. Strip it before parsing.

---

## [2026-08-03] Friend brief is a living start-here — update after every relevant ingest

- Tracked brief: `briefs/2026-08-02_friend-operator-lab-playbook.md` (`.gitignore` allowlist). It is the friend’s ordered checklist; pillar wiki pages hold depth.
- **Standing rule:** after each ingest / Phase-0 / deep-read that touches local AI, owned lab, product pentest, bounty, AI harnesses, or ASVS — sync the friend brief (or log `friend brief: n/a`). Canonized as ingest step **9b** in `CLAUDE.md`.
- Gitignored Phase-0 / ASVS / lab briefs stay machine-local detail; the tracked friend brief must still point at them and carry any checklist change the friend needs without opening those files.

---

## [2026-05-12] Bootstrapping the wiki from a 227-PDF Drive folder

- Google Drive API's `parentId = '<id>'` query returns empty for folders that are shared-with-me (only the folder metadata itself shows up, not the contents). Workaround: Playwright over the `drive.google.com/drive/folders/<id>` URL, then `document.querySelectorAll('[data-id]')` to extract file IDs + tooltip-derived titles. 227 files in ~3 scrolls.
- For a corpus this size, deep-reading every source is not viable in a session. Strategy: generate one source stub per file (frontmatter + Drive link + provenance), then deep-read a curated subset (~10) to anchor real content in the most-cited concept pages. The rest stays `read_status: unread-stub` until an actual query needs that page.
- Many corpus titles are bilingual (English + Portuguese) duplicates of the same content. Treat the PT-BR version as the canonical source-page and link the EN as `## Related translations` rather than maintain parallel pages.
- The `Related Wikis` cross-link table is most valuable when each row spells out the **shared territory** between the two wikis — not just a path. Without that, the LLM treats all sister-wiki references the same. With it, it knows when an OSINT query genuinely needs OSINT-wiki vs cybersecurity-wiki context.
