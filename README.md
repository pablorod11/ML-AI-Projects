# ML, AI, and MLOps projects

Personal projects exploring model evaluation, retrieval, monitoring, routing, and AI-assisted engineering workflows. The notebooks are self-contained demonstrations built around synthetic examples or bundled datasets. Their metrics describe those examples; they do not establish production accuracy, reliability, or cost savings.

## Project index

- [Linear regression](Linear_Regression_Model.ipynb): train, evaluate, and save a regression model on generated data.
- [Image classification](Image_Classification_Pipeline.ipynb): classify scikit-learn's bundled handwritten digits and inspect predictions.
- [Model regression detection](Copy_of_Model_Regression_Detection_System.ipynb): compare candidate and baseline models and apply deployment gates.
- [Data and model drift](ModelData_Drift_Detection.ipynb): monitor generated batches for distribution and performance changes.
- [Enterprise autocoding](Enterprise_Autocoding_MLOps_Platform.ipynb): demonstrate document classification, confidence routing, evaluation, and monitoring.
- [Human review pipeline](HITL_Review_Pipeline.ipynb): route low-confidence predictions for review and model retraining.
- [Hybrid retrieval and evaluation](Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb): compare lexical, latent semantic, and hybrid retrieval on validation examples, then report retrieval quality and routing on a separate held-out test cohort. This is the maintained RAG notebook.
- [LLM evaluation and regression testing](LLM_Eval_Regression_Testing_Framework.ipynb): compare simulated model outputs, track invalid responses, and apply release gates.
- [Prompt versioning and A/B testing](Prompt_Versioning_AB_Testing_Platform.ipynb): compare simulated prompt variants and log experiment results.
- [LLM cost autopilot](LLM_cost_Autopilot.ipynb): explore simulated request routing, token costs, and budgets.
- [Neural network and JEV integration](Neural_Network_JEV%20%281%29.ipynb): combine a local classifier and decision routing with an optional external service adapter.

## Setup and run

Clone the repository and create an isolated Python environment. The [validation guide](validation/README.md) contains the supported offline reproduction commands and [pinned dependencies](validation/requirements.txt):

```sh
git clone https://github.com/pablorod11/ML-AI-Projects.git
cd ML-AI-Projects
python3.12 -m venv .venv
.venv/bin/python -m pip install -r validation/requirements.txt
.venv/bin/python -m unittest discover -s validation -p "test_*.py" -v
.venv/bin/python validation/run_notebooks.py
```

For interactive exploration, open a notebook in a Jupyter-compatible editor using this environment and run its cells in order. The pinned validation environment supplies the execution dependencies; an interactive notebook editor is separate. Notebooks write local reports and model artifacts. The offline runner isolates each notebook under `validation/runs` and blocks network connections.

See [current validation results](validation/CURRENT_RESULTS.md) for recorded checks and limitations. Historical baseline reports describe the revisions named in those reports and can reference filenames that have since been consolidated. Notebook outputs can become stale after source changes; rerun the validation commands to produce fresh evidence.

## Offline demonstrations and live services

The LLM evaluation, prompt experiments, and cost-routing examples simulate responses or costs locally. The RAG notebook uses local TF-IDF and truncated SVD retrieval; it constructs prompts without calling a hosted generation model. The classification and monitoring examples use synthetic or bundled data rather than a production data feed.

The JEV notebook defaults to offline routing. Its optional live path requires explicitly enabling `use_jev`, configuring `TYPESAFE_API_KEY`, and checking the external service's current endpoint, model, and response contract. Offline validation removes the API key and does not verify live service compatibility, billing, or production deployment behavior. Keep credentials outside notebooks and saved outputs.

## Agent coordination skills

These directories contain reusable instructions and supporting references, separate from the ML demonstrations:

- [Napolean](napolean/README.md): coordinate bounded specialist missions and verify the integrated result. [Integration guidance](napolean/references/integrations.md) explains optional dependencies, including Graphify and its source-inspection fallback.
- [Napolean Security](napolean-security/README.md): coordinate scoped security reviews and evidence-backed vulnerability validation.
- [Design Workflow](design-workflow/README.md): coordinate UI direction, implementation, audits, and browser checks.
- [Euclidean](euclidean/README.md): check explicit claims against stated premises, with a standalone capacity-checking example.

Follow each skill's installation and dependency instructions. Copying a coordination skill does not install its external runtimes or enable its optional integrations.
