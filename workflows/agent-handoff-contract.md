# Cross-agent handoff contract

Every stage or agent handing work to another must provide:

- Task ID and goal.
- Authoritative artifact paths and stable requirement/feature/ADR IDs.
- Decisions made and the rationale; distinguish approved decisions from proposals.
- Files changed and current state of the worktree.
- Commands actually executed, their pass/fail/blocked status, and empirical verification evidence captured via `verification-before-completion`.
- Failed approaches and why they failed.
- Open questions, assumptions and risks.
- The exact next action and its expected output.

Do not pass secrets, credentials, private tokens or personal data into task files. Record handoffs in `.agent/tasks/<task-id>.md` using `templates/task-handoff.md` (via `task-handoff`). Prefer project-relative paths and concise summaries; the next agent should re-read the authoritative file instead of trusting copied excerpts.
