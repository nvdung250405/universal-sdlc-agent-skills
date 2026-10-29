# Incident Postmortem: [INCIDENT_NAME_OR_ID]

- **Incident Date**: [YYYY-MM-DD]
- **Incident Severity**: SEV-1 (Critical) | SEV-2 (Major) | SEV-3 (Minor)
- **Incident Commander / Lead**: [Name / Agent]
- **Status**: Complete | Action Items Pending
- **Canonical Path**: `docs/incidents/[YYYYMMDD-incident-slug]/postmortem.md`

---

## 1. Executive Summary
[Brief 1-paragraph summary describing what failed, the customer impact, and the ultimate resolution.]

- **Duration of Outage**: [e.g., 47 minutes]
- **Total Impacted Users / Requests**: [e.g., ~12% of API traffic returned HTTP 500]
- **Data Loss**: None | Identified and recovered

---

## 2. Timeline (All times in UTC)

| Time (UTC) | Event Description |
|---|---|
| `HH:MM` | Deployment `v1.4.2` begins in production. |
| `HH:MM` | Alert fires: `HighHttp5xxRate` on API Gateway (> 2%). |
| `HH:MM` | Incident responder acknowledges page and opens war room. |
| `HH:MM` | Rollback initiated to `v1.4.1`. |
| `HH:MM` | Traffic normalizes; error rates drop below 0.01%. Incident resolved. |

---

## 3. Root Cause Analysis (5 Whys)

1. **Why did the API return 500 errors?**
   - The database connection pool was exhausted.
2. **Why was the connection pool exhausted?**
   - New database queries in the auth middleware did not release connections on timeout.
3. **Why did the queries timeout?**
   - Missing index on the `user_tokens.expires_at` column caused full table scans under load.
4. **Why was the index missing in production?**
   - The migration ran in staging but was not applied during production deploy due to a pipeline script flag error.
5. **Why was the failure not caught before production?**
   - Staging test suites did not simulate connection saturation with unindexed volume.

---

## 4. Trigger & Contributing Factors
- **Trigger**: Deployment of commit `abcdef` with unindexed query.
- **Contributing Factors**:
  - Alert threshold on pool saturation was set too high.
  - Staging environment had 1/1000th of production table size.

---

## 5. What Went Well vs. What Went Poorly

### What Went Well
- Monitoring alerts detected the anomaly within 3 minutes of deploy.
- Rollback executed cleanly without requiring database restore.

### Where We Got Lucky or Struggled
- Runbook for connection pool recovery was outdated.
- Log volume overwhelmed triage search during the first 10 minutes.

---

## 6. Action Items (Preventative & Corrective)

| Action Item | Type | Owner | Target Date | Tracking Ticket |
|---|---|---|---|---|
| Add composite index on `user_tokens(user_id, expires_at)` | Fix | [Dev Name] | YYYY-MM-DD | #[TICKET] |
| Add CI pipeline gate checking migration execution parity | Prevention | [DevOps] | YYYY-MM-DD | #[TICKET] |
| Update operational runbook with connection pool drain command | Docs | [Agent/Dev] | YYYY-MM-DD | #[TICKET] |

