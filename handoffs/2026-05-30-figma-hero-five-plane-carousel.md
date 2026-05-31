# Figma hero five-plane carousel layering

Date: 2026-05-30 17:46 PDT
Agent: Hermes via OpenAI Codex
Repo: `meridian-landing`
Branch: `main`
Base SHA: `d1a36d7`
Final SHA or patch status: committed with this handoff

## Goal

Apply the approved five-plane Figma hero layering strategy from slide 1 to the remaining carousel images so the carousel can use the same parallax contract across all four slides.

## Files changed

- `figma-hero-shot.html`: replaced flattened slide 2, 3, and 4 artwork images with four explicit planes per slide: background, midground moving blocks, foreground subject, and anchored foreground block structure. Updated the hero build signature and image cache-bust query to `five-plane-20260530b`.
- `assets/figma-five-plane-test/hero02-*.png`: new slide 2 five-plane assets plus Figma reference and composite proof.
- `assets/figma-five-plane-test/hero03-*.png`: new slide 3 five-plane assets plus Figma reference and composite proof.
- `assets/figma-five-plane-test/hero04-*.png`: new slide 4 five-plane assets plus Figma reference and composite proof.
- `assets/figma-five-plane-test/hero02-04-five-plane-contact.png`: contact sheet comparing original Figma exports to the new five-plane composites.

## Behavior changed

All carousel slides now share the same semantic depth contract:

1. background photo plane moves lightly,
2. midground block plane moves fastest for parallax,
3. subject cutout moves with the photo plane,
4. anchored foreground block structure stays locked above the subject,
5. existing DOM chrome stays stable above the slide art.

The old `hero-artwork` flattened images are no longer used by slide 2, slide 3, or slide 4.

## Verification

- Read the live original Figma frame tree for the remaining selected hero frames: `674:41760`, `674:42167`, and `674:42942`.
- Exported fresh Figma source layers for the remaining slide frames and generated five-plane assets from those exports.
- Static asset check: all `<img src>` paths in `figma-hero-shot.html` exist.
- Static copy check: `figma-hero-shot.html` contains zero em dashes.
- Local browser check at `http://127.0.0.1:8766/figma-hero-shot.html?v=local-five-plane-20260530b`:
  - all four slides have four `.five-plane-layer` images,
  - zero `.hero-artwork` images are used in slides,
  - no broken image decodes,
  - active slide layers compute to z-indexes 1, 2, 3, and 4 with the anchored layer at z-index 4.
- Local visual checks captured screenshots for slides 2, 3, and 4 after clicking through the carousel.

## Open risks or follow-up

- The five-plane assets intentionally follow the approved simplified semantic contract rather than preserving every construction rectangle from the raw Figma boolean groups. This matches the slide 1 layering strategy Jason approved.
- Mobile remains in full-canvas inspection mode from the earlier task. Jason has not separately approved whether that should become the final mobile crop behavior.
