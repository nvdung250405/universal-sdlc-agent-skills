# Pull Request: [SHORT_SUMMARY_OF_CHANGE]

- **Type**: Feature | Bugfix | Refactor | Performance | Security | Docs
- **Related Spec / Issue**: Fixes #`[ISSUE_NUMBER]` / Implements `docs/features/[feature-id]/spec.md`
- **Author**: [Name / Agent]

---

## 1. Summary of Changes
[Concise explanation of what changes were made and why. Highlight any key architectural or interface modifications.]

- Change 1: [Brief description]
- Change 2: [Brief description]

---

## 2. Motivation & Context
[Why was this change necessary? What user problem, bug, or technical debt does it resolve?]

---

## 3. Verification & Test Evidence

> [!IMPORTANT]
> Evidence before assertions: list the commands actually executed and include real output summaries.

### Commands Executed
```bash
# Unit & integration tests
pytest tests/ -v
# or npm test

# Linting and type-checking
python scripts/lint_pack.py --strict
# or npm run typecheck
```

### Verification Results
- [x] All unit tests passed (`[X] passed in [Y]s`)
- [x] Strict linting and formatting passed (0 errors, 0 warnings)
- [x] Manual / Browser verification completed (screenshots or curl output attached if applicable)

---

## 4. Breaking Changes & Migration Steps
- [ ] **Breaking changes introduced?** (Yes / No)
- If yes, describe migration steps:
  - [Step 1: Run database migration `xyz`]
  - [Step 2: Update environment variable `ABC`]

---

## 5. Reviewer Checklist
- [ ] Code adheres to project style, conventions, and deep module boundaries.
- [ ] No unexplained telemetry, credential exposure, or insecure dependencies.
- [ ] Edge cases and failure modes are explicitly handled.
- [ ] Documentation and architectural decision records are updated if applicable.
