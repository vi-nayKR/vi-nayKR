# GitHub revamp plan — Vinay K R

## Execution status — 27 September 2026

- GitHub profile copy, bio/social link, and six pins are updated. The first week’s claim corrections, research frontend CI repair, and Appointment Review CI/metadata are published. The latest Agent Patterns and ReconcileAI runs pass on their published commits.
- ReconcileAI has a no-key fictional sample walkthrough and screenshot, a frozen synthetic benchmark manifest, item/evidence scoring, and upload rejection/cleanup checks. Gemini calls now have a configurable 60-second SDK timeout with retries disabled; tests cover timeout failure persistence, startup recovery, and missing-evidence review. The 19-test local suite and [CI on commit `f692ac6`](https://github.com/vi-nayKR/multimodal-document-intelligence/actions/runs/36268827492) pass. A live held-out report still needs a Gemini key; the user has none yet. Independent document review and three usability sessions remain.
- Agent Patterns fixture reporting and citation grading are corrected. Agent and cache routes now require reviewer authentication and server-assigned tenant scope. PostgreSQL checkpoint recovery across a fresh app instance, cross-tenant denial, and post-completion approval replay rejection pass locally and in [CI](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/actions/runs/36268033678). A sanitized fixture trace covers retrieval, approval pause/resume, and synthetic timeout failure; live-provider quality remains unmeasured because no provider key is available. The sample performs no external mutations.
- Medha’s reading path and claim boundaries are corrected. The PostgreSQL test forces competing bookings and a trigger-induced rollback; Go race tests and [CI](https://github.com/vi-nayKR/medha-platform-api/actions/runs/36267192789) pass. The README states the exercised invariant and limits, including the post-commit match update recovery gap.
- LinkedIn headline, About, ReconcileAI project, experience (including Medha from March 2026), and education are updated. LinkedIn did not generate previews for GitHub/portfolio Featured links. An X account does not yet exist, so X changes remain pending.
- A tested strict-checkpoint workaround was contributed to [LangGraph issue #7847](https://github.com/langchain-ai/langgraph/issues/7847#issuecomment-5849413260); maintainer follow-up is pending. Independent reviewers/usability sessions and live-provider outcome evidence remain open. This status records completed work; it does not turn the 12-week schedule into a finished result.

Audit date: **26 September 2026**. Primary account: [vi-nayKR](https://github.com/vi-nayKR).

**Recommendation: position yourself as an Applied AI engineer who can build the product, enforce business rules, and operate the backend.** Make ReconcileAI the lead project, Medha Platform API the engineering foundation, and FastAPI Agent Patterns the workflow reference.

Your existing work gives you enough material. The next improvement should be stronger evidence, clearer claims, and a faster route to the best work. “Top 1%” is an aspiration, not a percentile this audit can establish. The practical target is a profile that a hiring engineer can understand in 30 seconds and investigate successfully in 10 minutes.

This is a plan and proposed copy. The audit used authenticated `gh` reads, public source files, repository trees, Actions results, and the rendered GitHub profile. It did not run the applications or live model evaluations. LinkedIn and X accounts were not audited; their recommendations below are the follow-on strategy. Professional experience and employment outcomes remain self-reported. Planning assumes **8–10 hours per week for 12 weeks**, with Applied AI as the default role priority.

## 1. What your GitHub currently communicates

### What is already working

- The profile has a coherent AI/full-stack introduction, portfolio and resume links, professional history, research, and project links.
- ReconcileAI has a concrete user workflow, typed extraction, decimal reconciliation, correction handling, and an explicit statement that live model quality is unmeasured.
- FastAPI Agent Patterns has real implementation depth and a successful CI run at the inspected default-branch commit, including linting, types, tests, Redis integration, and a cache benchmark.
- Medha has a public backend reference and an organization showcase that discuss contribution boundaries. Preserve that attribution.
- The SRE lab contains a documented alert lifecycle and recovery exercise, which is useful supporting evidence for operating software.
- Appointment Review already includes desktop/mobile screenshots and documents its scheduling rules and limitations. Reuse this presentation pattern for the AI projects.

### Highest-impact gaps

| Priority | Observed evidence | Recommended change | Completion evidence |
| --- | --- | --- | --- |
| P0 | ReconcileAI is linked first in the README but absent from the six pins. An archived evaluation prototype occupies a pin. | Pin ReconcileAI first; remove the archived prototype from pins. | Public profile shows the intended order. |
| P0 | The RAG README claims “zero-hallucination,” +34% recall, and continuous quality evaluation. Its inspected evaluator implements token-overlap heuristics; no Actions runs or committed benchmark report were returned in the audit. | Correct the claims and remove it from featured placement pending a source-to-claim audit. | README distinguishes implemented behavior, proposed architecture, and unmeasured targets. |
| P0 | Agent Patterns' report says hybrid retrieval outperforms lexical, but its table shows lexical MRR **0.9773** versus hybrid **0.9545**; both have Recall@3 of 100%. | Fix the report generator's unconditional “Hybrid Advantage” statement, then regenerate the report. | A regression check catches reversed comparisons; generated prose agrees with the table. |
| P0 | The research project's latest CI at `716c498c` fails during frontend dependency installation. The error says `npm ci` needs a usable lockfile. Recent successful runs are “Keep Streamlit Alive.” | Check the frontend working directory and lockfile; commit a valid matching lockfile and pass the actual CI workflow. | Successful build at the new default-branch SHA, with a CI badge linked to that workflow. |
| P1 | ReconcileAI's tree contains evaluation code and a 50-case generator, but no committed live evaluation report or visual demo assets. | Publish a real-provider baseline, screenshot, and short walkthrough. | Versioned report with failures, configuration, and reproducible commands; actual product images. |
| P1 | The profile's initial desktop view is text-heavy. Six long project rows, extensive experience, and a broad stack push the native pins down the page. | Reduce the profile to a short introduction, three featured projects, a compact stack, and links to deeper evidence. | A reader can identify your role and best project without reading the full resume. |
| P1 | Appointment Review has no description, topics, homepage, or detected license; a workflow file exists but the API returns zero runs. | Add accurate metadata, decide reuse terms, and establish a successful run before promotion. | Useful About panel and a verified run at the current commit. |
| P1 | GitHub social accounts API returns an empty list. LinkedIn is only linked inside the README; no X username is configured. | Add the existing LinkedIn URL to profile social links; add X after confirming the real handle. | Public links resolve to your actual profiles. |
| P2 | The archived inference gateway still advertises throughput/cost numbers. Its benchmark prints a fixed **62.5%** saving rather than calculating it from billing measurements. | Correct or explicitly withdraw unsupported historical claims while keeping the repository archived. | An archive notice and clearly labeled measured, simulated, or unmeasured figures. |

The public inventory contains **16 repositories: 10 active and 6 archived**. All 16 showed zero stars at audit time. Stars are a discovery signal, not a quality gate; optimize first for people successfully inspecting and using the work.

### Evidence links for the critical findings

- [Profile README at the audited commit](https://github.com/vi-nayKR/vi-nayKR/blob/fea603722031d074a8acc3dd7cd165dd0f8389c9/README.md).
- [ReconcileAI README](https://github.com/vi-nayKR/multimodal-document-intelligence/blob/d2e1f62a2ae15bb1ccf9bae60e711152a1f7eb92/README.md), [evaluation runner](https://github.com/vi-nayKR/multimodal-document-intelligence/blob/d2e1f62a2ae15bb1ccf9bae60e711152a1f7eb92/scripts/run_reconciliation_eval.py), and [successful deterministic CI](https://github.com/vi-nayKR/multimodal-document-intelligence/actions/runs/35391573470).
- [Agent Patterns report](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/blob/62cefcbcd11c0ee716442b60ae5ae2198279bf80/evals/reports/benchmark_v1_report.md), [report generator and grading logic](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/blob/62cefcbcd11c0ee716442b60ae5ae2198279bf80/evals/evaluator.py), and [successful CI](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/actions/runs/35391261470).
- [RAG claims](https://github.com/vi-nayKR/enterprise-agentic-rag-platform/blob/0bdd4993e9f05b4c95461e1df11e6401fa2152aa/README.md), [heuristic evaluator](https://github.com/vi-nayKR/enterprise-agentic-rag-platform/blob/0bdd4993e9f05b4c95461e1df11e6401fa2152aa/src/evals/metrics.py), and [in-process MCP client](https://github.com/vi-nayKR/enterprise-agentic-rag-platform/blob/0bdd4993e9f05b4c95461e1df11e6401fa2152aa/src/mcp/client.py).
- [Failed research CI](https://github.com/vi-nayKR/Data-Visualization-Of-Time-Tradable-Assets-Using-ML/actions/runs/33626916336).
- [Inference gateway benchmark](https://github.com/vi-nayKR/local-llm-inference-gateway/blob/a23fae8c793905548ddc98c55631873150c13db5/tests/benchmark_throughput.py).

## 2. Positioning and presentation

### One professional story

Use **Applied AI Engineer | Full-Stack & Backend Systems** as the primary public identity. Your differentiator is the connection between uncertain model output and dependable application behavior: extraction, validation, human review, transactions, and usable interfaces.

The existing four-role job-search line makes the profile less focused. Lead with Applied AI and AI product roles; let Medha and Appointment Review demonstrate the backend/full-stack range. If backend roles become the primary target, move Medha first and ReconcileAI second. If full-stack roles become primary, promote Appointment Review after its CI gate.

Proposed GitHub bio, ready to use:

> Applied AI & full-stack engineer. Building document workflows with evidence, human review, and reliable backends. Python, TypeScript, Go. Bengaluru.

### Profile layout

1. Name, primary role, and one concrete sentence about what you build.
2. Portfolio, resume PDF, LinkedIn, and email on one line.
3. Three featured projects, each with its problem, proof, and honest status.
4. Four compact lines describing your working stack and engineering focus.
5. One paragraph for professional background and one research link.
6. One specific availability statement, if still current.

Aim for roughly **250–350 words** in the profile README. Keep detailed employment bullets, the full stack matrix, and DOCX resume access on the portfolio. These are editorial targets, not GitHub restrictions.

### Visual direction

- The current avatar is a neon illustrated emblem. For a hiring-focused presence, use a recognizable professional headshot across GitHub, LinkedIn, and X, or keep a consistent simple identity if you prefer an illustration.
- Use GitHub's native typography, generous spacing, and short project descriptions. A banner is optional; prioritize a legible first screen.
- Use real product screenshots in project READMEs. For ReconcileAI, show a finding and its highlighted source region rather than an empty upload screen.
- Include useful alt text, make text legible in dark/light mode, and inspect at a narrow mobile width.
- Limit badges to meaningful status: actual CI, release, and license where applicable. Avoid statistics cards and badge walls competing with the work.
- Keep existing repository URLs initially. Improve display titles without introducing link migrations.

### Proposed profile README

The following copy uses current public claims conservatively. Add new results only after their evidence exists.

```markdown
# Vinay K R

**Applied AI Engineer · Full-Stack & Backend Systems · Bengaluru**

I build AI-assisted workflows with source evidence, explicit business rules,
and human review. My work spans Python AI services, TypeScript interfaces,
and Go backends.

[Portfolio](https://portfolio.vinaykr.workers.dev/) ·
[Resume](https://portfolio.vinaykr.workers.dev/resumes/vinay_kr_resume_ats.pdf) ·
[LinkedIn](https://linkedin.com/in/vi-naykr) ·
[Email](mailto:vinayravindranatha@gmail.com)

## Selected work

### [ReconcileAI](https://github.com/vi-nayKR/multimodal-document-intelligence)
Invoice and purchase-order review with typed extraction, decimal-based
reconciliation, source evidence, and correction history.
Public prototype with deterministic tests and a synthetic evaluation dataset;
live-model quality is not yet measured.

### [Medha Platform API](https://github.com/vi-nayKR/medha-platform-api)
Public Go backend reference covering transactions, authorization, geospatial
discovery, and real-time messaging. Includes snapshot provenance and
co-contributor attribution.
[Product architecture](https://github.com/medha-innovations/engineering-showcase).

### [FastAPI Agent Patterns](https://github.com/vi-nayKR/fastapi-genai-agent-patterns)
Typed agent workflows with human approval, streaming, Redis caching,
and OpenTelemetry. Includes a fixture evaluation and documented requirements
for production deployment.

## Engineering focus

- AI: structured extraction, retrieval, evaluation, and human review.
- Product: Python/FastAPI, TypeScript/Angular/React, and Go.
- Systems: PostgreSQL, Redis, API contracts, and authorization.
- Delivery: automated tests, CI, observability, and failure recovery.

My professional background spans Medha Innovations, digital-asset custody,
and regulated gaming. The portfolio contains my experience and the
boundaries between professional work and public reference projects.

Co-author of [Data Visualisation of Time Tradable Assets Using Machine Learning
— IEEE NMITCON 2023](https://doi.org/10.1109/NMITCON58196.2023.10275962).

I am interested in Applied AI and AI product engineering opportunities.
```

## 3. Pins and the repository portfolio

GitHub supports up to six pinned repositories/gists. You can pin your public repositories and qualifying repositories you have contributed to; six is a limit, not a requirement. [GitHub profile reference](https://docs.github.com/en/account-and-profile/reference/profile-reference).

### Recommended pin order

| Slot | Repository | Purpose | Promotion gate |
| --- | --- | --- | --- |
| 1 | `multimodal-document-intelligence` | Flagship AI product workflow | Pin now with explicit prototype status; improve demo and evaluation next. |
| 2 | `medha-platform-api` | Backend depth and collaborative product work | Retain; add a short reading path and reconcile deployment-history wording. |
| 3 | `fastapi-genai-agent-patterns` | AI workflow controls and observability | Retain; correct generated benchmark claims immediately. |
| 4 | `homelab-sre-observability` | Failure handling and operations | Retain as supporting work; distinguish historical run evidence from current-commit verification. |
| 5 | `appointment-manager` | Product usability, accessibility, and business rules | Add after metadata and a successful current-commit CI run. |
| 6 | `Data-Visualization-Of-Time-Tradable-Assets-Using-ML` | Research continuity and analytical work | Retain only after CI is repaired; keep forecast limitations prominent. |

Use four pins while the last two gates are pending. Remove `llm-observability-eval-platform` and `enterprise-agentic-rag-platform` from the featured set. An empty slot is acceptable while you establish the evidence.

### Decision for every public repository

| Repository | Decision for this revamp |
| --- | --- |
| `vi-nayKR` | Shorten the profile using the draft above; maintain one coherent story. |
| `multimodal-document-intelligence` | Main investment: product demo, evaluation, reliability, user feedback. |
| `medha-platform-api` | Keep as the backend anchor; show one business flow end to end. |
| `fastapi-genai-agent-patterns` | Keep as the AI workflow reference; strengthen evaluation semantics and deployment boundaries. |
| `homelab-sre-observability` | Maintain one reproducible failure/recovery story; avoid expanding the lab just to list more tools. |
| `appointment-manager` | Supporting full-stack example; complete metadata and CI; no AI feature needed to justify it. |
| `Data-Visualization-Of-Time-Tradable-Assets-Using-ML` | Keep as research-linked work; repair build and evidence links; prioritize a simple forecasting baseline only if ML roles matter. |
| `enterprise-agentic-rag-platform` | Remove from pins; correct claims and label learning/reference scope. Reinvest only if it answers a distinct retrieval problem the agent-patterns project does not cover. |
| `medha-platform-infra` | Keep linked from the Medha backend/showcase as a historical operations reference. |
| `Portfolio-Ng` | Maintain working project, contact, and resume links. Use the website as the narrative layer. |
| `llm-observability-eval-platform` | Keep archived and unpinned; its existing limitations notice is useful. |
| `local-llm-inference-gateway` | Keep archived; amend unsupported benchmark claims. Reopen only with a real inference workload and measured hardware results. |
| `agy-statusline-config` | Keep archived as a personal utility. |
| `kubernetes-reliability-gamedays` | Keep archived; link selectively for platform-role applications. |
| `terraform-aws-reliability-baseline` | Keep archived; preserve lab status and cost controls. |
| `linux-operations-toolkit` | Keep archived as supporting Linux experience. |

Private projects do not need to become public to fill a portfolio. The public [Medha engineering showcase](https://github.com/medha-innovations/engineering-showcase) is already the appropriate place to explain the wider product ecosystem.

### Metadata to add or improve

| Repository | Proposed description | Topics to prioritize |
| --- | --- | --- |
| ReconcileAI | Invoice and purchase-order review with typed extraction, source evidence, decimal reconciliation, and human corrections. | `document-ai`, `applied-ai`, `python`, `fastapi`, `evaluation` |
| Medha API | Go backend reference for transactional booking, geospatial discovery, authorization, and real-time messaging. | `golang`, `postgresql`, `postgis`, `backend`, `websockets` |
| Agent Patterns | Typed AI workflow reference with approval checkpoints, streaming, Redis caching, observability, and evaluation fixtures. | `ai-agents`, `fastapi`, `langgraph`, `evaluation`, `opentelemetry` |
| Appointment Review | Clinic scheduling demo with conflict validation, accessible Angular screens, Express APIs, and MongoDB persistence. | `angular`, `typescript`, `express`, `mongodb`, `full-stack` |

Use a direct demo or case-study homepage when one exists. ReconcileAI currently links to the portfolio's general `#github` section; replace that with a project-specific destination once available. Add reuse terms only for code you have the right to license. RAG currently links a `LICENSE` file that was absent from the inspected tree; fix that mismatch.

## 4. Project work that will make the profile convincing

### A. ReconcileAI — flagship, approximately 30–38 hours

**User problem:** a reviewer needs to find invoice/PO discrepancies, check their source, correct extraction mistakes, and export the review trail.

**Build on the current implementation:** keep Docling, typed extraction, deterministic reconciliation, source evidence, and correction history. Avoid starting another document chatbot.

1. Create a reliable demonstration using permitted sample documents: upload → discrepancy → source highlight → correction → export. Include one failure/review-required path.
2. Add a sample-results mode requiring no API key. Clearly label it as prerecorded output. Keep a real extraction mode for people using their own key; show which mode is active.
3. Freeze the current development/held-out split before tuning. The existing generator produces 20 development and 30 held-out synthetic pairs. Use development data for iteration; version any later benchmark changes.
4. Run the real extraction pipeline on held-out cases and publish the actual results, including failed cases. Label synthetic results as synthetic. Add a small independently checked set of varied, permitted real documents when available.
5. Improve what the evaluation measures. The current runner compares **sets of discrepancy types** per case: it can overlook a wrong line item, wrong amount, or duplicate finding of the same type. Add item/amount correctness and evidence-location checks before calling it a complete reconciliation evaluation.
6. Record provider/model identifier, prompt/config version, commit, dataset hash, run date, environment, case count, failures, review rate, latency distribution, and token/cost accounting when available. The current runner lacks several of these fields and stops if a case raises; make partial failures visible in the report.
7. Add targeted failure checks for malformed/oversized documents, missing source evidence, provider timeouts, and interrupted jobs. Verify that all ambiguous outcomes reach human review.
8. If offering an internet-facing live demo, first add access control, upload validation, rate/cost limits, and a documented deletion/retention policy. A sample-only walkthrough is the first delivery option.
9. Ask three relevant reviewers to complete the same task. Record completion, corrections, confusion, and elapsed time with consent. Compare with a manual baseline before claiming time saved.

**Acceptance:** another person can see the complete workflow without a key, run the documented real mode, inspect one versioned evaluation with limitations, and trace at least three failures to fixes or explicit boundaries. A disappointing baseline is still useful evidence; do not select only successful cases.

### B. FastAPI Agent Patterns — workflow reliability, approximately 18–22 hours

**User problem:** a workflow should produce valid results, stop for approval, and recover from failures without losing state or taking unauthorized actions.

1. Correct the report generator and regenerate artifacts. Report lexical's higher MRR and the Recall@3 tie accurately. A simpler retrieval choice winning is a useful engineering result.
2. Label provider mode in every report. Separate deterministic fixture results from live-provider results; label the existing blended token-cost formula as an estimate.
3. Tighten grader semantics. The inspected pass rule allows any positive citation recall for an answerable case; 100% task success therefore does not mean complete citations. Define and report answer quality, citation correctness, approval behavior, and actual side effects separately.
4. Add a realistic task suite for one workflow: read operational documents and propose a change that requires approval. Include absent answers, conflicting/stale sources, foreign-tenant material, malformed tool arguments, and a refused action.
5. Demonstrate authorization derived from authenticated identity. A client-supplied tenant ID and fixture isolation tests do not establish a deployment security boundary.
6. For a deployable version, persist checkpoints and test approval across a process restart. Verify that retrying an approved action does not apply it twice. Use existing database capabilities and explicit idempotency keys.
7. Publish one sanitized trace showing retrieval, provider calls, waiting for approval, and completion/failure. Include a timeout trace and cost/latency boundaries.
8. If cross-client tool use is actually needed, integrate one real MCP tool and test it with an independent client. Make the permitted actions and authorization boundaries explicit. Avoid adding protocol work merely for a badge.

**Acceptance:** fixture/live results are distinguished; the report's conclusions match its data; a refused or unauthenticated action has no side effect; approved state survives a restart in the deployment version; retries are safe.

This evaluation-first direction is consistent with the emphasis on task outcomes, repeated trials, and appropriate graders in [Anthropic's agent evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). Choose the smallest workflow architecture that meets the task; [Anthropic's building-agents guidance](https://www.anthropic.com/engineering/building-effective-agents) also discusses the trade-off between simple workflows and autonomous agents.

### C. Medha Platform API — backend depth, approximately 12–16 hours

**Reader question:** can you explain and defend a business-critical backend flow beyond a list of technologies?

1. Add a “read this in 10 minutes” route through authorization → booking service → transaction helper → database changes → tests.
2. Choose booking consistency as the main case study. Explain competing bookings, allowed state transitions, rollback, and side-effect ordering.
3. Verify a real PostgreSQL integration test for concurrent conflicting bookings and failure rollback. Keep mock tests for fast logic checks, but distinguish them from database evidence.
4. Show one failure-and-recovery example. Include the command, expected invariant, result, and limitations.
5. If performance matters to the story, publish a reproducible workload with hardware, dataset size, concurrency, request mix, error rate, and p50/p95/p99. If it does not, omit performance adjectives.
6. Preserve co-contributor attribution and snapshot provenance. Replace absolute wording such as “zero cross-layer bypassing” unless a check actually enforces it.
7. Reconcile deployment history: the backend README describes a move from Kubernetes to Compose, while the showcase discusses current resume Kubernetes claims and an older Compose reference. Use dated snapshots and verified chronology; do not infer the live topology from either document.

**Acceptance:** a reviewer can follow one business invariant through code, database behavior, a runnable test, and an architecture decision, while understanding your contribution and the snapshot's age.

### Supporting projects — bounded improvements

- **Appointment Review:** add metadata; establish CI; show keyboard operation and error states. Add one real MongoDB persistence/integration check if claiming database behavior. Keep the documented single-process concurrency ceiling; solve cross-instance coordination only when deployment requires it.
- **Research terminal:** repair the frontend lockfile/CI; fix README links pointing to `../Resume/Guide/...`, which are outside this repository's public tree. If forecasting becomes a focus, compare with last-value and seasonal baselines using chronological splits and report MAE/RMSE by horizon. Distinguish static fundamentals from live data.
- **SRE lab:** use its existing postmortem and alert evidence. The inspected latest successful CI run points to `3be27d35`, while the default branch was `5bfa8a14`; verify workflow coverage for the published commit before asserting current success. Add one readable dashboard capture with the underlying query and failure timeline.

## 5. Skills to develop in the AI era, with evidence

Treat this as a gap map for public evidence, not a claim that you lack these skills. Learn through the projects above, with at most one focused topic per week.

| Priority | Skill | Public proof to produce | When |
| --- | --- | --- | --- |
| Essential | Python typing, async I/O, API error handling | Bounded provider calls, validated schemas, explicit errors, passing type/test gates | Weeks 1–4 |
| Essential | AI evaluation and experimental design | Versioned datasets, honest baselines, failure categories, reproducible results | Weeks 2–5 |
| Essential | Structured extraction and evidence grounding | Correct fields/amounts, source alignment, ambiguity routed to review | Weeks 2–5 |
| Essential | SQL, transactions, concurrency, idempotency | Real database test proving a booking invariant and safe retries | Weeks 6–8 |
| Essential | Retrieval quality | Lexical/dense/hybrid comparison on identical data, explained metric definitions | Weeks 6–7 |
| Essential | Agent workflow control | Approval, cancellation, deadlines, durable state, side-effect verification | Weeks 6–8 |
| Essential | Security and trust boundaries | Authenticated ownership, tenant isolation, hostile-document cases, safe tool permissions | Throughout |
| Essential | Product engineering and accessibility | Complete task flow, keyboard/error/loading states, mobile readability | Weeks 3–5 |
| Essential | Observability and deployment | One trace and one failure/recovery report with bounded cost and logs | Weeks 7–10 |
| Essential | AI-assisted development discipline | A real PR explaining the defect, generated changes reviewed, tests, and trade-offs | Every project milestone |
| Useful | MCP and tool interoperability | A real client/server integration when a workflow needs it | Week 8, conditional |
| Useful | Statistics and ML fundamentals | Correct metric denominators, leakage control, variation across runs | Alongside evaluation |
| Conditional | Fine-tuning, GPU serving, quantization | Reproducible quality/cost improvement over a simpler baseline | After the first 90 days, if a workload needs it |
| Conditional | Advanced Kubernetes/multi-agent infrastructure | Demonstrated operational need and measured benefit | After evidence of that need |

For MCP implementations, use the protocol's [security best-practices documentation](https://github.com/modelcontextprotocol/modelcontextprotocol/security) as the starting point. A JSON-RPC-shaped object and an in-process method call alone do not demonstrate interoperable transport or authorization.

Show that you can use AI coding tools thoughtfully: inspect generated changes, explain design decisions, reject unnecessary abstractions, and retain tests that expose real failure modes. A list of tools or a prompt collection does not establish those habits. Keep one small development-instructions file only when it helps a contributor run, test, or change that repository.

## 6. A consistent presentation standard for featured repositories

The first screen should answer: **who is it for, what can I see, what works, and how can I verify it?**

Use this README order:

1. Project name and one-sentence user problem.
2. Honest status: prototype, reference snapshot, lab, or deployed product.
3. One useful screenshot and demo/sample-results link.
4. Three implemented capabilities, each tied to a user outcome.
5. Small architecture diagram showing data flow and trust boundaries.
6. Quickstart with prerequisites, sample data, commands, and expected output.
7. Validation/evaluation results with scope, date, commit, and reproduction steps.
8. Two or three engineering decisions and their trade-offs.
9. Known limitations and the next concrete improvement.
10. Contribution boundaries, reuse terms, and contact/contribution instructions where useful.

Reuse existing `docs/`, `tests/`, and `evals/` directories. Add an evaluation report, case study, screenshot, or demo script only when it conveys evidence. Release notes should link to those artifacts.

Before featuring a release, verify:

- A clean setup succeeds using the documented versions and dependency lockfiles.
- CI tests the relevant behavior at the released commit; syntax/build checks are labeled accurately.
- Demo mode is visible; fixture outputs are never presented as live model results.
- Screenshots and sample data contain no real customer information or secrets.
- Every numerical claim has a report, denominator, environment, and limitation.
- Every link resolves publicly; a portfolio link does not masquerade as a live project demo.
- The repository's status and attribution match the profile and portfolio.

For live deployments, also verify access controls, rate/cost limits, deletion behavior, and error handling. Record an actual release after these gates pass; none of the nine repositories sampled for releases returned a GitHub Release during this audit.

## 7. Execution schedule

This is an estimate, not a delivery guarantee. Allocate 8–10 hours weekly: roughly six hours building/testing, two documenting/evaluating, and up to two on feedback or learning. If a gate fails, carry the work forward and defer optional MCP or secondary-project work.

| Week | Main work | Deliverable / exit gate |
| --- | --- | --- |
| 1 | Fix portfolio contradictions; correct report generator; repair research CI; update proposed profile/pins/metadata | Accurate public claims, focused front page, real CI status visible; unresolved projects demoted |
| 2 | Freeze ReconcileAI benchmark and run first real-provider baseline | Versioned report with configuration and per-case errors |
| 3 | Improve discrepancy/item/evidence scoring and fix highest-impact failures | One comparison with the baseline; held-out data kept separate from tuning |
| 4 | Add sample-results walkthrough, screenshot, and robust review/error states | A visitor completes the demonstration without credentials |
| 5 | Collect feedback from three relevant reviewers; revise onboarding | Recorded usability findings and one release with bounded claims |
| 6 | Correct Agent Patterns grading/mode labels and retrieval comparison | Reproducible fixture report; separate real-provider report if run |
| 7 | Add the chosen workflow's authorization, persistence, retry checks, and traces | Verified refusal, restart/resume, and duplicate-action behavior |
| 8 | Medha booking case study and database integration proof | One invariant explained and exercised end to end; optional MCP only if time remains |
| 9 | Finish Appointment Review metadata/CI and research evidence links; verify SRE demo evidence | Four to six pins whose evidence gates have passed |
| 10 | Make a useful contribution to a dependency you actually use | A reproducible issue, reviewed docs correction, or focused PR; merge is outside your control |
| 11 | Adapt the strongest case study for LinkedIn and X | Consistent profiles and evidence-linked publication drafts |
| 12 | Ask independent engineers to inspect the profile; fix the main friction | Final profile/repository check and a short next-quarter backlog based on feedback |

### First work session, in exact order

1. Record current profile/pins and the relevant repository commits.
2. Correct the RAG and inference-gateway claims; repair the agent report at its generator.
3. Repair the research build using the actual CI failure log.
4. Apply the shorter profile copy and four-pin initial lineup.
5. Fill Appointment Review metadata and add the known LinkedIn social link.
6. Open the profile as a public visitor; check first-screen clarity and all featured links.
7. Start the ReconcileAI baseline before spending time on custom visual assets.

Steps above are future implementation tasks. The current deliverable is this audited plan; writing it does not count as applying the profile or repository changes.

## 8. LinkedIn and X: the next phase

GitHub should hold the inspectable evidence. LinkedIn should explain your professional direction and engineering impact. X should show concise observations, demos, and technical discussion tied to that same work.

### LinkedIn draft direction

**Headline:** Applied AI Engineer | Full-Stack & Backend Systems | Python, TypeScript, Go | Building AI workflows with evidence and human review

**About opening:**

> I build AI-assisted workflows that connect model output to business rules, review interfaces, and dependable backend services. My public work includes invoice/PO reconciliation, typed agent workflows, and a Go backend reference. I document what is implemented, how it is tested, and where it still needs improvement.

Follow with a short, verified professional summary and one clear target role. Use Featured for the flagship demo/case study, its GitHub repository, and the portfolio. Keep employment dates/titles consistent with the resume. Only use impact numbers you can explain and substantiate.

Publish one substantive project story every one or two weeks: problem → decision → measured result → failure/limitation → evidence link. Example topics: why reconciliation arithmetic stays outside the model; where lexical retrieval beat hybrid; what a booking rollback test actually proves.

### X draft direction

**Bio:** Applied AI + full-stack engineer. Python, TypeScript, Go. Building document workflows, testing agents, and sharing the results. Bengaluru.

Use the same name/avatar and portfolio destination. The actual X handle is unknown; do not invent a URL or claim account availability.

Pinned post draft:

> I'm Vinay. I build AI workflows with evidence and human review. ReconcileAI reviews invoices against purchase orders and tracks corrections. Public prototype; evaluation limits are documented.
> https://github.com/vi-nayKR/multimodal-document-intelligence

After the evaluation is published, replace the status sentence with a scoped result and link to the report. Share one or two useful observations weekly; reuse project work instead of maintaining a separate content project. Avoid unsupported performance comparisons and “production-ready” claims.

These are content recommendations, not audited assessments of your existing LinkedIn/X profiles or claims about their ranking algorithms. No posts or messages are sent as part of this planning task.

## 9. How to know the revamp has worked

Use measurable review gates rather than a percentile or a star target.

| Horizon | Target | How to verify |
| --- | --- | --- |
| First week | Profile and project claims agree | Inspect profile, pins, READMEs, benchmark generator/output, and actual CI workflows |
| First month | One flagship can be understood and demonstrated independently | An unfamiliar engineer follows the README and demo without your help |
| By day 45 | Real AI quality evidence exists | Versioned real-provider report with dataset/configuration, failed cases, and limitations |
| By day 60 | One workflow demonstrates safe state changes and recovery | Tests/trace show authorization, refusal, restart/resume, and duplicate prevention |
| By day 90 | Three substantial engineering stories are inspectable | ReconcileAI product/eval; Agent Patterns workflow controls; Medha transaction case study |
| By day 90 | Four to six credible pins and consistent social positioning | Public visitor review across profile, repositories, portfolio, LinkedIn, and X |
| Ongoing | External feedback improves the work | Record specific user/reviewer feedback, resulting fixes, useful issues/PRs, and relevant conversations |

Ask reviewers three questions: “What role does this person fit?”, “Which project would you inspect first?”, and “Which claim needs more evidence?” Success means their answers match your intended positioning and they can find the proof.

Track profile/repository traffic and relevant inbound conversations as directional signals when available. They do not establish causation or guarantee hiring outcomes. Keep a small monthly note, not a custom analytics platform.

## 10. What to defer

- New general-purpose RAG, chatbot, or multi-agent repositories while existing projects lack complete evidence.
- Decorative contribution graphs, fake activity, star campaigns, and large tool-logo collections.
- Fine-tuning or GPU hosting without a workload and baseline that justify them.
- Another frontend/backend language for portfolio breadth. Deepen the existing Python/TypeScript/Go combination.
- Large platform rewrites, custom evaluation dashboards, or always-on paid demos before a simple report and sample walkthrough work.

The first milestone is an accurate, focused profile. The lasting improvement is three projects that other engineers can run, evaluate, question, and trust within their stated limits.
