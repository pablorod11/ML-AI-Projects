# ML-AI-Projects validation

Commit: `87c9d2052b889e35cfbde6dd085a6e9bba36e7e5`. Checked October 20, 2026.

**Result: all default offline paths run, but the repository has correctness findings.**

12/12 notebooks completed all 390/390 code cells in clean subprocesses. All notebook schemas and cell syntax passed. The standalone Euclidean checker passed its self-test and supplied capacity proof. All three bundled skills passed the installed Codex skill-format validator. No repository source was modified or published.

## Highest-priority evidence

- HITL: all 48/48 test rows share an underlying source description with training. Enterprise: 41/42 test rows do. Neural/JEV: 55/120 test rows exactly repeat training text, including every one of its 20 resume test rows. These splits do not establish performance on unseen source descriptions.

- Autopilot reports 97.0831% savings by comparing 2 executed requests against 10 premium-priced requests. Matching the same 2 prompts gives 85.6546% under the notebook’s simulated prices and token estimates. Neither number establishes real provider savings.

- The evaluation helper returns PASS for NaN metrics. Its failure-rate calculation counts an empty response as 0% failures; its confusion matrix drops ERROR predictions when labels exclude ERROR.

- Persisted drift profile raises KeyError for predictions when passed to monitor_batch. The optional online JEV branch returns JEV_RESPONSE rather than an allowed route, even when the mocked service supplies a valid choice. Live JEV behavior is unverified.

## Execution coverage

- [Copy_of_Model_Regression_Detection_System.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Copy_of_Model_Regression_Detection_System.ipynb): 31/31 code cells completed; 108.67 seconds.

- [Enterprise_Autocoding_MLOps_Platform.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Enterprise_Autocoding_MLOps_Platform.ipynb): 54/54 code cells completed; 108.24 seconds.

- [HITL_Review_Pipeline.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/HITL_Review_Pipeline.ipynb): 36/36 code cells completed; 107.88 seconds.

- [Hybrid_RAG_Retrieval_Eval_Pipeline (1).ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Hybrid_RAG_Retrieval_Eval_Pipeline%20(1).ipynb): 40/40 code cells completed; 20.35 seconds.

- [Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb): 39/39 code cells completed; 10.62 seconds.

- [Image_Classification_Pipeline.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Image_Classification_Pipeline.ipynb): 18/18 code cells completed; 7.86 seconds.

- [LLM_Eval_Regression_Testing_Framework.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_Eval_Regression_Testing_Framework.ipynb): 22/22 code cells completed; 5.73 seconds.

- [LLM_cost_Autopilot.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_cost_Autopilot.ipynb): 37/37 code cells completed; 2.63 seconds.

- [Linear_Regression_Model.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Linear_Regression_Model.ipynb): 18/18 code cells completed; 5.4 seconds.

- [ModelData_Drift_Detection.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/ModelData_Drift_Detection.ipynb): 26/26 code cells completed; 17.11 seconds.

- [Neural_Network_JEV (1).ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Neural_Network_JEV%20(1).ipynb): 26/26 code cells completed; 6.57 seconds.

- [Prompt_Versioning_AB_Testing_Platform.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Prompt_Versioning_AB_Testing_Platform.ipynb): 43/43 code cells completed; 2.51 seconds.


First three runs included concurrent Matplotlib font-cache creation (~108 seconds each). This is harness startup overhead, not a model performance benchmark. Initial font-cache warnings did not stop execution. Later runs took 2.5–20.4 seconds.

## Findings

P1 means misleading core evaluation/accounting evidence; P2 means a correctness defect or reusable-path failure; P3 means a documented-scope limitation to address before reuse. Cell indices below are zero-based. REPRODUCED means a fresh default artifact or focused minimal test demonstrated the behavior. SOURCE_CONFIRMED means the defect follows from inspected code; its conditional path was not dynamically exercised.

### F01 · P1 · Split source descriptions before generating variants

[Enterprise_Autocoding_MLOps_Platform.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Enterprise_Autocoding_MLOps_Platform.ipynb), cells 4. SOURCE_CONFIRMED.

