# CLP Agentic Specification

**Document type:** model-neutral operating specification  
**Applies to:** AI assistants, coding agents, content agents, human contributors, and future automated workflows working on CLP  
**Normative language:** “MUST” means a hard requirement; “SHOULD” means default practice unless a reason is documented; “MAY” means optional.

## 1. Mission

Help CLP evolve as a coherent, accessible, trustworthy, mobile-friendly learning experience while preserving its brand, architecture, content quality, and operational safety. Improve the project incrementally without losing decisions, context, or provenance when models and tools change.

## 2. Operating principles

1. **Repository-grounded:** inspect current source and workflow evidence before acting; do not treat chat memory as the source of truth.
2. **Model-neutral:** keep core rules, skills, schemas, and decisions in plain Markdown/YAML and portable web standards. Provider-specific adapters may link to this pack but MUST NOT redefine its policy.
3. **Human-governed:** the owner decides scope and approves merges, production changes, hosting changes, and other consequential actions.
4. **Small, reviewable changes:** prefer a coherent, minimal diff over a broad rewrite. Explain why a change is needed.
5. **Reusable by default:** recurring patterns become shared components with documented inputs, outputs, accessibility, responsive behavior, and examples.
6. **Content/presentation separation:** content owns page-specific meaning and choices; shared components and CSS own reusable rendering and presentation.
7. **Evidence over assertion:** distinguish source edits, successful build, successful deployment, visual verification, and production verification.
8. **Secure and privacy-aware:** do not commit secrets or personal/confidential data. Do not add telemetry, analytics, external APIs, or services without approval and documented privacy implications.
9. **Accessible and responsive by design:** accessibility and mobile behavior are acceptance criteria, not post-launch polish.
10. **Knowledge has a lifecycle:** decisions, open questions, component contracts, and recurring failure fixes are updated in repository documentation.

## 3. Task lifecycle

### Phase A — Orient
- Read `AGENTS.md` and this specification.
- Read the relevant skill(s) and handbook sections.
- Inspect the current branch, open PRs, source, workflow definitions, and latest workflow statuses.
- Identify whether relevant changes are merged, unmerged, proposed, or deployed.
- Record assumptions and uncertainties before editing.

### Phase B — Frame
Write down:
- User goal and expected behavior.
- Pages, components, assets, metadata, and workflows affected.
- Acceptance criteria, including responsive/accessibility requirements.
- Regression risks and required checks.
- Whether a durable rule, skill, or decision record must be updated.

For broad or cross-cutting changes, present a concise plan before implementation. Do not expand scope silently.

### Phase C — Design
- Inspect existing patterns before creating new ones.
- Define component contract and data ownership.
- Prefer semantic HTML and native browser behavior where suitable.
- Preserve current static-site architecture unless a documented requirement justifies more complexity.
- Identify content, presentation, behavior, metadata, build, and deployment responsibilities separately.

### Phase D — Implement
- Work on a feature branch and keep the diff focused.
- Reuse shared classes/includes and keep page-specific data in content/front matter.
- Avoid unrelated formatting churn and unrelated dependency changes.
- Update documentation and regression checks when a rule/component changes.
- Do not commit secrets, personal data, unsupported claims, or unlicensed assets.

### Phase E — Verify
- Run available build and static checks.
- Test affected routes and sibling pages sharing components.
- Test mobile portrait, mobile landscape/short viewport, intermediate width, and desktop.
- Check accessibility, theme behavior, link and asset paths, metadata, and console/network failures when tools permit.
- Verify the exact PR head SHA, build status, preview deployment status, and deployed preview revision.
- Mark anything not actually tested as unverified.

### Phase F — Release and report
- Push only to the feature branch.
- Provide PR, preview, and Actions links after pushing.
- Do not merge or change production settings without explicit approval.
- After approval/merge, verify production deployment separately.
- Report what changed, evidence, risks, open questions, and next approval required.

### Phase G — Preserve knowledge
Update, as applicable:
- `AGENTS.md` if a hard operating rule changed.
- `docs/agentic/architecture.md` for architecture/component boundaries.
- Relevant design/content/assets/QA/AI-readiness documentation.
- The corresponding `skills/*/SKILL.md`.
- `docs/agentic/decisions.md` for durable decisions, reversals, and open questions.

Do not save transient status as a permanent fact without a date and evidence. Do not leave a durable lesson only in conversation.

## 4. Skill selection and composition

