# Member Strategy doctor video

Date: 2026-05-22
Agent: Hermes
Repo: meridian-landing
Branch: main
Base SHA: 7ab8118
Final SHA or patch status: committed; see current HEAD

## Goal

Add a believable playable doctor video to the Strategy section of the member portal, placed above the existing written summary.

## Files changed

- `member.html`: added the Strategy video card, native video player, doctor attribution, and a small hidden-state fix for the risk bottom sheet so it does not obscure the Strategy summary on load.
- `assets/video/doctor-initial-assessment.mp4`: playable 1:07 physician assessment video with audio.
- `assets/video/doctor-initial-assessment-poster.jpg`: poster frame for the video player.

## Behavior changed

The Strategy tab now opens with a Dr. Thompson initial assessment video. The existing two-paragraph summary remains directly below the video. The video has native controls and plays with audio.

## Verification

- Verified video asset has H.264 video and AAC audio via `ffprobe`.
- Verified `member.html` contains the video before `.plan-status`.
- Verified new Strategy block contains no em dashes.
- Opened `member.html` locally at `http://127.0.0.1:8765/member.html?dev=3`.
- Clicked the video play control and confirmed `paused: false`, `currentTime` advanced, `duration: 67.4`, and no media error.
- Visual verification confirmed the doctor card appears first and the written summary is unobscured below.

## Open risks or follow-up

The doctor face and voice are prototype media, not an actual recorded clinician. Replace with real physician footage before a production patient launch.
