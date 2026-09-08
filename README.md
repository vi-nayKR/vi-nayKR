<div align="center">
  <p><samp>FULL STACK / APPLIED AI / RELIABILITY</samp></p>
  <h1>Vinay K R</h1>
  <p><strong>Software engineer · Bengaluru, India</strong></p>
  <a href="https://portfolio.vinaykr.workers.dev/">
    <img src="./vinay-ascii-portrait.png" width="280" alt="Vinay K R — black-and-white ASCII character portrait" />
  </a>
  <p><strong>I build the interface, the API, and the systems that keep them useful.</strong></p>
  <p><samp>Angular · TypeScript · Go · Python · Linux</samp></p>
</div>

<p align="center">
  <a href="https://portfolio.vinaykr.workers.dev/"><strong>Portfolio</strong></a> &nbsp;·&nbsp;
  <a href="https://portfolio.vinaykr.workers.dev/#resume"><strong>Resume</strong></a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/vi-naykr"><strong>LinkedIn</strong></a> &nbsp;·&nbsp;
  <a href="mailto:vinayravindranatha@gmail.com"><strong>Email</strong></a>
</p>

<p align="center">
  <a href="#selected-work">Selected work</a> ·
  <a href="#professional-experience">Experience</a> ·
  <a href="#engineering-toolkit">Toolkit</a> ·
  <a href="#education--research">Research</a>
</p>

---

## What I bring

I'm a software engineer with nearly three years of professional experience across fintech and regulated gaming. My work connects typed product interfaces, data-backed services, applied AI, and observable infrastructure.

- **Product engineering:** Angular and TypeScript interfaces, authorization and approval workflows, real-time updates, and APIs backed by relational data.
- **Applied AI:** Python services that make agent routing, retrieval, streaming, caching, and evaluation inspectable.
- **Reliability:** Instrumented services, actionable alerts, failure diagnosis, and recovery procedures exercised in reproducible labs.

I care about what happens after a feature works: how it behaves under failure, how someone diagnoses it, and how a change can be rolled back.

## Selected work

### 01 / Product systems

