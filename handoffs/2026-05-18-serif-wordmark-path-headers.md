# Serif wordmark and path headers

Date: 2026-05-18
Agent: Hermes
Repo: meridian-landing
Branch: main
Base SHA: a6e751ea3df5db200b1dbff7ec69a034f87402eb
Final SHA or patch status: pending commit

## Goal

Apply the new Aleron MD wordmark direction to page header surfaces and the path section.

## Files changed

- `index.html`: changed nav brand, path card headers, and footer brand to Source Serif 4 with italic MD.
- `v2.html`: same changes as `index.html`.

## Behavior changed

- Aleron MD brand text now reads as a serif roman Aleron with italic serif MD.
- The two path card headers use the same editorial serif voice.
- Existing landing structure and links are unchanged.

## Verification

- `git diff --check`: clean.
- Added-line em dash scan: clean.
- Local browser check at `http://localhost:8766/v2.html#apply`: computed nav, MD, path card, and footer font styles verified.

## Open risks or follow-up

- The source screenshot may imply an even more Garamond-like face than Source Serif 4. Current choice uses an already-loaded site font to avoid adding another dependency.
