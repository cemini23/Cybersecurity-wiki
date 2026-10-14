---
name: free-audit
description: >-
  Low-cost multi-model audit — Cursor packs context, Grok CLI audits + orchestrates
  claude-ds (DeepSeek V4 Flash), ≥2 live free OpenRouter models (excluding
  DeepSeek/Grok), plus an optional Gemini CLI leg on the free oauth tier. Use when
  the user says /free-audit, free audit, cheap audit, low-cost council, or wants
  multi-model review without Cursor Task spend.
license: MIT
metadata.author: cemini23
metadata.version: "1.1.0"
disable-model-invocation: true
permissions:
  - network
  - filesystem:read
  - filesystem:write
  - env
federation: true
---

# Free audit (Grok-orchestrated, low Cursor cost)

**Tier 1 only** — auditors report; they do not edit.

**Cost shape:** ~0 Cursor Task subagents. Cursor scopes + builds a pack + hands off to Grok. Grok is **auditor #1 and orchestrator**; then claude-ds / DeepSeek V4 Flash + ≥2 dynamic free OpenRouter models (no DeepSeek, no Grok/x-ai on the free legs) + an optional **Gemini CLI** leg on the free oauth tier.

Sibling skills: [cursor-audit](../cursor-audit/SKILL.md) (3× Cursor premium) · [super-audit](../super-audit/SKILL.md) (3× Cursor + paid API).

## Default auditor layout

| Slot | Channel | Role |
|------|---------|------|
| 1 | **Grok CLI** | Auditor + orchestrator + synthesizer |
| 2 | **claude-ds** / DeepSeek API `deepseek-v4-flash` | Deep reasoning / code |
| 3 | OpenRouter **free** (dynamic) | Distinct family #1 |
| 4 | OpenRouter **free** (dynamic) | Distinct family #2 |
| 5 | **Gemini CLI** (`gemini-2.5-pro`, free oauth) | Distinct family (Google) + **tool-using reader** |

Free OR selection excludes `deepseek*`, `grok*`, `x-ai/*`. Prefer family diversity (see [reference.md](reference.md)). Slot 5 is skipped without penalty when `gemini` is absent or unauthenticated.

## Gemini CLI leg (slot 5)

**Why it earns a slot:** it is the only **Google-family** channel, and unlike the HTTP legs it is a **tool-using agent** — it reads the pack directory itself instead of receiving inlined text. That directly covers the HTTP legs' known weakness (they must not emit `Read` stubs).

**Model pins — use ids that exist in the CLI today:**

- `gemini-2.5-pro` — default. Best reasoning, free oauth tier.
- `gemini-3-pro-preview` — optional second choice when a preview model is wanted.

**Do not use Argon here.** Gemini 4 Argon is not available in the CLI: the installed CLI predates it, CLI support is still an unmerged upstream PR, and Argon CLI access needs the Google **AI Ultra** plan. Argon is an app-only channel — run those audits by hand with the repo imported (see below).

**Auth:** Google-account oauth (`oauth-personal`), not an API key. Requires `gemini` on PATH and a prior `gemini` login (`~/.gemini/oauth_creds.json` present). Free tier — treat it like free OpenRouter: assume traffic may be logged, so **no secrets in the pack**.

**Invocation (Grok runs this in step 4):**

```bash
gemini --model gemini-2.5-pro \
  --approval-mode yolo \
  --include-directories "{pack}" \
  -p "$(cat {out}/GEMINI_HANDOFF.md)"
```

- `--approval-mode yolo` matches the always-approve default for headless readonly runs (same intent as Grok `--always-approve` and OpenCode `--auto`).
- `--include-directories "{pack}"` grants read access to the pack so the model reads real files.
- Write output to `{out}/auditor-gemini.md` using the [standard auditor format](reference.md).
- Confirm flags with `gemini --help` before the first run — the CLI surface changes between versions.
- **Skip on failure.** Missing binary, missing oauth, or a non-zero exit = drop slot 5 and note it. Never fail or stall the audit on this leg.

**JSON / API alternative:** if a `GEMINI_API_KEY` is present, the same slot can run as an HTTP leg through `run_non_grok_legs.py`. That is a paid key, not the free tier — prefer the CLI oauth path for a free audit.

## App-based large-code audits (no upload limit workaround needed)

For an audit too large to pack, or when Argon is wanted, use the **Gemini app GitHub import** instead of uploading files:

- Gemini web app → **Add file** → **More uploads** → **Import code** → paste the repo or branch URL → **Import**.
- Limits: **one repository per chat, up to 5,000 files, max 100 MB.**
- Private repos work when the GitHub account with access is linked to the Google account (GitHub app connects on first import; manage under Connected Apps).
- Read-only: no repo writes, and the import does **not** re-sync after the first pull.
- Desktop only.

## When to run

