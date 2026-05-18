# Aleron MD Marketing Design System v1

Date: 2026-05-17
Status: Baseline for future marketing exploration
Source: `landing/v2.html`

## Purpose

This v1 design system plants a clear flag for Aleron MD marketing work. It is not a full component library yet. It captures the current brand direction, tokens, and reusable patterns so future landing, campaign, and prototype work does not drift into unrelated visual languages.

Use this system for public and member-facing marketing surfaces. Do not apply it to physician clinical surfaces, which currently follow the physician design system.

## Research Model

This v1 follows the pattern used by mature brand and design systems:

- Strategy: why the brand exists, who it is for, and what it must make people feel.
- Foundations: color, type, spacing, grid, motion, imagery, and accessibility.
- Expression: photography, proof modules, copy patterns, section rhythm, and example layouts.
- Components: reusable buttons, nav, hero, proof, CTA, and content modules.
- Content: voice, tone, claim discipline, grammar rules, and approved phrases.
- Governance: do/don't examples, drift checks, and when to add new patterns.

References reviewed:

- Dropbox Brand Guidelines: https://www.dropboxbrand.com/
- Atlassian Design System Foundations: https://atlassian.design/foundations/
- IBM Design Language Color: https://www.ibm.com/design/language/color/
- Mailchimp Content Style Guide, Voice and Tone: https://styleguide.mailchimp.com/voice-and-tone/
- Apple Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines
- Shopify Polaris color and typography tokens: https://polaris-react.shopify.com/design/colors/color-tokens

Main takeaway: strong systems are not just galleries. They explain the decision logic behind the work, provide reusable assets and tokens, show correct and incorrect usage, and define how the system grows.

## Brand Direction

Aleron MD is premium preventive medicine with a human, cinematic, physician-led posture.

The brand should feel:

- Warm, quiet, and high-trust.
- Physician-led before technology-led.
- Emotionally grounded in future capacity, autonomy, and meaningful life moments.
- Clinically credible without becoming a dashboard or generic AI healthcare product.
- Selective and high-touch, not loud luxury.

The brand should not feel:

- Biohacker, quantified-self, or supplement-adjacent.
- Generic concierge clinic marketing.
- SaaS, neon, gradient-heavy, or dashboard-first.
- Cold hospital system, insurance portal, or enterprise software.
- Overly optimized around longevity claims.

## Naming And Voice

- Use `Aleron MD` for current product-facing work.
- Use `Meridian` only for historical context, unchanged legacy routes, or legal/company references already approved.
- Prefer direct, premium, physician-led language.
- Avoid generic longevity claims.
- Avoid marketing filler that could fit any concierge clinic.
- Keep medical claims grounded. If citing a clinical value, include the unit every time.
- Do not use em dashes in user-facing prose.
- Do not use rounded-pill eyebrow tags above headlines.

## Core Promise

Aleron MD preserves future capacity by combining physician judgment, complete personal data, and AI-assisted prevention.

The strongest framing is future availability:

- More of life remains open.
- Better decisions happen earlier.
- Risk, capacity, and vitality are reviewed together.
- AI helps the physician hold the whole picture, but the physician remains the accountable center.

## Visual Principles

1. Lead with human consequence.
   Use cinematic images of real-feeling life moments before abstract interfaces or charts.

2. Keep the surface restrained.
   The default palette is warm paper, cool rain-dark ink, warm ink, bone, and gold. Avoid extra accent colors unless they are part of photography.

3. Use clinical proof as support.
   Evidence sections should substantiate the story. They should not become the dominant first impression.

4. Preserve spacious editorial rhythm.
   Marketing pages should use large section spacing, strong typographic hierarchy, and clear narrative progression.

5. Let gold behave as warmth, not decoration.
   Gold is for emphasis, signal, section cues, and selected states. It should not become confetti.

6. Avoid visual over-systemization.
   This is not a SaaS shell. Cards, grids, and stats are allowed only when they clarify a specific claim or experience.

7. Show the decision, not just the decoration.
   A design system should teach why a layout is right. Every future showcase example should include intent, anatomy, and drift risks.

8. Keep accessibility explicit.
   Hero overlays, gold text, and dark proof sections must be checked for readable contrast. The premium feel cannot come at the expense of legibility.

## Tokens

Canonical v1 CSS tokens live in:

- `landing/design-system/tokens.css`

Use the `--amd-*` variables for new marketing CSS. The values are extracted from `landing/v2.html` and normalized for reuse.

Primary color roles:

- `--amd-ink`: cool black for rain hero and cold cinematic sections.
- `--amd-ink-warm`: warm black for premium dark sections.
- `--amd-paper`: default warm off-white surface.
- `--amd-paper-warm`: warm editorial section surface.
- `--amd-bone`: slightly cooler clinical/member surface.
- `--amd-gold`, `--amd-gold-light`, `--amd-gold-deep`: emphasis, highlight, and signal.
- `--amd-text`, `--amd-text-muted`: primary and secondary text on light surfaces.

Core type roles:

- Display: `Inter Tight`, weight 500, tight but not brittle.
- Body: `Inter`, regular to medium.
- Editorial quote: `Source Serif 4`, italic.
- Human warmth emphasis: `Cormorant Garamond`, italic, used sparingly.
- Data or small technical labels: `JetBrains Mono`, only where useful.

## System Anatomy

The marketing system should be documented in four visible layers:

