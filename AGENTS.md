# Aleron MD Agent Guide

This repo is the primary Aleron MD landing and prototype workspace.

## Source of truth order

1. `PROJECT_STATE.md` for current state and canonical file choices.
2. `AGENTS.md` for collaboration rules.
3. The current git commit.
4. `handoffs/` for task-specific implementation notes.
5. Existing HTML/CSS/JS files.

If these disagree, stop and update `PROJECT_STATE.md` before making product changes.

## Product boundaries

Aleron MD is a premium preventive medicine brand and care experience.

Aleron MD is not GOVO2. Do not import GOVO2 consent, Apple Sign In, workout, VO2max, Watch, or App Store release assumptions.

Aleron MD is related to Meridian as a product and clinical-intelligence lineage, but the public site must stand on its own.

## Repo shape

This repo contains:

- public landing pages and visual iterations
- image, video, logo, and illustration assets
- prototype subfolders for experience, trajectory, and engine concepts

The Quality of Life teaching tool is a separate sibling repo:

- local sibling: `../qol-three-slider`
- live route: `https://yimjason01-blip.github.io/qol-three-slider/aleron.html`

Do not assume all Aleron MD work lives in this repo. If a task touches the Quality of Life model, inspect the sibling repo too.

## Canonical files

`v2.html` is the current higher-fidelity landing iteration.

`index.html` is the root GitHub Pages entry and may lag `v2.html`. Do not overwrite either file unless the task explicitly says to promote or sync the canonical landing.

## Writing rules

- No em dashes in any user-facing prose.
- No rounded-pill eyebrow tags above headlines.
- Prefer direct, premium, physician-led language.
- Avoid generic longevity claims.
- Avoid marketing filler that could fit any concierge clinic.
- Keep medical claims grounded. If citing a clinical value, include the unit every time.

## Design rules

- Keep the Aleron MD palette warm, quiet, and premium.
- Preserve the current high-touch, human, editorial feel.
- Do not add generic SaaS gradients, neon accents, or dashboard-heavy visual language unless explicitly asked.
- Before replacing assets, verify the actual asset and rendered result.

## Codex handoff contract

For every non-trivial task:

1. Read `AGENTS.md` and `PROJECT_STATE.md` first.
2. Confirm whether the task is landing-only or also touches `../qol-three-slider`.
3. Check git status before editing.
4. Make the smallest coherent change.
5. Run at least a static verification pass:
   - search for em dashes in changed HTML/MD files
   - verify changed links or asset paths exist
   - open changed HTML locally if behavior or layout changed
6. Add a task handoff in `handoffs/` when the change is substantial.
7. Commit code and handoff together.

## Handoff file requirement

Use `handoffs/README.md` as the template. Include files changed, behavior changed, verification commands, and open risks.

## Deployment notes

This is a GitHub Pages static site. There is no build step unless a future task adds one.

If public behavior changed, push to the tracked branch and verify the live route after GitHub Pages updates.
