# Repository validation

Current repair verification: [CURRENT_RESULTS.md](CURRENT_RESULTS.md).

The baseline report describes commit 87c9d2052b889e35cfbde6dd085a6e9bba36e7e5 before repairs. It is historical evidence, not a claim about later source revisions.

Run all notebook code cells in fresh offline processes:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r validation/requirements.txt
.venv/bin/python -m unittest discover -s validation -p "test_*.py" -v
.venv/bin/python validation/run_notebooks.py
python3 euclidean/scripts/ecc.py --self-test
```

The runner blocks Python socket connections, removes the optional API key, and runs each notebook under validation/runs. This is a reproduction harness, not a security sandbox for untrusted notebooks. Each notebook has a 180-second timeout. It writes summary.json before exiting: exit 0 means a nonempty suite passed; exit 1 means a notebook failed, timed out, or no notebooks were found. Matplotlib uses a noninteractive backend; rendered plots, live service schemas, and production deployments are not verified.

The maintained RAG notebook is `Hybrid_RAG_Retrieval_Eval_Pipeline.ipynb`. The former `(1)` copy was consolidated into it; historical reports retain their original filenames and hashes.
