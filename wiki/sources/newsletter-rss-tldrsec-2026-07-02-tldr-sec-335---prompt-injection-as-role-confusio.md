---
title: tl;dr sec — [tl;dr sec] #335 - Prompt Injection as Role Confusion, PHP Ecosystem Security, New MCP Spec
type: source
tags: []
keywords: []
related: []
maturity: draft
created: 2026-07-05
updated: 2026-07-05
cross-wiki-source: @osint-wiki/sources/newsletter-rss-tldrsec-2026-07-02-tldr-sec-335---prompt-injection-as-role-confusio.md
---

# tl;dr sec — [tl;dr sec] #335 - Prompt Injection as Role Confusion, PHP Ecosystem Security, New MCP Spec

## Relations

- @osint-wiki/sources/newsletter-rss-tldrsec-2026-07-02-tldr-sec-335---prompt-injection-as-role-confusio.md  (cross-wiki source)

## Raw Concept

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-tldrsec-2026-07-02-tldr-sec-335---prompt-injection-as-role-confusio.md` during ingest.
What prompted this page + which sources synthesize into it — fill in on next
ingest pass.

## Narrative

Hey there,

 I hope you’ve been doing well!

  👰 🤵 Wedding

  This past weekend I attended a friend’s wedding, and it was heartwarming.

 The couple have been together over a decade, and had many fun stories to share from their time in college, to adventures on the East and West Coasts.

 There was a welcome party the night before at a local brewery, and it just so happened that the local Hells Angels chapter decided to have an event… at the same time and venue 😂 

 So it was half people dressed in wedding semi-formal attire celebrating love, and half Harleys, chains, black shirts, and whole arm tattoos. I subtly took a photo of one man wearing a shirt that said, “Every normal man must be tempted, as times, to spit on his hands, hoist the black flag, and begin slitting throats. -H.L. Mencken.” You know, chill stuff.

 At one point there was a motorcycle burnout that caused a big cloud of smoke, I think honoring someone who had passed. My friend said if no one does a burnout at his funeral he’ll be very disappointed.

 I enjoyed getting to meet the couple’s family and more of their friends, that gives you such an interesting view into their lives and who they’ve been over time.

 And I’ll never forget the joy of me dancing around my friend who adamantly doesn’t dance, except at EDM raves.

 It was nice to have a weekend offline, connecting with people, instead of being terminally online and “yOu’LL NeVeR b3lieVe WHat <model | open source repo> jUsT DroPPed?!11!”



    Sponsor

 📣    What Jamf changed to stop drowning in
 IT tickets

  500+ SaaS apps. Thousands of devices. A flood of help desk tickets. And a team of 30 people to manage all of it.

 That's the reality for Jamf's IT team - but instead of drowning, they built their way out. We're bringing them live on July 10th to show you exactly how they replaced manual, ticket-based IT work with intelligent workflows.

  Tune in to hear:

    The early use cases  that proved the value of intelligent workflows at Jamf

    Where AI fits into ITOps today  - and where it's going

   How they compressed  a year-long device audit into a matter of weeks

    👉    Register now!    👈

  Semgrep found automating a number of workflows with Tines quite helpful 👍️ 



 AppSec

   Quicklinks

    badkeys/badkeys  - Tool by  Hanno Böck  that checks cryptographic public keys for known vulnerabilities.

     Escape benchmarked Claude Opus 4.8 vs. their multi-agent multi-model pentesting harness on 4 apps  ,   Aikido and XBOW via Doyensec's numbers. On real apps with no public writeups, the harness found 4x more than the raw model. On severity-weighted score, it also led on both real apps.*

    Factoring "short-sleeve" RSA keys with polynomials  - Trail of Bits's Keegan Ryan  discovered hundreds of vulnerable "short-sleeve" RSA and DSA keys in the wild where private key bits were heavily biased toward 0 in regular patterns, and developed a polynomial-based factorization technique that exploits the regular structure of zero blocks to quickly recover 603 RSA and 74 DSA private keys.

    *Sponsored



  Vulnerability Reports Are Not Special Anymore
 Filippo Valsorda  argues that LLMs have changed how vulnerability reports should be perceived. For years, reports were treated as special because researchers provided scarce insight into where bugs lived and confidentiality long enough to ship a fix before an exploit. In 2026, LLMs find issues about as well as most security researchers, and anyone can run them. The bottleneck is no longer finding potential issues but assessing which ones are real and which actually affect users. Without an existing trust relationship, external reports add little to that triage, since picking through an LLM's output and picking through a  security@  inbox have roughly the same signal-to-noise. Confidentiality matters less for the same reason, since attackers can run their own LLMs and probably hit the same triage bottleneck as defenders. Valsorda believes that triage, rapid remediation, and prevention are the actual job now.



  We have Mythos at Home: GLM 5.2 beats Claude in our Cyber Benchmarks
Semgrep’s  Katie Paxton-Fear ,  Seth Jaksik ,  Brenden Noblitt , and  Erik Buchanan  benchmarked GLM 5.2, an open-weight model from Zhipu AI, against their IDOR detection dataset using only a basic Pydantic AI harness and prompt, finding it achieved 39% F1 score and beat Claude Code (32%) at roughly $0.17 per vulnerability found, though it still trailed Semgrep's multimodal pipeline with endpoint discovery scaffolding (53-61% F1, top with GPT 5.5).

 💡 I like posts comparing various models and vanilla models vs model + harnesses. It’d be interesting to know more about the dataset though- languages/frameworks in use, how many examples, etc.



  Snyk VulnBench JS 1.0: Can LLMs Find the Same Bugs Twice?
Snyk's  Liran Tal  describes evaluating Snyk’s VulnBench JS 1.0 (10 JavaScript fixtures with 44 Snyk Code reference findings, each a small Express-based application) across 300 vulnerability scans on (10 fixtures × 6 configurations × 5 repetitions) to measure LLM security review repeatability against Snyk Code SAST as a deterministic reference. As you’d expect, the post found results vary across different LLM-only scans.

 💡 This kind of felt like a puff piece. Of course a deterministic static analysis scan in this setup will be a) faster and b) more consistent than an LLM-based approach. Also, it’s no surprise that a product performs well on simple, small applications it was already tested on. A more representative benchmark would be testing on complex, real-world applications, or at least ones that the product hasn’t already been tuned on. If they released the benchmark apps + reproduction code that would be cool though.



    Sponsor

 📣  Clear your vulnerability queue

   Inbox zero for vulnerabilities sounds like a fantasy. Your SCA and SAST scanners flag thousands of findings: dependencies your app never calls, code paths an attacker can't reach.

  Maze Code is like if inbox zero was a thing for your code vulnerabilities. Maze investigates every finding across your code and dependencies, with context from code and cloud: is the vulnerable function reachable, does the package survive the build, is it exposed at runtime. The findings that aren't exploitable get closed with a reason for your auditors. For the ones that are risky, our agents write a fix and route it to the developer who owns that code.

   👉     Meet Maze Code     👈

   I like the product screenshots, it seems like they gather app-relevant context thoughtfully.



 Cloud Security

   Some notes on Lambda MicroVMs
 Aidan Steele  shares hands-on notes on AWS Lambda MicroVMs, a generalisation of Lambda functions that run code in a fresh VM for up to 8 hours. The shell side is a first-class capability since MicroVMs support PTYs natively with shell access through a dedicated AWS API, and inside the VM you can run Docker containers with full OS capabilities. Networking gets its own abstraction called a Lambda Network Connector, a configuration packaging subnets, security groups, and an IAM role for ENI management under its own ARN. The connectors create ENIs in your VPC but hide them by default unless a specific flag is set on the describe call, and AWS has placed resource-based policies on the ENIs so only the Lambda service can mutate them, closing off the old trick of attaching an elastic IP to a Lambda ENI for VPC-attached internet access.



  Holding blobs for ransom: Four methods for Azure Storage ransomware
Datadog's  Jonah Feldman  describes four techniques ransomware actors use against Azure Blob Storage, all encrypting victim data with keys the attacker controls. Client-side encryption and encryption scope abuse have been observed in the wild by BlackCat's Sphynx encryptor and STORM-0501 respectively, while customer-provided keys (CPK) and storage service encryption with customer-managed keys (CMK) remain theoretical but viable. He shows how attackers circumvent Azure's soft-delete protections with cross-tenant CMK configurations and federated identity credentials, placing the key vault in their own tenant so recovery requires paying ransom.

 The post includes Azure Activity, storage resource, and Key Vault event codes for detection, though CPK and encryption scope usage look like normal PutBlob requests in storage logs. Azure Defender for Storage adds threat detection across storage accounts, and three new Stratus Red Team techniques emulate CPK, encryption scopes, and CMK abuse for defense testing.

 For prevention, Feldman recommends immutability and versioning to block the download-encrypt-reupload pattern in client-side encryption and CPK, avoiding long-term credentials like SAS tokens with persistent data-plane access, and flagging cross-tenant CMK configurations to catch the bypass.



   Supply Chain

   indoor47/gh-workflow-hardener
Tool by  Dmytro  which scans GitHub Actions workflows for supply-chain risks like unpinned action references vulnerable to tag rewrites, overly broad permissions, and script injection from unsanitized PR inputs. The tool ships as a CLI, GitHub Action, VS Code extension, and hosted API, with an auto-fix mode that resolves action tags to commit SHAs.

 💡 Seems less mature than  zizmor , but I like to collect similar tools for future feature comparisons.



  Vulnerability and malware checks in uv
Astral's  William Woodruff  announces two new security features for uv in preview. uv audit scans dependencies for known vulnerabilities and deprecated packages, running 4-10x faster than pip-audit on typical projects by working from uv's already-locked resolutions. The second feature is an opt-in malware scan enabled with UV_MALWARE_CHECK=1, which checks OSV for known malicious packages during uv add and uv sync operations and terminates the sync before malicious code has a chance to run.

 💡 Love to see new security features in popular dev tools 🤘 



  One Month of Ecosystem Security Engineering
The PHP Foundation's  Volker Dusch  details one month of ecosystem security engineering work, during which the team scanned over 300 of the most-downloaded Composer packages and nearly all major frameworks using AI models with extended Cyber capabilities for vulnerability discovery, triage, reproducer generation, impact analysis, and fix suggestions. The effort has produced nearly 100 publicly available fixes across the ecosystem so far, with one case where 200 repositories applied the same GitHub Actions fix via a central template.

 The infrastructure runs on  Scrutineer , an open-source tool the team is developing with Alpha-Omega and ecosystem security engineers from other languages. Scrutineer runs Claude Code skills against open-source repos through a configurable scan pipeline that combines static analysis, model-backed audits, and maintainer identification, with findings landing in a structured database and a guided triage-to-disclosure workflow that can isolate each scan in an ephemeral Docker container. Dusch reports that maintainer report quality has gone up over the past months because maintainers now run their own coding agents to validate findings, though models still refuse to help with exploit work on complex vulnerabilities, and PHP core itself produces worse results than userland libraries because a language runtime is harder for agents to reason about.

 💡 Based on this post, it seems like this mass AI-scanning and patching effort has been well received by the PHP community, which is great. Perhaps because findings have already been reviewed + come with patches, and the effort feels like it’s coming from the community (vs some external party)?



   AI + Security

   Prompt Injection as Role Confusion
Charles Ye, Jasmine Cui, and Dylan Hadfield-Menell detail their ICML 2026 paper on prompt injection as role confusion,  with code on GitHub . Prompt injection succeeds not because attackers find clever phr
