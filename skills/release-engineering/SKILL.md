---
name: clp-release-engineering
description: Prepare, verify, and report safe CLP GitHub Pages pull-request previews and production releases.
---

# CLP Release Engineering Skill

## Use when
Pushing code, opening/updating PRs, diagnosing Actions, publishing previews, or deploying production.

## Procedure
1. Read `AGENTS.md` and `docs/agentic/qa-and-release.md`.
2. Confirm repository, branch, default branch, PR state, current head SHA, and current workflow definitions.
3. Make changes on a feature branch. Do not commit directly to production branch.
4. Wait for the build workflow; record its URL, conclusion, and tested SHA.
5. Wait for the PR-preview deployment workflow; record its URL, conclusion, and deployed PR SHA from the preview comment/log.
6. Confirm the preview URL uses the expected branch slug and inspect the actual route(s).
7. If the preview workflow is pending, failed, stale, or deployed a different SHA, say so and do not claim the latest revision is available.
8. Include preview URL, Actions URL, PR URL, and known limitations in the response after each push.
9. Never merge, change Pages settings, change hosting provider, or alter production routing without explicit user approval.
10. After an approved merge, verify production deployment and provide the production URL and successful deployment run.

## Acceptance criteria
- Production and preview content are not mixed up.
- Preview uses the exact PR revision and production output is rebuilt from the current production branch.
- Status report distinguishes build, deploy, visual QA, and production verification.
