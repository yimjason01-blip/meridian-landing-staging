# Aleron MD Project State

Last updated: 2026-05-17 07:10 PDT

## Current repo

- Repo: `meridian-landing`
- Remote: `https://github.com/yimjason01-blip/meridian-landing-staging.git`
- Branch: `main`
- Current HEAD: `31ada2f` (`Quiet Aleron footer layout`)
- Deploy target: GitHub Pages static site

## Current product state

Aleron MD is being developed as a premium preventive medicine landing experience plus companion decision tools.

The landing is currently split between:

- `index.html`: root deployed page
- `v2.html`: current higher-fidelity landing iteration

Treat `v2.html` as the current design candidate. Treat `index.html` as the current root entry. Do not merge or promote without an explicit task.

## Companion repo

The Quality of Life model lives in a separate repo:

- Repo: `qol-three-slider`
- Local sibling: `../qol-three-slider`
- Remote: `https://github.com/yimjason01-blip/qol-three-slider.git`
- Canonical tool file: `aleron.html`
- Live route: `https://yimjason01-blip.github.io/qol-three-slider/aleron.html`

The landing links to the Quality of Life model. Any change to that model must happen in the sibling repo.

## Important files in this repo

- `index.html`: root landing page
- `v2.html`: current higher-fidelity landing candidate
- `assets/`: image, video, illustration, logo, and generated media assets
- `prototypes/experience/`: experience design concepts
- `prototypes/trajectory/`: trajectory concepts
- `prototypes/engine/`: clinical engine concepts
- `handoffs/`: task handoffs for Codex, Hermes, or other agents

## Collaboration state

This repo is now prepared for Codex-style collaboration through:

- `AGENTS.md`
- `PROJECT_STATE.md`
- `handoffs/README.md`

The repo itself is the shared context boundary. Do not rely on chat memory as the source of truth.

## Current open questions

- Whether `v2.html` should replace `index.html` as the root public landing.
- Whether the Quality of Life model should remain a separate GitHub Pages repo or be brought into this repo as a subfolder.
- Whether older prototype files should be archived after the landing direction stabilizes.

## Verification baseline

No build step is required for the current static site.

Before declaring any user-visible copy or page change done:

1. Search changed files for em dashes.
2. Verify referenced assets exist.
3. Open the changed HTML locally or on GitHub Pages.
4. If behavior changed, test the actual browser interaction.
