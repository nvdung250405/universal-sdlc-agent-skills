# Quick-change workflow

Use only when scope is unambiguous, risk is low, and the change does not affect public contracts, data migrations, security boundaries or production state.

1. Read the relevant code, repository guidance and applicable skill.
2. State a concise acceptance condition before editing.
3. Implement a small change; add/update tests for behavior.
4. Run targeted checks, then any reasonably fast required project checks.
5. Review the diff for unintended changes and security/regression risks.
6. Report exact evidence and remaining uncertainty.

Escalate to the full feature loop when requirements become ambiguous, several independently testable capabilities appear, or architecture/data/security risks emerge.
