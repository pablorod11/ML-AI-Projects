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

The runner blocks network connections, removes the optional API key, and writes only under validation/runs. Each notebook has a 180-second timeout. Matplotlib uses a noninteractive backend; rendered plots, live service schemas, and production deployments are not verified.
