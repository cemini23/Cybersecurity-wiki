---
title: Friend day-1 Cursor setup — call checklist + /goal paste
type: brief
target: hands-on
created: 2026-08-05
updated: 2026-08-05
---

# Friend day-1 — remote Cursor setup (call + /goal)

**Audience:** Friend who has only used browser ChatGPT / Gemini.  
**Claudio:** on voice/video call — does **not** touch his machine.  
**Primary research later:** AI lab playbook (`briefs/2026-08-02_friend-operator-lab-playbook.md`).  
**Today:** Cursor + Dual-wiki (Cyber + OSINT OPSEC) + `claude-ds` + `/route` — **not** the Flash-class lab box.

---

## How the call works

1. Claudio walks him through **PART A** (manual, browser + installs) — pause until each checkbox is done.
2. Friend opens Cursor on the kit folder, opens **Agent** chat, pastes **PART B** (everything inside the fenced `/goal` block).
3. Agent runs autonomously; when it prints **YOUR TURN (manual)**, Claudio coaches those UI/key steps.
4. End when Agent prints the pass/fail Success Criteria table and `briefs/friend-day1-cheatsheet.md` exists.

**Hard stops (say out loud):** never paste API keys into Cursor chat · never `git push` unless Claudio says push OK · no TipDrop Discord / Stripe · no Ollama / big model downloads today · no offensive tool host installs.

---

## PART A — Before pasting /goal (Claudio reads; friend clicks)

Do these in order. Agent cannot do account signups for him.

### A1. Accounts (browser)

