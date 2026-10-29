# Role → skill map

| Role | Owns | Primary skills | Main outputs |
|---|---|---|---|
| Orchestrator | Selects workflow and prevents stage skipping | `using-sdlc-skills`, `sdlc-orchestrator`, `task-handoff`, `context-engineering` | task handoff, defect ledger |
| Product / Business Analyst | Problem framing, scope, business rules, requirements | `interview-me`, `idea-refine`, `requirements-engineering`, `spec-driven-development` | brief, SRS, use cases, RTM requirements columns |
| System / Software Architect | System structure, quality attributes, cross-cutting decisions | `software-architecture`, `api-and-interface-design`, `documentation-and-adrs` | architecture, API contracts, ADRs, RTM design refs |
| UX / UI | User flows, screen inventory, design system, accessible UI | `ux-foundations`, `ui-design`, `frontend-ui-engineering` | UX foundations, design tokens, screen manifest |
| Tech Lead / Planner | Feature slicing, ordering, dependencies and tasks | `implementation-planning`, `planning-and-task-breakdown`, `detailed-design` | implementation plan, technical design, tasks |
| Developer | Correct implementation in verified slices | `feature-implementation`, `incremental-implementation`, `test-driven-development`, `debugging-and-error-recovery`, `source-driven-development`, `git-workflow-and-versioning`, `code-simplification` | code, tests, commits, amended docs when approved |
| QA / Acceptance | Independent requirement-level verification | `acceptance-verification`, `browser-testing-with-devtools`, `pipeline-verify` | acceptance report, RTM test refs, verification evidence |
| Reviewer | Finds correctness, maintainability and regression issues | `code-review-and-quality`, `doubt-driven-development`, `pipeline-verify` | prioritized findings with severity and evidence |
| Security | Threats, unsafe trust boundaries, secure defaults | `security-and-hardening`, `code-review-and-quality` | security findings and mitigations |
| DevOps / SRE | CI/CD, release safety, telemetry and rollback | `ci-cd-and-automation`, `shipping-and-launch`, `observability-and-instrumentation`, `initial-deployment` | deploy notes, release gates, telemetry, rollback plan |
| Skill maintainer | Source curation and portability | `skill-authoring` | audited source mapping and portable skill updates |

Some skills become available only after `scripts/sync_upstream.py` downloads the selected upstreams. Run the pack linter before installation to detect incomplete synchronization.
