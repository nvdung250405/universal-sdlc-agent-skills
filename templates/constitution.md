# [PROJECT_NAME] Engineering Constitution

Version: [SEMVER]  
Ratified: [YYYY-MM-DD]  
Last amended: [YYYY-MM-DD]

## Core principles

### 1. Requirement and evidence traceability
Every non-trivial change MUST link to an accepted requirement or explicitly record why no formal requirement is needed. Completion claims MUST cite observed test/build/review evidence.

### 2. Tests protect behavior
Behavioral changes MUST include appropriate tests. A failing test, build, lint or security gate MUST NOT be deleted, weakened or bypassed merely to obtain a green result.

### 3. Interfaces and data need owners
Public API, shared schema, migration and architecture-boundary changes MUST be documented and reviewed before implementation when the decision is material or hard to reverse.

### 4. Secure by default
Secrets MUST NOT be committed. Input validation, least privilege, safe error handling and dependency risk MUST be considered for exposed or sensitive paths.

### 5. Small, reversible changes
Work SHOULD be delivered in small slices with explicit acceptance and rollback strategy. Destructive operations and production changes require an explicit human gate.

## Project-specific constraints

- Stack and supported runtimes: [FILL]
- Required commands (tests/build/lint/type check): [FILL]
- Coverage/performance/accessibility/security thresholds: [FILL; use measured baseline if no threshold exists]
- Architecture boundaries and forbidden dependencies: [FILL]
- Data retention, privacy and compliance requirements: [FILL]

## Governance

Changes to this constitution require review by [OWNER/ROLE]. A change that lowers a quality threshold must document the reason, affected risk, approver and expiry/revisit date. The agent MUST NOT amend this file to make its own change pass without approval.
