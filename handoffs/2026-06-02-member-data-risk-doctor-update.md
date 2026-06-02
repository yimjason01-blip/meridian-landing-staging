# Member data, risk, and doctor video update

Date: 2026-06-02 08:47 PDT
Agent: Hermes
Repo: meridian-landing
Branch: main
Base SHA: 55ccc13
Final SHA or patch status: committed on main; see current HEAD after this metadata amend

## Goal

Tighten the member-facing application after Jason's review:

- Replace the AI-looking doctor video visual with the less synthetic prior doctor portrait while preserving the strategy audio.
- Expand the Your Data tab so labs and wearable data feel like a real prevention intake rather than a sparse demo.
- Show all five model domains and make each risk model output use the same patient-facing category language.
- Correct the cardiovascular model framing so Lp(a) 72 nmol/L is treated as optimal and the CVD output reads low.

## Files changed

- `member.html`: expanded wearable/lab/genetic data display, added local CKD domain token, added risk chips, replaced four-model risk section with five domains, updated AI chat canned responses and risk bottom sheets.
- `assets/video/doctor-initial-assessment.mp4`: rebuilt the physician message video with a static frame from `assets/video/source_refs/doctor-photo-clean-540x394.jpg` and the original audio track.
- `assets/video/doctor-initial-assessment-poster.jpg`: regenerated from the new doctor video frame.

## Behavior changed

- Plan video now opens on the less AI-looking white doctor portrait.
- Your Data now includes richer wearable inputs: VO2 max, cardio fitness percentile, training minutes, Zone 2 time, workouts, HR recovery, RHR, HRV, sleep, respiratory rate, SpO2, steps, and active energy.
- Labs now include a fuller prevention panel across lipids, glycemic control, inflammation, kidney, liver, thyroid, nutrients, hormones, and CBC.
- Lp(a) is now shown as `72 nmol/L` with an `optimal` label.
- Risk tab now has five cards: Cardiovascular, Metabolic, Cancer, Kidney, Neuro & cognitive.
- Cardiovascular output now reads `Low`, with 10y ASCVD estimate `~2%`, Lp(a) 72 nmol/L optimal, VO2 max 54 mL/kg/min protective, and ApoB 88 mg/dL as watch.
- Cancer output now treats ATM as an elevated hereditary signal and notes pancreatic screening intensity depends on confirming family-history details.

## Verification

- Parsed `member.html` with Python `HTMLParser`: ok.
- Extracted inline `<script>` and ran `node --check`: ok.
- Searched changed HTML for em dash and en dash: zero.
- Verified old incorrect CVD/Lp(a) strings are gone: no `62 mg/dL`, no `9.4`, no `6.2`, no `Four risk models`.
- Local browser QA at `http://127.0.0.1:8891/member.html?local=1`:
  - Your Data renders expanded wearable/lab/genetic sections.
  - Risk tab renders five domain outputs.
  - Cardiovascular bottom sheet opens with corrected low-risk framing.
  - Browser console showed no JavaScript errors.
- Vision QA of local Plan tab video card: new doctor poster is visible and coherent.

## Open risks or follow-up

- The rebuilt physician video uses a static portrait with the original audio. This solves the AI-looking moving-video issue without generating a new speaking video, but it is not a live-action physician clip.
- The risk values are prototype display values, not a freshly run production engine output. They are aligned to the corrected Lp(a) 72 nmol/L interpretation and the current patient-facing model story.
