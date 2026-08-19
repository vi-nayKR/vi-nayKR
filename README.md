# Vinay K R
### Senior GenAI & Applied AI Systems Engineer
📍 **Bengaluru, India** (Hybrid / Remote) | Global Remote  
🌐 **Live Portfolio & Agent Playground:** [portfolio.vinaykr.workers.dev](https://portfolio.vinaykr.workers.dev)  
📫 **Email:** [vinayravindranatha@gmail.com](mailto:vinayravindranatha@gmail.com) | 💼 **LinkedIn:** [linkedin.com/in/vi-naykr](https://linkedin.com/in/vi-naykr)

---

## ⚡ Executive Summary
Senior GenAI & Applied AI Systems Engineer with **3+ years of enterprise experience** architecting high-throughput distributed microservices, autonomous agentic workflows, and production Generative AI platforms across fintech (**Liminal Custody**) and enterprise gaming systems (**Light & Wonder**).

- **Specialized in:** Advanced Hybrid RAG (pgvector HNSW + BM25 Reciprocal Rank Fusion), Multi-Agent State Graphs (LangGraph & Semantic Kernel), Model Context Protocol (MCP), and Local LLM Serving (vLLM PagedAttention + Redis vector semantic caching).
- **Scale Proof:** Architected Medha, an independent 21-service microservices platform load-tested at **500 Requests Per Second (RPS)** with **p95 latency < 85ms**.
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
│ 4. BACKEND & APIS             │ 5. EVALUATION & OBSERVABILITY    │ 6. FRONTEND & TESTING         │
│ • Python 3.12 (FastAPI Async) │ • Ragas 0.2 (RAG Triad Metrics)  │ • Angular 22 (Signals + SSE)  │
│ • C# 14 (.NET 10 Minimal APIs)│ • DeepEval & Arize Phoenix       │ • TypeScript 7 & RxJS         │
│ • Go (chi) & PostgreSQL 18    │ • OpenTelemetry & NeMo Guardrails│ • Cypress 15 (750+ E2E Tests) │
└───────────────────────────────┴──────────────────────────────────┴───────────────────────────────┘
```

---

## 🌟 Pinned Production Projects

### 1. [enterprise-agentic-rag-platform](https://github.com/vi-nayKR/enterprise-agentic-rag-platform)
*Python FastAPI · LangGraph · pgvector HNSW · BM25 RRF · Model Context Protocol (MCP) · Angular 22*
- Multi-Agent RAG engine indexing enterprise documents with **Hybrid Search (pgvector + BM25 with RRF)**, boosting recall by **34%**.
- Integrated **Model Context Protocol (MCP)** tool execution and automated **Ragas evaluation** (0.94 Faithfulness).
- Non-blocking SSE token streaming with real-time markdown citations directly to Angular 22 Signals.

### 2. [local-llm-inference-gateway](https://github.com/vi-nayKR/local-llm-inference-gateway)
*FastAPI · vLLM PagedAttention · Redis 8 Semantic Cache · Unsloth 4-bit LoRA · Docker*
- High-throughput inference gateway with **Redis 8 vector semantic caching (<5ms latency)**.
- Local quantized 8B model serving via **vLLM with PagedAttention and continuous batching**, cutting cloud API costs by **60%**.
- Automated 4-bit QLoRA fine-tuning pipeline using Unsloth on domain-specific compliance datasets.

### 3. [medha-distributed-engine](https://github.com/vi-nayKR/medha-distributed-engine)
*Go · PostgreSQL/PostGIS · Redis · k3s · Argo CD GitOps · Cloudflare Tunnel*
- Independent distributed backend with **21 bounded microservices, ~200 REST endpoints**, load-tested to **500 RPS (p95 < 85ms)**.
- PostGIS proximity search using `ST_DWithin` over GIST spatial indexing with distance-ordered keyset pagination.

---

## 📈 GitHub Metrics & Activity
![GitHub Contribution Graph](https://ghchart.rshah.org/vi-nayKR)
