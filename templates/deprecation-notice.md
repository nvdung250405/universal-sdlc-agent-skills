# Deprecation Notice & Migration Guide: [FEATURE_OR_API_NAME]

- **Target Item**: [Endpoint, Module, CLI command, or Schema Column]
- **Current Status**: Deprecated (Warning Active) | Sunset Scheduled | Retired
- **Effective Deprecation Date**: [YYYY-MM-DD]
- **Target Retirement (Removal) Date**: [YYYY-MM-DD]
- **Owner**: [Team / Agent]
- **Canonical Path**: `docs/migrations/[feature-slug]-deprecation.md`

---

## 1. Summary & Motivation

### What is Being Deprecated?
[Clear statement of the exact function, endpoint, or schema component being phased out.]

### Why is it Being Deprecated?
[Explain the reason: security vulnerability, performance bottleneck, replacement by a unified API, or architectural simplification.]

---

## 2. Deprecation & Sunset Timeline

| Phase | Date | Expected Consumer Behavior |
|---|---|---|
| **Announcement** | [YYYY-MM-DD] | Deprecation headers / logs added. New projects must not adopt. |
| **Brownout Window** | [YYYY-MM-DD] | Periodic artificial errors (e.g. 15-min simulated downtime) to catch unmigrated clients. |
| **Final Sunset** | [YYYY-MM-DD] | Complete removal. Endpoints return HTTP 410 Gone. Schema columns dropped. |

---

## 3. Migration Instructions (Before vs. After)

### Before (Deprecated Pattern)
```typescript
// Legacy call
const result = await legacyClient.getUserData({ id: 123 });
```

### After (Recommended Replacement)
```typescript
// Modern replacement with improved typing and caching
const result = await modernClient.users.getById("usr_123", { includeProfile: true });
```

---

## 4. Database Schema Migration (Expand/Contract Phase)
- **Phase 1 (Expand)**: New column/table created and dual-written.
- **Phase 2 (Backfill)**: Historical data migrated via background worker.
- **Phase 3 (Contract)**: Reads switched to new schema; old column marked `deprecated`.
- **Phase 4 (Drop)**: Old column dropped after verification: `ALTER TABLE ... DROP COLUMN ...`.

---

## 5. Support & Communication Channel
- Questions or migration assistance: `#[engineering-support]` or issue #[ISSUE_NUMBER].

