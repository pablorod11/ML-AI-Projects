# Notebook validation repairs

> For agentic workers: execute independent notebook groups with tests first and preserve shared-file ownership.

**Goal:** Repair the 18 scoped findings recorded in validation/BASELINE_REPORT.md and publish a reviewable PR.

**Architecture:** Preserve notebook-first examples. Extract original cells/functions into small unittest checks; do not create a second application implementation. Run every original notebook offline in a clean subprocess and preserve the old audit as historical evidence.

**Tech stack:** Python 3.12, NumPy, pandas, scikit-learn, scipy, matplotlib, notebook JSON, unittest.

**Spec:** validation/BASELINE_REPORT.md, commit 87c9d2052b889e35cfbde6dd085a6e9bba36e7e5.

## Constraints

- No live API calls, new credentials, or external-model uploads.
- Keep source families and exact normalized text out of multiple model splits.
- Make savings comparisons use identical successful request cohorts and disclose simulated prices.
- Reject invalid evaluation metrics; do not silently approve failed calibration.
- Clear stale notebook outputs and execution counts when source changes.
- Preserve original comments and established notebook organization.
- Leave live service behavior unverified unless exercised with real consented service responses.

## Tasks

- [x] ML group: tests fail on template overlap, persisted monitoring-profile mismatch, and invalid optional routing; repair and rerun tests.
- [x] Evaluation group: tests fail on ignored holdout, missing confusion classes, duplicated A/B runs, NaN gate, and invalid response accounting; repair and rerun tests.
- [x] Operations group: tests fail on source overlap, stale queues, empty log schema, unsafe threshold fallback, workload/token accounting, misleading daily-budget scope, and inconsistent log-loss gates; repair and rerun tests.
- [x] Integration: run all focused tests and all 12 notebooks, then inspect changed source and artifacts.
- [x] Independent review: address concrete correctness issues before publication.
- [ ] Publish branch and open PR with current verification evidence and limits.

## Review focus

- Tiny grouped splits must retain all classes without requiring exact original row counts.
- Empty/no-review and no-eligible-threshold paths must remain executable.
- NaN, infinity, unknown labels, and malformed service payloads must fail closed.
- Rerunning an experiment cell must not inflate independent sample counts.
- Historical audit figures must remain clearly separated from repaired-source results.