| Signal | Run? |
|--------|------|
| Want council opinions without Cursor Task burn | Yes |
| Pre-triage before cursor-audit / super-audit | Yes |
| GO/NO-GO with money/prod on the line | Prefer **super-audit**; free-audit is supplemental |
| Trivial one-line fix | No |

## Workflow (parent Cursor agent — keep tokens low)

```
Free audit progress:
- [ ] 1. Scope — target, question, constraints, mode
- [ ] 2. Pack — write tailored prompt + build_audit_pack.py
- [ ] 3. Prepare — prepare_free_audit.py (select free OR + write Grok handoff)
- [ ] 4. Hand off — handoff-to-grok / grok CLI (always-approve)
- [ ] 5. Deliver — paste ONLY the path to SYNTHESIS.md (or failure notice)
```

**Do not** dispatch Cursor Task auditors. **Do not** synthesize in Cursor — Grok writes the rollup.

Announce before handoff:

> Free audit — mode: `{mode}` · pack: `{pack}` · out: `{out}` · free OR: `{m1}, {m2}` · gemini: `on|skipped` · handoff: `{handoff}`

### Step 1 — Scope + mode

Same modes as cursor-audit (+ `prod-ship` like super-audit). Full matrix in [reference.md](reference.md).

State: **Target**, **Question**, **Constraints** (readonly), **Ruled-out**, **Mode**.

### Step 2 — Pack

1. Copy [prompt-template.md](prompt-template.md) → `reports/audit/free-{slug}/prompt.md` (fill mission + context).
2. Build pack:

```bash
python3 .cursor/skills/free-audit/scripts/build_audit_pack.py \
  --prompt reports/audit/free-{slug}/prompt.md \
  --out reports/audit/pack-free-{slug} \
  --artifact path/to/file:alias.ext \
  --code-path /abs/path/to/code
```

### Step 3 — Prepare handoff

```bash
python3 .cursor/skills/free-audit/scripts/prepare_free_audit.py \
  --pack reports/audit/pack-free-{slug} \
  --out reports/audit/free-{slug} \
  --mode {mode} \
  --workspace "$(pwd)"
```

Writes `out/GROK_HANDOFF.md`, `out/free_models.json`, and prints the shell command for Step 4.

### Step 4 — Hand off to Grok (always-approve)

Prefer TipDrop kit (always-approve default):

```bash
pwsh -File "$HOME/Desktop/projects/tipdrop-workspace-kit/scripts/handoff-to-grok.ps1" \
  -PromptFile reports/audit/free-{slug}/GROK_HANDOFF.md \
  -WorkDir "$(pwd)"
```

Or if `grok` is on PATH and authenticated:

```bash
grok --cwd "$(pwd)" --always-approve "$(cat reports/audit/free-{slug}/GROK_HANDOFF.md)"
```

Opt out of always-approve only if the operator asks (`-NoApprove` / ask mode).

Grok must:

1. Write its own auditor report → `{out}/auditor-grok.md`
2. Run non-Grok legs: `python3 .cursor/skills/free-audit/scripts/run_non_grok_legs.py --pack … --out …`  
   (HTTP legs **inline** pack files and forbid tool calls — DeepSeek/Nemotron must not emit Read stubs)
3. Run the **Gemini CLI leg** (slot 5) if `gemini` is available → `{out}/auditor-gemini.md`; skip on failure
4. Write Glasswing synthesis → `{out}/SYNTHESIS.md`

### Step 5 — Deliver (Cursor)

Paste **only** the synthesis path (file URL / workspace-relative link), e.g.:

> Free audit complete: `reports/audit/free-{slug}/SYNTHESIS.md`

If Grok failed: paste the error + handoff path. Do **not** re-run the full council inside Cursor Task.

## Safety

- **No secrets** in packs, free OpenRouter prompts, **or the Gemini CLI leg** (free oauth traffic may be logged).
- Readonly auditors — no prod writes, no LIVE Discord.
- Always-approve / skip-permissions defaults are intentional for headless readonly runs.
- The Gemini leg runs `--approval-mode yolo`, so it can use tools. Keep its working scope limited to the pack directory with `--include-directories`.

## Invocation phrases

- `/free-audit` · `free audit on …` · `cheap audit` · `low-cost council`
- Optional: `mode: security`, `quick`, `files: a, b`, `count: 3` (≥2 free OR slots), `no-gemini`

## Related

- [reference.md](reference.md) — modes, free-model ranking, synthesis template
- [examples.md](examples.md)
- [cursor-audit](../cursor-audit/SKILL.md) · [super-audit](../super-audit/SKILL.md) · [route](../route/SKILL.md)
- `@ccc-wiki/entities/skills/free-audit.md`
- Keys: export `OPENROUTER_API_KEY` / `DEEPSEEK_API_KEY` in the shell, or set `CEMINI_LLM_ROUTING_ENV` to an absolute routing-env path (scripts do not scan home trees). The Gemini leg uses **oauth, not a key**.