Cell 3 generates six prefix/suffix variants of each of only 40 original descriptions, then cell 4 splits individual rows. Related variants can land in training, validation, and test. The holdout therefore measures recognition of seen templates, and the validation threshold is calibrated on those same templates. Enterprise drop_duplicates removes exact duplicates only; HITL does not even remove exact duplicates.

Fix: Assign a source-description group ID; split groups first, then augment training only. Assert group and normalized-text disjointness. Report template holdout separately from independent golden cases.

```python
train_data, temp_data = train_test_split(
    data,
    test_size=0.40,
    stratify=data["label"],
    random_state=RANDOM_STATE
```

### F02 · P1 · Split source descriptions before generating variants

[HITL_Review_Pipeline.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/HITL_Review_Pipeline.ipynb), cells 4. SOURCE_CONFIRMED.

Cell 3 generates six prefix/suffix variants of each of only 40 original descriptions, then cell 4 splits individual rows. Related variants can land in training, validation, and test. The holdout therefore measures recognition of seen templates, and the validation threshold is calibrated on those same templates. Enterprise drop_duplicates removes exact duplicates only; HITL does not even remove exact duplicates.

Fix: Assign a source-description group ID; split groups first, then augment training only. Assert group and normalized-text disjointness. Report template holdout separately from independent golden cases.

```python
train_data, temp_data = train_test_split(
    data,
    test_size=0.40,
    stratify=data["label"],
    random_state=RANDOM_STATE
```

### F03 · P1 · Savings compare two different request workloads

[LLM_cost_Autopilot.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_cost_Autopilot.ipynb), cells 26. REPRODUCED.

On a clean sequential run only cells 15 and 16 call llm_autopilot (two requests). Cell 18 defines ten demo_requests but never executes them. The premium baseline prices those ten while autopilot_cost prices the original two, so comparison and savings_percent are invalid.

Fix: Execute demo_requests through autopilot and calculate both strategy totals from the identical successful prompt cohort, excluding or separately reporting blocked requests.

```python
autopilot_cost = total_cost

always_premium_cost = 0.0
for prompt in demo_requests:
```

### F04 · P2 · Reusable regression gate drops the log-loss check

[Copy_of_Model_Regression_Detection_System.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Copy_of_Model_Regression_Detection_System.ipynb), cells 27. SOURCE_CONFIRMED.

detect_regression computes probabilities but does not evaluate them. A candidate with identical hard predictions and substantially worse confidence/log_loss receives PASS here, although cells 10-14 reject log_loss increases above 0.05. The reusable API does not enforce the demonstrated release policy.

Fix: Compute log_loss deltas with the same probability class alignment and LOG_LOSS_MAX_INCREASE limit; centralize the checks to keep both entry points consistent.

```python
passed = (
        accuracy_delta
        >= -max_accuracy_drop
        and
        f1_delta
        >= -max_f1_drop
    )
```

### F05 · P2 · Failed threshold calibration still enables auto acceptance

[Enterprise_Autocoding_MLOps_Platform.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Enterprise_Autocoding_MLOps_Platform.ipynb), cells 20. SOURCE_CONFIRMED.

When no validation threshold reaches TARGET_AUTO_ACCEPT_ACCURACY, fallback 0.70 still routes qualifying predictions to AUTO_ACCEPT without evidence of meeting the target. This may occur precisely because accuracy was inadequate.

Fix: Disable automatic acceptance when calibration has no eligible threshold; report calibration failure and send traffic for review.

```python
else:

    AUTO_ACCEPT_THRESHOLD = (
        DEFAULT_AUTO_ACCEPT_THRESHOLD
    )
```

### F06 · P2 · Completed reviews remain PENDING in persisted queue

[Enterprise_Autocoding_MLOps_Platform.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Enterprise_Autocoding_MLOps_Platform.ipynb), cells 27. REPRODUCED.

After review_log is constructed and final_results updated, review_queue is never updated before saving review_queue.csv. Every completed review still appears pending in the queue artifact, conflicting with final_results and completion counts.

