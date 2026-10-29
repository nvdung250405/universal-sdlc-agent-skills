# Release readiness checklist

## Quality and security
- [ ] Required tests, build, lint and type checks ran; exact results are recorded.
- [ ] Acceptance report is Verified or approved exceptions are documented.
- [ ] Code review findings are resolved or explicitly accepted.
- [ ] Security/dependency/secret checks ran when applicable.

## Deployment safety
- [ ] Version, scope, migrations and dependencies are known.
- [ ] Backward compatibility and configuration changes are understood.
- [ ] Rollback/roll-forward plan has been exercised or reviewed.
- [ ] Secrets are provisioned through approved channels, not committed.
- [ ] Human approval for production/destructive action is recorded.

## Operations
- [ ] Logs/metrics/traces and health checks cover critical paths.
- [ ] Alerts and rollback triggers have owners and thresholds.
- [ ] Runbook/support notes and release notes are available.
- [ ] Post-deploy smoke test is defined and has an owner.

## Decision
- [ ] GO / NO-GO is recorded with owner, time, evidence and known risks.
