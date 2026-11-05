# CLP Knowledge Hub

This index is the front door to CLP's repository knowledge. Follow the audience path to authoritative documents. Roadmap and feature specifications are living records; feature PRs must synchronize them.

## Start here
- **Vision, phases, milestones, status:** [CLP Vision Roadmap](CLP-VISION-ROADMAP.md)
- **Operating contract:** [AGENTS.md](../AGENTS.md)
- **Model/tool-neutral agentic specification:** [Agentic Specification](agentic/agentic-spec.md)
- **Feature specification template:** [Feature Spec Template](templates/feature-spec-template.md)
- **Social profile and launch kit:** [X and Instagram launch pack](social-launch-pack.md)
- **Skill execution guide:** [Skills README](../skills/README.md)

## Audience paths
### Business / leadership
Roadmap → project context → decisions → channel plan.
### Product / functional
Roadmap → feature spec template → content management → authoring principles → content patterns.
### Engineering / integration
Architecture → agentic specification → decision log → hosting constraints.
### AI / agent engineers
AGENTS.md → agentic specification → skill routing → feature development → documentation synchronization.
### Quality engineering / operations
QA and release → design language → AI readiness → analytics/privacy contracts.

## Domain index
| Topic | Authority |
|---|---|
| Vision and milestones | [Roadmap](CLP-VISION-ROADMAP.md) |
| Agent/model portability | [Agentic spec](agentic/agentic-spec.md) |
| Architecture and components | [Architecture](agentic/architecture.md) |
| Functional feature records | Feature specs under docs/features, using the template |
| Integrations and data flow | Feature spec + architecture/domain contracts |
| CI/CD, build, deployment | [QA and release](agentic/qa-and-release.md), architecture, workflows under .github/workflows |
| QE and acceptance evidence | [QA and release](agentic/qa-and-release.md) |
| Performance, visual, accessibility | [Design language](agentic/design-language.md), QA and release |
| SEO/GEO/AIO/AI readiness | [AI readiness](agentic/ai-readiness.md) |
| Design system and authoring | [Design language](agentic/design-language.md), [authoring principles](design-and-authoring-principles.md) |
| Decisions | [Architecture decision log](architecture/decision-log.md), [agentic decisions](agentic/decisions.md) |
| Analytics/dashboard | Analytics measurement, dashboard data plan, functional inventory, privacy/security contract |

## Documentation lifecycle
Every feature executes the feature-development skill and applicable domain skills. At handover, execute documentation synchronization: update roadmap/milestone state, feature specification, patterns, decisions, skills, and evidence—or record why an artifact is unchanged. A passing build does not prove visual, accessibility, production, or business-outcome verification.

The source and workflow configuration are authoritative for implementation; documentation states intended contracts. When they disagree, record and resolve the discrepancy rather than silently assuming either is current.