Fix: Update queue statuses using completed record IDs, or persist separate pending and completed queues.

```python
review_queue[
    "review_status"
] = "PENDING"
```

### F07 · P2 · Completed reviews remain PENDING in persisted queue

[HITL_Review_Pipeline.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/HITL_Review_Pipeline.ipynb), cells 18. REPRODUCED.

After review_log is constructed and final_results updated, review_queue is never updated before saving review_queue.csv. Every completed review still appears pending in the queue artifact, conflicting with final_results and completion counts.

Fix: Update queue statuses using completed record IDs, or persist separate pending and completed queues.

```python
review_queue[
    "review_status"
] = "PENDING"
```

### F08 · P2 · No-review case loses the review-log schema

[HITL_Review_Pipeline.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/HITL_Review_Pipeline.ipynb), cells 24. REPRODUCED.

If review_queue contains none of JOB-006 through JOB-010 (e.g. thresholds/model changed or empty human_labels), reviews is empty and review_log has no columns. Cell 28 selecting review_log[["record_id", ...]] raises KeyError, despite cell 27 handling empty review counts.

Fix: Construct review_log with an explicit column schema, as the Enterprise notebook does.

```python
review_log = pd.DataFrame(
    reviews
)
```

### F09 · P2 · Validation/test split is unused in reported evaluation

[Hybrid_RAG_Retrieval_Eval_Pipeline (1).ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Hybrid_RAG_Retrieval_Eval_Pipeline%20(1).ipynb), cells 15, 17, 20, 34, 37. SOURCE_CONFIRMED.

Normal execution: every downstream recall, comparison, MRR and JSON report evaluates golden_data, never validation_data or test_data.

Fix: Use validation_data for comparisons/tuning, freeze settings, then compute and label final test metrics exclusively on test_data; export split membership.

```python
validation_data, test_data = train_test_split(
    golden_data,
    test_size=0.50,
    random_state=42,
    stratify=golden_data["true_code"]
)
...
mrr = mean_reciprocal_rank(golden_data)
```

### F10 · P2 · Failure-rate metric ignores invalid model responses

[LLM_Eval_Regression_Testing_Framework.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_Eval_Regression_Testing_Framework.ipynb), cells 7. REPRODUCED.

A substituted model returns None, an empty string, an unrecognized label or a misspelled/case-variant label rather than the two exact sentinels.

Fix: Validate/normalize prediction against the allowed label set immediately after model invocation, classify all invalid outputs as failures, and retain raw outputs/errors for diagnosis.

```python
failure_rate = (
        results["prediction"]
        .isin([
            "UNKNOWN",
            "ERROR"
        ])
        .mean()
    )
```

### F11 · P2 · Confusion matrix omits failed predictions

[LLM_Eval_Regression_Testing_Framework.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_Eval_Regression_Testing_Framework.ipynb), cells 7, 15. REPRODUCED.

Any model returns UNKNOWN or ERROR (both supported by evaluate_model), or any label outside LABELS.

Fix: Include UNKNOWN, ERROR and all observed prediction labels in the matrix, or separately display failure counts and verify displayed totals equal the evaluation set.

```python
ConfusionMatrixDisplay.from_predictions(
    golden_data["expected_label"],
    candidate_results["prediction"],
    labels=LABELS,
    xticks_rotation=45
)
```

### F12 · P2 · Deployment gate fails open on nonfinite metrics

[LLM_Eval_Regression_Testing_Framework.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_Eval_Regression_Testing_Framework.ipynb), cells 16. REPRODUCED.

Caller supplies NaN accuracy/F1/failure_rate and NaN class change, for example from missing or empty upstream evaluation slices.

Fix: Before threshold comparisons, reject missing/nonfinite/out-of-range baseline/candidate metrics, empty class results and nonfinite class changes; return an explicit INVALID_EVALUATION failure.

```python
if (
        candidate["accuracy"]
        < MIN_ACCURACY
    ):
...
"decision":
            "PASS"
            if not reasons
            else "FAIL",
```

