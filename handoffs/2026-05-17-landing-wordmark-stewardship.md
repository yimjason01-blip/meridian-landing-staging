# Landing wordmark and stewardship copy

Date: 2026-05-17 17:23 PDT
Agent: GPT-5.5 via OpenAI Codex
Repo: aleron-md consolidated workspace and meridian-landing-staging deploy repo
Branch: main
Base SHA: a6e751e in landing deploy repo
Final SHA or patch status: pending commit at handoff creation

## Goal

Apply the new Aleron MD wordmark treatment to the marketing landing page and make the membership value address the optimized-patient problem.

## Files changed

- `index.html`: updated nav and footer wordmark styling, retained the MD data-source icon row, and changed the membership section to maintained-advantage stewardship copy.
- `v2.html`: matched the wordmark and stewardship copy changes for the higher-fidelity landing candidate.

## Behavior changed

The landing page now shows a compact Aleron MD lockup with a gold monospace MD separated by a vertical divider. The lower membership section now answers why a healthy member keeps Aleron MD: maintaining position, detecting drift, knowing what not to chase, and applying new evidence personally.

## Verification

- Opened `http://127.0.0.1:8094/index.html?fix=wordmark-stewardship` locally.
- Confirmed DOM and computed styles show the new lockup: flex wordmark, `JetBrains Mono` MD, gold MD color, and visible left divider.
- Confirmed hero text is present after the change.

## Open risks or follow-up

- Need GitHub Pages propagation check after deploy.
- Visual model could not analyze the full screenshot because the screenshot exceeded model dimension limits; DOM and browser smoke checks passed locally.
