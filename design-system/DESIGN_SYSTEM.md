---
title: Aleron MD Design System
status: production kit draft
updated: 2026-06-01
source: Figma Reference page, live landing, current brand assets
---

# Aleron MD Design System

## Job

Help a builder create Aleron public, login, application, and member-facing surfaces without re-deciding brand, layout, or interaction details.

## Source of truth

See `PROVENANCE.md` for source-lane ownership. Do not add a token, asset, component, or pattern without a source lane.

1. Figma `Reference` page exports in `design-system/assets/reference-page/`
2. Brand assets in `design-system/assets/`
3. Semantic tokens in `tokens.css`
4. Shared primitives in `components.css`
5. Page patterns in `patterns.css`
6. Live landing implementation for behavior and layer mechanics

## Provenance

Every item belongs to one of these lanes: `figma-reference`, `figma-trajectory`, `figma-illustration`, `live-hero`, `identity-favicon`, `wordmark`, `login`, `landing-surface`, `component-derived`, or `excluded`.

## Build order

1. Import `patterns.css` for pages, or `components.css` for component-only surfaces.
2. Compose with section patterns first.
3. Use components inside patterns.
4. If a needed style is missing, add a semantic token or component before using it in page code.

## Foundations

- Surfaces: page, paper, cream, bone, card, dark, and sourced login dark.
- Text: primary, secondary, tertiary, inverse, inverse muted.
- Actions: primary, secondary, on-dark, hover, focus.
- Type: display, h1, h2, h3, body large, body, caption, label.
- Spacing: 4 px base scale from 4 to 128.
- Layout: max width, measure, gutters, section rhythm, breakpoints.
- Shape: square by default. Border radius is zero unless a source asset requires otherwise.
- Motion: subtle color, opacity, and border changes. No bounce or decorative motion.

## Components

- Wordmark and icon logo
- Header and footer
- Buttons with hover, disabled, and loading states
- Inputs, textareas, selects with focus, error, success, disabled
- Cards and panels
- Tabs
- Alerts
- Modal shell
- Code snippets

## Patterns

- Reference page overview
- Landing hero
- Landing hero reference from `figma-hero-shot.html`
- Trajectory proof from the Reference page frames
- Texture/moment screen references
- Application form section
- Login shell
- CTA/footer section

## Usage rules

- Use approved favicon, icon logo, and wordmark assets.
- Use `Apply for Membership` for acquisition actions.
- Use `Log In` for account entry.
- Do not use `Join`.
- Use square CTAs.
- Use approved fades and color roles only.
- Use the Figma Reference page for hero visual language, trajectory, illustration, texture, and palette decisions before using live-page leftovers.
- Do not inherit raw `Demo` CTA copy or rust Login tiles from Reference hero screenshots.
- Use human photography and editorial proof modules.
- Use isometric warm-brown objects or flat outlined registration-corner icons for moment illustrations.
- Do not use the old curve thumbnail or dark gold curve render as canonical design-system references.
- Clinical values must include units every time.
