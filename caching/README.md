# Cached LLM Cost Autopilot

Open `../LLM_cost_Autopilot.ipynb` in Jupyter or Colab and run all cells. It retains the local project's session-budget fixes and adds an exact-response cache. This directory contains cache tests, a benchmark, and recorded results.

The cache uses only Python's standard library: an OrderedDict with at most 128 entries, LRU eviction, and a 300-second TTL. Keys contain the full exact prompt, selected model, and RESPONSE_CONFIG_VERSION. Increment that version when templates, backend versions, or generation settings change. No lowercasing or semantic matching occurs. The cache is ephemeral, sequential, and intended for a single-user notebook. Do not share it between users without adding access isolation and concurrency controls.

Hits return the original response, log zero inference cost and tokens, and remain available after the session inference budget is exhausted. Logs include cache hits, lookup time (including routing), full request latency, and avoided estimated inference cost. Errors are logged, propagated, and never cached or charged by this mock implementation. A real provider may charge for failed requests; reconcile its usage separately. `use_cache=False` bypasses cache reads and writes. Clearing response_cache removes all retained responses.

## Verification

Using the existing project environment with numpy, pandas, matplotlib, and nbformat:

```sh
python test_cache.py
python benchmark.py
```

Eight tests pass: repeated-response reuse and accounting, exhausted budgets, expiry, configuration changes, model changes, bounded LRU eviction, bypass and exact matching, and provider errors. All 38 notebook code cells executed successfully and nbformat schema validation passed. The headless verification emitted three expected matplotlib warnings because plots cannot display under the Agg backend; plots render when the notebook is run interactively. Notebook outputs are cleared; rerun it to regenerate all displays.

## Single-run benchmark

See benchmark_results.json for the recorded measurements. For 24 requests cycling over three prompts, caching reduced mock model calls from 24 to 3, elapsed time from 628.098 ms to 113.684 ms, and estimated cost from $0.0084184 to $0.0010523 (87.5% lower). Responses matched exactly.

For 24 unique prompts, both modes made 24 model calls at the same estimated cost. Elapsed time increased from 295.339 ms to 327.352 ms in this run. These timings include noise; this is not a statistically established overhead estimate.

The notebook uses mock_llm, simulated sleeps, estimated tokens, and illustrative prices. No paid inference was performed. These results demonstrate avoided work on repeated inputs, not real provider savings or production performance.

Source: local working copy of https://github.com/pablorod11/ML-AI-Projects, copied on 2026-10-24. The cache extension is included in this repository.
