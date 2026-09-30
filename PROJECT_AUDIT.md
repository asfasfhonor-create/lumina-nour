# LUMINA / NOUR'S WORLD — PROJECT AUDIT

Status: pre-master audit
Date: 2026-09-29
Purpose: consolidate confirmed requirements, current implementation, source readiness, gaps, and conflicts before issuing the final project master.

## 1. Product identity and mission

LUMINA is Nour's personal learning world, not a generic homework-answer bot.

Primary outcomes:
- Master Nour's current Egyptian Third Preparatory curriculum.
- Improve Nour's English as a real language beyond the limits of Third Preparatory school English.
- Build practical, age-appropriate AI literacy and enjoyment of AI.
- Develop reasoning, problem solving, independent learning, verification, creativity, and confidence.
- Make useful learning attractive enough to compete with passive time-wasting content without copying harmful infinite-scroll or empty-reward mechanics.

## 2. Confirmed learner context

- Learner: Nour.
- School stage: Egyptian Third Preparatory.
- Language-school context: Science and Math materials are in English.
- The app should be mobile-first and feel personal to Nour.
- Nour's real photo is intended for the UI as a static personal visual; do not generate/replace her face for this purpose.

## 3. Curriculum source policy

Confirmed rule: curriculum first; AI explains and teaches.

The current-year source files are the primary authority for curriculum-bound teaching. The app must not silently substitute generic model knowledge for curriculum facts.

Current Project Sources now include:
- Arabic — first term.
- English — first term.
- Islamic Religion — first term.
- Social Studies — first term.
- Mathematics in English — student book.
- Science in English — student book.
- Computer/ICT — second semester.

There is also a duplicate/imported copy of the Computer/ICT PDF outside the Project-source copy.

Important source observations:
- The Religion book is structurally readable and contains explicit units, lessons, lesson objectives, activities, unit reviews, and a general term review.
- The Math file identifies itself as a Third Preparatory student book / first term and includes a 2025–2026 ministry curriculum-development cover, though some internal legacy printing text remains in the PDF.
- The Computer/ICT source identifies itself as Third Year Preparatory, Second Semester. Its index contains Data, Branching, Looping & Procedures, and Cyber bullying; internal credits include older revision history. The program must treat the supplied source as the source, not infer freshness from internal legacy dates alone.
- Some PDFs are image/scanned or not text-readable through the current file parser. Curriculum ingestion must therefore support page/image-aware extraction rather than assuming every PDF has clean selectable text.

No curriculum map should be invented from memory. It must be derived from the actual files.

## 4. English — two distinct tracks

### A. School English
- Grounded in Nour's school/current curriculum sources.
- Supports lessons, homework, review, exam preparation, vocabulary, grammar, reading, and writing as required by the school material.

### B. Real English / English Adventure
- Independent of the ceiling of Third Preparatory curriculum.
- Goal: improve Nour's actual English ability as a language.
- Start from her demonstrated level, not age/grade assumptions.
- Progress through practical Vocabulary, Grammar, Reading, Writing, Listening, Speaking, and Pronunciation.
- Use Arabic support when useful, then reduce assistance as competence improves.
- Include conversation, real-life situations, interactive stories, short writing, useful expressions, listening, speaking, pronunciation/shadowing, and daily challenges.
- Use a CEFR-like progression/assessment concept as a practical framework, while not reducing progress to a single label.
- School English and Real English must remain distinguishable in the product.

## 5. AI literacy — core pillar

AI is not merely the backend tutor. Learning AI is itself a major educational goal.

Nour should learn:
- What AI can and cannot do.
- How to ask better questions/prompts.
- How to inspect and improve prompts.
- How to verify answers rather than trust them automatically.
- Hallucination/error awareness.
- AI Detective / fact-checking habits.
- Comparing outputs.
- Using AI for study, research, summarization, files, and creativity.
- Creative Builder activities.
- Later, AI + Python projects.

Core principle:
Nour does not learn how to get answers from AI; she learns how to think with it, direct it, verify it, and use it to create something new.

No random AI PDFs are required merely to fill Sources. Specialized external AI learning sources should only be added if a real gap is identified.

## 6. Teaching behavior

Default learning loop:
Curiosity/mission → discover → understand → example → Nour tries → hint → retry → apply in a new context → quick check → record learning/mistake → review later.

Tutor rules:
- Understanding before memorization where possible.
- Do not reveal final answers immediately by default.
- Use progressive hints/scaffolding.
- Ask Nour to attempt.
- Diagnose why an answer is wrong.
- Adapt explanation style when she does not understand.
- Verify understanding after explanation.
- Use the original curriculum terminology for curriculum-bound teaching.
- Arabic explanation may support English curriculum terminology when useful.
- If memorization is genuinely required, make it meaningful and revisit it with spaced review.

