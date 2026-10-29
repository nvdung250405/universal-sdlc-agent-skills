# Operational Runbook: [SERVICE_OR_SUBSYSTEM_NAME]

- **Service / Component**: [Name]
- **Primary Owner / Team**: [Team / Contact Channel]
- **Repository**: [Repo URL / Local Path]
- **Last Verified**: [YYYY-MM-DD]
- **Canonical Path**: `docs/runbooks/[service-name].md`

---

## 1. System Overview & Architecture

### Service Purpose
[What does this service do? Which core user journeys depend on it?]

### Key Dependencies & Upstreams / Downstreams
- **Upstreams**: [Services calling this component]
- **Downstreams**: [Databases, queues, external APIs called by this component]

---

## 2. Service Health & SLOs

| Metric | Target (SLO) | Alert Threshold | Dashboard Link |
|---|---|---|---|
| Availability | 99.9% uptime | < 99.5% over 5m | [Dashboard URL] |
| Latency (p95) | < 200 ms | > 500 ms over 5m | [Dashboard URL] |
| Error Rate | < 0.1% HTTP 5xx | > 1.0% HTTP 5xx | [Dashboard URL] |

---

## 3. Common Alerts & Triage Procedures

### Alert: `HighErrorRate5xx`
- **Symptom**: HTTP 5xx response rate spikes above 1%.
- **Initial Diagnostics**:
  ```bash
  # Check recent error logs
  kubectl logs -l app=[service-name] --tail=100 | grep "ERROR"
  # Check database connection pool health
  curl -s http://localhost:8080/metrics | grep "db_pool"
  ```
- **Immediate Mitigation**:
  1. If related to recent deployment: Initiate immediate rollback.
  2. If caused by downstream timeout: Enable circuit breaker flag via config.

### Alert: `HighMemoryUsage / OOMKilled`
- **Symptom**: Pods restart frequently with exit code 137.
- **Immediate Mitigation**:
  1. Temporarily increase replica count or memory limit in deployment manifest.
  2. Capture heap dump for investigation: `kill -3 <pid>` or runtime profiler.

---

## 4. Routine Operations & Maintenance

### Graceful Restart
```bash
kubectl rollout restart deployment/[service-name]
```

### Database Migration Execution
```bash
./scripts/run-migrations.sh --dry-run
./scripts/run-migrations.sh --execute
```

### Drain & Traffic Shift
```bash
# Shift traffic away from unhealthy canary or node
kubectl cordon [node-name]
```

---

## 5. Escalation Contacts
- **Primary On-Call**: PagerDuty / Slack: `#[team-oncall]`
- **Secondary / Lead Engineer**: [Contact info]
- **Security Escalation**: `security@[domain.com]`

