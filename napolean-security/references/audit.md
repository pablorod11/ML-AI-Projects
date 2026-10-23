# Audit mission

## Reconnaissance

Resolve repository instructions and actual revision, dirty files, requested paths, and trustworthy diff base. For PRs, inspect changed code in its surrounding implementation and callers; compare removed protections and security-related history. Do not silently substitute an assumed base. Generated/vendor code may be excluded, but record exclusions and any relevant dependency boundary.

Map entry points, identities, privileges, data stores, external calls, sensitive assets, and deployment assumptions. Use existing threat models if current. Separate inferred architecture from observed routes and configuration. Graphify is optional navigation under Napolean; source and caller inspection remain necessary when it is absent or stale.

Choose a bounded inventory of surfaces and record each as examined, partially examined, skipped, or blocked. Large scopes require a coverage queue and a truthful stopping point. Do not describe a sample as a full audit.

## Application and API lenses

Inspect actual framework behavior before labeling patterns: authentication/session lifecycle; object, function, field, and tenant authorization; injection; output encoding; file traversal and archive extraction; upload processing; deserialization; server-side fetch/redirect controls; cryptography and randomness; unsafe defaults; resource exhaustion; race conditions and transaction boundaries. Test isolation across distinct users and roles when the authorized environment supports it.

For LLM applications, trace untrusted text into prompts, retrieved context, tools, agent delegation, and outbound requests. Inspect tool permissions, secret exposure, output use, memory contamination, and excessive action authority. Verify the current OWASP standard and edition before attaching category IDs; source repositories have inconsistent taxonomy dates. A checklist category is a lens, not finding evidence.

For smart contracts, native code, cryptographic implementations, or CI agent workflows, select the matching Trail of Bits specialist from its current catalog. Do not apply every specialist or generalize one language's scanner support to others.

## Tool-backed assessment

Use installed, inspected scanners appropriate to the stack. Record tool/version, input scope, command, exit status, output location, advisory date, and unsupported components. Inspect build/install scripts before executing untrusted repository code.

- Secrets: examine context and placeholder status; redact values. Distinguish a secret-like match from proven exposure. Recommend rotation if warranted; do not rotate or test credentials without authorization.
- Dependencies: use lockfile-resolved versions and current advisory evidence. Separate presence from runtime reachability, exposed functionality, and deployment impact. Missing scanners or unsupported lockfiles remain unassessed.
- Static analysis: trace source through transformations and guards to sink. Pattern matches nominate candidates; language/framework semantics determine findings.
- Dynamic validation: use the validation reference and an authorized target. Avoid capture of unrelated credentials or traffic.

Ghost's standalone scanners can supply evidence when actually available. Their absence does not prevent source review; label the fallback. Do not claim a Ghost scan occurred when only manual assessment ran.

## Source selection

AgriciDaniel supplies broad reconnaissance and domain coverage; vbsec supplies framework-aware review and false-positive discipline; agamm supplies application, API, and LLM review lenses. Ghost supplies tool-backed context and scan composition. Trail of Bits supplies deeper stack-specific analysis, differential review, and variants. Source-specific compatibility and limitations are in [sources](sources.md).
