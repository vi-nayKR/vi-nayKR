# Vinay K R
### Senior GenAI & Applied AI Systems Engineer
📍 **Bengaluru, India** (Hybrid / Remote) | Global Remote  
🌐 **Live Portfolio & 3D AI Space:** [portfolio.vinaykr.workers.dev](https://portfolio.vinaykr.workers.dev)  
📫 **Email:** [vinayravindranatha@gmail.com](mailto:vinayravindranatha@gmail.com) | 💼 **LinkedIn:** [linkedin.com/in/vi-naykr](https://linkedin.com/in/vi-naykr)

---

## ⚡ Executive Summary
Senior GenAI & Applied AI Systems Engineer with **3+ years of enterprise experience** architecting high-throughput distributed microservices, autonomous agentic workflows, and production Generative AI platforms across fintech (**Liminal Custody**) and enterprise gaming systems (**Light & Wonder**).

- **Specialized in:** Advanced Hybrid RAG (pgvector HNSW + BM25 Reciprocal Rank Fusion), Multi-Agent State Graphs (LangGraph & Semantic Kernel), Model Context Protocol (MCP), and Local LLM Serving (vLLM PagedAttention + Redis vector semantic caching).
- **Scale Proof:** Architected Medha, an independent 21-service domain-driven platform load-tested at **500 Requests Per Second (RPS)** with **p95 latency < 85ms**.
- **Quality Rigor:** Authored **750+ automated Cypress E2E regression tests** sustaining 100% compliance pass rates.

---

## 🛠️ Production Tech Stack

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 PRODUCTION AI & SYSTEMS STACK                                    │
├───────────────────────────────┬──────────────────────────────────┬───────────────────────────────┤
│ 1. GENAI & AGENTS             │ 2. RETRIEVAL & VECTOR STORES     │ 3. INFERENCE & SERVING        │
│ • LangGraph (Cyclic Graphs)   │ • PostgreSQL 18 + pgvector HNSW  │ • vLLM (PagedAttention)       │
│ • Semantic Kernel 1.79        │ • Reciprocal Rank Fusion (RRF)   │ • Redis 8.10 (Semantic Cache) │
│ • Model Context Protocol (MCP)│ • BM25 Sparse Search + Qdrant    │ • 4-bit QLoRA with Unsloth    │
├───────────────────────────────┼──────────────────────────────────┼───────────────────────────────┤
│ 4. BACKEND & APIS             │ 5. EVALUATION & OBSERVABILITY    │ 6. CLOUD & DEVOPS             │
│ • Python 3.12 (FastAPI Async) │ • Ragas 0.2 (RAG Triad Metrics)  │ • Kubernetes (k3s) & Argo CD  │
│ • C# 14 (.NET 10 Minimal APIs)│ • DeepEval & Arize Phoenix       │ • Cloudflare Zero Trust WAF   │
│ • Go (chi) & PostgreSQL 18    │ • OpenTelemetry & NeMo Guardrails│ • SeaweedFS S3 Object Store   │
└───────────────────────────────┴──────────────────────────────────┴───────────────────────────────┘
```

---

## 🌟 Flagship Production Repositories

### 1. [enterprise-agentic-rag-platform](https://github.com/vi-nayKR/enterprise-agentic-rag-platform)
*Python FastAPI · LangGraph · pgvector HNSW · BM25 RRF · Model Context Protocol (MCP) · Angular 22*
- Multi-Agent RAG engine indexing enterprise documents with **Hybrid Search (pgvector + BM25 with RRF, k=60)**, boosting recall by **34%**.
- Integrated **Model Context Protocol (MCP)** tool execution and automated **Ragas evaluation** (0.94 Faithfulness).
- Non-blocking SSE token streaming with real-time markdown citations directly to Angular 22 Signals.

### 2. [medha-platform-api](https://github.com/vi-nayKR/medha-platform-api)
*Go (chi) · PostgreSQL 17 + PostGIS · Redis 8.10 Pub/Sub · SeaweedFS · 500 RPS Scale Proof*
- High-throughput domain-driven Go backend featuring **21 strictly isolated bounded contexts** and **50 automated SQL migrations**.
- **PostGIS Geospatial Engine (`ST_DWithin` + GIST Indexing)** executing proximity discovery in $<15\text{ms}$.
- Distributed real-time **WebSocket messaging fan-out via Redis 8 Pub/Sub backplane**.
- Load-tested under sustained distributed concurrency at **500 RPS with 100% success rate (p95 latency <85ms)**.

### 3. [local-llm-inference-gateway](https://github.com/vi-nayKR/local-llm-inference-gateway)
*FastAPI · vLLM PagedAttention · Redis 8 Semantic Cache · Unsloth 4-bit LoRA · Docker*
- High-throughput inference gateway with **Redis 8 vector semantic caching (<5ms latency)** for recurring prompts.
- Local quantized 8B model serving via **vLLM with PagedAttention and continuous batching**, cutting cloud API costs by **60%**.
- Automated 4-bit QLoRA fine-tuning pipeline using Unsloth on domain-specific compliance datasets.

### 4. [fastapi-genai-agent-patterns](https://github.com/vi-nayKR/fastapi-genai-agent-patterns)
*Python 3.12 · LangGraph · OpenTelemetry · MCP Tool Server · Human-in-the-Loop*
- Production reference architecture for stateful multi-agent supervisor graphs with human-in-the-loop validation checkpoints.
- Custom Model Context Protocol (MCP) server for enterprise SQL generation and tool-calling execution.

### 5. [medha-platform-infra](https://github.com/vi-nayKR/medha-platform-infra)
*Kubernetes (k3s) · Argo CD GitOps · Cloudflare Zero Trust Tunnels · Terraform · SeaweedFS*
- Declarative GitOps infrastructure managing staging and production cluster overlays with **Argo CD pull-reconciliation**.
- **Zero Inbound Open Ports** perimeter using outbound Cloudflare Tunnels (`cloudflared`) and default-deny NetworkPolicies.
- High-performance distributed object storage topology using **SeaweedFS S3** with direct presigned client uploads.

### 6. [Portfolio-Ng](https://github.com/vi-nayKR/Portfolio-Ng)
*Angular 22 Signals · Three.js 3D GenAI Space · Vite · Tailwind CSS · Cloudflare Workers*
- Production portfolio featuring **interactive 3D GenAI Latent Vector Space (Three.js)**, Times New Roman resume view, and dark/light modes.
- Live deployment: [portfolio.vinaykr.workers.dev](https://portfolio.vinaykr.workers.dev/)

---

## 📈 GitHub Metrics & Activity
![GitHub Contribution Graph](https://ghchart.rshah.org/vi-nayKR)
