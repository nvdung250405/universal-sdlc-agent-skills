# Tasks: [FEATURE_NAME]

Inputs: [feature spec], [plan], [technical design], [contracts]  
Feature ID: `FEAT-NNN`

## Task list

Format: `T-NNN [P?] [FR/Story] Task summary` where `P` marks safe independent parallelism. Each task has concrete file paths, a verification method and a completion condition.

- [ ] T-001 [FR-AREA-001] [Task verb + outcome]
  - Depends on: [T-... or none]
  - Files: `path/to/file`, `path/to/test`
  - Acceptance: [observable behavior]
  - Verify: `[exact command]` and expected result
  - Risk/rollback: [..]

## Execution contract
- Execute in dependency order; do not start dependent tasks before prerequisites are verified.
- Keep one coherent slice at a time. Add/update tests with behavioral code.
- Do not silently alter the spec, API contract, database schema or quality gate; propose an amendment.
- Mark complete only after recording actual verification evidence.

## Final checks
- [ ] All tasks are complete or explicitly deferred with owner/reason
- [ ] Tests/build/lint run and results recorded
- [ ] Acceptance criteria and requirement IDs mapped
- [ ] Review/security gates completed when applicable
