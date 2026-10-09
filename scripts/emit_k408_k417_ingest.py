#!/usr/bin/env python3
"""Writer for K408-K417 ingest (2026-10-09). No attack payloads in wiki.

Slugs WITHOUT .md; every related ref MUST end with .md.
"""
from __future__ import annotations

import re
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1] / "wiki"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/cybersec"
DATE = "2026-10-09"


def w(rel, body):
    p = WIKI / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    print("wrote", rel)


def bump(t):
    return re.sub(r"^updated: \d{4}-\d{2}-\d{2}", f"updated: {DATE}", t, count=1, flags=re.M)


def add_related(rel, ref, note):
    assert ref.endswith(".md"), ref
    p = WIKI / rel
    t = p.read_text(encoding="utf-8")
    if f"  - {ref}" not in t:
        t = t.replace("related:\n", f"related:\n  - {ref}\n", 1)
    if f"- @{ref}" not in t:
        t = t.replace("## Relations\n\n", f"## Relations\n\n- @{ref} — {note}\n", 1)
    p.write_text(bump(t), encoding="utf-8")
    print("patched", rel, "→", ref)


def src(slug, title, arxiv, kid, pdf, narrative, concept, extra=None, ood=False, wire=""):
    assert not slug.endswith(".md")
    rels = ([f"  - {concept}"] if concept else []) + [f"  - {r}" for r in (extra or [])]
    for r in rels:
        assert r.strip().endswith(".md"), r
    rel_yaml = "related:\n" + "\n".join(rels) if rels else "related: []"
    rel_sec = f"\n## Relations\n\n- @{concept}\n" if concept else "\n## Relations\n\n"
    if extra:
        rel_sec += "".join(f"- @{r}\n" for r in extra)
    tags = "source, ood" if ood else "source, arxiv, agent-security"
    keywords = f"{arxiv}, ood" if ood else f"{arxiv}, {kid.lower()}"
    wire_line = wire or (
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (OOD)" if ood
        else f".cursor/rules/cemini-cybersec-agent-audit.mdc ({kid})")
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
| Read status | read (deep-read) |

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"sources/{slug}.md", body)


def concept(slug, title, kid, arxiv, narrative, related, wire, tags="agent-security"):
    assert not slug.endswith(".md")
    for r in related:
        assert r.endswith(".md"), r
    rels = "\n".join(f"  - {r}" for r in related)
    inl = "\n".join(f"- @{r}" for r in related)
    body = f"""---
title: "{title} ({kid})"
type: concept
tags: [concept, {tags}, {kid.lower()}]
keywords: [{arxiv}, {kid}]
related:
{rels}
maturity: draft
created: {DATE}
updated: {DATE}
wire_status: policy_wired
wire_target: "{wire}"
---

## Relations

{inl}

## Raw Concept

Question: **{title}** — operator steal from arXiv {arxiv}?

## Narrative

{narrative}

## Snippets

> See arXiv {arxiv} abstract. [Source: arXiv {arxiv} (retrieved {DATE})]
"""
    w(f"concepts/{slug}.md", body)


