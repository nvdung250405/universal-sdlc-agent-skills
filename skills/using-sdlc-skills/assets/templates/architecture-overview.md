# System Architecture Overview: [SYSTEM_OR_SERVICE_NAME]

- **Status**: Proposed | Accepted | Superseded
- **Architecture Lead**: [Name / Agent]
- **Last Updated**: [YYYY-MM-DD]
- **Canonical Path**: `docs/architecture.md` (or `docs/architecture/[subsystem].md`)

---

## 1. Executive Summary & Quality Attributes

### High-Level Summary
[Concise summary of the architectural vision, technical stack, and core trade-offs.]

### Primary Quality Attribute Goals
1. **Performance / Latency**: [e.g., p95 response time < 150ms]
2. **Reliability / Availability**: [e.g., 99.9% uptime, zero single points of failure]
3. **Security / Privacy**: [e.g., Zero Trust boundaries, encrypted at rest and in transit]
4. **Maintainability / Deep Modules**: [e.g., Explicit seams, clear contract boundaries]

---

## 2. System Context & Boundaries (C4 Level 1 & 2)

```mermaid
flowchart TD
    User["End User / Browser Client"]
    API["API Gateway / Edge Router"]
    Auth["Auth Service / Identity"]
    Core["Core Application Service"]
    DB[("Primary Database")]
    Queue["Async Task Queue"]
    Worker["Background Worker"]
    ThirdParty["External Providers (e.g., Stripe, SendGrid)"]

    User -->|HTTPS| API
    API -->|Validate Token| Auth
    API -->|Internal RPC/HTTP| Core
    Core -->|Read / Write| DB
    Core -->|Enqueue Job| Queue
    Queue -->|Consume| Worker
    Worker -->|Webhooks / API| ThirdParty
```

### External Dependencies & Integrations
| External System | Purpose | Protocol / Contract | Failure Mode / Fallback |
|---|---|---|---|
| [Provider A] | [Auth / Payments / Email] | [REST / gRPC / Webhook] | [Circuit breaker / Retry queue] |

---

## 3. Component Breakdown & Data Ownership

| Component / Subsystem | Primary Responsibility | Data Owned (Single Source of Truth) | Public Interface / Seam |
|---|---|---|---|
| `auth` | Identity, session validation, RBAC | User accounts, sessions, API tokens | `IAuthService` |
| `billing` | Subscription lifecycle, invoices | Invoices, payment state, plans | `IBillingService` |
| `core` | Domain business logic | Workspaces, project assets | REST / GraphQL API |

---

## 4. Key Cross-Cutting Design Decisions

### Data Storage & Consistency
- **Primary Datastore**: [e.g., PostgreSQL, DynamoDB]
- **Consistency Model**: [Strong consistency for financials, eventual for metrics]
- **Caching Strategy**: [e.g., Redis read-through cache with TTL]

### Security & Trust Boundaries
- **Authentication**: [JWT / Session cookies / OIDC]
- **Authorization**: [RBAC / ABAC enforcement points]
- **Secrets Management**: [Cloud Secret Manager / Vault, never in code]

---

## 5. Architectural Decision Records (ADRs) Index

| ADR ID | Decision Title | Status | Date |
|---|---|---|---|
| `ADR-001` | Selection of PostgreSQL for multi-tenant data (`docs/adr/ADR-001.md`) | Accepted | YYYY-MM-DD |
| `ADR-002` | Event-driven architecture for background jobs (`docs/adr/ADR-002.md`) | Accepted | YYYY-MM-DD |
