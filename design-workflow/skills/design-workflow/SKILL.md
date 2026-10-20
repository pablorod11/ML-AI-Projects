---
name: design-workflow
description: Coordinate installed Taste, Emil Kowalski, Impeccable, Awesome Design references, Vercel UI guidelines, ECC verification, and Playwright for building or improving web interfaces.
---

# Design workflow

Use only the installed resources relevant to the request. This workflow applies to UI work; it does not auto-start a redesign or browser session when asked only to explain or install skills.

## Resolve authority and direction

User instructions and the project's established brand, behavior, stack, and accessibility requirements take priority. Choose one primary design direction instead of merging contradictory aesthetics. Taste supplies art direction when requested; Awesome Design supplies concrete references; Emil supplies component and motion craft; Impeccable supplies scoped refinement and critique. A refinement preserves the existing identity; a requested redesign may establish a replacement direction.

## Work through the relevant stages

1. Inspect the actual project and request. Record any known product context and design constraints. For an existing UI, capture the relevant before state when browser access is available.
2. For new visual direction, use the sibling `design-taste-frontend/SKILL.md`. For real design-system examples, use `awesome-design-references/SKILL.md` and open only a relevant reference. Record a coherent direction using the project's existing DESIGN.md convention when available.
3. Implement the requested change with the existing stack. Use `emil-design-eng/SKILL.md` and focused Emil skills for component behavior, motion, performance, mobile interaction, and stress cases. Apply `impeccable/SKILL.md` and its matching command reference for critique, polish, accessibility, or responsive refinement. Read each skill before applying it; resolve conflicting aesthetic advice through the chosen direction and explicit project constraints.
4. Audit the touched UI using `web-design-guidelines/SKILL.md`, which fetches the current Vercel guidelines. Report actionable findings with file and line evidence, and repair in-scope issues.
5. Use ECC's `verification-loop/SKILL.md` and `e2e-testing/SKILL.md` for relevant engineering checks. Run the project's existing checks and tests; do not add unrelated tools or fabricate coverage. An unavailable check is UNVERIFIED, not PASS. For small reversible styling changes, do not introduce tests that merely mirror the implementation.
6. Use `playwright/SKILL.md` for real browser verification when a runnable UI exists. If the host provides an approved Playwright browser tool, use that host's interaction and confirmation rules. Otherwise follow the CLI skill. Prefer the project's existing test setup for durable E2E tests when requested. Exercise the key user flow, keyboard/focus behavior, narrow and wide viewports, overflow, loading/empty/error states when applicable, and reduced motion for animated work. Inspect screenshots and fix observed issues before repeating relevant checks.
7. Report what changed, what ran, and material limitations. A skill installation or CLI help check is not evidence that a product UI passed visual, accessibility, or E2E validation.

## Installed resources

Resolve these paths relative to this skill's parent directory; read only what you need:

- `design-taste-frontend/SKILL.md`: visual direction and its render-and-inspect loop.
- `emil-design-eng/SKILL.md`: UI and motion craft; additional Emil skills cover specialized work.
- `impeccable/SKILL.md`: scoped design commands and critique.
- `awesome-design-references/SKILL.md`: reference catalog.
- `web-design-guidelines/SKILL.md`: current UI audit rules.
- `verification-loop/SKILL.md`: ECC engineering verification.
- `e2e-testing/SKILL.md`: ECC Playwright test patterns.
- `playwright/SKILL.md`: browser automation.

Impeccable's skill includes a launcher that may need network access to download its pinned engine on first use. Hook installation and browser extensions are separate project setup, not prerequisites for using these skills. Do not overwrite host configuration or enable hooks implicitly.
