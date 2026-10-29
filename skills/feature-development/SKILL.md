---
name: feature-development
description: Plan, implement, verify, document, and hand over a complete CLP feature with an explicit self-inclusive documentation review.
---

# CLP Feature Development Skill

## Purpose and governing rule

Use this skill for every new feature, enhancement, integration, workflow capability, or meaningful behavior change in CLP. A feature is not ready to hand over until its implementation, verification, and documentation have been reviewed together.

**Documentation synchronization is a development activity performed by the feature author/agent—not a GitHub Actions documentation gate.** Do not create or rely on a GitHub Action to decide which documentation should change. Automated build/link checks may provide evidence, but they do not replace this skill's contextual review.

## Required workflow

### 1. Orient and establish evidence
1. Read `AGENTS.md`, `docs/agentic/README.md`, this skill, and relevant feature-specific skills.
2. Inspect the current implementation, configuration, active branch/PR, and latest relevant workflow evidence.
3. Label assumptions and distinguish proposed, implemented, build-verified, preview-deployed, visually verified, and production-verified states.
4. Identify the feature owner, intended users, user-visible outcomes, dependencies, security/privacy implications, and explicit non-goals.

### 2. Define feature completeness before coding
Write a compact feature plan that records:
- User problem and intended behavior.
- Functional requirements and acceptance criteria.
- Affected routes, components, content, assets, data models, APIs, integrations, configuration, and operational procedures.
- Accessibility, responsive, theme, SEO/AI-readiness and privacy requirements where applicable.
- Error, empty, loading, stale-data, unavailable-source and recovery states where applicable.
- Test strategy, release/rollback considerations, dependencies and owner approvals.

For cross-cutting work, identify the authoritative source of truth and avoid duplicating rules across documents.

### 3. Design and implement
1. Inspect and reuse existing architecture, shared components, design tokens, content patterns and skills.
2. Keep the diff scoped and reviewable; use a feature branch and do not merge or alter production without explicit owner approval.
3. Add tests or regression checks for the feature's behavior and known failure modes.
4. Keep secrets, personal data and unapproved telemetry out of source, logs, artifacts and public output.
5. Update operational instructions when implementation changes how the feature is configured, tested, deployed, supported or recovered.

### 4. Self-inclusive documentation review — mandatory before feature is ready
The feature author/agent MUST run the [Documentation Synchronization Skill](documentation-sync/SKILL.md) as a named step in the feature workflow. Treat it as a review of the feature being developed, not as a separate later cleanup task.

Review these targets and update only those relevant to the feature:
- `README.md`: user-facing project capabilities, setup, or status if affected.
- `AGENTS.md`: durable non-negotiable rule or instruction if changed.
- `docs/agentic/agentic-spec.md` and `docs/agentic/README.md`: lifecycle, agent behavior, or knowledge-base navigation if affected.
- `docs/agentic/architecture.md`: architecture, components, APIs, data flow, trust boundaries, runtime, dependencies or configuration.
- Relevant design-language, content-patterns, digital-assets, QA/release, AI-readiness, analytics/consent, security, and operations documentation.
- Relevant `skills/*/SKILL.md`: reusable procedure or acceptance criteria future agents must follow.
- `docs/agentic/decisions.md`: durable decisions, reversals, constraints, assumptions, and open questions.
- Functional inventory, data/schema contracts, runbooks, examples, and user/developer instructions where relevant.
- PR description: scope, changed docs, validation evidence, limitations and remaining work.

For every documentation target, make one of three deliberate decisions: **update it**, **link to the authoritative source**, or **no change needed**. Do not mechanically edit every file. Avoid conflicting copies of the same rule; keep one canonical rule and link to it elsewhere.

If no documentation changes are needed, record in the PR that this review occurred and why. Do not state that documentation is synchronized merely because a documentation file was added.

### 5. Verify the complete feature
- Run relevant build, unit/integration, accessibility, schema, security/privacy, link, SEO and other available checks.
- Test relevant success, empty, error and recovery states.
- Check affected sibling pages/components and responsive/theme behavior.
- Check paths under production and preview base paths when relevant.
- Review the diff for accidental secrets, unrelated changes, stale instructions and mismatches between implementation and docs.
- Verify the exact PR head SHA, checks, preview deployment and rendered behavior where tooling allows.
- Mark checks not run or behavior not inspected as unverified. A successful build is not visual or production verification.

### 6. Readiness and handover
Before declaring the feature ready for review, provide:
- Feature outcome and changed source/documentation files.
- Acceptance criteria and check results, with exact revision and workflow links.
- Preview/deployment link and the evidence for the exact revision, when available.
- Documentation synchronization summary: documents updated, linked, or intentionally unchanged.
- Known limitations, security/privacy concerns, open questions, rollback/failure behavior and next owner decision.
- Explicit statement of what remains unverified.

Feature readiness means documentation and implementation agree; it does not itself authorize merge or production release.

## Feature readiness checklist

- [ ] Goal, scope, non-goals and acceptance criteria are explicit.
- [ ] Implementation follows current architecture and reusable patterns.
- [ ] Relevant tests and failure/edge cases are covered.
- [ ] Security, privacy, accessibility and responsive implications are reviewed.
- [ ] Documentation Synchronization Skill was run by the feature author/agent.
- [ ] Relevant docs, skills, inventories, schemas and decisions were updated or intentionally left unchanged with rationale.
- [ ] PR description records the documentation review and validation evidence.
- [ ] Documentation claims match the actual implementation and verified state.
- [ ] Exact revision and preview/check evidence are reported; unknowns remain explicit.
- [ ] Owner approval is obtained for merge, production changes and other consequential actions.

## Relationship to other skills

- Always use [Documentation Synchronization Skill](documentation-sync/SKILL.md) as the mandatory documentation-review phase.
- Combine with architecture, design-language, content-patterns, digital-assets, QA/accessibility, release-engineering, AI-readiness, analytics or domain-specific skills as appropriate.
- This skill is a model-neutral process guide, not a permission grant. `AGENTS.md` and explicit owner approvals take precedence.
