# Skill trigger testing guide

## Build a small test matrix

Use prompts from real tasks instead of repeating the skill name verbatim.

| Case | Expected | Example for a code-review skill |
|---|---|---|
| Positive: explicit | Activate | “Review this diff for correctness and regressions.” |
| Positive: natural wording | Activate | “Can you check what might break in this change?” |
| Positive: artifact-based | Activate | “Compare this PR with the acceptance criteria.” |
| Negative: neighboring role | Do not activate | “Implement the feature described in this ticket.” |
| Negative: unrelated | Do not activate | “Explain this SQL query to a beginner.” |
| Boundary: mixed intent | Prefer the owning workflow | “Review this code and then deploy it to production.” |

## Record results

For each run, record:

- agent and model/version;
- prompt verbatim;
- expected skill and actual skill(s) activated;
- whether the intended procedure completed;
- any tool, path, or capability assumption that failed.

Test both false positives and false negatives. When activation is wrong, first tighten the skill description or the router ownership map. Do not immediately add more instructions to the body: the body is generally read only after activation.

Repeat the same test set after changing `name`, `description`, router rules, adapters, or relevant upstream version. Keep a small regression set in the repository so a future edit does not silently degrade routing.
