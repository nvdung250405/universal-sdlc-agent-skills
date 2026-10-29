# Full SDLC workflow

Use for new systems, major capabilities, complex integrations, or material-risk initiatives. This workflow coordinates the pack's 16 SDLC stages, applying Demand-Driven Skill Loading and the canonical artifact contract. Skip artifacts that add no value and record why.

---

## 1. Discovery & Problem Framing (Stage 1)
1. Read repository context, existing architectural constraints, and constitution (`AGENTS.md` / `constitution.md`).
2. If problem statement or target users are ambiguous, run `interview-me` and `idea-refine`.
3. Use `customer-research` when user interview transcripts, customer support logs, or market alternatives need synthesis.
4. Scaffold and write `docs/discovery/[initiative]/opportunity-brief.md` (from `templates/opportunity-brief.md`) to capture problem framing, target persona, and initial hypotheses.

## 2. Requirements & Product Definition (Stage 2)
5. Use `pm-product-spec` to author or update `docs/prd.md` (from `templates/PRD.md`) with evidence, measurable outcomes, epics, non-goals, and risks.
6. Run `pm-spec-quality-audit` on significant PRD changes to catch build-damaging ambiguities, hidden assumptions, or missing flows early.
7. For each user-facing capability, use `pm-user-story` to author Story blocks and Given/When/Then Acceptance Criteria inside `docs/features/<feature-id>/spec.md` (from `templates/feature-spec.md`). Do not create separate duplicate story files.
8. Run formal `requirements-engineering` only when formal system specifications (`docs/specs/SRS.md`) or regulatory traceability (`docs/specs/RTM.md`) are required.

## 3. Architecture, Deep Design & Security (Stages 3 & 12)
9. Use `software-architecture` to establish component boundaries, C4 models, and data ownership in `docs/architecture.md` (from `templates/architecture-overview.md`).
10. Use `codebase-design` for deep module seams, `domain-modeling` for ubiquitous domain language, and `database-design` for persistence schema, normalization, and indexing strategy.
11. Run `threat-model-analyst` to produce a STRIDE-A threat model, data flow diagram (DFD), and abuse case mitigations in `docs/security/threat-model-[system].md` (from `templates/threat-model.md`). Coordinate with `security-and-hardening`.
12. Use `documentation-and-adrs` to record material architectural decisions and trade-offs in `docs/adr/ADR-NNN-[slug].md` (from `templates/ADR.md`).

## 4. Planning, Breakdown & Execution Strategy (Stage 4)
13. Use `planning-and-task-breakdown` as the **sole owner** of the final task list in `docs/features/<feature-id>/tasks.md` (from `templates/tasks.md` and `templates/plan.md`). Include explicit dependency edges, exact target file paths, and automated verification commands.
14. Use `to-tickets` when breaking plans into standalone tracer-bullet tickets with blocking links.
15. Use `subagent-driven-development` when orchestrating parallel implementation across isolated subagent workspaces.

## 5. Construction & Implementation Loop (Stage 5)
16. Implement in thin, verifiable slices using `incremental-implementation`.
17. Drive behavioral changes through tests with `test-driven-development` (red-green-refactor loop).
18. Ground framework and API usage in official documentation via `source-driven-development`.
19. Apply stack-specific specialist skills when relevant: `vercel-react-best-practices` (Next.js/React), `auth-implementation-patterns` (OAuth/OIDC/RBAC), `docker-expert` (containers).
20. When tests fail or bugs appear, invoke `systematic-debugging`: reproduce, isolate, state hypothesis, verify cause, and write regression guard before fixing.

## 6. Testing, Verification & Benchmarking (Stage 6)
21. Run unit, integration, and wire-level contract tests using `api-contract-testing` for client-provider interfaces.
22. Execute browser automation with `webapp-testing` (Playwright) or `browser-testing-with-devtools` (DevTools MCP).
23. Run load, stress, and scalability benchmarks with `k6-load-testing` when throughput or latency SLAs are critical.
24. Audit accessibility compliance with `screen-reader-testing` and `web-design-guidelines` for public web surfaces.

## 7. Review, Quality Gates & Acceptance (Stage 7)
25. Conduct multi-axis code review with `code-review-and-quality`; invoke `receiving-code-review` when processing human or reviewer feedback.
26. Generate the pull request description from `templates/pull-request.md` with explicit summary, motivation, and commands run.
27. Run `verification-before-completion` to gather fresh, empirical test evidence. Record acceptance in `docs/features/<feature-id>/acceptance-report.md` (from `templates/acceptance-report.md`).

## 8. Release, Deployment & Cost Governance (Stages 8 & 16)
28. Prepare release notes and changelog in `docs/releases/v[X.Y.Z].md` (from `templates/release-notes.md`) using `git-workflow-and-versioning` for semantic tagging.
29. Validate deployment safety and rollback procedures against `templates/release-checklist.md` with `shipping-and-launch` and `ci-cd-and-automation`.
30. Audit cloud spending and resource rightsizing with `cost-optimization` before production rollout.
31. Production deployments and destructive actions require explicit human authorization.

## 9. Operations, Observability & Learning (Stages 9, 11 & 15)
32. Configure dashboards, error alert thresholds, and SLO tracking with `observability-and-instrumentation` and `service-mesh-observability`.
33. Publish component runbook in `docs/runbooks/[service-name].md` (from `templates/runbook.md`).
34. For post-launch telemetry and experimentation, define tracking taxonomy in `docs/analytics/tracking-plan.md` (`analytics`) and experiment design in `docs/experiments/[id].md` (`ab-testing`).
35. For production anomalies or outages, transition immediately to `workflows/incident-response.md`.

---

## Control Rules
- **Single Source of Truth:** One canonical artifact per scope; do not create duplicate PRDs, feature specs, or competing task lists.
- **Evidence Before Claims:** A planned test is not evidence; always report exact commands run and real terminal output.
- **Zero Fabricated Requirements:** If requirements are contradictory or missing, amend the owning spec instead of inventing behavior in code.