Homework Coach:
- Start by asking how Nour thinks the problem should begin.
- Hint 1 → Hint 2 → explanation → full solution only when genuinely needed.

Teach Me:
- Explain simply.
- Check understanding.
- Try another explanation if needed.
- Confirm understanding through a small application.

## 7. Engagement philosophy

The UI should not feel like traditional direct teaching.

Use:
- Missions.
- Mysteries.
- Adventures.
- Quests.
- Stories.
- Puzzles.
- Creation challenges.
- Meaningful achievement.

Examples:
- Science Lab mystery.
- Math Quest.
- Social Studies detective/time travel.
- English story mission.
- AI Detective.

Every short interaction should end in a meaningful outcome: understanding, a new word, a solved problem, an AI skill, a creation, or demonstrated mastery.

Do not use infinite scroll or empty addictive reward loops.

## 8. Gamification

Planned:
- XP.
- Levels.
- Streak.
- Badges.
- Daily Mission.

Rules:
- Rewards must correspond to meaningful learning evidence.
- Progress must persist.
- Avoid granting mastery/XP solely because a button was clicked.
- Potential AI-skill badges include Prompt Explorer, AI Detective, Fact Checker, Creative Builder.

Current branch only contains demo/session-based XP/streak/level behavior. It is not yet real persistent gamification.

## 9. Mastery and adaptive learning

Required:
- Mastery Map by subject → unit → lesson → concept.
- States such as not started / learning / needs review / mastered.
- Mistake Notebook.
- Mistake classification: concept, application, question reading, inference, linking, calculation, English/language comprehension, careless error.
- Spaced repetition/review queue.
- Adaptive difficulty.
- Persistent Tutor Profile.
- Weekly Smart Plan.
- Curriculum progress tracking.

Mastery must be evidence-based.

## 10. Exam Mode

Required behavior:
- Choose subject/unit/scope, time, and difficulty where appropriate.
- Questions grounded in actual curriculum sources.
- Assess understanding/application rather than rote recall where the curriculum supports it.
- Grade/analyze.
- Identify weak concepts and mistake patterns.
- Route weak areas into review/mastery system.

The exact exam style should be aligned to current verified curriculum/assessment evidence rather than assumed from older patterns.

## 11. Uploads and future materials

The app should retain a permanent upload capability so future PDFs, school notes, worksheets, and problem images can be used.

The design should distinguish:
- Temporary use: ask/study this file now.
- Permanent learning source: intentionally add/index a trusted material into the knowledge base.

A future upload must not silently become authoritative curriculum content without classification.

## 12. Curriculum knowledge architecture

Target hierarchy:
Subject → Term → Unit → Lesson → Concept/Source/Page.

Requirements:
- Retrieve relevant pages/chunks rather than repeatedly sending whole books.
- Preserve source provenance.
- Show useful source references in curriculum answers where feasible.
- Clearly distinguish curriculum-grounded answers from optional enrichment.
- Handle scanned/image-heavy PDFs.
- Do not build a vector database merely because it is fashionable; use the simplest reliable retrieval approach that works for the real files.

## 13. Subjects

Confirmed seven subject areas:
- English.
- Science.
- Math.
- Arabic.
- Social Studies.
- Islamic Religion.
- ICT/Computer.

The product can use engaging names such as English Adventure, Science Lab, Math Quest, Arabic World, Religion Journey, ICT Lab, while keeping curriculum identity clear.

## 14. UI/UX

Confirmed direction:
- Mobile first.
- Nour's World.
- Dreamy/premium dark navy-purple visual language with warm pink/lavender/blue accents.
- Rounded/glowing cards and low clutter.
- Clear typography.
- English visually prominent.
- Nour's real photo as a personal avatar/welcome element.
- Subject worlds plus a separate Quick Access area.
- Persistent/clear back navigation such as العودة إلى عالم نور.
- Youthful without becoming childish.

Quick Access should preserve useful existing tools rather than delete them during redesign.

## 15. Existing/legacy tools to preserve

- PDF study tool.
- AI Buddy / study companions.
- Problem-image upload / Homework Coach.
- English tool.
- Escape Room.
- Python beginner area.
- Goals/planner and motivational message.

Feature redesign is allowed, silent feature loss is not.

## 16. Python

