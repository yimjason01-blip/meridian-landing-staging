# Aleron Figma Hero Rebuild Specification

## Purpose

**In brief.** This spec resets the Aleron hero work back to first principles. The goal is not to keep repairing the current HTML file, and it is not to ship a flat screenshot wrapper. The goal is to rebuild the page from the original Figma source with a clear layer manifest, a defined DOM contract, and objective visual acceptance tests.

The rest of this spec defines the source of truth, the build mode, the layer model, the implementation sequence, and the gates that must pass before the page is shown as working.

## Defined Terms

- **Source frame**: the actual Figma frame or child frame that represents the intended web section.
- **Reference export**: a full-frame PNG export from Figma used only as the visual oracle for comparison.
- **Layer manifest**: a written table of every shipped visual layer, including Figma node ID, name, bounding box, source asset, DOM element, z-order, and motion behavior.
- **Artwork plane**: a raster layer that contains photography, masked photography, complex gradients, or complex Figma boolean geometry.
- **Stable UI layer**: real DOM text or controls that do not move during hero slide transitions, including logo, headline, CTA buttons, slide count, and carousel controls.
- **Depth plane**: a semantic grouping used for stacking, such as background photo, anchored color mass, floating block, foreground subject, or stable UI.
- **Motion layer**: a layer allowed to transform during carousel or parallax behavior.
- **Anchored layer**: a layer that must not move during carousel or parallax behavior.
- **Hotspot**: an invisible clickable region over a flat reference image. Hotspots are allowed only for reference mocks, not for the final layered website rebuild.
- **Acceptance crop**: a screenshot crop from the browser and the matching crop from the Figma reference export, used for visual comparison.

## Decision: rebuild as a layer-faithful website, not a flat mock

**In brief.** The correct deliverable is a real website rebuild that preserves Figma visual fidelity while keeping the important elements as inspectable HTML layers. A flat full-frame export is useful as a reference oracle, but it is not the product because it bakes in text, buttons, counts, and geometry. The previous failure came from mixing these modes: first too many hand-patched fragments, then an overcorrection to flat screenshots.

This section establishes the only acceptable build mode for the restart.

### Chosen mode

Build a **layer-faithful HTML reconstruction**:

- Full Figma frame exports are used as visual references only.
- Photos and complex geometric/gradient groups may be raster assets.
- Logo, headline, buttons, slide count, dots, and section text are real DOM unless the Figma source proves they should be image-only.
- Every significant DOM or raster layer is traceable to a Figma node ID.
- No hand-placed visual layer ships without an entry in the layer manifest.

### Rejected modes

1. **Flat screenshot page**
   - Rejected because it bakes UI into pixels and prevents real motion, responsive behavior, text edits, and clean clickable controls.

2. **Incremental patching of the current messy file**
   - Rejected because the current file has accumulated corrections without a single authoritative layer map.

3. **Freehand visual approximation**
   - Rejected because the user explicitly wants the original Figma design, not a redesign.

## Source of Truth

**In brief.** Figma is the source of truth, not the current HTML file and not the latest deployed page. The current HTML may be used only as a list of prior mistakes and possibly a source of known asset filenames. The rebuild starts by extracting the Figma node tree and producing a fresh layer manifest before any HTML is written.

The rest of this section defines exactly what must be pulled from Figma.

### Required Figma source material

For each hero slide and each following section included in the file:

- Source frame ID
- Full-frame reference PNG export
- Child node tree at sufficient depth to see visual layers
- Every text node and its exact string
- Every visible button/control node and its bounding box
- Every photo/image fill node and its bounding box
- Every complex group, boolean, gradient, mask, or union that must be exported as a raster asset
- Hidden or duplicate layers, explicitly marked as ignored or used

### Known Figma context from the failed pass

Known page:

- Figma page: `Hero Treatment`

Known source candidates already observed:

