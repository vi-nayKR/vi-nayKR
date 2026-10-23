# Vinay K R

**Software Engineer · Backend & Full-Stack · Applied AI**
Bengaluru, India · [Portfolio](https://portfolio.vinaykr.workers.dev/) · [ATS résumé](https://portfolio.vinaykr.workers.dev/resumes/Vinay_K_R_Software_Engineer_Resume_ATS.pdf) · [LinkedIn](https://linkedin.com/in/vi-naykr) · [Email](mailto:vinayravindranatha@gmail.com)

I build backend workflows and applied-AI applications with explicit authorization, evaluation and human review. My background includes full-stack work at Light & Wonder and Liminal Custody, plus collaborative co-founder engineering at Medha Innovations.

## Applied-AI flagships

### [TraceWard — approval-gated incident triage](https://github.com/vi-nayKR/fastapi-genai-agent-patterns)

Predefined checkpointed workflow: parse logs, retrieve related incidents, suggest causes/fixes and request approval before persisting a **local ticket draft**. It does not file external issues or execute fixes.

- [Architecture](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/blob/docs/portfolio-evidence/docs/architecture.md) · [Evidence and limitations](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/blob/docs/portfolio-evidence/docs/evidence.md) · [Local demo script](https://github.com/vi-nayKR/fastapi-genai-agent-patterns/blob/docs/portfolio-evidence/docs/demo-script.md)
- Recorded evaluation uses 50 synthetic known-family holdouts. Approval-bypass probes are not proof of general security or production incident accuracy.
- The no-key demonstration uses deterministic suggestions, not a fresh model response.

### [ReconcileAI — evidence-backed document review](https://github.com/vi-nayKR/multimodal-document-intelligence)

Local invoice/PO workbench combining parsing, typed extraction, decimal-exact checks, source evidence and correction history. A reviewer can correct extracted data and rerun controls without another model call.

- [Architecture](https://github.com/vi-nayKR/multimodal-document-intelligence/blob/docs/portfolio-evidence/docs/architecture.md) · [Evidence and limitations](https://github.com/vi-nayKR/multimodal-document-intelligence/blob/docs/portfolio-evidence/docs/evidence.md) · [Local demo script](https://github.com/vi-nayKR/multimodal-document-intelligence/blob/docs/portfolio-evidence/docs/demo-script.md)
- Recorded Gemini field F1 of 76.0% covers 20 held-out CORD receipts, not invoice/PO discrepancy accuracy. Synthetic controls and review burden are reported separately.
- The fictional prerecorded sample bypasses live OCR/model extraction; it is not payment authorization.

## Professional background and ownership

- **Light & Wonder:** internship Mar–Jul 2023; employment Aug 2023–Jul 2025. Final title: Senior Associate Software Engineer. No unverified promotion date is asserted.
- **Liminal Custody / First Answer India Services Pvt. Ltd.:** Software Engineer, Full Stack, Nov 2025–Mar 2026.
- **Medha Innovations:** self-funded, two-founder venture, Mar–Sep 2026 as reported. Collaborative Go backend and integration work; [scope and public references](MEDHA.md).
- October AI prototypes are follow-on portfolio/R&D work, not backdated venture deliveries. Detailed employer contributions are résumé-reported, not independently verified by public code.

## Supporting engineering evidence

- [Medha backend publication-review snapshot](https://github.com/vi-nayKR/medha-platform-api/tree/security/publication-review): transactions, PostGIS, role-aware APIs and messaging. Public hardening does not certify the private deployed system.
- [Homelab SRE](https://github.com/vi-nayKR/homelab-sre-observability/tree/hardening/production-readiness): isolated single-host deployment, authenticated alert reception and file-restore checks—not HA, independent paging or full application recovery certification.
- [Research application](https://github.com/vi-nayKR/Data-Visualization-Of-Time-Tradable-Assets-Using-ML): 2023 [IEEE publication](https://doi.org/10.1109/NMITCON58196.2023.10275962), with a separate 2026 rebuild and retained negative forecasting results.
- EvidenceRAG remains a supporting harness with an incomplete live pilot, not a primary enterprise-deployment claim.

The canonical portfolio source is `vinay-portfolio`; archived `Portfolio-Ng` is superseded. Contribution counts are not business impact, and private commit IDs are not public deployment evidence.

Open to backend/software engineering and backend-heavy full-stack roles with opportunities to build reliable AI-enabled workflows.

<details>
<summary>Visual profile card</summary>

<img src="assets/hud.svg?v=4" alt="Vinay K R — Software Engineer, backend and applied AI. Python, TypeScript and Go. Bengaluru." width="100%">

</details>