**[Medha Platform API](https://github.com/vi-nayKR/medha-platform-api)** · `Go` `PostgreSQL / PostGIS` `Redis` `WebSockets`

A domain-driven backend for event scheduling, location-based discovery, and real-time messaging. The implementation brings together separated domain modules, spatial queries, authentication, Redis-backed message delivery, and operational health checks.

**Explore:** [Architecture](https://github.com/vi-nayKR/medha-platform-api/blob/main/architecture.md) · [System design](https://github.com/vi-nayKR/medha-platform-api/blob/main/system_design.md) · [Backend source](https://github.com/vi-nayKR/medha-platform-api/tree/main/internal)

The frontend side of my work is also visible in **[Portfolio-Ng](https://github.com/vi-nayKR/Portfolio-Ng)**, the Angular and TypeScript source for my [live portfolio](https://portfolio.vinaykr.workers.dev/).

### 02 / Applied AI

**[FastAPI Agent Patterns](https://github.com/vi-nayKR/fastapi-genai-agent-patterns)** · `Python` `FastAPI` `LangGraph` `OpenTelemetry`

A reference implementation of typed agent routing, checkpointed human approval, server-sent event streaming, and Redis caching. Deterministic default workers make the control flow testable without a model key; tracing connects API requests, agent runs, and cache operations.

**Explore:** [Implementation](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/tree/main/src) · [Tests](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/tree/main/tests) · [Design notes](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/tree/main/docs)

**[Agentic RAG Platform](https://github.com/vi-nayKR/enterprise-agentic-rag-platform)** explores hybrid retrieval, reciprocal rank fusion, relevance grading, query rewriting, and answers with citations.

<sub>Both AI repositories are archived personal reference projects. The RAG platform is a prototype.</sub>

### 03 / Reliability and platform engineering

| Project | Engineering focus | Explore |
| --- | --- | --- |
| **[Homelab SRE Observability](https://github.com/vi-nayKR/homelab-sre-observability)** | Instrumented Go service, Prometheus SLOs and burn-rate alerts, Grafana dashboards, probes, and recovery drills. | [Architecture](https://github.com/vi-nayKR/homelab-sre-observability/blob/main/docs/ARCHITECTURE.md) · [Runbooks](https://github.com/vi-nayKR/homelab-sre-observability/tree/main/runbooks) |
| **[Kubernetes Reliability Game Days](https://github.com/vi-nayKR/kubernetes-reliability-gamedays)** | Seven bounded exercises covering cutovers, failed rollouts, dependency failures, memory limits, and PDB-governed worker drains. | [Exercises](https://github.com/vi-nayKR/kubernetes-reliability-gamedays/tree/main/gamedays) · [Postmortem](https://github.com/vi-nayKR/kubernetes-reliability-gamedays/blob/main/postmortems/2026-08-24-worker-drain-endpoint-race.md) |
| **[Terraform AWS Reliability Baseline](https://github.com/vi-nayKR/terraform-aws-reliability-baseline)** | Two-AZ infrastructure design, budget notifications, an optional ECS/ALB path, mocked-provider plans, and policy checks. | [Architecture](https://github.com/vi-nayKR/terraform-aws-reliability-baseline/blob/main/docs/ARCHITECTURE.md) · [Cost boundary](https://github.com/vi-nayKR/terraform-aws-reliability-baseline/blob/main/docs/COST_BOUNDARY.md) |

<sub>These are personal labs with documented evidence boundaries. Terraform validation uses a mocked AWS provider; a live AWS deployment has not been demonstrated. Professional experience is described separately below.</sub>

## Professional experience

**Liminal Custody · Software Engineer, Full Stack**<br />
Nov 2025 – Mar 2026 · Bengaluru

- Built Angular policy-configuration and approval flows for transaction risk, transfers, address lists, and wallet groups.
- Implemented backend rule evaluation and data models with cached evaluation and external address-risk integration.
- Worked on organization-scoped authorization, quorum approvals, and role-based access controls across frontend and backend.

**Light & Wonder · Senior Associate Software Engineer**<br />
Aug 2023 – Jul 2025 · Bengaluru · Promoted from Associate Software Engineer

- Built and modernized Angular interfaces for financial, player-management, and device-facing workflows, integrated with C#/.NET APIs and SQL Server.
- Delivered real-time UI updates with RxJS and WebSockets; resolved a subscription lifecycle leak affecting long-running devices.
- Implemented audit-data capture and reporting workflows, with Cypress end-to-end regression coverage.

**Light & Wonder · Full-Stack Intern**<br />
Mar 2023 – Jul 2023 · Bengaluru

- Built a game recommendation system with Angular, C#/.NET Core, REST APIs, and SQL Server during a 16-week internship.

## Engineering toolkit

| Area | Technologies and practices |
| --- | --- |
| **Interfaces** | Angular, TypeScript, RxJS, reactive forms, HTML, CSS, WebSockets |
| **Services** | Go, Python / FastAPI, Node.js / Express, C# / .NET, REST APIs, authentication, RBAC |
| **Data** | PostgreSQL, PostGIS, SQL Server, Redis, relational modeling, caching |
| **Applied AI projects** | LangGraph, RAG, hybrid retrieval, RRF, SSE, semantic caching, evaluation |
| **Platform labs** | Linux, systemd, Docker, Kubernetes / kind, Kustomize, Terraform, Ansible |
| **Quality and operations** | Cypress, GitHub Actions, OpenTelemetry, Prometheus, Grafana, Alertmanager, SLOs, runbooks |

## Education & research

**B.E. in Computer Science · Siddaganga Institute of Technology**<br />
2019 – 2023 · **CGPA: 8.65/10**

Co-author of **[Data Visualisation of Time Tradable Assets Using Machine Learning](https://ieeexplore.ieee.org/document/10275962)**, published through IEEE.<br />
DOI: `10.1109/NCNSP56992.2023.10275962`

---

<p align="center">
  <strong>Have a product, an API, or a reliability problem to work through?</strong><br />
  <a href="mailto:vinayravindranatha@gmail.com">vinayravindranatha@gmail.com</a> ·
  <a href="https://portfolio.vinaykr.workers.dev/#resume">View my resume</a>
</p>

<p align="center">
  <sub>Terminal-inspired visual roots: <a href="https://github.com/Andrew6rant">Andrew Grant</a>. Portrait and profile content are original.</sub>
</p>
