# LUMINA — IMPLEMENTATION PLAN

> Execution plan derived from MASTER_REQUIREMENTS.md.
> Rule: curriculum-bound behavior is not finalized until Nour's current-year source files are available and inspected.

## Delivery strategy

Build a usable vertical slice first, then deepen intelligence and persistence without breaking existing working tools. Keep production/main protected until review and testing.

## Phase 0 — Current foundation

Status: in progress on `feature/nour-mobile-ui`.

Already represented in the development branch:
- Mobile-first Nour's World home.
- Daily Mission demo with XP/level.
- Seven subject entry cards.
- Existing PDF, AI Buddy, problem image, English, Escape Room, Python, and goals tools preserved.
- Curriculum-grounding instructions improved where a PDF is supplied.
- MASTER_REQUIREMENTS.md established as product source of truth.

Known temporary limitations:
- XP, streak, tasks, chat, and mission completion are session-only.
- Subject cards are placeholders.
- AI Explorer is a placeholder.
- PDF processing still sends the whole uploaded file to Gemini.
- No persistent curriculum knowledge base yet.
- No persistent mastery/mistake profile yet.

## Phase 1 — App structure and reliable navigation

Goal: turn the prototype into a maintainable app shell without changing curriculum content.

Deliverables:
- Separate home, subject, quick-tools, AI Lab, and parent-facing navigation concepts.
- Reusable UI components/helpers instead of one growing monolithic screen.
- Consistent back navigation.
- Mobile-first behavior retained.
- Existing working features preserved during refactor.

Acceptance:
- App starts without syntax/import errors.
- Every existing tool remains reachable.
- No Gemini/API secret is committed.
- No curriculum claims are hardcoded from memory.

## Phase 2 — Curriculum ingestion and map

Blocked until the complete current-year curriculum source set is visible.

Deliverables after source inspection:
- Inventory by subject, term, unit, lesson, source, and page/range where available.
- Curriculum map based only on supplied/current verified materials.
- Retrieval strategy that sends only relevant source chunks/pages to the tutor.
- Source references shown with curriculum answers.
- Clear separation between curriculum content and optional enrichment.

Acceptance:
- A curriculum answer can identify the source used.
- Missing source information is reported instead of invented.
- Retrieval is tested across all available subjects.

## Phase 3 — Persistent learning brain

Goal: remember Nour's learning rather than resetting each session.

Data to persist:
- Profile/settings.
- XP, level, streak, badges.
- Mission attempts and completion.
- Subject/unit/lesson/concept mastery.
- Mistakes and diagnosed mistake type.
- Review queue/spaced repetition.
- Tutor adaptation signals.
- Goals/tasks and useful activity history.

Architecture rule:
Choose the simplest reliable low-cost persistence option after reviewing the actual deployment constraints. Supabase is a candidate, not an automatic dependency.

Acceptance:
- Closing/reopening the app does not lose progress.
- A repeated mistake can reappear later as a review task.
- Mastery changes only from meaningful evidence, not button clicks.

## Phase 4 — Core learning modes

Build:
- Teach Me.
- Homework Coach with progressive hints.
- Exam Mode.
- Adaptive practice.
- Mistake Notebook.
- Spaced Review.
- Weekly Smart Plan.

Acceptance:
- Default flow does not reveal final answers immediately.
- Wrong answers generate useful diagnosis and a retry/hint.
- Difficulty can adapt from demonstrated performance.
- Exam questions are grounded in the mapped curriculum.

## Phase 5 — English Adventure

Build progressive skills:
Vocabulary → Grammar → Reading → Writing → Listening → Speaking → Pronunciation.

Behavior:
- Arabic support when useful.
- Assistance gradually reduces.
- Practical language and short challenges.
- Track skill-specific mastery.

Voice/listening/pronunciation are added only after the text learning loop is stable.

## Phase 6 — AI Lab

Goal: teach Nour to think with AI, not copy from it.

Progression:
- What AI can/cannot do.
- Better prompts.
- AI Detective: spot weak/incorrect answers.
- Fact checking and source awareness.
- Compare outputs.
- Study/research/summarization workflows.
- Creative Builder.
- Later: AI + Python projects.

Meaningful badges can be attached to demonstrated skills.

## Phase 7 — Engagement layer

Wrap real learning in:
- Missions.
- Mysteries.
- Quests.
- Stories.
- Creation challenges.
- Achievement feedback.

No infinite scroll or empty reward loops. XP/badges must reflect learning actions.

## Phase 8 — Parent dashboard

Provide a concise parent view:
- What Nour studied.
- Mastery movement.
- Recurring weak concepts.
- Review due.
- English progress.
- AI skill progress.
- Suggested next focus.

Keep it separate from Nour's playful main experience.

## Phase 9 — Hardening and release

Test:
- Mobile layout.
- Navigation and state.
- Gemini unavailable/missing key/error paths.
- File/image upload paths.
- Curriculum grounding.
- Persistence.
- Duplicate XP/reward prevention.
- Secret leakage.
- Regression of original features.

Release rule:
Do not merge the development branch to main until the tested build is explicitly approved.

## Immediate next actions

While curriculum uploads are incomplete:
1. Stabilize/refactor the app shell and navigation.
2. Keep curriculum-specific placeholders neutral.
3. Prepare persistence/data model without binding to unverified curriculum details.
4. Run syntax/static checks on every code change.
5. Re-check Project Sources periodically.

As soon as the complete curriculum set is visible:
1. Freeze a source inventory.
2. Build the curriculum map.
3. Choose retrieval/chunking based on the real files.
4. Implement the first complete vertical slice: one subject lesson → tutor → attempt → mistake/mastery → review.
5. Generalize that proven flow across subjects.
