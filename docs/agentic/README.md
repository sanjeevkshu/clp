# CLP Agentic Engineering Handbook

**Purpose:** preserve the knowledge acquired while building CLP so future work can continue across AI models, coding agents, IDEs, and human contributors without depending on chat history or a particular vendor.

## Start here
- [Agentic operating specification](agentic-spec.md) — lifecycle, risk model, skill routing, and completion evidence.
- [Root operating contract](../../AGENTS.md) — mandatory guardrails and workflow.
- [Project context and current baseline](project-context.md)
- [Architecture and runtime](architecture.md)
- [Design language and interaction rules](design-language.md)
- [Content model and reusable patterns](content-patterns.md)
- [Digital assets and media](digital-assets.md)
- [QA, release, and deployment safety](qa-and-release.md)
- [SEO, GEO, AIO, and AI readiness](ai-readiness.md)
- [Analytics measurement and consent](analytics-measurement.md)\n- [Decision log and open questions](decisions.md)

## Portable skills
Skills are plain Markdown with a small YAML front matter header. They contain task-specific checklists and acceptance criteria and do not depend on a model API or a proprietary agent framework.

- [Architecture skill](../../skills/architecture/SKILL.md)
- [Design language skill](../../skills/design-language/SKILL.md)
- [Content patterns skill](../../skills/content-patterns/SKILL.md)
- [Digital assets skill](../../skills/digital-assets/SKILL.md)
- [QA and accessibility skill](../../skills/qa/SKILL.md)
- [Release engineering skill](../../skills/release-engineering/SKILL.md)
- [Documentation synchronization skill](../../skills/documentation-sync/SKILL.md) — mandatory review of README, agentic specs, skills, and operational docs in every implementation PR.
- [AI readiness skill](../../skills/ai-readiness/SKILL.md)

## How to use this pack with any AI model
1. Give the model `AGENTS.md` and this handbook first.
2. Provide only the relevant skill(s), the task, acceptance criteria, and the current branch/PR.
3. Ask it to inspect source and current CI state before acting; do not ask it to rely on unverified memory.
4. Require a plan and list of files to change before broad refactors.
5. Require evidence-based reporting: exact revision, commands/checks, results, deployment link, and remaining uncertainty.
6. After a durable decision or pattern change, update the docs/skill and decision log in the same PR.

## Source-of-truth hierarchy
1. Current repository source and configuration.
2. Current successful workflow results and deployment evidence for the exact revision.
3. Accepted/merged decisions and this handbook, updated as implementation evolves.
4. Open PRs and unmerged changes, clearly labeled as proposed.
5. Chat history, summaries, generated suggestions, and model inference.

If documentation and implementation disagree, do not silently choose one. Inspect the code, identify the discrepancy, and update the relevant documentation in the same approved change.

## Status vocabulary
- **Verified:** inspected in current source or validated by a named check at a specific revision.
- **Implemented, not yet preview-verified:** code is committed but the latest preview has not yet been confirmed.
- **Proposed:** recommended future direction, not current implementation.
- **Open question:** requires product-owner input or additional evidence.

## Mandatory documentation synchronization

Every implementation PR must use the [documentation synchronization skill](../../skills/documentation-sync/SKILL.md). Keep README, agentic specifications, relevant skills, and release instructions aligned with actual code and workflows. Record what changed and the evidence checked in the PR. Do not confuse build success with visual verification or production verification.


### Theme-aware logo assets
The shared header and footer use the approved dark/light Vriksha PNG pair and swap according to the active theme. See the design-language and digital-assets documents for the implementation contract and validation requirements.


## Public webmaster dashboard and analytics integration
- [Technical design](../WEBMASTER-DASHBOARD-DATA-PLAN.md) — architecture, trust boundaries, WIF identity, data contract, publication safety and rollout sequence.
- [Functional inventory and acceptance matrix](public-analytics-dashboard-functional-inventory.md) — capability-by-capability current/planned status and release gates.
- [Privacy/security contract](public-analytics-dashboard.md) and [portable implementation skill](../../skills/public-analytics-dashboard/SKILL.md).

Treat the dashboard shell and federation validation workflow on PR #21 as unmerged until verified otherwise. The manual validation workflow is not the scheduled refresh pipeline. Check PR head, latest Actions run, and exact-SHA preview before stating status.
