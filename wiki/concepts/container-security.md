---
title: Container + Kubernetes Security
type: concept
tags: [container, k8s, cloud-native]
keywords: [container, docker, kubernetes, k8s, escape]
related:
  - concepts/cloud-pentest.md
  - sources/container-security-overview-pt-1.md
  - sources/kubernetes-exploitation-introduction-cheatsheet.md
  - entities/people/joas-a-santos.md
maturity: draft
created: 2026-05-12
updated: 2026-05-12
---

## Relations

- @concepts/cloud-pentest.md
- @sources/container-security-overview-pt-1.md
- @sources/kubernetes-exploitation-introduction-cheatsheet.md
- @entities/people/joas-a-santos.md

## Raw Concept

Two corpus PDFs anchor (Container Security Overview + Kubernetes Exploitation Cheatsheet).

## Narrative

Container security = (1) hardening individual containers (image scanning, no privileged mode, non-root users, read-only FS, capabilities pruning, secrets handling), (2) container escape research (kernel CVEs, runc/containerd CVEs, namespace abuse, capability escalation), (3) Kubernetes-specific attacks (kubeconfig leakage, exposed kubelet, pod-spec abuse for lateral movement, namespace boundary breaks, RBAC misconfigurations, etcd access). Standard tools: kube-hunter, kube-bench, peirates, kubectl-who-can, Pacu (k8s extensions).
