#!/usr/bin/env python3
"""Exact arithmetic checks for the Euclidean capacity model. No dependencies."""
import copy
import json
import sys
from fractions import Fraction
from pathlib import Path

SOURCES = {
    "TOTAL_CAPACITY": {"NODE_LIMIT", "REPLICA_COUNT", "AXIOM_TOTAL_CAPACITY"},
    "TRAFFIC_PER_NODE": {"INGRESS_PEAK", "REPLICA_COUNT", "LOAD_BALANCER", "AXIOM_EVEN_DISTRIBUTION"},
    "OVERLOADED": {"INGRESS_PEAK", "TOTAL_CAPACITY", "AXIOM_OVERFLOW_RULE"},
}


def exact_keys(obj, keys, label):
    if not isinstance(obj, dict) or set(obj) != set(keys):
        raise ValueError(f"{label} requires exactly: {', '.join(sorted(keys))}")


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        raise ValueError("Expected a finite number or exact decimal string")
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError, OverflowError) as exc:
        raise ValueError("Expected a finite number or exact decimal string") from exc


def verify(proof):
    exact_keys(proof, {"definitions", "claims"}, "Proof")
    facts, claims = proof["definitions"], proof["claims"]
    exact_keys(facts, {"NODE_LIMIT", "REPLICA_COUNT", "INGRESS_PEAK", "LOAD_BALANCER"}, "Definitions")
    exact_keys(claims, SOURCES, "Claims")
    limit, nodes, ingress = (number(facts[k]) for k in ("NODE_LIMIT", "REPLICA_COUNT", "INGRESS_PEAK"))
    if limit <= 0 or nodes <= 0 or nodes.denominator != 1 or ingress < 0:
        raise ValueError("Require NODE_LIMIT > 0, integer REPLICA_COUNT > 0, INGRESS_PEAK >= 0")
    if type(facts["LOAD_BALANCER"]) is not bool:
        raise ValueError("LOAD_BALANCER must be boolean")
    expected = {
        "TOTAL_CAPACITY": limit * nodes,
        "TRAFFIC_PER_NODE": ingress / nodes,
        "OVERLOADED": ingress > limit * nodes,
    }
    errors = []
    results = []
    for name, sources in SOURCES.items():
        claim = claims[name]
        exact_keys(claim, {"value", "sources"}, name)
        cited = claim["sources"]
        if not isinstance(cited, list) or not all(isinstance(s, str) for s in cited):
            raise ValueError(f"{name}.sources must be a list of strings")
        problems = []
        if len(cited) != len(set(cited)) or set(cited) != sources:
            problems.append("Sources must match the axiom and all required premises exactly")
        if name == "TRAFFIC_PER_NODE" and not facts["LOAD_BALANCER"]:
            problems.append("Even distribution is not established")
        actual = claim["value"]
        if name == "OVERLOADED":
            matches = type(actual) is bool and actual == expected[name]
        else:
            matches = number(actual) == expected[name]
        if not matches:
            problems.append("Claim contradicts the computed result")
        errors.extend(f"{name}: {p}" for p in problems)
        results.append({"claim": name, "expected": expected[name] if name == "OVERLOADED" else str(expected[name]),
                        "status": "INVALID" if problems else "VALID"})
    return {"valid": not errors, "scope": "Three capacity claims under supplied premises; numeric results are exact RPS", "claims": results, "errors": errors}


def reject_duplicates(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def read_proof(text):
    return json.loads(text, parse_float=str, object_pairs_hook=reject_duplicates,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(f"Invalid number: {value}")))


def self_test():
    sample = read_proof((Path(__file__).resolve().parents[1] / "examples/capacity.json").read_text())
    assert verify(sample)["valid"]
    wrong = copy.deepcopy(sample)
    wrong["claims"]["TOTAL_CAPACITY"]["value"] = 18000
    assert not verify(wrong)["valid"]  # Valid citations cannot launder false arithmetic.
    wrong = copy.deepcopy(sample)
    wrong["claims"]["OVERLOADED"]["value"] = False
    assert not verify(wrong)["valid"]
    boundary = copy.deepcopy(sample)
    boundary["definitions"]["INGRESS_PEAK"] = 15000
    boundary["claims"]["TRAFFIC_PER_NODE"]["value"] = 5000
    boundary["claims"]["OVERLOADED"]["value"] = False
    assert verify(boundary)["valid"]  # Equality does not trigger strict overflow.
    uneven = copy.deepcopy(sample)
    uneven["definitions"]["LOAD_BALANCER"] = False
    assert not verify(uneven)["valid"]
    for bad in ({}, {"definitions": sample["definitions"], "claims": {}}):
        try:
            verify(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Incomplete proof accepted")
    for raw in ('{"x": 1, "x": 2}', '{"x": NaN}'):
        try:
            read_proof(raw)
        except ValueError:
            pass
        else:
            raise AssertionError("Malformed input accepted")
    print("ECC self-test passed")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    if len(sys.argv) != 2:
        print("Usage: ecc.py proof.json | ecc.py --self-test", file=sys.stderr)
        return 2
    try:
        result = verify(read_proof(Path(sys.argv[1]).read_text()))
    except (OSError, ValueError, TypeError, RecursionError) as exc:
        print(json.dumps({"valid": False, "errors": [str(exc)]}))
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
