# Feature Specification: [FEATURE_NAME]

- Feature ID: `FEAT-NNN`
- Status: Draft | In Review | Approved | Superseded
- Owner: [ROLE/TEAM]
- Last updated: [YYYY-MM-DD]
- Related Epic(s): [EPIC-...]
- Related system requirements: [FR-..., NFR-...] (when applicable)

> This is the canonical feature artifact. Keep detailed User Stories and Acceptance Criteria here unless the project explicitly chooses another single authoritative location. Do not maintain duplicate Story/AC records across multiple files.

## 1. Problem and objective
[Problem/evidence, affected users, why this matters, expected value. Mark unvalidated assumptions explicitly.]

## 2. Scope
### In scope
- [Capability]

### Out of scope
- [Explicit exclusions]

## 3. Actors and business rules
- **Actors/personas:** [Relevant roles]
- **Business rules:** [Rules with a source/owner, or `None identified`]
- **Constraints/dependencies:** [Relevant constraints]

## 4. User Stories and Acceptance Criteria

### US-FEAT-NNN-001 — [Story title]
- **Priority:** P1 | P2 | P3 (or the project's agreed scale)
- **Story:** As a [user/persona], I want [capability], so that [value/outcome].
- **Independent test:** [How this story can be verified independently]
- **Dependencies:** [Other stories/contracts, or None]

#### Acceptance Criteria

**AC-FEAT-NNN-001 — [Scenario title]**

- **Given:** [Initial context/preconditions]
- **When:** [User action or system event]
- **Then:** [Observable and testable result]

**AC-FEAT-NNN-002 — [Error/edge scenario title]**

- **Given:** [Relevant invalid, boundary or failure condition]
- **When:** [Action or event]
- **Then:** [Expected observable behavior]

#### Story notes
- **Edge cases:** [Relevant boundary, empty, duplicate, unauthorized, unavailable, retry or concurrency cases]
- **Open questions:** [Unresolved decisions; do not silently invent answers]

> Repeat the Story block for each independently valuable slice. Given/When/Then is the default for behavioral scenarios; do not force system constraints or non-functional requirements into artificial User Stories.

## 5. Functional requirements (when needed)
| ID | Requirement (testable, one obligation) | Priority | Source | Acceptance/evidence |
|---|---|---|---|---|
| FR-FEAT-NNN-001 | The system MUST ... | Must | [source] | [observable result/test] |

## 6. Non-functional requirements and constraints (when needed)
| ID | Quality attribute | Measurable requirement | Verification method |
|---|---|---|---|
| NFR-FEAT-NNN-001 | Performance/Security/Availability/etc. | [Threshold or behavior, or mark TBD with owner] | [Command/measurement] |

## 7. Data and external contracts
- Entities/data ownership: [..]
- API/events/integrations: [..]
- Authorization/privacy/retention: [..]
- Compatibility and migration: [..]

## 8. Outcome / success criteria (when applicable)
| ID | Outcome | Baseline | Target | How measured |
|---|---|---|---|---|
| SC-001 | [User/business/system outcome] | [baseline/unknown] | [target] | [measurement] |

## 9. Assumptions and open questions
- **Assumptions:** [Mark validation status and owner]
- **Blocking questions:** [Question, owner, needed-by]

## 10. Verification and approval gate
- [ ] Problem, value and scope are clear enough for this feature's risk level
- [ ] Stories represent user value and are split to a reasonable, independently verifiable size
- [ ] Acceptance Criteria are observable and testable; important error/edge paths considered
- [ ] Requirement/contract references are traceable when needed
- [ ] Security, privacy, compatibility and migration impacts considered when relevant
- [ ] Open questions are resolved or explicitly accepted by the right owner
- Reviewer / decision / date: [..]
