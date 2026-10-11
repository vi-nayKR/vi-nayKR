<div align="center">

<img src="assets/medha-work.svg" alt="Proof of work at Medha Innovations: 754 commits across 10 private repositories, Feb to Oct 2026" width="100%">

</div>

## `// WHAT THIS IS`

I'm a founding engineer at **Medha Innovations**, which has two founders. Everything lives in the private
[`medha-innovations`](https://github.com/medha-innovations) GitHub org, so outsiders can't open the code.
This page is the evidence I *can* publish: my authored commits, counted straight from `git log`.

- **754 commits by me** in 10 repos, Feb – Oct 2026. Merge commits, CI bots, Dependabot and my co-founder's commits are excluded.
- GitHub attributes these commits to **@vi-nayKR**, so they also count toward my contribution graph as private contributions.
- Each SHA below is a real commit. I'm happy to share my screen and open any of them during an interview.

## `// REPOS`

| Repo | What I built | Stack | My commits / all | Active |
|---|---|---|---:|---|
| `medha-api` | Core backend: V2 API, OTP auth, multi-platform push, WebSockets, booking & assignment flows | Go · PostgreSQL · Redis | **385** / 680 | Feb – Aug 2026 |
| `medha-admin-panel` | Ops console: users, events, feed, storage, AI config, server & Docker monitoring, audit log | React · TypeScript · Bun | **108** / 113 | May – Aug 2026 |
| `medha-infra` | Production GitOps: k8s + Argo CD, two-node runtime, MinIO → SeaweedFS migration | k8s · Argo CD · Terraform | **82** / 123 | Jul – Oct 2026 |
| `medha-web` | Public site: landing page, live Panchanga API, Kannada localisation, SEO | React · Astro · TS | **62** / 69 | Jun – Sep 2026 |
| `medha-care` | Care platform built in phases: identity, scheduling & booking, visit records, clinician KYC gate | Rust · TypeScript | **34** / 36 | Sep 2026 |
| `medha-ios` | Native iOS app at parity with Android, with a real unit-test suite | Swift · SwiftUI · SwiftData | **26** / 26 | Jun – Jul 2026 |
| `medha-sahayak` | Realtime LLM booking assistant with grounding gate and a real-LLM baseline eval | Python · FastAPI | **16** / 18 | Oct 2026 |
| `medha-ops-assistant` | Offline engineering-docs QA with citations, measured eval, int8 reranker in 512 MiB | Python | **14** / 21 | Oct 2026 |
| `medha-android` | Dev/prod flavours, presigned-upload fix, auth fixes (app is mostly my co-founder's) | Kotlin | **14** / 360 | Jun – Aug 2026 |
| `medha-agent` | Specs, sprint stories, architecture & handoff docs for all repos | Markdown | **13** / 34 | Feb – Aug 2026 |

## `// COMMIT HIGHLIGHTS`

Picked from the log. The messages are verbatim; "…" marks where a long one was cut short.

**medha-api** · Go backend
| SHA | Date | Commit |
|---|---|---|
| `35cee70` | 2026-03-28 | feat(auth): implement OTP via MessageCentral; feat(notif): multi-platform push notifications … |
| `b2aaa63` | 2026-04-15 | feat(v2): add refresh token & logout endpoints, remove V1 swagger annotations |
| `1778f5c` | 2026-05-06 | refactor: finalize V2 API transition and remove V1 legacy code |
| `fc9cb0c` | 2026-05-20 | feat: implement Yajman-to-Pandith direct connections flow |
| `59ccc26` | 2026-06-07 | Optimize database queries, indexing, and production Docker configurations |
| `9968041` | 2026-07-01 | feat: implement singular admin-pushed assignment flow and remove connection requests flow |

**medha-infra** · platform
| SHA | Date | Commit |
|---|---|---|
| `dd4ca9d` | 2026-07-18 | feat: establish production GitOps infrastructure |
| `436c88b` | 2026-07-20 | chore(infra): migrate medha-web and medha-admin-panel frontends to k8s cluster |
| `b6b2e20` | 2026-08-07 | feat(stage-a): deploy SeaweedFS alongside MinIO, no cutover yet |
| `ce7994f` | 2026-08-07 | feat(stage-b): cut over from MinIO to SeaweedFS |
| `30c47f4` | 2026-08-20 | feat(infra): deploy synchronous two-node runtime |

**medha-sahayak / medha-ops-assistant** · applied AI
| SHA | Date | Commit |
|---|---|---|
| `ca7328b` | 2026-10-05 | feat: initial release of Medha Sahayak realtime AI booking assistant |
| `8d6f55c` | 2026-10-06 | feat(eval): add openai_compat provider and real-llm baseline evaluation |
| `09b9209` | 2026-10-06 | fix(eval): resolve honesty citations, count retries, log turns, and document limitations |
| `49b1674` | 2026-10-05 | Add offline cited engineering-document assistant and measured evaluation |
| `113371f` | 2026-10-06 | feat(retrieval): add budget-conscious int8 reranker fitting 512 MiB container |

**medha-care** · Rust platform
| SHA | Date | Commit |
|---|---|---|
| `a2647dd` | 2026-09-24 | backend(p1): public API and service catalog |
| `d8b7a13` | 2026-09-24 | backend(p2): identity profiles and provider review |
| `99800a6` | 2026-09-24 | backend(p3): scheduling and booking |
| `8f12e27` | 2026-09-26 | feat(kyc): add 3-step clinician statutory verification gate and pure-Rust KMC QR automated verification |

**medha-ios / medha-admin-panel / medha-web** · clients
| SHA | Date | Commit |
|---|---|---|
| `14edb59` | 2026-07-21 | Implement Phase 1, 2, and 3: Core infrastructure (MedhaDataStore, MedhaSecurity), Networking client and DTOs (MedhaNetwork), and SwiftData database models … with complete unit test suites passing. |
| `56d4d42` | 2026-07-22 | Fix cert pinning blocking all API/WebSocket traffic, profile post grid/preview, and banner consistency |
| `a9b5b2e` | 2026-06-07 | feat: add docker monitoring, websockets, and project documentation |
| `7297f92` | 2026-07-09 | feat(admin): implement console security, settings manager, log audit timeline, and layout improvements |
| `bc881a6` | 2026-07-30 | feat: add end-to-end Kannada language localization and digit formatting |

## `// HOW THE NUMBERS ARE MADE`

`git log --all --no-merges` over my local clones of every org repo. A commit counts only if I authored it, under any of my
git identities. Line counts are left out on purpose, because vendored corpora and generated Swagger specs would inflate them.

<div align="center">

[← back to profile](README.md) &nbsp;·&nbsp; `want a live code walkthrough?` [say hi](mailto:vinayravindranatha@gmail.com)

</div>
