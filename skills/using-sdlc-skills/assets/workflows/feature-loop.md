# Feature development loop

Use for implementing a feature in an existing codebase. Read existing repository context and guidance first. Do not fork a second artifact system.

---

## 1. Specification & Quality Gate
1. Identify feature scope and canonical spec path: `docs/features/<feature-id>/spec.md` (scaffold from `templates/feature-spec.md` if not present).
2. If product intent is unsettled, consult or update `docs/prd.md` with `pm-product-spec`.
3. Use `pm-user-story` to add/refine user-facing stories and Given/When/Then Acceptance Criteria directly inside `docs/features/<feature-id>/spec.md`. For purely technical changes, use a technical spec or ADR instead of fabricating stories.
4. Run `pm-spec-quality-audit` if the specification is complex, ambiguous, or needs a pre-build quality gate.

## 2. Architecture & Design Seams (Conditional)
5. Invoke specialist skills only when the change crosses boundaries:
   - Component boundaries or C4 models: `software-architecture`
   - Database schema or migrations: `database-design`
   - REST/gRPC/GraphQL contract changes: `api-and-interface-design` and `api-contract-testing`
   - Design trade-offs: `documentation-and-adrs` (`docs/adr/ADR-NNN-[slug].md`)
   - Threat boundaries or sensitive data: `threat-model-analyst` and `security-and-hardening`
   - UI styling and design tokens: `frontend-design` and `frontend-ui-engineering`

## 3. Planning & Task Breakdown
6. Use `planning-and-task-breakdown` as the **sole author** of the final `docs/features/<feature-id>/tasks.md` (from `templates/tasks.md`). Every task must specify target file paths, dependencies, acceptance conditions, and exact verification commands.

## 4. Construction & TDD Loop
7. Implement in thin, verifiable slices using `incremental-implementation`.
8. Write tests before code with `test-driven-development` where behavioral tests can drive the implementation. Ground unfamiliar APIs with `source-driven-development`.
9. For unexpected test failures or regressions, invoke `systematic-debugging`: reproduce, isolate root cause, state hypothesis, and add regression guard.

## 5. Review, Verification & Acceptance
10. Run relevant unit, integration, contract, and browser tests (`webapp-testing` or `browser-testing-with-devtools`).
11. Conduct code review using `code-review-and-quality`; prepare PR description using `templates/pull-request.md`.
12. Execute `verification-before-completion` to record fresh empirical evidence in `docs/features/<feature-id>/acceptance-report.md` (from `templates/acceptance-report.md`).
13. Update session handoff log in `.agent/tasks/<task-id>.md` using `task-handoff`.

---

> [!NOTE]
> If implementation uncovers an unexpected architecture, data migration, or security risk larger than initially estimated, pause and route back to the owning design/spec stage before continuing.
