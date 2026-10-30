# Full SDLC workflow (System & Initiative Lifecycle)

Use for new systems, major capabilities, complex integrations, or material-risk initiatives. This workflow coordinates foundational system establishment, enforces cross-cutting stage-gate reviews at every hand-off, delegates individual capabilities to `workflows/feature-loop.md`, and governs release readiness, observability, and operations.

Activities are iterative, overlapping, and non-linear. Skip artifacts that add no value and record why.

---

## Discovery
1. Read repository context, existing architectural constraints, and constitution (`AGENTS.md` / `constitution.md`).
2. If problem statement or target users are ambiguous, run `interview-me` and `idea-refine`.
3. Use `customer-research` when user interview transcripts, customer support logs, or market alternatives need synthesis.
4. Scaffold and write `docs/discovery/[initiative]/opportunity-brief.md` (from `templates/opportunity-brief.md`) to capture problem framing, target persona, and initial hypotheses.
5. **Stage-Gate Review (Discovery Hand-off):** Verify problem clarity and evidence validity. If the problem framing remains speculative or ungrounded, pause and revisit `interview-me` before authoring product requirements.

## Requirements
6. Use `pm-product-spec` to author or update `docs/prd.md` (from `templates/PRD.md`) with problem evidence, measurable outcomes, epic breakdowns, non-goals, and identified risks.
7. Run formal `requirements-engineering` only when formal system specifications (`docs/specs/SRS.md`) or regulatory traceability (`docs/specs/RTM.md`) are required.
8. **Stage-Gate Review (Requirements Hand-off via Cross-Cutting Audit):**
   - Run `pm-spec-quality-audit` on `docs/prd.md` to identify build-damaging ambiguities, missing alternative flows, hidden assumptions, or unmeasurable acceptance criteria.
   - Run `writing-guidelines` / `writing-for-agents` to ensure requirements are clear, concise, and unambiguous for autonomous agents.
   - **Gate Decision:** If *Critical* or *High-severity* gaps are uncovered, do not proceed to Architecture. Return to Step 6 to resolve requirements deficiencies first.

## Architecture & System Design
9. Use `software-architecture` to establish component boundaries, C4 models, subsystem responsibilities, and data ownership in `docs/architecture.md` (from `templates/architecture-overview.md`).
10. Establish **Centralized System Contracts (Contract-First)**:
    - Use `api-and-interface-design` to define top-level inter-service contracts, public API gateway specifications (OpenAPI/REST, GraphQL, gRPC `.proto`), and shared asynchronous event schemas before designing internal storage.
    - Use `domain-modeling` to unify domain entities, value objects, and ubiquitous language across all subsystem boundaries.
    - Use `codebase-design` to define deep module seams and interface segregation.
    - Apply `api-contract-testing` to generate wire-level compatibility fixtures and provider-consumer contract tests based on these centralized specifications.
11. Define persistence architecture: select database engines (relational/document/time-series), replication, and data partitioning strategies. Align persistence models to support the established system contracts.
12. Use `documentation-and-adrs` to record material architectural decisions and trade-offs in `docs/adr/ADR-NNN-[slug].md` (from `templates/ADR.md`).
13. **Stage-Gate Review (Architecture Hand-off via Security & FinOps):**
    - Run `threat-model-analyst` to produce a STRIDE-A threat model, data flow diagram (DFD), and abuse case mitigations in `docs/security/threat-model-[system].md` (from `templates/threat-model.md`). Coordinate with `security-and-hardening` to verify trust boundaries.
    - Run `cost-optimization` to evaluate infrastructure sizing, token budgets, and multi-cloud architectural cost feasibility.
    - **Gate Decision:** If unmitigated critical security risks or unsustainable cost projections exist, halt progression. Revise architecture and ADRs in Step 9–12 before delegating construction.

