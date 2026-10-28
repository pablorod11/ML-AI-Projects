# ML, AI, and MLOps projects

I use these projects to practice model evaluation, retrieval, monitoring, and confidence-based routing. The repository also contains reusable skills for coordinating engineering work and checking claims.

The notebooks use synthetic examples or bundled datasets. Their metrics describe those examples; they do not establish production accuracy, reliability, or cost savings.

[Portfolio and demos](https://pablo-rodriguez-portfolio.awakejoy13.chatgpt.site/) · [Recorded validation](validation/CURRENT_RESULTS.md) · [Run the checks](validation/README.md)

## Current project releases

- [Exact-response LRU/TTL cache](caching/README.md): standard-library Python caching with version-aware keys, expiry, bypass controls, and eight documented tests. A simulated repeated-input benchmark reduces mock calls from 24 to three; unique prompts show no reduction.
- [QuantLab Probability Research](https://huggingface.co/spaces/PabloRod11/quantlab-probability-research): a browser-local workbench with chronological calibration/model selection/evaluation, numerical diagnostics, and audit exports. A separate Python benchmark uses synthetic data; neither establishes a trading edge.
- [Imperial LLM model 004](https://huggingface.co/spaces/PabloRod11/imperial-llm): an upstream-derived character Transformer adapted for browser inference and continued training. Its card records 6.20% lower next-character test loss on a fresh 64-story same-domain sample. The hardened source download has verified Linux checks; [GitHub integration remains a draft PR](https://github.com/pablorod11/ML-AI-Projects/pull/2), separate from the published Space.

## Resumes

Updated October 27, 2026. Each PDF is two pages and links to current project evidence.

- [Python Developer and Software Engineer](https://pablo-rodriguez-portfolio.awakejoy13.chatgpt.site/python-software-engineer-resume.pdf?v=39)
- [AI and ML Evaluation](https://pablo-rodriguez-portfolio.awakejoy13.chatgpt.site/ai-mlops-resume.pdf?v=39)
- [Business Systems and Data Quality](https://pablo-rodriguez-portfolio.awakejoy13.chatgpt.site/business-systems-resume.pdf?v=39)

## Start here

- **Retrieval:** [Hybrid retrieval and evaluation](Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb) compares lexical, latent semantic, and hybrid retrieval on validation examples, then reports results on a separate held-out test cohort.
- **Model quality:** [Model regression detection](Copy_of_Model_Regression_Detection_System.ipynb) compares candidate and baseline models and applies deployment gates.
- **Human review:** [Human review pipeline](HITL_Review_Pipeline.ipynb) routes low-confidence predictions for review and model retraining.
- **Agent workflows:** [Napolean](napolean/README.md) coordinates bounded specialist missions and verifies the integrated result. Small tasks stay inline.

## Notebook studies

### Train and inspect models

- [Linear regression](Linear_Regression_Model.ipynb): train, evaluate, and save a regression model on generated data.
- [Image classification](Image_Classification_Pipeline.ipynb): classify scikit-learn's bundled handwritten digits and inspect predictions.
- [Neural network and JEV integration](Neural_Network_JEV%20%281%29.ipynb): combine a local classifier and decision routing with an optional external service adapter.

### Evaluate, monitor, and route

- [Model regression detection](Copy_of_Model_Regression_Detection_System.ipynb): compare candidate and baseline models and apply deployment gates.
- [Data and model drift](ModelData_Drift_Detection.ipynb): monitor generated batches for distribution and performance changes.
- [Enterprise autocoding](Enterprise_Autocoding_MLOps_Platform.ipynb): demonstrate document classification, confidence routing, evaluation, and monitoring.
- [Human review pipeline](HITL_Review_Pipeline.ipynb): route low-confidence predictions for review and model retraining.

### Explore retrieval and LLM evaluation

- [Hybrid retrieval and evaluation](Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb): compare retrieval methods on validation examples and report held-out test quality and routing. This is the maintained RAG notebook.
- [LLM evaluation and regression testing](LLM_Eval_Regression_Testing_Framework.ipynb): compare simulated model outputs, track invalid responses, and apply release gates.
- [Prompt versioning and A/B testing](Prompt_Versioning_AB_Testing_Platform.ipynb): compare simulated prompt variants and log experiment results.
- [LLM cost autopilot](LLM_cost_Autopilot.ipynb): explore simulated request routing, token costs, and budgets.

## Reproduce the offline checks

The [October 24, 2026 validation record](validation/CURRENT_RESULTS.md) reports 23 passing regression tests and 11 maintained notebooks completing 351 code cells. That record describes the checked revision and documents the host-specific font workaround. Rerun the commands below to check your own environment.

Clone the repository and create an isolated Python environment using the [pinned dependencies](validation/requirements.txt):

```sh
git clone https://github.com/pablorod11/ML-AI-Projects.git
cd ML-AI-Projects
python3.12 -m venv .venv
.venv/bin/python -m pip install -r validation/requirements.txt
.venv/bin/python -m unittest discover -s validation -p "test_*.py" -v
.venv/bin/python validation/run_notebooks.py
```

The offline runner isolates each notebook under `validation/runs` and blocks network connections. Notebooks write local reports and model artifacts. For interactive exploration, open a notebook in a Jupyter-compatible editor using the same environment and run its cells in order; the editor is separate from the pinned execution dependencies.

The [validation guide](validation/README.md) explains the supported reproduction workflow. Historical baseline reports describe the revisions named in those reports and can reference filenames that have since been consolidated. Notebook outputs can become stale after source changes.

## Simulation and live-service boundaries

The LLM evaluation, prompt experiments, and cost-routing examples simulate responses or costs locally. The RAG notebook uses local TF-IDF and truncated SVD retrieval; it constructs prompts without calling a hosted generation model. Classification and monitoring examples use synthetic or bundled data rather than a production feed.

The JEV notebook defaults to offline routing. Its optional live path requires explicitly enabling `use_jev`, configuring `TYPESAFE_API_KEY`, and checking the external service's current endpoint, model, and response contract. Offline validation removes the API key and does not verify live service compatibility, billing, or production deployment behavior. Keep credentials outside notebooks and saved outputs.

Plot appearance, live APIs, GPU behavior, shared multiuser concurrency, and production deployment remain unverified by the recorded offline checks.

## Reusable engineering skills

These directories contain instructions and supporting references, separate from the notebook demonstrations:

- [Napolean](napolean/README.md): coordinate bounded specialist missions and verify the integrated result. [Integration guidance](napolean/references/integrations.md) covers optional dependencies and source-inspection fallbacks.
- [Napolean Security](napolean-security/README.md): coordinate scoped security reviews and validate candidate vulnerabilities against evidence.
- [Design Workflow](design-workflow/README.md): coordinate UI direction, implementation, audits, and browser checks.
- [Euclidean](euclidean/README.md): check explicit claims against stated premises, with a standalone capacity-checking example.

Follow each skill's installation and dependency instructions. Copying a coordination skill does not install its external runtimes or enable optional integrations. See each skill's documentation for credits and validation limits.
