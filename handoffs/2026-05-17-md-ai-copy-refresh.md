# MD AI copy refresh

## Goal

Update the Aleron MD x AI landing section so the four icon cards map directly to the intended ideas:

1. Genetics
2. Labs
3. Wearable data
4. Data privacy

Also replace the verbose MD x AI paragraph with shorter physician-led copy.

## Files changed

- `index.html`
- `v2.html`

## Behavior changed

- The MD x AI lead paragraph is now a shorter three-sentence message:
  - genetics, labs, wearables, and history should not be siloed
  - Aleron creates one physician-led view with AI support
  - the output is a clearer next step
- The icon cards now match their icon themes and lead with Genetics.
- `v2.html` MD x AI grid spacing now matches `index.html` with more breathing room.

## Verification commands

```bash
grep -n '—\|–' index.html v2.html | head -40
```

Result: remaining dash characters are in comments only, not user-visible prose.

```bash
git diff -- index.html v2.html
```

Result: reviewed changed copy and spacing only.

## Open risks

- Data privacy language says data is never sold, never shared with insurers, and never used to train outside models. Legal/privacy policy should confirm this before public launch.
- This does not promote `v2.html` over `index.html`; both were updated in place.
