# Selected Figma surfer frame swap

Date: 2026-05-30
Repo: `meridian-landing`
Source Figma frame: `694:44997` (`MacBook Pro 16" - 14`)
Source visual slide: `694:45052` (`Slide 16:9 - 54`)

## Goal

Replace the current surfer/ocean carousel image with the currently selected Figma execution, because the selected frame has the better visual treatment.

## Implementation

Rebuilt slide 2 (`hero02-*`) from the selected Figma visual slide while preserving the existing five-plane HTML contract:

1. `hero02-bg-plane.png`
   - `694:47607`
   - `694:45053`
   - `694:47598`
   - `694:47604`
2. `hero02-mid-blocks-plane.png`
   - `694:45054`
3. `hero02-subject-plane.png`
   - `694:45086`
4. `hero02-anchor-block-plane.png`
   - `694:45073`

Also saved:

- `hero02-selected-figma-reference.png`
- `hero02-selected-reference-vs-five-plane.png`

## Notes

The Figma exports for the image rectangles were clipped by the selected 1728 x 968 frame, so their visible x positions are:

- left tile: `x=0`
- center tile: `x=365`
- right sliver: `x=1595`

Using the original absolute bbox y offset would miscompose the assets, because the exported PNGs are already clipped vertically to the selected frame.

## Verification

The generated five-plane composite was compared against the selected Figma reference:

- mean RGB diff: `0.042`
- max diff: `22.33`
- pixels with diff > 50: `0`
- no diff bbox above threshold 35

The HTML was updated to cache-bust slide 2 assets with `five-plane-20260530e` and build signature `five-plane-test-20260530e-selected-surfer-frame`.

Because the selected frame has four carousel items, the hero count chrome was also corrected from `/005` to `/004` and the initial current count from `004` to `001`.
