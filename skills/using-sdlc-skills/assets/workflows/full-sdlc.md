# Full SDLC workflow (System & Initiative Lifecycle)

Use for new systems, major capabilities, complex integrations, or material-risk initiatives. This workflow coordinates foundational system establishment, delegates individual capabilities to `workflows/feature-loop.md`, and governs release readiness, observability, and operations.

Activities are iterative, overlapping, and non-linear. Skip artifacts that add no value and record why.

---

## 1. Discovery & Problem Framing
1. Read repository context, existing architectural constraints, and constitution (`AGENTS.md` / `constitution.md`).
2. If problem statement or target users are ambiguous, run `interview-me` and `idea-refine`.
3. Use `customer-research` when user interview transcripts, customer support logs, or market alternatives need synthesis.
4. Scaffold and write `docs/discovery/[initiative]/opportunity-brief.md` (from `templates/opportunity-brief.md`) to capture problem framing, target persona, and initial hypotheses.

## 2. Product Definition & Scope Baseline
5. Use `pm-product-spec` to author or update `docs/prd.md` (from `templates/PRD.md`) with problem evidence, measurable outcomes, epic breakdowns, non-goals, and identified risks.
6. Run `pm-spec-quality-audit` on significant PRD changes to catch build-damaging ambiguities, hidden assumptions, or missing flows early.
7. Run formal `requirements-engineering` only when formal system specifications (`docs/specs/SRS.md`) or regulatory traceability (`docs/specs/RTM.md`) are required.

## 3. Contract-First Architecture Baseline, System Contracts & Security
8. Use `software-architecture` to establish component boundaries, C4 models, subsystem responsibilities, and data ownership in `docs/architecture.md` (from `templates/architecture-overview.md`).
9. Establish **Centralized System Contracts (Contract-First)**:
   - Use `api-and-interface-design` to define top-level inter-service contracts, public API gateway specifications (OpenAPI/REST, GraphQL, gRPC `.proto`), and shared asynchronous event schemas before designing internal storage.
   - Use `domain-modeling` to unify domain entities, value objects, and ubiquitous language across all subsystem boundaries.
   - Use `codebase-design` to define deep module seams and interface segregation.
   - Apply `api-contract-testing` to generate wire-level compatibility fixtures and provider-consumer contract tests based on these centralized specifications.
10. Define persistence architecture: select database engines (relational/document/time-series), replication, and data partitioning strategies. Align persistence models to support the established system contracts.
11. Run `threat-model-analyst` to produce a STRIDE-A threat model, data flow diagram (DFD), and abuse case mitigations in `docs/security/threat-model-[system].md` (from `templates/threat-model.md`). Coordinate with `security-and-hardening`.
12. Use `documentation-and-adrs` to record material architectural decisions and trade-offs in `docs/adr/ADR-NNN-[slug].md` (from `templates/ADR.md`).

## 4. Platform, Tooling & Developer Environment
13. Configure automated quality gates, linting, and commit-time formatting using `setup-pre-commit` and `git-guardrails-claude-code`.
14. Establish base containerization or build environments using `docker-expert` or platform templates when containerized delivery is needed.

## 5. Incremental Capability Delivery (Feature Loop Delegation)
15. For each epic or capability defined in `docs/prd.md`:
    - Transition to `workflows/feature-loop.md` to author the canonical feature specification (`docs/features/<feature-id>/spec.md` with `pm-user-story`), plan tasks (`docs/features/<feature-id>/tasks.md` with `planning-and-task-breakdown`), and execute the TDD construction loop (`incremental-implementation`, `test-driven-development`).
    - Use `subagent-driven-development` when orchestrating independent feature loops in parallel across isolated subagent workspaces.
    - Collect empirical verification evidence for each capability before completing its slice.

## 6. System-Level Integration, Verification & Benchmarking
16. Verify cross-service integration contracts and wire compatibility using `api-contract-testing`.
17. Execute end-to-end automated flows with `webapp-testing` (Playwright) or `browser-testing-with-devtools` (Chrome DevTools MCP).
18. Run load, stress, and scalability benchmarks with `k6-load-testing` when throughput or latency SLAs are critical.
19. Audit accessibility compliance with `screen-reader-testing` and `web-design-guidelines` for public web surfaces.

## 7. Review, Quality Gates & Acceptance
20. Conduct multi-axis code review with `code-review-and-quality`; invoke `receiving-code-review` when processing human or reviewer feedback.
21. Generate the pull request description from `templates/pull-request.md` with explicit summary, motivation, and commands run.
22. Run `verification-before-completion` to gather fresh, empirical test evidence across the whole system. Record overall acceptance in `docs/features/<feature-id>/acceptance-report.md` (from `templates/acceptance-report.md`).

## 8. Release, Deployment & Cost Governance
23. Prepare release notes and changelog in `docs/releases/v[X.Y.Z].md` (from `templates/release-notes.md`) using `git-workflow-and-versioning` for semantic tagging.
24. Validate deployment safety, migration readiness, and rollback procedures against `templates/release-checklist.md` with `shipping-and-launch` and `ci-cd-and-automation`.
25. Audit cloud spending and resource rightsizing with `cost-optimization` before production rollout.
26. Production deployments and destructive actions require explicit human authorization.

## 9. Operations, Observability & Learning
27. Configure dashboards, error alert thresholds, and SLO tracking with `observability-and-instrumentation` and `service-mesh-observability`.
28. Publish operational runbook in `docs/runbooks/[service-name].md` (from `templates/runbook.md`).
29. For post-launch telemetry and experimentation, define tracking taxonomy in `docs/analytics/tracking-plan.md` (`analytics`) and experiment design in `docs/experiments/[id].md` (`ab-testing`).
30. For production anomalies or outages, transition immediately to `workflows/incident-response.md`.

---

## Control Rules
- **Non-Linear Execution:** Stages and sections provide capability boundaries, not rigid sequential waterfall gates. Return to earlier sections whenever new discoveries or constraints arise.
- **Single Source of Truth:** One canonical artifact per scope; do not create duplicate PRDs, feature specs, or competing task lists.
- **Evidence Before Claims:** A planned test is not evidence; always report exact commands run and real terminal output.
- **Zero Fabricated Requirements:** If requirements are contradictory or missing, amend the owning spec instead of inventing behavior in code.
