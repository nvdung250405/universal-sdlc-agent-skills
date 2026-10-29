# Bug-fix workflow

1. Capture the observed symptom, expected behavior, environment and available reproduction evidence.
2. Use `systematic-debugging` before changing code: reproduce, isolate, state a hypothesis, test the hypothesis and identify root cause.
3. Add or update a regression test. Use `test-driven-development` where practical; show the pre-fix failure when the test setup permits it.
4. Make the smallest fix that addresses the cause. If expected behavior or a contract is unclear, consult the owning spec/requirement rather than inventing product behavior.
5. Run focused regression tests, relevant suite, build/lint and runtime/browser checks as applicable.
6. Use `code-review-and-quality` for material changes and `security-and-hardening` when trust boundaries, permissions, credentials or sensitive data are involved.
7. Use `verification-before-completion` before reporting the fix as verified. State checks not run and residual risk.
