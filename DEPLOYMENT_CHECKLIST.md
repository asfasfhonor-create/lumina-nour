# LUMINA — Deployment & Release Checklist

Status: pre-release development branch

## Required server-side secrets

Configure only in Streamlit secrets. Never commit real values.

- `GEMINI_API_KEY` — AI features.
- `NOUR_APP_PIN` — optional whole-app PIN.
- `PARENT_PIN` — optional Parent Dashboard PIN.
- `NEON_DATABASE_URL` — pooled Neon PostgreSQL connection string for the dedicated LUMINA NOUR database.
- `NOUR_LEARNER_KEY` — stable internal learner key for Nour.

The Neon connection string must remain server-side and use SSL. Prefer the pooled connection string from Neon for hosted app traffic.

## Database activation

1. Create a dedicated **LUMINA NOUR** Neon project on the Free plan. Do not reuse PROJECT LEDGER databases.
2. Apply `neon/lumina_schema.sql` once in the Neon SQL editor.
3. Copy the **pooled** PostgreSQL connection string with SSL enabled.
4. Add `NEON_DATABASE_URL` and `NOUR_LEARNER_KEY` to Streamlit secrets.
5. Launch the app and verify that attempts, mistakes, reviews, XP, streak, badges, and English profile survive a fresh browser session.
6. Export a portable backup from Parent Dashboard and verify that it contains remote learning evidence but no secrets.

## Curriculum checks

- English Term 1 source-backed.
- Science Term 1 + Term 2 source-backed from the supplied combined PDF.
- Math Term 1 + Term 2 source-backed from the supplied combined PDF.
- Arabic Term 1 source-backed.
- Social Studies Term 1 source-backed.
- Religion Term 1 source-backed.
- ICT supplied Second Semester source-backed.
- Missing terms are never invented.

## Functional smoke test

- Home loads on mobile width.
- Nour real photo displays correctly.
- Every enabled school-subject card opens.
- Back-to-home works from every world.
- Daily Mission opens a mapped lesson.
- Weekly Plan renders.
- Exam Mode records correct/incorrect evidence.
- Mistake Notebook receives incorrect checks.
- Correct retry resolves the linked mistake/review.
- XP is awarded once per new evidence item only.
- Streak reflects learning days only.
- Parent Dashboard requires its PIN when configured.
- Whole-app PIN blocks entry when configured.
- Real English baseline stores profile.
- Curriculum Search finds examples in English and Arabic and grounds AI answers to mapped evidence.
- Gemini provider failure does not crash the app.
- Neon disconnect/failure is surfaced without exposing credentials.
- Fresh browser session restores durable learner profile and history from Neon.

## Release gates

Do not merge the development PR until:

- GitHub Quality workflow is green on the exact candidate commit.
- Dedicated Neon persistence is activated and verified, or explicitly deferred for a prototype release.
- Mobile/live UI smoke testing is complete.
- No secret values appear in GitHub.
- Source coverage labels match the actual supplied files.
- User approves the final merge.
