# Starter Artifact Templates Catalog

Thư mục `templates/` chứa các **khuôn mẫu khởi tạo chuẩn hóa (Starter Templates / Blueprints)** tương ứng trực tiếp với các tạo phẩm thực tế trong 16 giai đoạn của vòng đời phát triển phần mềm ([docs/sdlc-practical-matrix.md](../docs/sdlc-practical-matrix.md)).

---

## 1. Nguyên tắc Khế ước Tạo phẩm (Artifact Contract)

- **100% Canonical Artifacts:** Mỗi template trong thư mục này đại diện cho một tạo phẩm độc lập được quy định trong Matrix. Không chứa file rác, không chứa snippet phân đoạn, không chứa tài liệu nội bộ.
- **Quy trình sử dụng:** Khi bắt đầu một giai đoạn, sao chép template tương ứng sang **đường dẫn chuẩn (canonical path)** của dự án và điền thông tin thực tế.
- **Single Source of Truth:** Tuyệt đối không chỉnh sửa trực tiếp file trong `templates/` cho một feature cụ thể; luôn làm việc trên file tại canonical path.

---

## 2. Bảng Danh mục 22 Templates theo 16 Giai đoạn SDLC

| Stage (Giai đoạn) | Starter Template | Canonical Destination Path | Companion Skills |
| :--- | :--- | :--- | :--- |
| **1. Discovery** | [`opportunity-brief.md`](opportunity-brief.md) | `docs/discovery/[initiative]/opportunity-brief.md` | `interview-me`, `idea-refine`, `customer-research` |
| **2. Requirements** | [`PRD.md`](PRD.md)<br>[`feature-spec.md`](feature-spec.md)<br>[`SRS.md`](SRS.md)<br>[`RTM.md`](RTM.md) | `docs/prd.md`<br>`docs/features/[feature-id]/spec.md`<br>`docs/specs/SRS.md`<br>`docs/specs/RTM.md` | `requirements-engineering`<br>`spec-driven-development`<br>`pm-product-spec`<br>`pm-user-story` |
| **3. Architecture & Design** | [`architecture-overview.md`](architecture-overview.md)<br>[`ADR.md`](ADR.md)<br>[`DDS.md`](DDS.md) | `docs/architecture.md`<br>`docs/adr/ADR-NNN-[slug].md`<br>`docs/features/[feature-id]/design.md` | `software-architecture`<br>`codebase-design`<br>`domain-modeling`<br>`database-design`<br>`api-and-interface-design`<br>`documentation-and-adrs` |
| **4. Planning & Breakdown** | [`plan.md`](plan.md)<br>[`tasks.md`](tasks.md)<br>[`task-handoff.md`](task-handoff.md) | `docs/features/[feature-id]/plan.md`<br>`docs/features/[feature-id]/tasks.md`<br>`.agent/tasks/[task-id].md` | `planning-and-task-breakdown`<br>`subagent-driven-development`<br>`task-handoff` |
| **5. Implementation** | *(Source code & migrations)* | `src/...`, `migrations/...` | `incremental-implementation`<br>`test-driven-development` |
| **6. Testing & Verification** | [`acceptance-report.md`](acceptance-report.md) | `docs/features/[feature-id]/test-report.md` | `api-contract-testing`<br>`browser-testing-with-devtools`<br>`k6-load-testing` |
| **7. Review & Acceptance** | [`pull-request.md`](pull-request.md)<br>[`acceptance-report.md`](acceptance-report.md) | `.github/pull_request_template.md`<br>`docs/features/[feature-id]/acceptance-report.md` | `code-review-and-quality`<br>`receiving-code-review`<br>`verification-before-completion` |
| **8. Release & Deployment** | [`release-notes.md`](release-notes.md)<br>[`release-checklist.md`](release-checklist.md) | `docs/releases/v[X.Y.Z].md`<br>*(release gate check)* | `shipping-and-launch`<br>`ci-cd-and-automation`<br>`git-workflow-and-versioning` |
| **9. Operations & Incidents** | [`incident-postmortem.md`](incident-postmortem.md)<br>[`runbook.md`](runbook.md) | `docs/incidents/[YYYYMMDD-slug]/postmortem.md`<br>`docs/runbooks/[service-name].md` | `observability-and-instrumentation`<br>`service-mesh-observability` |
| **10. Maintenance & Evolution** | [`deprecation-notice.md`](deprecation-notice.md) | `docs/migrations/[slug]-deprecation.md` | `deprecation-and-migration`<br>`code-simplification` |
| **11. Product Learning** | [`experiment-brief.md`](experiment-brief.md)<br>[`tracking-plan.md`](tracking-plan.md) | `docs/experiments/[exp-id]-[slug].md`<br>`docs/analytics/tracking-plan.md` | `ab-testing`<br>`analytics` |
| **12. Security & Privacy** | [`threat-model.md`](threat-model.md) | `docs/security/threat-model-[system].md` | `threat-model-analyst`<br>`security-and-hardening`<br>`secrets-management` |
| **13. Platform & DevEx** | *(Setup scripts & workflows)* | `.devcontainer/...`, `.github/workflows/...` | `setup-pre-commit`<br>`ci-cd-and-automation` |
| **14. AI Governance** | [`constitution.md`](constitution.md) | `AGENTS.md` / `CLAUDE.md` / `.agent/constitution.md` | `context-engineering`<br>`writing-for-agents` |
| **15. Documentation** | [`runbook.md`](runbook.md)<br>[`architecture-overview.md`](architecture-overview.md) | `docs/guides/...` | `documentation-and-adrs`<br>`doc-coauthoring` |
| **16. Cost Governance** | *(Attribution reports)* | `docs/infrastructure/cost-report.md` | `cost-optimization`<br>`terraform-specialist` |
