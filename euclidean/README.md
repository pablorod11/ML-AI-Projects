# Euclidean Skill

A reusable agent skill for checking whether explicit claims follow from stated facts and axioms.

Euclidean separates facts from assumptions, checks the support for each claim, and flags contradictions or missing premises. A valid source tag alone is not evidence of a valid conclusion.

## Use cases

- Review architecture proposals against stated constraints.
- Find unsupported assumptions in requirements and recommendations.
- Check whether cited facts support generated claims.
- Verify structured server-capacity calculations with the included Python checker.

## Quick start

Requires Python 3.9 or newer. No third-party Python dependencies.

```sh
python3 scripts/ecc.py examples/capacity.json
python3 scripts/ecc.py --self-test
```

The supplied example has three nodes at 5,000 RPS each and ingress of 18,000 RPS. The checker verifies 15,000 RPS total capacity, 6,000 RPS per node under even distribution, and overload.

Input schema: [examples/capacity.json](examples/capacity.json). Exit codes: 0 for valid claims, 1 for invalid claims, 2 for input errors. Numeric outputs use exact rational arithmetic.

## Skill installation

Copy this folder into a skill directory supported by your agent environment under the name `euclidean`. Read [SKILL.md](SKILL.md) for the workflow and invoke `$euclidean` where supported. Includes Codex interface metadata in [agents/openai.yaml](agents/openai.yaml).

## Verification and limits

Validated against the skill-format checks in [affaan-m/ECC at revision 5af4395](https://github.com/affaan-m/ECC/tree/5af4395e5c52643b7f5ecc716079cd253504b354): strict skill validation and all four Codex surface checks, using an isolated fixture containing this skill and the upstream MLE skill required by the surface test. The checker self-tests and 11 additional boundary/input checks also passed. This is not a run of ECC's full repository suite or a certification by its maintainers.

Machine verification is limited to the three structured capacity claims. Reviews in other domains are agent judgments, not formal proofs. The checker does not establish factual truth of the input definitions, predict real system behavior, or replace runtime tests.

This is a standalone skill, not the full ECC framework or an MCP server. ECC refers to the upstream engineering workflow repository; no affiliation is implied.
