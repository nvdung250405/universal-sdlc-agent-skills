# Build verification report

- Build date: 2026-10-24
- Scope: static pack (47 skills), templates, manifests, local sync transaction tests and installer dry-run.

## Results

| Check | Result | Evidence |
|---|---|---|
| Strict pack lint | PASS | `python scripts/lint_pack.py --strict` — 47 skills, 0 errors, 0 warnings, complete: true |
| Unit tests | PASS | `python -m unittest discover -s tests -v` — 14 tests (11 PackStaticTests + 3 SyncTransactionTests) |
| Python syntax compilation | PASS | `python -m compileall -q scripts tests` |
| Frontmatter validation | PASS | All 47 SKILL.md use only allowed frontmatter keys |
| Provenance hash coverage | PASS | All 47 skills have provenance records; all adapted skills have content_sha256 |
| Skill map coverage | PASS | All 47 skills assigned to exactly one skill-map group |
| Third-party license files | PASS | 8/8 derived sources have LICENSE in third_party/ |
| Installer dry-run (37 core) | PASS | `python scripts/install.py custom --dest ... --dry-run` |
| Installer with-extras (47 total) | PASS | `python scripts/install.py custom --dest ... --with-extras --dry-run` |

## Pack composition at this build

| Tier | Count | Sources |
|---|---|---|
| Core skills | 37 | 25 sync-managed (Addy×18, Superpowers×6, Anthropic×1) + 9 adapted (Uxcel×3, SDLC-Kit×2, Hobson×2, sickn33×1, api-contract-testing×1) + 3 pack-owned |
| Extras | 10 | 4 sync-managed (Addy×3, Anthropic×1) + 6 adapted (Hobson×2, sickn33×4) |

## Limitations

- No real agent session was run. This report does not establish behavioral compatibility or successful end-to-end SDLC execution across agents.
- A live sync/fetch against GitHub was not run in this build environment. Addy, Superpowers and Anthropic skills remain locked to the source revisions recorded in `upstream.json` / `manifests/upstream-lock.json`.
- Nine adapted skills (Uxcel ×3, SDLC-Kit ×2, wshobson ×2, sickn33 ×1, api-contract-testing ×1) are local adaptations. Source files were reviewed, but source revisions are not pinned to a commit SHA; the stored `content_sha256` detects local content drift, not upstream revision identity. These require manual upstream review before refreshing.
- Adapter dry-runs validate configured destination paths, not the vendors' live discovery behavior. Verify current agent path conventions when installing.
