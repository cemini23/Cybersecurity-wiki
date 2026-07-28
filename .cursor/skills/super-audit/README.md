# super-audit

Five-model super audit skill — three Cursor readonly Task subagents plus two cheaper OpenAI-compatible API auditors (OpenRouter, DeepSeek, custom `ADVISOR_*`). Tailor a domain prompt and audit pack before each run; synthesize consensus across five opinions before prod GO/NO-GO.

**Requires:** Cursor with Task subagents, multi-model access, and API keys for the HTTP leg (optional but recommended). Companion to [cursor-audit](../cursor-audit/) (3-model baseline).

## Install

```bash
# Option A — from agent-toolkit-demo (this repo)
git clone https://github.com/cemini23/agent-toolkit-demo.git
cp -r agent-toolkit-demo/skills/super-audit ~/.cursor/skills/

# Per-project (committed in repo)
cp -r skills/super-audit /path/to/your-project/.cursor/skills/
```

Set `SKILL_DIR` in commands to the install path (see SKILL.md).

### API keys

Export provider keys in the shell (never commit keys). Optionally set
`CEMINI_LLM_ROUTING_ENV` to an absolute path of a local routing file you manage
outside the skill — scripts will not scan project dotenv trees.

```bash
export OPENROUTER_API_KEY=sk-or-...
export DEEPSEEK_API_KEY=sk-...
# Optional WC-style advisor:
export ADVISOR_API_KEY=$OPENROUTER_API_KEY
export ADVISOR_MODEL=google/gemini-2.5-flash
# optional: export CEMINI_LLM_ROUTING_ENV=/absolute/path/to/your-routing-file
```

Discover what's available:

```bash
python3 "$SKILL_DIR/scripts/discover_api_keys.py"
```

API leg needs `httpx`: `pip install httpx`

## Validate

```bash
# Prefer a local checkout of vet (avoid remote install-from-URL in CI/agents):
#   git clone https://github.com/cemini23/vet.git && pip install -e ./vet
pip install vet
vet skills/super-audit/SKILL.md --profile skillmd --strict
```

## Invoke

In Cursor chat:

- `super audit on <target>`
- `/super-audit mode: prod-ship`
- `5-model audit before prod deploy`
- `quick super audit on scripts/foo.sh`

## Workflow (short)

1. Copy [prompt-template.md](prompt-template.md) → tailor mission + context
2. `build_audit_pack.py` → `audit_prompt.md` + `PACK_INDEX.md`
3. Dispatch 3× Cursor Task (readonly)
4. `run_api_auditors.py` → Grok + DeepSeek (or custom `auditors.json`)
5. Synthesize 5-model rollup brief

## Toolkit stack

| Layer | Tool |
|-------|------|
| Static skill/brief gates | [vet](https://github.com/cemini23/vet) |
| Fast multi-model review | [cursor-audit](../cursor-audit/) (3 auditors) |
| Pre-ship council + API opinions | **super-audit** (this skill) |
| Third-party repo adoption | [phase0](https://github.com/cemini23/phase0) |

Run **vet** on brief handoffs — static REJECT overrides multi-model SHIP.

## Docs

- Model matrix + key discovery: [reference.md](reference.md)
- Poker S1 + WC bot examples: [examples.md](examples.md)
- Default API roster: [auditors.default.json](auditors.default.json)

## License

MIT — see [LICENSE](../../LICENSE) in agent-toolkit-demo root.
