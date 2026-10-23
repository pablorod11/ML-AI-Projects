# Reproduce model004

Extract source.zip and enter imperial-llm. The exact model003 starting weights are in models/story-baseline003; space/ contains the selected model004. Use Python3.12 with the measured PyTorch2.2.2 CPU runtime (macOS x86_64). Normalized licensed corpus and fresh test membership are bundled; no dataset download is required.

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements-story.txt
.venv/bin/python -m pytest tests/test_finetune_stories.py -q
.venv/bin/python scripts/finetune_stories.py --baseline models/story-baseline003 --output experiments/reproduction-new
.venv/bin/python scripts/prepare_story_release.py --run experiments/reproduction-new --output experiments/browser-preview-new
node experiments/browser-preview-new/test_inference.cjs
node experiments/browser-preview-new/test_generation.cjs
```

Choose a new output directory. Test evaluation occurs only after validation selection; subsequent reruns are reproducibility checks, not new independent holdouts. No retraining or fresh-test rescoring was performed to prepare this release. The exact original executed training script is preserved in evidence/finetune_stories.executed.py. Later edits add an explicit baseline path and import formatting; weights are unchanged.

For the packaged release:

```sh
npm ci
npm run test:model
npx playwright install chromium firefox webkit
npm run test:browser
python3 -m http.server 4173 --bind 127.0.0.1 --directory space
```

The browser suite covers generation, stop, invalid inputs, failure recovery, deep links, keyboard focus, desktop/mobile layout and the validation-only learning curve. Four optional screenshot-baseline tests remain skipped unless explicitly enabled and reviewed on matching OS/browser. Full upstream Python tests require a newer supported PyTorch/Python environment for compile/RMSNorm and available distributed loopback. Passing focused/release checks does not imply the broad suite is green.
