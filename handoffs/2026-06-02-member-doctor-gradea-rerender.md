# Member doctor video Grade-A rerender

Date: 2026-06-02
Agent: Hermes
Repo: meridian-landing
Branch: main
Base SHA: cb1a2e4
Final SHA or patch status: committed on main; see current HEAD

## Goal

Fix the lazy prior physician image execution. The previous attempt carved a mobile app screenshot into the video card. Jason rejected that as not Grade-A. Replace it with a native 16:9 re-rendered telehealth poster: realistic white physician as the main feed, Asian male patient in a proper picture-in-picture tile, no mobile-frame crop.

## Files changed

- `assets/video/doctor-initial-assessment-poster.jpg`: replaced with the selected native 16:9 re-render.
- `assets/video/doctor-initial-assessment.mp4`: rebuilt as a static-frame video using the new poster and the existing audio track.
- `assets/video/source_refs/doctor-video-rerender-gradea-source.png`: saved original generated source asset.
- `assets/video/source_refs/doctor-video-rerender-gradea-16x9.jpg`: saved selected final crop before 1280x720 poster resize.
- `member.html`: updated cache-bust stamp to `member-rerender-gradea-20260602`.

## Behavior changed

The Strategy tab video now uses a native widescreen telehealth poster rather than a carved-out mobile screenshot. It shows a realistic white physician with stethoscope in a modern clinic setting and an Asian male patient in a bottom-right PIP tile.

## Verification

- Generated multiple candidates and vision-graded them.
- Selected candidate 4 after targeted re-render because it had the strongest realism, doctor authority, stethoscope, no visible hands, no text artifacts, and native 16:9 framing.
- Vision check on final poster passed: native 16:9, no mobile/screenshot crop, realistic white physician, Asian male PIP, no hands/text/crop artifacts.
- `member.html` parsed with Python HTMLParser.
- Inline JS passed `node --check`.
- Changed HTML contains cache-bust `member-rerender-gradea-20260602` and no stale `member-consult-ref-20260602`.
- Video has H.264 video and AAC audio streams, duration 66.5 seconds.

## Open risks or follow-up

This is still AI-rendered prototype media, not real physician footage. It is a materially better execution than the screenshot crop, but true production should eventually use real clinician media.
