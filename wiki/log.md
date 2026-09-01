## [2026-09-01] ingest | K316 SIR / K317 EvoSkill / K318 J-lens / K319 BLOOM-WILT + OOD OntoLearner

Full ingest of 5 NEW inbox arXiv PDFs. Next Cybersec IDs **K316–K319** (dual-ID vs CCC LifePlanner/TAU-Agent/ProgRouter/AsymSpec). **No clone this batch** (BLOOM-WILT null SPDX HOLD).

- **NEW** `@sources/arxiv-2608-30207-sir-cua-self-improving-redteam.md` + `@concepts/failure-driven-cua-ipi-red-teaming.md` — **K316** REFERENCE. SIR: failure-driven adaptive IPI red-team for computer-use agents; deterministic VM oracle + joint success. HF space `TrustSafeAI/SIR` WATCH. No IPI payloads in wiki.
- **NEW** `@sources/arxiv-2608-30429-evoskill-injection.md` + `@concepts/evoskill-injection-self-evolving-agents.md` — **K317** REFERENCE. EvoSkill Injection / SARGE: skill generation pipeline as attack surface; persistent retrieval-time harm. No malicious trajectories in wiki.
- **NEW** `@sources/arxiv-2608-31084-j-lens-multi-token-readout.md` + `@concepts/multi-token-concept-readout-audit.md` — **K318** WATCH. J-lens multi-token SAE verbalization for refusal-surface audit; not enforcement.
- **NEW** `@sources/arxiv-2608-31105-bloom-wilt-logit-tilting-audit.md` + `@concepts/logit-tilting-rare-behaviour-audit.md` — **K319** REFERENCE HOLD. BLOOM-WILT multi-turn rare-behaviour elicitation; `AdrSkapars/bloom-wilt` license null.
- **NEW OOD stub** `@sources/arxiv-2608-31118-ontolearn-llm-size-ood.md` — ontology learning scale study; not cyber-primary.
- **Backlinks:** skill-misevolution, experience-driven-redteam-skill-evolution, evolving-attack-skill-libraries, agent-skill-injection, faithful-agent-asr-measurement, ai-redteam-evidential-ceiling, agent-runtime-guardrails, counterfactual-simulatability-llm-explanations, chain-of-thought-decorative-reasoning-audit.
- **Phase-0:** `scripts/adopt_k316_k319_phase0.sh` **ALL PASS**; no clones.
- **Phase-1:** K316–K319 → agent-audit + lab-redteam (K318 audit only).
- **Dual-ID:** K316–K319 appended to overlay + fragment + k-dual-id rule; `restore_cybersec_dual_id.py --check` OK.
- **friend brief:** add-on **39**.
- **Briefs:** `briefs/2026-09-01_k316-k319-ingest.md`.
- **Sweep:** `wiki/sweeps/2026-09-01-daily.md`.

## [2026-08-31] follow-up | K314 advisory runtime + IAB/StepGuard re-hunt

Implemented recommended K314 follow-ups (no IAB clone — bench not public).

- **Runtime (advisory):** `scripts/k314_enforcement_precheck.py` + `scripts/test_k314_enforcement_precheck.py`; CI step added. Operator checklist — not a Cursor hook.
- **Re-hunt:** `scripts/k307_k315_rehunt.sh` (wrapper keeps `k307_k313_rehunt.sh`); `scripts/instruction_arbitration_bench_inventory.sh` — IAB not found; WATCH `junwenleong/stateful-agent-security-eval` (MIT, adjacent).
- **Federation skill:** `.cursor/skills/external-reference-monitor/` (`federation: true`, operator-invoked) → CCC canon + sync.
- **Phase-0:** `adopt_k314_k315_phase0.sh` asserts K314 runtime + IAB inventory.
- **friend brief:** add-on **38**.

## [2026-08-31] ingest | K314 Recognition–enforcement gap / K315 Security-agent SLR + OOD NL2AGBench

Full ingest of 3 NEW inbox arXiv PDFs (daily sweeps 2026-08-29 through 2026-08-31). Next Cybersec IDs **K314–K315** (dual-ID vs CCC K314 Recuris / K315 ToolMinimize). **No clone this batch.**

- **NEW** `@sources/arxiv-2608-28502-recognition-without-enforcement.md` + `@concepts/recognition-enforcement-gap-instruction-arbitration.md` — **K314** REFERENCE. Recognition–enforcement gap: models decode source-format features and verbalize forged authority yet execute conflicting tool calls under permissive configs (~99% verbal detection vs ~99% execution on GPT-4.1-mini). Fleet-mean attack success ~1.21% but concentrated in deterministic prompt–model cells; external reference monitor (authenticated routing + capability-gated tools) blocks tested channel forgery. InstructionArbitrationBench at release — **no spoof templates in wiki**. Pairs K303 + K276 + K277 + K307.
- **NEW** `@sources/arxiv-2608-28490-llm-security-agents-survey.md` + `@concepts/security-agent-authority-auditability-slr.md` — **K315** REFERENCE. SLR of 100 papers (Jan 2023–Mar 2026): field built agents that **act** but not agents with **bounded authority** or **auditable behavior**. Three-axis taxonomy (Approach / Application / Assessment). Pairs K271 + K311.
- **NEW OOD stub** `@sources/arxiv-2608-28481-ood-nl2agbench.md` — geometry NL→AlphaGeometry DSL; execution-based verification steal → `@concepts/nl-to-ltl-requirements-llm.md`.
- **Backlinks:** agent-runtime-guardrails, nl-security-rules-vs-builtin-deny, refusal-under-knowledge-withhold-contract, measurement-integrity-mcp-security-eval, faithful-agent-asr-measurement, llm-pentest-automation, ai-pentest-harness-landscape, nl-to-ltl-requirements-llm.
- **Phase-0:** `scripts/adopt_k314_k315_phase0.sh` **ALL PASS**; no clones.
- **Phase-1:** K314 → agent-audit + mcp-tool-control + lab-redteam (external enforcement); K315 → agent-audit (assessment taxonomy).
- **Dual-ID:** K314–K315 appended to overlay + fragment + restore script; `restore_cybersec_dual_id.py --check` OK.
- **friend brief:** add-on **37**.
- **Briefs:** `briefs/2026-08-31_k314-k315-ingest.md`.
- **Sweeps:** `wiki/sweeps/2026-08-29-daily.md` + `2026-08-30-daily.md` + `2026-08-31-daily.md` committed.

**Archive** (egress-fi cybersec/):
- `arxiv-2608.28502-recognition-without-enforcement-configuration-de.pdf`
- `arxiv-2608.28490-llm-based-agents-for-software-and-systems-securi.pdf`
- `arxiv-2608.28481-nl2agbench-benchmarking-llm-auto-formalization-f.pdf`

## [2026-08-28] follow-up | K312 loop-state runtime + SPDX re-hunt HOLD

Operator OK: implement leftover K312 accumulator, then lint / commit / push / federation sync.

- **Runtime:** `scripts/k312_loop_state.py` + second fail-closed command on `.cursor/hooks.json` `beforeShellExecution` / `preToolUse` (after K303). Persistent non-decaying state at `.local/k312-loop-state.json` (gitignored). Bound default 3 unauthorized irreversible actions; grant does not zero history. Known mediated paths (`git push` without `--force`, archive-to-egress, prod briefs scp) logged + allowed.
- **Tests / CI:** `scripts/test_k312_loop_state.py`; workflow step next to K303.
- **Re-hunt HOLD:** `scripts/k307_k313_rehunt.sh` — StepGuard still null SPDX; no matching paper repos. Do not clone RTLGuardai / AbacusCTF / getathelas/LoopHarness.
- **Phase-0:** `scripts/adopt_k310_k313_phase0.sh` now asserts k312 script + hook + tests.
- **Federation:** `.cursor/skills/loop-safety-state/` (`federation: true`, operator-invoked); canon copied to CCC then `sync_federation_cursor_skills.sh`; `restore_cybersec_dual_id.py --check`.
- **friend brief:** add-on **36**.
- **Wiki:** `@concepts/non-decaying-loop-safety-state.md` + source page `wire_status: runtime_wired`.

## [2026-08-28] ingest | K310 RTLGuard / K311 CTF-ABACUS / K312 LoopHarness / K313 RedEvoAgent + OOD

Full ingest of 9 NEW inbox arXiv PDFs (daily sweeps 2026-08-27 + 2026-08-28). LANE mid (OpenCode Zen free → claude-ds Flash; route handoff). Next Cybersec IDs **K310–K313** (dual-ID vs CCC K310 AP2 / K311 SCOUT / K312 StepGuard / K313 StarHarness). **No public SPDX clone this batch** (name-collision repos are NOT the papers).

- **NEW** `@sources/arxiv-2608-26049-rtlguard.md` + `@concepts/rtl-codegen-poison-defense.md` — **K310** REFERENCE. Poisoned RTL fine-tunes carry hardware-Trojan backdoors triggered by benign prompts; RTLGuard sanitizes with a small clean teacher + teacher-student objective + feature alignment/KD, lowering ASR while preserving RTL functional/synthesizable. Pairs cweep + Gradient Immunity / DataShield. No public repo at hunt.
- **NEW** `@sources/arxiv-2608-26237-ctf-abacus.md` + `@concepts/trace-verified-ctf-agent-eval.md` — **K311** REFERENCE. CTF evals overstate capability: trace-verified exploits are only 62–87% of recovered flags (1,435 attempts / 240 challenges / six models / two judge lenses). Steal: flag ≠ demonstrated exploit; report a trace-verified rate. Pairs K271 faithful ASR + K278 ATOBench. Authorized-lab eval only.
- **NEW** `@sources/arxiv-2608-27141-safety-does-not-compose.md` + `@concepts/non-decaying-loop-safety-state.md` — **K312** REFERENCE. Trajectory-scoped safeguards re-init per loop; fragmented cross-iteration evidence ⇒ every trajectory-scoped monitor has TPR = FPR; a decaying risk score / fixed cooling-off is insufficient. LoopHarness keeps a persistent non-decaying loop-level safety state + mediated commits, bounding unauthorized irreversible actions. Pairs K307 StepGuard (StepGuard stays K307, not CCC K312). Do NOT clone getathelas/LoopHarness (Apple OS).
- **NEW** `@sources/arxiv-2608-27439-redevoagent.md` + `@concepts/experience-driven-redteam-skill-evolution.md` — **K313** REFERENCE, lab-only. Black-box red-team agent distills trajectories into a human-readable attack skill, evolved via tool-effectiveness profiling + Deciding-Tool Attribution + a **validation ratchet** (keep only updates that improve validation). Transfers across attacker models / harnesses (Claude Code / Codex class). **Lab-only; no `.cursor/skills` evolve from attack runs; no attack-skill bodies in wiki.** Pairs K283 JailbreakSkill + misevolution.
- **NEW OOD stubs** (wont_wire): `@sources/arxiv-2608-25612-ood-wifi-respiratory-csi.md` (commodity-CSI sensor steal) · `@sources/arxiv-2608-26086-ood-traceml.md` (outcome benches hide process) · `@sources/arxiv-2608-26103-ood-zero-wam.md` (no cyber adopt) · `@sources/arxiv-2608-27417-ood-vlm-retrieval-heads.md` (visual evidence can be unfaithful → pairs K308 decorative CoT) · `@sources/arxiv-2608-27420-ood-weak-model-rlvr.md` (no trainer wire).
- **Backlinks:** cweep-rtl-cwe-early-prevention, faithful-agent-asr-measurement, atobench-verification-chain-deception, step-level-agent-guardrails, evolving-attack-skill-libraries, skill-misevolution, agent-runtime-guardrails, airkey-wifi-acoustic-pin-sidechannel, wireless-pentest, ai-redteam-evidential-ceiling, chain-of-thought-decorative-reasoning-audit.
- **Phase-0:** `scripts/adopt_k310_k313_phase0.sh` **ALL PASS**; no clones (RTLGuardai / AbacusCTF / LoopHarness / loopharness.ai / TraceML all name-collision, not the papers).
- **Phase-1:** K310 → agent-audit (sanitize-before-trust); K311 → agent-audit + lab-redteam (trace-verified); K312 → agent-audit + lab-redteam + mcp-tool-control (loop state); K313 → agent-audit + lab-redteam (lab-only skill evolution).
- **Dual-ID:** K310–K313 appended to overlay + fragment + restore script; `restore_cybersec_dual_id.py --check` OK.
- **friend brief:** add-on **35**.
- **Briefs:** `briefs/2026-08-28_k310-k313-ingest.md` · `briefs/2026-08-28_atto-loop-compose.md`.
- **Sweeps:** `wiki/sweeps/2026-08-27-daily.md` + `wiki/sweeps/2026-08-28-daily.md` committed.

**Archive** (egress-fi cybersec/):
- `arxiv-2608.26049-rtlguard-a-lightweight-teacher-student-defense-f.pdf`
- `arxiv-2608.26237-how-do-llm-agents-actually-get-the-flag-trace-le.pdf`
- `arxiv-2608.27141-safety-does-not-compose-non-decaying-loop-state.pdf`
- `arxiv-2608.27439-redevoagent-automatic-red-teaming-agent-with-exp.pdf`
- `arxiv-2608.25612-a-subcarrier-aware-approach-for-robust-respirato.pdf`
- `arxiv-2608.26086-traceml-an-empirical-analysis-of-human-agent-pla.pdf`
- `arxiv-2608.26103-zero-wam-in-context-world-action-modeling-from-h.pdf`
- `arxiv-2608.27417-retrieval-heads-meet-vision-uncovering-how-vlms.pdf`
- `arxiv-2608.27420-boosting-llm-exploration-via-weak-model-guidance.pdf`

## [2026-08-26] follow-up | K307 StepGuard inventory + prod brief

Recommended post-ingest implementations from K307–K309 closeout.

- **StepGuard LICENSE re-hunt:** `gh api repos/zheng977/StepGuard` still **null SPDX**, no LICENSE file — **NO-GO clone** unchanged.
- **NEW** `scripts/stepguard_inventory.sh` (`check` | `adopt`) + federation skill `.cursor/skills/stepguard-inventory/` — K292 harness hash guard; no HF weights.
- **Phase-0:** `adopt_k307_k309_phase0.sh` now calls stepguard inventory check.
- **Entity/source:** `@entities/tools/stepguard.md` + `@sources/arxiv-2608-24777-stepguard.md` re-hunt stamps.
- **Prod brief:** `briefs/2026-08-26_k307-k309-ingest.md` → `cemini-prod:/opt/cemini/briefs/` (1569 bytes).
- **friend brief:** n/a

## [2026-08-26] ingest | K307 StepGuard / K308 decorative CoT / K309 prompt security redistribution

Full ingest of 3 NEW inbox arXiv PDFs from daily sweep 2026-08-26. LANE easy (Cursor parent; wiki pattern).

- **NEW** `@sources/arxiv-2608-24777-stepguard.md` + `@concepts/step-level-agent-guardrails.md` + `@entities/tools/stepguard.md` — **K307** CONDITIONAL-GO. StepGuard: 4B step-level guard (pre-execution tool check + trajectory audit); StepGen + Balance-GRPO; ASR ↓77.3% mean on AgentDojo/AgentDyn, utility ↓2.8 pts. Repo `zheng977/StepGuard` ~6MB **no LICENSE** at hunt — no clone until SPDX; HF weights `ninty-seven/StepGuard` — no download. Dual-ID: ≠ CCC MediSkill-Evo K307.
- **NEW** `@sources/arxiv-2608-24790-decorative-reasoning-medical-cot.md` + `@concepts/chain-of-thought-decorative-reasoning-audit.md` — **K308** REFERENCE. Medical CoT perturbation audit; cdr 72.9% on destructive edits; chain corruption ≈0 ΔAcc; CoT often decorative. Dual-ID: ≠ CCC MetaCaster K308.
- **NEW** `@sources/arxiv-2608-24857-prompt-structure-security-redistribution.md` + `@concepts/llm-codegen-prompt-security-redistribution.md` — **K309** REFERENCE. 424 Python tasks; GPT-4o/LLaMA; structured prompts cut refusals but redistribute Bandit severity/CWE mix; dominant CWE-78/CWE-502 persist. Dual-ID: ≠ CCC Prime Agent K309.
- **Backlinks:** agent-runtime-guardrails, nl-security-rules-vs-builtin-deny, faithful-agent-asr-measurement, atobench-verification-chain-deception, coding-agent-supply-chain-install-gap.
- **Phase-0:** `scripts/adopt_k307_k309_phase0.sh` ALL PASS; no StepGuard clone.
- **Phase-1:** K307 → agent-audit + mcp-tool-control (pre-execution guard); K308/K309 → agent-audit (CoT ≠ evidence; prompt ≠ SAST).
- **Dual-ID:** K307–K309 appended to overlay + restore script check OK.
- **friend brief:** add-on **34**.
- **Briefs:** `briefs/2026-08-26_k307-k309-ingest.md`.
- **Sweep:** `wiki/sweeps/2026-08-26-daily.md` committed.

**Archive** (egress-fi cybersec/):
- `arxiv-2608.24777-stepguard-learning-step-level-guardrails-with-sc.pdf`
- `arxiv-2608.24790-right-diagnoses-decorative-reasoning-a-perturbat.pdf`
- `arxiv-2608.24857-prompt-structure-redistributes-not-reduces-an-em.pdf`

## [2026-08-25] runtime | K303 fail-closed deny + K298 secret_grant + dual-ID restore

Operator OK on remaining follow-ups from K301–K306 ingest.

- **K303 runtime:** `.cursor/hooks.json` (`failClosed: true`) calls `python3 scripts/k303_k298_policy.py --hook` on `beforeReadFile` / `beforeTabFileRead` / `beforeShellExecution` / `preToolUse`. Denies `.env` (not `.env.example`), SSH private keys, `cat .env`, `printenv *KEY*`. Wrapper `.cursor/hooks/k303-deny.sh` kept executable; hooks.json uses python3 directly so a missing `+x` cannot lock the agent again.
- **K298 runtime:** `scripts/secret_grant.py` loads `.env` into the child and redacts values from stdout/stderr — planner never sees the secret. `claude_settings.json.example` deny list for Claude Code (copy to gitignored `.claude/settings.json`).
- **Dual-ID:** owned overlay `.cursor/rules/cemini-cybersec-k-dual-id.mdc` + fragment `.cursor/rules/overlays/cybersec-k-dual-id.fragment.mdc` + `scripts/restore_cybersec_dual_id.py`. CCC `sync_federation_cursor_skills.sh` re-inserts the Cybersec block after copying shared `cemini-phase1-policy-wires.mdc`. Corrected mislabel: K300–K306 are Cybersec IDs, not a CCC wave.
- **SPDX re-hunt 2026-08-25:** CLEAR / SDP / BT-NFT / TrustRAG committee / BreakGuard LLM tests — still no public SPDX clone (name-collision repos unchanged). `golden_critic` stays REFERENCE `wont_wire`.
- **CI:** `restore_cybersec_dual_id.py --check` + `test_k303_k298_runtime.py` before wiki_lint.
- **friend brief:** add-on **33**.

## [2026-08-25] ingest | K301 CLEAR / K302 PsychJail / K303 CLAUDE.md-deny / K304 SDP / K305 BT-NFT / K306 LLM-compliance + OOD Rebite/critic

Full ingest of 8 NEW inbox arXiv PDFs + archive-only for the 2 leftovers (rainfall 2608.16088 / travel 2608.20320 — already wiki pages). LANE mid. OpenCode Zen free → claude-ds Flash; route handoff.