- [ ] **GitHub** account — signed in. Email Claudio his GitHub username.
- [ ] Claudio invites him to private **`cemini23/llm-wiki-by-cemini`** — friend **Accepts** invite (email or github.com/notifications).
- [ ] Confirm he can open (while logged in): https://github.com/cemini23/Cybersecurity-wiki (public) and https://github.com/cemini23/llm-wiki-by-cemini (private — 404 until invite accepted).
- [ ] **DeepSeek** platform account → create API key → leave tab open (https://platform.deepseek.com/api_keys). Do **not** paste key into chat.
- [ ] **OpenRouter** account → create API key → leave tab open (https://openrouter.ai/keys). Free models are enough for day-1 easy lane.
- [ ] **Cursor** account — will sign in during A3 (https://cursor.com — download for his OS).
- [ ] Optional day-1: **xAI / Grok** account for later mid/hard route (https://console.x.ai) — can defer if tired; research works without it.

### A2. System tools (install if missing)

**Windows 11**

- [ ] Git: https://git-scm.com/download/win (defaults OK; enable “Git from command line”)
- [ ] Node.js **LTS**: https://nodejs.org
- [ ] PowerShell **7**: `winget install Microsoft.PowerShell` or https://aka.ms/powershell
- [ ] Close and reopen Terminal after installs

**macOS**

- [ ] Xcode CLT / Git: Terminal → `xcode-select --install` if `git` missing
- [ ] Node LTS: https://nodejs.org or `brew install node` if he has Homebrew
- [ ] Optional: `brew install powershell` (kit scripts prefer `pwsh`; bash shims also work after adopt)

**Either OS — verify in a new terminal:**

```text
git --version
node --version
npm --version
```

Windows also: `pwsh --version`

### A3. Cursor app (manual UI)

- [ ] Download + install Cursor from https://cursor.com
- [ ] Open Cursor → **Sign in**
- [ ] **Settings** (gear / `Ctrl+,` or `Cmd+,`) → **Models** (or Cursor Settings → Models):
  - Enable **Claude** models available on his plan (at least one Sonnet/Opus-class if offered)
  - Enable **Auto / Composer** (or current default agent model) if listed
  - If **Grok** appears in the model list — enable for later hard fallback (optional day-1)
  - Leave exotic/local models off unless Claudio says otherwise
- [ ] **Settings → Agent** (names vary by Cursor version):
  - Turn **Auto-run** / **YOLO** / auto-approve tools **ON** (needed so `/route` last-resort does not stall)
  - Prefer **Agent** mode for the setup chat (not Ask-only)
- [ ] **Settings → Features / Privacy** (if shown): default OK for day-1; do not disable indexing entirely
- [ ] Optional: Settings → General → note which **plan** he is on (Pro / Business / etc.) — tell Claudio for billing coaching

### A4. Bootstrap folder + clone kit (terminal — still manual)

Pick one home for Cemini research (friend chooses; Claudio suggests):

| OS | Suggested umbrella |
|----|--------------------|
| Windows | `C:\dev\cemini-lab\` |
| macOS | `~/Projects/cemini-lab/` |

```powershell
# Windows (PowerShell 7)
New-Item -ItemType Directory -Force -Path C:\dev\cemini-lab | Out-Null
cd C:\dev\cemini-lab
git clone https://github.com/cemini23/tipdrop-workspace-kit.git tipdrop-kit
cd tipdrop-kit
git checkout master
git pull --ff-only
```

```bash
# macOS / Linux
mkdir -p ~/Projects/cemini-lab
cd ~/Projects/cemini-lab
git clone https://github.com/cemini23/tipdrop-workspace-kit.git tipdrop-kit
cd tipdrop-kit
git checkout master
git pull --ff-only
```

- [ ] Clone finished without auth errors (kit is **public**)
- [ ] Cursor → **File → Open Folder** → open the **`tipdrop-kit`** folder (not the parent only)
- [ ] Wait until Cursor finishes indexing (status bar)
- [ ] Open **Agent** chat (not Composer-only if that blocks terminal tools)
- [ ] Paste **PART B** below (from `/goal` through the end of the fence)

### A5. Keys file (do after Agent creates the template — or now if you prefer)

When Agent says so (or now):

```powershell
# Windows
New-Item -ItemType Directory -Force -Path $env:USERPROFILE\.cemini | Out-Null
Copy-Item .\config\llm-routing.env.example $env:USERPROFILE\.cemini\llm-routing.env
notepad $env:USERPROFILE\.cemini\llm-routing.env
```

```bash
# macOS
mkdir -p ~/.cemini
cp config/llm-routing.env.example ~/.cemini/llm-routing.env
open -e ~/.cemini/llm-routing.env   # or: nano ~/.cemini/llm-routing.env
```

Friend types **only** in that file (never in chat):

```text
DEEPSEEK_API_KEY=...his key...
OPENROUTER_API_KEY=...his key...
ROUTE_PROFILE=claudio
ROUTE_ALWAYS_APPROVE=1
```

- [ ] Save file · close editor · tell Claudio “keys file saved” (do **not** read keys aloud)

---

## PART B — Paste into Cursor Agent (start at the next line)

```
/goal Friend day-1: set up Cursor research harness (Cyber wiki primary + OSINT OPSEC sidecar + tipdrop-kit route/claude-ds + federation skills + MCP/plugins) for an AI-novice operator on a call with Claudio — all SCs green or explicit blockers; write friend-day1-cheatsheet.md; no TipDrop product, no Ollama, no lab GPU weights

── CONTEXT ──
- Operator: friend (new to AI tooling — only browser ChatGPT/Gemini before today). Claudio on voice call; friend clicks everything.
- Working dir: tipdrop-workspace-kit clone already open in Cursor (PART A4). Detect OS (Windows vs macOS) and use matching paths.
- Primary research canon: Cybersecurity wiki. OPSEC sidecar: private OSINT wiki (llm-wiki-by-cemini). Lab playbook: briefs/2026-08-02_friend-operator-lab-playbook.md (in Cyber repo after clone) — do NOT install abliterated Flash / vLLM / Strix host tools today.
- Umbrella (create if missing): Windows C:\dev\cemini-lab\ · macOS ~/Projects/cemini-lab/
- Kit hosts scripts only — WorkDir for research = Cybersecurity-wiki path after clone.
- Constraints:
  - NEVER ask him to paste API keys / PATs into chat. Keys only in ~/.cemini/llm-routing.env or OS env.
  - NO git push unless operator says "push OK".
  - NO TipDrop Discord/Stripe/scanner LIVE. NO Ollama pull. NO multi-GB model downloads.
  - NO curl|sh host installs of offensive tools. No CyberStrike/Strix host install today.
  - Prebind: only install from URLs/scripts already in tipdrop-kit or allowlisted public GitHub (cemini23/*, agent-toolkit-demo).
  - Speak in plain language in the FINAL DELIVERABLE (novice). During work, print clear YOUR TURN (manual) blocks when he must click Settings or type keys.
  - Profile: ROUTE_PROFILE=claudio (cloud route; no Ollama required).

── SUCCESS CRITERIA (ALL MUST BE TRUE) ──

A — Machine + kit
1. OS/arch/RAM/free-disk recorded in briefs/friend-day1-setup-report.md (create under kit briefs/ or Cyber briefs/ if Cyber already cloned — prefer kit `.local/reports/friend-day1-YYYY-MM-DD.md` if briefs gitignored; also write tracked copy path he can open).
2. tipdrop-kit on latest master (ff-only); HEAD SHA recorded.
3. Git, Node/npm, and pwsh-or-bash available; versions in report.

B — Dual wikis
4. Cybersecurity-wiki cloned under umbrella/projects/ (or kit/projects/) via install-federation-wikis.ps1 or direct git clone; wiki/index.md readable.
5. llm-wiki-by-cemini cloned same way; wiki/index.md readable. If private clone fails (invite), STOP with YOUR TURN: accept GitHub invite, then re-run — do not invent wiki content.
6. Cursor multi-root OR clear instructions in cheatsheet: open Cyber as daily folder; keep OSINT + kit accessible. Prefer creating a `.code-workspace` under umbrella that includes tipdrop-kit + Cybersecurity-wiki + llm-wiki-by-cemini.

C — claude-ds + route always-approve
7. install-claude-ds.ps1 run successfully; `claude-ds` (or shim) on PATH for new terminals.
8. adopt-route-always-approve.ps1 run; ROUTE_ALWAYS_APPROVE noted; Claude-ds skip-permissions default.
9. ~/.cemini/llm-routing.env exists (from example). Agent verifies file exists and non-empty DEEPSEEK_API_KEY / OPENROUTER_API_KEY **names present** without printing secret values. If missing → YOUR TURN notepad instructions (PART A5).
10. Smoke: route-task -Profile claudio -DryClassify "easy: summarize a wiki note" succeeds.
11. Smoke: route-task -Profile claudio -WorkDir <Cybersecurity-wiki absolute path> "easy: In one short paragraph, what is the operator lab playbook authorization floor?" returns a sensible summary (or claude-ds/OpenRouter fallback with notice). Quote WorkDir if path has spaces.

D — Skills, rules, toolkit
12. install-agent-toolkit.ps1 run (cursor-audit + super-audit into kit .cursor/skills).
13. sync-federation-cursor-skills.ps1 run if present; else copy canon skills goal, route, to-issues, grill-with-docs, i-have-adhd (+ cursor-audit, super-audit) to user-global ~/.cursor/skills (or %USERPROFILE%\.cursor\skills) AND into Cybersecurity-wiki/.cursor/skills if that repo has/should have .cursor.
14. User-global or workspace rules include cemini-goal-skill / tipdrop-route-outsource or cemini-route-outsource (alwaysApply route outsource). Reload Window reminder printed.

E — MCP + Claude Code plugins (day-1 tier)
15. Configure minimal MCP: github + fetch. Use kit mcp.json.example as base → user-global ~/.cursor/mcp.json OR workspace .cursor/mcp.json. YOUR TURN for GitHub PAT: scopes repo (private OSINT) — he creates at github.com/settings/tokens and pastes into mcp.json **himself** in an editor, not chat. Agent may open the example file and mark the placeholder.
16. After claude-ds works: launch one non-interactive note that he should run later in an interactive claude-ds session: /plugin install commit-commands@claude-plugins-official ; github@claude-plugins-official ; context7@claude-plugins-official. Record in cheatsheet. Skip ralph-loop, exa (paid), TipDrop Discord skills as daily drivers.
17. Document Grok CLI as optional: install + `grok login` when he wants mid/hard code; research day-1 does not require it. If grok already installed, do not break auth.

F — Cursor UI checklist completed (manual confirmation)
18. Write into cheatsheet a **Cursor Settings checklist** he can re-read: Models enabled; Agent Auto-run ON; which folder to open daily; how to start Agent chat; how to say "route this".
19. Operator verbally confirms (Agent asks once in YOUR TURN) that Settings → Models and Auto-run match the checklist — mark SC18/19 pass when he says "done".

G — Teaching artifacts
20. Create briefs/friend-day1-cheatsheet.md in tipdrop-kit (and copy or pointer under Cybersecurity-wiki/briefs/ if Cyber is writable) covering: what Cursor vs ChatGPT is; dual-wiki table; when to /goal vs /route vs claude-ds; OSINT OPSEC reading order (from friend playbook); hard stops; smoke commands; plugin/MCP list.
21. Append a short entry to tipdrop-kit wiki/log.md OR Cyber wiki/log.md noting day-1 setup date + machine summary (no secrets).
22. Print final SC pass/fail table + next-session: read friend playbook Dual-wiki + §0–1 only (no hardware buy today).

── OPERATING RULES — NON-NEGOTIABLE ──
1. PLAN FIRST — numbered phases; show plan in chat before destructive moves.
2. WORK AUTONOMOUSLY — only stop for YOUR TURN (manual) or true blockers (invite, missing keys, disk full).
3. Plain-language YOUR TURN blocks: exactly what to click, what to type, what to say when finished.
4. SELF-VERIFY — run version checks, test paths, DryClassify, one easy route smoke.
5. DEBUG YOURSELF — fix PATH/shim/permission issues; do not leave broken shims.
6. No secrets in reports, cheatsheets, log, or chat.
7. Prefer kit scripts over ad-hoc installs.
8. STAY ON GOAL — lab hardware / Strix install = note for later, do not do today.
9. IF BLOCKED — leave machine in a clean recoverable state; list exact resume commands.
10. CHECK EVERY SC before stopping.

── QUALITY BAR ──
Novice-readable cheatsheet; reproducible commands; Win + Mac notes where commands differ; cite kit script paths.

── EXECUTION PLAN (follow; adapt paths to OS) ──

Phase 0 — Inventory
- Record OS, shell, git/node versions, free disk, umbrella path.
- Confirm cwd is tipdrop-kit root (CLAUDE.md or START-HERE.md + scripts/route-task.ps1).

Phase 1 — Federation wikis
- Run: powershell/pwsh -ExecutionPolicy Bypass -File ./scripts/install-federation-wikis.ps1
  (or on Mac: pwsh ./scripts/install-federation-wikis.ps1)
- If script assumes David Desktop paths, override -Workspace to umbrella/tipdrop-kit and ensure projects/ receives Cybersecurity-wiki + llm-wiki-by-cemini.
- Fallback: git clone https://github.com/cemini23/Cybersecurity-wiki.git and git clone https://github.com/cemini23/llm-wiki-by-cemini.git into <umbrella>/projects/
- Verify both wiki/index.md files.

Phase 2 — Workspace file
- Write <umbrella>/cemini-friend-lab.code-workspace with folders: tipdrop-kit, Cybersecurity-wiki, llm-wiki-by-cemini.
- YOUR TURN: File → Open Workspace from File → select that .code-workspace (or confirm multi-root).

Phase 3 — Keys template + claude-ds + adopt
- Ensure ~/.cemini/llm-routing.env from config/llm-routing.env.example; YOUR TURN to paste keys if empty.
- pwsh -File ./scripts/install-claude-ds.ps1
- pwsh -File ./scripts/adopt-route-always-approve.ps1
- New shell smoke: claude-ds --help or equivalent; route-task DryClassify.

Phase 4 — Toolkit + skills sync
- pwsh -File ./scripts/install-agent-toolkit.ps1
- Run sync-federation-cursor-skills.ps1 if present; else manual copy of skills listed in SC13.
- YOUR TURN: Command Palette → Developer: Reload Window

Phase 5 — MCP
- Prepare mcp.json from example with github + fetch only.
- YOUR TURN: create GitHub PAT (repo scope), paste into mcp.json locally, Reload Window, enable MCP servers in Cursor Settings → Tools & MCP if toggles exist.
- Skip lazy-tool, prod-mcp, stash (Claudio prod — not for friend).

Phase 6 — Route smoke on Cyber
- route-task -Profile claudio -WorkDir "<abs path to Cybersecurity-wiki>" "easy: …authorization floor…"
- If path has spaces, quote or use /tmp symlink pattern from route skill.

Phase 7 — Cheatsheet + report + log
- Write friend-day1-cheatsheet.md + setup report; log line; SC table.

── FINAL DELIVERABLE ──
Per-SC pass/fail · paths created · cheatsheet location · exact YOUR TURN items still open · first research homework (friend playbook Dual-wiki + §0 only)
```

---

## PART C — After Agent says done (Claudio coaches, ~10 min)

- [ ] Open workspace file `cemini-friend-lab.code-workspace`
- [ ] Open `briefs/friend-day1-cheatsheet.md` (kit) — skim together
- [ ] Friend practice phrase: **“route this: summarize the operator lab authorization floor”** in Agent on Cyber folder
- [ ] Friend practice: open `briefs/2026-08-02_friend-operator-lab-playbook.md` in Cyber — read Dual-wiki + §0 only tonight
- [ ] Remind: ChatGPT/Gemini browser still fine for casual Qs; **lab research + wiki edits** use Cursor + route so cost stays on DeepSeek/OpenRouter
- [ ] Homework: OSINT OPSEC list in playbook (fingerprint-suite → …) — read-only, no tool installs
- [ ] Schedule lab-hardware call separately (path A VRAM) — not today

---

## Claudio pre-call pack

1. Invite GitHub user to `cemini23/llm-wiki-by-cemini` **before** the call  
2. Send this file (or raw PART B) via Signal/email/Drive — he needs PART A even if Agent paste is later  
3. Have DeepSeek + OpenRouter signup links ready  
4. Optional: Cursor Pro reimbursement / plan choice decided  
5. Keep TipDrop product / David 5090 / Ollama out of the script unless he asks  

## Related

- Friend playbook: `briefs/2026-08-02_friend-operator-lab-playbook.md`  
- Kit: `START-HERE.md`, `scripts/install-claude-ds.ps1`, `scripts/adopt-route-always-approve.ps1`, `scripts/install-federation-wikis.ps1`, `docs/OPTIONAL-PLUGINS-AND-MCP.md`  
- Route skill: tipdrop-kit `.cursor/skills/route/SKILL.md`