## Platform & Developer Experience (cross-cutting setup)
14. Configure automated quality gates, linting, and commit-time formatting using `setup-pre-commit` and `git-guardrails-claude-code`.
15. Establish base containerization or build environments using `docker-expert` or platform templates when containerized delivery is needed.

## Implementation & Construction (Feature Loop Delegation)
16. For each epic or capability defined in `docs/prd.md`:
    - Transition to `workflows/feature-loop.md` to author the canonical feature specification (`docs/features/<feature-id>/spec.md` with `pm-user-story`), plan tasks (`docs/features/<feature-id>/tasks.md` with `planning-and-task-breakdown`), and execute the TDD construction loop (`incremental-implementation`, `test-driven-development`).
    - Use `subagent-driven-development` when orchestrating independent feature loops in parallel across isolated subagent workspaces.
    - Record active execution progress and role hand-offs using `task-handoff` (`.agent/tasks/<task-id>.md`).
    - Collect empirical verification evidence for each capability before completing its slice.

## Testing & Verification
17. Verify cross-service integration contracts and wire compatibility using `api-contract-testing`.
18. Execute end-to-end automated flows with `webapp-testing` (Playwright) or `browser-testing-with-devtools` (Chrome DevTools MCP).
19. Run load, stress, and scalability benchmarks with `k6-load-testing` when throughput or latency SLAs are critical.
20. Audit accessibility compliance with `screen-reader-testing` and `web-design-guidelines` for public web surfaces.

## Review & Acceptance
21. Conduct multi-axis code review with `code-review-and-quality`; invoke `receiving-code-review` when processing human or reviewer feedback.
22. Generate the pull request description from `templates/pull-request.md` with explicit summary, motivation, and commands run.
23. **Stage-Gate Review (Acceptance Gate):**
    - Run `verification-before-completion` to gather fresh, empirical test evidence across the whole system.
    - Record overall acceptance verification in `docs/features/<feature-id>/acceptance-report.md` (from `templates/acceptance-report.md`).
    - **Gate Decision:** If any required check fails, regressions appear, or test evidence is missing, do not proceed to release. Loop back to Implementation or Testing to resolve issues.

## Release & Deployment
24. Prepare release notes and changelog in `docs/releases/v[X.Y.Z].md` (from `templates/release-notes.md`) using `git-workflow-and-versioning` for semantic tagging.
25. Validate deployment safety, migration readiness, and rollback procedures against `templates/release-checklist.md` with `shipping-and-launch` and `ci-cd-and-automation`.
26. Audit cloud spending and resource rightsizing with `cost-optimization` before production rollout.
27. Production deployments and destructive actions require explicit human authorization.

## Operations & Incident Response
28. Configure dashboards, error alert thresholds, and SLO tracking with `observability-and-instrumentation` and `service-mesh-observability`.
29. Publish operational runbook in `docs/runbooks/[service-name].md` (from `templates/runbook.md`).
30. For production anomalies or outages, transition immediately to `workflows/incident-response.md`.

## Product Learning & Measurement
31. Define product telemetry taxonomy in `docs/analytics/tracking-plan.md` using `analytics` to measure funnel metrics and adoption.
32. Design and evaluate continuous experiments using `ab-testing` in `docs/experiments/[id].md` (via `workflows/experimentation-loop.md`).

---

## Control Rules
- **Stage-Gate Quality Invariant:** Hand-offs between stages require explicit cross-cutting review. If gate criteria are not satisfied, loop back to the deficient stage rather than advancing.
- **Non-Linear Execution:** Stage titles define capability domains matching the Master Matrix, not rigid sequential waterfall gates. Return to earlier stages whenever new evidence or risks emerge.
- **Single Source of Truth:** One canonical artifact per scope; do not create duplicate PRDs, feature specs, or competing task lists.
- **Evidence Before Claims:** A planned test is not evidence; always report exact commands run and real terminal output.
- **Zero Fabricated Requirements:** If requirements are contradictory or missing, amend the owning spec instead of inventing behavior in code.
