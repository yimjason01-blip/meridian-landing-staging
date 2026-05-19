# Member portal link from landing

Date: 2026-05-19
Agent: Hermes, gpt-5.5 via OpenAI Codex
Repo: /Users/jasonyim/Projects/meridian-landing
Branch: main
Base SHA: 8759710
Final SHA or patch status: pending commit

## Goal

Link the public Aleron MD landing page to the member portal flow by bringing over the Join CTA pattern and the intermediate login screen from the consolidated Aleron workspace.

## Files changed

- `index.html`: updated top nav to show Quality of Life, Join, and Login. Login points to `login.html`. Mobile sticky primary CTA now reads Join.
- `v2.html`: mirrored the same nav and mobile CTA change so the design candidate stays aligned.
- `login.html`: copied the intermediate member login simulation into this repo. It routes successful sign-in to `member.html` and uses demo identity text.
- `member.html`: copied the member portal prototype into this repo.

## Behavior changed

Landing visitors can now click Login from the desktop nav, arrive at the intermediate login screen, enter the simulation password, and continue into the member portal. Join still routes to the application section.

## Verification

- Confirmed `login.html` and `member.html` exist in the repo.
- Checked div, section, nav, main, and footer tag balance for changed HTML files. All tested deltas were zero.
- Scanned changed files for em dashes. Remaining hits are in CSS comments or HTML comments only.
- Opened local `index.html`, clicked Login, entered `password123`, and verified navigation into `member.html`.

## Open risks or follow-up

- This is still a static simulated login, not real authentication.
- The member portal contains synthetic patient content and should be reviewed before use as a public demo route.
