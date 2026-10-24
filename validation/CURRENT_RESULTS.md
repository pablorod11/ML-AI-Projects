# Current verification — 2026-10-24

The validation hardening changes pass 23 regression tests and all 11 maintained notebooks (351 code cells) in fresh offline worker processes. The runner exits 0 for this successful run. Notebook hashes, timings, and startup diagnostics are recorded in [hardening-results.json](hardening-results.json).

- Notebook failure, startup failure, timeout, and empty-suite results cause a nonzero runner exit. CLI tests cover successful execution, cell failure, startup failure, and the empty suite.
- Drift monitoring raises ValueError for empty/nonfinite features, mismatched schemas, nonfinite or misaligned metric arrays, and invalid accuracy. Unlabeled monitoring with accuracy=None remains supported.
- The repaired RAG notebook is maintained under Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb. Its regression test checks validation comparison and held-out test reporting/routing. The redundant (1) notebook was removed.
- README now indexes all 11 projects and explains synthetic data, optional live services, and skill dependencies.
- ECC self-test, pip dependency consistency, notebook schema validation, and git diff whitespace checks pass.

On this macOS host, Matplotlib font inventory stalled in system_profiler. A temporary PATH wrapper returned exit 1 for that command during the final headless run, allowing Matplotlib to use available fonts. Some workers emitted font-cache lock warnings; notebook execution still passed. Earlier stalled runs and initial 30-second test timeouts are not counted as passing evidence. The CLI test deadline now allows the runner's 180-second notebook timeout to finish.

Plot appearance, live APIs, GPU behavior, shared multiuser concurrency, and production deployment remain unverified. No Graphify command, installed skill, or connector was available; relationships were inspected through source and rg.

The sections below and results.json are historical evidence from the previous repairs, before consolidation; their 12-notebook count and hashes do not describe this revision.

# Previous repair verification

All 18 scoped baseline findings are addressed. The historical baseline report remains unchanged for traceability.

- 16 focused regression tests pass. The original failures were reproduced before repair.
- All 12 notebooks completed all 390 original code cells in fresh offline processes after repairs.
- Modified notebooks have saved outputs and execution counts cleared so old metrics are not presented as current results.
- Three independently reviewed repair groups cover model splits/monitoring, LLM evaluation, and operations/accounting. The review found and closed an additional parser-exception escape.

## Changes by finding

- Classifier source descriptions/templates now stay in disjoint train/validation/test groups. Only training descriptions are augmented. Small synthetic holdouts remain insufficient to claim enterprise generalization.
- Review queue exports reflect completed decisions, and empty review logs retain their schema.
- Failed threshold calibration disables automatic acceptance.
- Autopilot savings price the same successful prompts in both strategies. Dashboard totals include output tokens. The simulated cap is explicitly a session budget, not a persisted daily cap.
- Reusable regression checks enforce the same log-loss constraint as the demonstrated release policy.
- RAG comparisons use validation data; final metrics and routing use the held-out test cohort, with exported split identities.
- All invalid model outputs count as failures; confusion matrices retain observed failure classes; invalid/nonfinite evaluations fail closed.
- Rerunning the A/B experiment cell resets its cohort rather than duplicating deterministic subjects.
- Drift reference profiles retain the arrays required for monitoring after reload.
- Optional JEV routing accepts only validated adapter choices and defaults to HUMAN_REVIEW. Adapter errors fail closed; process interrupts propagate. No live API response schema is assumed or claimed verified.

Run-specific notebook hashes and execution summaries are in results.json. Exact dependencies are in requirements.txt. Live services, GPU behavior, visual plots, shared multiuser concurrency and production deployment remain unverified.