1. Brand board.
   A fast visual page for Jason, Hermes, Codex, and future collaborators to understand the brand's shape.

2. Foundations.
   Reusable CSS tokens, type roles, spacing, section surfaces, and motion values.

3. Module specimens.
   Real examples of hero, proof, CTA, narrative, image, and section treatments with usage guidance.

4. Drift checks.
   Side-by-side examples of what belongs and what does not. This is the fastest way to prevent visual drift.

## Reusable CSS

Baseline CSS lives in:

- `landing/design-system/base.css`
- `landing/design-system/components.css`

These files are not wired into production pages yet. They are the v1 extraction target for future work.

Use these class prefixes for new marketing surfaces:

- `amd-container`
- `amd-display`, `amd-h1`, `amd-h2`, `amd-h3`
- `amd-lede`, `amd-body-lg`, `amd-eyebrow`
- `amd-section`, `amd-section-dark`, `amd-section-warm`, `amd-section-bone`
- `amd-nav`, `amd-nav-brand`, `amd-nav-link`
- `amd-button`, `amd-button-primary`, `amd-button-ghost-dark`
- `amd-hero`, `amd-hero-media`, `amd-hero-content`

## Canonical Patterns

### Hero

Use a full-bleed cinematic image or video. Text sits over the media, not inside a card. The hero should signal Aleron MD in the first viewport and hint at what comes next.

Current canonical hero qualities:

- Dark cinematic overlay.
- Human moment, not abstract health imagery.
- Direct headline about future capacity.
- One primary CTA and one secondary CTA.
- Minimal nav.

Hero anatomy:

- Full-bleed image or video.
- Dark overlay only when needed for contrast.
- One direct headline with a human outcome.
- One lede that states the physician-led mechanism.
- One primary action, one optional secondary action.
- No badge, pill, or decorative eyebrow above the headline.

### Sections

Use full-width bands rather than floating page cards.

Approved section modes:

- Light paper editorial section.
- Warm paper narrative section.
- Bone clinical/member section.
- Warm dark proof or emotional section.
- Cool dark cinematic transition.

### Buttons

Primary buttons are quiet, rounded, and clear. Secondary buttons can use a translucent dark treatment on media.

Do not create busy CTA clusters. Most sections should have zero or one action.

### Eyebrows

Use text-only uppercase labels. Do not place them inside pill shapes.

### Proof

Use evidence to support the reroute idea. Keep units explicit. Do not overstate causality.

Preferred structure:

- One plain-language claim.
- A small number of driver examples.
- A clear note that overlapping drivers are not additive.
- Source naming short enough to scan.

Proof anatomy:

- Plain-language claim.
- One primary number or small set of drivers.
- Driver explanation in human language.
- Source posture or source family.
- Boundary note when drivers overlap, model outputs are illustrative, or clinical behavior is not yet verified.

### Imagery

Preferred imagery:

- Rain, natural light, family, motion, travel, care team, lab moments, home moments.
- Real-feeling people and specific environments.
- Product images only when they clarify the care loop.

Avoid:

- Generic smiling stock portraits.
- Sterile hospital hallway imagery.
- Abstract AI brains, glowing networks, generic DNA spirals.
- Overly aspirational luxury cues disconnected from care.

Image anatomy:

- Real-feeling person, care moment, or future-capacity moment.
- Natural light or cinematic contrast.
- Room for typography.
- No generic doctor handshake, abstract AI network, supplement imagery, or glossy tech dashboard hero.

## Content And Claims

Voice:

- Direct.
- Physician-led.
- Calmly premium.
- Specific.
- Human before technical.

Tone can shift by context:

- Hero: emotionally direct, short, future-oriented.
- Proof: precise, sourced, bounded.
- Application: selective, respectful, low-pressure.
- Clinical value: sober, no hype.

Claim rules:

- Every clinical value needs its unit.
- Composite claims must explain whether drivers overlap.
- Avoid implying diagnosis, guaranteed prevention, or model certainty.
- Use AI as assistance to physician judgment, not as autonomous care.
- Use "Aleron MD" for current product-facing work.

## Relationship To Current Files

Current source pages:

- `landing/v2.html`: intended future root candidate and source for this v1 system.
- `landing/index.html`: current root entry until Jason explicitly approves promotion.

Prototype reference areas:

- `landing/prototypes/experience/`
- `landing/prototypes/trajectory/`
- `landing/prototypes/engine/`

The prototype folders are useful exploration references, not canonical system files. New production work should start from this design system and `landing/v2.html`.

## Governance

Add a new marketing pattern only when at least one of these is true:

- The pattern appears in an approved Aleron MD surface.
- The pattern is needed by two or more planned surfaces.
- The pattern solves a recurring content or layout problem better than existing modules.
- Jason explicitly approves it as a new direction.

Before adding a new pattern, check:

- Does it still feel physician-led?
- Does it preserve the warm, quiet, premium palette?
- Does it avoid SaaS gradients, neon accents, and dashboard-first language?
- Does it explain the clinical or human consequence clearly?
- Does it fit the current token set without inventing unnecessary colors or type styles?

## Next Steps

1. Use this v1 system as the baseline for new marketing exploration.
2. When the landing deploy plan starts, decide whether to wire these CSS files into `v2.html`.
3. Expand the HTML board with annotated approved and rejected examples as new surfaces are explored.
4. Build a small section inventory only after one more page or campaign surface needs reuse.
5. Keep this system small until repeated patterns justify more structure.
