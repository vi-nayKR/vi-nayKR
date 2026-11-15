# Medha Innovations — Engineering Overview

Medha Innovations was a booking and messaging venture founded in 2026. As Co-founder and Founding Engineer, I architected and built the core platform backend and deployment infrastructure.

---

## Engineering Focus & Architecture

The architecture was engineered around a modular Go backend designed for low latency, geospatial queries, and real-time state synchronization:

* **Core Services**: Built in Go using domain-driven modular boundaries, health check probes, structured JSON logging, and grace-period lifecycle management.
* **Geospatial & Storage**: PostgreSQL schemas with PostGIS geospatial indexing for high-speed location discovery and localized entity matching.
* **Real-Time Communication**: Redis pub/sub and WebSocket channels powering instant messaging and booking status transitions.
* **Infrastructure**: Two-node Linux architecture managed via systemd, Docker, Nginx reverse proxy with TLS termination, nftables firewalling, and automated daily backup routines.

---

## Public Reference Repositories

* [Go Backend Reference (`medha-platform-api`)](https://github.com/vi-nayKR/medha-platform-api) — Modular Go architecture, PostGIS queries, and role-based APIs.
* [Infrastructure Baseline (`medha-platform-infra`)](https://github.com/vi-nayKR/medha-platform-infra) — Production deployment baseline, systemd configurations, and operations runbooks.
* [Medha Innovations GitHub Organization](https://github.com/medha-innovations)

---

[← Back to Profile](README.md)
