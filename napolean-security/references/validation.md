# Validation, variants, and remediation

## Candidate to verdict

1. Record the precise claim, affected revision, attacker capabilities, reachable entry, trust boundary, and observable impact.
2. Trace complete source-to-sink behavior, including route registration, middleware, imported helpers, parameter binding, encoding, configuration, and error handling. For logic/concurrency bugs, name the violated invariant and state transition.
3. Challenge the claim: identify a concrete protection, unreachable path, invalid prerequisite, version mismatch, or counterexample that would reject it. Read that evidence rather than assuming it exists or is absent.
4. Reproduce safely if runtime evidence is needed and authorized. Use an isolated local fixture or designated test environment, deterministic inputs, negative controls, and a bounded timeout. Keep live endpoints, accounts, traffic capture, and state changes within the existing mission authority.
5. Adjudicate `confirmed-static`, `confirmed-runtime`, `rejected`, or `unresolved`. Explain why; record runtime gaps even when static evidence is decisive.

Bug Hunter informs the proposer/challenger/adjudicator separation. Its upstream runtime has its own role payloads, state schemas, Node prerequisites, flags, and supported dependency parsers. This skill does not implement those helpers or accept its flags as executable commands. Use its full runtime only after reading the current installation and preflight instructions.

Ghost's live validation separates static route tracing from optional proxy evidence. HTTP success alone is insufficient: compare authorization, returned data, or state against the claimed security property. Capture only necessary traffic, redact tokens, and do not change host trust stores incidentally.

## Variant search

Start from a validated root cause. Confirm a search pattern matches the known issue, then generalize one feature at a time across the authorized scope. Inspect each new match for the same violated invariant and for mitigating differences. Use `rg` for narrow searches and inspected Semgrep/CodeQL tooling for semantic patterns when warranted. Record search scope, pattern limitations, confirmed variants, and dismissed look-alikes. A name match is not a shared exploit.

## Fix mission

An audit-only request stops at evidence and recommendations. For an authorized fix, settle the invariant and affected files, preserve unrelated user changes, then make the smallest complete correction using project conventions. Workers own disjoint files; the commander owns integration. Avoid opportunistic refactors and dependency upgrades without a demonstrated need.

Add a meaningful regression check for the demonstrated failure. Establish that it detects the vulnerable behavior, then verify corrected behavior plus legitimate use. Run relevant existing checks and inspect the final diff for new boundary changes. If tooling cannot run, give the exact limitation and leave runtime verification unresolved. Search for missed variants when the root cause plausibly recurs.

Use an existing suitable checkout or isolated worktree according to repository instructions. Do not automatically commit, push, publish a report, or merge because a subordinate workflow includes those steps.