### F13 · P2 · Dashboard total_tokens omits output tokens

[LLM_cost_Autopilot.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_cost_Autopilot.ipynb), cells 35. REPRODUCED.

Every successful request has output_tokens, but the dashboard sums only input_tokens under the name total_tokens. For the short default prompt this omits the 100 estimated output tokens.

Fix: Create per-request total_tokens = input_tokens + output_tokens and aggregate it, or rename to input_tokens.

```python
total_tokens=("input_tokens", "sum"),
```

### F14 · P2 · Saved reference profile cannot serve as monitor_batch reference metrics

[ModelData_Drift_Detection.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/ModelData_Drift_Detection.ipynb), cells 22. REPRODUCED.

Reloading reference_profile.joblib and supplying it as reference_metrics to monitor_batch. Cell 15 calls reference_metrics["confidence"].mean() and reference_metrics["predictions"].mean(); the artifact stores a scalar confidence and positive_rate, and has no predictions key.

Fix: Persist the complete reference_metrics dictionary with predictions/confidence arrays, or change monitor_batch to explicitly accept the persisted aggregate schema and use confidence/positive_rate scalars. Test monitoring after reloading the profile.

```python
reference_profile = {
    "features": FEATURES,
    "X_reference": X_reference,
    "accuracy": reference_accuracy,
    "confidence": reference_confidence,
    "positive_rate": reference_positive_rate
}
```

### F15 · P2 · Split synthetic text by template before reporting generalization metrics

[Neural_Network_JEV (1).ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Neural_Network_JEV%20(1).ipynb), cells 3. REPRODUCED.

Using validation_accuracy/test_accuracy as evidence of generalization to new enterprise documents. Cell 2 randomly repeats only eight templates per class and cell 3 splits rows rather than template groups; the RESUME class generates 100 rows from eight constant strings with no substitutions. Repeated template families can enter every split.

Fix: Track template_id during generation and group-disjoint split templates; also assert that normalized text and template IDs do not overlap across partitions. For enterprise generalization claims, evaluate on independently collected documents.

```python
train_data, temp_data = train_test_split(
    data,
    test_size=0.40,
    random_state=RANDOM_STATE,
    stratify=data["document_type"]
)
```

### F16 · P2 · Successful JEV calls do not return a usable routing decision

[Neural_Network_JEV (1).ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Neural_Network_JEV%20(1).ipynb), cells 19. REPRODUCED.

Calling route_document(row, use_jev=True) for any row passing hard_policy, when ask_jev succeeds. Every successful response returns JEV_RESPONSE instead of one of AUTO_PROCESS/HUMAN_REVIEW/ESCALATE, regardless of the service answer.

Fix: Parse the documented JEV response schema, validate the selected route against the three allowed decisions, and return it in decision; use HUMAN_REVIEW for absent/invalid choices. Add a mocked online-path test.

```python
response = ask_jev(row)

return {
    "decision": "JEV_RESPONSE",
    "source": "jev",
    "response": response
}
```

### F17 · P2 · Rerunning experiment cell counts deterministic duplicates as independent observations

[Prompt_Versioning_AB_Testing_Platform.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/Prompt_Versioning_AB_Testing_Platform.ipynb), cells 17, 18, 19, 26. SOURCE_CONFIRMED.

Rerun cell 19 without resetting cell 17, a normal interactive notebook action.

Fix: Make a run explicit: reset logs at the start of cell 19, or assign run IDs and deduplicate by experiment/subject/request and bootstrap independent subject clusters.

```python
experiment_logs.append(
        log
    )
...
for request_id in range(
    REQUESTS
):
...
    run_request(
        subject_id=request_id,
```

### F18 · P3 · Daily budget is a process-lifetime counter