def main() -> int:
    # ---------- K408 web-agent hijack -------------------------------------
    src("arxiv-2610-09240-adversarial-images-hijack-web-agents",
        "Adversarial images hijack web agents from visual grounding to browser execution",
        "2610.09240", "K408",
        "arxiv-2610.09240-adversarial-images-hijack-web-agents-from-visual.pdf",
        "**K408** — a modern **web agent is a vision-language model that both perceives and acts**, so a "
        "perturbed *image* on a page is not just visual noise: the agent reads it as grounding evidence and "
        "then **executes** on it in the browser. The attack therefore crosses two stages — it hijacks "
        "**visual grounding** and carries through to **browser execution** — which is why a screenshot-level "
        "guard is not enough. Repo `github.com/MoonTea0416/WebMirage`; licence not stated. Operator steal: "
        "**an image on a page an agent browses is untrusted input on the same footing as a tool "
        "description** — the K421 data/control collapse, in the browser rather than the cluster. Treat any "
        "agent that reads pixels and holds browser credentials as needing a **least-privilege browser "
        "context**, not a better prompt. Authorized lab only. **No perturbation recipes or attack code in "
        "wiki.**",
        "concepts/adversarial-images-hijack-web-agents.md",
        ["concepts/model-is-not-a-security-boundary-kubernetes-agents.md",
         "concepts/prompt-injection-detector-calibration.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K408)")
    concept("adversarial-images-hijack-web-agents",
        "Adversarial images hijack web agents", "K408", "2610.09240",
        "An agent that **reads pixels and then acts** collapses the boundary between content and command. A "
        "page image the agent merely *looks at* can steer its **visual grounding**, and because the same "
        "agent holds browser execution, that steer becomes an **action** — the attack crosses from "
        "perception into the execution stage rather than stopping at mis-description.\n\n"
        "The operator consequence: screencast or OCR filtering is a **perception** control, and the failure "
        "here is **downstream of it**. What helps is bounding what the browser context can *do* once "
        "grounding is wrong — least-privilege sessions, action confirmation for credentialed steps, and "
        "treating any rendered image as untrusted input. Same shape as K421's 'the model is not a security "
        "boundary', applied to the browser.",
        ["sources/arxiv-2610-09240-adversarial-images-hijack-web-agents.md",
         "concepts/model-is-not-a-security-boundary-kubernetes-agents.md",
         "concepts/prompt-injection-detector-calibration.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K408)")

    # ---------- K409 defensive sufficiency --------------------------------
    src("arxiv-2610-09892-defensive-sufficiency-stackelberg",
        "Defensive sufficiency in a Stackelberg model of AI security",
        "2610.09892", "K409",
        "arxiv-2610.09892-defensive-sufficiency-in-a-stackelberg-model-of.pdf",
        "**K409 — when does the test → repair → update loop actually give you security?** The paper answers "
        "with three conditions over a **finite attack surface**: every unresolved attack keeps a "
        "**persistent chance of discovery** (epsilon), **repairs are effective**, and **updates preserve "
        "earlier protection**. Under those, the surface is defended with probability 1 — "
        "**P(T > t) ≤ min{{1, N(1−epsilon)^t}}** and **E[T] ≤ N/epsilon**, so coverage time for "
        "probability 1−delta is **t ≥ log(N/delta)/epsilon**. The third condition is the one operators "
        "break: an update that fixes today's failure while reopening yesterday's resets the clock.\n\n"
        "The second result is structural and surprising: **repair regions, not singletons.** Region-level "
        "expected completion time is **m·H_m** against **N·H_N** for singleton repairs (N = m·r, r > 1) — "
        "fixing a *class* of failures is asymptotically far cheaper than fixing each instance. The rest is "
        "an economic model (attacker cost kappa, discovery rate eta) for **when investing in the feedback "
        "loop is worth it at all**, with simulation matching the theory to within a fraction of a point. "
        "Operator steal: a red-team program is only a control if **findings persist, repairs hold, and "
        "updates do not regress** — and repairing a category beats repairing the case. Pairs K390 (the "
        "no-regression promotion gate) and K285-a (local suppression is not repair).",
        "concepts/defensive-sufficiency-feedback-loop.md",
        ["concepts/cross-task-no-regression-skill-promotion-gate.md",
         "concepts/local-suppression-vs-repair.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K409)")
    concept("defensive-sufficiency-feedback-loop",
        "When the test-repair loop is actually a control", "K409", "2610.09892",
        "Red-teaming and incident feedback only produce security under three conditions: **every unresolved "
        "attack keeps a persistent chance of being discovered**, **repairs work**, and **updates preserve "
        "earlier protection**. Drop the third and the loop churns — you fix one thing and reopen another, "
        "and the completion clock never runs down. Given all three, a finite surface is covered with "
        "probability 1, with expected time bounded by **N/epsilon** and coverage time "
        "**log(N/delta)/epsilon**.\n\n"
        "The second, cheaper rule: **repair regions, not singletons** — **m·H_m** against **N·H_N** — so a "
        "fix that closes a *class* of failure beats a pile of per-case fixes. And the loop is an "
        "investment: when the attacker's cost is high enough, **deterrence** (no new capability needed) "
        "beats buying more detection. Ask of any security program: **do findings persist, do repairs hold, "
        "and do updates stop regressing?**",
        ["sources/arxiv-2610-09892-defensive-sufficiency-stackelberg.md",
         "concepts/cross-task-no-regression-skill-promotion-gate.md",
         "concepts/local-suppression-vs-repair.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K409)")

    # ---------- K410 SOC remediation proxy --------------------------------
    src("arxiv-2610-09906-constrained-action-ai-remediation-siem",
        "Constrained-action AI remediation for SIEM/XDR via a guardrails proxy",
        "2610.09906", "K410",
        "arxiv-2610-09906-constrained-action-ai-remediation-for-siem-xdr-v.pdf",
        "**K410** — SOCs are drowning in correlated alerts with too few analysts, and LLM remediation is "
        "the obvious lever. This wires an LLM into SIEM/XDR **through a NeMo-Guardrails proxy** so the "
        "model proposes remediation but a rail constrains what it can emit. Injection defence over 200 "
        "adversarial variants (AdvBench, JailbreakBench, HarmBench, homoglyph, Base64, fake `[SYSTEM]` "
        "framing, zero-width): **proxy recall 94.5% at 0.1% FPR** against a raw LLM's **25.0% at 0.0%** — "
        "+69.5 pp — with the proxy catching **189/200** at the input rail.\n\n"
        "The cost is latency: proxy P50 **14.14 s** against **0.31 s** for the bare call (~46×), and the "
        "latency curve goes bimodal. The fix is the interesting part: a **deterministic Tier-0 gate** in "
        "front — **58% recall at 0.00% FPR, 0.18 s (78× faster)**, and alone it recovers all 50 augmented "
        "records **with zero LLM calls**. Live active-response testing (T1110, T1059, T1078): **54 injected "
        "alerts produced 41 action records, every one requiring manual approval, none dispatched**, and an "
        "argument validator rejected a target failing its schema. Operator steal: **cheap deterministic "
        "gate first, LLM rail second, and human approval on every action** — the schema validator is doing "
        "real work, not decoration. Pairs K307/K312 (gate before the irreversible step).",
        "concepts/constrained-action-soc-remediation.md",
        ["concepts/step-level-agent-guardrails.md",
         "concepts/non-decaying-loop-safety-state.md",
         "concepts/model-is-not-a-security-boundary-kubernetes-agents.md"],
        wire=".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K410)")
    concept("constrained-action-soc-remediation",
        "Constrained-action SOC remediation", "K410", "2610.09906",
        "Let an LLM triage SIEM/XDR alerts, but never let it act unconstrained: put a **rail** between the "
        "model and the effect so it can only emit schema-valid remediation. Measured on 200 injection "
        "variants, that rail took recall from **25.0% to 94.5%** at 0.1% false-positive rate — but cost "
        "**14.14 s** median against a 0.31 s bare call.\n\n"
        "The design lesson is the **cascade**: a deterministic **Tier-0 gate** in front gives 58% recall at "
        "**0.00% FPR in 0.18 s with no LLM calls at all**, and catches content the LLM rail misses. Then "
        "the rail, then **manual approval on every action** — in live testing 41 action records were "
        "produced from 54 injected alerts and **none were dispatched**. Two rules generalise: **order the "
        "cheap deterministic check first**, and **validate the arguments, not just the intent** (the "
        "schema check rejected an action whose target came from attacker-controlled metadata).",
        ["sources/arxiv-2610-09906-constrained-action-ai-remediation-siem.md",
         "concepts/step-level-agent-guardrails.md",
         "concepts/non-decaying-loop-safety-state.md",
         "concepts/model-is-not-a-security-boundary-kubernetes-agents.md"],
        ".cursor/rules/cemini-cybersec-mcp-tool-control.mdc (K410)")

    # ---------- K411 post-hallucination reasoning -------------------------
    src("arxiv-2610-10455-phrbench-post-hallucination-reasoning",
        "PHRBench: a behavioral evaluation of post-hallucination reasoning in LLMs",
        "2610.10455", "K411",
        "arxiv-2610.10455-phrbench-a-behavioral-evaluation-of-pos.pdf",
        "**K411 — what a model does *after* it hallucinates matters more than that it hallucinated.** "
        "PHRBench feeds models a premise containing a hallucination and measures subsequent **reasoning "
        "behaviour**, not just answer accuracy. Across 18 models, hallucinated premises cost **7.7 "
        "percentage points** of accuracy on average — and the drop is **larger for proprietary models "
        "(11.0%) than open-source (6.1%)**, with GPT-5.2 falling 16.9 points. It is not one domain: "
        "Biomedicine 8.34 pp, Physics 7.12, Code Generation 6.89 (17 of 18 models drop there).\n\n"
        "The taxonomy is the reusable part. **Hallucination Compliance** versus **Heuristic Correction** — "
        "and correction is rare: Qwen2.5 7.58% at 1.5B rising to 26.48% at 72B; GLM-4-9B 1.98%; GPT-5.2 "
        "3.69%. Only **11 of 18** models produce **insightful trajectories** above 10%. Insightful paths "
        "show **more reasoning words (~+34.7)** and a much higher **belief-update frequency (0.68 vs "
        "0.24)** — the model actually revises, rather than reasoning longer around a wrong premise. "
        "Augmentation type matters: State Distortion costs 9.4 pp, Rule Contradiction 7.4, "
        "**Pseudoscientific Entanglement only 1.8** — a fluent pseudo-scientific framing barely moves the "
        "score. Operator steal: **test whether a model corrects or commits**, and prefer belief-update "
        "frequency over output length as the signal. Pairs K308 (decorative reasoning) and K337 "
        "(explanation necessity).",
        "concepts/post-hallucination-reasoning-behavior.md",
        ["concepts/chain-of-thought-decorative-reasoning-audit.md",
         "concepts/llm-explanation-necessary-sufficient-audit.md",
         "concepts/measurement-integrity-mcp-security-eval.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K411)")
    concept("post-hallucination-reasoning-behavior",
        "Does the model correct or commit?", "K411", "2610.10455",
        "A hallucination is not a single wrong token — it is a premise the model then reasons from. "
        "PHRBench measures the aftermath: given a hallucinated premise, does the model **correct** or "
        "**commit**? Committing is the norm. Hallucinated premises cost **7.7 pp** of accuracy on "
        "average, more for **proprietary** models (11.0%) than open ones (6.1%), and **correction is "
        "rare** — only 11 of 18 models produce insightful trajectories above 10%.\n\n"
        "The discriminating signal is **belief-update frequency**, not length: insightful paths run "
        "**0.68 vs 0.24** and carry ~35 more reasoning words, so a model that reasons *longer* around a "
        "wrong premise looks busy without being right. And not all bad premises are equal — a fluent "
        "**pseudoscientific** framing costs only **1.8 pp** while **state distortion** costs **9.4**. "
        "Operator rule: when auditing reasoning, ask whether the model **revises under contradiction** — "
        "pairs the K308 finding that chain-of-thought is not evidence.",
        ["sources/arxiv-2610-10455-phrbench-post-hallucination-reasoning.md",
         "concepts/chain-of-thought-decorative-reasoning-audit.md",
         "concepts/llm-explanation-necessary-sufficient-audit.md",
         "concepts/measurement-integrity-mcp-security-eval.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K411)")

    # ---------- K412 engramedit -------------------------------------------
    src("arxiv-2610-10533-engramedit-conditional-memory-knowledge-updates",
        "EngramEdit: decoupled knowledge updates in LLMs through conditional memory",
        "2610.10533", "K412",
        "arxiv-2610.10533-engramedit-decoupled-knowledge-updates-in-llms-t.pdf",
        "**K412** — knowledge editing usually fights the model's weights. EngramEdit instead puts updates "
        "in a **conditional memory** and reads them back at inference, leaving the base model alone. On "
        "CounterFact (2,000 sequential edits) **Efficacy 99.5** and **Generalization 97.0** against "
        "pre-edit 9.5 / 11.2, with **Utility 93.9** versus 35.8 — and it beats MoEEdit on Generalization "
        "(97.0 vs 67.1) and Memory-FT on Utility.\n\n"
        "The most useful result is the **memory-disable test**: after 2,000 edits, disabling the "
        "fact-related updated embeddings (~4.7 per fact) turns **89.4%** of previously successful prompts "
        "into failures and moves the edit margin from **15.5 to −5.9**, while **matched random disabling** "
        "causes **0 failures** and moves the margin by −0.0003. That is a clean demonstration that the "
        "edit lives in the **memory**, not in a prompt-level artefact — the control an editing claim "
        "usually lacks. Multi-hop is where it gets honest: on MQuAKE **CoT accuracy 25.2** vs 8.5 for "
        "fine-tuning, but 2-hop 36.92 falls to 15.09 at 4-hop, and **8.66% of facts sharing an n-gram "
        "account for 97.96% of Efficacy failures**. Operator steal: for any model-update claim, **demand a "
        "disable test with a random-disabling control** — and expect n-gram collisions to be the failure "
        "mode. Pairs K285-a (local suppression is not repair).",
        "concepts/conditional-memory-knowledge-editing.md",
        ["concepts/local-suppression-vs-repair.md",
         "concepts/agent-execution-provenance.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K412)")
    concept("conditional-memory-knowledge-editing",
        "Conditional memory, and the disable test", "K412", "2610.10533",
        "Updating a model's knowledge by rewriting weights damages everything around the edit. Putting the "
        "update in **conditional memory** instead keeps the base model intact — **Efficacy 99.5 / "
        "Generalization 97.0** with **Utility 93.9** after 2,000 sequential edits.\n\n"
        "The transferable method is the **evidence**, not the architecture: **disable the fact-related "
        "memory and see if the behaviour reverts.** It does — **89.4%** of successes become failures and "
        "the margin flips from +15.5 to −5.9 — while **random disabling** changes nothing (−0.0003, zero "
        "failures). That control separates a real memory edit from a prompt artefact, and it is rare in "
        "editing papers. Two caveats to carry: multi-hop degrades with depth (36.92% at 2-hop to 15.09% at "
        "4-hop), and **n-gram collisions** concentrate the failures — 8.66% of facts carry 97.96% of them.",
        ["sources/arxiv-2610-10533-engramedit-conditional-memory-knowledge-updates.md",
         "concepts/local-suppression-vs-repair.md",
         "concepts/agent-execution-provenance.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K412)")

    # ---------- K414 ReSI -------------------------------------------------
    src("arxiv-2610-12233-resi-recursive-safety-improvement",
        "ReSI: recursive safety improvement toward resistant and resilient AI",
        "2610.12233", "K414",
        "arxiv-2610-12233-resi-recursive-safety-improvement-towar.pdf",
        "**K414 — a post-training loop that beats frontier models on safety at a few points of benign "
        "cost.** ReSI runs a **recursive** improvement loop with a **Pareto gate**: a round is accepted "
        "only if it improves safety without breaking the benign budget, and the loop stops when no round "
        "passes. X-Teaming ASR falls to **31.45%** against a backbone mean of **86.01%** (−54.56 pp) — "
        "better than **GPT-5.6-Luna at 56.69%**, and frontier models sit at 56.69–84.85%. The hardest "
        "slice moves most: **H-CoT ASR 72–100% → 0–18%**.\n\n"
        "The cost is stated honestly: benign full-compliance drops **2.80 pp** on two of four models and "
        "**IFEval loose accuracy falls 1.31–2.07 pp**; GPQA-Diamond and MMLU-Pro move within about ±2 pp. "
        "Accepted rounds were few — 1 to 3 per model, each loop then stopping because **the next round had "
        "no Pareto-gate pass**. Operator steal: **gate every safety round on a benign cost budget and stop "
        "when the gate stops passing** — that is what keeps a safety loop from trading capability away "
        "silently. Pairs K390 (the no-regression promotion gate) and K409 (defensive sufficiency).",
        "concepts/recursive-safety-improvement-pareto.md",
        ["concepts/cross-task-no-regression-skill-promotion-gate.md",
         "concepts/defensive-sufficiency-feedback-loop.md",
         "concepts/psychological-multiturn-jailbreaks.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K414)")
    concept("recursive-safety-improvement-pareto",
        "Recursive safety improvement under a Pareto gate", "K414", "2610.12233",
        "A safety-improvement loop is only safe for the product if it cannot quietly spend capability to "
        "buy safety. ReSI's structure is the steal: **each round is accepted only if it passes a Pareto "
        "gate on a benign cost budget**, and the loop **stops when no round passes**. That yielded "
        "X-Teaming ASR **31.45%** against an 86.01% backbone — better than the frontier model at 56.69% — "
        "with H-CoT dropping from 72–100% to 0–18%.\n\n"
        "The honest cost: **−2.80 pp** benign full-compliance on two models and **−1.31 to −2.07 pp** "
        "IFEval. And note the loop self-terminated after **1–3 rounds** because the gate stopped passing — "
        "that termination is a feature, not a failure: it is the budget telling you the remaining safety "
        "gains cost more capability than they are worth. Generalise the shape: **gate, measure the benign "
        "cost, stop when the gate fails.**",
        ["sources/arxiv-2610-12233-resi-recursive-safety-improvement.md",
         "concepts/cross-task-no-regression-skill-promotion-gate.md",
         "concepts/defensive-sufficiency-feedback-loop.md",
         "concepts/psychological-multiturn-jailbreaks.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K414)")

    # ---------- K415 + K416 compliance verdicts ---------------------------
    src("arxiv-2610-12313-verdict-without-the-rule-compliance-invariance",
        "Verdict without the rule: diagnosing and auditing LLM compliance systems",
        "2610.12313", "K415",
        "arxiv-2610.12313-verdict-without-the-rule-diagnosing-and.pdf",
        "**K415 — an LLM compliance verdict may not depend on the rule it was given.** The test is direct: "
        "**delete, swap, or negate the governing rule while holding the case fixed**, and check whether the "
        "verdict changes (**OCS**) or the model's internal compliance representation shifts at all "
        "(**ICS-delta**). Across five models and 20 regulatory / platform-policy domains, neither moves "
        "much: mean **OCS-agg = 0.069**, i.e. roughly **7% of verdicts change** when the rule is "
        "perturbed, against ~90% baseline accuracy. Best single case is still only **0.265**.\n\n"
        "Two things keep this from being a measurement artefact, and they are the reason to trust it. "
        "First, a **bias-corrected permutation null** puts the expected OCS near 0.5 while observed sits "
        "at 0.07–0.09 (every p < 0.0001). Second, on the **rule-necessary subset** — cases where the "
        "baseline is right and deletion makes it wrong — OCS-swap is **0.73–1.00** against a pooled "
        "0.08–0.12. So the metric *does* fire when the rule genuinely decides. The authors' own reading is "
        "that low OCS largely reflects **scenario-side label signal**: the case facts alone determine the "
        "verdict in most items. LegalBench (**0.255**) and ContractNLI (**0.318**) move far more than the "
        "synthetic set (0.081), which is exactly what you would expect if the synthetic cases are easier "
        "to call from facts alone. Operator steal: **a compliance model's verdict is not evidence that it "
        "consulted the rule** — audit with a rule perturbation and report the rule-necessary subset "
        "separately. Pairs K416 and K398.",
        "concepts/compliance-verdict-rule-invariance.md",
        ["concepts/citation-is-not-consultation.md",
         "concepts/compliance-boundary-adjacent-pair-search.md",
         "concepts/guardrail-construct-validity-agent-eval.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K415)")
    src("arxiv-2610-12361-cited-but-not-consulted-authority-swap-audit",
        "Cited but not consulted: a counterfactual audit of legal authority use",
        "2610.12361", "K416",
        "arxiv-2610.12361-cited-but-not-consulted-a-counterfactual-audit-o.pdf",
        "**K416 — the citation is not the consultation.** Models justify legal decisions by **naming the "
        "statute or precedent**, and that naming is treated as evidence the decision follows from it. The "
        "audit substitutes the named authority for an **unrelated one**, holds the case facts fixed, and "
        "**decodes the verdict from hidden states** rather than waiting for the output. Across seven "
        "open-weight models (8B–70B) and four benchmarks spanning judicial and contractual reasoning, the "
        "verdict often does not track the swapped authority. Same lab as K415 (Lexsi Labs) and the same "
        "shape of finding: the **stated ground** and the **operative ground** are different things. "
        "Operator steal: **never accept a citation as proof of reliance** — perturb the cited authority "
        "and watch the decision, and prefer a hidden-state read over the model's own account of why. Pairs "
        "K415, K398 and K396. Research and audit framing only.",
        "concepts/compliance-verdict-rule-invariance.md",
        ["concepts/compliance-boundary-adjacent-pair-search.md",
         "concepts/faithful-agent-asr-measurement.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K416)")
    concept("compliance-verdict-rule-invariance",
        "A compliance verdict is not evidence the rule was read", "K415+K416",
        "2609.12313 / 2609.12361",
        "Two matched audits from the same lab, and they say the same thing from two directions.\n\n"
        "**K415:** perturb the **governing rule** — delete, swap, negate — with the case fixed. Mean "
        "**OCS-agg = 0.069**: only about **7%** of verdicts change, against ~90% baseline accuracy, with a "
        "permutation null near 0.5 and every p < 0.0001. On the **rule-necessary subset** the metric fires "
        "properly (**0.73–1.00**), so the tool works — it is the models that mostly do not use the rule. "
        "Detailed benchmarks move far more (**LegalBench 0.255, ContractNLI 0.318**) than a synthetic set "
        "(0.081), consistent with the synthetic cases being decidable from facts alone.\n\n"
        "**K416:** substitute the **cited authority** for an unrelated one, hold facts fixed, and decode "
        "the verdict from hidden states. The verdict often does not follow the swap. A model naming the "
        "right statute is not evidence it reasoned from that statute.\n\n"
        "The operator rule: **a citation is not a consultation, and a verdict is not proof the rule was "
        "applied.** Audit with a **rule perturbation**, report the rule-necessary subset separately, and "
        "where you can, read the decision from **hidden state** rather than the model's stated reason. Same "
        "family as K398 (adjacent-pair obligation boundaries) and K396 (report sensitivity, not one "
        "number).",
        ["sources/arxiv-2610-12313-verdict-without-the-rule-compliance-invariance.md",
         "sources/arxiv-2610-12361-cited-but-not-consulted-authority-swap-audit.md",
         "concepts/compliance-boundary-adjacent-pair-search.md",
         "concepts/guardrail-construct-validity-agent-eval.md",
         "concepts/faithful-agent-asr-measurement.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K415+K416)")

    # ---------- K417 ORCAGen ----------------------------------------------
    src("arxiv-2610-12415-orcagen-context-aware-malware-deception",
        "ORCAGen: orchestrating context-aware malware deception with RAG-guided generative AI",
        "2610.12415", "K417",
        "arxiv-2610-12415-orcagen-orchestrating-context-aware-malware-dece.pdf",
        "**K417 — deception instead of eviction.** Malware defenses normally remove or isolate a suspicious "
        "program as fast as possible. That contains the threat and **throws away the observation "
        "opportunity**. ORCAGen instead builds **context-aware deception playbooks** with RAG-guided "
        "generative AI, so the running sample keeps yielding attacker behaviour while being neutralised.\n\n"
        "**On 15 synthesized scenarios** (max 3 refinements) zero-shot deception success is **100%** for "
        "GPT-5.5 and Gemini 3.5 Flash, against **66.67%** (GPT-4o), **60%** (Claude Sonnet 4.5) and "
        "**26.67%** (Qwen3-Coder); refinement takes every model to **100%**, with **0 false positives and "
        "0 false negatives after validation**. On **150 real-world samples** (50 each of keyloggers, "
        "information stealers, ransomware, from ANY.RUN and VirusTotal, Mar-May 2026) complete "
        "neutralisation is **92% / 100% / 96%** with deception failure of 8% / 0% / 2%.\n\n"
        "The ablation is the useful part: against **direct prompting** (0% zero-shot, 46.67% after five "
        "refinements) and **RAG-enhanced prompting** (53.33% → 73.33%, then flat), the structured "
        "orchestration is what produces reliable playbooks — and it is **lightweight and deterministic at "
        "runtime**, with ~**27.69 ms** overhead and **zero hallucinated APIs** for the strongest models. "
        "Operator steal: **removing a sample is a containment decision, not an intelligence decision** — "
        "when the goal is learning the attacker, deception preserves the observation. Defensive lab only. "
        "**No malware payloads, playbook bodies, or generated code in wiki.**",
        "concepts/context-aware-malware-deception-playbooks.md",
        ["concepts/deception-aware-honeypot-ai-pentesters-rouxii.md",
         "concepts/agent-decoy-defense-autonomous-pentest.md"],
        wire=".cursor/rules/cemini-cybersec-lab-redteam.mdc (K417)")
    concept("context-aware-malware-deception-playbooks",
        "Deception preserves the observation an eviction destroys", "K417", "2610.12415",
        "Standard malware response optimises for **containment**: remove or isolate at once. It works, and "
        "it discards the chance to watch the attacker. ORCAGen takes the other branch — generate a "
        "**context-aware deception playbook** for the specific sample so it keeps running under control.\n\n"
        "The striking result is that this is now cheap: **100% zero-shot deception success** on the "
        "strongest models against 60-67% for weaker ones, **92-100% complete neutralisation** on 150 "
        "real-world samples, and refinement closes the gap to 100% within a handful of rounds. The "
        "ablation shows why structure matters — direct prompting manages **0% zero-shot**, and "
        "retrieval-augmented prompting plateaus around 73%, while the orchestrated form is reliable **and "
        "deterministic at runtime** (~28 ms).\n\n"
        "Operator rule: **'remove the sample' and 'learn from the sample' are different decisions** — pick "
        "deliberately, and when you choose to learn, a generated playbook is now a practical tool rather "
        "than a research demo. Pairs the Rouxii deception-aware-honeypot line. Defensive lab only.",
        ["sources/arxiv-2610-12415-orcagen-context-aware-malware-deception.md",
         "concepts/deception-aware-honeypot-ai-pentesters-rouxii.md",
         "concepts/agent-decoy-defense-autonomous-pentest.md"],
        ".cursor/rules/cemini-cybersec-lab-redteam.mdc (K417)")

    # ---------- K413 image-generator misinformation -----------------------
    src("arxiv-2610-11112-false-claims-credible-images",
        "False claims, credible images: a red-teaming benchmark for commercial image generators",
        "2610.11112", "K413",
        "arxiv-2610-11112-false-claims-credible-images-a-red-teaming-bench.pdf",
        "**K413 — the model knows the claim is false and renders it anyway.** The paper names a "
        "**verification-generation gap**: a commercial image model can label a claim as misinformation "
        "under verification and still produce it as **credible visual evidence**. The numbers make the gap "
        "explicit — **FCR (false-claim rejection) = 100.00% while ASR = 77.01%** on GPT-Image-2 (delta "
        "+22.99) and **100.00% vs 55.82%** on Nano Banana 2 (delta +44.18). Knowing is not acting.\n\n"
        "**EPIREAL-BENCH** is 10,000 verified prompts and 10,000 selected images over 10 claim categories "
        "and 10 credible visual formats; **EPIREAL-ATTACK** is a skill-guided black-box search over a "
        "Pareto set of validity / misinformation realization / visual credibility. Direct prompting "
        "already yields **above 70% average ASR** (GPT-Image-2 77.01, Grok Imagen 2.0 89.43, Seedream 5.0 "
        "Flash 73.20, Nano Banana 2 55.82); the attack pushes every model past **95%**. Input-level "
        "filters do not hold — keyword filter, NSFW classifier, and a prompt checker all sit under 38% "
        "interception on every model.\n\n"
        "**The constructive result:** **Verification-Guided Prompting (VGP)** — ask the same model to "
        "check the claim before generating it, with **no retrieval and no weight change** — lifts "
        "interception from 10.70% to **76.20%** (GPT-Image-2) and 32.40% to **93.00%** (Nano Banana 2). "
        "Benign factual prompts still resolve at 92.8-99.1%. Repo `github.com/Ye-ze-yu/EpiReal-Bench`; "
        "licence not stated. Operator steal: **a capability the model demonstrably has in one mode is not "
        "a control in another** — if you need the check to bind, make it a step in the pipeline. Pairs "
        "K415/K416 (the same stated-versus-operative gap) and the deepfake-detection line. **No "
        "misinformation prompts or generated examples in wiki.**",
        "concepts/verification-generation-gap.md",
        ["concepts/compliance-verdict-rule-invariance.md",
         "concepts/armor-plusplus-agentic-deepfake-detector-attacks.md"],
        wire=".cursor/rules/cemini-cybersec-agent-audit.mdc (K413)")
    concept("verification-generation-gap",
        "Knowing a claim is false is not refusing to render it", "K413", "2610.11112",
        "A model can **verify** that a claim is misinformation and still **generate** it as credible visual "
        "evidence. The measured gap is stark: **FCR 100.00% against ASR 77.01%** on one commercial "
        "generator, **100.00% vs 55.82%** on another. The capability exists; it simply does not gate the "
        "output.\n\n"
        "This is the third instance in this wiki of the same shape — K415 (a compliance verdict invariant "
        "to the rule) and K416 (a citation that is not a consultation). **Stated knowledge and operative "
        "behaviour are different objects**, and the instrument that reveals the difference is a "
        "**perturbation**, not the model's own account.\n\n"
        "The constructive finding is that the gate can be made to bind: **asking the same model to verify "
        "before generating**, with no retrieval and no weight change, took interception from 10.70% to "
        "**76.20%** and from 32.40% to **93.00%** on two models, at no cost to benign prompts (92.8-99.1%). "
        "Operator rule: **do not assume a check the model can perform is a check that constrains it — put "
        "it in the pipeline as a step.**",
        ["sources/arxiv-2610-11112-false-claims-credible-images.md",
         "concepts/compliance-verdict-rule-invariance.md",
         "concepts/armor-plusplus-agentic-deepfake-detector-attacks.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K413)")

    # K416's own concept
    concept("citation-is-not-consultation",
        "A citation is not a consultation", "K416", "2610.12361",
        "Naming the statute is the cheapest way to make a legal answer look grounded, and it is treated as "
        "evidence that the decision follows from that statute. It is not. Substitute the cited authority "
        "for an **unrelated one**, hold the facts fixed, and decode the verdict from **hidden states**: "
        "across seven open-weight models (8B-70B) and four judicial / contractual benchmarks, the verdict "
        "often does not follow the swap.\n\n"
        "So a **stated ground** and an **operative ground** are different objects, and the model's own "
        "explanation is the wrong instrument for telling them apart. Audit with a **perturbation** — swap "
        "the authority and watch the decision — and prefer a hidden-state read over the model's account of "
        "why. Same shape as K415's rule-perturbation audit: both ask whether the thing the model says it "
        "used is the thing it actually used. Pairs K398 and K396.",
        ["sources/arxiv-2610-12361-cited-but-not-consulted-authority-swap-audit.md",
         "concepts/compliance-verdict-rule-invariance.md",
         "concepts/compliance-boundary-adjacent-pair-search.md",
         "concepts/faithful-agent-asr-measurement.md"],
        ".cursor/rules/cemini-cybersec-agent-audit.mdc (K416)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
