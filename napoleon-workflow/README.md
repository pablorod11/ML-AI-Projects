# Napoleon Workflow

A Codex skill that coordinates specialists through one commander responsible for the integrated result.

Small tasks stay inline. Larger tasks use bounded missions, clear file ownership, explicit dependencies, and verification after integration.

## What it combines

- **Napoleon commander approach:** The coordinator owns scope, shared contracts, task assignment, integration, and final checks.
- **Superpowers:** Selects the relevant discovery, planning, debugging, and execution process.
- **Graphify:** Helps explore repository relationships; findings are checked against source files.
- **Vercel Agent Skills:** Supplies task-specific guidance for the relevant stack.
- **Ponytail:** Favors existing code, standard libraries, native features, and the smallest correct implementation.
- **Euclidean:** Separates assumptions from evidence and checks explicit claims within their stated premises.
- **Design Workflow:** Coordinates UI direction, implementation, audits, and browser verification when applicable.
- **Humanizer and Caveman:** Natural prose in deliverables and concise chat without changing technical facts.

The workflow loads relevant specialists on demand. It respects available agent slots and assigns shared files a single owner. Missing optional tools have disclosed fallbacks.

## Install

Clone this repository, then copy the skill folder into your personal Codex skills directory:

```sh
git clone https://github.com/pablorod11/ML-AI-Projects.git
mkdir -p ~/.codex/skills/napoleon-workflow
cp ML-AI-Projects/napoleon-workflow/SKILL.md ~/.codex/skills/napoleon-workflow/
cp -R ML-AI-Projects/napoleon-workflow/agents ML-AI-Projects/napoleon-workflow/references ~/.codex/skills/napoleon-workflow/
```

If you use a custom `CODEX_HOME`, use its `skills` directory instead. Avoid overwriting a modified installation without reviewing the differences.

## Use

```text
Use $napoleon-workflow to fix this issue and verify the integrated result.
```

Or:

```text
Use $napoleon-workflow to coordinate these independent module changes.
```

## Dependencies and scope

This repository contains coordinating instructions and UI metadata. It does not bundle or install the named third-party skills or Graphify runtime. Read [integration guidance](references/integrations.md) for resolution and fallback behavior.

Napoleon refers to a general commander approach, not a separate Napoleon product. Using this skill does not grant permission to publish, message others, or change host configuration.

## Validation

The initial version passed the Codex skill structure validator and an independent simulated review covering small edits, shared schema ownership, concurrency limits, graph/source contradictions, unsupported safety claims, and prose editing with missing tools. These checks do not establish real-project effectiveness or compatibility with every upstream release.

## Credits

- [Superpowers](https://github.com/obra/superpowers)
- [Graphify](https://github.com/Graphify-Labs/graphify)
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)
- [Humanizer](https://github.com/blader/humanizer)
- The local Euclidean, Caveman, and Design Workflow skills, and the Ponytail plugin used to compose this workflow.

Upstream projects retain their own licenses and ownership. Their inclusion here describes integration intent and does not imply endorsement.
