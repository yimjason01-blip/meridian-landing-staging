# Member doctor video visual swapped to consult reference

Date: 2026-06-02
Agent: Hermes
Repo: meridian-landing
Branch: main
Base SHA: 80ad7a6
Final SHA or patch status: committed on main; see current HEAD

## Goal

Respond to Jason's correction that the doctor image still did not use the previous Aleron landing reference. Use the more realistic image of a white physician speaking with an Asian male patient in picture-in-picture.

## Files changed

- `assets/video/source_refs/doctor-video-consult-with-patient-reference.jpg`: saved the cropped source reference from `assets/patient-prototype-current.png`.
- `assets/video/doctor-initial-assessment-poster.jpg`: regenerated as a 16:9 poster with the consult reference centered over blurred side fill.
- `assets/video/doctor-initial-assessment.mp4`: rebuilt as a static consult-reference visual with the existing physician-readout audio.
- `member.html`: updated the video/poster cache-bust query to `member-consult-ref-20260602`.

## Behavior changed

The Strategy tab video now shows the previous landing page's realistic telehealth visual: white male physician in a lab coat speaking, with an Asian male patient in the bottom-right picture-in-picture window. It no longer shows the solo AI-looking physician portrait.

## Verification

- Local poster vision check confirmed the white physician plus Asian male PIP are visible.
- HTML parsed successfully.
- Inline JavaScript passed `node --check`.
- Changed HTML has zero em dashes and zero en dashes.
- Video has both H.264 video and AAC audio streams, duration 66.5 seconds.

## Open risks or follow-up

The visual is still a static poster/video frame sourced from the previous landing page screenshot, not newly recorded footage. It is more realistic and reference-faithful, but production should eventually use real physician media.