- Outer page frame: `674:41346`, `MacBook Pro 16" - 73`
- Slide frame candidate: `674:41401`, `MacBook Pro 16" - 14`
- Slide 2 inner frame candidate: `674:41815`, `MacBook Pro 16" - 14`
- Slide 3 inner frame candidate: `674:42168`, `MacBook Pro 16" - 14`
- Slide 4 inner frame candidate: `674:42997`, `MacBook Pro 16" - 14`
- Curve section candidate: `674:41519`, `Frame 68`

These are not automatically final. The rebuild must confirm the intended source frames from the Figma document before coding.

## Layer Model

**In brief.** The hero is treated as a stack of semantic depth planes, not as a pile of images. Each plane has one job: photo, anchored mass, floating block, foreground subject, or stable UI. Motion is allowed only on layers explicitly marked as motion layers in the manifest.

The rest of this section defines the required planes and rules.

### Required hero planes

1. **Background photo plane**
   - Contains the base photographic image or images.
   - May be a raster export if Figma uses masks, fills, or crops that are expensive to recreate.

2. **Anchored color mass plane**
   - Contains large left-side color fields, broad geometric masses, and static branded block structures.
   - Must not parallax unless the Figma reference or explicit design direction says it should move.

3. **Floating block plane**
   - Contains only the smaller independent geometric blocks intended to move or enter with the carousel.
   - Each block must have its own Figma node ID and bounding box.
   - No floating block may be added by eye.

4. **Foreground subject plane**
   - Used only when a person, hand, face, body, or object must visually occlude a block.
   - If Figma does not provide a clean cutout, a derived cutout may be created, but it must be labeled as derived and visually audited for halos.

5. **Stable UI plane**
   - Logo, headline, CTA buttons, slide counts, carousel dots, and other controls.
   - Built as real DOM unless the section is explicitly a static reference mock.
   - Does not move during slide transitions.

### Required section planes after the hero

For each non-hero section:

- Static art or chart raster plane if the chart is complex.
- Real DOM text and buttons if the text and controls are meant to be editable or clickable.
- Layer manifest entries for each exported asset and DOM control.

## Layer Manifest Requirements

**In brief.** The layer manifest is the contract between Figma and code. It prevents the rebuild from turning into another pile of guessed CSS positions. No implementation starts until the manifest exists for the first hero slide and the pattern is approved.

Each manifest row must include:

- Slide or section name
- Figma node ID
- Figma node name
- Node type
- Bounding box relative to source frame: `x`, `y`, `width`, `height`
- Exported asset filename, if any
- DOM selector
- Depth plane
- Z-order
- Motion behavior: anchored, carousel, parallax, or none
- Notes: hidden, duplicate, derived, or intentionally ignored

### Example row shape

```text
Slide 1 | 674:41459 | Lawrence photo foreground | RECTANGLE | x 224, y 0, w 1506, h 968 | slide1-foreground.png | .slide-1 .foreground-subject | foreground subject | z 40 | carousel only | derived alpha check required
```

## Implementation Sequence

**In brief.** The implementation must proceed in small, checkable phases. Each phase produces an artifact that can be compared to Figma before the next phase starts. If a phase fails visual comparison, the rebuild stops there instead of stacking more fixes on top.

### Phase 0: preserve and isolate

- Save the current messy HTML as an archive file.
- Create a fresh rebuild file or branch.
- Do not edit the current production file until the rebuild passes local gates.

### Phase 1: source extraction

- Pull the Figma document info.
- Confirm the exact source frames for the hero slides and following sections.
- Export full-frame reference PNGs for each source frame.
- Save the raw node JSON or MCP output to a local reference directory.

### Phase 2: manifest first

- Produce the layer manifest for slide 1.
- Review it against the Figma node tree and full-frame export.
- Only after slide 1 manifest is coherent, repeat for slides 2 to 4 and the curve section.

### Phase 3: static rebuild before motion

- Build the HTML/CSS with no carousel animation and no parallax.
- Render one slide at a time.
- Match the Figma reference at desktop size first.
- Verify real DOM controls are clickable.
- Verify no horizontal overflow.

### Phase 4: responsive fit

