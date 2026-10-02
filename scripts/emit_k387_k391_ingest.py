#!/usr/bin/env python3
"""Writer for K387-K391 ingest (2026-10-02). No attack payloads in wiki."""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-10-02"


def w(rel: str, body: str) -> None:
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump_updated(text: str) -> str:
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", text, count=1, flags=re.M)


def add_related(rel: str, ref: str, note: str) -> None:
    p = WIKI / rel
    t = p.read_text(encoding="utf-8")
    yaml_line = f"  - {ref}"
    if yaml_line not in t:
        t = t.replace("related:\n", f"related:\n{yaml_line}\n", 1)
    body_line = f"- @{ref} — {note}"
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n{body_line}\n", 1)
    t = bump_updated(t)
    p.write_text(t, encoding="utf-8")
    print("patched related", rel, "→", ref)


def src(
    slug: str,
    title: str,
    arxiv: str,
    kid: str,
    pdf: str,
    narrative: str,
    concept: str,
    extra_related: list[str] | None = None,
    ood: bool = False,
    wire: str = "",
) -> None:
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra_related or [])]
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else "\n## Relations\n\n"
    if extra_related:
        rel_sec += "".join(f"- @{r}\n" for r in extra_related)
    tags = "source, ood" if ood else "source, arxiv, agent-security"
    keywords = f"{arxiv}, ood" if ood else f"{arxiv}, {kid.lower()}"
    wire_line = wire or (
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)"
        if ood
        else f".cursor/rules/cemini-cybersec-lab-redteam.mdc ({kid})"
    )
    body = f"""---
title: "{title}"
type: source
tags: [{tags}]
keywords: [{keywords}]
{rel_yaml}
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
phase_0_verdict: "REFERENCE {DATE} — no attack payloads in wiki."
wire_status: policy_wired
wire_target: "{wire_line}"
---

## Relations
{rel_sec}
## Raw Concept

| Field | Value |
|-------|-------|
| Title | {title} |
| arXiv | {arxiv} |
| Location | {EGRESS}/{pdf} |
| Retrieved | {DATE} |
| Read status | read (deep-read via grok CLI) |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"sources/{slug}.md", body)


def concept_page(
    slug: str,
    title: str,
    kid: str,
    arxiv: str,
    narrative: str,
    related: list[str],
    wire: str,
) -> None:
    rel_yaml = "\n".join(f"  - {r}" for r in related)
    rel_inline = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, agent-security, {kid.lower()}]
keywords: [{arxiv}, {kid}]
related:
{rel_yaml}
maturity: draft
created: {DATE}
updated: {DATE}
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{rel_inline}

## Raw Concept

Question: **{title}** — operator steal from arXiv {arxiv}?

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"concepts/{slug}.md", body)


def main() -> int:
    # ---------------- K387 ------------------------------------------------
    src(
        "arxiv-2610-00590-hierarchical-llm-cyber-defense",
        "Towards hierarchical cyber defense with large language models: from planning to execution",
        "2610.00590",
        "K387",
        "arxiv-2610.00590-towards-hierarchical-cyber-defense-with-large-la.pdf",
        "**K387** — an RL cyber defender is tied to the network it trained on; hierarchical RL splits "
        "strategic targeting from tactical execution but still retrains per scale. The authors ask whether "
        "**frozen zero-shot LLMs** give retraining-free control, and what changes when LLM control moves from "
        "planning to execution. Controller-agnostic planner-executor: the planner picks a subnet every k=5 "
        "steps, the executor picks a primitive action (deploy decoy / isolate host / nothing). Three "
        "configurations — **RL+RL, LLM+RL, LLM+LLM** — over six models (3B→70B, two cyber-specialised) on "
        "Cyberwheel at 15 / 100 / 1,010 hosts. **Planner-only substitution gives limited gains** as the network "
        "grows; extending control to execution is what helps. Llama-3.3-70B LLM+LLM holds lateral movement to "
        "~1% of steps and impact near zero at all three scales **with one frozen weight set**, where RL+RL "
        "degrades with scale (impact 1.22% → 5.10% → 15.20%) and is retrained per scale. Operator steal: "
        "hierarchical separation is not enough on its own — a weak executor caps the planner's benefit; test "
        "the **whole stack** at each scale, not the planner alone. Counter-example worth keeping: "
        "Trendyol-Cybersecurity-70B collapses at the large scale (compromise 14.45%, defense 12.95%) where the "
        "general-purpose 70B holds — **security specialisation is not a cross-scale guarantee**. No repo "
        "(© 2026 IEEE). **No attack payloads in wiki.**",
        "concepts/hierarchical-llm-cyber-defense-planner-executor.md",
        [
            "concepts/cyber-range-autonomous-incident-response-agents.md",
            "concepts/sentinel-rl-soc-topological-reasoning.md",
            "concepts/trident-agentic-drl-defense-redteam.md",
        ],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K387)",
    )
    concept_page(
        "hierarchical-llm-cyber-defense-planner-executor",
        "Hierarchical LLM cyber defense — planner vs executor",
        "K387",
        "2610.00590",
        "Split an autonomous defender into a **planner** (which subnet to defend) and an **executor** (which "
        "action to take), then swap RL or a frozen LLM into each slot. The finding to carry: **replacing only "
        "the planner buys little**; the gain comes when the executor is strong too. Measure the whole stack "
        "across network scales — a controller that looks good at 15 hosts can fail at 1,010. Keep the "
        "**specialisation trap** in view: a cyber-tuned model can beat a general model at one scale and "
        "collapse at another. Defense-side lab only; no attack recipes.",
        [
            "sources/arxiv-2610-00590-hierarchical-llm-cyber-defense.md",
            "concepts/cyber-range-autonomous-incident-response-agents.md",
            "concepts/sentinel-rl-soc-topological-reasoning.md",
            "concepts/trident-agentic-drl-defense-redteam.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K387)",
    )

    # ---------------- K388 ------------------------------------------------
    src(
        "arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid",
        "Video-Index: a curated meta-benchmark for video understanding",
        "2610.00960",
        "K388",
        "arxiv-2610.00960-video-index-a-curated-meta-benchmark-for-video-u.pdf",
        "**K388** — a benchmark score should certify the capability it claims, but models can exploit answer "
        "options, question text, or partial visual evidence instead. The authors define an **attack pyramid**: "
        "five nested shortcut-attacker sets with growing access (options → text → other items → one frame or "
        "captions → shuffled/truncated video). **Exploitability** ε = max attacker accuracy − chance; a "
        "benchmark **breaks** at the first level where ε exceeds the reference model's margin. Auditing 115 "
        "video benchmarks: **35 break before seeing a single frame**; on 51 benchmarks with temporal probes, "
        "**shuffled frames keep a median 96%** of full-video accuracy; near-duplicate questions make up at "
        "least half the items in 63 benchmarks. Operator steal for **any** agent-security eval, not just "
        "video: **a score is a capability certificate only above the strongest tested shortcut** — report a "
        "**breaking level** beside the certificate, and gate your own benchmark with a red-team pass that "
        "drops items a weak attacker already solves. Repo not stated. **Audit-only — no precheck script.**",
        "concepts/benchmark-shortcut-attack-pyramid-audit.md",
        [
            "concepts/guardrail-construct-validity-agent-eval.md",
            "concepts/ai-redteam-evidential-ceiling.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K388)",
    )
    concept_page(
        "benchmark-shortcut-attack-pyramid-audit",
        "Benchmark shortcut attack pyramid",
        "K388",
        "2610.00960",
        "Audit a benchmark by attacking it at nested levels of access: **options only → question text → other "
        "items in the pool → a single frame or captions → shuffled or truncated video**. Report the "
        "**breaking level** — the first level where the shortcut beats the reference margin — beside the "
        "headline score. Apply it to **agent-security** evals the same way: if a blind or option-only "
        "attacker already scores near the reported number, the score certifies nothing. Watch **near-duplicate "
        "items** and **effective size** (a 200-item draw can hold ~32 effective items). Audit-only.",
        [
            "sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md",
            "concepts/guardrail-construct-validity-agent-eval.md",
            "concepts/ai-redteam-evidential-ceiling.md",
            "concepts/faithful-agent-asr-measurement.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K388)",
    )

    # ---------------- K389 ------------------------------------------------
    src(
        "arxiv-2610-01058-momat-quantized-llm-jailbreak-defense",
        "MOMAT: mixture of multiple atlases for low-power jailbreak defense of quantized LLMs",
        "2610.01058",
        "K389",
        "arxiv-2610.01058-momat-mixture-of-multiple-atlases-for-low-power.pdf",
        "**K389** — **quantization weakens alignment safeguards**, and the effect is **scale-dependent**: "
        "Llama2-13B shows negligible ASR change under W4A8 (Δ −0.7% AdvBench / −2.0% Malicious Instruct) while "
        "**Llama2-7B rises** (Δ **+4.4%** / **+3.0%**). The 7B model is the one that compresses to 3.76 GB and "
        "is therefore the realistic edge deployment — so **the compression that makes a model deployable is "
        "the compression that erodes its safety**. **MOMAT** organises safety knowledge into domain-localised "
        "**atlases** (semantic clusters of harmful/benign samples + policy templates), retrieves top-k per "
        "atlas, and scores with a lightweight MoE detector, with a compute-in-memory similarity engine. "
        "Results on W4A8 quantised models: **ASR 0.00** on both AdvBench and Malicious Instruct for "
        "**Llama2-7B** (undefended 32.5% / 28.0%) and **Mistral-7B** (undefended 68.2% / 67.5%), with **FRR "
        "unchanged** (+0.0) — no benign overkill. CiM retrieval cuts a 100-query batch from 15,052.44 ms to "
        "3,207.21 ns and energy from 8.1e7 µJ to 3.32 µJ. Operator steal: **do not assume a safety-tuned "
        "model stays aligned after quantisation** — re-measure ASR *and* FRR at the shipped precision, and "
        "report both. 223.2k-sample dataset promised. **No jailbreak payloads in wiki.**",
        "concepts/quantized-llm-jailbreak-defense-atlas.md",
        [
            "concepts/defender-centric-jailbreak-utility.md",
            "concepts/llm-adversarial-fuzzing.md",
            "concepts/crescendo-multi-turn-jailbreak.md",
            "concepts/instruction-hierarchy-conflict-benchmark.md",
        ],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K389)",
    )
    concept_page(
        "quantized-llm-jailbreak-defense-atlas",
        "Quantized-LLM jailbreak defense — atlas retrieval",
        "K389",
        "2610.01058",
        "**Quantisation degrades safety alignment, and smaller models lose more.** Before deploying a guard on "
        "a quantised model, re-measure **ASR at the shipped precision** — a model that was aligned in FP16 can "
        "be materially weaker at W4A8. Measure **FRR** too: a defense that suppresses ASR by over-refusing "
        "benign traffic is a failure, and the useful result here is zero ASR with **FRR unchanged**. The "
        "defense pattern worth stealing is **domain-localised retrieval** (atlases) rather than one flat safety "
        "corpus, because quantisation erodes exactly the global embedding geometry a flat corpus relies on.",
        [
            "sources/arxiv-2610-01058-momat-quantized-llm-jailbreak-defense.md",
            "concepts/defender-centric-jailbreak-utility.md",
            "concepts/llm-adversarial-fuzzing.md",
            "concepts/crescendo-multi-turn-jailbreak.md",
            "concepts/instruction-hierarchy-conflict-benchmark.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K389)",
    )

    # ---------------- K390 (OOD: embodied agents) -------------------------
    src(
        "arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood",
        "Reconstruct, practice, go real: guided self-improvement for embodied agents",
        "2610.02204",
        "K390",
        "arxiv-2610.02204-reconstruct-practice-go-real-guided-self-improve.pdf",
        "**K390 — OOD for security, in-scope for agent-harness evolution.** RPG improves a robot execution "
        "system **without updating model weights**: reconstruct practice tasks from an offline dataset, run "
        "them in simulation, diagnose failures with privileged simulator state plus video, then revise a shared "
        "**skill library and system prompt**. The transferable mechanism is the **promotion gate**: a candidate "
        "revision is eligible only if mean task success rises **and** no task drops more than one success in "
        "five, and merged revisions are retested under the same gate. Report: 28.6% → 95.0% over 15 rounds on "
        "22 held-out tasks; 30/30 physical trials. Security relevance: **none** — no adversary or attack "
        "surface. Keep it as a **harness-evolution pattern** (gate skill/prompt writes on no-regression across "
        "tasks), which pairs with the validation-ratchet family. Project page `rpg-robot.github.io`, license "
        "not stated — no clone.",
        "concepts/cross-task-no-regression-skill-promotion-gate.md",
        [
            "concepts/skill-misevolution.md",
            "concepts/experience-driven-redteam-skill-evolution.md",
            "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        ],
        ood=True,
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K390)",
    )
    concept_page(
        "cross-task-no-regression-skill-promotion-gate",
        "Cross-task no-regression skill promotion gate",
        "K390",
        "2610.02204",
        "An agent files an update to its own **skill library or system prompt** only if a gate passes on "
        "**every** task in the suite: mean success must rise **and** no single task may fall more than a set "
        "margin. Merged revisions are retested under the same gate, so an integration that fixes one task but "
        "breaks another is rejected. This is the no-regression sibling of the validation ratchet — use it to "
        "bound **skill and prompt writes** in an owned harness. Domain is robot manipulation; the mechanism is "
        "harness-general. **No skill bodies in wiki.**",
        [
            "sources/arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood.md",
            "concepts/skill-misevolution.md",
            "concepts/experience-driven-redteam-skill-evolution.md",
            "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        ],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K390)",
    )

    # ---------------- K391 ------------------------------------------------
    src(
        "arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use",
        "KaliBench: a fine-grained benchmark for cybersecurity tool use on Kali Linux with runtime-free verifiable rewards",
        "2610.02206",
        "K391",
        "arxiv-2610.02206-kalibench-a-fine-grained-benchmark-for-cybersecu.pdf",
        "**K391** — measures whether a model can turn a plain-language request into an **exact, executable** "
        "Kali Linux command: 8,504 query–command pairs, 1,642 tools, 23 capability dimensions, five security "
        "phases. Scoring is **runtime-free** — deterministic canonicalisation plus alias-aware matching, no "
        "execution. Headline: **no open-weight model exceeds 42% exact-command accuracy** unrestricted (best "
        "41.3%); proprietary best is 61.68%. The diagnostic that transfers: **tool choice is not the "
        "bottleneck, the arguments are** — tool accuracy rises **72.0% → 95.2%** when candidates are narrowed, "
        "and exact-correct rises **22.3% → 73.1%** only when documentation is supplied. SFT+GRPO on the "
        "benchmark lifts an 8B model by **7.5 points** mean Total Score, near a 685B MoE. Operator steal: "
        "score tool invocation against a **fixed reference**, and **split tool-selection from "
        "argument-construction** in any tool-gate diagnostic. **Licence discrepancy:** the paper states "
        "**CC BY-NC 4.0**, but the repo has **no LICENSE file and no README licence text** (verified via "
        "`gh api` 2026-10-02) — treat the claim as unverified, **no clone**. Repo `github.com/RISys-Lab/KaliBench`. **No attack payloads in wiki.**",
        "concepts/kalibench-nl-to-cli-tool-use-eval.md",
        [
            "concepts/secure-ai-powered-pentest-agents.md",
            "concepts/privescalate-llm-linux-privilege-escalation.md",
            "concepts/security-agent-authority-auditability-slr.md",
        ],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K391)",
    )
    concept_page(
        "kalibench-nl-to-cli-tool-use-eval",
        "KaliBench — NL-to-CLI tool-use evaluation",
        "K391",
        "2610.02206",
        "Score an agent's tool invocation against a **fixed reference command**, not against its own account "
        "of what it ran. KaliBench does this **without executing** anything: canonicalise the command, then "
        "match tool name, alias-aware optional flags, and ordered positional arguments. The split worth "
        "reusing is **tool selection vs argument construction** — selection nearly resolves when the candidate "
        "set is narrowed, while exactness does not move until the arguments are pinned down. Report both, "
        "never a single 'tool accuracy' figure. Caveat: ground truth comes from manuals captured at build "
        "time, so flags drift. Licence claim unverified — no clone, no dataset download.",
        [
            "sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md",
            "concepts/secure-ai-powered-pentest-agents.md",
            "concepts/privescalate-llm-linux-privilege-escalation.md",
            "concepts/security-agent-authority-auditability-slr.md",
        ],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K391)",
    )

    # ---------------- cross-links into existing concepts -------------------
    _backlinks = {
        "sources/arxiv-2610-00590-hierarchical-llm-cyber-defense.md": (
            "concepts/cyber-range-autonomous-incident-response-agents.md",
            "concepts/sentinel-rl-soc-topological-reasoning.md",
            "concepts/trident-agentic-drl-defense-redteam.md",
        ),
        "sources/arxiv-2610-00960-video-index-benchmark-shortcut-attack-pyramid.md": (
            "concepts/guardrail-construct-validity-agent-eval.md",
            "concepts/ai-redteam-evidential-ceiling.md",
            "concepts/faithful-agent-asr-measurement.md",
        ),
        "sources/arxiv-2610-01058-momat-quantized-llm-jailbreak-defense.md": (
            "concepts/defender-centric-jailbreak-utility.md",
            "concepts/llm-adversarial-fuzzing.md",
            "concepts/crescendo-multi-turn-jailbreak.md",
            "concepts/instruction-hierarchy-conflict-benchmark.md",
        ),
        "sources/arxiv-2610-02204-rpg-embodied-agent-self-improvement-ood.md": (
            "concepts/skill-misevolution.md",
            "concepts/experience-driven-redteam-skill-evolution.md",
            "concepts/skilldre-dual-stage-malicious-skill-evolution-lab.md",
        ),
        "sources/arxiv-2610-02206-kalibench-nl-to-cli-cybersecurity-tool-use.md": (
            "concepts/secure-ai-powered-pentest-agents.md",
            "concepts/privescalate-llm-linux-privilege-escalation.md",
            "concepts/security-agent-authority-auditability-slr.md",
        ),
    }
    for source_ref, concept_refs in _backlinks.items():
        for concept_ref in concept_refs:
            add_related(concept_ref, source_ref, "K387-K391 ingest source page")

    _concept_links = {
        "concepts/cyber-range-autonomous-incident-response-agents.md": "concepts/hierarchical-llm-cyber-defense-planner-executor.md",
        "concepts/trident-agentic-drl-defense-redteam.md": "concepts/hierarchical-llm-cyber-defense-planner-executor.md",
        "concepts/guardrail-construct-validity-agent-eval.md": "concepts/benchmark-shortcut-attack-pyramid-audit.md",
        "concepts/ai-redteam-evidential-ceiling.md": "concepts/benchmark-shortcut-attack-pyramid-audit.md",
        "concepts/faithful-agent-asr-measurement.md": "concepts/benchmark-shortcut-attack-pyramid-audit.md",
        "concepts/defender-centric-jailbreak-utility.md": "concepts/quantized-llm-jailbreak-defense-atlas.md",
        "concepts/skill-misevolution.md": "concepts/cross-task-no-regression-skill-promotion-gate.md",
        "concepts/experience-driven-redteam-skill-evolution.md": "concepts/cross-task-no-regression-skill-promotion-gate.md",
        "concepts/secure-ai-powered-pentest-agents.md": "concepts/kalibench-nl-to-cli-tool-use-eval.md",
        "concepts/privescalate-llm-linux-privilege-escalation.md": "concepts/kalibench-nl-to-cli-tool-use-eval.md",
    }
    for rel, ref in _concept_links.items():
        add_related(rel, ref, "K387-K391 cross-link")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
