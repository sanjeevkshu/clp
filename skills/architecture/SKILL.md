---
name: clp-architecture
description: Inspect and evolve the CLP static-site architecture, component boundaries, URLs, build, and runtime safely.
---

# CLP Architecture Skill

## Use when
Changing Jekyll structure, layouts/includes, shared JavaScript, CSS loading, URL routing, configuration, build workflows, dependencies, or proposing new runtime services.

## Procedure
1. Read `AGENTS.md`, `docs/agentic/architecture.md`, and the decision log.
2. Inspect current files and workflows; distinguish deployed facts from open PR changes.
3. Draw the current flow and identify affected content, composition, presentation, behavior, metadata, and deployment boundaries.
4. Prefer the smallest solution compatible with the existing static Jekyll architecture.
5. Check `baseurl`, `relative_url`, `absolute_url`, permalinks, canonical metadata, and nested PR-preview behavior.
6. Reuse shared includes/components; document new component inputs, outputs, states, accessibility, and responsive behavior.
7. If introducing a dependency/service, document why static HTML/Jekyll is insufficient, ownership, cost, privacy/security, failure modes, deployment, and maintenance.
8. Update architecture docs and decision log for durable changes.
9. Verify the exact PR SHA through build and preview workflows.

## Acceptance criteria
- Clear boundaries; no unnecessary framework or service.
- Production and preview builds remain separated.
- URLs and assets work under `/clp` and nested preview base paths.
- No secrets or environment-specific assumptions are committed.
- Documentation matches the actual implementation and identifies open questions.