- Add responsive behavior only after desktop matches.
- Test mobile using explicit breakpoints.
- Preserve the intended crop and hierarchy instead of scaling every Figma coordinate blindly.

### Phase 5: carousel

- Add carousel behavior only after all static slides match.
- Stable UI layer remains fixed.
- Only motion-approved artwork planes move.
- No opacity fade if the desired behavior is slide-in motion.

### Phase 6: parallax

- Add scroll parallax last.
- Parallax applies only to layers marked as `motion behavior: parallax` in the manifest.
- Broad anchored masses must report `transform: none` during scroll.

### Phase 7: deploy only after verification

- Commit the rebuild.
- Push to the deploy branch.
- Confirm the live URL serves the new signature strings and assets.
- Browser-check the live URL before calling it done.

## Acceptance Gates

**In brief.** A rebuild is acceptable only if it passes structural, visual, interaction, responsive, and deployment gates. A visual pass alone is not enough, and a code pass alone is not enough. The final claim must be backed by the live URL, not local files.

### Structural gates

- Layer manifest exists and matches all shipped layers.
- Every meaningful asset has a source Figma node ID or a `derived` label.
- No obsolete backup asset directory is referenced.
- No untracked visual assets are required for the page to render.
- No DOM layer exists solely because it looked right by eye.

### Visual gates

- Full hero screenshot compared against full-frame Figma reference at desktop size.
- Acceptance crops checked for the main occlusion points and geometric blocks.
- Each carousel slide checked after transition settles.
- Curve section checked against its reference export.
- No duplicated text, duplicated buttons, or baked-plus-live UI overlap.

### Interaction gates

- Top CTA is a real clickable anchor or button.
- Demo CTA is a real clickable anchor or button.
- Carousel controls are keyboard-focusable if visible.
- Play Video is a real clickable anchor or button.
- Focus states are visible.

### Responsive gates

- `document.documentElement.scrollWidth === window.innerWidth`.
- Key CTA remains inside the viewport on laptop and mobile.
- No font size below 12px.
- Mobile crop preserves the intended visual subject and readable text.

### Motion gates

- At scroll midpoint, only parallax-approved elements have transforms.
- During carousel transition, stable UI bounding boxes do not move.
- Reduced-motion mode disables large transforms.

### Deployment gates

- Git status is clean in the deploy repo.
- Commit is pushed to the live branch.
- Live URL returns the new HTML signature.
- Live browser check shows 0 missing images and 0 horizontal overflow.

## Non-Goals

**In brief.** This restart is a rebuild, not a redesign. The spec intentionally excludes new art direction, new copy, and animation experiments until the static Figma-faithful version is correct. The point is to recover trust in the source mapping before adding behavior.

Out of scope until the rebuild passes:

- New hero copy
- New section design
- New photo choices
- New geometric language
- Parallax tuning
- Carousel motion polish
- Performance micro-optimizations beyond obvious image sizing

## Stop Conditions

**In brief.** If the rebuild starts drifting, the work stops before more fixes are layered on. The correct response to repeated visual mismatch is to return to the Figma node tree and layer manifest, not to add another CSS patch. Three failed visual patch attempts means the architecture is wrong.

Stop and re-check the source if any of these happen:

- A block appears in the browser but is not in the manifest.
- A block is missing and cannot be traced to a Figma node.
- A foreground cutout has a rectangular background or visible halo.
- The same visual bug survives two patch attempts.
- Browser vision contradicts the source frame export.
- A full-frame export looks right but the layered version cannot match it.

## First Implementation Task

**In brief.** The first real task is not coding. The first task is to generate the source-frame inventory and layer manifest for slide 1, then compare it to the full-frame reference. Only after that passes should a fresh HTML file be created.

Deliverable for the first task:

1. `figma-source-inventory.md`
2. `figma-layer-manifest.md`
3. `assets/figma-reference/hero-01-reference.png`
4. One browser screenshot of the reference export only
5. A short decision note confirming the source frame and build mode
