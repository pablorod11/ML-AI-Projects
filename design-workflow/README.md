# Design Workflow

A reusable coordination skill for AI-assisted UI work: choose a coherent visual direction, build with care, audit the interface, and verify it in a browser.

## What it coordinates

- [Taste](https://github.com/Leonxlnx/taste-skill): art direction and visual iteration.
- [Emil Kowalski’s skills](https://github.com/emilkowalski/skills): interface details and motion craft.
- [Impeccable](https://github.com/pbakaus/impeccable): critique, polish, and scoped refinement.
- [Awesome Design MD](https://github.com/VoltAgent/awesome-design-md): concrete design references.
- [Vercel Web Design Guidelines](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines): UI code audits.
- [ECC](https://github.com/affaan-m/ECC): engineering verification and E2E testing patterns.
- [Playwright skill](https://github.com/openai/skills/tree/main/skills/.curated/playwright): real browser checks.

The workflow keeps the user’s brief and existing brand authoritative, chooses one primary direction, and loads only relevant specialist guidance. It does not claim that combining more rules automatically produces better design.

## Included here

- `skills/design-workflow/`: the coordinating skill and Codex metadata.
- `skills/awesome-design-references/`: a reference helper with an attributed, pinned catalog and its upstream MIT license.
- `sources.json`: the upstream revisions used in the validated local setup.

The specialist upstream repositories remain dependencies, not vendored copies or claims of original authorship.

## Installation

Install the two skills in this folder using a compatible skill installer, or copy each skill folder into your agent’s skills directory. Install the specialist dependencies using their linked official instructions. The coordinating skill expects these sibling folders:

```text
design-workflow/
awesome-design-references/
design-taste-frontend/
emil-design-eng/
impeccable/
web-design-guidelines/
verification-loop/
e2e-testing/
playwright/
```

Additional skills from Emil’s repository are useful for specialized tasks but are not required to understand the coordinating workflow. Installing this folder alone does not install those dependencies, Playwright browsers, or Impeccable’s engine.

A compatible installer can discover the custom skills from this repository:

```sh
npx skills add pablorod11/ML-AI-Projects --skill design-workflow awesome-design-references -a codex -g
```

Follow each dependency’s current supported installation path. Avoid installing the same upstream skill through multiple methods. Impeccable can download a pinned engine on first use; review its upstream runtime and telemetry documentation. Automatic hooks are separate project setup.

## Use

```text
Use $design-workflow to improve the settings page. Preserve the existing brand,
use Emil’s guidance for motion, audit with Web Design Guidelines,
and verify the key flow with Playwright.
```

## Validation and limits

The local 23-skill setup passed Codex skill validation and ECC’s strict skill-format validation. ECC’s four Codex surface checks passed in an isolated fixture including its required MLE entry. Impeccable’s engine probe, Taste’s library command, and Playwright CLI help succeeded. Host-provided Playwright locators also inspected a real browser page successfully.

These are installation and readiness checks, not evidence that a product UI passed accessibility, visual regression, or E2E tests. The complete ECC repository suite and a fresh-machine dependency installation were not tested. Report checks that could not run as unverified.

## Attribution

This repository’s contribution is the coordination workflow and reference helper. The named projects belong to their respective authors; no affiliation or endorsement is implied. The bundled Awesome Design catalog is from VoltAgent/awesome-design-md at the revision in sources.json; its original license is preserved in `skills/awesome-design-references/references/LICENSE`.
