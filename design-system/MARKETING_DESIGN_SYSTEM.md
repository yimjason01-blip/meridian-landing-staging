---
title: Aleron MD Design System
status: locked lowercase reference
updated: 2026-06-01
source: live landing, Figma hero frames, current lowercase favicon asset
---

# Aleron MD Design System

## Identity

Aleron MD is premium preventive medicine with a lowercase, warm, human, editorial visual system. The system starts with the lowercase white `a` on a rust-to-navy fade, then expands into the Figma hero language: human photography, hard rectangular color planes, cream editorial sections, rust/navy curves, and restrained physician-led copy.

Use the approved Aleron assets and visual references in this folder. Do not substitute historical, deck, or generic medical SaaS directions.

## Source stack

1. Live public landing root: `https://yimjason01-blip.github.io/meridian-landing-staging/`
2. Figma hero source inventory: `figma-source-inventory.md`
3. Figma hero layer manifest: `figma-layer-manifest.md`
4. Reference exports:
   - `assets/figma-reference/hero-01-reference.png`
   - `assets/figma-reference/hero-02-reference.png`
   - `assets/figma-reference/curve-reference.png`
5. Identity assets:
   - `assets/favicon.svg`
   - `assets/favicon-512.png`
   - `assets/apple-touch-icon.png`
   - `assets/figma-hero-layers/logo_4x.png`

## Brand assets

- Icon logo: lowercase white `a` on rust-to-navy fade.
- Favicon: same lowercase fade asset at SVG, ICO, 16, 32, 48, 192, and 512 px.
- Apple touch icon: same identity, 180 px.
- Primary landing wordmark: Figma PNG wordmark, lowercase `aleron` with `MD` treatment, white on dark/fade.
- Ink wordmark: generated from the same Figma PNG alpha for light backgrounds. Do not substitute the title-case fallback in lowercase-system artifacts.

## Color tokens

- `--amd-bg`: `#FFFEFB`, warm near-white page.
- `--amd-cream`: `#EFEAE0`, editorial cream section.
- `--amd-bone`: `#ECE5D6`, clinical light section.
- `--amd-grid`: `#DED8CC`, faint structural grid.
- `--amd-ink`: `#242426`, primary text and panel ink.
- `--amd-ink-deep`: `#0F1014`, dark field.
- `--amd-navy`: `#1E2A4A`, identity fade endpoint.
- `--amd-navy-figma`: `#2C3240`, Figma curve and block navy.
- `--amd-hero-blue`: `#414C6A`, hero base field.
- `--amd-rust`: `#B9562A`, identity fade start and CTA accent.
- `--amd-rust-figma`: `#A2653B`, Figma curve/block rust.
- `--amd-warm-band`: `#F3CE97`, quiet warm radial band.
- `--amd-fade-icon`: rust-to-navy identity gradient.
- `--amd-fade-hero`: rust, burgundy, navy photo overlay.

## Typography

- Display: `Inter Tight`, 500, tight tracking, large and quiet.
- Body/UI: `Inter`, 400 to 600, never shouty.
- Wordmark: use the asset first. Do not recreate by eye when the asset is available.
- Serif: `Source Serif 4` only for editorial warmth, quotes, and fallback wordmark contexts.
- Mono: only for age markers, file paths, counters, and technical labels.

## Geometry

- CTAs are square-edge. `border-radius: 0`.
- Header CTA is a single square `Log In` button.
- `Apply for Membership` belongs in the hero or section CTA slot, not as a second header button.
- Figma hero blocks are hard-edged rectangles. Do not round them.
- Cards and panels stay square unless the source asset itself has a radius.
- Eyebrows are plain uppercase text, not pills.

## Components

### Header

- Left: lowercase Figma wordmark asset.
- Right: one square-edge `Log In` action.
- No `Join` label.
- No frosted pill, no rounded capsule cluster, no dual top-right CTA set.

### Buttons

- Primary on dark: transparent or cream fill with square corners.
- Primary on light: ink or rust with square corners.
- Ghost: 1 px stroke, square corners, no blur.
- Hover: slight color/luminance shift only. No bounce, glow, or rounded treatment.

### Icon system

- Icons must be two-color or one-color.
- Approved language: modular pictograms, plan symbols, cut-paper apertures, dither or hatching.
- If an icon needs more than two colors to work, it does not belong in the lowercase system.
- Do not use dark analytic mysticism, HUD anatomy, wireframe people, neon networks, or generic AI brain imagery.

### Sections

- Hero: human photography plus rust-to-navy hard block/fade system.
- Curve/proof: cream field, faint grid, rust-to-navy curve, square markers.
- Login/member: calm square panels, lowercase icon identity, no invented glows.
- Photo sections: warm analog photography. Product UI supports the story, it does not lead it.

## Hard rules

1. Do not use the uppercase black `A` favicon as a source for this system.
2. Do not use the reverted pitch deck as reference.
3. Do not make CTAs rounded or frosted.
4. Do not put `Apply` in the public header unless Jason explicitly changes the header model.
5. Do not use `Join` on public Aleron acquisition surfaces.
6. Do not invent fades. Pull from Figma or the current favicon fade.
7. Do not let charts become generic dashboards.
8. Do not use pill eyebrows.
9. Do not strip units from clinical values.
10. Do not write melodramatic patient copy.

## What this is not

- Not the uppercase black `A` identity branch.
- Not a pitch deck theme.
- Not a medical SaaS dashboard skin.
- Not a generic concierge clinic brand.
- Not a cold AI-health analytic interface.

## Verification checklist

- The design-system page has favicon links pointing to the lowercase fade asset.
- The visible icon logo is lowercase `a` on rust-to-navy fade.
- The visible wordmark uses the Figma lowercase wordmark asset.
- Buttons render square, not rounded.
- Source references include Figma hero and curve thumbnails.
- No uppercase favicon cache-bust appears in the design-system files.
