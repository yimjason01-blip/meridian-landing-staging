# Handoff: Aleron design system — Reference-page source + reorg

## State (current)
Live: https://yimjason01-blip.github.io/meridian-landing-staging/design-system/
Source repo: `/Users/jasonyim/Projects/meridian-landing/`, source on `main`, deployed by copying `design-system/` to `gh-pages`.

Latest commits:
- `main`: `ef2e71b` (reorg), preceded by `529dba5`, `8c77d42`.
- `gh-pages`: `a8ba77a`.

## What this work established
1. Primary visual-language source is the Figma `Reference` page (`785:6560`), NOT the `Website` page and NOT old Website-derived curve thumbnails.
2. Reference page lanes, captured as exports in `design-system/assets/reference-page/`:
   - Hero visual treatment (photo + warm-to-navy gradient field + axis-aligned rectangular mosaic blocks + white lowercase wordmark).
   - Trajectory language (cream grid, PolySans headline, Space Mono axes/section nav, gradient curve, square markers, dashed counterfactual, small annotation cards).
   - Illustration Set A: isometric warm-brown object illustrations with dark stroke.
   - Illustration Set B: flat outlined icons with registration/crop-mark corners.
   - Texture moments: sparse mobile status screens, one centered illustration/icon, one bottom-anchored CTA.
   - Palette: charcoal `#242426`, burgundy black `#2C1F29`, slate blue `#3C4662`, reference rust `#A35520`, reference gold `#CD9453`, cream `#EFEAE0`, page white, warm fade, main fade.

## Hard separations (do not re-conflate)
- Hero appears in exactly TWO places, by role:
  - "Hero visual lane" card in the Source map = visual language only.
  - "Hero implementation pattern" in Patterns = live hero mechanics (`figma-hero-shot.html`, `figma-layer-manifest.md`).
- Reference hero screenshots are visual-only. Do NOT inherit raw `Demo` CTA copy, rust Login tiles, or header behavior from them. Production header/CTA = single `Log In` in header, `Apply for Membership` acquisition CTA, square edges, never `Join`.
- Excluded: old `figma-curve-thumb.webp` and dark gold `assets/curve.jpg` as canonical curve refs; rounded/frosted CTA families; pitch-deck styling.

## Visible page order (locked)
Overview, Identity, Source map, Foundations, Typography, Components, Forms, Patterns, Implementation.
- Earlier mistake fixed: had 3 overlapping hero concepts (Assets card + Reference page + Patterns) and separate Assets/Reference/Provenance sections. Now: Identity = marks only; Source map = source-lane logic; Patterns = one hero implementation + trajectory proof + form + login + CTA.

## Files
- `design-system/index.html` — visible kit.
- `design-system/tokens.css` — semantic + Reference-page palette tokens.
- `design-system/components.css`, `patterns.css`, `base.css`.
- `design-system/DESIGN_SYSTEM.md`, `MARKETING_DESIGN_SYSTEM.md` (kept in sync), `PROVENANCE.md` (source-lane ownership).
- `design-system/assets/reference-page/*.png` — Reference exports.

## Deploy + verify workflow
1. Edit on `main`, commit, push.
2. Copy `design-system/` to `gh-pages` (tmp dir copy), commit, push, switch back to `main`.
3. Poll live until `id="source-map"` appears (GitHub Pages cache lag ~30-60s).
4. Browser-verify: 9 sections, 0 broken images, exactly 1 `hero-visual` card, exactly 1 `Hero implementation pattern`, no `id="assets"`/`id="reference-page"`/`id="provenance"`.

## Known tooling gotchas this session
- `terminal` interrupted repeatedly on simple `python3 -c`/heredoc; use `execute_code` (Python) or `read_file`/`search_files` instead.
- `patch` tool reported the canonical file path as "not found" intermittently; recover by re-reading via file tools, then patch.
- `browser_vision` rejects full-page screenshots (>8000px tall); crop the captured screenshot with PIL (`browser_screenshot_*.png`) and run `vision_analyze` on the crop.

## Canonical skill reference
`aleron-md-canonical-repo-location` → `references/lowercase-design-system-reference.md` is updated to match all of the above (page order, hero visual-only rule, verification checklist). Load it first next session.
