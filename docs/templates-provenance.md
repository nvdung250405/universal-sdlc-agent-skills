# Template and skill provenance

This pack vendors selected Agent Skills from Addy Osmani and Agentic SDLC Kit, and keeps selected GitHub Spec Kit templates as source references. Keep the license/notice files that accompany each upstream.

The portable templates in this directory are pack-level integration templates designed to align a single artifact contract across all 16 SDLC stages (from Discovery, Requirements, Architecture, Planning, Testing, Review, Release, Operations, to Learning and Security). For the complete template catalog and canonical path mapping, see [templates/README.md](../templates/README.md).

To compare with the original Spec Kit templates, inspect `third_party/upstreams/github-spec-kit/templates/` after running `scripts/sync_upstream.py`.

When changing source selection, record repo URL, upstream path, commit lock, license, any patch/exclusion, and why the source was selected in `upstream.json` / `manifests/skill-map.json`.
