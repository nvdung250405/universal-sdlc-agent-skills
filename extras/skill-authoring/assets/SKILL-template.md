---
name: example-skill
description: Performs one defined capability for concrete situations. Use when the request asks to [specific trigger] or when [observable condition] is present.
---

# Purpose

State the capability and the problem it owns. Do not duplicate another skill's primary responsibility.

## Inputs and preconditions

- Required input:
- Existing artifacts or project conventions to inspect:
- Preconditions and constraints:

## Procedure

1. Inspect the authoritative source artifacts before making assumptions.
2. Perform the smallest ordered set of actions that achieves the goal.
3. Preserve existing project conventions and record material decisions.
4. If required information or a capability is unavailable, state the blocker and use a safe fallback where possible.

## Outputs

List the exact files, artifacts, or findings to produce. Use project-relative paths and stable IDs where appropriate.

## Verification

Define observable checks and commands. Distinguish checks run from checks not run.

## Stop or escalate when

- The scope is ambiguous in a way that could change the design or outcome.
- A destructive, production, security-sensitive, or irreversible action requires approval.
- Required evidence, permissions, tools, or source files are unavailable.
