# Requirements Traceability Matrix (RTM)

Stable IDs: `FR-*`, `NFR-*`, `UC-*`, `ADR-*`, `FEAT-*`, and test IDs are never recycled. Retire entries instead of deleting them.

| Requirement ID | Requirement summary / status | Use case | Architecture / ADR | Feature / plan | Detailed design / contract | Test / acceptance evidence |
|---|---|---|---|---|---|---|
| FR-AREA-001 | [summary; Active/Retired] | UC-001 | ADR-001 | FEAT-001 | [path/section] | [test ID, command, result] |

## Ownership rules
- Requirements owner: creates IDs and edits requirement text/status.
- Architecture owner: adds architecture/ADR references; does not rewrite requirement semantics.
- Planning owner: maps requirements to feature/plan IDs.
- Detailed design owner: appends design/contract references.
- QA/acceptance owner: adds test references only after evidence is observed.

## Verification status
Do not manually mark a requirement “verified” merely because a task is complete. Verification requires an acceptance test/evidence reference and an observed passing result. Record partial coverage or blocked checks explicitly.
