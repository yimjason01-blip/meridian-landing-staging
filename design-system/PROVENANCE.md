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

Primary visual-language source allocated by the designer.

- Figma page: `Reference` (`785:6560`).
- Design-system copies: `design-system/assets/reference-page/*.png`.
- Belongs here: hero visual treatments, trajectory frames, illustration systems, texture/moment screens, and palette.
- Hero screenshots provide visual language only. Production CTA copy, acquisition CTA placement, and header behavior come from the live hero contract and current product rules.
- This is primary for initial design-system language. The live Website page is implementation evidence, not the source of visual vocabulary.

### figma-trajectory

Trajectory and curve grammar from the Reference page.

- Figma frames: `2` (`785:7272`), `3` (`785:7322`), `4` (`785:7169`).
- Belongs here: cream grid fields, PolySans narrative headlines, Space Mono axes and section indicators, gradient curve strokes, square data markers, dashed counterfactuals, and small annotation cards.
- Excludes: `assets/curve.jpg` dark gold render and the old `figma-curve-thumb.webp` screenshot as canonical references.

### figma-illustration

Illustration and icon grammar from the Reference page texture frames.

- Figma frames: `Texture` frames under the `Icon Set A (Isometric)` and `Icon Set B (Flat Outlined)` labels.
- Belongs here: warm-brown isometric object illustrations with dark strokes, flat outlined document/order icons with registration-corner marks, sparse mobile moment screens, and bottom-anchored single CTAs.

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
- Old `figma-curve-thumb.webp` curve screenshot as a canonical reference.
- Dark gold `assets/curve.jpg` render for the light Aleron system.
- Raw `Demo` CTA copy and rust Login tiles visible inside Reference hero screenshots.
- Unverified black/gold/tan historical marketing tokens.
- Any generated visual that is not in the live landing, Figma source, favicon assets, login, or member surface.

## Token source map

- `--amd-logo-icon-fade`: identity-favicon.
- `--amd-login-fade`: login.
- `--amd-reference-main-fade`: figma-reference / Color Palette.
- `--amd-reference-warm-fade`: figma-reference / Color Palette.
- `--amd-color-surface-page`: figma-reference / live-hero / landing-surface.
- `--amd-color-surface-paper`: landing-surface.
- `--amd-color-surface-cream`: figma-reference / live-hero / landing-surface / login.
- `--amd-color-surface-bone`: landing-surface.
- `--amd-color-surface-dark`: figma-reference / live-hero / login.
- `--amd-color-surface-burgundy`: figma-reference / Color Palette.
- `--amd-color-surface-deep`: login / figma-reference.
- `--amd-color-rust`: identity-favicon.
- `--amd-color-rust-figma`: figma-trajectory.
- `--amd-color-rust-reference`: figma-reference / Color Palette.
- `--amd-color-gold-reference`: figma-reference / Color Palette.
- `--amd-color-navy`: identity-favicon.
- `--amd-color-navy-figma`: figma-trajectory.
- `--amd-color-reference-blue`: figma-reference / Color Palette.
- `--amd-color-hero-blue`: live-hero.
- Status colors: component-derived pending stronger product source.

## Verified lineage (2026-06-01)

Reference tokens checked node-by-node against Figma page `Reference` (`785:6560`) using the Talk to Figma bridge, not from memory. Every value below is EXACT to its source node fill (hex match).

Color Palette slide (`Slide 16:9 - 27`, `785:7645`):

- `--amd-color-surface-page` `#FFFEFB` = Rectangle 128 `#fffefb`. EXACT.
- `--amd-color-surface-cream` `#EFEAE0` = Rectangle 127 `#efeae0`. EXACT.
- `--amd-color-surface-dark` `#242426` = Rectangle 123 `#242426`. EXACT.
- `--amd-color-surface-burgundy` `#2C1F29` = Rectangle 129 `#2c1f29`. EXACT.
- `--amd-color-reference-blue` `#3C4662` = Rectangle 124 `#3c4662`. EXACT.
- `--amd-color-rust-reference` `#A35520` = Rectangle 126 `#a35520`. EXACT.
- `--amd-color-gold-reference` `#CD9453` = Rectangle 125 `#cd9453`. EXACT.
- `--amd-reference-main-fade` `#232426 -> #3B4662` = Rectangle 131 gradient `#232426 -> #3b4662`. EXACT stops.
- `--amd-reference-warm-fade` `#A35520 / #532F4B 43% / #23315F 93%` = Rectangle 132 gradient `#a35520 / #532f4b 42.9% / #23315f 92.7%`. EXACT stops (rounded positions).

Trajectory frame (`4`, `785:7169`):

- `--amd-color-rust-figma` `#A2653B` = curve data marker Rectangle 165 `#a2653b`. EXACT.
- `--amd-color-navy-figma` `#2C3240` = axis labels and indicator markers `#2c3240`. EXACT.

Asset-sourced lanes (no palette pigment to match): `--amd-logo-icon-fade` and `--amd-color-rust`/`--amd-color-navy` derive from the favicon icon (rasterized asset); `--amd-login-fade` from `login.html`; `--amd-color-hero-blue` from the live hero. These are correct by lane assignment, not palette-swatch comparison.

Result: 11/11 palette and trajectory tokens confirmed, zero drift. Re-run this check with the Talk to Figma bridge before any palette change ships.

## Build rule

When adding anything new, label it with one of the source lanes above. If no lane fits, it is not ready for the design system.
