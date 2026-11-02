---
title: Imperial LLM
emoji: 🏛️
colorFrom: gray
colorTo: green
sdk: static
app_file: index.html
pinned: false
license: mit
short_description: A small story Transformer running in your browser.
---

# Imperial LLM: character model 004

A 30,643-parameter causal Transformer continued from Imperial model 003. Two blocks, four heads, 32-dimensional embeddings, 64-character context and 51-character vocabulary. No external pretrained weights, instruction tuning, retrieval or safety training. It remains an educational story-continuation model, not an assistant.

## Training and selection

Full-parameter AdamW continuation on the 512 packaged normalized TinyStories training stories. Two runs share initialization, seed 1729, uniform story/window training draws, batch 16 and gradient clip 1.0. Windows never cross story boundaries. One run uses constant LR 0.001; the other cosine LR 0.0003→0.00003. Both execute 2400 optimizer steps; validation is checked every 200 steps, retaining the minimum including step 0. Early stopping patience 3 is configured but neither run stops early. The constant schedule at step 2400 wins by validation CE alone. Training/validation runtime of selected run: 89.3s on CPU, PyTorch 2.2.2, one thread. Its inherited model 003 had 2400 earlier continuation steps; this release adds 2400 more.

## Evaluation

Fresh final test CE, nats per normalized character: **1.615683 → 1.515439**, **6.20% lower**. Sampled loss improves on62/64 stories; largest per-story increase: 0.022554. Baseline and candidate use the same inputs and targets. Four seeded 64-character windows per story yield16,384 predictions; windows may overlap. Final test is scored after checkpoint and schedule selection; it is never used for gradients or retuning.

Validation CE: 1.610060 → 1.508940; selected-checkpoint training CE: 1.480559. These use story-contained windows, so they are not directly comparable to model 003's published stream-window losses. Only validation was recorded over time; no training curve is fabricated. The page displays a validation-only curve and the separately measured selected-checkpoint training CE.

## Data and license

Modified normalized TinyStories V2 GPT-4 by Ronen Eldan and Yuanzhi Li, revision f54c09fd23315a6f9c86f9dc80f725de7d8f9c64. Data license: [CDLA-Sharing-1.0](https://cdla.dev/sharing-1-0/); code: MIT. Training and validation reuse 512 and 64 whole stories, respectively. The fresh test comprises 64 additional complete official-validation-source stories whose normalized hashes are absent from all 640 packaged train/validation/old-test stories. Exact duplicates are excluded; near duplicates were not assessed. Normalization retains the original model 002 alphabet: curly apostrophes become ASCII, unsupported capitals become lowercase, other unsupported characters become spaces. Corpus files, original notices, attribution and exact membership hashes are included in source.zip.

## Limits

Lower next-character cross-entropy does not establish improved story coherence, reasoning, instruction following, safety or out-of-domain generalization. Generated samples remain misspelled and often incoherent. The same-domain final sample is small; one training seed and overlapping sampled windows do not establish statistical significance. The inherited validation set already informed model 003. The 64-character context is a major constraint.

## Identity and reproduction

Candidate JSON SHA-256:`986699bbf0668f6d1aa5da67c373fe53770f7ce5e9efb3e337b5c0d7a42fe376`. Baseline JSON SHA-256:`f68c3ffac926081593dca074191c9845aa1a09c5830be1c1f088f9c63b147f0a`. Checkpoint and JSON contain identical weights; training.json carries hashes, three Python logit cases, schedule histories and corpus provenance. Read REPRODUCE.md. The source includes models/story-baseline003 for exact reinitialization. The full upstream Python suite is not green on the measured legacy runtime; see RELEASE_CHECKS.json for executed release checks and documented upstream failures.