Current purpose:
- Beginner-friendly code explanation.
- Line-by-line understanding.
- Ask Nour to predict output before revealing it.
- Small modifications/challenges.

A true execution sandbox is lower priority than the core learning brain.

## 17. Parent view

A separate parent dashboard is required, without cluttering Nour's experience.

Useful weekly snapshot:
- What she studied.
- Mastery movement.
- Recurring weak concepts.
- Reviews due.
- English progress.
- AI skill progress.
- Suggested next focus.

It should be informative rather than intrusive.

## 18. Persistence and data

Current app has no durable database; session state is temporary.

Persistent data should eventually cover:
- Learner profile/settings.
- XP/levels/streak/badges.
- Mission attempts/completions.
- Mastery.
- Mistakes.
- Review queue.
- Adaptive tutor signals.
- Goals/tasks.
- Useful learning history.

Choose the simplest reliable low-cost backend after deployment constraints are confirmed. Supabase is a candidate, not an automatic decision.

## 19. Security/privacy

- Never expose or commit API keys.
- Keep secrets in deployment secret management.
- A light PIN/password or parent separation can be added where useful.
- Safe handling of uploaded learning materials.
- Nour's photo is a UI asset; it should not be sent to Gemini merely to display it.

## 20. Current technical implementation

Current stack:
- Python.
- Streamlit.
- google-genai.
- Gemini 2.5 Flash inside the app.
- Pillow for images.
- Streamlit Community Cloud deployment.
- GitHub repository: mohamed-hamuda/lumina-nour.

Current development branch:
- feature/nour-mobile-ui.

Current development work includes:
- Mobile-first home.
- Seven subject cards.
- Daily English mini mission.
- Demo XP/streak/level.
- AI Explorer placeholder.
- Existing Quick Access tools retained.
- Improved tutor prompts.
- MASTER_REQUIREMENTS.md.
- IMPLEMENTATION_PLAN.md.

Production/main has intentionally not been merged with this development work yet.

## 21. Development-tool decisions

- Codex is excluded from the Nour/Lumina project so its quota can be preserved for the user's accounting project.
- ChatGPT handles project management, architecture, implementation/review, GitHub work, and testing available through this workflow.
- Gemini remains the intended AI engine inside the finished Lumina app.
- Using Gemini as an additional development assistant is opt-in: explain the value/task first and get Mohamed's approval before using it for development work.

## 22. Current known gaps

Not yet complete:
- Final curriculum map.
- Persistent database.
- Permanent curriculum ingestion/retrieval.
- Real subject hubs.
- Real mastery tracking.
- Mistake Notebook.
- Spaced review.
- Adaptive tutor profile.
- Exam Mode.
- Full Homework Coach flow.
- Full English skill progression.
- Listening/speaking/pronunciation.
- Functional AI Lab.
- Parent Dashboard.
- Persistent meaningful gamification.
- Nour photo integrated into the branch.
- Full mobile/live regression test.
- Robust Gemini/network failure handling.
- Authentication/PIN if retained as final requirement.
- Modular code structure.

## 23. Conflicts resolved by later decisions

- Early UI-phase constraints that postponed database/RAG/voice/real gamification were phase boundaries, not permanent rejections. Later approved product requirements include these features in later phases.
- The app is not limited to school English; later confirmed direction creates School English plus a separate language-development track beyond grade level.
- Subject cards initially being presentation-only was a safe first UI step; final product requires functional subject hubs.
- Initial prototype estimates should not be treated as final-product estimates. Rapid AI-assisted code generation and full tested product readiness are different scopes.

## 24. Items intentionally not frozen before source mapping/testing

The final Master should avoid pretending the following are settled until evidence/implementation review:
- Exact database vendor.
- Exact retrieval/vector technology.
- Exact CEFR starting level for Nour before assessment.
- Exact mastery thresholds/scoring formula.
- Exact XP economy.
- Exact exam templates until current assessment evidence is mapped.
- Exact voice/STT/TTS provider.
- Exact authentication/PIN flow.
- Exact module/file architecture after refactor.
- Whether every supplied source represents the same academic year/term; source metadata must be recorded rather than assumed.

## 25. Pre-master conclusion

The project is ready for a final Master Specification after:
1. Treating the seven supplied curriculum areas as the initial source inventory.
2. Mapping their real internal structure and recording source metadata/term coverage.
3. Carrying forward every confirmed requirement in this audit.
4. Marking unresolved technical choices as decisions-to-make rather than silently choosing them.
5. Defining acceptance criteria and implementation order in the Master.

No large new feature implementation should precede the Master freeze, except investigation/testing needed to make the Master accurate.
