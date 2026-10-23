# Napolean Security

**Command the audit. Fortify the code.**

A reusable AI security skill that coordinates repository and PR reviews, vulnerability validation, variant hunting, scoped fixes, dependency and secret assessment, and agent defense. Napolean owns scope, specialist coordination, evidence, and final verification.

## How it works

1. Define the target, revision, authorization, and acceptance evidence.
2. Select the relevant audit, validation, or agent-defense mission.
3. Investigate candidates, challenge assumptions, and adjudicate against source and runnable checks.
4. Report confirmed findings, unresolved questions, verification results, and coverage gaps.

Verdicts distinguish source-backed findings from runtime demonstrations: `confirmed-static`, `confirmed-runtime`, `rejected`, and `unresolved`. Missing tooling never counts as a clean scan.

## Install in Codex

Clone this repository, then copy the contents of its `napolean-security/` directory into a new `napolean-security` folder inside your personal Codex skills directory (normally `~/.codex/skills/`, or `$CODEX_HOME/skills/` when configured). Keep `SKILL.md`, `agents/`, and `references/` together. Avoid overwriting an existing installation without reviewing changes.

The companion [Napolean skill](../napolean/SKILL.md) is also available in this repository. If the separate `napolean` skill is available, this skill loads it as commander. Otherwise it discloses the fallback and uses the embedded commander contract. It does not install Napolean or its optional dependencies.

## Example requests

```text
Use $napolean-security to review this API PR against its merge base,
report only. Focus on tenant authorization and dependencies.
Validate candidates and state untested surfaces.
```

```text
Use $napolean-security to validate this finding, search for related
instances, and fix confirmed issues with regression checks.
```

## Contents

- [SKILL.md](SKILL.md): mission selection, command, and evidence contract.
- [Audit](references/audit.md): application/API/LLM, dependency, and secret review.
- [Validation](references/validation.md): skeptical verification, variants, and fixes.
- [Agent defense](references/agent-defense.md): plugin supply chain, guards, isolated execution, and incident triage.
- [Sources](references/sources.md): all ten upstream projects, attribution, compatibility, and limitations.

## Upstream inspiration

AgriciDaniel/claude-cybersecurity, tanviet12/vbsec, agamm/claude-code-owasp,
ghostsecurity/skills, goplussecurity/agentguard, codexstar69/bug-hunter,
kenryu42/cc-safety-net, anthropics/defending-code-reference-harness,
trailofbits/skills, and cloudflare/security-audit-skill.

This repository contains coordinating instructions and attributed summaries. It does not vendor upstream executables, install scanners, enable runtime hooks, or guarantee that code is secure. Native integrations require separate inspection and setup. Upstream names identify sources, not endorsement. Upstream licensing and compatibility notes are preserved in the source reference.
