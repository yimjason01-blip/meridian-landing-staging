# Figma hero slide 3 motion block fix

Date: 2026-05-30
Agent: Hermes via OpenAI Codex
Repo: `meridian-landing`
Branch: `main`
Base SHA: `1cf12df`

## Goal

Restore the two missing rectangular motion blocks on the beach runner carousel slide.

## Files changed

- `assets/figma-five-plane-test/hero03-mid-blocks-plane.png`: added the two missing Figma-derived motion blocks.
- `assets/figma-five-plane-test/hero03-five-plane-composite.png`: regenerated the slide 3 proof composite.
- `figma-hero-shot.html`: cache-busted slide 3 image URLs to `five-plane-20260530d` and updated the build signature to `five-plane-test-20260530d-slide3-motion-blocks`.

## Root cause

The slide 3 mid block plane had been simplified too aggressively. It kept the central dark block but omitted:

1. the top-center warm block from Figma node `674:42206`,
2. the right-side dark block from Figma node `674:42200`.

These two regions were visible in the full Figma reference but absent from the generated five-plane composite.

## Fix

Used the Figma exports as source pixels and patched only those two missing regions into `hero03-mid-blocks-plane.png`, preserving the existing five-plane contract:

1. background photo,
2. midground moving blocks,
3. subject cutout,
4. anchored foreground blocks,
5. DOM chrome.

## Verification

- Pixel comparison against `hero03-figma-reference.png` improved from large missing-region diffs to only small edge residuals.
- New composite diff stats: mean RGB diff `0.085`, pixels over threshold 35: `831`.
- Verified the top-center and right-side block regions now contain nontransparent pixels in the mid block plane.
- Verified the corrected composite visually includes both missing blocks.

## Open risks

- Remaining diff pixels are minor 1 to 2 px edge alignment artifacts, not missing blocks.
- The broader carousel still uses the full-canvas mobile fit from the earlier mobile patch.
