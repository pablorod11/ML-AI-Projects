---
name: euclidean
description: Check explicit claims against stated definitions and axioms using a Euclidean proof discipline. Use for constraint consistency, capacity proofs, or requests for assumption checks.
---

# Euclidean verification

ECC refers to the upstream [affaan-m/ECC](https://github.com/affaan-m/ECC) engineering workflow repository. This is a standalone Euclidean verification skill compatible with its Codex skill format. The bundled `ecc.py` performs capacity constraint checking; it does not implement or install the full ECC framework.

Produce a concise, auditable proof artifact: definitions, applicable axioms, explicit claims with sources, and a conclusion. Do not request or expose private internal reasoning logs.

1. Extract the supplied ground truths with units and scope. Distinguish facts from assumptions; do not silently promote assumptions into facts.
2. Derive each claim from named definitions, axioms, or already established claims. A recognized citation establishes provenance, not logical validity.
3. Check arithmetic, units, inequalities, and whether every premise actually supports the claim. Mark unsupported claims UNVERIFIED and contradictions INVALID. Say VALID only within the checked model and its premises.
4. State the conclusion and any missing premises. Revise a failed proof only with justified premises; never change ground truths to make it pass.

## Deterministic capacity checking

For the supplied load-balancing model, run the bundled standard-library checker:

```sh
python3 <skill-directory>/scripts/ecc.py <proof.json>
```

Use [examples/capacity.json](examples/capacity.json) as the input schema. The top-level object requires exactly `definitions` and `claims`. Definitions provide numeric NODE_LIMIT, REPLICA_COUNT, INGRESS_PEAK and boolean LOAD_BALANCER (true means perfect even distribution). Numbers may be JSON numbers or exact decimal strings; REPLICA_COUNT must be a positive integer.

Each required claim has exactly `value` and `sources`. The checker validates all required claims and citations, recomputes the results with exact rational arithmetic, rejects unknown fields and incomplete proofs, and exits 0 for valid, 1 for invalid, 2 for input errors. Run `python3 <skill-directory>/scripts/ecc.py --self-test` to exercise valid, false, boundary, and malformed proofs.

The implemented axioms are:

- AXIOM_TOTAL_CAPACITY: TOTAL_CAPACITY = NODE_LIMIT * REPLICA_COUNT.
- AXIOM_EVEN_DISTRIBUTION: TRAFFIC_PER_NODE = INGRESS_PEAK / REPLICA_COUNT, provided LOAD_BALANCER is true.
- AXIOM_OVERFLOW_RULE: OVERLOADED = (INGRESS_PEAK > TOTAL_CAPACITY).

The original example yields 15,000 RPS capacity, 6,000 RPS per node, and overload. The overflow axiom predicts degradation or drops; it does not quantify actual packet loss or choose which failure occurs.

This checker proves these three structured capacity claims only. Free-form prose, other domains, runtime behavior, and factual truth of supplied definitions require separate checking. Do not report them as machine verified.

## ECC repository integration

For an ECC contribution, put the canonical skill in `skills/euclidean/` and its Codex mirror in `.agents/skills/euclidean/`, preserving scripts, examples, and `agents/openai.yaml`. Run the repository skill and Codex surface validators; check its current manifests and catalog before claiming contribution readiness. Personal installation is separate from repository registration. No MCP servers, hooks, agent-role configuration, or credentials are required by this checker.
