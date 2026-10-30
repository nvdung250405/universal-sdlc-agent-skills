# Canonical Artifact & Template Contracts

This reference document defines the complete mapping and ownership rules for the pack's 22 canonical artifact templates across all 16 SDLC stages.

---

## 1. Principles of Artifact Ownership

1. **Starter Template vs. Canonical Artifact:**
   - Files in `templates/` (and router assets `assets/templates/`) are **starter templates / blueprints**.
   - They provide an initial skeleton with pre-defined sections, quality prompts, and required fields.
   - When initiating work, the agent or engineer copies the template to the **Canonical Destination Path** on disk and populates it with real project context.
   - **Never maintain duplicate files** (e.g., do not create both `feature-spec.md` and `spec.md` for the same feature).
2. **One Artifact, One Owner:**
   - Every artifact type has exactly one authoritative owner skill that governs its creation, structure, and amendments.
3. **Evidence Before Assertions:**
   - A written test plan or design checklist is not evidence. Artifacts recording verification (`acceptance-report.md`, `pull-request.md`) must contain real terminal output and observed check results.

---

## 2. Complete Artifact & Template Mapping Table (22 Canonical Artifacts)

| Stage | Starter Template | Canonical Destination Path | Primary Owner Skill | Purpose / Description |
|---|---|---|---|---|
| **1. Discovery** | `templates/opportunity-brief.md` | `docs/discovery/[initiative]/opportunity-brief.md` | `interview-me`, `idea-refine`, `customer-research` | Problem framing, target users, research evidence, and initial hypotheses. |
| **2. Requirements** | `templates/PRD.md` | `docs/prd.md` | `pm-product-spec` | Product intent, user problems, measurable outcomes, epics, non-goals, and risks. |
| **2. Requirements** | `templates/feature-spec.md` | `docs/features/<feature-id>/spec.md` | `spec-driven-development`, `pm-user-story` | Canonical feature specification containing User Stories and BDD Given/When/Then AC. |
| **2. Requirements** | `templates/SRS.md` | `docs/specs/SRS.md` *(or `docs/srs.md`)* | `requirements-engineering` | Formal Software Requirements Specification for compliance-heavy or high-complexity projects. |
| **2. Requirements** | `templates/RTM.md` | `docs/specs/RTM.md` *(or `docs/rtm.md`)* | `requirements-engineering` | Requirements Traceability Matrix linking requirements to designs, tasks, and tests. |
| **3. Architecture** | `templates/architecture-overview.md` | `docs/architecture.md` | `software-architecture` | System boundaries, C4 models, component breakdown, and data ownership. |
| **3. Architecture** | `templates/ADR.md` | `docs/adr/ADR-NNN-[slug].md` | `documentation-and-adrs` | Architectural Decision Record capturing context, options considered, and trade-offs. |
| **3. Architecture** | `templates/DDS.md` | `docs/features/<feature-id>/design.md` | `software-architecture`, `codebase-design` | Detailed Design Specification (LLD) for complex subsystem or data model changes. |
| **4. Planning** | `templates/plan.md` | `docs/features/<feature-id>/plan.md` | `spec-driven-development` | Implementation strategy, technical context, and governance checks. |
| **4. Planning** | `templates/tasks.md` | `docs/features/<feature-id>/tasks.md` | `planning-and-task-breakdown` | Single authoritative task list with dependency edges, files, and verification commands. |
| **4. Planning** | `templates/task-handoff.md` | `.agent/tasks/<task-id>.md` | `task-handoff` | Active session state, progress log, and cross-agent / cross-session handoff notes. |
| **6. Verification** | `templates/acceptance-report.md` | `docs/features/<feature-id>/acceptance-report.md` | `verification-before-completion` | Empirical test evidence, build logs, and acceptance verification before completion. |
| **7. Review** | `templates/pull-request.md` | `.github/pull_request_template.md` *(or PR body)* | `code-review-and-quality` | PR description, change motivation, test evidence, and reviewer checklist. |
| **8. Release** | `templates/release-notes.md` | `docs/releases/v[X.Y.Z].md` | `shipping-and-launch` | Release highlights, detailed changelog, breaking changes, and deployment procedures. |
| **8. Release** | `templates/release-checklist.md` | `docs/releases/release-checklist.md` | `shipping-and-launch` | Pre-deployment quality, security, operations, and rollback readiness gates. |
| **9. Operations** | `templates/incident-postmortem.md` | `docs/incidents/[YYYYMMDD-slug]/postmortem.md` | `observability-and-instrumentation` | Root cause analysis (5 Whys), outage timeline, impact metrics, and action items. |
| **9. Operations** | `templates/runbook.md` | `docs/runbooks/[service-name].md` | `observability-and-instrumentation` | Operational triage, service health SLOs, diagnostic commands, and recovery runbooks. |
| **10. Evolution** | `templates/deprecation-notice.md` | `docs/migrations/[slug]-deprecation.md` | `deprecation-and-migration` | Sunset timeline, breaking change warnings, and 4-phase Expand/Contract migration instructions. |
| **11. Learning** | `templates/experiment-brief.md` | `docs/experiments/[exp-id]-[slug].md` | `ab-testing` | A/B testing design, falsifiable hypothesis, sample sizing, variants, and statistical results. |
| **11. Learning** | `templates/tracking-plan.md` | `docs/analytics/tracking-plan.md` | `analytics` | Event tracking taxonomy, trigger conditions, property schemas, and privacy guardrails. |
| **12. Security** | `templates/threat-model.md` | `docs/security/threat-model-[system].md` | `threat-model-analyst` | STRIDE-A threat analysis, data flow diagrams (DFD), trust boundaries, and mitigations. |
| **14. Governance** | `templates/constitution.md` | `AGENTS.md` / `docs/constitution.md` | `context-engineering`, `writing-for-agents` | Project constitution, agent guardrails, coding conventions, and architectural invariants. |

---

## 3. Scaffolding Automation

To scaffold any canonical artifact instantly, use the CLI tool:
```bash
python scripts/scaffold.py <alias> --id <id> [--title <title>]
```

Supported aliases: `brief`, `prd`, `spec`, `srs`, `rtm`, `arch`, `adr`, `design`, `plan`, `tasks`, `handoff`, `acceptance`, `pr`, `release`, `checklist`, `postmortem`, `runbook`, `deprecation`, `experiment`, `tracking`, `threat-model`, `constitution`.
