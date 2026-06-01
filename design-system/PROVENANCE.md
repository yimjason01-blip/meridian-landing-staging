# Aleron MD Design System Provenance

This file prevents source-lane conflation. Every reusable asset, token, component, and pattern must identify its source lane before it becomes part of the design system.

## Source lanes

### live-hero

Current executed landing hero.

- Canonical file: `figma-hero-shot.html`
- Live route: `https://yimjason01-blip.github.io/meridian-landing-staging/figma-hero-shot.html`
- Layer manifest: `figma-layer-manifest.md`
- Layer assets: `assets/figma-hero-layers/`
- Belongs here: hero layer stack, carousel mechanics, parallax mechanics, hero logo placement, hero CTA geometry.

### figma-reference

Reference exports used for comparison and visual anchoring.

- Files: `assets/figma-reference/*.png`
- Belongs here: reference thumbnails, curve reference, visual checks.
- Does not become production code unless copied into a pattern intentionally.

### identity-favicon

Browser and icon identity assets.

- Files: `assets/favicon.svg`, favicon PNGs, ICO, Apple touch icon.
- Design-system copies: `design-system/assets/icon-logo-lowercase-a.png`, `favicon-16.png`, `favicon-32.png`, `apple-touch-icon.png`.
- Belongs here: icon logo preview, favicon set, logo fade token.

### wordmark

Aleron wordmark assets.

- Primary asset: `assets/figma-hero-layers/logo_4x.png`.
- Design-system copies: `wordmark-lowercase-figma.png`, `wordmark-lowercase-ink.png`.
- Belongs here: header/brand lockup examples.

### login

Aleron-owned login surface.

- Canonical file: `login.html`.
- Belongs here: login page gradient, square login panel, login form pattern.

### landing-surface

General landing surfaces and non-hero sections.

- Files: `index.html`, `v2.html`, selected sections in `figma-hero-shot.html`.
- Belongs here: page, cream, bone, paper surfaces; proof/curve section wrappers.

### component-derived

System primitives derived from repeated usage and build needs.

- Files: `design-system/components.css`, `design-system/patterns.css`.
- Belongs here: buttons, fields, cards, tabs, alerts, modal shell, forms.
- Rule: if a component introduces a new visual decision, add a sourced token first.

### excluded

Do not import these into the current design system.

- Reverted pitch deck aesthetic pass.
- Synthetic hero mock from the first production-kit draft.
- Unverified black/gold/tan historical marketing tokens.
- Any generated visual that is not in the live landing, Figma source, favicon assets, login, or member surface.

## Token source map

- `--amd-logo-icon-fade`: identity-favicon.
- `--amd-login-fade`: login.
- `--amd-color-surface-page`: live-hero / landing-surface.
- `--amd-color-surface-paper`: landing-surface.
- `--amd-color-surface-cream`: live-hero / landing-surface / login.
- `--amd-color-surface-bone`: landing-surface.
- `--amd-color-surface-dark`: live-hero / login.
- `--amd-color-surface-deep`: login.
- `--amd-color-rust`: identity-favicon.
- `--amd-color-rust-figma`: live-hero.
- `--amd-color-navy`: identity-favicon.
- `--amd-color-navy-figma`: live-hero.
- `--amd-color-hero-blue`: live-hero.
- Status colors: component-derived pending stronger product source.

## Build rule

When adding anything new, label it with one of the source lanes above. If no lane fits, it is not ready for the design system.
