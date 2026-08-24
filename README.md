# Vinay K R

### Site Reliability / Platform Engineer · Linux · Go · Observability · Safe Delivery

Bengaluru, India · Open to SRE, platform engineering and production engineering roles

[Portfolio](https://portfolio.vinaykr.workers.dev) · [LinkedIn](https://linkedin.com/in/vi-naykr) · [Email](mailto:vinayravindranatha@gmail.com)

I am a software engineer with nearly three years across fintech and regulated gaming, now specializing in site reliability engineering. I build and operate Linux platforms, instrument services, automate safe change, test recovery and document incidents.

My public work is evidence-led: claims link to source, tests, public CI or a clearly bounded lab result. Independent exercises are not presented as employer production or on-call experience.

## Selected reliability work

### [Homelab SRE Observability](https://github.com/vi-nayKR/homelab-sre-observability)

An instrumented Go service with Prometheus, Alertmanager, Grafana and black-box probing. Versioned SLO and burn-rate rules, exact firing/resolved webhook assertions, runbooks and a completed postmortem are exercised in public CI.

### [Kubernetes Reliability Game Days](https://github.com/vi-nayKR/kubernetes-reliability-gamedays)

Seven automated failure/change scenarios on an ephemeral three-node kind cluster, including bad releases, dependency readiness, DNS policy, OOM and worker drain. The repository retains diagnosis, recovery, policy checks and a completed drain-race corrective action.

### [Linux Operations Toolkit](https://github.com/vi-nayKR/linux-operations-toolkit)

An Ansible baseline for Debian and Arch with SSH, nftables, time synchronization, bounded metrics, persistent verified backups and metadata-only diagnostics. Public CI requires strict second-run idempotence and successful recovery from six guarded Linux drills.

### [Terraform AWS Reliability Baseline](https://github.com/vi-nayKR/terraform-aws-reliability-baseline)

A cost-first Terraform design with Budget/SNS guardrails, default-off service resources, mocked plan tests and policy/security validation. It is deliberately labeled validation-only until a real budget-capped apply, health check and destroy are retained.

### [Medha Platform Infrastructure](https://github.com/vi-nayKR/medha-platform-infra) and [API](https://github.com/vi-nayKR/medha-platform-api)

A self-hosted two-node Debian platform running Go APIs, PostgreSQL, Redis and SeaweedFS behind Nginx and Cloudflare. The repositories cover systemd-managed Docker roles, nftables, dependency-aware health, guarded stateful cutover, rollback, backups, structured logging, timeouts and graceful shutdown. Historical Kubernetes/GitOps material is explicitly separated from the current runtime.

## Operating toolkit

```text
Systems:       Linux, systemd, journald, SSH, nftables, Nginx
Containers:    Docker, Compose, Kubernetes, kind, Kustomize, Argo CD
Observability: Prometheus, PromQL, Alertmanager, Grafana, black-box probing, SLOs
Automation:    Go, Bash, Ansible, Terraform, GitHub Actions
Data:          PostgreSQL/PostGIS, Redis, SeaweedFS/S3-compatible storage
Foundation:    Angular, TypeScript/Node.js, C#/.NET, SQL, Cypress
```

## Evidence boundaries

- The reliability repositories are bounded independent labs, not employer production systems.
- The AWS repository has not yet been applied to a real account.
- The live Medha runtime is systemd-managed Docker; its Kubernetes/Argo CD material is historical.
- I do not claim professional on-call, measured production MTTR reductions or unsupported benchmark numbers.

## Professional foundation

At Light & Wonder and Liminal Custody, I delivered and debugged application behavior across typed web clients, APIs, authentication/authorization, data-backed workflows, WebSockets, audit/reporting and regression automation. That application-code depth is the bridge I bring to reliability work.

## Research

Co-author of “Data Visualisation of Time Tradable Assets Using Machine Learning,” published through IEEE in 2023.
