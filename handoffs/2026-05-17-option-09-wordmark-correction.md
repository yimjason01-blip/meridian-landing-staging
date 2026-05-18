# Option 09 wordmark correction

Date: 2026-05-17 17:43 PDT
Agent: GPT-5.5 via OpenAI Codex
Repo: aleron-md consolidated workspace and meridian-landing-staging deploy repo
Branch: main
Base SHA: c42426f in landing deploy repo
Final SHA or patch status: pending commit at handoff creation

## Goal

Replace the incorrect extrapolated Aleron MD wordmark with the supplied `aleron-md-option-09-black.svg` direction.

## Files changed

- `index.html`: changed nav and footer wordmark to serif `Aleron MD`, with Aleron regular and MD bold, no divider, no gold MD.
- `v2.html`: matched the same wordmark correction.
- `assets/logos/aleron-md-option-09-black.svg`: added reference SVG asset matching the supplied option-09 direction.

## Behavior changed

The landing page no longer uses the compact divided lockup. It now uses the option-09 style: title-case Aleron in regular serif and all-caps MD in bold serif.

## Verification

- Opened `http://127.0.0.1:8094/index.html?fix=option09-serif` locally.
- Browser computed styles confirmed Source Serif 4 regular for Aleron and Source Serif 4 bold for MD, no divider, no gold MD.
- Vision checked cropped rendered viewport and confirmed the logo matches the option-09 style and the hero remains intact.

## Open risks or follow-up

- Need GitHub Pages propagation check after deploy.
