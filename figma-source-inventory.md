# Figma Source Inventory

## Decision

Build mode: layer faithful HTML reconstruction.

Figma is the source of truth. Full frame PNG exports are visual references only. Real UI stays in DOM. Complex photography, masks, gradients, and boolean geometry use raster assets exported from Figma and mapped by node ID.

## Source page

- Figma page: Hero Treatment
- Outer frame: 674:41346, MacBook Pro 16" - 73, 1728 x 2509
- Hero slide 1: 674:41401, MacBook Pro 16" - 14, 1728 x 968
- Hero slide 2: 674:41815, MacBook Pro 16" - 14, 1728 x 968
- Hero slide 3: 674:42168, MacBook Pro 16" - 14, 1728 x 968
- Hero slide 4: 674:42997, MacBook Pro 16" - 14, 1728 x 968
- Curve section: 674:41519, Frame 68, 1728 x 861

## Reference exports

- assets/figma-reference/hero-01-reference.png from 674:41401
- assets/figma-reference/hero-02-reference.png from 674:41815
- assets/figma-reference/hero-03-reference.png from 674:42168
- assets/figma-reference/hero-04-reference.png from 674:42997
- assets/figma-reference/curve-reference.png from 674:41519

## Shipped layered asset directory

- assets/figma-hero-layers/

This directory contains the raster depth planes and derived subject cutouts used by the clean rebuild.

## Build contract

- Do not ship the rebase full frame PNGs as the hero.
- Use the full frame PNGs only for reference comparison.
- Preserve stable UI as DOM: logo, headline, Apply, Demo, slide counts, dots, Play Video.
- Only elements marked as motion layers may transform during carousel or scroll.
- Broad color masses and static grid groups remain anchored during scroll.
