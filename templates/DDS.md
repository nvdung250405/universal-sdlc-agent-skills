# Detailed Design Specification (DDS / LLD): [FEATURE_NAME]

- Feature ID: `FEAT-NNN`
- Related SRS / spec: [path/version]
- Architecture / ADRs: [links]
- Status: Draft | In Review | Approved

## 1. Purpose, scope and boundaries
- Included/excluded behavior:
- Requirement IDs satisfied:
- Existing code/modules affected:

## 2. Design overview
[Component responsibilities and boundaries. Include Mermaid sequence/component diagrams when they clarify behavior.]

## 3. Interfaces and contracts
For every public or cross-module interface, document method/endpoint/event, inputs, outputs, validation, errors, authorization, idempotency, pagination/versioning and compatibility.

| Contract | Input | Output | Failure behavior | AuthN/AuthZ | Requirement IDs |
|---|---|---|---|---|---|

## 4. Data model and persistence
- Entities/tables/collections and relationships:
- Keys, constraints, indexes and invariants:
- Transaction and consistency boundaries:
- Migration/backfill/rollback:
- Privacy, retention and deletion:

## 5. Detailed behavior
### Main flow
### Alternate and error flows
### State machine / concurrency / retries
### Validation and business rules

## 6. Security and privacy
- Trust boundaries and assets:
- Threats and mitigations:
- Secrets and sensitive fields:
- Authorization rules and audit logging:

## 7. Reliability, performance and operations
- Timeouts/retries/idempotency:
- Expected load and performance targets:
- Logs/metrics/traces/alerts:
- Feature flags, rollout and rollback:

## 8. Test design and acceptance
| Requirement/criterion | Test level and scenario | Evidence/command | Owner |
|---|---|---|---|

## 9. Implementation tasks
Link `tasks.md`; do not embed a duplicate task list here.

## 10. Decisions and unresolved questions
- Accepted decisions: [ADR links]
- Proposed changes to upstream design: [approval/status]
- Open questions: [owner/date]

## Design review gate
- [ ] Every relevant requirement is addressed or explicitly out of scope
- [ ] Interfaces, schemas and failure behavior are defined
- [ ] Security/privacy and non-functional requirements have concrete treatment
- [ ] Migration and rollback are described where relevant
- [ ] Design fits the existing codebase and architecture decisions
- [ ] Reviewer approval recorded
