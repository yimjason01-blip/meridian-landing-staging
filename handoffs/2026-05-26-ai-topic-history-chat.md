# Aleron AI topic-history chat

Date: 2026-05-26
Agent: Hermes
Repo: meridian-landing-staging
Branch: main
Base SHA: b43b4d2
Final SHA or patch status: 8267fb7

## Goal

Replace the Aleron AI chat architecture with the familiar LLM pattern: a left-side topic history and a selected chat on the right. Clicking a plan card's AI button should create a new AI chat topic instead of reusing a generic surface.

## Files changed

- `member.html`: Reworked the Aleron AI subtab into a two-column chat shell with a dark History rail, active thread pane, and per-topic history rendering. Updated AI thread creation so each plan-card AI CTA starts a new topic-scoped thread.

## Behavior changed

- Connect → Aleron AI now shows a dark left History rail with topic rows and snippets.
- The selected topic renders on the right with context, messages, suggestions, and the shared input.
- The History rail has a `+` button to start a blank AI chat.
- Clicking `Ask Aleron AI about this →` from a plan card starts a new thread for that card, selects it in History, and pre-fills the input with the card-scoped starter.

## Verification

- Parsed the inline script with `new Function(...)`; result: ok.
- Confirmed `member.html` contains zero em dashes.
- Local browser verification on `http://127.0.0.1:8891/member.html`:
  - Clicking CAC Scan → `Ask Aleron AI about this →` opens Connect → Aleron AI.
  - History rail shows CAC Scan as the active topic plus Current plan.
  - Input is prefilled with `I have a question about the CAC Scan: `.
  - `+` starts a new blank AI chat.
  - Browser console showed no JavaScript errors.

## Open risks or follow-up

- This is still a static prototype. Thread state is in-memory only and resets on page reload.
