# Validation hardening implementation plan

**Goal:** Apply the four improvements approved in chat: reliable runner status, invalid drift input rejection, one repaired RAG notebook, and useful project documentation.

**Architecture:** Preserve notebook functions and existing dependencies. Keep the repaired RAG contents under the original filename. Test externally visible results and CLI exit codes.

**Constraints:** Work in the existing clean clone. No publishing, host configuration changes, or Graphify installation. Historical validation evidence remains historical.

## Tasks

- [x] Runner: add `validation/test_runner.py` with real temporary notebooks; observe failure for cell errors, startup errors, and empty suites. Update `validation/run_notebooks.py` to exit 1 unless results are nonempty and all statuses are PASS. Verify successful notebooks still exit 0.
- [x] Drift: add `validation/test_drift.py`; reproduce nonfinite/empty inputs being accepted. Validate at shared feature/metric boundaries in `ModelData_Drift_Detection.ipynb`, raising ValueError for invalid input while retaining unlabeled accuracy=None support. Verify normal monitoring still runs.
- [x] RAG and README: point the heldout regression test at `Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb`, reproduce failure, replace it with repaired `(1)` contents, remove duplicate. Add project navigation and explicit demonstration limits to README.
- [x] Integration: run all unittest tests, all remaining notebooks offline, ECC self-test, notebook JSON validation, and diff checks. Update validation documentation and save fresh run evidence separately from historical evidence. Produce a reviewable patch and concise verification record.

## Review focus

Check failing startup, empty suites, invalid monitoring arrays, unlabeled monitoring, and canonical RAG cohort separation. No live API, GPU, plot rendering, or deployment claims.
