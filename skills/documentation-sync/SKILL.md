---
name: documentation-sync
description: Keep project documentation and model-neutral agentic guidance synchronized with every implementation change.
---

# Documentation synchronization skill

## Trigger and relationship to feature development

The [Feature Development Skill](../feature-development/SKILL.md) MUST invoke this skill as a self-inclusive documentation-review phase for every feature, enhancement, integration, or meaningful behavior change. Run this skill while the feature is being developed and before handover/review—not as a separate post-implementation cleanup.

This is an author/agent responsibility and contextual review, not a GitHub Actions documentation gate. Do not create or depend on a workflow that mechanically decides which documents must change. Automated checks can validate links/builds, but they cannot replace this review.

## Procedure

1. **Inspect the baseline.** Read `README.md`, `AGENTS.md`, `docs/agentic/README.md`, and the relevant sections of `docs/agentic/` and `skills/`. Inspect current source and workflows; do not rely on chat memory or old summaries as the authority.
2. **Map the change.** Identify affected user-visible behavior, routes, components, assets, design decisions, build/deployment flows, validation checks, and operator instructions.
3. **Review documentation targets.** Check whether the change requires updates to:
   - `README.md` and project status/release instructions;
   - `AGENTS.md` and `docs/agentic/agentic-spec.md`;
   - architecture, design language, content patterns, digital assets, QA/release, AI-readiness, analytics, and decisions documents;
   - one or more portable skills;
   - contribution templates, workflows, or automated guardrails.
4. **Update in the same PR.** When a lasting rule, capability, workflow, route, asset convention, acceptance criterion, or operational fact changes, update its source-of-truth document in the same PR. Avoid duplicate rules; link to the authoritative rule.
5. **Keep status truthful.** Distinguish implemented, in-progress, planned, and externally verified capabilities. Do not call a feature live merely because code exists or CI passes. Do not describe a live domain as a future launch. Cite the exact commit, workflow, and preview when claiming verification.
6. **Check links and consistency.** Verify repository paths and Markdown links, ensure instructions agree with actual workflows/source, and remove stale or contradictory release gates.
7. **Record the review.** Add a concise PR section titled `Documentation synchronization` listing documents updated and why. If none need changes, state that the review was performed and explain why no documentation edits were warranted.
8. **Validate.** Run available link/build/documentation checks. If a check cannot be run, disclose that limitation rather than implying it passed.

## Acceptance checklist

- [ ] README accurately reflects the current live site, architecture, workflows, and release model.
- [ ] Agentic spec and `AGENTS.md` remain aligned.
- [ ] Relevant skills and design/content/asset rules are current.
- [ ] No stale planned-vs-live claims or contradictory release instructions remain in touched documents.
- [ ] Paths and links resolve.
- [ ] PR records documentation review and exact validation evidence.
- [ ] Production is not changed without explicit approval.

## Output

Report the docs reviewed, docs changed, validation performed, unresolved drift, and any work intentionally deferred.

## Logo/theme acceptance
When a change touches shared branding or color themes, confirm that the approved header and footer artwork sits on a white background in both themes, with no filters changing the logo colors. Check desktop, mobile portrait, and mobile landscape layouts and record the result in the PR.


## Theme-aware branding check
For logo/theme changes, verify both header and footer use the approved dark/light Vriksha PNGs and the selected variant follows the root `data-theme` attribute. Confirm the theme toggle updates both, asset colors are not altered by filters, and existing layout sizing remains intact across desktop and mobile. Record automated CI evidence separately from visual verification.
