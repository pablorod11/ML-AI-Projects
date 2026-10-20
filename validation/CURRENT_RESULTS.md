# Repair verification

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