- **NEW** `@sources/arxiv-2608-21278-clear-latent-adapter-routing.md` + `@concepts/conditional-safety-adapter-routing.md` — **K301** REFERENCE (no public code at hunt; no weight download). CLEAR: hidden-state gate continuously routes a safety LoRA on a frozen backbone (h′ = (W + g·ΔW)h); Llama-3-8B-Instruct HarmBench ASR 32.3%→0.5%, GSM8K up to +7.1pp vs global SFT/LoRA. Steal: global LoRA/SFT ≠ proof of safety; prefer conditional/selective intervention; gating scores as drift telemetry.
- **NEW** `@sources/arxiv-2608-23028-psychjail.md` + `@concepts/psychological-multiturn-jailbreaks.md` — **K302** LAB-ONLY. PsychJail: psychology-guided multi-turn persuasion (PKM change-of-meaning factorization, 40-tactic PAP taxonomy, PKM-gated trajectory reward); avg ASR 87.3% over 4 victims; four susceptibility fingerprints (rationalist / credibility-driven / narrative-monoculture / broadly persuadable) labeled **conjecture**. **No persuasion recipes / attack prompts / PoCs in wiki**; `FengZeyugit/PsychJail` repo **NO-GO clone** (null SPDX + ~2GB). Authorized-lab only.
- **NEW** `@sources/arxiv-2608-23550-claude-md-vs-builtin-deny.md` + `@concepts/nl-security-rules-vs-builtin-deny.md` — **K303** (primary wire). 481 public CLAUDE.md files; only ~4–16% of extracted security rules match a built-in deny/permission/sandbox control (strict 4.4%, 95% CI 2.6–6.7%); extraction recall 66.3%. Write-only channel: NL "do not" ≠ platform `deny`; prefer built-in deny/hooks (PreToolUse) over prose-only rules; secrets never in NL rules only.
- **NEW** `@sources/arxiv-2608-23497-safety-direction-penalty.md` + `@concepts/reasoning-induced-misalignment.md` — **K304** REFERENCE (no public code at hunt; no clamp recipes). RIM: harmless reasoning SFT can weaken safety (conditional — only Qwen2.5-3B/7B reproduce it); R/S activation directions coupled; SDP penalizes movement along the safety direction, iterative scope expansion. Steal: reasoning FT is a safety event; safety-representation drift is a measurable diagnostic.
- **NEW** `@sources/arxiv-2608-22754-bluetooth-nft-soft-pairing.md` + `@concepts/bluetooth-nft-soft-pairing.md` — **K305** REFERENCE (prototype in-paper; no code at hunt). NFT soft pairing decouples BT pairing from service authorization (NFBT/NFDT on-chain binding, challenge-response, ERC1155 — gas ~93.4% cheaper batch vs ERC721-style). Steal: pairing ≠ authorization; test the service-auth decision point. **Authorized lab / owned devices only; no LIVE pairing manipulation / unauthorized RF.**
- **NEW** `@sources/arxiv-2608-21317-llm-regulatory-compliance-artifacts.md` + `@concepts/llm-generated-compliance-artifacts.md` — **K306** Watch. LLM DPIA/DPP generation: vague standards (DPIA) need higher-context prompts; strict formats (DBP) consistent but hallucinate more. Steal: compliance artifacts are **candidates, not deliverables**; HITL; schema-valid ≠ correct (pairs rule-blindness + K300 candidate-tests).
- **NEW** `@sources/arxiv-2608-21289-ood-rebite-food-journaling.md` — OOD HCI (UIST '26); steal optional: goal-at-view-time vs capture-time metrics (not cyber runtime).
- **NEW** `@sources/arxiv-2608-23566-ood-critic-bpco.md` — OOD RL trainer; **golden_critic REFERENCE clone** (`github.com/QPHutu/golden_critic`, Apache-2.0, ~14MB → `.local/adopts/golden_critic`) — **wont_wire**; pairs no-GRPO-trainer-as-wired-harness; no HF weight dumps.
- **Backlinks** (`related:` only): system-prompt-leakage, agent-runtime-guardrails, local-abliterated-llm-pentest-stack, mcp-security-posture, decoy-hardening-open-weight-abliteration, tripwire-safety-neuron-clamp, wireless-pentest, compliance-detector-rule-blindness, coding-agent-supply-chain-install-gap, crescendo-multi-turn-jailbreak, ai-redteam-evidential-ceiling, llm-generated-dependency-breaking-tests, ai-for-cybersecurity, ai-pentest-harness-landscape.
- **Phase-0:** `scripts/adopt_k301_k306_phase0.sh` — every new page exists; forbidden clones absent (PsychJail PoC / GRPO trainer runtime / CLEAR weights / HuichiZhou leftovers); golden_critic Apache-2.0 14MB REFERENCE `wont_wire`; dual-ID restored K282–K306 incl. K298–K300; index slugs present.
- **Phase-1:** K302/K305 → lab-redteam (authorized-lab only); K301/K303/K304/K306 → agent-audit (NL rules ≠ deny; no global LoRA as safety proof; reasoning FT = safety event; compliance artifacts need HITL); K303 → mcp-tool-control (prose ≠ enforcement, prefer PreToolUse deny / sandbox). **Restored Cybersec dual-ID block after BPS/EnvHarness/Wayfinder section** (CCC steal kept; K282–K300 wave + K301–K306 appended).
- **friend brief:** add-on **32** (CLAUDE.md-deny gap / PsychJail lab-only / CLEAR+SDP safety-FT / BT-NFT scope / LLM-compliance HITL).
- **Briefs:** `briefs/2026-08-25_k301-k306-ingest.md` + atto `briefs/2026-08-25_atto-claude-md-deny.md`; prod `scp` → cemini-prod:/opt/cemini/briefs/.
- **Sweeps:** `wiki/sweeps/2026-08-22-daily.md` … `2026-08-25-daily.md` committed.
- **Federation skills:** `.cursor/skills/{skill-set-budget,env-harness-wrap,wayfinder}/` committed **as-is** (`federation: true`; no body rewrite; no auto-evolve).

**Archive**: 10 PDFs → egress-fi cybersec/ (8 NEW + rainfall 40MB + travel 2.7MB leftovers). Scp with `-o ConnectTimeout=30 -o ServerAliveInterval=15`; if jump host hangs → log residual, do not block commit.

## [2026-08-21] ingest | K298 Inadvertent Context Leakage / K299 TrustRAG committee RAG / K300 BreakGuard dependency tests + OOD CSI rainfall / travel agents

Full ingest of 4 inbox arXiv PDFs (`wiki/sweeps/2026-08-21-daily.md`) + inbound brief `briefs/2026-08-21_k244-context-leakage-adr.md` (filed as **K298** — inbound wave label K244 ≠ Cybersec Trident K244 ≠ CCC UrbanAgent K244). LANE mid. DeepSeek Flash wrote pages then API-fail; Cursor parent closed archive/commit/CI.

- **NEW** `@sources/arxiv-2608-19857-inadvertent-context-leakage.md` + `@concepts/inadvertent-context-leakage.md` — **K298** REFERENCE (inbound brief source, no inbox PDF). Benign-output covert channel: refusal ≠ no leak; 2-digit near-perfect / 4-digit 82% exact on Opus 4.6; suppression ρ=0.95 with leakage. Defense steal: no secrets in context with third-party-visible generation; tool-layer grants that never return the secret. **No attack prompts / no decoder PoCs** (defensive policy only).
- **NEW** `@sources/newsletter-rss-tldrsec-2026-08-20-tldr-sec-342.md` — **K298** supporting: Uber ADR telemetry (prompts/MCP/traces/tool calls) + two-tier detector + ADR-Bench; SPIFFE `act=agent` short-lived SVIDs (`sub=human`/`act=agent`); Cloudflare task-scoped access + Trust Ratchet.
- **NEW** `@sources/substack-rss-secpro-2026-08-21-ai-ready-soc.md` — **K298** supporting: one asset-ID map; agent least privilege; RAG runbooks; automate gather not decide.
- **NEW** `@concepts/agent-runtime-identity-adr.md` — ADR telemetry + SPIFFE `act=agent` synthesis.
- **NEW** `@concepts/agent-safety-executable-evaluation.md` — benign-output predicate tests, not only jailbreaks.
- **NEW** `@sources/arxiv-2608-20097-trustrag-committee-rag.md` + `@concepts/committee-certified-rag-provenance.md` — **K299** REFERENCE (no public SPDX at hunt; **name collision** — HuichiZhou/TrustRAG 2501.00879 + gomate-community are NOT this artifact; no clone; no MP-SPDZ/blockchain clone). Committee ZK scoring + MPC aggregation + hash commitments → replayable RAG ranking.
- **NEW** `@sources/arxiv-2608-20167-breakguard-dependency-breaking-tests.md` + `@concepts/llm-generated-dependency-breaking-tests.md` — **K300** REFERENCE (paper claims GitHub prototype; hunt found no matching repo with SPDX — ProgrammerNomad/BreakGuard is a Windows app, Tahiram32/breakguard unrelated MIT product). 27/89 (30.3%) BUMP BCs; ~$0.90/detected BC; crash-type > behavioral; **tests are candidates, not a merge gate**.
- **NEW** `@sources/arxiv-2608-16088-ood-rainfall-csi-sensing.md` — OOD meteorology; steal: commodity Wi-Fi/LTE CSI is an environmental sensor → AirKey/DoDTrack; authorized RF lab only.
- **NEW** `@sources/arxiv-2608-20320-ood-travel-behavior-agents.md` — OOD transportation; steal: auditable multi-agent survey→model workflow (researcher-approved revisions, no auto-mutation).
- **Backlinks** (`related:` only): system-prompt-leakage, local-abliterated-llm-pentest-stack, mcp-security-posture, agent-runtime-guardrails, coding-agent-supply-chain-install-gap, airkey, dodtrack OOD, ai-for-cybersecurity, soc-operations, agent-least-privilege-tool-selection, agent-execution-provenance, ai-redteam-evidential-ceiling, faithful-agent-asr-measurement, agent-data-injection-attacks, planner-state-integrity-embodied-agents, npm-supply-chain-defense, llm-code-review-agent-security, wireless-pentest.
- **Phase-0:** `scripts/adopt_k298_k300_phase0.sh` — no forbidden clones (TrustRAG / HuichiZhou / gomate / BreakGuard app / MP-SPDZ / leakage PoCs / fools-gold leftovers); no OSINT BloodBash/bbot checks (those belong to K295 script).
- **Phase-1:** K298 → lab-redteam + agent-audit + mcp-tool-control; K299/K300 → agent-audit; dual-ID block K298–K300 appended to `cemini-phase1-policy-wires.mdc` (CCC + K295–K297 kept intact).
- **friend brief:** add-on **31** (context leakage / tool-layer secrets / TrustRAG name collision / BreakGuard candidate-tests).
- **Briefs:** batch `briefs/2026-08-21_k298-k300-ingest.md` + atto `briefs/2026-08-21_atto-context-leakage.md` + per-K; prod `scp` → cemini-prod:/opt/cemini/briefs/.
- **Sweep:** `wiki/sweeps/2026-08-21-daily.md` retained + committed.
- **Route:** mid Flash wrote pages then DeepSeek API fail → OpenRouter fail → parent close. CCC federation overwrite of shared `cemini-phase1-policy-wires.mdc` (CCC K295–K299) restored Cybersec dual-ID block (keep CCC wave; do not collapse K#).
- **Inbound CCC Thinkingbox brief** (`briefs/2026-08-21_k296-thinkingbox-from-ccc.md`): steal already in CCC K296 section; Cybersec **K296 stays Trusted Workflow Relays** — no new Cybersec K#.

**Archive**: TrustRAG 2608.20097 + BreakGuard 2608.20167 on egress-fi cybersec/. Rainfall 2608.16088 (~40MB local; remote had a 23MB partial) and travel 2608.20320 still local — jump-host scp hung; retry when egress is healthy.

## [2026-08-20] ingest | K295 Fool's Gold / K296 Trusted Workflow Relays / K297 TI→detection + brief-sync (BloodBash / bbot / rule-blindness / CCC excess-authority)

Full ingest of 5 inbox arXiv PDFs (`wiki/sweeps/2026-08-20-daily.md`) + inbound 08-18/08-19/08-20 briefs. LANE hard. Grok CLI implement.

- **NEW** `@sources/arxiv-2608-17202-fools-gold-defensive-deception.md` + `@concepts/decoy-hardening-open-weight-abliteration.md` — **K295** REFERENCE (no public SPDX; no attack recipe / no decoy payload ingest). Dual-ID ≠ CCC K290.
- **NEW** `@sources/arxiv-2608-17361-trusted-workflow-relays.md` + `@concepts/trusted-workflow-relay-email-abuse.md` — **K296** REFERENCE; authorized email/lab only; no phishing kits.
- **NEW** `@sources/arxiv-2608-19011-ti-to-detection-rule-grounding.md` + `@concepts/knowledge-driven-detection-rule-grounding.md` — **K297** REFERENCE (YouTube demo only); enrich+template+judge.
- **NEW** `@sources/arxiv-2608-17067-ood-disco-t2i-defense.md` — OOD → image-gen; no T2I weights.
- **NEW** `@sources/arxiv-2608-19025-ood-self-prompting-literature-extraction.md` — OOD science; steal = consensus ≠ ground truth.
- **NEW** `@entities/tools/bloodbash.md` — **K242** Extract-only; OSINT `.local/adopts/BloodBash` MIT ~104MB pointer; no cyber re-clone; Context-no-PoC cluster listed.
- **NEW** `@entities/tools/bbot.md` — **K241** AGPL Extract-only; OSINT shelf ~15MB; never vendor Atto.
- **NEW** `@sources/arxiv-2608-16852-rule-blindness-compliance-detectors.md` + `@concepts/compliance-detector-rule-blindness.md` — Watch; crossed-rule audit; no FujitsuResearch clone.
- **NEW** `@sources/arxiv-2608-18351-excess-authority-least-privilege.md` + `@concepts/task-conditioned-excess-authority.md` — CCC **K290** (≠ Cybersec CHIVE K290).
- **Phase-0:** `scripts/adopt_k295_k297_phase0.sh` — no forbidden clones; BloodBash/bbot OSINT pointers.
- **Phase-1:** K295/K296/K242 → lab-redteam; CCC K290 + rule-blindness + K297 → agent-audit; **restored** Cybersec dual-ID block after CCC K290–K294 in `cemini-phase1-policy-wires.mdc`.
- **friend brief:** add-on **30** (Fool's Gold vs abliteration, email-relay scope, BloodBash Extract-only, bbot AGPL).
- **Sweep:** `wiki/sweeps/2026-08-19-daily.md` + `2026-08-20-daily.md` retained.

**Archive**: 5 PDFs → egress-fi cybersec/

## [2026-08-18] ingest | K282 ARENA-audio / K283 JailbreakSkill / K288 ESTI / K290 CHIVE + brief-sync (Tripwire / SVP / RA-Bench / DFI)

Full ingest of 5 inbox arXiv PDFs (`wiki/sweeps/2026-08-18-daily.md`) + inbound 08-17 briefs. LANE hard. Grok CLI implement credits-out after core pages; claude-ds Pro hang → Cursor parent takeover from SIP.

- **NEW** `@sources/arxiv-2608-15578-arena-audio-lalm-redteam.md` + `@concepts/audio-grounded-lalm-redteaming.md` + `@entities/tools/arena-audio-redteam.md` — **K282** REFERENCE (no public SPDX URL). Audio-grounded RT (text-safe + audio-harmful); split MD-Judge vs Llama Guard 3; FDR/PSR on four LALMs. Dual-ID ≠ CCC K282 AgentRewind. Pairs ILL K267.
- **NEW** `@sources/arxiv-2608-16465-jailbreakskill.md` + `@concepts/evolving-attack-skill-libraries.md` + `@entities/tools/jailbreakskill.md` — **K283** NO-GO clone (null SPDX). Evolving attack-skill library; +17.5/+13.4 ASR (AdvBench/HarmBench). Dual-ID ≠ CCC K283 Twin. Pairs misevolution.
- **NEW** `@sources/arxiv-2608-16806-esti-state-semantic-injection.md` + `@concepts/planner-state-integrity-embodied-agents.md` + `@entities/tools/esti-bench.md` — **K288** REFERENCE; **same paper as CCC K288** (cyber-primary). Planner-state integrity; P-ASR ≠ E-ASR.
- **NEW** `@sources/arxiv-2608-16747-chive-counterfactual-explanations.md` + `@concepts/counterfactual-simulatability-llm-explanations.md` + `@entities/tools/chive.md` — **K290** GO REFERENCE clone `.local/adopts/chive` MIT ~11MB; runtime wont_wire.
- **NEW** `@sources/arxiv-2608-16795-ood-historical-backtesting-astronomy.md` — OOD astronomy; steal = LLM-judge κ / memorized relevance ≠ foresight.
- **NEW** `@sources/arxiv-2608-14392-tripwire-safety-neuron-clamp.md` + `@concepts/tripwire-safety-neuron-clamp.md` — inbound **K240** Watch; no clamp abliterated models without HITL. Dual-ID ≠ OSINT Talon / CCC robotics.
- **NEW** `@sources/arxiv-2608-14529-deterministic-gapsvp-hardness.md` + `@concepts/lattice-pqc-hardness-watch.md` — SEO K159 overflow; PQC watch; no clone.
- **NEW** `@sources/arxiv-2608-14391-ood-ra-bench-crisis-video.md` — OOD → image-gen; no 93.8GB clone.
- **Indexed** `@concepts/differential-fault-injection-llm-code-stub.md` (CCC K284 pointer).
- **Phase-0:** `scripts/adopt_k282_k288_phase0.sh` — CHIVE clone; no JailbreakSkill clone.
- **Phase-1:** K282/K283/K288 → lab-redteam; K283/K290/K240 → agent-audit; K288 → mcp-tool-control; dual-ID block in `cemini-phase1-policy-wires.mdc`.
- **friend brief:** add-on 29 (ARENA+ILL, JailbreakSkill lab-only, ESTI state integrity, Tripwire no-clamp).
- **Sweep:** `wiki/sweeps/2026-08-16-daily.md` … `2026-08-18-daily.md` retained.

**Archive**: 5 PDFs → egress-fi cybersec/

## [2026-08-15] brief-sync | fill inbound 08-14 wiki stubs (misevolution / HARD / scraper / labels / InterSAGE / OOD 13069)


Inbound briefs pointed at wiki paths that did not exist on this wiki (primary homes: OSINT K237, CCC K277/K278, image-gen OOD). Filed synthesis stubs + bidir; no new Cybersec K IDs (do not reuse OSINT K237 or CCC K277/K278 — Cybersec K277=RSM, K278=ATOBench).

- **NEW** `@sources/arxiv-2608-12851-skill-misevolution.md` + `@concepts/skill-misevolution.md` — OSINT K237; three lifecycle gates; no unattended skill auto-evolve
- **NEW** `@sources/arxiv-2608-12977-self-evolving-security.md` + `@concepts/self-evolving-runtime-defense.md` — HARD gate vs policy evolver; HITL before prod harness mutate
- **NEW** `@entities/tools/cyberscraper-2077.md` + `@entities/tools/rustscan.md` — awareness only; OSINT owns clones; owned-lab / written-scope
- **NEW** `@sources/arxiv-2608-12880-labels-not-endpoints.md` + `@concepts/measurement-integrity-mcp-security-eval.md` — CCC K277; labels ≠ endpoints
- **NEW** `@sources/arxiv-2608-13030-intersage.md` + `@concepts/intersage-trust-native-ioa-protocol.md` — CCC K278 InterSAGE (≠ Cybersec ATOBench)
- **NEW** `@sources/arxiv-2608-13069-ood-behavioral-reprogramming.md` — OOD pointer → image-gen
- **Updated** self-evolving-agent-security, skillsec-lifecycle, safety-harness-evolution, agent-skill-injection, mcp-security-posture, owned-target-whitehat-lab, nmap, ai-for-cybersecurity, local-abliterated, osint-for-cybersecurity, faithful-agent-asr, atobench-verification-chain, agentic-containment, internet-of-agentic-ai, harnessopt-bench, index.md
- **Phase-1**: skill-misevolution + CCC dual-ID notes already in `cemini-phase1-policy-wires.mdc` (federation dirty file this batch)
- **friend brief:** add-ons for misevolution/HARD, owned-lab scraper/RustScan, labels≠endpoints, InterSAGE identity
- **Sweep:** `wiki/sweeps/2026-08-15-daily.md` retained (0 new PDFs)
- **friend brief:** updated

**Archive**: n/a (no inbox PDFs)


Full ingest of 4 inbox arXiv PDFs (2608.12996 / 2608.13463 / 2608.13476 / 2608.13496) + operator-flagged ente (E2EE cloud) Atto steal. Grok CLI out → claude-ds Flash (`deepseek-v4-flash`).

- **NEW** `@sources/arxiv-2608-12996-atobench-deceptive-observations.md` + `@concepts/atobench-verification-chain-deception.md` + `@entities/tools/atobench.md` — **K278** REFERENCE (placeholder repo, 0-byte tree). Verification-chain eval under deceptive target observations; SQLi: median +14 actions/+9 reps, no route restores supported finding → activity ≠ verification.
- **NEW** `@sources/arxiv-2608-13476-marc-v1-clinical-multi-agent.md` + `@entities/tools/marc-v1.md` + `@concepts/deterministic-multi-agent-orchestration-failure-attribution.md` — **K279** GO clone (MIT, 20MB shallow `raw-sources/repos/MARC-v1`). Deterministic staged orchestration + Decomposer + stage-wise failure attribution; clinical runtime wont_wire.
- **NEW** `@sources/arxiv-2608-13496-yavin-secure-edge-pim-tee.md` + `@concepts/pim-tee-untrusted-memory-bus.md` — **K280** REFERENCE (HPCA 2027, no public RTL). TEE does not cover PIM/memory bus; LightSaber + ASCON in-DRAM; bus-as-untrusted mental model.
- **NEW** `@entities/tools/ente.md` + `@concepts/e2ee-consumer-cloud-threat-model.md` — **K281** NO clone (AGPL ~704MB > cap). Atto steal (dedicated ente E2EE brief); threat-model + UX (recovery/share/zero-knowledge) vs Atto M2/M11/M13.
- **NEW** `@sources/arxiv-2608-13463-ood-mllm-routed-ensembles.md` — **OOD** → image-gen wiki (routed stub `@image-gen-wiki/sources/arxiv-2608-13463-mllm-routed-ensembles-routed.md`); wont_wire.
- **Updated** llm-pentest-automation, agent-decoy-defense-autonomous-pentest, faithful-agent-asr-measurement, redagentbench, ai-redteam-evidential-ceiling, agent-execution-provenance, role-specialization-multi-tool-coordination, agent-runtime-guardrails, chiplet-llm-hardware-security, hardware-id-masking-opsec, anti-tamper-protection-classes, anonymity-networks, endpoint-encryption-deniable-storage, account-recovery-deanonymization, ai-for-cybersecurity, index.md (bidirectional backlinks)
- **Phase-1 wires**: K278 → lab-redteam + agent-audit; K279 → mcp-tool-control (clinical wont_wire); K280 → agent-containment; K281 → Atto brief is the wire + cyber steal-from note
- **Briefs**: prod k278–k281 + OOD route; atto `2026-08-14_ente-e2ee-cloud-steal.md` (dedicated) + harness steal; GuruWatcher nofit; poker ATOBench steal
- **friend brief**: updated (E2EE vault + agent-eval add-ons)
- **Phase-0**: `scripts/adopt_k278_k281_phase0.sh` PASS
- **Sweep**: `wiki/sweeps/2026-08-14-daily.md` retained
- **Dual-ID:** concurrent CCC K277–K281 in shared `cemini-phase1-policy-wires.mdc`; CCC K278 = InterSAGE ≠ Cybersec K278 ATOBench; MARC-v1 = CCC K279 ∧ Cybersec K279 — resolve by file+wiki

**Archive**: 4 PDFs → egress-fi cybersec/

## [2026-08-13] ingest | K274–K277 full ingest (WhiteNet / wireless AInf / tutor withhold / RSM) + OOD I2V route

Full ingest of 5 inbox arXiv PDFs (`wiki/sweeps/2026-08-13-daily.md`). LANE hard. All 4 in-scope papers **REFERENCE** (no public SPDX code at retrieval); OOD I2V routed to image-gen. K IDs K274–K277 (K270–K273 not reused).

- **NEW** `@sources/arxiv-2608-06581-whitenet-spectral-whitening.md` + `@concepts/spectral-whitening-wireless-protocol-id.md` — **K274** REFERENCE: WhiteNet channel-robust identification of overlapping IEEE 802.11 across unseen channels (spectral whitening exploits channel-vs-modulation scale separation; synthetic overlap mixer; U-Net+NL 889K → 10K edge). Wireless spectrum-awareness / rogue-transmitter detection tradecraft
- **NEW** `@sources/arxiv-2608-11337-association-privacy-wireless-formal.md` + `@concepts/association-inference-attack-wireless.md` — **K275** REFERENCE: allowlist-based Association Inference (AInf) attacks in BLE reconnection + Wi-Fi P2P persistent groups; Tamarin-verified mitigation (condition-oblivious responses + replay-resistance + distance bounding); Wi-Fi Alliance + Bluetooth SIG acknowledged
- **NEW** `@sources/arxiv-2608-12292-tutor-withhold-refusal-contract.md` + `@concepts/refusal-under-knowledge-withhold-contract.md` — **K276** REFERENCE: deployed tutor enforces answer-withholding as a per-turn machine-checkable contract (non-LLM policy core on trusted state, deterministic code detector, collusion-resistant judge, reason-capturing calibration loop → over-help ladder). Harness steal for any agent that must refuse a capability it has
- **NEW** `@sources/arxiv-2608-12311-rsm-role-specialization.md` + `@concepts/role-specialization-multi-tool-coordination.md` — **K277** REFERENCE: Role Specialization Model coordinating Antigravity/Gemini CLI/Qwen Code (Architect/Analyst/Specialist); role-drift failure mode + prompt-hardening + ISO 25010 qualitative eval. Zenodo DOI not yet registered
- **NEW** `@sources/arxiv-2608-12290-ood-i2v-agentic-optimization.md` — OOD route: I2V Agentic Self-Improvement (Google) → image-gen wiki; `wont_wire`
- **Updated** (bidirectional backlinks): wireless-pentest, wifi-broadcast-rate-edge-moe, rf-fingerprint-probe-point-benchmark, rf-fingerprint-temperature-drift, airkey-wifi-acoustic-pin-sidechannel, hardware-id-masking-opsec, responsible-disclosure, vanhoef-mac-randomization-not-enough, agent-runtime-guardrails, concept2scenario-refusal-suppression, mcp-security-posture, agent-skill-injection, safety-harness-evolution, coding-agent-context-pruning, multi-tool-threshold-mcp-poisoning, ai-for-cybersecurity, index.md
- **Phase-0:** `scripts/adopt_k274_k277_phase0.sh` PASS — all 4 REFERENCE (no clones; WhiteNet no GitHub, 11337 pcloud-only artifact, 12292 deployed no code, 12311 Zenodo pending)
- **Phase-1:** K274 + K275 → `cemini-cybersec-lab-redteam.mdc`; K276 → `cemini-cybersec-agent-audit.mdc`; K277 → `cemini-cybersec-mcp-tool-control.mdc`
- **Briefs:** K274/K275/K276/K277 + OOD I2V route → prod (`scp cemini-prod:/opt/cemini/briefs/`); atto K276/K277 steal; poker Arena (OSINT + Gambling) K276/K277; GuruWatcher nofit; image-gen OOD pointer
- **friend brief:** add-on 29 (K276 withhold-contract harness guardrail + K277 tool-coordination + K275 AInf product-pentest check)
- **Archive:** 5 PDFs → egress-fi cybersec/
- **Sweep:** `wiki/sweeps/2026-08-13-daily.md` retained (historical sweeps tracked)
- **Dual-ID:** concurrent CCC K274–K276 (CDH/VAKRA/RSM) in shared `cemini-phase1-policy-wires.mdc`; RSM 2608.12311 = CCC K276 ∧ Cybersec K277 — resolve by file+wiki

## [2026-08-12] ingest | hardened alternative OSes (GrapheneOS / Qubes / Whonix / Kicksecure / Tails)

Operator asked for more-secure alternate OSes; “Graphine” = **GrapheneOS**. Architecture + first-party docs. **Not** kits: no unofficial non-Pixel Graphene ports, no flash/unlock runbooks, no Magisk/PIF, no claiming any OS is anonymous.

- **NEW** `@concepts/hardened-alternative-operating-systems.md` — pick by threat: Graphene (Pixel exploit/sandbox/verified-boot), Qubes (Xen containment), Kicksecure (hardened Debian, no forced Tor), Whonix (Kicksecure + Gateway/Workstation, all traffic via Tor), Tails (amnesic live), Calyx ≠ Graphene-class
- **NEW** `@entities/tools/grapheneos.md` — official production **Pixels only**; relock bootloader (unlocked = incomplete install); sandboxed Play optional; hardened_malloc / MTE; still fails Google-certified Play Integrity STRONG
- **NEW** `@entities/tools/qubes-os.md` — assume software will be exploited; confine to qubes; not a phone
- **NEW sources (5):** GrapheneOS features; GrapheneOS FAQ; Qubes intro; Whonix About; Whonix vs Kicksecure. Vendor HTML, no PDF archives
- **Updated** secure-boot-vs-device-ownership (Graphene relocks; STRONG is Google-certified-image, not merely locked bootloader), hardware-id-masking-opsec, anonymity-networks, system-hardening, agent-vm-sandboxing, commercial-spyware, mobile-app-attestation, operator-lab-playbook, tails MAC source, kali-linux (pentest suite ≠ daily-driver hardening), index.md
- **Phase-0:** all REFERENCE `wont_wire`; no Graphene/Qubes tree clones
- **Phase-1:** none
- **Briefs:** friend playbook add-on 28 (OS pick by threat; Pixel Graphene; Qubes desktop; Whonix vs Kicksecure; no flash kits)
- **friend brief:** updated
- **Archive:** none (all sources vendor HTML)

## [2026-08-12] ingest | endpoint-encryption / deniable-storage classes + product build integrity (SLSA/sigstore) + Secure Boot vs device ownership

Operator-requested follow-up batch (mid lane, Flash). Same OPSEC/product-defense floor. Architecture + first-party docs. **Not** kits: no hidden-volume / header-wipe procedures, no Secure Boot / DSE / Magisk / PIF bypass, no fake SLSA attestations.

- **NEW** `@concepts/endpoint-encryption-deniable-storage.md` — FDE (BitLocker/FileVault/LUKS) protects the *lost disk*, not the running OS; TPM-only unlock is seamless; deniable-storage (VeraCrypt hidden volume) hides a second filesystem from a coerced password, exists only if usage rules hold, and does **not** beat live malware (`@concepts/commercial-spyware-stalkerware-defense.md`); FDE ≠ anonymity
- **NEW** `@concepts/product-build-integrity-slsa-sigstore.md` — release-artifact layer vs npm dependency-pinning layer; SLSA v1.0 build track L0–L3 (L1 provenance, L2 signed hosted-build provenance, L3 hardened builds); Sigstore keyless signing (Fulcio/Rekor/Cosign, OIDC identity); reproducible-build criteria; verify on the update path
- **NEW** `@concepts/secure-boot-vs-device-ownership.md` — the same stack that stops evil-maid/bootkits (Secure Boot PK/KEK/db/dbx, ELAM, HVCI, Play Integrity STRONG, Vanguard Pre-Check) denies the owner custom kernels / dual-boot / some anonymity setups; product policy options (lock STRONG vs allow custom at lower trust); operator: Secure Boot on for daily driver, written-scope lab exceptions
- **NEW sources (7):** VeraCrypt hidden volumes (architecture only); Microsoft BitLocker overview; Apple FileVault; SLSA v1.0 levels; Sigstore overview; Reproducible Builds; Microsoft Secure Boot (UEFI). All vendor HTML, no PDF archives.
- **Updated** system-hardening, hardware-id-masking-opsec, software-license-binding, mobile-app-attestation, anti-tamper-protection-classes, pre-release-product-pentest, npm-supply-chain-defense (pointer: different layer), hardware-bound-identity, anonymity-networks, commercial-spyware-stalkerware-defense, + microsoft-elam / hvci / riot-vanguard / google-play-integrity sources (bidirectional backlinks), index.md
- **Phase-0:** all REFERENCE `wont_wire`; no VeraCrypt/LUKS setup clones, no SLSA/sigstore monorepo clones
- **Phase-1:** none
- **Briefs:** friend playbook add-on 27 (FDE vs deniable class; SLSA/sigstore for *your* artifacts; attestation vs owner-controlled devices — no kits)
- **friend brief:** updated
- **Archive:** none (all sources vendor HTML)

## [2026-08-12] ingest | metadata / traffic analysis / censorship PT / spyware defense / account-recovery OPSEC

Operator-requested batch (borderline, architecture). Defense + freedom-of-information framing (journalists / dissidents / operators / product users in hostile networks). **Not** kits: no SIM-swap how-tos, no working Tor-bridge runbooks, no spyware/stalkerware installers, no warrant-evasion.

- **NEW** `@concepts/metadata-traffic-analysis-anonymity.md` — path encryption ≠ metadata privacy; an AS/global observer links circuits via timing/volume (Murdoch & Danezis; Tor entry guards; Signal sealed sender); MAC rand / VPN ≠ unlinkability
- **NEW** `@concepts/censorship-circumvention-pluggable-transports.md` — DPI/IP blocking ≠ traffic confirmation; obfs4 / meek / Snowflake / WebTunnel / FTE as PT class; uTLS / JA3 TLS-fingerprint class; domain-fronting as a Dead End (architecture, not a current recipe)
- **NEW** `@concepts/commercial-spyware-stalkerware-defense.md` — mercenary spyware (NSO-class) + consumer stalkerware are **endpoint compromise**, not a Tor failure; defense class: Lockdown Mode, Amnesty MVT triage, assume-burn + hardware replacement for high-confidence infection; product steal: don't ship a telemetry implant
- **NEW** `@concepts/account-recovery-deanonymization.md` — anonymity dies at **recovery** (SIM, email, SSO, passkeys, backup codes); SIM swap as canonical recovery-takeover vector (IC3 + FCC 2023 port-out rules); product steal: recovery flows are an authz-bypass class
- **NEW sources (10):** Tor support entry guards; Murdoch & Danezis *Low-Cost Traffic Analysis of Tor* (PDF → egress-fi); Tor Snowflake; Tor pluggable-transports doc; Apple Lockdown Mode; Amnesty Mobile Verification Toolkit (README; custom license → **REFERENCE** `wont_wire`, no clone); Amnesty Pegasus forensic methodology; FBI IC3 SIM-swap PSA (I-020822-PSA); Google Advanced Protection; Signal sealed sender
- **Updated** anonymity-networks, hardware-id-masking-opsec, system-hardening, operator-lab-playbook, osint-for-cybersecurity, owned-target-whitehat-lab, pre-release-product-pentest, index.md (bidirectional backlinks)
- **Phase-0:** all REFERENCE; no clones (MVT custom license deliberately anti-surveillance → REFERENCE not clone)
- **Phase-1:** none — no ADOPT/GO runtime
- **Briefs:** friend playbook add-on 26 (metadata/recovery/spyware inventory; Snowflake/Tor PT for *censorship* not crime; Lockdown Mode / MVT as defense)
- **friend brief:** updated
- **Local adopts:** none
- **Archive:** 2 PDFs (murdoch-danezis-low-cost-traffic-analysis.pdf, fcc-sim-swap-port-out-rules-2023.pdf) → egress-fi cybersec/ (local copies removed on success)
- **Deferred follow-up:** `concepts/endpoint-encryption-deniable-storage.md` (VeraCrypt hidden volume as a *class*, no procedures) — new-file budget at cap (14/15); flagged for a future ingest

## [2026-08-12] ingest | license-bind / anti-tamper / Windows CI / Joas / mobile attestation

Lanes 1–5 of the "cracking research" handoff, kept to product-pentest / authorized-lab **architecture** (classes not kits). No keygens, unpackers, DRM bypasses, or ban-evasion material.

- **NEW** `@concepts/software-license-binding.md` (lane 1) — bind to ≥2 of {account, device-hash, TPM/attestation, online lease}; repair paths (Autopilot / digital license / KMS lease); no keygens
- **NEW** `@concepts/anti-tamper-protection-classes.md` (lane 2) — integrity / packing / virtualization / online-heartbeat / OS-trust-stack classes; Denuvo / VMProtect / Themida as class exemplars only
- **NEW** `@concepts/mobile-app-attestation.md` (lane 5) — Play Integrity verdicts + App Attest / DeviceCheck; server verifies, client relays; no Magisk/PIF kits
- **NEW sources:** Microsoft HVCI / memory integrity; Microsoft ELAM; Microsoft Kernel DMA Protection (IOMMU); Microsoft WDAC / App Control overview; Microsoft volume activation (KMS/ADBA/MAK); Revenera FlexNet; Irdeto Denuvo kernel AC + anti-piracy; Collberg & Thomborson IEEE TSE 2002 (skimmed — abstract elided, taxonomy details TENTATIVE); Google Play Integrity; Apple App Attest
- **NEW entity:** Denuvo (REFERENCE, `wont_wire`)
- **Lane 4:** Joas *Game Hacking 1* PDF fetched (Drive ID) + **read** (19 pages, link-index deck); AC component taxonomy p.12–13 ingested on anti-tamper-protection-classes; bypass-guide + UC thread titles catalog-only. Stub upgraded `unread-stub` → `read`. Archived to egress-fi.
- **Updated** hardware-bound-identity (trust-stack subsection + lab rule 3), system-hardening (HVCI/ELAM/WDAC/IOMMU high-assurance clients), windows-pentest, mobile-pentest, game-hacking, av-edr-bypass, pre-release-product-pentest, OA3/Oofhours/Autopilot/Riot/GetRuntimeAttestationReport sources (bidirectional backlinks), index.md
- **Phase-0:** all REFERENCE; no packer/DRM/crack clones; tuts4you/UnknownCheats unpack blogs = NO-GO existence-only (Dead Ends)
- **Phase-1:** none — no ADOPT/GO runtime
- **Briefs:** friend playbook add-on 25 (own license bind + mobile attestation; not cracking third-party DRM)
- **friend brief:** updated
- **Local adopts:** none
- **Archive:** 1 PDF (joas-game-hacking-1.pdf) → egress-fi cybersec/ (local copy removed on success)

## [2026-08-12] ops | friend playbook harness host = agent-toolkit

- Friend start-here: harness host row now `~/Projects/agent-toolkit` (TipDrop kit retired 2026-08-08; redirects only). `/route` v2.3: Flash vs Pro inside one `claude-ds`.
- **friend brief:** updated

## [2026-08-12] ingest | anti-cheat / license hardware-bound identity (authorized lab)

Operator-requested ingest after OPSEC HWID pages: identifier map + AC/licensing architecture for owned-product pentest / written-scope RE. Not ban-evasion kits.

- **NEW** `@concepts/hardware-bound-identity-anticheat-licensing.md` — HWID as a **bundle**; demand-start vs boot-start load order; cheap-spoof tells; OA3/Autopilot as licensed cousin; no spoof-driver clones (`wont_wire`)
- **NEW sources:** ARES 2024 / arXiv 2408.00500 (kernel AC vs rootkit taxonomy); s4dbrd kernel-AC survey (HTML); secret.club BattlEye architecture 2019 (architecture only); Microsoft OA3 hardware hash; Autopilot motherboard-replacement 4K HH path; **DeepSeek citation hunt:** Oofhours OA3Tool fields; Check Point firmware-table API; Microsoft `GetRuntimeAttestationReport`; Riot Vanguard On-Demand (TPM EK); Epic v. Araujo (HWID spoof as DMCA); FACEIT Enhanced Verification
- **NEW entities:** BattlEye, Easy Anti-Cheat, Riot Vanguard (all REFERENCE; distinct from DFIR `@entities/tools/vanguard.md`)
- **Updated** hardware-id-masking-opsec (points at AC map; still no kits), game-hacking, windows-pentest, av-edr-bypass, pre-release-product-pentest, owned-target-whitehat-lab, SystemIdentification source, Joas game-hacking-1 stub, index.md
- **Phase-0:** all REFERENCE; no HWID-changer / kdmapper / secret.club bypass clones. DeepSeek listed commercial gitbooks + GitHub spoof repos as **NO-GO** (existence only; not ingested)
- **Phase-1:** none — no ADOPT/GO runtime
- **Briefs:** friend playbook add-on 24 (own license/AC product pentest, not third-party unban)
- **friend brief:** updated
- **Local adopts:** none
- **Archive:** 1 PDF (2408.00500) → egress-fi cybersec/ (local copy removed on success)
- **Executor:** `claude-ds` citation hunt (architecture/policy URLs Cursor search often drops); kits still refused

## [2026-08-12] ingest | hardware-ID masking for OPSEC / anonymity

Operator-requested ingest (wiki gap). No daily-sweep inbox; PDFs fetched to `research to be indexed/` then archived.

- **NEW** `@concepts/hardware-id-masking-opsec.md` — identifier **layers**; OS MAC rand is necessary not sufficient; isolation > in-place spoof; no HWID-spoofer kits (`wont_wire`)
- **NEW sources:** Vanhoef AsiaCCS 2016; Martin PETS 2017 / 1703.02874; Kohno 2005 clock skew; Laperdrix 1905.01051; DrawnApart 2201.09956 (NO-GO clone); StateFi 2507.02478; Puig 2606.25788; Microsoft SystemIdentification; Tails MAC docs; Android AOSP MAC randomization
- **Updated** anonymity-networks, osint-for-cybersecurity, wireless-pentest, agent-vm-sandboxing, system-hardening, operator-lab-playbook, game-hacking (explicit out-of-scope for ban evasion), rf-fingerprint-probe-point, windows-pentest, mobile-pentest, index.md
- **Cross-wiki:** `@osint-wiki/entities/tools/fingerprint-suite.md` backlink (browser fingerprint ≠ host HWID)
- **Phase-0:** all REFERENCE; no clones (DrawnApart GitHub is a tracker artifact)
- **Phase-1:** none — no ADOPT/GO runtime
- **Briefs:** `briefs/2026-08-12_hardware-id-opsec-checklist.md` (gitignored); friend playbook OPSEC reading order + add-on 23
- **friend brief:** updated
- **Local adopts:** none
- **Archive:** 7 PDFs → egress-fi cybersec/ (local copies removed on success)

## [2026-08-12] ingest | K270–K272 (GFlowNet / REDAgentBench / Cross-lingual safety) + 2 OOD routes

**Inbox**: 5 NEW arXiv PDFs from `wiki/sweeps/2026-08-12-daily.md`.

- **OOD** 2608.11044 TEAMMix hierarchical text classification — stub `@sources/arxiv-2608-11044-ood-teammix-htc.md`; brief `briefs/2026-08-12_ood-teammix-htc-route.md`; no adopt (`wont_wire`)
- **OOD** 2608.11121 GenAI in statistical research (dWOLS/DTR) — stub `@sources/arxiv-2608-11121-ood-genai-statistical-research.md`; brief `briefs/2026-08-12_ood-genai-statistical-research-route.md`; no adopt (`wont_wire`)
- **NEW** `@sources/arxiv-2608-10171-gflownets-llm-attacks-turkcell.md` + `@concepts/gflownet-automated-redteam-attack-generation.md` — **K270** GFlowNet attacker–victim–evaluator attack generation (Turkcell); SFT→GFN→MLE staging, SR 0.08→0.79, first Turkish attacker; REFERENCE (no public code); policy_wired
- **NEW** `@sources/arxiv-2608-10669-redagentbench-faithful-agent-asr.md` + `@concepts/faithful-agent-asr-measurement.md` + `@entities/tools/redagentbench.md` — **K271** executable agent RT + faithful ASR (exposure/execution/observation/adjudication), REG gap + action-time reminder; REFERENCE (benchmark unreleased); policy_wired
- **NEW** `@sources/arxiv-2608-11146-illusion-cross-lingual-safety-lrl.md` + `@concepts/cross-lingual-safety-transfer-lrl.md` — **K272** English-only safety ≠ LRL safety (LoDNA: <10% refusal-signal retention Twi/Hausa/Amharic/Swahili); REFERENCE (LoDNA not yet public); policy_wired
- **Updated** gflowrl-distribution-matching-attacker-rl, llm-adversarial-fuzzing, local-abliterated-llm-pentest-stack, agent-runtime-guardrails, ai-redteam-evidential-ceiling, agent-data-injection-attacks, safety-harness-evolution, multilingual-long-horizon-agent-evaluation, ai-for-cybersecurity, index.md (bidirectional backlinks)
- **Phase-0**: `scripts/adopt_k270_k272_phase0.sh` PASS (asserts 9 pages + K270–K272 wire bullets + no clones)
- **Phase-1**: `cemini-cybersec-lab-redteam.mdc` §K270/§K271/§K272; `cemini-cybersec-agent-audit.mdc` §K271. Shared `cemini-phase1-policy-wires.mdc` later synced CCC K270–K273 (MCP/ACM) with dual-ID note — Cybersec K270–K272 stay in domain rules; resolve by file+wiki
- **Briefs**: K270/K271/K272 + 2 OOD routes → prod `cemini-prod:/opt/cemini/briefs/`; atto K271 agent-eval steal; GuruWatcher nofit; poker Arena (OSINT + Gambling) K271 agent-eval steal
- **friend brief:** updated (K271 faithful-ASR discipline + K270 GFlowNet lab pattern + K272 LRL eval scope add-ons)
- **Local adopts**: none — all three in-scope papers REFERENCE (no public code at Phase-0; under 500MB N/A)
- **Archive**: five PDFs → egress-fi cybersec/ (local copies removed); inbox empty
- **Sweep**: `wiki/sweeps/2026-08-12-daily.md` retained (ingest spent)

## [2026-08-11] ingest | K267–K269 (ILL / SHE / Taboo) + 2 OOD routes

**Inbox**: 5 NEW arXiv PDFs from `wiki/sweeps/2026-08-11-daily.md`.

- **OOD** 2608.06866 DoDTrack Wi-Fi Doppler sensing/localization — stub `@sources/arxiv-2608-06866-ood-dodtrack-wifi-doppler-tracking.md`; brief `briefs/2026-08-11_ood-dodtrack-wifi-doppler-route.md`; no adopt (`wont_wire`)
- **OOD** 2608.09930 Beyond-Naturalness TTS eval — stub `@sources/arxiv-2608-09930-ood-beyond-naturalness-tts-eval.md`; brief `briefs/2026-08-11_ood-beyond-naturalness-tts-route.md` → image-gen or skip; no adopt (`wont_wire`)
- **NEW** `@sources/arxiv-2608-09158-ill-inaudible-low-frequency-lalms.md` + `@concepts/inaudible-low-frequency-audio-attacks.md` + `@entities/tools/ill-inaudible-low-frequency-lockout.md` — **K267** ILL inaudible-LF audio red team vs LALMs + DRG requery defense; REFERENCE (no public code); policy_wired
- **NEW** `@sources/arxiv-2608-09885-she-safety-harness-evolution.md` + `@concepts/safety-harness-evolution.md` + `@entities/tools/she-safety-harness-evolution.md` — **K268** SHE four-artifact harness evolution + validity + safety-utility selection; **GO** Apache-2.0 clone `raw-sources/repos/SHE` @ `0c656460` ~4.4MB; policy_wired + lab adopt
- **NEW** `@sources/arxiv-2608-09900-taboo-decoding-level-diagnostic.md` + `@concepts/decoding-level-taboo-diagnostic.md` — **K269** Taboo word-boundary logit-masking diagnostic; REFERENCE (Zenodo CC-BY-4.0 ~234KB, no clone); policy_wired
- **Updated** llm-adversarial-fuzzing, agent-runtime-guardrails, ai-for-cybersecurity, llm-pentest-automation, harnessopt-bench, self-evolving-agent-security, blast-radius-reversible-context-eviction, airkey-wifi-acoustic-pin-sidechannel, wireless-pentest, safety-harness-evolution, index.md
- **Phase-0**: `scripts/adopt_k267_k269_phase0.sh` PASS (asserts pages + SHE clone SHA/size + K267–K269 wire bullets)
- **Phase-1**: `cemini-cybersec-lab-redteam.mdc` §K267/§K268/§K269; `cemini-phase1-policy-wires.mdc` §K268 (renumbered SHE off duplicate K265; canon CCC + cyber + user-global synced via `sync_federation_cursor_skills.sh`); `cemini-cybersec-agent-audit.mdc` §K269; CCC `ccc-k266-k269-phase1-wires.mdc` awareness
- **Briefs**: K267/K268/K269 + 2 OOD routes → prod `cemiini-prod:/opt/cemini/briefs/`; atto K268/K269; GuruWatcher K269/K268; poker (OSINT + Gambling) K269/K268; CCC `docs/briefs/`
- **friend brief:** updated (K268 harness hygiene + K269 refusal-surface audit + K267 audio-lane add-ons)
- **Local adopts**: SHE only (<500MB). No ILL/Taboo clone (no public code / CC-BY-4.0 REFERENCE).
- **Archive**: five PDFs → egress-fi cybersec/ (local copies removed)

## [2026-08-10] ingest | K265–K266 (Blast Radius / ShieldAI) + OOD QNLP

- **OOD** 2608.07439 DisCoCat/QNLP financial rewrite — stub `@sources/arxiv-ood-qnlp-discocat-financial-2608.07439.md`; brief `briefs/2026-08-10_ood-qnlp-discocat-financial-route.md` → OSINT; no adopt
- **NEW** `@sources/arxiv-2608-07440-blast-radius.md` + `@concepts/blast-radius-reversible-context-eviction.md` + `@entities/tools/blast-radius-necrophoresis.md` — **K265** REFERENCE (no public Chalk SPDX); policy_wired
- **NEW** `@sources/arxiv-2608-07446-shieldai-oss-ai-risk-tools.md` + `@concepts/taxonomy-driven-oss-ai-risk-mitigation.md` + `@entities/tools/shieldai-risk-taxonomy-mapping.md` — **K266** GO Apache-2.0 clone `raw-sources/repos/ShieldAI` ~896KB
- **Updated** coding-agent-context-pruning, trajectory-context-control, llm-adversarial-fuzzing, agent-runtime-guardrails, ai-for-cybersecurity, harnessopt-bench, post-training-adaptation-taxonomy, swe-pruner-pro, fuzzyai, index.md
- **Phase-0**: `scripts/adopt_k265_k266_phase0.sh` PASS
- **Phase-1**: `cemini-phase1-policy-wires.mdc` §K265 (cyber + CCC + user-global); `cemini-cybersec-lab-redteam.mdc` §K266; renumbered off CCC K260 ResidencyRL / OSINT K261–K264
- **Briefs**: prod K265/K266 → cemini-prod; atto K265 steal + K266 nofit; GuruWatcher nofit; poker K265 steal + K266 nofit; CCC handoff; local-lab briefs
- **friend brief:** updated (K265/K266 deep-research add-ons)
- **Local adopts**: ShieldAI only (<500MB). No Blast Radius clone.
- **Archive**: three PDFs → egress-fi cybersec/

## [2026-08-07] phase1-wire | Aug 7 ARIA/taxonomy/NL-LTL/HarnessOpt → lab-redteam

- policy_wired concepts aria-instruction-backdoor-redteam / post-training-adaptation-taxonomy / nl-to-ltl-requirements-llm / harnessopt-bench → `.cursor/rules/cemini-cybersec-lab-redteam.mdc` (arXiv-titled section; federation K249–K252 Scale-CDA/canary/RAC/ArtAnno untouched); lab K254/K255/K258 posture bullets; no clones/installs

## [2026-08-07] ingest | K249–K252 (ARIA / post-training taxonomy / NL→LTL / HarnessOpt-Bench)

**Inbox**: 4 NEW arXiv PDFs from `wiki/sweeps/2026-08-07-daily.md`.

- **NEW** `@sources/arxiv-2608-05659-aria-instruction-backdoor-redteam.md` + `@concepts/aria-instruction-backdoor-redteam.md` — **K249** REFERENCE (no public ARIA code)
- **NEW** `@sources/arxiv-2608-06246-post-training-adaptation-taxonomy.md` + `@concepts/post-training-adaptation-taxonomy.md` — **K250** REFERENCE survey
- **NEW** `@sources/arxiv-2608-06287-nl-to-ltl-requirements.md` + `@concepts/nl-to-ltl-requirements-llm.md` — **K251** REFERENCE (HITL formalization)
- **NEW** `@sources/arxiv-2608-06301-harnessopt-bench.md` + `@concepts/harnessopt-bench.md` — **K252** REFERENCE (Scale; no public bench code)
- **Updated** llm-adversarial-fuzzing, PIMiner, local-abliterated, DataShield, Gradient Immunity, llm-pentest-automation, self-evolving-agent-security, ai-for-cybersecurity, index
- **Phase-1:** restored cybersec digest bullets after federation K230–K253 sync overwrite; added ARIA / taxonomy / NL→LTL / HarnessOpt notes (digest K# collide with federation Scale-CDA/canary/RAC/ArtAnno/Argus — follow rule text)
- **Lab-redteam:** ARIA instruction-backdoor RT in authorization list
- **Local adopts:** none (<500MB) — no public code
- **Briefs:** K249–K252 → prod; Atto K250/K252 light; poker K252 light; GuruWatcher no-fit; TipDrop/David n/a
- **friend brief:** ARIA lab RT + taxonomy + HarnessOpt HITL
- **Sweep:** `wiki/sweeps/2026-08-07-daily.md`
- **CI note:** GHA Actions budget empty — local lint gates only; push still done

**Archive** (egress-fi cybersec/): all four PDFs archived (06246 completed 2026-08-07 via rsync after partial scp)

## [2026-08-06] brief | K225 shepherd/loopx local-abliterated-lab

- Staged local brief `briefs/2026-08-06_k225-shepherd-loopx-lab.md` (gitignored briefs/). OSINT Phase-0 clones shepherd+loopx REFERENCE; L0p4Map GPL patterns-only; bountyforge NO-GO.

## [2026-08-06] ingest | K244–K248 (Trident / HoRFFI / Gradient Immunity / chiplet / PIMiner)

**Inbox**: 5 NEW arXiv PDFs from `wiki/sweeps/2026-08-06-daily.md`.

- **NEW** `@sources/arxiv-2608-04317-trident-agentic-drl-redteam.md` + `@concepts/trident-agentic-drl-defense-redteam.md` — **K244** REFERENCE (no public code)
- **NEW** `@sources/arxiv-2608-04881-horffi-high-openness-rffi.md` + `@concepts/horffi-high-openness-rffi.md` — **K245** REFERENCE
- **NEW** `@sources/arxiv-2608-05045-gradient-immunity-malicious-finetune.md` + `@concepts/gradient-immunity-malicious-finetune.md` — **K246** REFERENCE; `OpenCausaLab/Gradient-Immunity` empty/no LICENSE — skip clone
- **NEW** `@sources/arxiv-2608-05063-chiplet-llm-hardware-security.md` + `@concepts/chiplet-llm-hardware-security.md` — **K247** REFERENCE survey
- **NEW** `@sources/arxiv-2608-05108-piminer-prompt-injection-redteam.md` + `@concepts/piminer-agentic-prompt-injection-redteam.md` + `@entities/tools/piminer.md` — **K248** CONDITIONAL-GO MIT ~28MB lab clone
- **Updated** openart/gpt-red/cyber-capable/adversary-emulation, RF fingerprint + wireless, DataShield + local-abliterated, CWEEP, PI calibration + llm-adversarial-fuzzing + crescendo, ai-for-cybersecurity, index, adoption table
- **Phase-1:** restored STAIR/TokTier/Salami/adaptive-TTS bullets after federation K230–K248 sync overwrite; added PIMiner + Gradient Immunity notes (digest K# collide with federation UrbanAgent/HIVE/TurnSight — follow rule text)
- **Lab-redteam:** PIMiner + Trident-class DRL red in authorization list
- **Local adopts:** PIMiner only (~28MB <500MB); no Gradient-Immunity clone
- **Briefs:** K244–K248 → prod; Atto K246/K248 light; poker K248 light / rest no-fit; GuruWatcher no-fit; TipDrop/David n/a (lane → local-abliterated-lab)
- **friend brief:** PIMiner lab gate + Gradient Immunity vs path A + Trident/HoRFFI/chiplet light
- **Sweep:** `wiki/sweeps/2026-08-06-daily.md`

**Archive** (egress-fi cybersec/): five `arxiv-2608.04*` / `050*` / `05108` PDFs

## [2026-08-05] friend brief | day-1 Cursor /goal paste (remote call)

- **NEW tracked** `briefs/2026-08-05_friend-day1-cursor-goal-paste.md` — PART A manual (accounts, Cursor Models/Auto-run, Git/Node, kit clone) + PART B pasteable `/goal` (wikis, claude-ds, route, skills, MCP github/fetch, plugins list, cheatsheet) + PART C post-call coaching
- **friend brief:** Dual-wiki day-1 points at goal-paste; Sources updated
- **.gitignore:** allowlist `!briefs/2026-08-05_friend-day1-cursor-goal-paste.md`
- Novice / remote: Claudio on call only; no TipDrop product, no Ollama/Flash weights day-1

## [2026-08-05] friend brief | dual-wiki start (Cyber + OSINT OPSEC)

- **friend brief:** added § Dual-wiki start — Cyber primary + private OSINT OPSEC sidecar; day-1 Cursor/route/`claude-ds` vs later path-A lab; OSINT OPSEC reading order (fingerprint-suite → octobrowser → arkham → MITRE ATLAS → cua + Phase-0 habit)
- **Updated** `@concepts/operator-lab-playbook.md` — dual-wiki pointer (no full duplicate)
- Access note: friend needs GitHub invite to `cemini23/llm-wiki-by-cemini` before kit `install-federation-wikis.ps1` can clone OSINT

## [2026-08-05] brief | K224 AI-Surface + reverse-skill (from OSINT)

- Local brief `briefs/2026-08-05_k224-ai-surface-reverse-skill.md` (gitignored) — MIT Integrate for lab PR scan + reverse-skill clone under OSINT `.local/adopts/`
- getprism.su Watch only; authorized lab scope unchanged

## [2026-08-05] routing | federation TipDrop slot → local abliterated lab

- OSINT/CCC: TipDrop/David brief lane retired; **local-abliterated-lab** now an active research-queue target
- Inbound federation briefs for abliterated LLM / owned lab / AI pentest harness → `briefs/` + `@concepts/local-abliterated-llm-pentest-stack.md` / `@concepts/operator-lab-playbook.md`
- Links eval CCC **v10.5** scores `local-abliterated-lab overlap` (surface 10)

## [2026-08-05] ingest | K241–K243 (Wi-Fi broadcast / AirKey / adaptive TTS) + 2 OOD

**Inbox**: 5 NEW arXiv PDFs from `wiki/sweeps/2026-08-05-daily.md`.

- **NEW** `@sources/arxiv-2608-02341-wifi-broadcast-rate-edge-moe.md` + `@concepts/wifi-broadcast-rate-edge-moe.md` — **K241** REFERENCE
- **NEW** `@sources/arxiv-2608-03151-airkey-wifi-acoustic-pin-inference.md` + `@concepts/airkey-wifi-acoustic-pin-sidechannel.md` — **K242** REFERENCE; lab-redteam policy
- **NEW** `@sources/arxiv-2608-03961-adaptive-fuzzy-test-time-sampling.md` + `@concepts/adaptive-fuzzy-test-time-sampling.md` — **K243** REFERENCE; Phase-1 adaptive TTS budget
- **OOD stubs:** `@sources/arxiv-ood-remote-sensing-unievo-rs-2608.03911.md`, `@sources/arxiv-ood-transformer-sidpp-2608.03921.md` + route brief
- **Updated** wireless-pentest, local-abliterated, network-security, social-engineering, GradCuit, TokTier, llm-pentest-automation, ai-for-cybersecurity, index, digest ANDNOT
- **Phase-1:** restored STAIR/Salami/TokTier exactness bullets after federation K230–K243 sync overwrite; added adaptive TTS
- **Local adopts:** none (no public code <500MB)
- **Briefs:** K241–K243 → prod; Atto K243 light; poker K243 light; GuruWatcher no-fit; TipDrop/David n/a
- **friend brief:** AirKey physical risk + adaptive TTS on path A; Wi-Fi broadcast light; OOD n/a
- **Sweep:** `wiki/sweeps/2026-08-05-daily.md`

**Archive** (egress-fi cybersec/): five `arxiv-2608.02*` / `039*` PDFs

## [2026-08-04] brief | DiffAttack FR evasion routed from image-gen

- `briefs/2026-08-04_diffattack-fr-evasion-from-image-gen.md` — arXiv:2607.28936 LDM FR evasion (USF); defensive WATCH; no install.

## [2026-08-04] ingest | K236–K240 (ART-PDDL / OpenART / Salami / MedPRESS / GradCuit)

**Inbox**: 5 NEW arXiv PDFs from `wiki/sweeps/2026-08-04-daily.md`.

- **NEW** `@sources/arxiv-2608-00143-symbolic-art-attack-chain-pddl.md` + `@concepts/symbolic-art-attack-chain-granularity.md` — **K236** REFERENCE
- **NEW** `@sources/arxiv-2608-00677-openart-agent-redteam-evolution.md` + `@concepts/openart-environment-evolution-agent-redteam.md` + `@entities/tools/openart.md` — **K237** CONDITIONAL-GO clone ~19MB AGPL
- **NEW** `@sources/arxiv-2608-01637-salami-collusive-memory-poisoning.md` + `@concepts/salami-collusive-memory-poisoning.md` — **K238** REFERENCE; Phase-1 collusive-memory policy
- **NEW** `@sources/arxiv-2608-02520-medpress-patient-pressure-sycophancy.md` + `@concepts/multi-turn-pressure-sycophancy.md` — **K239** REFERENCE (ladder pattern)
- **NEW** `@sources/arxiv-2608-02585-gradcuit-test-time-latent-reasoning.md` + `@concepts/gradcuit-test-time-latent-reasoning.md` — **K240** REFERENCE (NO LICENSE — no clone)
- **Updated** adversary-emulation, red-team-ops, caldera, MITRE ATT&CK, GPT-Red, llm-adversarial-fuzzing, cyber-capable containment, ADI, experiential/STAIR memory, crescendo, social-engineering, InferScale, ai-for-cybersecurity, index
- **Briefs:** K236–K240 → prod; Atto K238 light; poker K236/K237 no-fit + K238 light; GuruWatcher n/a; TipDrop/David n/a
- **Phase-0:** OpenART PASS CONDITIONAL-GO (AGPL lab); GradCuit NO LICENSE skip; others REFERENCE
- **Phase-1:** collusive memory bullets in `cemini-phase1-policy-wires.mdc`; OpenART noted in lab-redteam rule
- **Local adopts:** OpenART only (~19MB). GradCuit skipped.
- **friend brief:** OpenART lab AGPL + Salami memory coalition checklist; ART-PDDL light; MedPRESS/GradCuit n/a for friend product
- **Sweep:** `wiki/sweeps/2026-08-04-daily.md`

**Archive** (egress-fi cybersec/): five `arxiv-2608.*` PDFs

## [2026-08-03] ingest | K220 cyber tool register from OSINT revenue eval

- **Parent:** `@osint-wiki/sources/eval-url-revenue-cyber-agent-harness-2026-08-03.md` (thin brief was insufficient — promoted)
- **NEW source:** `@sources/osint-k220-cyber-agent-harness-eval-2026-08-03.md`
- **NEW entities:** cloakquest3r · damn-vulnerable-drone · hacktools · raccoon · black-cat · bypassav · torbot
- **Updated concepts:** osint-for-cybersecurity · web-pentest-methodology · av-edr-bypass · ai-pentest-harness-landscape (Black-cat peer row) · llm-pentest-automation · owned-target-whitehat-lab · red-team-operations · cf-hero peer
- **Brief:** `briefs/2026-08-03_k220-cyber-context-catalog.md` expanded
- **Posture:** Reference / Steal-from / Lab only — no Cemini product Integrate; null-SPDX = no clone; TorBot GPL-3 Reference-only
- **friend brief:** updated 2026-08-03 evening — §2 DVD optional lab; §4 CloakQuest3r/Raccoon; §5 Black-cat steal-from + K220 hard stops; deep-research #13

## [2026-08-03] ingest | Joas archive closeout + K233–K235 (CWEEP / STAIR / TokTier)

**Inbox**: 3 NEW arXiv PDFs (2607.29604 / 29658 / 29678) + Joas deep-read leftovers (PDFs already synthesized 2026-08-02).

- **Joas closeout:** archived 5 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/`; source Locations updated; `@concepts/buffer-overflow.md` → **validated**; eCPPT cram `briefs/2026-08-03_ecppt-exam-cram.md`
- **NEW** `@sources/arxiv-2607-29604-cweep-rtl-cwe-static-analysis.md` + `@concepts/cweep-rtl-cwe-early-prevention.md` + `@entities/tools/cweep.md` — **K233** CONDITIONAL-GO clone ~15MB
- **NEW** `@sources/arxiv-2607-29658-stair-hierarchical-repair-trajectories.md` + `@concepts/stair-hierarchical-repair-plans.md` — **K234** REFERENCE; Phase-1 policy wire
- **NEW** `@sources/arxiv-2607-29678-toktier-stateful-tokenization.md` + `@concepts/toktier-exact-stateful-tokenization.md` — **K235** REFERENCE; Phase-1 policy wire
- **Updated** experiential-abstraction, coding-agent-context-pruning, InferScale/vLLM/local-abliterated, CoGate, llm-pentest-automation, ai-for-cybersecurity, ecppt, index
- **Briefs:** K233–K235 prod + eCPPT cram; friend brief sync (TokTier TTFT + Joas archive + eCPPT pointer)
- **Routing:** Atto / poker / TipDrop / David — **n/a** (no genealogy/persona/poker fit). Prod SCP K234/K235 (+ K233 light).
- **Phase-0:** cweep PASS CONDITIONAL-GO; STAIR/TokTier REFERENCE (no public code)
- **Phase-1:** policy bullets STAIR hierarchical reconstruct + TokTier exact tokenize (`.cursor/rules/cemini-phase1-policy-wires.mdc`)
- **Local adopts:** cweep only (<500MB). Buffer-Overflow-Labs skipped (NO LICENSE).
- **friend brief:** TokTier + eCPPT cram + Joas egress note; CWEEP n/a unless RTL
- **Sweep:** `wiki/sweeps/2026-08-01-daily.md` … `2026-08-03-daily.md` committed

**Archive** (egress-fi cybersec/):
- Joas 5 PDFs (already up)
- `arxiv-2607.29604-…pdf`, `arxiv-2607.29658-…pdf`, `arxiv-2607.29678-…pdf`

## [2026-08-03] query | Friend dual-model hardware preference (planner + executor)

- **Not locked to one HF slug** — pick best abliterated **V4-Flash-0731** planner for path A
- **Current default:** [cebeuq/DeepSeek-V4-Flash-0731-abliterated](https://huggingface.co/cebeuq/DeepSeek-V4-Flash-0731-abliterated) (native ~167 GB; refusal↓ + tool-call intact); alts apetersson / cyberneurova / fraserprice
- **Path A hardware:** NVIDIA multi-GPU **~160–320 GB** or Apple **≥128/256 GB** quants; executor 7B–14B coder-abliterated; **not** single 48 GB
- **friend brief:** planner ranking table + buy path A; note to re-pick weights as better abliterated Flash successors land

## [2026-08-03] ops | Friend brief living sync after every relevant ingest

- **Standing rule:** CLAUDE.md ingest step **9b** — after ingest / Phase-0 / deep-read touching local AI, owned lab, product pentest, bounty, AI harnesses, or ASVS: update `briefs/2026-08-02_friend-operator-lab-playbook.md` or log `friend brief: n/a`
- **Also:** LESSONS.md 2026-08-03; ROADMAP backlog note; maintainer blurb on the brief; hub Raw Concept corrected (brief is tracked, not gitignored)

## [2026-08-02] research | Friend hard pack — strix-omlx + peers + ASVS/lab briefs + Joas deep-read

- **D1 strix-omlx Phase-0:** CONDITIONAL-GO clone `raw-sources/repos/strix-omlx` @ `b623b9f` (~3.3MB Apache-2.0); NEW `@entities/tools/strix-omlx.md`; upgraded `@sources/github-strix-omlx.md`; brief `briefs/2026-08-02_strix-omlx-phase0.md` (no host setup)
- **D2 harness peers desk:** NEW entities `@entities/tools/hexstrike-ai.md` (MIT REFERENCE), `@entities/tools/cai-framework.md` (dual-license REFERENCE, no clone ~207MB), `@entities/tools/pentestgpt.md` (MIT REFERENCE); sources `github-hexstrike-ai` / `github-cai-framework` / `github-pentestgpt`; landscape Peers table filled
- **D3 ASVS L2 brief:** `briefs/2026-08-02_asvs-l2-product-ship-checklist.md` (gitignored OK); ship-bar pointer on `@concepts/pre-release-product-pentest.md`
- **D4 owned-lab recon brief:** `briefs/2026-08-02_owned-lab-golden-image-recon.md`; golden-image pointer on `@concepts/owned-target-whitehat-lab.md`
- **D5 Joas deep-read batch:** Drive PDFs fetched to `research to be indexed/` — deep-read BOF intro/guide/beginners + eCPPT notes + CTH intro PT.1; enriched `@concepts/buffer-overflow.md`, `@concepts/threat-hunting.md`, `@entities/certifications/ecppt.md`
- **Friend brief:** refreshed start-here — harness pick section, ASVS/lab/Strix/CyberStrike/strix-omlx/peers checklists, Joas deep-read item 10, local briefs inventory
- **Lint target:** bidirectional + dangling clean

## [2026-08-02] phase0 | Strix (usestrix/strix)

- **Verdict:** CONDITIONAL-GO — Apache-2.0 verified; real Docker sandbox; soft scope; telemetry default-on
- **Clone:** `raw-sources/repos/strix` (~11MB shallow `main` @ `dbc427d`) — host CLI **not** installed
- **UPDATED:** `@entities/tools/strix.md` + `@sources/github-strix.md` + landscape + playbook links
- **Brief (gitignored):** `briefs/2026-08-02_strix-phase0.md` — pipx/uv only, `STRIX_TELEMETRY=0`, no curl|sh
- **Friend brief:** deep-research item 7 added
- **Compare:** prefer Strix over CyberStrike when Apache + container isolation matter; MIT agents when already on Claude Code

## [2026-08-02] polish | Friend brief + route WorkDir spaces + leftover sources

- **Sources:** `@sources/github-ablitafuzzer.md`, `@sources/devto-red-team-ai-benchmark.md` (wired into local-abliterated stack)
- **Friend brief:** deep-research reading order rewritten (harness → local AI → owned lab → ASVS → bounty → CyberStrike)
- **Route fix:** CCC `route/SKILL.md` documents spaces hygiene; `~/.local/bin/route-task` exports `ROUTE_WORKDIR`/`CLAUDE_DS_WORKDIR`; kit `test-route-workdir-spaces.ps1` green
- **Sync:** federation skills re-synced from CCC

## [2026-08-02] research | Friend-lab deep research pass

- **Gather:** opencli arXiv + Hacker News + Reddit (netsec/bugbounty/LocalLLaMA); WebSearch (Brave MCP auth timeout; Exa keys absent)
- **Pack:** `.scratch/friend-research-2026-08-02/` (gitignored)
- **Deepened:** local-abliterated stack (model classes, OMLX/SGLang, benchmark caution); bug-bounty (2026 stack + anti-noise); owned-lab topologies; pre-release **ASVS 5.0.0**
- **NEW:** `@concepts/ai-pentest-harness-landscape.md`, `@entities/tools/strix.md`, sources `owasp-asvs-5`, Penligent/Rizvi/strix-omlx/github-strix
- **Friend brief:** enriched with deep-research checklist (tracked)

## [2026-08-02] phase0 | CyberStrike (CyberStrikeus/CyberStrike)

- **Verdict:** CONDITIONAL-GO — AGPL-3.0; OpenCode fork; **no sandbox**; `scope_check` advisory-only
- **Clone:** `raw-sources/repos/CyberStrike` (~219MB shallow `dev` @ `93a51658`) — host CLI **not** installed
- **NEW:** `@entities/tools/cyberstrike.md` + `@sources/github-cyberstrike.md`
- **Brief (gitignored):** `briefs/2026-08-02_cyberstrike-phase0.md` — VM-only human gates
- **Wire:** deferred (ask before npm -g / MCP); linked from operator-lab-playbook + llm-pentest-automation
- **Compare:** prefer MIT `@entities/tools/pentest-ai-agents.md` / `pentest-ai` when AGPL or host risk unacceptable

## [2026-08-02] playbook | Friend operator lab coverage hub

- **Hub:** `@concepts/operator-lab-playbook.md` — start-here path (local AI → owned lab → product pentest → bounty)
- **NEW concepts:** `local-abliterated-llm-pentest-stack`, `owned-target-whitehat-lab`, `pre-release-product-pentest`
- **NEW entities:** `ollama`, `vllm` (thin stubs)
- **Expanded:** `@concepts/bug-bounty.md` — beefy-box ROI, recon pipeline, Tier-1/2 scope hygiene
- **Brief (tracked):** `briefs/2026-08-02_friend-operator-lab-playbook.md` — un-ignored 2026-08-02 so friend can read from repo
- **Cross-wiki:** image-gen `de-censoring-techniques` for abliteration theory; cybersec page stays ops/text-LLM focused
- **Note:** `route-task` mid chain hit WorkDir space-truncation on claude-ds; pages landed via Grok CLI implementers + parent hub integration

## [2026-07-30] ingest | AgentSnare decoy defense (from CCC K227)

- Concept `@concepts/agent-decoy-defense-autonomous-pentest.md` + source stub 2607.26998
- CCC cross-wiki stub; **NO-GO** decoy stack install

---

# Cybersecurity Wiki — Operations Log



## [2026-07-31] ingest | arXiv K230–K232 (TCA-SIR, CoGate, AISPA)

- **Sources:** 2607.28498 TCA-SIR; 2607.28529 CoGate; 2607.28617 AISPA/SystemPromptIndex
- **Concepts:** tca-sir-target-conditioned-inspiration-retrieval; cogate-confidence-gated-secure-code; aispa-system-prompt-assurance-audit
- **Entities:** system-prompt-index (REFERENCE — NO LICENSE)
- **Phase-0:** `scripts/adopt_k230_k232_phase0.sh` — no local clones
- **Briefs:** K230–K232 → prod; poker K231/K232; TipDrop/David K231/K232; Atto K230/K232
- **Archive:** 3 PDFs → egress-fi cybersec

## [2026-07-31] phase1 | Cybersec agent-security backlog clear

- **Policy rules (alwaysApply):** `cemini-cybersec-mcp-tool-control.mdc`, `cemini-cybersec-agent-audit.mdc`, `cemini-cybersec-agent-containment.mdc`, `cemini-cybersec-lab-redteam.mdc` + CLAUDE.md Phase-1 section
- **Stamps:** ~65 `policy_wired` · ~113 `wont_wire` (REFERENCE/OOD/trainers/NO LICENSE) · deferred remainder (LICENSE/Docker/Phase-0 watches)
- **Runtime:** `cve-mcp` in `.cursor/mcp.json` → `raw-sources/repos/cve-mcp-server` (`uv run`); entity `runtime_wired`
- **Skipped MCP:** jadx-mcp-server, pentest-ai (still deferred); Image-gen / 3D / GRPO / Harbor/Modal

## [2026-07-30] ingest | arXiv K225–K229 (RFFI temperature, GPT-Red, InferScale, KAMR, ByDeWay-V2)

- **Sources:** 2607.25070 RFFI temperature; 2607.26115 GPT-Red; 2607.27090 InferScale; 2607.27136 KAMR; 2607.27145 ByDeWay-V2
- **Concepts:** rf-fingerprint-temperature-drift; gpt-red-self-play-red-teaming; inferscale-kv-injection-personalized-serving; kamr-knowledge-aligned-multihop-retrieval; bydeway-v2-explainable-spatial-reasoning
- **Entities:** InferScale (GO BSD-3 ~1.4MB)
- **Phase-0:** `scripts/adopt_k225_k229_phase0.sh`; GPT-Red/KAMR/ByDeWay/RFFI dataset REFERENCE
- **Briefs:** K225–K229 → prod; poker K226/K227; TipDrop/David K226/K227; Atto K227/K228
- **Archive:** 5 PDFs → egress-fi cybersec

## [2026-07-29] ingest | arXiv K220–K224 (evidential ceiling, Concept2Scenario, agent containment, IH-B, KuTIE)

- **Sources:** 2607.21735 evidential ceiling; 2607.23496 Concept2Scenario; 2607.25379 cyber-capable agent containment; 2607.25987 IH-Benchmark; 2607.25995 KuTIE/VulnCare
- **Concepts:** ai-redteam-evidential-ceiling; concept2scenario-refusal-suppression; cyber-capable-agent-evaluation-containment; instruction-hierarchy-conflict-benchmark; topology-aware-k8s-llm-remediation
- **Entities:** ai-redteam-evidential-limits (GO MIT ~528KB); vulncare (GO Apache ~2.6MB); kutie-artifacts (CONDITIONAL Dynatrace lab ~2.9MB)
- **Phase-0:** `scripts/adopt_k220_k224_phase0.sh`; Concept2Scenario + IH-B REFERENCE (no public code)
- **Briefs:** K220–K224 → prod; poker steals K220/K222/K223; TipDrop/David K222/K223; Atto K222/K223
- **Archive:** 5 PDFs → egress-fi cybersec


## [2026-07-24] ingest | arXiv K215–K219 (drone FL, CodeMonitor, PATS, Thinkink, RFFI)

- **Sources:** 2607.20280 drone FL chained deauth/impersonation; 2607.20852 Code Monitor Red Teaming; 2607.21419 PATS; 2607.21468 Thinkink; 2607.21564 RF fingerprint probe points
- **Concepts:** drone-fl-chained-deauth-impersonation; code-monitor-red-teaming-public-tests; pats-policy-aware-agent-rl-scaffold; thinkink-ink-native-llm-canvas; rf-fingerprint-probe-point-benchmark
- **Phase-0:** all REFERENCE — no public repos <500MB to adopt; `scripts/adopt_k215_k219_phase0.sh`
- **Briefs:** K215–K219 → prod; poker steals K215/K216; no David/TipDrop
- **Archive:** 5 PDFs → egress-fi cybersec

## [2026-07-23] ingest | arXiv K210–K214 (KYA, ethics, Schwartz, safety bounds, Notes-to-self)

- **Sources:** 2607.19837 Know Your Agent; 2607.20255 ethics (deepen CCC stub); 2607.20270 Schwartz recognition; 2607.20286 probabilistic safety bounds; 2607.20372 Notes-to-self
- **Concepts:** agent-reconnaissance-ipi-pentesting; ethics-autonomous-offensive-ai-agents (deepen); llm-schwartz-value-recognition; llm-probabilistic-safety-bounds; experiential-abstraction-memory
- **Entities:** know-your-agent (REFERENCE/wait); notes-to-self (CONDITIONAL-GO clone ~16MB)
- **Phase-0:** `scripts/adopt_k210_k214_phase0.sh`; KYA public code not found
- **Briefs:** K210–K214 → prod; poker steals K210/K211; no David/TipDrop
- **Archive:** 5 PDFs → egress-fi cybersec

## [2026-07-22] ingest | arXiv K202–K205 + BioSecBench stub

- **Sources:** 2607.19267 authority framing / Senthex RELAY; 2607.19313 OC-GRPO; 2607.19318 VQE-AdvBench; 2607.19345 GEAR; BioSecBench 2607.19262 cross-wiki stub (CCC K203)
- **Concepts:** authority-framing-agentic-cicd; off-context-privileged-rlvr; quantum-vqe-adversarial-robustness; evidence-aware-long-context-grounding; biosecbench-surveillance-verifiable-agent-eval
- **Entities:** senthex-research (GO clone ~672KB); oc-grpo (GO clone ~24MB)
- **Phase-0:** `scripts/adopt_k202_k205_phase0.sh` PASS; local adopts <500MB
- **Briefs:** K202–K205 → cemini-prod:/opt/cemini/briefs/; poker steals K202/K204; no David/TipDrop
- **Archive:** 4 PDFs → egress-fi cybersec; inbox empty
- **Lint:** CI-strict `--fail-on-dangling --fail-on-bidirectional` exit 0

Append-only chronological log of ingests, queries, and lint passes. Newest entries at the bottom.

---

## [2026-05-12] scaffold | Workspace bootstrapped from SEO wiki-template

- Forked `wiki-template/` to `~/Desktop/projects/Cybersecurity wiki/`
- Adapted `CLAUDE.md` for cybersecurity-vertical scope: offensive security + defensive operations + career/education
- Created entity subfolders: certifications, tools, frameworks, threat-actors, platforms, people, vendors, programming-languages
- Wrote README, ROADMAP, LESSONS, LICENSE, hot.md
- Added `Related Wikis` table linking `osint-wiki`, `image-gen-wiki`, `seo-wiki`, `3d-printing-wiki`
- Added cybersecurity-specific `Hands-on rules — ethics + legality` block (authorization, responsible disclosure, dual-use tools, kid-safety framing)

## [2026-05-12] ingest | Joas A Santos cybersecurity PDF corpus (227 PDFs)

- **Source**: shared Google Drive folder `ebooks Joas` (folder ID `12Mvq6kE2HJDwN2CZhEGWizyWt87YunkU`, owner joasantonio108@gmail.com)
- **Author**: Joas A Santos (Brazilian cybersecurity educator, Red Team Leader). LinkedIn: [joas-antonio-dos-santos](https://www.linkedin.com/in/joas-antonio-dos-santos/). GitHub: [CyberSecurityUP](https://github.com/CyberSecurityUP).
- **Method**: Drive API `parentId` query returned empty for shared folders, so contents were enumerated via Playwright DOM scrape (`[data-id]` attributes + tooltip-derived titles). Full inventory persisted to `.scratch/drive_inventory.tsv`
- **Pages touched** — 50+ entities/concepts + 226 source stubs:
  - **226 source stubs** generated via `scripts/build_source_stubs.py` (frontmatter + Drive file-ID provenance + read_status=unread-stub)
  - **2 validated frameworks**: MITRE ATT&CK (full deep-read from `Mitre Att&ck Study Overview.pdf`), Cyber Kill Chain (Unified Cyber Kill Chain content from `Red Team Operations – Concepts #1.pdf`)
  - **8 tool entities**: Cobalt Strike, Metasploit, Burp Suite, Caldera, Maltego, Wazuh, Nmap, BloodHound
  - **10 certification entities**: OSCP, OSWA, OSWE, CRTO, CEH, CompTIA Security+/PenTest+, eCPPT/eCPTX/eWPT
  - **5 vendor entities**: Offensive Security, eLearnSecurity, CompTIA, EC-Council, Zero-Point Security
  - **1 platform**: HackTheBox
  - **1 person**: Joas A Santos (anchor for the entire source corpus)
  - **1 threat actor**: APT28 (only named APT in the corpus)
  - **4 programming language entities**: Python, C/C++, JavaScript, PowerShell — all security-focused
  - **5 validated concepts**: Red Team Operations, Adversary Emulation, AV/EDR Bypass, Web Pentest Methodology, OSINT for Cybersecurity
  - **20+ draft concepts**: SOC Operations, Incident Response, Threat Hunting, Malware Analysis, Exploit Development, Cyber for Kids, Social Engineering, Windows Pentest, Privilege Escalation, Cloud Pentest, Mobile Pentest, Network Security, Container Security, Bug Bounty, Responsible Disclosure, Cybersecurity Careers, Anonymity Networks, Cyberwarfare, AI for Cybersecurity, Blockchain Security, Metaverse Security, Game Hacking, Zero Trust, Purple Team Operations
- **Deep-reads (anchor pages)**: 4 PDFs fully ingested:
  1. `Mitre Att&ck Study Overview.pdf` → @entities/frameworks/mitre-attack.md
  2. `Red Team Operations – Concepts #1.pdf` → @concepts/red-team-operations.md + @entities/frameworks/cyber-kill-chain.md + @concepts/adversary-emulation.md
  3. `AV and EDR Bypass Techniques for new Hackers - Update 2022.pdf` → @concepts/av-edr-bypass.md
  4. `Web PenTesting Checklist by Joas.pdf` → @concepts/web-pentest-methodology.md
- **Cross-wiki backlinks** added: web-pentest-methodology references `@seo-wiki/concepts/web-vitals.md`; osint-for-cybersecurity references `@osint-wiki/concepts/typed-relation-dependencies.md`
- **Read status**: 4 sources `deep-read`, 222 sources `unread-stub` (titles + provenance only; deep-read deferred to future sessions per the ROADMAP)
- **Maturity at write time**: 8 pages `validated` (5 concept + 2 framework + 1 person), 47 pages `draft` (will mature with future ingests + corpus deep-reads)

## [2026-05-12] cross-link | added cybersecurity-wiki backlinks to 4 sibling wikis

- Updated `osint-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `image-gen-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `seo-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `3d-printing-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row

## [2026-05-12] follow-ups | post-publication fixes + content expansion

- **Lint orphan fix**: improved `scripts/fix_wiki_refs.py` (3 passes, idempotent) — fixed the bidirectional-fix bug where `set_related()` failed to recognize one-space-indented `- foo` YAML list items. Result: orphans went 41 → 0, bidirectional gaps 0, dangling refs 0.
- **Deep-reads (3 more PDFs)** — upgraded the following from `draft` → `validated`:
  - `Linux Privilege Escalation – Overview.pdf` → @concepts/privilege-escalation.md (11 Linux privesc technique categories + enumeration script inventory + Windows privesc + community references)
  - `Incident response - overview.pdf` → @concepts/incident-response.md (NIST SP 800-61r2 + SANS PICERL + SOC-vs-CSIRT + DFIR tooling)
  - `INFOSEC PROEFICIENCY COLORS.pdf` → @concepts/cybersecurity-careers.md (the color taxonomy — Red/Blue/Purple/Yellow/Green/White/Orange teams, lane→role mapping, cert ladder by lane)
- **New threat-actor pages** (3): @entities/threat-actors/apt29.md (Cozy Bear / SVR), @entities/threat-actors/lazarus.md (DPRK), @entities/threat-actors/lockbit.md (RaaS criminal). Threat-actor coverage now 4 pages, spans state + criminal axes.
- **Cross-wiki fix**: replaced dangling `@seo-wiki/concepts/web-vitals.md` (page doesn't exist in SEO wiki) with `@seo-wiki/concepts/local-seo-foundations.md` (verified to exist). Cross-wiki dangling: 0.
- **Maturity counts after follow-up**: 11 pages `validated` (5 + 3 upgraded concepts + 2 framework + 1 person), 50 pages `draft`, 226 source stubs `draft + unread-stub`.
- Updated `image-gen-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `seo-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row
- Updated `3d-printing-wiki` CLAUDE.md `Related Wikis` table → added `cybersecurity-wiki` row

## [2026-05-12] lint | full maintenance pass — wiki green across all 8 checks

- Ran `scripts/wiki_lint.py` against the 290-page corpus. Three latent issues surfaced:
  1. **CLAUDE.md OSINT-wiki path was wrong** — `../../Desktop/OSINT WORKSPACE/wiki/` resolved with an extra `Desktop/` segment. Corrected to `../../OSINT WORKSPACE/wiki/`. This unblocks the lint's cross-wiki resolver for every `@osint-wiki/...` reference.
  2. **Double-`@` typo** in @concepts/osint-for-cybersecurity.md `## Relations` block — `@@osint-wiki/concepts/typed-relation-dependencies.md` corrected to `@osint-wiki/...`. The lint regex was matching at offset 1, dropping the cross-wiki alias context.
  3. **Trailing-period boundary bug** in @concepts/osint-for-cybersecurity.md narrative — a sentence ended with `...typed-relation-dependencies.md.`, and the cross-wiki regex greedily captured the trailing dot. Rewrote the sentence so the reference sits mid-sentence.
- **Lint result (all 8 checks clean):** 0 orphans, 0 bidirectional gaps, 0 dangling related links, 0 missing @path body mentions, 0 frontmatter quality issues, 0 stale `[NEEDS VERIFICATION]` tags, 0 dangling cross-wiki refs (4 cross-wiki refs all resolve).
- **Remaining "issues" that are by design**, not bugs: 226 cited unread-stub source pages (the deep-read pipeline backlog) and 20 thin concept pages (<100 narrative words) awaiting source-driven expansion. Both tracked in `ROADMAP.md`.

## [2026-05-13] adoption | Phase-1 deep-dives — 4 K42-routed tools + LLM-security concept buildout

Adopted the 4 GO / CONDITIONAL-GO tools that the 2026-05-13 K42 multi-wiki cross-routing audit identified as cybersecurity-wiki-relevant. The 4 corresponding briefs in `briefs/` (cua, fuzzyai, pentest-ai-agents, pydns-scanner) have been actioned with full Phase-1 implementation.

**10 new pages created:**

Entity pages (4):
- @entities/tools/cua.md — Apple Virtualization.Framework + Lume agent-VM sandbox (FOSS, agent-action tracing). Cross-wiki backlink to @osint-wiki/entities/tools/cua.md.
- @entities/tools/fuzzyai.md — CyberArk's LLM adversarial fuzz framework (Apache-2.0, 18 attack methods including PAIR + Crescendo). Cross-wiki backlink to @osint-wiki/entities/tools/fuzzyai.md.
- @entities/tools/pentest-ai-agents.md — 0xSteph LLM-driven red-team automation (MIT, 1100+ stars, v3.2). Documents the Tier 1 / Tier 2 scope-enforcement model.
- @entities/tools/pydns-scanner.md — xullexer DNS server discovery tool (MIT, 337 stars). Includes mandatory `## Ethical use` section (Phase-1 conditional-GO requirement from K42 evaluation).

Concept pages (6):
- @concepts/agent-vm-sandboxing.md — 3-property methodology (disposable VM substrate / agent-action tracing / explicit isolation boundary). Anchors cua.
- @concepts/llm-adversarial-fuzzing.md — Umbrella methodology distinguishing prompt injection / jailbreak / adversarial fuzzing.
- @concepts/pair-prompt-pattern.md — PAIR single-turn jailbreak (arXiv 2310.08419, Chao et al. 2023).
- @concepts/crescendo-multi-turn-jailbreak.md — Multi-turn escalation attack (arXiv 2404.01833, Russinovich et al. 2024).
- @concepts/llm-pentest-automation.md — Tier 1/2 model + scope-enforcement + findings JSON schema. Anchors pentest-ai-agents.
- @concepts/dns-server-discovery-vs-subdomain-enumeration.md — Recon-discipline distinction. Prevents pydns-scanner misuse (it does *not* enumerate subdomains; it discovers DNS servers).

**17 existing pages updated with bidirectional backlinks** — frontmatter `related:` + body `## Relations` block edits to maintain the wiki's bidirectional invariant. Pages touched: red-team-operations, exploit-development, incident-response, malware-analysis, av-edr-bypass, ai-for-cybersecurity, llm-vulnerability-discovery, social-engineering, responsible-disclosure, bug-bounty, cybersecurity-careers, network-security, osint-for-cybersecurity, web-pentest-methodology, bloodhound, metasploit, nmap. All bumped `updated:` to 2026-05-13.

**Source memory anchors** (from 2026-05-13 K42 audit and follow-up evaluations):
- Obs #507 — K42 multi-wiki cross-routing audit (15 tools flagged for cybersec ingest, 4 prioritized here)
- Obs #502, #506, #508, #509 — individual GO/CONDITIONAL-GO decisions for cua / fuzzyai / pentest-ai-agents / pydns-scanner
- Obs #519, #521, #525, #527 — entity page creation events
- Obs #531, #532, #537, #541, #542 — methodology concept page creation events

**Out of scope (Phase-2 candidates):**
- Per-CVE deep-reads of PAIR + Crescendo academic papers — currently we cite arXiv IDs but haven't synthesized the full method descriptions into snippets.
- Lab-validation of pentest-ai-agents Tier-2 mode against a test target — currently `[TENTATIVE]` on the actual operational claims.
- Tooling-stack briefs for Caldera + Atomic Red Team comparisons against pentest-ai-agents — both are LLM-pentest adjacent but not yet evaluated.

## [2026-05-13] cross-wiki route | xullexer/PYDNS-Scanner — async DNS recon (Slipstream + SlipNet)

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/entities/pydns-scanner-xullexer.md (stub)

## [2026-05-13] cross-wiki route | 0xSteph/pentest-ai-agents — shell-only Claude Code subagents for pentest workflows

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/entities/pentest-ai-agents-0xsteph.md (stub)

## [2026-05-14] cross-wiki route | apktool-mcp-server — Android Reverse Engineering via MCP

Cross-wiki stub routed from `@osint-wiki/entities/tools/apktool-mcp-server.md`.
- Created wiki/entities/apktool-mcp-server.md (stub)

## [2026-05-14] cross-wiki route | T-Pot — Multi-Honeypot Deception Framework

Cross-wiki stub routed from `@osint-wiki/entities/tools/tpotce.md`.
- Created wiki/entities/tpotce.md (stub)

## [2026-05-14] cross-wiki route | Decepticon — Autonomous Red-Team Multi-Agent Framework

Cross-wiki stub routed from `@osint-wiki/entities/tools/decepticon.md`.
- Created wiki/entities/decepticon.md (stub)

## [2026-05-15] cross-wiki route | Claude-Red — Offensive Security Skills Library for Claude Code

Cross-wiki stub routed from `@osint-wiki/entities/tools/claude-red-offensive-skills.md`.
- Created wiki/entities/claude-red-offensive-skills.md (stub)

## [2026-05-15] ingest | Redteam Kit — 22 PDFs (shared Drive folder)

- **Source**: Google Drive shared folder [Redteam Kit](https://drive.google.com/drive/folders/1_UR7Kns9v3vIUyPPP0dTGBKdD1JOZupx) (owner hidden, shared 2026-05-15)
- **Contents**: 22 English-language cybersecurity PDFs — books, playbooks, field manuals, and technique references. Distinct corpus from the Joas A Santos (PT-BR/EN) seed corpus.
- **Method**: Enumerated via Playwright DOM snapshot (Drive API search doesn't return shared-folder children). File IDs not captured — Drive API search by title also returns empty for shared files.
- **Pages touched** — 22 source stubs:
  1. `2025-cybersecurity-attacks-playbooks` — SOC/IR playbooks
  2. `cloud-hacking-playbook` — Cloud offensive playbook
  3. `cloud-attack-vectors` — Cloud attack surface reference
  4. `for-red-team-operation` — Red team operations guide
  5. `hacking-the-art-of-exploitation-2nd-edition` — Jon Erickson classic (exploit dev)
  6. `hacking-computer-hacking-security-testing` — Pentest fundamentals
  7. `hacking-mastery-with-kali-linux` — Kali Linux mastery
  8. `hacking-multifactor-authentication` — MFA bypass techniques (new topic area)
  9. `hands-on-hacking` — Practical hacking guide
  10. `network-attacks-and-exploitation` — Network attack/exploitation
  11. `no-starch-press-hacking-apis` — Web API hacking (new topic area)
  12. `offline-bruteforce-wps` — WPS brute-force attacks
  13. `password-cracking-techniques` — Hash cracking techniques
  14. `penetration-testing-with-kali-linux` — Kali pentest guide
  15. `phishing-dark-waters` — Advanced phishing techniques
  16. `practical-redteaming` — Practical red team operations
  17. `red-team-guides` — Red team guides collection
  18. `red-hat-linux-security-and-optimization` — RHEL hardening
  19. `rtfm-red-team-field-manual-v2` — RTFM v2 quick reference
  20. `ssh-hardening-and-offensive-mastery` — SSH hardening + tunneling (new topic area)
  21. `the-hacker-playbook-3-practical` — Peter Kim's Hacker Playbook 3
  22. `window-privilege-escalation-automated-script` — Windows privesc automation
- **Genuine topic gaps filled**: MFA hacking (#8), web API hacking (#11), SSH hardening (#20) — these seed entirely new topic areas with no prior source coverage
- **Kali Linux gap filled**: two Kali-specific sources (#7, #14) — first dedicated Kali source pages despite it being a core pentest platform
- **Read status**: all 22 sources `unread-stub`; deep-read deferred
- **Total wiki size**: 249 source stubs (227 Joas + 22 Redteam Kit), ~54 entity pages, ~31 concept pages, 4 threat-actor pages
- **New concept pages** created to anchor the ingest:
  - `concepts/buffer-overflow.md` — Stack/heap overflow + shellcode fundamentals
  - `concepts/credential-access.md` — MITRE TA0006 credential dumping + password cracking
  - `concepts/linux-pentest.md` — Linux enumeration + privilege escalation
  - `concepts/linux-security.md` — RHEL hardening, SELinux, SSH defense
  - `concepts/phishing.md` — Spear phishing + MFA bypass + infrastructure
  - `concepts/pivoting.md` — Lateral movement + tunneling + port forwarding
  - `concepts/system-hardening.md` — CIS/STIG system hardening frameworks
  - `concepts/wireless-pentest.md` — WiFi/WPS/Bluetooth/RFID attacks
  - `concepts/defense-in-depth.md` — Layered security architecture
- **New entity pages**: `entities/tools/kali-linux.md` (pentest distro), `entities/tools/multi-cloud-red-team.md` (multi-cloud red team ops)
- **Backlinks**: 26 existing pages updated (11 concept + 15 entity/source) to maintain bidirectional invariant
- **Lint state**: 0 new orphans, 0 new bidirectional gaps, 0 new dangling links from this ingest

## [2026-05-15] cross-wiki route | chekusu/mails — AI email parsing, dual-use phishing-domain enumeration

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/concepts/2026-05-13_chekusu-mails-dual-use.md (stub)

## [2026-05-16] cross-wiki route | jadx-mcp-server + osmedeus (OSINT v3 tool-eval)

Two new tool pages cross-routed from the OSINT workspace tool-evaluation ingest (`@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md`), both rated Adopt tier with cybersec as primary-fit wiki.
- New pages: `entities/tools/jadx-mcp-server.md` (Android RE + live debugging via MCP, JADX decompiler), `entities/tools/osmedeus.md` (orchestration engine for security scanning).
- **Backlink wiring** — reciprocal `related:` + Relations entries added to maintain bidirectional invariant:
  - jadx-mcp-server: `concepts/mobile-pentest.md`, `concepts/malware-analysis.md`, `entities/apktool-mcp-server.md` (sibling Android-RE MCP server)
  - osmedeus: `concepts/red-team-operations.md`, `concepts/bug-bounty.md`, `concepts/web-pentest-methodology.md`, `entities/tools/nmap.md` (Osmedeus integrates nmap)
- **Cross-wiki concept backlinks** — two pages now referenced by sibling-wiki tool pages:
  - `concepts/osint-for-cybersecurity.md` → `@osint-wiki/entities/tools/socid-extractor.md` (cross-platform social-account identifier-extraction; threat-actor correlation)
  - `concepts/blockchain-security.md` → `@osint-wiki/entities/tools/polymarket-insider-tracker.md` (Polymarket funding-chain analysis; threat-actor financial profiling)
- **av-edr-bypass reading list** — one catalog-reference line added (APC-routine remote write primitive write-up; Reference-only tier, ETW/telemetry tamper-detection awareness).
- Index updated: 2 new Tools rows. All modified pages bumped to `updated: 2026-05-16`.

## [2026-05-16] phase-0 | K49 Adopt-tier tool audits (jadx-mcp-server, Osmedeus)

Phase-0 clone audits of the 2 cybersec K49 Adopt-tier tools. Verdicts in each entity page's `## Phase-0 Audit` section.

- **jadx-mcp-server → GO.** Apache-2.0 confirmed (verbatim LICENSE). 510 stars, 5 open issues, multi-contributor. No GPL contamination — Python deps permissive; JADX not vendored (talks over MCP to a separate plugin). Mseep.ai audit badge confirmed real.
- **Osmedeus → GO.** MIT confirmed. 6,314 stars, ~8-year project, active multi-contributor (last push 2026-05-11). Go `go.mod` deps all permissive, no copyleft. The cloud runaway-compute concern is resolved — `docs/cloud/` documents `--auto-destroy`, orphan detection, and `max_hourly_spend`/`max_total_spend` ceilings (av-edr-bypass-class concern → `[CONFIRMED]`).

## [2026-05-16] ingest | BlueTeam Kit (26 PDFs) + KALI For 2023 video course

Two shared Google Drive folders ingested. The Drive API still cannot enumerate shared-folder children — the BlueTeam Kit folder was scraped via Playwright for `data-id`s, then each file's title/metadata fetched via `get_file_metadata`.

- **BlueTeam Kit** (`drive/folders/1v4dQsqYe6ekjgaoImDuU0CcEJKymx1Vs`, owner `cipherphantomofficials@gmail.com`) — 26 PDFs, all defensive / blue-team scope: SOC analyst material (Splunk, QRadar, EDR, threat hunting, IR runbooks), 4 full books (*Next-Gen SOC with IBM QRadar*, *Cybersecurity Blue Team Strategies*, *Effective Threat Investigation for SOC Analysts*, *Open-Source SOC*), and networking/crypto primers (CCNA, Cisco SD-WAN ×2, networking essentials, encryption & hashing). 26 source stubs created (`unread-stub`).
- **2. KALI For 2023** (`drive/folders/1GTheDOkj1I70zzW4CXOZk8ctwIb3dyHN`) — a 50-part Kali Linux video course (`Chapter 1.mp4` … `Chapter 50.mp4`, ~1.8 GB). No per-chapter titles or transcripts; video is not synthesizable into prose. Catalogued as **one** source page (`sources/kali-for-2023-video-course.md`) per user decision — not 50 content-free stubs.
- **4 new entity/concept pages**: `entities/tools/splunk.md`, `entities/tools/qradar.md` (commercial SIEMs — 3 + 2 corpus PDFs respectively); `concepts/siem.md` (no dedicated SIEM page existed despite a SIEM-heavy corpus); `concepts/endpoint-detection-response.md` (defensive counterpart to the existing offensive `av-edr-bypass.md`).
- **Backlinks** — 15 existing pages patched to hold the bidirectional invariant: `soc-operations` (+25), `threat-hunting` (+10), `incident-response` (+9), `network-security` (+7), `defense-in-depth`, `malware-analysis`, `linux-security`, `purple-team-operations`, `adversary-emulation`, `cybersecurity-careers`, `osint-for-cybersecurity`, `av-edr-bypass`, `entities/tools/wazuh`, `entities/tools/kali-linux`, `entities/frameworks/mitre-attack`. All bumped to `updated: 2026-05-16`.
- Index updated: 2 new Defensive-concept rows, 2 new Tools rows, Sources count 249→275 (and the prior Joas miscount 227→226 corrected per `hot.md`).
- Source total: 248 → 275.

## [2026-05-17] deep-read | Threat Hunting 101 (LogRhythm, R. F. Smith) — promoted concepts/threat-hunting.md draft → validated

First BlueTeam Kit deep-read. The LogRhythm white paper provides an 8-hunt structural skeleton (process / behavior / scripting / AV-follow-up / persistence / lateral-movement / DNS / honeypot), each anchored to specific Windows Event IDs or Sysmon event classes — exactly the scaffolding the existing one-paragraph threat-hunting concept page was missing.

- **`sources/threat-hunting-101.md`**: `unread-stub` → `read`; full Narrative with the 8-hunt summary + per-hunt log-source mapping; `## Snippets` extracting the Lucene/SQL baseline queries + Windows Event ID tables + DNS-rebinding mechanism; `## Dead Ends` for hash-only whitelisting + WSH auditing.
- **`concepts/threat-hunting.md`**: `draft` → `validated`. Added Pyramid-of-Pain mental model, log-substrate prerequisites, full 8-hunt catalog with MITRE ATT&CK tactic mapping, hunt-program maturity ladder, Snippets, Dead Ends.
- **NEW `entities/tools/sysmon.md`** (draft): no Sysmon page existed despite every BlueTeam Kit threat-hunt source assuming Sysmon is deployed. Documents the 10 highest-value event IDs (1, 3, 7, 8, 10, 11, 12-14, 19-21, 22, 25), SwiftOnSecurity + sysmon-modular configs (last-validated marked `[NEEDS VERIFICATION 2026-05-17]`), defense-stack positioning (above default Security Log, below commercial EDR, default FOSS-SOC sensor), and operational pitfalls (config noise, no self-tamper-protection).
- **Backlinks** (bidirectional invariant held): added `sysmon.md` ↔ `concepts/siem.md`, `concepts/soc-operations.md`, `concepts/endpoint-detection-response.md`, `entities/frameworks/mitre-attack.md`, `sources/effective-threat-investigation-soc-analysts.md`, `sources/blue-team-handbook.md`, `sources/open-source-soc-guide.md`. Added `concepts/threat-hunting.md` ↔ `concepts/endpoint-detection-response.md` (was missing).
- **Index updated**: new Tools row for Sysmon; `concepts/threat-hunting.md` maturity bumped draft → validated.
- Source `read-status`: `unread-stub` count: 275 → 274 (`threat-hunting-101.md` now `read`).

## [2026-05-17] deep-read | Ransomware Investigation Runbook (Kumar Bineet Ranjan) — new concepts/ransomware.md (validated)

Second BlueTeam Kit deep-read. 15-section SOC playbook (triage → collect → query → process review → TP/FP score → contain + recover); concrete enough to warrant a dedicated concept page rather than just inlining the takeaways into `incident-response.md`.

- **`sources/ransomware-investigation-runbook.md`**: `unread-stub` → `read`; full Narrative (15-section summary), `## Snippets` (TP/FP scoring rubric, VSS-deletion commands, Splunk mass-write + encoded-PowerShell queries, ransom-note filename catalog, certutil LOLBin pattern, encrypted-extension catalog), Dead Ends (entropy as sole signal, power-off destroys evidence, PowerShell-alone false-positive rate).
- **NEW `concepts/ransomware.md`** (validated): defensive-operations synthesis. Kill-chain → defender-signal mapping table, RaaS + double/triple/quad extortion landscape, the canonical VSS-deletion detection, full TP/FP scoring rubric, 10-step play sequence, recovery rules (no-pay default, backup hygiene, krbtgt double-rotation, breach-notification clock), LOLBin reference table (12 binaries × normal/misuse/detection-cue).
- **Backlinks** (bidirectional invariant held): added `concepts/ransomware.md` ↔ `incident-response`, `malware-analysis`, `soc-operations`, `threat-hunting`, `endpoint-detection-response`, `entities/tools/sysmon`, `entities/threat-actors/lockbit`, `entities/frameworks/mitre-attack`, `sources/ransomware-investigation-runbook`, `sources/ransomware-investigation-osint-and-hunting-overview-pt1`, `sources/2025-cybersecurity-attacks-playbooks`.
- **Index updated**: new Doctrine + methodology row for `concepts/ransomware.md` (validated).
- Source `read-status`: `unread-stub` count: 274 → 273 (`ransomware-investigation-runbook.md` now `read`).

## [2026-05-17] partial-ingest | Open-Source SOC (Basta et al., Wiley 2025) — Ch 1-2 extracted, Ch 4-15 deferred

Third BlueTeam Kit deep-read attempt — and a partial. The 6.2 MB PDF exceeds direct-read token limits; subagent extraction surfaced Ch 1-2 + partial Ch 3 only. Ch 4-15 body text was not extractable in the response stream. Honest path: ingest what was readable, document the gap, defer the rest.

- **`sources/open-source-soc-guide.md`**: `unread-stub` → `skimmed` (NOT `read`); Narrative expanded with Ch 1-2 content (5 pillars, 3 SOC operating models, alert-volume math, Cyber Kill Chain 7-stage, three-tier threat-intel typology, 76% zero-trust adoption stat), 7 verbatim Snippets quotes from Basta et al., Dead Ends section documenting the extraction gap + `[NEEDS VERIFICATION 2026-05-17]` flag for Ch 4-15. Pages estimated ~400+; author Basta/Basta/Anwar/Essar, Wiley 2025.
- **NEW `concepts/threat-intelligence.md`** (validated): the wiki had no dedicated CTI page despite >15 pages referencing CTI concepts. Sourced from Ch 2 of the Basta book. Three-tier (strategic/tactical/operational) typology + source taxonomy (OSINT / commercial / ISAC / gov / internal) + 5-step intel lifecycle + tooling stack (MISP / OpenCTI / TheHive / Cortex / Yeti / TAXII) + CTI-in-the-SOC integration points + 4 common pitfalls. Links to all four corpus threat-actor pages (APT28, APT29, Lazarus, LockBit) + MITRE ATT&CK + Cyber Kill Chain.
- **`concepts/soc-operations.md`** promoted `draft` → `validated`: extended Narrative with the 5-pillar framework table (people/processes/technology/governance/data), 3 SOC operating models (in-house/co-managed/MSSP) + 7 decision criteria, alert-volume reality (20k endpoints → 500k alerts/day; 1k/analyst/day → 10 real), Cyber Kill Chain 7-stage defender-signal mapping table, zero-trust adoption signal.
- **Backlinks** (bidirectional invariant held — lint passed 0 gaps): added `concepts/threat-intelligence.md` ↔ `soc-operations`, `threat-hunting`, `incident-response`, `osint-for-cybersecurity`, `adversary-emulation`, `ransomware`, `entities/frameworks/mitre-attack`, `entities/frameworks/cyber-kill-chain`, `entities/threat-actors/apt28`, `entities/threat-actors/apt29`, `entities/threat-actors/lazarus`, `entities/threat-actors/lockbit`. Added `cyber-kill-chain` ↔ `soc-operations`, `open-source-soc-guide`. Added `zero-trust` ↔ `open-source-soc-guide`. Added `mitre-attack` ↔ `open-source-soc-guide`.
- **Index updated**: new Doctrine + methodology row for `concepts/threat-intelligence.md` (validated); `concepts/soc-operations.md` maturity bumped draft → validated.
- Source `read-status`: `unread-stub` count: 273 → 272 (`open-source-soc-guide.md` now `skimmed`).

## [2026-05-17] partial-ingest | Effective Threat Investigation for SOC Analysts (Yahia, Packt 2023) — Ch 1-3 extracted, Ch 4-15 deferred

Fourth BlueTeam Kit deep-read — second partial. The 13.3 MB PDF (~280 pages, file ID `19kYHrfybBmTgrwUrPlUjcNdByhD0AGq9`) was delegated to a general-purpose subagent for chunked extraction; subagent confirmed Ch 1-3 extractable, Ch 4-15 body text (Windows Event ID tables, NTLM/Kerberos Event IDs pp. 71-72, firewall/proxy/DNS field tables) collapsed into a bare hyperlink/index dump beyond Ch 4 paragraph 1. Honest path: same partial-ingest pattern as the Basta SOC guide — promote source to `skimmed`, create only the concept pages whose chapter content was readable, defer the Windows-event-log / firewall / proxy / DNS tunneling / C2 / WAF / sandbox concept pages until re-extraction via `pdftotext -layout`.

- **`sources/effective-threat-investigation-soc-analysts.md`**: `unread-stub` → `skimmed` (NOT `read`); Narrative expanded with Ch 1-3 content (email phishing taxonomy + sandbox evasion + 5-sub-investigation workflow + SPF/DKIM/DMARC trio + Windows event-log defaults + Windows 11 336-log-file count + 6 Security event categories). 12 verbatim Snippets quotes from Yahia (Ch 1 phishing-prevalence stat, ISO-file evasion, sandbox sleep tactic, Yahia keyword catalog; Ch 2 MUA/MSA/MTA flow, Return-Path validation; Ch 3 default log path, 336-log count). Dead Ends section documenting the extraction gap + `[NEEDS VERIFICATION 2026-05-17]` flag for Ch 4-15. Adoption-decisions section lists 4 changes adopted now + 9 concept pages deferred.
- **NEW `concepts/phishing-investigation.md`** (validated): SOC-analyst phishing-triage workflow — the wiki had `concepts/phishing.md` (offensive perspective) but no defensive-investigation counterpart despite Yahia Ch 1-2 dedicating ~50 pages to it. Email-threat taxonomy table (spearphishing-attachment / spearphishing-link / BEC / blackmail), attacker email-security evasion tradecraft table, common phishing subject/filename keyword catalog, Yahia's 5-sub-investigation workflow (sender reputation → spoofing validation → sender behavior → subject/filename → content/URL/attachment), SPF qualifier table + DKIM field table + DMARC field table, investigation tool stack (MxToolbox, Talos, URLscan, VirusTotal, ANY.RUN, CyberChef, AbuseIPDB), triage-outcome handoff table, 5 defender priorities.
- **NEW `entities/people/mostafa-yahia.md`** (draft): author-entity for Mostafa Yahia (Egyptian MSSP SOC lead, GCFA/GCIH/IBM QRadar/CCNA per Packt 2023 front matter — `[NEEDS VERIFICATION 2026-05-17]` for employer / LinkedIn). Mirrors the @entities/people/joas-a-santos.md pattern — defensive-investigation-side anchor (where Joas anchors offensive-side concept pages, Yahia anchors defensive-investigation pages).
- **`concepts/incident-response.md`** extended: added Ch 3 Windows event-log triage toolchain (Event Viewer, PsLogList, Event Log Explorer, EvtxECmd, HELK, Mordor datasets) with cost/use-case table; documented default log path `C:\Windows\System32\winevt\Logs`, registry-relocation key, Windows 11 336-default-log count, 6 Security-log event categories. Added `phishing-investigation` + `mostafa-yahia` backlinks.
- **`concepts/threat-intelligence.md`** extended: added "Canonical SOC-analyst pivot stack" section with the 4 named OSINT-TI pivots from Yahia Ch 14 (VirusTotal / IBM X-Force Exchange / AbuseIPDB / Google) as the Tier-1 first-touch stack before commercial feeds.
- **Backlinks** (bidirectional invariant held): added `concepts/phishing-investigation.md` ↔ `phishing`, `social-engineering`, `incident-response`, `threat-intelligence`, `soc-operations`, `threat-hunting`, `osint-for-cybersecurity`, `entities/people/mostafa-yahia`, `sources/effective-threat-investigation-soc-analysts`. Added `entities/people/mostafa-yahia` ↔ `phishing-investigation`, `soc-operations`, `threat-hunting`, `incident-response`, `effective-threat-investigation-soc-analysts`.
- **Index updated**: new Doctrine + methodology row for `concepts/phishing-investigation.md` (validated); new People row for `entities/people/mostafa-yahia.md` (draft).
- Source `read-status`: `unread-stub` count: 272 → 271 (`effective-threat-investigation-soc-analysts.md` now `skimmed`).
- **Deferred** (extraction-gap follow-up): `concepts/windows-event-log-investigation.md`, `concepts/powershell-attack-detection.md`, `concepts/lateral-movement-detection.md`, `concepts/firewall-log-investigation.md`, `concepts/proxy-log-investigation.md`, `concepts/dns-tunneling.md`, `concepts/c2-detection.md`, `concepts/waf-investigation.md`, `concepts/malware-sandboxing.md` — chapters exist in Yahia's TOC but body text + tables were not extractable.
- **Follow-up tracked**: re-extract Ch 4-15 of Basta et al. via pdftotext + page-range read; only then can `open-source-soc-guide.md` move to `read` + the deferred concept pages (`log-analysis`, `network-traffic-analysis`, `security-analytics-ml`, `insider-threat`) be created.

## [2026-05-17] cross-wiki route | gau + katana + gopacket + openvpn-install (OSINT 56-repo tool eval)

Cross-routed 4 security tools into this wiki from the OSINT-workspace 56-repo multi-wiki tool-evaluation ingest (`@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`). All 4 are cybersec-primary fit; verdicts are doc-level (Phase-0 clone audits still owed before production adoption). All 4 licenses are permissive — clean for the IP sale.

- **NEW `entities/tools/gau.md`** (draft): gau (getallurls), lc/gau, MIT, Go. Multi-provider known-URL discovery — fetches a domain's known URLs from AlienVault OTX, the Wayback Machine, and Common Crawl simultaneously. Passive recon / attack-surface mapping; established in Kali Linux. Tier: **Adopt**.
- **NEW `entities/tools/katana.md`** (draft): katana, projectdiscovery/katana, MIT, Go. Scriptable web crawler with standard HTTP + headless-browser modes; extracts URLs / JS paths / API endpoints from SPA frameworks; Go API (`NewCrawlerOptions`, `ClassifyPage`). ~1,567 commits, enterprise-grade lifecycle controls. Tier: **Adopt**. Fills the headless-browser (G5) gap noted in the cariddi audit.
- **NEW `entities/tools/gopacket.md`** (draft): gopacket, mandiant/gopacket, Apache-2.0, Go. High-performance packet-decoding library (decoding routines in `layers_decoder.go`); ~630 stars, 0 open issues. Tier: **Steal-from** — extract specific decoding logic into bespoke defensive tooling, not deploy whole.
- **NEW `entities/tools/openvpn-install.md`** (draft): openvpn-install, angristan/openvpn-install, Unlicense (public domain), Bash. Single-script secure OpenVPN deployment automation; notable for refined NAT detection + dual-stack DNS resolver handling (`resolvePublicIP()`) + extensive IPv6-routing edge-case handling. Tier: **Steal-from** — extract the IPv6-detection / routing shell snippets, not the monolithic installer.
- **Backlinks** (bidirectional invariant held): `gau` ↔ `concepts/bug-bounty`, `concepts/web-pentest-methodology`, `concepts/osint-for-cybersecurity`, `entities/tools/cariddi`, `entities/tools/katana`. `katana` ↔ `concepts/web-pentest-methodology`, `concepts/bug-bounty`, `entities/tools/cariddi`, `entities/tools/gau`, `entities/tools/osmedeus`. `gopacket` ↔ `concepts/network-security`, `concepts/threat-hunting`, `entities/tools/nmap`. `openvpn-install` ↔ `concepts/network-security`, `concepts/system-hardening`. All 4 backlink `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`.
- **`updated:` bumped** on pre-existing pages touched: `entities/tools/cariddi.md`, `entities/tools/nmap.md`, `concepts/web-pentest-methodology.md`, `concepts/bug-bounty.md`, `concepts/network-security.md`, `concepts/threat-hunting.md`, `concepts/system-hardening.md` (and `osint-for-cybersecurity.md` already at 2026-05-17).
- **Index updated**: 4 new Tools rows.

## [2026-05-17] deep-read | Splunk trio (110-query SPL catalog + SPL command reference + 24 SOC-2 use cases) — full extraction, splunk entity promoted to validated

Fifth BlueTeam Kit deep-read — first **full** extraction (not partial). Three small Splunk PDFs from the BlueTeam Kit Drive folder were read in full via `mcp__claude_ai_Google_Drive__read_file_content`: a community-curated 110-query SPL detection catalog, an alphabetical SPL command reference, and Rajneesh Gupta's 24 SOC-2-mapped SPL use cases. No extraction gap this time — the PDFs are small + structurally repetitive (cheatsheet format), so they fit within the read-stream budget. The `entities/tools/splunk.md` stub gets promoted from 1-paragraph draft to validated entity page with full SPL primer + catalog tables + SOC-2 mapping.

- **`sources/100-splunk-queries-soc-analyst.md`**: `unread-stub` → `read` (validated). Narrative restructured into 9 hunt-class categories (auth 28 / process 18 / lateral 8 / network+C2+exfil 15 / web-app 6 / ransomware 5 / recon+CVE 8 / phishing 3 / data+DDoS+ATO remainder). 5 verbatim Snippets (failed-logins, PowerShell encoded, RDP lateral, DNS tunneling, ransomware shadow-copy deletion).
- **`sources/splunk-commands-reference.md`**: `unread-stub` → `read` (validated). Narrative documents the high-value SPL command subset (search/stats/eval/where/rex/table/sort/dedup/top/timechart/chart/lookup/iplocation/transaction/streamstats/eventstats/join/append/makeresults/inputlookup) and the canonical SPL pipeline shape. 4 Snippets (pipeline canonical, rex named-capture, eventstats annotate, transaction caveat).
- **`sources/splunk-siem-soc2-use-cases.md`**: `unread-stub` → `read` (validated). Narrative maps Gupta's 24 use cases to Trust Service Criteria (CC6.1 Logical Access 13 use cases / CC6.6 Change Management 1 / CC6.7 System Operations 8 / CC6.8 Risk Mitigation 2). 3 Snippets (UC2 brute-force, UC9 exfil, UC21 config-change). Author Gupta noted as named-entity.
- **`entities/tools/splunk.md`**: 1-paragraph stub → validated entity page. Sections: SPL primer with pipeline mental model; Detection-query catalog with 9 hunt-class tables (~50 queries quoted across the rows); SPL command reference (the 20-command high-value subset); SOC 2 use-case mapping table (24 use cases by TSC); Pitfalls + cost discipline; Comparison vs QRadar + Wazuh. 6 verbatim Snippets. Dead Ends section (hash-based detection, join at scale, CVE-string-match, encoded-PowerShell on 4688 alone). Maturity: draft → validated.
- **NEW `entities/people/rajneesh-gupta.md`** (draft): author-entity stub for Rajneesh Gupta (@rajneeshcyber), author of the SOC 2 use-cases PDF. `[NEEDS VERIFICATION 2026-05-17]` for LinkedIn / employer / credentials.
- **Backlinks** (bidirectional invariant held — lint passed 0 gaps): added `entities/tools/splunk.md` ↔ `concepts/threat-hunting`, `concepts/incident-response`, `concepts/endpoint-detection-response`, `concepts/ransomware`, `concepts/phishing-investigation`, `concepts/threat-intelligence`, `entities/frameworks/mitre-attack`, `entities/tools/sysmon`, `sources/effective-threat-investigation-soc-analysts`, `sources/open-source-soc-guide`, `sources/soc-analyst-book`, `entities/people/rajneesh-gupta`. Added `sources/100-splunk-queries-soc-analyst.md` ↔ `incident-response`, `ransomware`, `phishing-investigation`, `mitre-attack`, `sysmon`. Added `sources/splunk-commands-reference.md` ↔ `threat-hunting`. Added `sources/splunk-siem-soc2-use-cases.md` ↔ `incident-response`, `threat-hunting`, `rajneesh-gupta`. Added `rajneesh-gupta` ↔ `siem`, `soc-operations`, `splunk`.
- **Index updated**: `entities/tools/splunk.md` maturity row bumped draft → validated with detailed description. New People row for `entities/people/rajneesh-gupta.md` (draft).
- Source `read-status`: `unread-stub` count: 271 → 268 (3 Splunk source pages now `read`).

## [2026-05-17] partial-ingest | Building a Next-Gen SOC with IBM QRadar (Kothekar, Packt 2023) — Ch 1-4 extracted, Ch 5-12 deferred. Final BlueTeam Kit queue item.

Sixth BlueTeam Kit deep-read — second partial-extraction pattern (matches Basta SOC guide + Yahia SOC textbook). The 126,426-character PDF (file ID `1F6E53JLQJcB88lGcrfa7Q9s68o46bM7j`, located via past-transcript JSONL `tool_use_id` match because Drive `search_files` returns empty for the shared folder) exceeds inline read budget. Subagent delegation surfaced Ch 1-4 in full (~36% body coverage); Ch 5-12 are TOC-summary only. Honest path: write what's extracted, flag what isn't, defer the rest.

- **`sources/next-gen-soc-ibm-qradar.md`**: `unread-stub` → `skimmed` (NOT `read`); Narrative expanded with full author/publisher/ISBN/page-count metadata (Kothekar, Packt 2023, ISBN 978-1-80107-602-9, 12 chapters / 3 parts / ~165 body pages), TOC structure (Part I Foundations / Part II Detection+tuning / Part III Apps+ops), extraction-coverage table marking ✅ vs ⚠️ TOC-only per topic. Next-extraction priority: WinCollect (Ch 12) > rule-wizard+AQL (Ch 5-7).
- **`entities/tools/qradar.md`**: 6-line draft stub → validated entity page. Sections: Architecture overview (Console + N managed-host taxonomy table: EP, EC, FP, QFlow, Data Node, QNI, QRIF, QPCAP, QVM, QRM, App Host, DLC); Console + EP subservices (Tomcat, hostcontext, hostservices, ecs-ec-ingress, ecs-ec, ecs-ep, qflow, accumulator, ariel-proxy/query); Two-database split (Ariel time-series local + Postgres config replicated) with operator-implication framing; Core concepts table (event, flow, log source, DSM, offense, BB, rule, reference set, coalescing, traffic analysis); Ingestion protocols (active vs passive); Flow capture + 64-byte payload foot-gun + Superflow types A/B/C with detection use; Custom Rule Engine kinds (event/flow/common/offense/anomaly/behavioral); One end-to-end CRE example (Linux SSH brute force from Ch 4); EPS/FPM licensing model + 7.4 single-capacity-license transition + sizing math (2 TB/day ≈ 46,296 EPS); Deployment topologies (all-in-one / distributed / HA / DR / Community Edition); Upgrade pitfalls (GlusterFS→DRBD, Patch All UI button); Operator foot-guns (JDBC marker-file, time-zone drift, UDP-514 syslog, App Host mandate for UBA/Watson); Apps + extensions section (TOC-only with `[NEEDS VERIFICATION 2026-05-17]`); Comparison table vs Splunk + Wazuh. 3 verbatim Snippets. Dead Ends section explicitly cataloging the 4 extraction gaps (AQL syntax, rule-writing patterns, UBA/Watson/UCM, WinCollect). Maturity: draft → validated.
- **NEW `entities/people/ashish-m-kothekar.md`** (draft): author-entity stub for Ashish M Kothekar (IBM SWAT/SME path, 16+ years IBM Security threat-management products per book front matter). `[NEEDS VERIFICATION 2026-05-17]` for current employer / LinkedIn / additional publications.
- **Backlinks** (bidirectional invariant held — lint passed 0 gaps): added `entities/tools/qradar.md` ↔ `concepts/threat-hunting`, `concepts/incident-response`, `concepts/endpoint-detection-response`, `entities/tools/sysmon`, `sources/open-source-soc-guide`, `entities/people/ashish-m-kothekar`. Added `sources/next-gen-soc-ibm-qradar.md` ↔ `concepts/threat-hunting`, `concepts/incident-response`, `concepts/endpoint-detection-response`, `entities/tools/splunk`, `entities/tools/wazuh`, `entities/tools/sysmon`. Added `entities/people/ashish-m-kothekar.md` ↔ `concepts/siem`, `concepts/soc-operations`.
- **Index updated**: `entities/tools/qradar.md` maturity row bumped draft → validated with detailed description. New People row for `entities/people/ashish-m-kothekar.md` (draft).
- Source `read-status`: `unread-stub` count: 268 → 267 (`next-gen-soc-ibm-qradar.md` now `skimmed`).
- **BlueTeam Kit deep-read queue: CLEARED.** All 26 BlueTeam Kit PDFs are now either `read` (Splunk trio: 3 PDFs), `skimmed` with extraction-gap documented (Basta SOC, Yahia SOC textbook, Kothekar QRadar: 3 PDFs), or remain at `unread-stub` (20 lower-priority PDFs that weren't part of the targeted deep-read pass for SIEM / threat-hunting / EDR / IR / phishing / SOC-architecture). Next-extraction priorities recorded per partial-ingest entry (Basta Ch 4-15; Yahia Ch 4-15 Windows event tables; Kothekar Ch 12 WinCollect + Ch 5-7 AQL/rule-wizard).

## [2026-05-19] ingest | Python Ethical Hacking MASTERCLASS — Zero to Mastery (video course)

User dropped a Google Drive folder link with no instructions; established pattern → ingest. Folder `1Uc1I973Cg7Mo6j_KYgsHReC0kR9Jq-OM` ("SaleWebDesign.Com-Python-Ethical-Hacking-MASTERCLASS-Zero-Mastery", owner `horahibarish@gmail.com`, created 2023-04-26). Drive API cannot enumerate shared-folder children (known trap) → Playwright scrape of `[data-id]` nodes returned 19 titled section subfolders + 4 marketing `.txt` junk files. Second video course in the corpus (after Kali For 2023) → same handling: video has no transcripts, not synthesizable into prose, catalogued as **one** `unread-stub` source page (per user decision, KALI precedent).

- **NEW `sources/python-ethical-hacking-masterclass.md`** (draft, `unread-stub`): source page for the 19-section video course. Curriculum table — sections 1–11 generic Python language (setup → essentials → control flow → loops → data structures → functions/modules → classes → exceptions → network programming → file I/O); sections 12–19 entry-level ethical hacking (testing lab → Linux CLI → anonymity → information gathering → port scanning → gaining access → maintaining access → wrap-up). Follows the standard recon→scan→exploit→persist kill-chain arc paired with a from-scratch Python primer. Provenance note: folder carries `GET 100% OFF COUPONS.txt` / `SaleWebDesign.Com` marketing artefacts characteristic of a repackaged/pirated paid course — noted for honesty, not endorsed.
- **Backlinks** (bidirectional invariant held): added `sources/python-ethical-hacking-masterclass.md` ↔ `entities/programming-languages/python.md`, `entities/tools/kali-linux.md`, `entities/tools/nmap.md`, `entities/tools/metasploit.md`, `concepts/osint-for-cybersecurity.md`, `concepts/anonymity-networks.md`. 6 pages patched (frontmatter `related:` + body `## Relations`), `updated:` bumped to 2026-05-19 on each.
- **Index updated**: Sources count 275 → 276; the video-course line now reads "**2** video courses" (Kali Linux 2023 + Python Ethical Hacking MASTERCLASS).
- No raw source moved — Drive-only, consistent with the four-folder corpus storage decision.

## [2026-05-21] ingest | Cross-wiki brief triage — 15 briefs inventoried, 11 entity stubs + 31 index entries created

All 15 briefs in `briefs/` triaged: 5 already-ingested (content previously folded into wiki during K42 Phase-1 adoption) + 10 unprocessed cross-wiki routing briefs from OSINT wiki tool evaluations.

**11 new entity stub pages** (Adopt/Steal-from tier):
- `entities/tools/defenseclaw.md` — Cisco AI Defense (Apache-2.0, 654 stars)
- `entities/tools/deepzero.md` — Windows kernel-driver vuln research (MIT, 425 stars)
- `entities/tools/grex.md` — Regex generation for SOC/IR (Apache-2.0, ~8,129 stars)
- `entities/tools/vanguard.md` — Single-binary DFIR toolkit (MIT, ~118 stars)
- `entities/tools/raptor.md` — Claude Code offensive/defensive agent (Steal-from)
- `entities/tools/src-hunter-skill.md` — Claude Code bug-bounty skill (MIT, 305 payloads)
- `entities/tools/bluehood.md` — Bluetooth telemetry monitoring (MIT, 977 stars)
- `entities/tools/super-spr.md` — Zero-trust networking (BSD-3-Clause, 565 stars)
- `entities/tools/reconftw.md` — Apex recon automation (MIT, 7.5k+ stars)
- `entities/tools/evilsocket-audit.md` — 8-stage vuln-discovery agent, Glasswing pattern (MIT, 388 stars)
- `entities/tools/offensive-claude.md` — Claude Code offensive workstation, 25 skill modules

**~31 index-only catalog entries** (Steal-from/Defer/Reference tier) added to `wiki/index.md` under new "Cross-wiki routed tool evaluations" subsection, covering K42 (9 items), K15 (2), K53 (2), K51 (5), K54 (6), K55 (3), K56 (2).

**~18 Reject-tier items** dropped (not catalogued).

**Bidirectional invariant**: 18 existing concept/tool pages received backlinks for new entity stubs. Lint verified: 0 orphans, 0 bidirectional gaps across 422 pages.

**All 15 briefs** marked `processed: 2026-05-21`.

## [2026-05-22] ingest | Cross-wiki brief triage — K55-2 + K57 (2 new briefs)

**K55-2** (`briefs/2026-05-21_k55-2-cybersec-toolset-from-osint-tool-eval.md`): Ran `gh api` license verification on 6 primary-fit entries. Results: `Awesome-Hacking` CC0-1.0, `open-source-web-scanners` Apache-2.0, `jadx-ai-mcp` Apache-2.0, `reconftw` MIT (already `@entities/tools/reconftw.md`), `CF-Hero` and `LLM4Pentest` still no SPDX license.

- **NEW** `@entities/tools/cf-hero.md` (draft, Defer) — Cloudflare origin-IP discovery stub; adoption gated on manual LICENSE audit
- **Updated** `@entities/tools/jadx-mcp-server.md` — K55-2 sibling note for `jadx-ai-mcp`
- **Index**: 5 K55-2 rows in cross-wiki eval table; `cf-hero` row in main Tools table; `LLM4Pentest` tier bumped Reference → Defer with K55-2 cross-ref
- **Backlinks**: `cf-hero` ↔ `web-pentest-methodology`, `osint-for-cybersecurity`, `reconftw`

**K57** (`briefs/2026-05-22_k57-cybersec-tool-eval-rejects-from-osint.md`): Reject-tier methodology reference only — no entity stubs. **4 index rows** added (Galaxy-Bugbounty-Checklist, BugBounty-Recon-Methodology, sqlmap, NoSQLMap). `open-source-web-scanners` already indexed from K55-2 with verified Apache-2.0.

Both briefs marked `processed: 2026-05-22`.

## [2026-05-23] ingest | Cross-wiki brief triage — K60 (1 new brief)

**K60** (`briefs/2026-05-23_k60-cybersec-tool-eval-from-osint.md`): 20-URL OSINT eval; four cybersec-routed items.

- **NEW** `@entities/tools/pentest-ai.md` (draft, CONDITIONAL-GO Phase-0) — `0xSteph/pentest-ai` MCP + `ptai` CLI; MIT verified; distinct from validated `pentest-ai-agents`
- **Updated** `@entities/tools/pentest-ai-agents.md` — sibling cross-link; removed stale "out of scope" wording
- **Index**: 4 K60 rows (KaliGPT Reject/NC, h4cker Reference, pentest-ai entity, NVISO catalog Defer) + main Tools table row for `pentest-ai`
- **Backlinks**: `pentest-ai` ↔ `llm-pentest-automation`, `ai-for-cybersecurity`, `pentest-ai-agents`

No entity stubs for KaliGPT (commercial NC), h4cker (reference catalog), or NVISO catalog (no SPDX).

Brief marked `processed: 2026-05-23`.

## [2026-05-24] ingest | Cross-wiki brief triage — K63 Nidhogg (1 new brief)

**K63** (`briefs/2026-05-24_k63-cybersec-nidhogg-from-osint.md`): `Idov31/Nidhogg` — GPL-3.0 Windows kernel rootkit (~2.4k★). Steal-from tier: DKOM / `ActiveProcessLinks` process-hiding tradecraft for blue-team MITRE mapping; **no binary import**.

- **NEW** `@entities/tools/nidhogg.md` (draft, Steal-from) — defensive tradecraft table + T1014/T1562 anchors; GPL deployment boundary documented
- **Index**: K63 row in cross-wiki eval table + main Tools table row
- **Backlinks**: `nidhogg` ↔ `av-edr-bypass`, `endpoint-detection-response`, `malware-analysis`, `privilege-escalation`, `red-team-operations`, `mitre-attack`

Brief marked `processed: 2026-05-24`.

## [2026-05-26] ingest | Cross-wiki brief triage — K68 (1 new brief)

**K68** (`briefs/2026-05-26_k68-cybersec-tool-eval-from-osint.md`): 22-URL OSINT eval; five cybersec-routed repos.

- **NEW** `@entities/tools/iron-proxy.md` (draft, Adopt-eligible) — egress firewall for untrusted workloads (Apache-2.0)
- **NEW** `@entities/tools/cryptex-oss.md` (draft, Adopt-eligible) — LLM red-team transform/mutator toolkit (MIT, 162 transforms)
- **Index**: 3 Steal-from/Reject rows (facex, centaur, ZishanAdThandar/pentest GPL-3.0)
- **Backlinks**: `iron-proxy` ↔ zero-trust, network-security, defense-in-depth, container-security, agent-vm-sandboxing; `cryptex-oss` ↔ llm-adversarial-fuzzing, ai-for-cybersecurity, fuzzyai

Brief marked `processed: 2026-05-26`.

## [2026-05-27] ingest | Cross-wiki brief triage — K71 (1 new brief)

**K71** (`briefs/2026-05-27_k71-cybersec-tooling-from-osint.md`): 27-URL OSINT eval; two cybersec-routed items — both **index-only**, no entity stubs.

- **Reference**: Hackers-Arise AI enumeration article (methodology only, no code) — complements existing K54 Hackers-Arise MCP log index row
- **Reject**: `blacklanternsecurity/bbot` — AGPL-3.0 confirmed via `gh api`; copyleft poison pill for IP-sale surfaces (same posture as TruffleHog/gitGraber)

**Index**: 2 K71 rows added to cross-wiki eval table.

Brief marked `processed: 2026-05-27`.

## [2026-05-28] ingest | Cross-wiki brief triage — K73 (1 new brief)

**K73** (`briefs/2026-05-28_k73-security-tool-phase0-outcomes.md`): security-tool Phase-0 outcome routing from OSINT wiki.

- **NEW** `@entities/tools/cve-mcp-server.md` (draft, CONDITIONAL-GO) — Apache-2.0 security-intel MCP server for CVE/EPSS/KEV/ATT&CK enrichment in cybersec workstation workflows
- **Reject reiterated**: `blacklanternsecurity/bbot` AGPL-3.0 copyleft posture remains reject for IP-sale-bearing production surfaces (already indexed under K71; now annotated K71,K73)
- **Index**: 1 new K73 row (`cve-mcp-server`) + bbot brief provenance widened to `K71, K73`
- **Backlinks**: `cve-mcp-server` ↔ `threat-intelligence`, `threat-hunting`, `osint-for-cybersecurity`, `incident-response`, `pentest-ai`

Brief marked `processed: 2026-05-28`.

## [2026-05-31] ingest | Cross-wiki brief triage — K88 (1 new brief)

**K88** (`briefs/2026-05-31_k88-skillspector-cybersec-from-osint.md`): skill/MCP supply-chain eval from OSINT wiki.

- **NEW** `@entities/tools/nvidia-skillspector.md` (draft, Adopt) — Apache-2.0 agent/MCP skill supply-chain scanner; LangGraph `skillspector.graph` API; import boundary: cybersec workstation vetting only, no trading-stack integration until Phase-0 lab validation
- **Reference**: `FareedKhan-dev/train-llm-from-scratch` (MIT) — index-only
- **Reject**: `ahegazy0/linux-basics-for-hackers-notes` (no LICENSE); `LHRLAB/Graph-R1` (NC-SA per eval; gh api MIT 2026-05-31 — verify before override)
- **Index**: 1 Tools row + 4 cross-wiki eval rows (Adopt + Reference + 2 Reject)
- **Backlinks**: `nvidia-skillspector` ↔ `ai-for-cybersecurity`, `npm-supply-chain-defense`, `llm-pentest-automation`, `defenseclaw`, `claude-code-ultimate-guide`, `src-hunter-skill`

Brief marked `processed: 2026-05-31`.

## [2026-06-01] ingest | Cross-wiki brief triage — K93 (1 new brief)

**K93** (`briefs/2026-06-01_k93-cybersec-digest-netviz-from-osint.md`): federated daily digest install + netviz Adopt upgrade.

- **Structural**: federated daily digest installed (`scripts/daily_research_digest_run.py`, `daily_research_fetch.py`, `daily_research_config.yaml`, `wiki/sweeps/`, `wiki/meta/daily-research-digest-cadence.md`); LaunchAgent `com.cemini.daily-research-digest.cybersec` written to `~/Library/LaunchAgents/` (not tracked)
- **NEW** `@entities/tools/netviz.md` (draft, Adopt) — `ShadowArcanist/netviz` MIT; upgraded from K53 Steal-from; Phase-0 analyst-laptop only
- **Index**: netviz cross-wiki row upgraded `Steal-from K53` → `Adopt K53, K93` + Tools table row
- **Backlinks**: `netviz` ↔ `osint-for-cybersecurity`, `threat-intelligence`, `red-team-operations`, `maltego`, `bloodhound`, `reconftw`

Brief marked `processed: 2026-06-01`.

## [2026-06-01] ingest | Agent security arXiv cluster (5 PDFs)

**Source**: daily digest inbox — five May 2026 arXiv papers on tool-using agent security.

- **NEW** `@concepts/agent-runtime-guardrails.md` (draft) — synthesizes failure modes (authority confusion, permission laundering, sleeper attack, dual-surface injection) + defenses (ePCA, AIRGuard, ChainCaps) + eval hygiene (AAR, per-surface ASR)
- **NEW** `@entities/tools/airguard.md` (draft, CONDITIONAL-GO) — MIT runtime authority guard; paper arXiv:2605.28914
- **NEW** `@entities/tools/chaincaps.md` (draft, Reference) — MCP composition IFC pattern; paper arXiv:2605.26542
- **5 source pages** (1 deep-read anchor 2605.29251 ePCA guardrail + 4 read): 28914, 26542, 28201, 30454
- **Backlinks**: `agent-runtime-guardrails` ↔ `ai-for-cybersecurity`, `llm-adversarial-fuzzing`, `llm-pentest-automation`, `agent-vm-sandboxing`, `crescendo-multi-turn-jailbreak`, `defenseclaw`, `nvidia-skillspector`, `iron-proxy`, `airguard`, `chaincaps`
- **Raw sources** moved to `raw-sources/`

## [2026-06-02] ingest | Daily digest inbox — 2 agent-security papers

**Source**: AM digest run (`wiki/sweeps/2026-06-02-daily.md`) — ClawHub scanner study + AgentRedBench.

- **NEW** `@sources/arxiv-2606-01494-clawhub-security-signals.md` — VT vs static vs SkillSpector on 67k+ OpenClaw skills
- **NEW** `@sources/arxiv-2606-02240-agentredbench.md` — dynamic redteam + AgentRedGuard for SaaS integrations
- **NEW** `@entities/tools/agentredguard.md` (draft, Reference)
- **Updated** `@concepts/agent-runtime-guardrails.md` — layered skill governance + integration-aware guards
- **Backlinks** `nvidia-skillspector`, `airguard`, `llm-adversarial-fuzzing`, `index.md`
- **Sweep** `2026-06-02-daily.md` marked ingested; PDFs → `raw-sources/`
- **Ops** `~/bin/cemini-daily-research-digest-cybersec` loads `~/.cemini/exa-api-key` + `.env` for LaunchAgent (fixes exit 2 when key missing under launchd)

## [2026-06-04] ingest | Cross-wiki brief K98 — SeClaw agent security eval

**K98** (`briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md`): arXiv:2606.02302 trajectory-aware agent security benchmark.

- **NEW** `@sources/arxiv-2606-02302-seclaw-spec-driven-agent-security.md` (read)
- **NEW** `@entities/tools/seclaw-eval.md` (draft, Reference — no LICENSE on GitHub API at Phase-0)
- **Updated** `agent-runtime-guardrails`, `llm-pentest-automation`, `llm-adversarial-fuzzing`, `index.md`
- **Backlinks** OSINT `@osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md` + `@osint-wiki/concepts/seclaw-agent-security-evaluation.md`
- **PDF** → `raw-sources/arxiv-2606.02302-seclaw-spec-driven-security-task-synthesis-for-e.pdf`
- Brief marked processed 2026-06-04

## [2026-06-04] ingest | Daily digest — OWASP LLM defense attribution (arXiv:2606.02822)

**Source**: `research to be indexed/` — daily digest fetch.

- **NEW** `@sources/arxiv-2606-02822-owasp-llm-defense-attribution.md` (read)
- **NEW** `@entities/tools/llm-defense-lattice.md` (draft, Reference — GitHub license NOASSERTION)
- **Updated** `agent-runtime-guardrails`, `llm-adversarial-fuzzing`, `llm-pentest-automation`, `ai-for-cybersecurity`, `defenseclaw`, `cryptex-oss`, `seclaw-eval`, `index.md`
- **PDF** → `raw-sources/arxiv-2606.02822-which-defense-closes-which-threat-attributing-ow.pdf`
- **Sweep** `2026-06-04-daily.md` marked ingested

## [2026-06-04] ingest | CCC handoff — defenseclaw sidecar + SeClaw eval canon

**Brief:** `@ccc-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md`

- **Updated** `@entities/tools/defenseclaw.md` — sidecar install (`DEFENSECLAW_LLM_KEY`, port 18970), MCP scanner runbook, Splunk/OTel optional; CONDITIONAL-GO CLI scanners (CCC trial 2026-06-04)
- **NEW** `@concepts/seclaw-agent-security-evaluation.md` — canonical trajectory-eval concept; CCC/OSINT remain methodology pointers
- **Backlinks** `seclaw-eval`, `agent-runtime-guardrails`, `index.md` adopt row for defenseclaw
- Brief marked processed 2026-06-04

## [2026-05-31] query | defenseclaw sidecar trial — Codex observe runbook

- **Executed** laptop sidecar trial: `defenseclaw-gateway start` on `:18970`, `defenseclaw setup codex --yes --restart` — 18/3/10 doctor; health OK
- **Updated** `@entities/tools/defenseclaw.md` — full Codex sidecar trial runbook, adoption table bumped to observe-mode ADOPTED
- **Updated** `index.md` adopt row — sidecar observe adopted

## [2026-05-31] ops | defenseclaw sidecar stopped (on-demand)

- Sidecar not always-on — stopped after trial; CLI scanners remain on PATH
- **Updated** `@entities/tools/defenseclaw.md` — adoption table notes on-demand sidecar

## [2026-06-03] ingest | K95 — skill injection cluster (3 arXiv)

- **Sources** — 2606.00485 Confused ChatGPT, 2606.01567 defenses/enablers, 2606.03024 SkillGuard
- **Concept** — `agent-skill-injection.md`
- **Cross-wiki** — steal permission model → `@ccc-wiki/concepts/skill-vetting.md`; OSINT prod brief `2026-06-03_k95-skillguard-permission-steal-cemini-prod`
- **PDFs** → librarian; inbox cleared

## [2026-06-05] ingest | K100 — MCP security + NeuroLog batch (5 arXiv)

- **Sources** — 2606.00669 NeuroLog (OSINT handoff); 2605.24248 attested tool admission; 2606.04425 prompt injection persistence; 2606.04769 MCP description–code drift; 2606.05567 ZERO-APT
- **Concepts** — `mcp-security-posture`, `neuro-symbolic-auditable-reasoning`
- **PDFs** → librarian; inbox cleared

## [2026-05-31] deep-read | K100 — MCP security + NeuroLog batch (5 arXiv)

- **Deep-read** all 5 K100 sources (`read_status: read`) — attested MCP admission, SPI benchmark, DCI measurement, ZERO-APT, NeuroLog
- **Promoted** `@concepts/mcp-security-posture.md`, `@concepts/neuro-symbolic-auditable-reasoning.md` → **validated**
- **Updated** `agent-runtime-guardrails`, `agent-skill-injection`, `llm-pentest-automation`, `llm-vulnerability-discovery`, `defenseclaw`, `index.md`
- **PDFs** archived to `raw-sources/` (2605.24248, 2606.00669, 2606.04425, 2606.04769, 2606.05567)

## [2026-05-31] brief | K100 SPI checklist + prod-mcp allowlist

- **NEW** `briefs/2026-05-31_ccc-handoff-k100-spi-skill-vetting-checklist.md` → CCC skill-vetting steps 9–11
- **NEW** `briefs/2026-05-31_prod-mcp-allowlist-draft-k100.md` → lazy-tool / prod-mcp deny-by-default YAML draft
- **OSINT mirror** `briefs/2026-05-31_prod-mcp-allowlist-draft-k100-from-cybersec.md` + `.cursor/mcp-allowlist-draft.yaml`

## [2026-06-06] ingest | Daily digest — BAS→Sigma + WebMCP MSTI (2 arXiv)

**Source**: `research to be indexed/` — daily digest fetch (2026-06-06 sweep).

- **NEW** `@sources/arxiv-2606-05252-bas-to-siem-detection-as-code-synthesis.md` (read) — deterministic locked-corpus finding → Sigma starter rules; OpenSearch replay 30%/14% held-out fire rates
- **NEW** `@sources/arxiv-2606-06387-webmcp-tool-surface-poisoning.md` (read) — Mid-Session Tool Injection (MSTI): hijacking up to 100% ASR, framing with 85% task completion
- **Updated** `siem`, `mcp-security-posture`, `agent-runtime-guardrails`, `llm-defense-lattice`, `arxiv-2606-02822-owasp-llm-defense-attribution`, `index.md`
- **PDFs** → `raw-sources/arxiv-2606.05252-from-attack-simulation-to-siem-rule-determin.pdf`, `raw-sources/arxiv-2606.06387-webmcp-tool-surface-poisoning-runtime-manipulati.pdf`
- **Inbox cleared** — 2/2 files ingested

## [2026-06-06] brief | K102 — defending-code reference harness

**Brief:** `briefs/2026-06-06_k102-cybersec-defending-code-harness-from-osint.md`

- **NEW** `@entities/tools/defending-code-reference-harness.md` (draft, CONDITIONAL-GO — Apache-2.0, laptop Docker/gVisor only)
- **NEW** `@concepts/docker-agent-sandbox-allowlist-proxy.md` — vp-internal + egress allowlist pattern
- **Updated** `agent-vm-sandboxing`, `llm-vulnerability-discovery`, `exploit-development`, `agent-skill-injection`, `index.md`
- **Backlinks** `@osint-wiki/entities/tools/defending-code-reference-harness.md`
- **Brief triage:** K100 CCC handoff → processed (CCC skill-vetting steps 9–11 live); prod-mcp allowlist → delivered (YAML in OSINT `.cursor/`); world-cup audit → archived (2026-06-03 drop)

## [2026-06-07] ingest | Daily digest — agent execution provenance survey (arXiv 2606.04990)

**Source**: `research to be indexed/` — daily digest fetch (2026-06-07 sweep).

- **NEW** `@sources/arxiv-2606-04990-agent-traces-evidence-provenance.md` (read) — 33-page survey: evidence tracing + execution provenance taxonomy, benchmark gap analysis
- **NEW** `@concepts/agent-execution-provenance.md` — process-level accountability framework mapped to K95–K100 wiki stack
- **Updated** `agent-runtime-guardrails`, `seclaw-agent-security-evaluation`, `mcp-security-posture`, `agent-skill-injection`, `ai-for-cybersecurity`, `siem`, `index.md`
- **PDF** → `raw-sources/arxiv-2606.04990-from-agent-traces-to-trust-evidence-tracing-and.pdf`
- **Inbox cleared** — 1/1 file ingested

## [2026-06-09] ingest | Daily digest — MalSkillBench, Synthetic APTs, POISE (3 arXiv papers)

**Source**: `research to be indexed/` — daily digest fetch (2026-06-09 sweep).

- **NEW** `@sources/arxiv-2606-07131-malskillbench-runtime-verified-malicious-skills.md` (read) — 3,944 runtime-verified malicious skills; CI 98.4% vs PI collapse; wild-only eval bias up to 66 recall pts
- **NEW** `@sources/arxiv-2606-07158-synthetic-apts-ttp-attribution-collapse.md` (read) — CSI APT personas converge at Recon/IA; Velociraptor-as-C2 in 8/10 enterprise runs; topology > persona
- **NEW** `@sources/arxiv-2606-07943-poise-position-aware-skill-injection.md` (read) — ASR = payload + task-verifier pass; 89.3% on Skill-Inject; body placement stealth
- **NEW** `@entities/tools/malskillbench.md` (draft, Reference — GitHub `lxyeternal/MalSkillBench`)
- **Updated** `agent-skill-injection`, `agent-runtime-guardrails`, `threat-intelligence`, `adversary-emulation`, `nvidia-skillspector`, `index.md`
- **PDFs** → `raw-sources/arxiv-2606.07131-malskillbench-a-runtime-verified-benchmark-of-ma.pdf`, `raw-sources/arxiv-2606.07158-synthetic-apts-the-collapse-of-ttp-based-attribu.pdf`, `raw-sources/arxiv-2606.07943-poise-position-aware-undetectable-skill-injectio.pdf`
- **Inbox cleared** — 3/3 files ingested

## [2026-06-11] ingest | Daily digest — AutoSUT, CFD, Secure LLM Agents survey (3 arXiv papers)

**Source**: `research to be indexed/` — daily digest fetch (2026-06-11 sweep).

- **NEW** `@sources/arxiv-2606-08700-autosut-environment-semantics-gap.md` (read) — environment semantics gap in ATT&CK STIX; 97.6% software lacks version+CPE; non-unique SUT witness CVE-2021-41773
- **NEW** `@sources/arxiv-2606-09084-context-fractured-decomposition-attacks.md` (read) — CFD provenance gap; +28.14 pp ASR vs Crescendo/ToA; lineage tagging mitigation
- **NEW** `@sources/arxiv-2606-10749-toward-secure-llm-agents-survey.md` (read) — 247-paper lifecycle survey; compositional defense gap; stateful/multi-agent risks
- **NEW** `@entities/tools/autosut.md` (draft, Reference — GitHub reproducibility artifact)
- **NEW** `@concepts/context-fractured-decomposition-attacks.md` — artifact-mediated cross-session jailbreak class
- **Updated** `adversary-emulation`, `threat-intelligence`, `agent-execution-provenance`, `agent-runtime-guardrails`, `crescendo-multi-turn-jailbreak`, `ai-for-cybersecurity`, `mcp-security-posture`, `mitre-attack`, `index.md`
- **PDFs** → `raw-sources/arxiv-2606.08700-autosut-the-environment-semantics-gap-in-structu.pdf`, `raw-sources/arxiv-2606.09084-context-fractured-decomposition-attacks-on-tool.pdf`, `raw-sources/arxiv-2606.10749-toward-secure-llm-agents-threat-surfaces-attacks.pdf`
- **Inbox cleared** — 3/3 files ingested

## [2026-06-12] ingest | Daily digest — 6G CPS closed-loop security survey (arXiv 2606.08173)

**Source**: `research to be indexed/` — daily digest fetch (2026-06-12 sweep).

- **NEW** `@sources/arxiv-2606-08173-ai-native-closed-loop-6g-cps-security.md` (read) — PRISMA 128-study survey; MEC sense/detect → O-RAN/SDN mitigate → FL retrain; ATT&CK + CDR feature space
- **NEW** `@concepts/6g-cps-closed-loop-security.md` — OT/smart-grid/V2X defensive architecture synthesis
- **Updated** `network-security`, `soc-operations`, `siem`, `zero-trust`, `threat-intelligence`, `ai-for-cybersecurity`, `wireless-pentest`, `mitre-attack`, `index.md`
- **PDF** → `raw-sources/arxiv-2606.08173-ai-native-closed-loop-security-for-6g-enabled-cy.pdf`
- **Inbox cleared** — 1/1 file ingested

## [2026-06-12] ingest | K112 Google discovery-doc fuzzing + K113 AI-Research-SKILLs brief

- **K112** — `concepts/google-discovery-document-api-fuzzing.md` + `sources/brief-k112-cybersec-google-ai-api-fuzzing-2026-06-12.md` from OSINT Posts Post 4
- **K113 brief staged** — `briefs/2026-06-12_k113-cybersec-ai-research-skills-from-osint.md` (Orchestra skills subset; entity on OSINT)
- **Cross-wiki** — `@osint-wiki/sources/trading-posts-compilation-9-2026-06-12.md`, `@osint-wiki/sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md`

## [2026-06-12] ingest | K113 AI-Research-SKILLs entity + laptop inventory

- **Entity** — `entities/tools/ai-research-skills.md` (cherry-pick map: safety-alignment, post-training, PEFT, distributed, MLOps)
- **Source** — `sources/brief-k113-cybersec-ai-research-skills-2026-06-12.md`
- **Updated** — `seclaw-agent-security-evaluation`, `google-discovery-document-api-fuzzing`, `index.md`
- **Trial** — 98 SKILL.md counted on laptop clone; full npx install operator-gated

## [2026-06-13] ingest | K114 — VATS + containment gap

**Source**: `research to be indexed/` — daily digest fetch (2026-06-13 sweep); federation K114 cross-wiki ingest.

- **NEW** `@sources/arxiv-2606-07992-vats-error-path-mcp-injection-2026-06-13.md` (read, **GO**) — error-path MCP IPI; 3× baseline ACR; $M_4$ middle universal exploit; framework vs model alignment gap
- **NEW** `@sources/arxiv-2606-12797-agentic-containment-gap-framework-audit-2026-06-13.md` (read, **GO**) — P1–P6 framework audit; zero native compliance; memory poison 88.9% targeted denial; sub-ms deterministic gates
- **NEW** `@concepts/agentic-containment-principles.md` — P1–P6 matrix + LangChain/AutoGPT/OpenAI SDK compliance table
- **Updated** `mcp-security-posture`, `agent-runtime-guardrails`, `agent-skill-injection`, `index.md`
- **PDFs** remain in inbox pending `raw-sources/` move — operator-gated per ingest ritual
- **Inbox** — 2/2 files wiki-ingested (PDF move deferred)

## [2026-06-15] ingest | GT-MCP trajectory context control (2606.10322)

**Source**: `research to be indexed/arxiv-2606.10322-game-theoretic-multi-agent-control-for-robust-co.pdf` — daily digest sweep.

- **NEW** `@sources/arxiv-2606-10322-game-theoretic-multi-agent-context-control-gt-mcp.md` (read, **Reference** — no public code artifact)
- **NEW** `@concepts/trajectory-context-control.md` — GT-MCP control loop, trust signals, layer placement vs K100
- **Brief** `briefs/2026-06-15_gt-mcp-trajectory-context-control-harness.md` — prod-mcp memory-commit gate draft
- **Updated** `agent-runtime-guardrails`, `mcp-security-posture`, `ai-for-cybersecurity`, `agentic-containment-principles`, `context-fractured-decomposition-attacks`, `crescendo-multi-turn-jailbreak`, `arxiv-prompt-injection-persistence-2606.04425`, `index.md`
- **Phase-0** Reference — await GT-MCP implementation + LICENSE before CONDITIONAL-GO
- **PDF** → `raw-sources/arxiv-2606.10322-game-theoretic-multi-agent-context-control-gt-mcp.pdf`
- **Inbox cleared** — 1/1 file ingested

## [2026-06-16] ingest | SEVRA-BENCH — LLM PR review agent social engineering

**Source**: `research to be indexed/arxiv-2606.13757-sevra-bench-social-engineering-of-vulnerabilitie.pdf`

- **NEW** `@sources/arxiv-2606-13757-sevra-bench-social-engineering-review-agents.md` (read, **Reference**)
- **NEW** `@entities/tools/sevra-bench.md` — GitHub `rufimelo99/malicious-pr-bench`; HF `RedAI4Code/SEVRA`; no LICENSE on GitHub API
- **NEW** `@concepts/llm-code-review-agent-security.md` — merge-gate threat model + 15 framing classes
- **Brief** `briefs/2026-06-16_sevra-bench-pr-review-agent-eval.md` — pre-rollout eval checklist
- **Updated** `social-engineering`, `agent-runtime-guardrails`, `llm-vulnerability-discovery`, `mcp-security-posture`, `seclaw-agent-security-evaluation`, `ai-for-cybersecurity`, `npm-supply-chain-defense`, `seclaw-eval`, `index.md`
- **Phase-0** Reference — CONDITIONAL-GO after LICENSE; Docker Gitea lab only
- **PDF** → `raw-sources/arxiv-2606.13757-sevra-bench-social-engineering-review-agents.pdf`
- **Inbox cleared** — 1/1 file ingested

## [2026-06-17] ingest | IoAI — Internet of Agentic AI (2606.12835)

**Source**: `research to be indexed/arxiv-2606.12835-the-internet-of-agentic-ai-communication-coordin.pdf`

- **NEW** `@sources/arxiv-2606-12835-internet-of-agentic-ai-communication-coordination.md` (read, **Reference** — vision paper)
- **NEW** `@concepts/internet-of-agentic-ai-ioai.md` — IoAI architecture + Table 4 threat taxonomy mapped to K100/K114
- **Brief** `briefs/2026-06-17_ioai-threat-taxonomy-prod-mcp-handoff.md` → scp `cemini-prod:/opt/cemini/briefs/`
- **Brief** `briefs/2026-06-17_ccc-handoff-ioai-containment-matrix.md` → `@ccc-wiki/briefs/`
- **Phase-0 re-audit** SEVRA (`malicious-pr-bench`): LICENSE still null/404 — **Reference** unchanged
- **Phase-0 re-audit** GT-MCP: no public repo — **Reference** unchanged
- **Updated** `mcp-security-posture`, `agentic-containment-principles`, `agent-runtime-guardrails`, `ai-for-cybersecurity`, `trajectory-context-control`, `llm-code-review-agent-security`, `sevra-bench`, `arxiv-2606-13757`, `arxiv-2606-10322`, `index.md`
- **PDF** → `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.12835-the-internet-of-agentic-ai-communication-coordin.pdf`
- **Inbox cleared** — 1/1 file ingested

## [2026-06-18] ingest | EA compromise risk quantification (2606.19106)

**Source**: `research to be indexed/arxiv-2606.19106-quantifying-compromise-risk-in-exceptional-acces.pdf`

- **NEW** `@sources/arxiv-2606-19106-exceptional-access-compromise-risk-quantification.md` (read, **Reference** — decision-support framework)
- **NEW** `@concepts/exceptional-access-risk-quantification.md` — T-EA vs OTT-EA taxonomy + four-layer framework + practitioner checklist
- **Brief** `briefs/2026-06-18_ea-risk-framework-policy-handoff.md` — policy deliberation handoff (hands-on)
- **Phase-0** Zenodo 20554740 (CC-BY-4.0 repro scripts) — **Reference**; no prod deployment
- **Updated** `threat-intelligence`, `cyberwarfare`, `defense-in-depth`, `incident-response`, `ai-for-cybersecurity`, `index.md`
- **PDF** → `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.19106-quantifying-compromise-risk-in-exceptional-acces.pdf`
- **Inbox cleared** — 1/1 file ingested

## [2026-06-19] ingest | Over-privileged tool selection — TOOLPRIVBENCH (2606.20023)

**Source**: `research to be indexed/arxiv-2606.20023-when-lower-privileges-suffice-investigating-over.pdf`

- **NEW** `@sources/arxiv-2606-20023-over-privileged-tool-selection-toolprivbench.md` (read, **Reference**)
- **NEW** `@concepts/agent-least-privilege-tool-selection.md` — OPUR/PED framework + mitigation ladder
- **NEW** `@entities/tools/toolprivbench.md` — benchmark entity
- **Brief** `briefs/2026-06-19_toolprivbench-prod-mcp-eval-checklist.md` — hands-on prod-mcp eval harness
- **Phase-0** `AISafetyHub/agent-tool-selection-bias` — README MIT badge, gh api LICENSE null/404 — **Reference** until SPDX filed
- **Updated** `mcp-security-posture`, `agent-runtime-guardrails`, `agent-skill-injection`, `agentic-containment-principles`, `ai-for-cybersecurity`, `zero-trust`, `airguard`, `index.md`
- **PDF** → `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2606.20023-when-lower-privileges-suffice-investigating-over.pdf`
- **Inbox cleared** — 1/1 file ingested

## [2026-06-20] digest pass | Empty inbox — ECC, Skillgate, OpenClaw stub

**Inbox**: empty (0 PDFs; 2606.19106 + 2606.20023 dupes skipped overnight).

- **NEW** `@entities/tools/ecc.md` — Phase-0 **CONDITIONAL-GO** (`ecc-agentshield` npm MIT); full bundle Steal-from; typosquat warning at 218k★
- **NEW** `@entities/tools/skillgate.md` — Phase-0 **Reference** (Mitiga SaaS, skillgate.mitiga.ai)
- **NEW** `@sources/openreview-openclaw-real-world-safety-analysis.md` — unread-stub; manual OpenReview PDF fetch deferred
- **Brief** `briefs/2026-06-20_agent-config-scan-stack-phase0.md` — Skillgate vs SkillSpector vs AgentShield ladder
- **Updated** `mcp-security-posture`, `agent-skill-injection`, `agent-runtime-guardrails`, `nvidia-skillspector`, `defenseclaw`, `index.md`

## [2026-06-20] lint | Post-digest maintenance pass

- **516 pages** indexed; **0** bidirectional gaps; pre-existing cross-wiki dangling refs unchanged

## [2026-06-21] ingest | Probabilistic agent verification (2606.20510) + wireless tangential (2606.18734)

**Inbox**: 2/2 PDFs ingested + archived.

- **NEW** `@sources/arxiv-2606-20510-efficient-sound-probabilistic-verification-ai-agents.md` — Google DeepMind DRO + probabilistic Datalog; Phase-0 **Reference** (no public artifact)
- **NEW** `@concepts/agent-probabilistic-datalog-verification.md` — Layer-2 guardrail between ePCA and LLM-as-Judge
- **NEW** `@sources/arxiv-2606-18734-point-cloud-wireless-channel-prediction.md` — skimmed tangential RF digital-twin ref
- **Brief** `briefs/2026-06-21_probabilistic-agent-guardrail-dro-handoff.md` — prod-mcp noisy-classifier checklist
- **Updated** `agent-runtime-guardrails`, `mcp-security-posture`, `ai-for-cybersecurity`, `neuro-symbolic-auditable-reasoning`, `wireless-pentest`, `6g-cps-closed-loop-security`, `splunk` (CVE-2026-20253 digest stub), `arxiv-2605-29251`, `index.md`
- **Digest touch** — R1–R3 Splunk CVE-2026-20253 on `@entities/tools/splunk.md` `[NEEDS VERIFICATION 2026-06-21]`

**Archive**:
- `cemini-egress-fi:.../arxiv-2606.20510-2606-20510v1-efficient-and-sound-probabilistic-v.pdf`
- `cemini-egress-fi:.../arxiv-2606.18734-2606-18734v1-point-cloud-assistant-localized-sta.pdf`

## [2026-06-22] ingest | System prompt leakage + AREA (2606.18673)

**Inbox**: 1/1 PDF ingested + archived.

- **NEW** `@sources/arxiv-2606-18673-prompt-leaking-attacks-area.md` — 1,200-app measurement, attention drift, AREA; Phase-0 **Reference** (NESA-Lab/AREA, no LICENSE)
- **NEW** `@concepts/system-prompt-leakage.md` — LLM07 exfiltration vs injection
- **NEW** `@entities/tools/leakbench-area.md` — LeakBench + AREA entity
- **NEW** `@concepts/safeclawbench-staged-agent-security.md` — CCC K121 cross-wiki stub (bidirectional fix)
- **Brief** `briefs/2026-06-22_system-prompt-leak-redteam-checklist.md`
- **Updated** `agent-runtime-guardrails`, `mcp-security-posture`, `ai-for-cybersecurity`, `llm-adversarial-fuzzing`, `llm-defense-lattice`, `agent-skill-injection`, `responsible-disclosure`, `arxiv-2606-02822`, `seclaw-agent-security-evaluation`, `defenseclaw`, `index.md`

**Archive**: `cemini-egress-fi:.../arxiv-2606.18673-understanding-and-mitigating-prompt-leaking-atta.pdf`

## [2026-06-23] ingest | 5-paper batch — OSINT LoC, DEFENGRAPH, guard calibration, CITADEL, self-evolution

**Inbox**: 5/5 PDFs ingested + archived.

- **NEW** `@sources/arxiv-2606-20610-osint-ai-loss-of-control-detection.md` + `@concepts/ai-loss-of-control-osint-monitoring.md` — OSINT/CTI for AI loss of control (Reference)
- **NEW** `@sources/arxiv-2606-21059-defengraph-knowledge-graph-blue-team.md` + `@entities/tools/defengraph.md` — KG+RAG SOC assistant (Reference, no repo)
- **NEW** `@sources/arxiv-2606-22659-confidently-wrong-prompt-injection-calibration.md` + `@concepts/prompt-injection-detector-calibration.md` + `@entities/tools/picalib-research.md` — severity S metric (Reference)
- **NEW** `@sources/arxiv-2606-22939-citadel-csi-jamming-iiot.md` — IIoT jamming stub (skimmed)
- **NEW** `@sources/arxiv-2606-23075-self-evolving-llm-agent-safety-mlas.md` + `@concepts/self-evolving-agent-security.md` — MLAS matrix + OpenClaw/Hermes case studies
- **Briefs** `2026-06-23_prompt-guard-severity-calibration-handoff.md`, `2026-06-23_self-evolving-agent-assessment-checklist.md`, `2026-06-23_ai-loc-osint-monitoring-handoff.md`
- **Updated** `agent-runtime-guardrails`, `mcp-security-posture`, `agentic-containment-principles`, `osint-for-cybersecurity`, `threat-intelligence`, `incident-response`, `soc-operations`, `siem`, `ai-for-cybersecurity`, `llm-adversarial-fuzzing`, `llm-defense-lattice`, `safeclawbench-staged-agent-security`, `openreview-openclaw-real-world-safety-analysis`, `network-security`, `index.md`

**Archive**: 5 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/cybersec/`

## [2026-06-24] ingest | 6-paper batch — Tool-Guard, CLAWAUDIT, ARENA, PORTICO, IGAC (+ legal routed)

**Inbox**: 5/6 cybersecurity PDFs ingested + archived; 1 off-topic legal AI PDF archived only.

- **NEW** `@sources/arxiv-2606-20922-tool-guard-isolated-planning-tool-description-poisoning.md` + `@concepts/cross-tool-description-poisoning.md` + `@entities/tools/tool-guard.md` — cross-tool metadata poisoning; Phase-0 **CONDITIONAL-GO** (MIT)
- **NEW** `@sources/arxiv-2606-21071-clawaudit-local-agent-runtime-audit.md` + `@concepts/local-agent-runtime-audit.md` + `@entities/tools/clawaudit.md` — OpenClaw runtime static audit; Phase-0 **CONDITIONAL-GO** (no LICENSE)
- **NEW** `@sources/arxiv-2606-21377-arena-autonomous-defense-transferability.md` + `@concepts/autonomous-defense-agent-transferability.md` — SOC agent transferability gap; **Reference**
- **NEW** `@sources/arxiv-2606-22504-portico-lingering-authority-coding-agents.md` + `@concepts/lingering-authority-revocable-capabilities.md` — revocable planner capabilities; **Reference**
- **NEW** `@sources/arxiv-2606-22916-intent-governed-tool-authorization-igac.md` + `@concepts/intent-governed-tool-authorization.md` — IGAC intent certificates; **Reference**
- **Skipped wiki** `arxiv-2606.23913` legal AI formal verification — off-topic; archived to egress only
- **Briefs** `2026-06-24_tool-guard-*`, `clawaudit-*`, `portico-*`, `igac-*`, `arena-*`, `ccc-handoff-agent-security-ingest-batch.md`
- **Updated** `mcp-security-posture`, `agent-runtime-guardrails`, `agent-skill-injection`, `agent-least-privilege-tool-selection`, `soc-operations`, `ai-for-cybersecurity`, `openreview-openclaw-real-world-safety-analysis`, `defenseclaw`, `index.md`
- **Inbox cleared** — 6/6 files archived

## [2026-06-25] ingest | Agentic red-team security audit (2606.24496)

**Inbox**: 1/1 PDF ingested + archived.

- **NEW** `@sources/arxiv-2606-24496-red-teaming-the-agentic-red-team.md` + `@concepts/agentic-offensive-security-kill-chain.md` — agent-phishing + worker/orchestrator kill chain (Reference meta-audit)
- **Briefs** `2026-06-25_agentic-red-team-secure-architecture-handoff.md`, `2026-06-25_agent-phishing-tier2-eval-checklist.md`
- **Brief audit** — 38 wiki `briefs/` refs; 37 on disk; 1 missing (`2026-05-31_prod-mcp-allowlist-draft-k100-from-cybersec.md`, log-only OSINT mirror — not wiki-linked)
- **Updated** `llm-pentest-automation`, `agent-runtime-guardrails`, `red-team-operations`, `agent-vm-sandboxing`, `ai-for-cybersecurity`, `mcp-security-posture`, `airecon`, `index.md`
- **Phase-0** Cracken paper Reference; AIRecon flagged CONDITIONAL-GO pending docker cap re-audit

**Archive**: `cemini-egress-fi:.../arxiv-2606.24496-red-teaming-the-agentic-red-team.pdf`

## [2026-06-26] ingest | ShareLock MCP + ToxSearch-S (2606.27027 + 2606.24166)

**Inbox**: 2/2 PDFs ingested + archived.

- **NEW** `@sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md` + `@concepts/multi-tool-threshold-mcp-poisoning.md` — Shamir multi-tool MCP threshold poisoning; Phase-0 **Reference** (no artifact)
- **NEW** `@sources/arxiv-2606-24166-toxsearch-s-distributed-toxicity-search.md` — speciated QD toxicity search + MPI; Phase-0 **Reference**
- **Briefs** `2026-06-26_sharelock-multi-tool-threshold-mcp-redteam-checklist.md`, `2026-06-26_toxsearch-s-adversarial-fuzzing-handoff.md`
- **CCC brief** `2026-06-26_ccc-handoff-sharelock-toxicity-ingest.md`
- **Updated** `mcp-security-posture`, `cross-tool-description-poisoning`, `agent-runtime-guardrails`, `agent-skill-injection`, `llm-adversarial-fuzzing`, `ai-for-cybersecurity`, `red-team-operations`, `responsible-disclosure`, `fuzzyai`, `tool-guard`, `index.md`
- **Inbox cleared** — 2/2 files archived

**Archive**:
- `cemini-egress-fi:.../arxiv-2606.27027-sharelock-a-stealthy-multi-tool-threshold-poison.pdf`
- `cemini-egress-fi:.../arxiv-2606.24166-2606-24166v1-distributed-quality-diversity-searc.pdf`

## [2026-06-27] ingest | AOHP + ToolBench-X + CraaS (2606.23449 + 2606.25819 + 2606.24226)

**Inbox**: 3/3 PDFs ingested + archived.

- **NEW** `@sources/arxiv-2606-23449-aohp-os-level-agent-harness.md` + `@entities/tools/aohp.md` — AOSP agent-native OS harness; Phase-0 **CONDITIONAL-GO** (Apache-2.0, ~93★)
- **NEW** `@sources/arxiv-2606-25819-toolbench-x-tool-environment-unreliability.md` + `@concepts/tool-environment-unreliability-eval.md` + `@entities/tools/toolbench-x.md` — tool P_h unreliability benchmark; Phase-0 **Reference** (no LICENSE, release pending)
- **NEW** `@sources/arxiv-2606-24226-crypter-as-a-service-exploit-in.md` + `@concepts/crypter-as-a-service.md` — exploit.in CraaS ecosystem; Phase-0 **Reference**
- **Briefs** `2026-06-27_aohp-agent-native-os-harness-handoff.md`, `2026-06-27_toolbench-x-prod-mcp-reliability-eval-checklist.md`, `2026-06-27_craas-exploit-in-threat-intel-handoff.md`
- **CCC brief** `2026-06-27_ccc-handoff-aohp-toolbench-craas-ingest.md`
- **Updated** `agent-runtime-guardrails`, `agent-vm-sandboxing`, `mcp-security-posture`, `seclaw-agent-security-evaluation`, `llm-pentest-automation`, `av-edr-bypass`, `threat-intelligence`, `osint-for-cybersecurity`, `mobile-pentest`, `ai-for-cybersecurity`, `index.md`
- **Inbox cleared** — 3/3 files archived

**Archive**:
- `cemini-egress-fi:.../arxiv-2606.23449-2606-23449v1-aohp-an-open-source-os-level-agent.pdf`
- `cemini-egress-fi:.../arxiv-2606.25819-2606-25819v1-beyond-function-calling-benchmarkin.pdf`
- `cemini-egress-fi:.../arxiv-2606.24226-2606-24226v1-inside-crypter-as-a-service-an-ecos.pdf`

## [2026-06-27] lint | Brief audit + backlink fill

- **Brief audit** — 45 wiki `briefs/` refs; 44 on disk; 1 missing (`2026-05-31_prod-mcp-allowlist-draft-k100-from-cybersec.md`, log-only OSINT mirror — not wiki-linked)
- **NEW** `@entities/tools/reverse-skill.md` — K129 Adopt stub (primary home; OSINT cross-route)
- **Filled** brief backlinks on `aohp`, `toolbench-x`, `agent-vm-sandboxing`, `agent-least-privilege-tool-selection`, `sevra-bench`, `llm-code-review-agent-security`, `mobile-pentest`, `llm-pentest-automation`, `offensive-claude`, `claude-red-offensive-skills`

## [2026-06-30] ingest | No new PDFs — brief audit + sweep

**Inbox**: 0/0 — overnight digest fetched 0 PDFs (dupes + non-arXiv only).

- **Brief audit** — 48 wiki `briefs/` refs; 44 on disk; 1 missing (`2026-05-31_prod-mcp-allowlist-draft-k100-from-cybersec.md`, log-only OSINT mirror)
- **Filled** brief backlinks: `defenseclaw`, `seclaw-agent-security-evaluation`, `agent-execution-provenance` (K125 MemClaw), `mcp-security-posture` (CCC batch index)
- **Sweep** `wiki/sweeps/2026-06-30-daily.md` committed

## [2026-07-01] ingest | AI-Infra-Guard technical report (2606.31227)

**Inbox**: 1/1 PDF ingested + archived (digest pick R7 — overnight inbox was empty).

- **NEW** `@sources/arxiv-2606-31227-ai-infra-guard-technical-report.md` + `@concepts/layer-paradigm-agent-red-teaming.md`
- **Updated** `@entities/tools/ai-infra-guard.md` — technical report M1–M4, ~4,018★ refresh; Phase-0 **CONDITIONAL-GO** (external Docker)
- **Briefs** `2026-07-01_ai-infra-guard-layer-paradigm-red-team-handoff.md`, `2026-07-01_ai-infra-guard-external-scanner-lab-checklist.md`
- **CCC brief** `2026-07-01_ccc-handoff-ai-infra-guard-technical-report-ingest.md`
- **Updated** `mcp-security-posture`, `agent-skill-injection`, `llm-pentest-automation`, `local-agent-runtime-audit`, `index.md`
- **Sweep** `wiki/sweeps/2026-07-01-daily.md` committed

**Archive**:
- `cemini-egress-fi:.../arxiv-2606.31227-ai-infra-guard-technical-report.pdf`

## [2026-07-02] ingest | Robust-TO confidence-aware tool orchestration (2606.26904)

**Inbox**: 1/1 PDF ingested + archived.

- **NEW** `@sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md` + `@concepts/confidence-aware-tool-orchestration.md` — Blind Trust Problem + (result, confidence) pattern; Phase-0 **Reference** (no code repo)
- **Briefs** `2026-07-02_robust-to-confidence-aware-tool-routing-handoff.md`, `2026-07-02_prod-mcp-tool-confidence-contract-checklist.md`
- **CCC brief** `2026-07-02_ccc-handoff-robust-to-confidence-orchestration-ingest.md`
- **Updated** `tool-environment-unreliability-eval`, `agent-runtime-guardrails`, `llm-pentest-automation`, `seclaw-agent-security-evaluation`, `mcp-security-posture`, `ai-for-cybersecurity`, `index.md`
- **Sweep** `wiki/sweeps/2026-07-02-daily.md` committed

**Archive**:
- `cemini-egress-fi:.../arxiv-2606.26904-confidence-aware-tool-orchestration-robust-to.pdf`

## [2026-07-03] ingest | Cognitive heuristics in LLM vuln detection (2606.30587)

**Inbox**: 1/1 PDF ingested + archived.

- **NEW** `@sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md` + `@concepts/cognitive-heuristics-llm-vuln-detection.md` — halo/framing/anchoring; 97% suppression PoC; Phase-0 **Reference**
- **Briefs** `2026-07-03_cognitive-heuristics-llm-scanner-redteam-checklist.md`, `2026-07-03_ci-merge-gate-cognitive-context-hardening-handoff.md`
- **CCC brief** `2026-07-03_ccc-handoff-cognitive-heuristics-vuln-detection-ingest.md`
- **Updated** `llm-code-review-agent-security`, `llm-vulnerability-discovery`, `social-engineering`, `ai-for-cybersecurity`, `agent-runtime-guardrails`, `sevra-bench`, `defending-code-reference-harness`, `arxiv-2606-13757`, `index.md`
- **Sweep** `wiki/sweeps/2026-07-03-daily.md` committed

**Archive**:
- `cemini-egress-fi:.../arxiv-2606.30587-words-speak-louder-cognitive-heuristics-llm-vuln-detection.pdf`

## [2026-07-03] lint | Brief audit + backlink fill

**Inbox**: 0/0 — no new PDFs.

- **Brief audit** — 54 wiki `briefs/` refs; 67 on disk; 1 missing (`2026-05-31_prod-mcp-allowlist-draft-k100-from-cybersec.md`, log-only OSINT mirror)
- **Filled** brief backlinks: `llm-code-review-agent-security`, `sevra-bench`, `layer-paradigm-agent-red-teaming`, `defending-code-reference-harness`, `llm-vulnerability-discovery`, `tool-environment-unreliability-eval`

## [2026-07-04] ingest | HCP MCP execution-control invariants (2606.29073)

**Inbox**: 1/1 PDF ingested + archived.

- **NEW** `@sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md` + `@concepts/mcp-execution-control-invariants.md` + `@entities/tools/handle-capability-protocol.md` — eight invariants I1–I8; B0 10/10, B1 6/10, B2 0/10 attacks; Phase-0 **CONDITIONAL-GO** (MIT, 0★)
- **Briefs** `2026-07-04_hcp-mcp-execution-control-handoff.md`, `2026-07-04_prod-mcp-eight-invariants-checklist.md`
- **CCC brief** `2026-07-04_ccc-handoff-hcp-execution-control-ingest.md`
- **Updated** `mcp-security-posture`, `agent-runtime-guardrails`, `agent-execution-provenance`, `intent-governed-tool-authorization`, `cross-tool-description-poisoning`, `agent-least-privilege-tool-selection`, `ai-for-cybersecurity`, `chaincaps`, `airguard`, `index.md`
- **Sweep** `wiki/sweeps/2026-07-04-daily.md` committed

**Archive**:
- `cemini-egress-fi:.../arxiv-2606.29073-hcp-mcp-execution-control-invariants.pdf`

## [2026-07-07] ingest | Steerability via constraints — coding-agent oversight (2607.02389)

**Inbox**: 1/1 PDF ingested + archived.

- **NEW** `@sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md` + `@concepts/substrate-constraints-coding-agent-oversight.md` — substrate + docs CLI; reviewer recall **54.5% → 90.9%**; Phase-0 **Reference**
- **Briefs** `2026-07-07_steerability-substrate-coding-agent-oversight-handoff.md`, `2026-07-07_harness-substrate-constraints-checklist.md` (David adoption → `tipdrop-workspace-kit/briefs/2026-07-07_k138-substrate-constraints-agent-oversight-adopt.md`)
- **CCC brief** `2026-07-07_ccc-handoff-steerability-substrate-ingest.md` + CCC concept stub
- **Updated** `agent-runtime-guardrails`, `mcp-security-posture`, `llm-code-review-agent-security`, `local-agent-runtime-audit`, `agent-vm-sandboxing`, `ai-for-cybersecurity`, `neuro-symbolic-auditable-reasoning`, `seclaw-agent-security-evaluation`, `defending-code-reference-harness`, `index.md`
- **Sweep** `wiki/sweeps/2026-07-07-daily.md` committed

**Archive**:
- `cemini-egress-fi:.../arxiv-2607.02389-steerability-constraints-coding-agent-oversight.pdf`

## [2026-07-05] cross-wiki route | tl;dr sec — [tl;dr sec] #335 - Prompt Injection as Role Confusion, PHP Ecosystem Security, New MCP Spec

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-tldrsec-2026-07-02-tldr-sec-335---prompt-injection-as-role-confusio.md`.
- Created wiki/sources/newsletter-rss-tldrsec-2026-07-02-tldr-sec-335---prompt-injection-as-role-confusio.md (stub)

## [2026-07-05] cross-wiki route | Packt SecPro — Identity Became the New Perimeter

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-secpro-2026-07-03-identity-became-the-new-perimeter.md`.
- Created wiki/sources/substack-rss-secpro-2026-07-03-identity-became-the-new-perimeter.md (stub)

## [2026-07-07] cross-wiki route | The Engineering Club — Security Edition — How I’d Respond in the First Hour After a Package I Use Got Hacked

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-seceng-weekly-2026-07-06-how-id-respond-in-the-first-hour-after-a-package.md`.
- Created wiki/sources/substack-rss-seceng-weekly-2026-07-06-how-id-respond-in-the-first-hour-after-a-package.md (stub)

## [2026-07-07] ingest | HexStrike-AI security-tool orchestration study (2607.02873)

Cross-wiki ingest from CCC full-ingest batch (K140). arXiv 2607.02873 (USTC) — 774 picoCTF trials over HexStrike-AI (150+ tools/MCP).
- Created `sources/arxiv-2607-02873-hexstrike-security-tool-orchestration.md`, `concepts/security-tool-orchestration-determinants.md`, `briefs/2026-07-07_hexstrike-client-first-order-orchestration-checklist.md`.
- Key finding: **driving client is first-order** (2.1× gap, same model); solve 55.4%→72.0% via tool/agent fixes; residual failures reasoning-bound not missing-tool.
- Verdict **REFERENCE** — eval methodology + least-privilege corroboration; HexStrike-AI MIT (lab-only).
- Cross-wiki: `@ccc-wiki/concepts/client-as-first-order-harness-factor.md` (bidirectional).

## [2026-07-10] ingest | CAGE-1 + PolyWorkBench (2607.03510, 2607.06008)

**Inbox**: 2/2 PDFs ingested + archived.

- **NEW** `@sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md` + `@concepts/cage-1-enterprise-agent-governance-eval.md` — Prebind Assurance + 12-dimension enterprise eval; Phase-0 **Reference**
- **NEW** `@sources/arxiv-2607-06008-polyworkbench-multilingual-long-horizon.md` + `@concepts/multilingual-long-horizon-agent-evaluation.md` + `@entities/platforms/polyworkbench.md` — 67-task multilingual benchmark; harness disclosure; Phase-0 **Reference**
- **Briefs** `2026-07-10_cage-1-prebind-assurance-handoff.md`, `2026-07-10_prod-mcp-prebind-assurance-checklist.md`, `2026-07-10_polyworkbench-multilingual-eval-handoff.md`, K151/K152 prod briefs
- **David (tipdrop)** `2026-07-10_k151-prebind-assurance-adopt.md`
- **CCC brief** `2026-07-10_ccc-handoff-cage-polyworkbench-ingest.md`
- **Updated** `mcp-execution-control-invariants`, `agent-runtime-guardrails`, `agent-execution-provenance`, `intent-governed-tool-authorization`, `agentic-containment-principles`, `mcp-security-posture`, `seclaw-agent-security-evaluation`, `security-tool-orchestration-determinants`, `ai-for-cybersecurity`, `agent-data-injection-attacks`, `index.md`
- **Sweep** `wiki/sweeps/2026-07-10-daily.md` committed

**Archive**:
- `cemini-egress-fi:.../arxiv-2607.03510-2607-03510v1-cage-1-control-assurance-and-govern.pdf`
- `cemini-egress-fi:.../arxiv-2607.06008-2607-06008v1-polyworkbench-benchmarking-multilin.pdf`

## [2026-07-09] ingest | ADI + SpellSmith MCP taint (2607.05120, 2607.07461)

**Inbox**: 2/2 PDFs ingested + archived.

- **NEW** `@sources/arxiv-2607-05120-agent-data-injection-attacks.md` + `@concepts/agent-data-injection-attacks.md` — ADI trusted/untrusted isolation; **50%** ASR vs **<1%** II on guardrails; Phase-0 **CONDITIONAL-GO** (`compsec-snu/adi`)
- **NEW** `@sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md` + `@concepts/mcp-taint-style-vulnerabilities.md` + `@entities/tools/spellsmith.md` — **81.13%** MCP vulns taint-style; SpellSmith **0.13%** case ASR; Phase-0 **Reference**
- **Briefs** `2026-07-09_adi-trusted-untrusted-data-handoff.md`, `2026-07-09_prod-mcp-trusted-untrusted-data-isolation-checklist.md`, `2026-07-09_spellsmith-mcp-taint-mitigation-handoff.md`
- **David (tipdrop)** `2026-07-09_k139-agent-data-injection-harness-adopt.md`
- **CCC brief** `2026-07-09_ccc-handoff-adi-spellsmith-ingest.md`
- **Updated** `mcp-security-posture`, `agent-runtime-guardrails`, `mcp-execution-control-invariants`, `cross-tool-description-poisoning`, `llm-code-review-agent-security`, `ai-for-cybersecurity`, `agent-execution-provenance`, `index.md`
- **Sweep** `wiki/sweeps/2026-07-09-daily.md` committed

**Archive**:
- `cemini-egress-fi:.../arxiv-2607.05120-agent-data-injection-attacks.pdf`
- `cemini-egress-fi:.../arxiv-2607.07461-spellsmith-mcp-taint-style-vulnerabilities.pdf`

## [2026-07-08] cross-wiki | K149 cyber

- CyberChef context brief

## [2026-07-15] cross-wiki route | Firewall3D: Hardware Firewall for Defending 3D Printers Against Firmware Attacks

Cross-wiki stub routed from `@3d-printing-wiki/sources/2026-asgar-firewall3d-firmware-hardware.md`.
- Created wiki/sources/2026-asgar-firewall3d-firmware-hardware.md (stub)

## [2026-07-16] ingest | AMT-X + AHA + SkillSec + GFlowRL (K175–K178)

**Inbox**: 6 PDFs (5 digest + 1 manual fetch 2607.13987); 4 core ingested; 2 OOD brief-only.

- **NEW** `@sources/arxiv-2607-11151-amt-x-phase-structured-multi-turn-red-teaming.md` + `@concepts/amt-x-phase-structured-multi-turn-red-teaming.md` — dual overall/full ASR; Phase-0 **REFERENCE**
- **NEW** `@sources/arxiv-2607-11698-agent-hacks-agent-autoresearch.md` + `@concepts/vulnerability-concept-graph-production-agent-red-teaming.md` + `@entities/tools/aha-auto-research-red-teaming.md` — VCG; Phase-0 **CONDITIONAL-GO**; local clone `raw-sources/repos/Auto-research-red-teaming` (~169MB)
- **NEW** `@sources/arxiv-2607-13987-agent-skill-security-skillsec-eval.md` + `@concepts/skillsec-lifecycle-agent-skill-security.md` — 5-stage lifecycle; Phase-0 **REFERENCE**
- **NEW** `@sources/arxiv-2607-13394-gflowrl-distribution-matching-rl.md` + `@concepts/gflowrl-distribution-matching-attacker-rl.md` — attacker-diversity slice; Phase-0 **NO-GO** (repo 404)
- **OOD** PAT translation (2607.14040) + Deep Interaction (2607.14049) — `briefs/2026-07-16_ood-pat-translation-deep-interaction-route.md` (no source stubs)
- **Briefs** K175–K178 handoffs + prod; CCC handoff; David tipdrop K176/K177; poker K176 light steal
- **Updated** crescendo, pair, llm-adversarial-fuzzing, agent-skill-injection, layer-paradigm, seclaw, cage-1, ADI, ai-for-cybersecurity, fuzzyai, malskillbench, index.md
- **Sweeps** `wiki/sweeps/2026-07-11-daily.md` … `2026-07-16-daily.md` present (uncommitted until user asks)

**Archive**:
- `cemini-egress-fi:.../arxiv-2607.11151-amt-x-phase-structured-multi-turn-red-teaming-wi.pdf`
- `cemini-egress-fi:.../arxiv-2607.11698-agent-hacks-agent-autoresearch-for-production-ag.pdf`
- `cemini-egress-fi:.../arxiv-2607.13394-gflowrl-scaling-distribution-matching-rl-to-larg.pdf`
- `cemini-egress-fi:.../arxiv-2607.13987-agent-skill-security-threat-models-attacks-defenses.pdf`
- `cemini-egress-fi:.../arxiv-2607.14040-can-an-old-dog-be-taught-new-tricks-taking-llms.pdf`
- `cemini-egress-fi:.../arxiv-2607.14049-deep-interaction-an-efficient-human-ai-interacti.pdf`

## [2026-07-17] ingest | DataShield + PRISM + hard-example synthesis + self-consistency (K184–K187)

**Inbox**: 5 digest PDFs; 4 core ingested; 1 OOD brief-only (wireless localization).

- **NEW** `@sources/arxiv-2607-15081-datashield-risky-finetune-data.md` + `@concepts/datashield-risky-finetune-data-filtering.md` + `@entities/tools/datashield.md` — consensus subspace FT filter; Phase-0 **CONDITIONAL-GO**; local clone ~3MB
- **NEW** `@sources/arxiv-2607-15218-prism-physical-vs-content-danger.md` + `@concepts/physical-vs-content-danger-embodied-agents.md` — CD vs PD; Phase-0 **REFERENCE**
- **NEW** `@sources/arxiv-2607-14256-agentic-hard-example-synthesis.md` + `@concepts/agentic-hard-example-synthesis-content-safety.md` — FNR 41.2→24.5%; Phase-0 **REFERENCE**
- **NEW** `@sources/arxiv-2607-15277-partition-prompt-aggregate-self-consistency.md` + `@concepts/llm-statistical-self-consistency-macro-fallacy.md` — macro fallacy; CCC primary
- **OOD** 2607.14938 wireless localization — `briefs/2026-07-17_ood-wireless-localization-survey-route.md`
- **Briefs** K184–K187 handoffs + prod; CCC handoff; David K184/K185; poker K185
- **Updated** llm-adversarial-fuzzing, agent-runtime-guardrails, cage-1, VCG, AMT-X, crescendo, self-evolving-agent-security, ai-for-cybersecurity, index.md
- **Sweep** `wiki/sweeps/2026-07-17-daily.md`

**Archive**:
- `cemini-egress-fi:.../arxiv-2607.14256-…pdf`
- `cemini-egress-fi:.../arxiv-2607.14938-…pdf`
- `cemini-egress-fi:.../arxiv-2607.15081-…pdf`
- `cemini-egress-fi:.../arxiv-2607.15218-…pdf`
- `cemini-egress-fi:.../arxiv-2607.15277-…pdf`

## [2026-07-18] ingest | install-gap deepen + ARMOR++ (K188) + wireless OOD

**Inbox**: 5 PDFs (3 wireless digest OOD; 2 deepen/manual — 2607.15143, 2607.15246).

- **DEEPEN** `@sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md` + `@concepts/coding-agent-supply-chain-install-gap.md` — harness×model; Sentinel **404**; reinforces CCC **K179** ADOPT (no new K)
- **NEW** `@sources/arxiv-armor-plusplus-deepfake-agentic-2607.15246.md` + `@concepts/armor-plusplus-agentic-deepfake-detector-attacks.md` — AADD-LQ ViT ASR 0.443; Phase-0 **REFERENCE** (**K188**); no local adopt (weights >500MB)
- **OOD** 2607.14775 OFDM-ISAC + 2607.14778 UAV sensing + 2607.14938 localization — `briefs/2026-07-18_ood-wireless-isac-uav-sensing-route.md`
- **ROUTE** `@sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md` + `@concepts/mcp-security-evidence-grounded-detection.md` — CCC **K189** primary; cybersec REFERENCE stub
- **Briefs** install-gap + ARMOR handoffs; prod K188; CCC handoff; David Sentinel-404 reinforce; poker K179 light steal
- **Updated** npm-supply-chain, cage-1, agent-runtime-guardrails, skillsec, llm-code-review, VCG, llm-adversarial-fuzzing, ai-for-cybersecurity, agentic-hard-example, index.md; CCC backlinks
- **Local adopts**: none this batch
- **Sweep** `wiki/sweeps/2026-07-18-daily.md`

**Archive**:
- `cemini-egress-fi:.../arxiv-2607.14775-…pdf`
- `cemini-egress-fi:.../arxiv-2607.14778-…pdf`
- `cemini-egress-fi:.../arxiv-2607.14938-…pdf` (re-archive ok)
- `cemini-egress-fi:.../arxiv-2607.15143-…pdf`
- `cemini-egress-fi:.../arxiv-2607.15246-…pdf`

## [2026-07-18] adoption | CONDITIONAL-GO / Adopt local clones + CLIs (<500MB)

Cleared the Phase-0 local-adoption backlog for tools with public repos under the space budget. `raw-sources/repos/` now **~305MB** total (gitignored).

**Shallow clones added:** Tool-Guard, handle-capability-protocol, ClawAudit (no LICENSE — methodology only), defending-code-reference-harness, pentest-ai, pentest-ai-agents, cve-mcp-server, netviz, reverse-skill, SkillSpector, adi, FuzzyAI, iron-proxy, cryptex-oss, AIRGuard, agentshield.

**CLIs installed:** `skillspector` v2.3.13 (`uv tool`), `agentshield` via `ecc-agentshield@1.4.0` npm (`~/.local/bin/agentshield`).

**Skipped (not needed / out of policy):** Sentinel 404; ARMOR++/FlowGuard/SpellSmith no public code; AOHP AOSP-lab; cua ~269MB (would blow headroom vs AHA already at 169MB); AI-Infra-Guard source vendor-poison (external Docker only); GFlowRL 404.

**Updated** entity pages with Local clone/adoption stamps + `@concepts/agent-data-injection-attacks.md`.

## [2026-07-18] adoption | raise cap + actually use adopted tools

- **Cap:** soft ~2GB for `raw-sources/repos/` (was informal 500MB/tool) so GO tools are not skipped
- **NEW clones:** `cua` (~387MB), `defenseclaw` (~704MB) + isolated `raw-sources/defenseclaw-home`
- **Fixed:** dead `defenseclaw` symlink (`/tmp/...`); CLI + `skill-scanner` / `mcp-scanner` restored to `~/.local/bin`
- **NEW** `scripts/adopted_security_preflight.sh` — agent runs skillspector + agentshield + skill-scanner
- **Ran preflight:** federation skills SAFE/LOW; `~/.claude` agentshield medium (marketplace deny-list gaps); reverse-skill pack CRITICAL as wholesale install
- **Schema:** `CLAUDE.md` Phase-0 §7–8 + session ritual §2 (adopt ⇒ use)
- **Brief:** `briefs/2026-07-18_adopted-tools-use-it-checklist.md` (you vs agent)
- **Still USER:** Lume/cua VM; optional Codex sidecar; review ~/.claude marketplace plugin

## [2026-07-18] ops | federation Cursor security preflight

- Canon: `CCC/scripts/cursor_security_preflight_federation.sh` → `~/.local/bin/cursor-security-preflight`
- Cybersec wrapper `scripts/adopted_security_preflight.sh` now defaults to **all** workspaces
- Rule synced to all federation `.cursor/rules/` + `~/.cursor/rules/` via `sync_federation_cursor_skills.sh`
- Ran `--quick` across 20 roots (41 scan units). Note: federation `super-audit` skill scores CRITICAL under SkillSpector static (dual-use audit content) — expected; do not treat as malware install

## [2026-07-19] ingest | wireless OOD re-drop (digest) + query tighten

**Inbox**: same 3 PDFs as 2026-07-18 OOD (digest re-fetch; arXiv IDs were not stubbed so skip-dup missed).

- **OOD stubs** (block future re-fetch): `@sources/arxiv-ood-wireless-ofdm-isac-2607.14775.md`, `@sources/arxiv-ood-wireless-uav-sensing-2607.14778.md`, `@sources/arxiv-ood-wireless-localization-survey-2607.14938.md`
- **Brief** `briefs/2026-07-19_ood-wireless-isac-uav-sensing-route.md`
- **Config** tightened `daily_research_config.yaml` wireless `arxiv_query` (Wi-Fi/WPA/BLE/evil-twin; ANDNOT ISAC/localization/OFDM)
- **No** Phase-0 / David / poker / prod / local adopt
- **Sweep** `wiki/sweeps/2026-07-19-daily.md`

**Archive**: re-verified on egress; local inbox cleared.

## [2026-07-20] ingest | daily digest 5 arXiv (CAV-STIX + CRAFT + IO-Link + competencies + EvoOMG OOD)

**Inbox**: 5 PDFs from `wiki/sweeps/2026-07-20-daily.md` (all NEW).

- **OOD** 2607.07045 EvoOMG Wi-Fi MLO MAC RL — stub `@sources/arxiv-ood-wireless-evoomg-mlo-2607.07045.md`; brief `briefs/2026-07-20_ood-wireless-evoomg-mlo-route.md`; wireless `arxiv_query` ANDNOT MLO/EDCA/goodput/MADDPG
- **NEW** `@sources/arxiv-2607-15840-io-link-wireless-pren-50742.md` + `@concepts/industrial-safety-security-convergence.md` — prEN 50742; IOLW 8→2; REFERENCE
- **NEW** `@sources/arxiv-2607-16083-llm-research-competencies.md` + `@concepts/llm-research-competency-model.md` — Zenodo CC-BY pack **adopted** `raw-sources/repos/llm-research-competencies-zenodo` (~396KB)
- **NEW** `@sources/arxiv-2607-16122-craft-rubric-capability-diagnosis.md` + `@concepts/rubric-capability-tree-diagnosis.md` — **K195** REFERENCE (no code)
- **NEW** `@sources/arxiv-2607-16175-cav-stixgen-open-weight-stix.md` + `@concepts/llm-cve-to-stix-generation.md` + `@entities/tools/cav-stixgen.md` — **K196** REFERENCE (figshare WAF/unverified license)
- **Updated** threat-intelligence, mitre-attack, network-security, wireless-pentest, ai-for-cybersecurity, datashield concept, autosut, index.md
- **Briefs**: OOD + OT handoff + competencies handoff; prod K195/K196 → `cemini-prod:/opt/cemini/briefs/`; CCC handoffs; poker K195 steal + K196 no-fit
- **David / TipDrop**: skipped (no image/persona install path)
- **Phase-0**: `scripts/adopt_k195_k196_phase0.sh` PASS
- **Local adopts**: Zenodo pack only (<500MB). No CAV-STIX clone.
- **Sweep**: `wiki/sweeps/2026-07-20-daily.md`

**Archive** (egress-fi cybersec/):
- `arxiv-2607.07045-…pdf`
- `arxiv-2607.15840-…pdf`
- `arxiv-2607.16083-…pdf`
- `arxiv-2607.16122-…pdf`
- `arxiv-2607.16175-…pdf`

## [2026-07-21] ingest | daily digest 5 arXiv (A-MESS, BioBreaker, smart-grid, SWE-Pruner, EoBench)

**Inbox**: 5 PDFs from `wiki/sweeps/2026-07-21-daily.md` (all NEW).

- **NEW** `@sources/arxiv-2607-17152-a-mess-defender-centric-jailbreak.md` + `@concepts/defender-centric-jailbreak-utility.md` — **K197** REFERENCE
- **NEW** `@sources/arxiv-2607-18056-intern-biobreaker-biosecurity.md` + `@concepts/llm-biosecurity-red-teaming.md` — **K198** REFERENCE (no operational bio content)
- **NEW** `@sources/arxiv-2607-18147-llms-agents-smart-grids-tutorial.md` + `@concepts/solver-grounded-agentic-ot.md` + `@entities/tools/llms-agents-smartgrids-code.md` — **K199** REFERENCE (NO LICENSE)
- **NEW** `@sources/arxiv-2607-18213-swe-pruner-pro.md` + `@concepts/coding-agent-context-pruning.md` + `@entities/tools/swe-pruner-pro.md` — **K200** CONDITIONAL-GO; local clone ~8.7MB
- **NEW** `@sources/arxiv-2607-18232-eobench-expressions-of-belief.md` + `@concepts/llm-belief-expression-robustness.md` — REFERENCE (EoB unlicensed)
- **Updated** llm-adversarial-fuzzing, crescendo, pair, datashield, ai-for-cybersecurity, responsible-disclosure, network-security, 6g-cps, industrial-safety, social-engineering, index.md
- **Briefs**: K197–K200 → prod; CCC handoff; poker K197/K200 steal + K198/K199 no-fit
- **David / TipDrop**: skipped (no persona/image install path)
- **Phase-0**: `scripts/adopt_k197_k200_phase0.sh` PASS
- **Sweep**: `wiki/sweeps/2026-07-21-daily.md`

**Archive**: five PDFs → egress-fi cybersec/


## [2026-07-29] cross-wiki route | Optimistic Verifiable Claims — confidential G-code bidding (arXiv:2607.25517)

Cross-wiki stub routed from `@3d-printing-wiki/sources/2026-corn-optimistic-verifiable-claims.md`.
- Created wiki/sources/2026-corn-optimistic-verifiable-claims.md (stub)

## [2026-08-03] brief | K220 cyber Context catalog from OSINT

- Brief: `briefs/2026-08-03_k220-cyber-context-catalog.md` — Context/Pass only, no Integrate
## [2026-08-09] docs | README accuracy + Support block
- README: refreshed corpus counts (~436 sources), welcoming tone, ingest/archive wording
- Support: thank-you + Outlier Weekly / youratto.com / guruwatcher.com / YouTube
- CLAUDE.md Related Wikis: added game-dev-wiki row (matches federation table)
- friend brief: n/a
