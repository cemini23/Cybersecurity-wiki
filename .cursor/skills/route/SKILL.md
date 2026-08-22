---
name: route
description: >-
  Sort any task into easy / mid / hard / money and outsource it via one unified
  chain (OpenRouter free, OpenCode Zen free sidecar, Grok CLI, claude-ds /
  DeepSeek Flash family, Cursor Grok). Always-approve is the skill default. Use
  when the user says /route, "route this", "route as recommended", or asks to
  auto-pick cheap executors. Sibling habit to "hand it to grok" - handoff-to-grok
  is under-the-hood, not a separate workflow. Base case for all Cemini projects -
  not TipDrop-specific.
license: MIT
metadata.author: cemini23
metadata.version: "2.4.1"
federation: true
---

# /route - unified task sorter (easy · mid · hard · money)

**Cemini base-case task router.** Say **route as recommended** / `/route` / `route this`. Works for Atto, CCC, OSINT, TipDrop, wikis - whatever the current project WorkDir is.

**Canon script host:** private repo [`cemini23/agent-toolkit`](https://github.com/cemini23/agent-toolkit) (`~/Projects/agent-toolkit`, or `/opt/cemini/agent-toolkit` on prod). Set `ROUTE_KIT` if needed. TipDrop workspace-kit only has deprecated redirect stubs. `handoff-to-grok.ps1` is an implementation helper called by `route-task` - operators should not maintain a separate "handoff vs route" habit.

## Skill contract (non-negotiable)

**Always-approve is the default on every route executor - all machines, all profiles.**

| Executor | Default (MUST) | Opt out only when operator asks |
|----------|----------------|----------------------------------|
| **Grok CLI** (plan mid / implement hard) | `--always-approve` via `handoff-to-grok.ps1` | `-NoApprove` |
| **OpenCode sidecar** (live Zen free pick; easy/mid execute, hard last cheap backup) | `opencode run --auto` via `opencode-run.ps1` | `-NoApprove` / `ROUTE_OPENCODE_ASK=1` |
| **claude-ds Flash family** (`deepseek-v4-flash` or `deepseek-v4-flash-vision-exp`; easy + mid execute, mid Grok-out plan, hard Grok-out first implement) | official `dsh` + `DSH_PERMISSION_MODE=danger-full-access` via `claude-ds.ps1` | `-NoSkipPermissions` / `CLAUDE_DS_ASK=1` |
| **claude-ds Pro** (`deepseek-v4-pro`; audits + hard backup only) | official `dsh` + `DSH_PERMISSION_MODE=danger-full-access` via `claude-ds.ps1` | `-NoSkipPermissions` / `CLAUDE_DS_ASK=1` |
| **Cursor Grok** (fallback plan/implement) | Auto-run / full tool approve | UI Auto-run off / ask mode |
| Easy API scripts | no tool sandbox - N/A | - |

**PATH name stays `claude-ds`.** Worker is official DeepSeek Harness (`dsh`, pin `install-dsh.ps1` → `~/.dsh-cemini`). Isolated Claude Code at `~/.deepseek-claude` is **fallback** (`CLAUDE_DS_FORCE_LEGACY=1` or dsh cannot boot). On prod, `deepseek-claude` may still exist as that fallback. Resolve: `claude-ds` → kit `claude-ds.ps1` / `claude-ds.sh` → `deepseek-claude` → `~/.deepseek-claude/deepseek-claude`. Do **not** put `dsh` on PATH as a second coding loop — the shim owns it. **OpenCode is a sidecar executor**, not a `claude-ds` replacement (2026-08-12 Phase-0 NO-GO reversed **only** for opt-in Zen-free `opencode run`; model is a **live catalog pick**, not a locked id). Missing `opencode` skips to Flash with an install hint. Never `curl | bash`. Never rewrite `~/.config/opencode/opencode.json`.

Without always-approve, headless tools cancel → chain falls through to Cursor → burns quota. That is a skill bug, not an operator preference.

Secret deny rules on Grok still apply (K172). LIVE Discord / `.env` flips still need explicit OK.

Adopt on any machine once: `pwsh -File ~/Projects/agent-toolkit/scripts/adopt-route-always-approve.ps1`

## Parse

Accept `/route <task>`, `route as recommended: …`, or a message starting with `/route` / `route this:`.

- **Empty body:** ask what the task is.
- **Body present:** classify, announce lane + why, then **outsource** (never implement in the parent Cursor session except Cursor Grok fallback).

## Critical: parent Cursor is not the default implementer

When this skill runs **inside Cursor Agent**:

1. Announce lane + one-line why.
2. **Easy:** shell `route-task` (OpenRouter free → OpenCode Zen free → claude-ds **Flash family**). Do not draft in Cursor. Never Pro.
3. **Mid:** pack repo/task context into the handoff (or let `route-task` auto-pack), then shell `route-task` so **Grok CLI plans** and **OpenCode then Flash family execute**. OpenCode is **not** the mid default planner — mid plan stays Grok. **Grok usage out** (`ROUTE_GROK_OUT=1` / `-SkipGrokPlan`) with no Plan: **claude-ds Flash family plans** (not Pro), then cheap execute. Usable `## Plan` already present: skip Grok → cheap execute. Grok **auth** (exit 42): tell operator `grok login` — do not treat as usage-out. If OpenCode + claude-ds/DeepSeek are out: script picks **best live OpenRouter free** model for chat execute fallback.
4. **Hard/money:** write the **plan** in this session with a **premium** model (Fable / Opus / session premium) into the handoff `## Plan` section, then shell `route-task` / `handoff-to-grok` so **Grok CLI implements**. **Grok usage out + usable Plan:** **claude-ds Flash family**, then **Pro** (hard backup), then **OpenCode Zen free**, else Cursor Grok. Hard SkipGrok with no Plan still needs Cursor premium Plan (quality gate). Else Task `grok-implementer` / Cursor Grok implement.
5. Summarize executor results only (lane, executor chain, verify evidence, residual risk from `_route_runs/`). Re-implement in the parent Cursor session when the script prints **Cursor Grok fallback** or **claude-ds HANG - Cursor parent takeover** (watchdog). Verify evidence still required - no status-only "done".

Preferred operator habit: `route-task` from a project terminal - or `/route` in Agent when Cursor context/premium plan is needed.

```bash
# Mac (shims on PATH) - cwd = project
cd ~/Projects/atto
route-task -Profile claudio "route as recommended: fix allowlist drift"
# Refresh shims once:
pwsh -File ~/Projects/agent-toolkit/scripts/adopt-route-always-approve.ps1
```

```powershell
$kit = "$HOME/Projects/agent-toolkit"
pwsh -File "$kit/scripts/route-task.ps1" -WorkDir "$HOME/Projects/atto" -Profile claudio "hard: …"
```

## WorkDir (base case)

Resolution order:

1. `-WorkDir` / `ROUTE_WORKDIR` / `CEMINI_ROUTE_WORKDIR`
2. `Repo:` / `WorkDir:` path in the task text
3. **Current project directory** (cwd with `.git` / `AGENTS.md` / `pyproject.toml` / …)
4. TipDrop scanner **only** if the task is clearly scanner/TipDrop work
5. Else fail and ask for `-WorkDir`

### Paths with spaces (Cybersecurity wiki, CCC, OSINT, …)

Federation roots like `~/Projects/Cybersecurity wiki` previously truncated at the space when `Start-Process -ArgumentList` joined tokens. **Fixed in agent-toolkit** (`Invoke-PwshScriptNamedArgs` EncodedCommand splat + `claude-ds` `Repair-SpacedWorkDirBinding`).

Operator hygiene still:

1. Prefer quoted `-WorkDir "/Users/…/Cybersecurity wiki"` (or let the `route-task` bash shim pass `"$(pwd)"`).
2. Optional: `export CLAUDE_DS_WORKDIR="$PWD"` / `export ROUTE_WORKDIR="$PWD"` before routing.
3. Smoke: `pwsh -File ~/Projects/agent-toolkit/scripts/test-route-workdir-spaces.ps1`
4. Mid/hard implement: use **`route-task` / `handoff-to-grok.ps1 --always-approve`**, not bare Task `grok-implementer` with `acceptEdits` (headless cancels writes).

## SIP + verify gates (v2.1)

Mid execute and hard/money implement require a SIP handoff: **WorkDir**, **Success criteria**, **Verify**, **NEVER**; hard/money also need a real **Plan**. Incomplete → SDR exit **3** (not silent Grok). Opt out: `-NoSip`.

After implement, `## Verify` commands run in WorkDir; failure fails the route. Opt out: `-SkipVerify`.

Mid tasks that look like multi-file/tests/LIVE/secrets auto-escalate to hard/money unless forced with `mid:` / `deepseek:`.

Run logs: `agent-toolkit/briefs/handoffs/_route_runs/`. Parent summaries must include verify evidence - no status-only "done".

## Grok-out + Flash vs vision vs Pro + OpenCode (v2.4)

**Official DeepSeek Harness** (`@deepseek-ai/dsh`, pin via `install-dsh.ps1`) is the `/route` worker behind the `claude-ds` PATH name (operator GO 2026-08-14). `-Model` writes a per-job `dsh --patch` overlay (`deepseek-v4-flash` / `deepseek-v4-flash-vision-exp` / `deepseek-v4-pro`). Always-approve is `DSH_PERMISSION_MODE=danger-full-access`. PromptFile is a file path inside the headless task (not `cat` into argv). Isolated Claude Code at `~/.deepseek-claude` remains **fallback only**. Do **not** put `dsh` on PATH or replace `claude-ds` with OpenCode. Wiki: `entities/tools/deepseek-harness.md`. Prod Node 20 stays; dsh uses a Node 24 sidecar.

**OpenCode sidecar (v2.4.1):** `opencode run --auto --dir <WorkDir> --model <id>` with prompt from a file (no `$` interpolation). Empty / alias `free` = **live Zen free pick** (`GET https://opencode.ai/zen/v1/models`, ~15 min cache) — Ox Alpha wins **while it is still listed free**, then other coding free models, then generic `-free`, then may-train free (Big Pickle / Hy3). Do **not** lock one id. Pin with `ROUTE_OPENCODE_MODEL`. Offline fallback only: `opencode/x-preview-f-free`. Inspect: `pwsh -File scripts/select-opencode-zen-free-model.ps1`. Missing binary / auth fail = skip to next fallback. Install: `pwsh -File scripts/install-opencode.ps1` (npm only, never curl|bash) then human `opencode auth login`. `ROUTE_SKIP_OPENCODE=1` disables the sidecar.

Public cursor-route 0.1.10 added `--worker opencode` with Zen free models. Private `/route` steals that adapter as a sidecar; mid plan stays Grok; PATH `claude-ds` is unchanged.

| Role | Model | When |
|------|-------|------|
| Easy **execute** (chat) | OpenRouter free | Wording / drafts; no tools; no secrets |
| Easy + mid **execute** (tools) | OpenCode Zen free, then Flash family | Cheap coding agents after OpenRouter chat (easy) or Grok plan (mid) |
| Easy + mid **execute** (paid) | `deepseek-v4-flash` or `deepseek-v4-flash-vision-exp` | After OpenCode skip/fail. Vision auto-pick on screenshot/image/png/jpg/webp/ui mock/multimodal/vision. `ROUTE_CLAUDE_DS_FLASH_MODEL` still wins |
| Mid **plan** when Grok CLI usage is out | Flash family (never Pro) | `-SkipGrokPlan` / `ROUTE_GROK_OUT=1` / Credits-RateLimit-Network fail, no usable Plan |
| Hard **implement** when Grok CLI usage is out | Flash family, then Pro, then OpenCode | SkipGrok + Plan, or Grok implement fail + Plan |
| Hard **plan** | Cursor premium | Quality gate — Pro/OpenCode do not replace this |
| Audits | Pro allowed | cursor-audit / super-audit; not `/route` easy/mid |

Override ids: `ROUTE_CLAUDE_DS_FLASH_MODEL` / `ROUTE_CLAUDE_DS_VISION_MODEL` / `ROUTE_CLAUDE_DS_PRO_MODEL`. Pin OpenCode: `ROUTE_OPENCODE_MODEL` (empty/`free` = live pick). Refresh catalog: `ROUTE_ZEN_REFRESH=1`.

| Knob | Meaning |
|------|---------|
| `-SkipGrokPlan` / `ROUTE_GROK_OUT=1` | Skip Grok; mid: Flash family plans if needed then cheap execute; hard: Flash then Pro then OpenCode if Plan usable |
| `ROUTE_SKIP_OPENCODE=1` | Disable OpenCode sidecar this run |
| `-HandoffPath path.md` | Reuse SIP handoff (after premium plan or hang resume) |
| `ROUTE_CLAUDE_DS_HANG_SECONDS` | Stall kill (default **360**) - no stdout/WorkDir mtime progress |
| `ROUTE_CLAUDE_DS_MAX_SECONDS` | Hard wall (default **2700**) |

Grok **auth** is not usage-out: print `grok login`. If a usable Plan is already on the hard handoff, Flash then Pro then OpenCode still implement before Cursor Grok.

Usable Plan = filled section (≥80 chars), not the empty hard-lane placeholder. Resume: `route-task -SkipGrokPlan -HandoffPath <handoff> "mid: execute handoff <handoff>"`.

When watchdog fires, parent Cursor **may** implement from the SIP handoff; still run Verify / claim evidence.

## Lanes (must follow)

| Lane | Meaning | Action |
|------|---------|--------|
| **easy** | Words / drafts / rewrite / wiki notes | **OpenRouter free** → **OpenCode Zen free** → **claude-ds Flash family**. Never Pro. |
| **mid** | Plan then cheap tool execute | Context pack → **Grok CLI plan** → OpenCode then Flash family. Grok usage out / no Plan → **Flash family plans** (not Pro) then cheap execute. Usable Plan → cheap execute. Hang → parent takeover. Fallbacks: Cursor Grok plan; best live OR free chat |
| **hard** | Code / tests / multi-file | **Cursor premium plan** → **Grok CLI implement**. Grok usage out + Plan → **Flash family**, then **Pro**, then **OpenCode**. Else Cursor Grok implement |
| **money** | Scoring, Stripe, Greeks, P&L, LIVE / ship | **Same as hard** + stricter money guardrails. Do not auto-LIVE. |
| **ambiguous** | Unclear | Ask: easy / mid / hard / money? |

**Fallbacks:** never hard-stop on first provider credit/usage failure - walk the chain. Grok **auth** still prints `grok login`; with usable Plan prefer Flash then Pro then OpenCode before Cursor Grok.

Force prefixes: `easy:`, `mid:` / `deepseek:` / `opencode:`, `hard:`, `money:` (first line of multi-line prompts). Bare mentions of "DeepSeek" in NEVER lists do **not** force mid - use `use deepseek` or `deepseek:` prefix. `opencode:` is mid with OpenCode-first execute (same cheap chain).

## Profiles

- Env `ROUTE_PROFILE=david|claudio` (aliases: `CEMINI_ROUTE_PROFILE`, `TIPDROP_ROUTE_PROFILE`) or `-Profile` on the script.
- Profiles no longer change easy provider order (free OR → OpenCode → Flash family for both). Kept for logging / future local opts.
- Always-approve does **not** change by profile.

## Operating rules

1. Announce lane + one-line why before acting.
2. Hard **and money**: Cursor premium writes plan; Grok CLI implements. Grok usage out: **Flash family**, then **Pro**, then **OpenCode**. Parent Cursor only as Cursor Grok fallback.
3. Money: same execute path as hard; require LIVE OK for live flips.
4. On provider credit/auth failure: try next fallback leg **and notify** (console banner + Desktop `ROUTE-FALLBACK-NOTICE.txt` with top-up link).
5. No secrets in handoff files. No LIVE Discord unless user says LIVE OK. **Do not send secrets to free OpenRouter or OpenCode Zen models** (they may log/train). Live pick prefers Ox Alpha while it is free (zero-retention) over may-train models like `opencode/big-pickle`; pin with `ROUTE_OPENCODE_MODEL` if you need a frozen id.
6. **Always pass always-approve** on Grok + OpenCode `--auto` + claude-ds unless the operator explicitly requested ask mode (`-NoApprove` / `ROUTE_OPENCODE_ASK=1` / `CLAUDE_DS_ASK=1`).
7. K172 carve-out: only the reviewed handoff path (`handoff-to-grok.ps1` / `route-task`) with scoped `--cwd`, secret deny rules, and optional `--sandbox workspace`. No free-form `grok` against home trees.
8. Mid Grok **usage** failure → **Flash family plans** then cheap execute (or fill Plan then `-SkipGrokPlan`). Mid Grok **auth** → `grok login`. Hard Grok failure + Plan → Flash then Pro then OpenCode; else **Cursor Grok implement**.
9. Do not claim done without verify evidence (or explicit SDR/block). Hang takeover still requires Verify.
10. **Skill misevolution HITL** (arXiv 2608.12851): skills can worsen with practice — no unattended auto-evolve of this skill's promote/refine cycles; changes land via HITL only. On verify fail, **reconsider the Plan, not only retry** (Vero lesson: a wrong definition burns 16 failed lemma attempts). Keep the **external eval contract**: do not rewrite `## Verify` mid-run to match a failing execution.

## PowerShell one-liners

```powershell
cd ~/Projects/agent-toolkit
.\scripts\adopt-route-always-approve.ps1   # once per machine
.\scripts\install-opencode.ps1             # optional sidecar; then: opencode auth login
.\scripts\route-task.ps1 -WorkDir ~/Projects/atto "Draft support FAQ"
.\scripts\route-task.ps1 "mid: strengthen this wiki note"
.\scripts\route-task.ps1 -Interactive "hard: Fix the allowlist drift"
.\scripts\route-task.ps1 -DryClassify "Is this Stripe soft-gate safe to ship?"
.\scripts\route-task.ps1 -NoApprove "…"   # rare: ask mode for this run only
.\scripts\route-task.ps1 -SkipGrokPlan -HandoffPath ~/path/handoff.md "mid: execute handoff ~/path/handoff.md"
$env:ROUTE_GROK_OUT = "1"   # session: skip Grok; require usable Plan
$env:ROUTE_SKIP_OPENCODE = "1"  # this run: skip Zen sidecar
.\scripts\select-openrouter-free-model.ps1  # print best live OpenRouter free model id
.\scripts\select-opencode-zen-free-model.ps1  # print best live Zen free model id
```

## Related

- `~/Projects/agent-toolkit/scripts/adopt-route-always-approve.ps1` - machine adopt
- `.../handoff-to-grok.ps1` - Grok CLI plan (`-PlanOnly`) or implement
- `.../opencode-run.ps1` / `install-opencode.ps1` - OpenCode Zen-free sidecar
- `.../ask-openrouter.ps1` / `claude-ds.ps1` - Flash family (easy/mid execute) or `-Model deepseek-v4-pro` (hard backup / audits)
- `.../lib/Get-RouteModel.ps1` - Flash / vision / Pro / OpenCode ids
- `.../lib/Test-RouteHandoffSip.ps1` - SIP contract
- `.../lib/Test-RoutePlanPresent.ps1` - usable Plan + Grok-out helpers
- `.cursor/rules/cemini-route-outsource.mdc` - always-on outsource + always-approve (`tipdrop-route-outsource.mdc` is a filename alias)
- `.cursor/rules/cemini-phase1-policy-wires.mdc` §Skill misevolution (SHE / arXiv 2608.12851) - no unattended auto-evolve of `.cursor/skills/*`; HITL on write ≠ retrieval-time safety
