# Member doctor video recorded-message solo poster

Date: 2026-06-02
Agent: Hermes
Repo: meridian-landing
Branch: main
Base SHA: 49c4c09
Final SHA or patch status: committed on main; see current HEAD

## Goal

Correct the physician video model: this is a recorded physician message, not a live video call, so the patient should not appear in the poster. Remove the Asian male/PIP and use a solo physician recorded-message frame.

## Files changed

- `assets/video/doctor-initial-assessment-poster.jpg`: replaced with a native 16:9 solo physician poster.
- `assets/video/doctor-initial-assessment.mp4`: rebuilt as a static-frame video using the new solo poster and existing audio.
- `assets/video/source_refs/doctor-video-recorded-solo-source.png`: saved original generated source asset.
- `assets/video/source_refs/doctor-video-recorded-solo-16x9.jpg`: saved selected 16:9 crop before 1280x720 poster resize.
- `member.html`: updated cache-bust stamp to `member-recorded-solo-20260602`.

## Behavior changed

The Strategy tab video now shows one realistic white physician only, framed as a recorded video message. There is no patient picture-in-picture and no second person.

## Verification

- Generated three solo physician candidates and vision-graded them.
- Selected candidate 3 because it scored highest for human recorded-video realism while preserving 16:9, stethoscope, no hands, no text/logo artifacts, and no PIP.
- Final poster vision check passed: one realistic white physician only, no Asian person, no PIP, native 16:9, no mobile screenshot/crop artifacts, no hands/text/logo artifacts.
- `member.html` parsed with Python HTMLParser.
- Inline JS passed `node --check`.
- Changed HTML contains cache-bust `member-recorded-solo-20260602` and no stale `member-rerender-gradea-20260602`.
- Video has H.264 video and AAC audio streams, duration 66.5 seconds.

## Open risks or follow-up

Still prototype/generated media, not actual recorded clinician footage. Production should replace with real physician footage when available.