Use only the skills relevant to the task, but combine them for cross-cutting work:
- Layout/include/CSS architecture: Architecture + Design Language + QA.
- New page/article/FAQ: Content Patterns + Design Language + Digital Assets + QA + AI Readiness.
- Image/logo work: Digital Assets + Design Language + QA.
- Metadata/schema/answerability: AI Readiness + Content Patterns + QA.
- Any push/PR/deploy: Release Engineering + QA.
- Cross-cutting component: Architecture + the component-specific skill + QA + Release Engineering.

A skill is a portable checklist, not an autonomous permission grant. A skill cannot override the operating contract or user approval requirements.

## 5. Permission and risk model

### Safe to do within an approved task
- Read repository source and docs.
- Inspect current workflow logs/statuses.
- Make scoped changes on the active feature branch.
- Add tests and documentation.
- Run non-destructive build and validation commands.
- Open or update a PR when the task requests implementation and the workflow permits it.

### Requires explicit owner approval
- Merge a PR or push directly to the production branch.
- Change hosting provider, GitHub Pages settings, domain, DNS, or production deployment configuration.
- Delete or replace approved brand assets.
- Add paid services, third-party trackers, analytics, external APIs, backend data collection, or new dependencies with material operational/privacy impact.
- Publish legal, privacy, commercial, or factual claims that require owner sign-off.
- Make destructive repository or data changes.
- Enable public-facing AI actions that write data, contact people, spend money, or make consequential decisions.

### Never
- Expose secrets, tokens, personal data, or confidential content.
- Claim a deployment or visual check passed without evidence.
- Treat model-generated text as verified fact without review.
- Make a preview deployment overwrite production intentionally.
- bypass the shared FAQ accordion or component standards for convenience.

## 6. Required component contract

Every new shared component SHOULD document:
- Purpose and when to use it.
- Inputs/data shape and required/optional values.
- Output/semantic markup and accessibility behavior.
- Responsive and theme behavior.
- Dependencies and styling hooks.
- Example usage.
- Known limitations and tests.
- Migration plan for existing duplicates, where applicable.

FAQ contract is already explicit: every Common Questions/FAQ section uses `_includes/faq-accordion.html`, with page-specific `faq_items` in front matter and a unique section ID.

## 7. Completion definition

A task is not “done” merely because code was written. State completion by evidence:
- **Implemented:** source change exists.
- **Build-verified:** required build/check passed.
- **Preview-deployed:** deployment succeeded for the exact PR SHA.
- **Visually verified:** actual rendered page was inspected at stated viewports.
- **Production-verified:** approved production deployment and live route were checked.

These states are independent and MUST NOT be conflated.

## 8. Portability and maintenance

- Keep the canonical rules in Markdown, component data in YAML/front matter, and automation in transparent repository workflows.
- Avoid dependence on one model's hidden memory, private prompt format, or proprietary API.
- When adding a provider-specific instruction file, make it a thin pointer to `AGENTS.md` and the relevant skills.
- Revisit the pack when architecture, hosting, brand, content model, or release workflow changes.
- Prefer explicit dates, revision IDs, links, and status labels over vague claims such as “latest” or “already deployed”.


## 9. Mandatory documentation synchronization

Every implementation PR MUST run the [documentation synchronization skill](../../skills/documentation-sync/SKILL.md). Review README, the root operating contract, this specification, the handbook index, and the relevant architecture/design/content/digital-asset/QA/release/AI-readiness documents and skills. Update the source-of-truth documentation in the same PR whenever implementation changes routes, user-visible behavior, shared components, brand assets, workflows, capabilities, validation, or operating procedures. If no edits are required, record that the review occurred and why.

Documentation MUST distinguish planned, implemented, build-verified, preview-deployed, visually verified, and production-verified states. A successful build does not prove visual correctness. Claims about the live site or release readiness must be supported by current source or evidence for the exact commit. Production remains protected by explicit owner approval.


## Theme-aware shared logo contract
Both shared header and footer MUST use the approved `clp-vriksha-logo-dark.png` and `clp-vriksha-logo-light.png` repository assets. Variant selection follows the active root theme attribute set by `assets/js/main.js`; never infer theme from viewport or page type. Preserve each asset unchanged and do not add color-altering filters. Keep layout sizing separate from asset selection and validate both themes at desktop and mobile sizes.


## Theme-aware shared logo contract
Both shared header and footer MUST use the approved `clp-vriksha-logo-dark.png` and `clp-vriksha-logo-light.png` repository assets. Variant selection follows the active root theme set by `assets/js/main.js`; do not infer theme from viewport or page type. Preserve asset files unchanged and do not apply color-altering filters. Keep layout sizing separate from theme selection and validate both themes at desktop and mobile sizes.
