# LUMINA NOUR — V1 RELEASE AUDIT

**Date:** 2026-09-30  
**Branch:** `feature/nour-mobile-ui`  
**PR:** #1 — must remain Draft until Mohamed gives explicit merge approval.  
**Build label:** `RC-2026.09.30-B`

## Executive result

LUMINA has completed the code-side V1 quality audit. The remaining gates are live deployed-UI checks that cannot be proven from repository/CI alone.

## Verified production data

Six El-Moasser supplementary PDFs are registered for learner `nour` in `lumina_trusted_sources` and exist as non-empty objects in the private `lumina-trusted-sources` bucket:

1. English Guide Answers — correction reference only.
2. Maths Main Book — explanation/practice.
3. Maths Assessments & Final Revision — practice/revision.
4. Maths Guide Answers — correction reference only.
5. Science Main Book — explanation/practice.
6. Science Notebook — review/exam practice.

Official curriculum sources remain higher priority than supplementary sources.

## Learning-engine QA

Verified by automated tests:

- gentle start → building → light challenge progression;
- unresolved mistakes force a step-down/review state;
- one-question-at-a-time learner flow;
- progressive support after wrong attempts;
- question cognitive-load constraints;
- full transaction: incorrect Science answer → mistake + review queue → correct retry → XP;
- repeated review evidence cannot falsely inflate mastery;
- Exam Mode defaults to gentle practice with optional higher levels.

## Supplementary-source QA

Verified contracts:

- Main Book may explain and provide supported practice;
- assessment/revision sources are preferred for extra practice;
- Answer Guides are learner-hidden;
- generated practice must contain exactly three options, hint, explanation, and a valid correct index;
- supplementary prompts explicitly preserve Ministry curriculum authority;
- missing/unsupported source coverage must not be guessed.

## AI Literacy QA

Hands-on activities now include:

- Fix the Prompt;
- Compare Two AI Answers;
- Verify With Evidence;
- Write a Prompt;
- AI Detective;
- Verification Plan.

Successful AI activities produce durable skill evidence for prompting, comparison, evidence quality, verification, and uncertainty handling.

## Real English QA

Verified:

- separate School English and Real English tracks;
- baseline skill snapshot;
- skill-level scores;
- adaptive Arabic/English support;
- Reading Detective;
- writing, conversation, and vocabulary activities;
- recommended next focus from observed weakest skill;
- parent dashboard visibility;
- actual Reading/Writing/Conversation/Vocabulary activity evidence is persisted separately from the initial baseline, avoiding false claims that an AI-generated coaching response is automatically a correct proficiency score.

## Mobile / UX / privacy QA

Automated guards verify:

- phone breakpoint at 640px;
- reduced portrait size and padding on mobile;
- touch-friendly button height;
- Streamlit learner-facing toolbar hidden;
- no committed secrets;
- large curriculum PDF limit raised to 500 MB;
- permanent-source UI clearly distinguishes selected files from saved files;
- save confirmation survives Streamlit rerun;
- partial upload failures remain visible after rerun;
- Parent Dashboard includes a lightweight object-size integrity check for all saved source files;
- learning backup/restore includes AI profile and daily-mission profile state.

## Remaining live gates

Before merging to `main`:

1. Confirm Streamlit is serving the exact latest feature-branch candidate.
2. In the deployed app, open a Science or Maths lesson and trigger one saved-PDF action such as **فهمهالي أبسط** or **هاتلي تحدّي مناسب**.
3. Confirm the returned content is relevant to that lesson and displays the supplementary source label.
4. Perform one final phone-width visual smoke.
5. If optional PIN controls are enabled, verify them.
6. Mohamed gives explicit merge approval.

## Merge rule

Do **not** merge PR #1 automatically. Passing this audit does not replace explicit Mohamed approval.
