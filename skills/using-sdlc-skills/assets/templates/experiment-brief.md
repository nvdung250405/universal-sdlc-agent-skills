# Experiment Brief: [EXPERIMENT_NAME]

- **Experiment ID**: `EXP-[NNN]`
- **Status**: Planned | Running | Concluded | Rolled Out | Discarded
- **Owner**: [Product Manager / Growth Lead / Agent]
- **Target Surface**: [Landing Page / Checkout Funnel / Dashboard / Feature X]
- **Canonical Path**: `docs/experiments/[exp-id]-[slug].md`

---

## 1. Hypothesis Statement

> **Because** [qualitative feedback, analytics friction, or user observation],  
> **we believe that** [specific change or variant introduced]  
> **will cause** [expected behavioral or metric outcome]  
> **for** [target user segment / traffic cohort].  
> **We will know this is true when** [primary metric meets statistical significance threshold].

---

## 2. Metrics & Decision Criteria

### Primary Metric (Overall Evaluation Criterion - OEC)
- **Metric Name**: [e.g., Checkout Completion Rate (%)]
- **Current Baseline**: [e.g., 3.2%]
- **Minimum Detectable Effect (MDE)**: [e.g., +10% relative, or +0.32% absolute]
- **Target Statistical Significance**: 95% confidence ($p < 0.05$), Power: 80%

### Secondary / Guardrail Metrics
- **Secondary (Positive Indicators)**: [e.g., Average Order Value, Time to Checkout]
- **Guardrail Metrics (Must Not Degrade)**: [e.g., Page load latency, payment gateway error rate, refund requests]

---

## 3. Experiment Design & Variants

| Variant | Description | Traffic Split | Key Difference |
|---|---|---|---|
| **Control (A)** | Existing baseline implementation | 50% | Original UI / behavior |
| **Treatment (B)**| [Variant description] | 50% | [Specific change, e.g. 1-click checkout button] |

- **Target Audience / Eligibility**: [e.g., All logged-in desktop users in US/EU]
- **Estimated Duration**: [e.g., 14 days to achieve required sample size of ~25,000 users/variant]

---

## 4. Results & Statistical Analysis (Post-Test)

| Variant | Sample Size (N) | Conversions | Conversion Rate | Relative Lift | p-value | Statistically Significant? |
|---|---|---|---|---|---|---|
| **Control (A)** | [N_A] | [C_A] | [Rate_A] | Baseline | — | — |
| **Treatment (B)**| [N_B] | [C_B] | [Rate_B] | [Lift %] | [p] | Yes / No |

### Guardrail Status
- Guardrail metrics impact: [No degradation observed / Note any anomalies]

---

## 5. Rollout Decision & Next Steps
- **Decision**: Ship Treatment B (100% Rollout) | Iterate Variant | Roll Back to Control
- **Key Learnings**: [What did we discover about user preferences or behavior?]
- **Follow-up Experiments**: [Next hypothesis to test]

