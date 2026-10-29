# Telemetry & Event Tracking Plan: [FEATURE_OR_APPLICATION_NAME]

- **Status**: Draft | Implemented | Verified
- **Owner**: [Analytics Lead / Agent]
- **Date**: [YYYY-MM-DD]
- **Target Platforms**: Web (GA4 / Mixpanel) | Mobile | Backend API
- **Canonical Path**: `docs/analytics/tracking-plan.md`

---

## 1. Tracking Principles & Naming Conventions
- **Naming Pattern**: `noun_action` in lower_snake_case (e.g., `checkout_started`, `button_clicked`).
- **Standard Global Properties** attached to every event:
  - `user_id`: Unique persistent identifier (or `null` if anonymous).
  - `session_id`: Unique session string.
  - `platform`: `web` | `ios` | `android`.
  - `app_version`: Semantic version string.
  - `timestamp_utc`: ISO 8601 UTC timestamp.

---

## 2. Event Taxonomy & Dictionary

| Event Name | Trigger Condition | Required Properties | Optional Properties | Destination Tool |
|---|---|---|---|---|
| `signup_completed` | User finishes registration and confirms email | `method` (email, google, github) | `referral_code` | GA4, Mixpanel, Warehouse |
| `checkout_initiated`| User clicks "Proceed to Checkout" | `cart_id`, `item_count`, `currency`, `total_amount` | `coupon_applied` | GA4, Mixpanel |
| `feature_used` | User executes core action (e.g. export report) | `feature_id`, `duration_ms` | `export_format` | Mixpanel, PostHog |

---

## 3. Detailed Property Schemas

### `checkout_initiated`
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "cart_id": { "type": "string" },
    "item_count": { "type": "integer", "minimum": 1 },
    "currency": { "type": "string", "enum": ["USD", "EUR", "VND"] },
    "total_amount": { "type": "number", "minimum": 0 },
    "coupon_applied": { "type": "string" }
  },
  "required": ["cart_id", "item_count", "currency", "total_amount"]
}
```

---

## 4. Privacy & Compliance Guardrails
- [x] **No PII in telemetry**: Passwords, email addresses, credit card numbers, and physical addresses must NEVER be passed as event properties.
- [x] **Consent Enforcement**: Tracking disabled if user rejects cookie/telemetry banner.

---

## 5. Verification & Testing Checklist
- [ ] Events verified via DebugView / Network tab (`collect` payload verified).
- [ ] Property types match schema (no numbers passed as stringified values).
- [ ] Duplicate event firing prevented on page reloads or rapid clicks.

