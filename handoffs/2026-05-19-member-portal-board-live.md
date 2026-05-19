# Member portal board live update

Date: 2026-05-19
Agent: Codex
Repo: meridian-landing
Branch: main
Base SHA: eccd251
Final SHA or patch status: committed on main

## Goal

Apply the member portal board updates to the legacy landing repo that backs the GitHub Pages route at `https://yimjason01-blip.github.io/meridian-landing-staging/member.html`.

## Files changed

- `member.html`: updated the Plan board model, renamed the visible workspace label to Patient Portal, and kept the Summary tab as two paragraphs only.

## Behavior changed

- The visible label now reads Patient Portal.
- Upcoming contains six locked, muted cards with lock icons and no patient actions.
- Top priorities contains three patient-action cards that open a detail modal.
- The detail modal has a top-level Mark as complete action and an inline confirmation step.
- Confirming completion moves the priority into Physician review as a waiting item.
- Physician review cards are static waiting items.

## Verification

- `git diff --check -- member.html` passed.
- Searched `member.html` for em dashes, none found.
- Local browser check at `http://127.0.0.1:8793/member.html` confirmed Patient Portal label, two summary paragraphs, six locked upcoming cards, three priority actions, zero draggable cards, zero card tab indexes, and no console errors.

## Open risks or follow-up

- GitHub Pages update timing depends on the push completing and Pages propagation.
