# Figma hero carousel — current state and open items

Date: 2026-05-31
Agent: Hermes
Repo: meridian-landing (remote: yimjason01-blip/meridian-landing-staging)
Branch: main
Base SHA: d13e454
Final SHA: 7093879 (main), 29988b8 (gh-pages)

## What this file is

A cold-start handoff for the layered Figma hero carousel (`figma-hero-shot.html`). It captures the
current shipped state, the architecture, and the open follow-ups so a new session can resume without
re-deriving context.

## Live URL

https://yimjason01-blip.github.io/meridian-landing-staging/figma-hero-shot.html

Build signature currently live: `live-polish-20260531-header-login-only`

## Canonical file

`figma-hero-shot.html` — single self-contained HTML file (inline CSS + JS). 1728x968 desktop canvas.

Note: this is NOT `index.html` or `v2.html`. Per AGENTS.md, `v2.html` is the higher-fidelity landing
candidate and `index.html` is the root entry. `figma-hero-shot.html` is the layered-hero work surface.
Do not promote/sync into index or v2 without an explicit task.

## Hero architecture (five-plane carousel)

Four slides, each built from five depth planes (z-index order):

1. Background photo plane (z1)
2. Midground moving blocks plane (z2)
3. Subject cutout plane (z3) — person
4. Foreground anchored blocks plane (z4)
5. Chrome / DOM (z5+) — logo, headline, CTAs, carousel dots

Assets live in `assets/figma-five-plane-test/hero0{1-4}-*.png`.

Hard rules:
- Background plane and subject cutout plane MUST share the same `--slide-image-shift` transform
  (both `translate3d(var(--slide-image-shift), 0, 0)`). A mismatched parallax factor caused photo
  drift earlier.
- Anchored foreground blocks are z4 (above subject, below chrome).
- Figma boolean/group exports can clip children outside the bounding box. Always verify a full-frame
  pixel diff against the Figma reference, not just the exported node. (Slide 3 was missing two motion
  blocks for exactly this reason; fixed by exporting child nodes separately and compositing.)

## Current shipped interaction state

- Hero entrance animation (staggered fade/rise on logo, headline, subheadline, CTAs).
- Carousel: dots + keyboard + swipe. NO arrows (Jason found them too busy — keep them removed).
- Slide count micro-animation (001 / 004).
- Curve section: IntersectionObserver draw-on reveal.
- Partner modal (employer/broker/employee preview), opens from `#partners`, closes on backdrop/Escape.
- Sticky header: fixed logo top-left, fixed `Log in` top-right; a slim translucent dark bar fades in
  after `window.scrollY > 24`.

## Header CTA decision (latest)

Top-right header is `Log in` ONLY. A paired `Log in` + `Apply` cluster in the corner read as a
segmented slider/tab and was rejected. The shared translucent dark container was removed too.

The hero CTA row still carries both real CTAs: `Apply →` (primary) and `For Employers →` (secondary,
routes to `#partners`). `For Employers` replaced `See a demo` to avoid implying consumer self-serve
software. Never use `Join`.

## Verification baseline (what "done" looks like)

Run before claiming any hero change is live:
- `data-build-signature` updated and visible in the live HTML
- top-right header reads `Log in` only
- hero row reads `Apply` + `For Employers`
- 0 broken images (`[...document.images].filter(i=>!i.complete||i.naturalWidth===0)`)
- 0 JS console errors
- 0 em dashes
- 0 carousel arrows
- bg and subject plane transforms match per slide

## Deploy procedure (two branches)

`meridian-landing-staging` serves the public page from `gh-pages`, not `main`. To ship:
1. Commit + push on `main`.
2. Copy the changed file to a temp dir.
3. `git checkout gh-pages` and `git reset --hard origin/gh-pages`.
4. Copy the changed file in, commit, push `gh-pages`.
5. `git checkout main`.
6. Verify the live URL with a cache-bust query and computed-style/DOM checks (GitHub Pages lags ~30-60s).

## Open risks / follow-ups (next session candidates)

1. Mobile CSS (full-canvas fit, 1728x968 aspect ratio, from commit 35e3e56) is NOT yet validated by
   Jason on a real device. The portrait-crop media query was replaced; this needs a real-device look.
2. Curve section had a dark horizontal band artifact observed during demo verification (likely a
   z-index overlap). Not yet addressed in the live page. Verify whether it persists.
3. Untracked working-dir cruft: `assets/figma-five-plane-test/runner-rerender-candidates/` holds
   rejected AI runner-image edits. Jason said leave the runner image as-is. These are not committed.
   Decide whether to delete or keep as scratch.
4. Runner (slide 3) subject image: Jason declined AI re-renders. Leave unchanged unless he re-asks.

## Source-of-truth pointers

- `AGENTS.md` — collaboration rules, writing/design rules.
- `PROJECT_STATE.md` — canonical file choices (note: predates the figma-hero work; reflects v2/index).
- Skill `aleron-md-canonical-repo-location` — repo location trap, deploy nuance, CTA conventions
  (`references/public-landing-cta-conventions.md`).
- Prior handoffs: `2026-05-30-figma-hero-five-plane-carousel.md`,
  `2026-05-30-figma-hero-slide3-motion-block-fix.md`, `2026-05-30-selected-surfer-frame-swap.md`.
