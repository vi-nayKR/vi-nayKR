# Vinay K R

### Site Reliability / Platform Engineer · Linux · Go · Observability · Safe Delivery

Bengaluru, India · Open to SRE, platform engineering, and production engineering roles

[Portfolio](https://portfolio.vinaykr.workers.dev) · [LinkedIn](https://linkedin.com/in/vi-naykr) · [Email](mailto:vinayravindranatha@gmail.com)

I am a software engineer with 3+ years of enterprise experience delivering and debugging production-facing software across fintech and regulated gaming. I am now specializing in site reliability engineering: Linux operations, observable services, failure-aware delivery, and automation that makes systems easier to operate.

My public work follows an evidence-first rule: claims should be traceable to source, tests, CI, or a clearly labeled lab result. Independent projects are not presented as employer production experience.

## Selected reliability work

### [Homelab SRE Observability](https://github.com/vi-nayKR/homelab-sre-observability)

A reproducible reliability lab built around an instrumented Go service, Prometheus, Alertmanager, Grafana, Blackbox Exporter, and Node Exporter. It includes a starter 99.5% availability SLO, multi-window burn-rate alerts, failure injection, runbooks, game-day procedures, a postmortem template, and CI that proves failure and recovery paths.

### [Medha Platform Infrastructure](https://github.com/vi-nayKR/medha-platform-infra)

Operations material for a two-node, systemd-managed Docker runtime: role-separated services, Nginx, nftables, PostgreSQL, Redis, SeaweedFS, verified backups, health-gated cutovers, and rollback procedures. Historical Kubernetes and GitOps definitions remain labeled as prior design material.

### [Medha Platform API](https://github.com/vi-nayKR/medha-platform-api)

A domain-driven Go modular monolith with PostgreSQL/PostGIS, Redis-backed real-time communication, S3-compatible storage, versioned migrations, structured request logging, dependency-aware health checks, rate limits, startup retries, and graceful shutdown.

## Current operating toolkit

```text
Systems:       Linux, systemd, SSH, nftables, Nginx, process supervision
Containers:    Docker, Compose; Kubernetes/Kustomize/Argo CD lab material
Observability: Prometheus, Alertmanager, Grafana, Blackbox Exporter, SLOs
Data:          PostgreSQL/PostGIS, Redis, SeaweedFS/S3-compatible storage
Automation:    Go, Bash, GitHub Actions, operational validation scripts
Foundation:    Angular, TypeScript, Node.js, C#/.NET, SQL, Cypress
```

## What I am building next

- Kubernetes reliability game days: probes, disruption, saturation, rollback, and incident evidence.
- A Terraform AWS reliability baseline with safe defaults, validation, and cost boundaries.
- A Linux operations toolkit for repeatable host diagnostics, backup verification, and recovery drills.

## Professional foundation

At Light & Wonder and Liminal Custody, I worked on enterprise application delivery, testing, API integration, authentication and authorization, data-backed workflows, and production debugging. That software engineering foundation now informs how I approach operability: make failure visible, automate verification, document recovery, and avoid claims the evidence cannot support.

## Research

Co-author of “Data Visualisation of Time Tradable Assets Using Machine Learning,” published through IEEE in 2023.
