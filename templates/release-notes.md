# Release Notes: v[X.Y.Z]

- **Release Date**: [YYYY-MM-DD]
- **Release Owner / Lead**: [Name / Agent]
- **Target Environment**: Production | Staging
- **Semver Type**: Major (breaking) | Minor (new features) | Patch (bugfixes)

---

## 1. Release Highlights
[A 2-3 sentence executive summary of the most important capabilities or fixes delivered in this release.]

---

## 2. Detailed Changelog

### 🚀 Features & Enhancements
- **[Feature Name]**: [Description of what is new and how users benefit] ([#PR](https://github.com/org/repo/pull/123))
- **[Feature Name]**: [Description] ([#PR](https://github.com/org/repo/pull/124))

### 🐛 Bug Fixes
- **[Fix Title]**: [What issue was fixed and impact] ([#PR](https://github.com/org/repo/pull/125))

### ⚡ Performance & Reliability
- [Optimization description, benchmark improvement, or latency reduction]

### 🔒 Security & Compliance
- [Dependency patch, vulnerability fix, or hardening change]

---

## 3. Breaking Changes & Deprecations
> [!WARNING]
> Highlight any breaking API changes, dropped configs, or schema migrations requiring operator intervention.

- [None or specific breaking change details]

---

## 4. Deployment & Migration Procedures

### Pre-Deployment Checklist
- [ ] Database backup confirmed.
- [ ] Secrets and environment variables configured in target environment.

### Deployment Steps
```bash
# Example migration & deploy commands
migrate up
deploy --version v[X.Y.Z]
```

### Verification & Smoke Tests
- [ ] Healthcheck endpoint returns HTTP 200: `GET /healthz`
- [ ] Critical user journeys verified in production (login, checkout, core workflow).

---

## 5. Rollback Procedure
If p95 latency spikes > 500ms or 5xx error rate exceeds 0.5% during canary:
1. Revert deploy traffic to previous revision `v[X.Y.Z-1]`.
2. Run database rollback if schema migration was backward-incompatible: `migrate down 1`.
3. Notify incident response channel: `#incident-response`.