[LLM_cost_Autopilot.ipynb](https://github.com/pablorod11/ML-AI-Projects/blob/87c9d2052b889e35cfbde6dd085a6e9bba36e7e5/LLM_cost_Autopilot.ipynb), cells 15. SOURCE_CONFIRMED.

For a kernel that stays alive across a UTC/local day boundary, spent_today is never reset. Conversely rerunning cell 10 resets spend during the same day. The advertised daily cap therefore cannot be enforced across days or notebook restarts.

Fix: Track date plus spend in persistent state; reset atomically when the defined billing day changes. Explicitly label session budget if persistence is intentionally out of scope.

```python
def budget_remaining():
    return DAILY_BUDGET - spent_today
```

## Euclidean proof scope

Definitions: completion means each original code cell returned without exception in the stated environment. Evaluation independence means a held-out source family is absent from training. Workload equality means both cost strategies price the same prompt cohort and outcome policy.

Checked execution claim: VALID within the offline harness, recorded cell statuses, and dependency snapshot. This is not universal correctness or proof across dependency versions.

Independent-source holdout claim: INVALID for the three measured text classifiers. Reproductions establish shared sources or exact text overlap. New-source generalization remains UNVERIFIED.

Autopilot comparison claim: INVALID for the default report because the workload cardinalities differ (2 versus 10). Arithmetic uses simulated prices and token heuristics.

Capacity example: VALID under supplied premises only. Node limit 5,000 RPS, 3 replicas, ingress 18,000 RPS, perfect even distribution. Total capacity 15,000 RPS; traffic per node 6,000 RPS; strict overflow true. No actual service capacity, packet-loss rate, or runtime reliability is established.

## Research-method checks

ARS validation status: ANALYZED. Default execution and targeted defects were checked; no independent scientific replication or population-level model validation is claimed.

All 11 requested statistical fallacy categories were considered for applicability:

- Simpson’s paradox: not established; no claimed aggregate-versus-subgroup reversal was demonstrated.
- Ecological fallacy: no group-to-individual causal claim identified.
- Berkson/selection bias: synthetic template sampling limits external validity; no population selection effect estimated.
- Collider bias: no applicable causal adjustment model identified.
- Base-rate neglect: synthetic balanced classes do not establish deployed prevalence or predictive values.
- Regression to the mean: no applicable before/after intervention claim tested.
- Survivorship bias: ERROR/UNKNOWN omissions in the confusion view are a confirmed failure-visibility defect. This does not establish longitudinal attrition bias.
- Look-elsewhere effect: multiple feature-drift tests use per-feature thresholds; family-wise false-positive control is not established.
- Garden of forking paths: deterministic demos are exploratory; preregistered confirmatory model-selection evidence is absent.
- Correlation versus causation: no real causal intervention was executed. Simulated savings are accounting outputs, not operational causal evidence.
- Reverse causality: not applicable to the deterministic/mock routing comparisons; no temporal causal identification claimed.

## Limits and reproduction

Execution used original notebook cell text through a Python harness, with IPython display support, noninteractive Matplotlib, per-notebook working directories, three concurrent processes, one numeric thread per process, and a 180-second per-notebook hard timeout. HTTP/network connections were blocked and TYPESAFE_API_KEY removed. Source code itself was not rewritten. Browser plots and interactive notebook frontends were not visually validated.

No product web interface exists in this repository; the design-workflow folder contains skills and documentation. Its product UI/accessibility/E2E stages therefore do not apply. Skill-format success is not UI validation. Optional APIs, GPU execution, deployment, long-running daily budgets, concurrent production review, and compatibility with other dependency versions remain UNVERIFIED. Dependencies are not pinned upstream; the included freeze records the tested environment.

Fresh artifacts, run logs, extracted source, reproductions, and original repository snapshot are included in validation-evidence.zip. No environment credentials are included.

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r repo-validation/requirements-validated.txt
.venv/bin/python repo-validation/run_notebooks.py
.venv/bin/python repo-validation/reproduce_ml.py
.venv/bin/python repo-validation/reproduce_ops.py
.venv/bin/python repo-validation/reproduce_llm.py
.venv/bin/python repo-validation/reproduce_boundaries.py
python3 ML-AI-Projects/euclidean/scripts/ecc.py --self-test
```
