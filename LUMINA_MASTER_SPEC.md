# LUMINA / NOUR'S WORLD — MASTER SPECIFICATION

**Status:** Master v1.6 — APPROVED IMPLEMENTATION AUTHORITY  
**Date:** 2026-09-30  
**Product owner:** Mohamed  
**Learner:** Nour  
**Repository:** `mohamed-hamuda/lumina-nour`

> This is the single governing specification for LUMINA. Earlier requirement, audit, inventory, resume, and implementation documents remain useful history/evidence, but where they conflict with this Master, this Master governs. Mohamed approved proceeding with this Master on 2026-09-29.

---

## 1. Product vision

LUMINA is Nour's personal learning world. It is not a generic chatbot, a PDF reader, or a homework-answer machine.

It has four equal long-term missions:

1. Help Nour master her actual Egyptian Third Preparatory curriculum.
2. Develop her English as a real language beyond the ceiling of her school grade.
3. Build practical, enjoyable, critical AI literacy.
4. Build durable learning skills: reasoning, problem solving, research, verification, creativity, communication, independence, and confidence.

The product should become something Nour voluntarily opens because she wants to discover, solve, create, improve, or complete something meaningful.

Success is **learning and voluntary return**, not maximum screen time.

---

## 2. Non-negotiable product principles

### 2.1 Curriculum first
For curriculum-bound learning, Nour's supplied curriculum files are the primary source of truth. AI teaches from them; it does not silently replace them with generic memory.

### 2.2 Understanding before answer
Default behavior is coaching:
**curiosity → understand → example → Nour tries → hint → retry → application → check → record → later review.**

### 2.3 Fun with educational substance
Missions, stories, mysteries, quests, challenges, creation, and rewards are presentation mechanisms for real learning. No empty engagement loops.

### 2.4 English is bigger than school English
School English and real-language development are separate but connected tracks.

### 2.5 AI literacy is a subject and a tool
Nour must learn how to think with AI, direct it, verify it, challenge it, and create with it—not merely obtain answers.

### 2.6 Evidence-based progress
Mastery, XP, badges, levels, and recommendations must reflect demonstrated learning, not button clicks.

### 2.7 Extensibility is mandatory
LUMINA must be designed so future skills, subjects, learning modes, content sources, assessment types, AI tools, and parent analytics can be added without rebuilding the application core.

### 2.8 Preserve useful capabilities
Redesign must not silently remove useful existing tools.

---

## 3. Learner experience

The main interface is **Nour's World**.

It should feel:
- personal;
- mobile-first;
- polished and youthful, not childish;
- visually inviting;
- low-clutter;
- bilingual where educationally useful;
- English-forward without blocking understanding;
- consistent enough to feel like one world while allowing each subject its own personality.

Visual direction:
- dark navy/purple base;
- warm pink/lavender/blue accents;
- rounded, premium cards;
- clear typography;
- correct RTL/LTR handling;
- Nour's real photo as a static avatar/welcome asset;
- preserve photo aspect ratio;
- do not send the photo to Gemini merely to display it.

Navigation:
- Home / Nour's World;
- subject worlds;
- skill worlds;
- Quick Access tools;
- clear back route;
- separate parent area.

---

## 4. Core curriculum source inventory

Initial supplied subject areas:

1. Arabic — Term 1.
2. English — Term 1.
3. Islamic Religion — Term 1.
4. Social Studies — Term 1.
5. Mathematics in English — one supplied student-book PDF that contains a verified Term 1 section and a bundled explicit Term 2 section.
6. Science in English — one supplied student-book PDF that contains a verified Term 1 section and a bundled explicit Term 2 section.
7. Computer / ICT — supplied Second Semester source.

The curriculum catalog must model term scopes separately even when two terms share the same physical PDF file. A filename or cover label alone must not override verified internal term boundaries.

The detailed file-derived structure is maintained in `CURRICULUM_INVENTORY.md`.

Important technical fact: the corpus is mixed. Some PDFs expose usable parsed text; several important books are page-image/scanned in the current parser. Therefore LUMINA must not assume text-only ingestion.

Curriculum evidence can include:
- text;
- page images;
- diagrams;
- formulas;
- maps;
- tables;
- figures;
- page layout when educationally relevant.

---

## 5. Curriculum knowledge model

Canonical hierarchy:

**Subject → Track → Term/Semester → Unit/Chapter → Lesson/Topic → Concept/Skill → Source → Page/Range**

`Track` is optional and is used where separation matters, e.g. School English vs Real English.

Every permanent curriculum item should preserve provenance:
- source file;
- displayed academic metadata;
- subject;
- term/semester;
- unit/chapter;
- lesson/topic;
- concept/skill;
- page/range;
- extraction type (text/image/mixed);
- source status/trust classification.

For curriculum answers:
- retrieve the smallest useful evidence;
- preserve curriculum terminology;
- use the evidence in explanation;
- distinguish optional enrichment;
- expose useful source location where feasible;
- never silently invent missing curriculum material.

A vector database is optional, not a goal. Retrieval technology is chosen after testing the actual corpus.

---

## 6. Future file upload system

Upload remains a permanent product capability.

Supported learning inputs should progressively include:
- PDF;
- images/photos of questions;
- worksheets;
- school notes;
- future supported document types where useful.

Every upload must have a clear role:

### Temporary material
Use it now for a question, explanation, homework, summary, or practice without making it authoritative permanent knowledge.

### Permanent trusted source
Intentionally classify and index it into the learning library.

Permanent sources use an explicit hierarchy:
- **Official / Ministry** — defines curriculum scope and authoritative school content.
- **Supplied by parent** — trusted parent-provided material whose role is explicitly recorded.
- **Supplementary** — external books/notes used to strengthen explanation, examples, practice and revision without silently overriding the official source.

Supplementary books are not passive PDF storage. Their intended roles are recorded, including:
- Main Book → explanation + examples + supported practice.
- Assessments / Final Revision → practice + review + assessment patterns.
- Notebook / Revision Book → review + exam-style reinforcement.
- Answer Guide → correction reference only; hidden from learner-facing study content.

The system must not silently promote an arbitrary uploaded file into authoritative curriculum.

Future source management should support:
- classification;
- subject/skill assignment;
- term/unit metadata;
- duplicate detection where practical;
- replace/update source;
- disable/archive source without corrupting learning history.

---

## 7. Subject worlds

Core school subject worlds:

### English
School English plus linked Real English development.

### Science Lab
Prediction, observation, diagrams, concepts, experiments, why/how reasoning, applications, scientific vocabulary.

### Math Quest
Reasoning, patterns, formulas/notation, guided problems, multiple approaches where appropriate, error diagnosis.

### Arabic World
Listening, reading/texts, grammar, spelling, speaking, writing/expression and the actual integrated book structure.

### Social Detective
Geography/history, maps, chronology, cause/effect, comparison, evidence, inference and narrative investigations.

### Religion Journey
Creed, Quran/interpretation, Tajweed, worship, biography/figures, values/ethics, understanding and life application while preserving source framing.

### ICT Lab
Teach the supplied school ICT source with its actual terminology—including VB.NET where present—without silently replacing it with Python.

Each subject world can share platform services but must not be a cosmetic copy of the same chatbot.

---

## 8. English architecture

English has two distinct tracks sharing one learner language profile.

### 8.1 School English
Grounded in Nour's curriculum.

The supplied Term 1 book includes:
- Personal Identity;
- Communication with Family and Friends;
- Artificial Intelligence;
- Screen Time;
- Design Thinking;
- Why Do We Like Stories?;
- reviews.

School English should preserve the source's integrated skills and lesson patterns where relevant:
- vocabulary;
- grammar/functions;
- reading;
- writing;
- listening;
- speaking;
- higher-order thinking;
- guided-to-independent production.

### 8.2 Real English / English Adventure
Not limited by Third Preparatory level.

Goal: develop Nour's actual language ability.

Skill profile:
- Vocabulary;
- Grammar;
- Reading;
- Writing;
- Listening;
- Speaking;
- Pronunciation.

Experience can include:
- practical conversations;
- interactive stories;
- real-life scenarios;
- useful expressions;
- short writing;
- listening challenges;
- speaking;
- pronunciation/shadowing;
- mini missions;
- creative tasks.

Start from demonstrated ability, not grade assumptions.

Use a CEFR-like progression as a practical framework where helpful, but do not reduce Nour to a single label.

Arabic assistance is adaptive: use it when it unlocks understanding and reduce it as Nour becomes more capable.

Future English assessment should identify skill-level strengths and weaknesses and continuously update the language profile.

---

## 9. AI Lab

AI literacy is a first-class learning world.

Progression should cover:
- what AI is and is not;
- good questions;
- prompt construction;
- prompt improvement;
- asking for hints rather than answers;
- comparing outputs;
- checking claims;
- hallucinations and uncertainty;
- trustworthy-source habits;
- study/research/summarization;
- text, image, and file workflows;
- creativity;
- privacy and responsible use;
- later AI + Python projects.

Learning style:
**Create → Experiment → Discover → Verify → Reflect.**

Experiences:
- AI Detective;
- Prompt Challenge;
- Fact Checker;
- Creative Builder;
- compare two explanations;
- identify an unsupported claim;
- improve a weak AI response;
- build a study aid and evaluate it.

Potential badges:
- Prompt Explorer;
- AI Detective;
- Fact Checker;
- Creative Builder.

Badges require evidence.

---

## 10. Future Skills Framework — mandatory architecture

LUMINA is not hard-coded to today's seven subjects and current skill list.

A future skill such as:
- Critical Thinking;
- Public Speaking;
- Research Skills;
- Financial Literacy;
- Creative Writing;
- Advanced Coding;
- Presentation Skills;
- Study Skills;
- another future skill chosen by Mohamed

must be addable as a module without rewriting the application core.

A skill/module definition should be able to declare:
- id and name;
- category (school subject / language / life skill / AI / coding / future category);
- icon/visual identity;
- description;
- prerequisites;
- levels/stages;
- concepts/competencies;
- mission/activity types;
- assessment rules;
- mastery dimensions;
- rewards/badges;
- source requirements;
- AI tutor instructions;
- enabled/disabled state;
- parent-dashboard metrics.

The core platform should discover/render registered modules rather than require duplicated hard-coded navigation logic for every new skill.

**Acceptance test:** adding a normal new skill should primarily involve adding/configuring its module, content, and rules—not redesigning navigation, database fundamentals, progress engine, or tutor core.

---

## 11. Teaching engine

Default tutor loop:

1. Trigger curiosity or identify the need.
2. Establish what Nour already understands.
3. Explain the smallest useful idea.
4. Show an example where appropriate.
5. Ask Nour to try.
6. Give progressive hints rather than immediate answers.
7. Diagnose the error.
8. Change teaching method if needed.
9. Ask for a new application.
10. Verify understanding.
11. Record evidence/mistake/mastery.
12. Schedule review where appropriate.

Possible explanation modes:
- simpler language;
- Arabic support;
- analogy;
- story;
- visual/diagram reference;
- worked example;
- smaller steps;
- compare/contrast;
- real-world application.

The tutor should not make unsupported psychological judgments about Nour.

---

## 12. Teach Me Mode

When Nour says she does not understand:

1. locate the exact concept;
2. ask/check prior understanding where useful;
3. explain simply;
4. ask one small comprehension question;
5. change method if needed;
6. let Nour try;
7. verify with a new example;
8. record evidence;
9. schedule review if still weak.

Avoid default long information dumps.

---

## 13. Homework Coach

For images/files/homework:

**What do you think we should start with? → Hint 1 → Hint 2 → worked reasoning → final answer only when needed → quick check.**

Curriculum-bound homework should retrieve the relevant curriculum evidence where available.

The goal is to help Nour become less dependent on the coach over time.

---

## 14. Mastery Engine

Canonical mastery hierarchy:

**Module/Subject → Unit/Stage → Lesson/Competency → Concept/Skill**

Core states:
- Not started;
- Learning;
- Needs review;
- Mastered.

Mastery is based on evidence across attempts/reviews—not one correct click.

The engine should support subject-specific evidence while sharing a common progress contract.

Examples:
- Math: reasoning/problem type/concept.
- English: reading vs speaking vs vocabulary etc.
- Science: concept + application/interpretation.
- AI: prompt skill + verification behavior.

Exact thresholds remain configurable and must be validated rather than permanently hard-coded.

---

## 15. Mistake Notebook

Record educationally useful mistakes:
- module/subject;
- concept/skill;
- question/task;
- Nour's response;
- correct reasoning/target;
- mistake category;
- hints required;
- date;
- source reference when relevant;
- review status;
- later performance.

Initial mistake categories:
- concept understanding;
- application;
- question reading;
- inference;
- linking ideas;
- calculation;
- English/language comprehension;
- careless error.

Categories must be extensible.

---

## 16. Spaced Review and adaptive learning

The system should generate review work from:
- mistakes;
- weak mastery;
- elapsed time;
- repeated hint dependence;
- curriculum priorities;
- English skill gaps;
- AI-skill gaps.

Review should use a different question/context when possible rather than simply repeating the same answer.

Adaptive difficulty and scaffolding should change from observed learning evidence.

Current approved difficulty progression:
- **Level 1 — Gentle start:** one small concept check, no pressure, no timer, no penalty.
- **Level 2 — Build understanding:** a small application after evidence of initial understanding.
- **Level 3 — Light challenge:** only after at least two distinct successful checks and no unresolved misconception forcing a step-back.

If Nour struggles, LUMINA must step down automatically, reveal progressively stronger hints, re-explain from verified evidence, and later revisit the concept in a different context. Difficulty must never rise merely because of age or school grade.

---

## 17. Exam Mode

Inputs may include:
- subject/module;
- unit/scope;
- time;
- difficulty where appropriate;
- practice purpose.

Behavior:
- use curriculum evidence;
- follow actual source/verified assessment patterns;
- hide answer key until completion;
- support understanding/application/reasoning where appropriate.

After exam:
- result;
- question-level feedback;
- weak concepts;
- mistake categories;
- recommended next action;
- mastery update only where evidence supports it;
- review queue entries.

Do not freeze generic exam templates until current assessment evidence is verified.

---

## 18. Daily Mission and Weekly Smart Plan

Daily Mission is selected from real learning needs:
- curriculum progress;
- weak concept;
- due review;
- English development;
- AI challenge;
- upcoming assessment;
- creative/skill mission.

Weekly plan balances:
- school curriculum;
- English;
- AI;
- reviews;
- optional future skills.

It must avoid overload.

---

## 19. Healthy engagement and gamification

Use:
- XP;
- levels;
- streak;
- badges;
- missions;
- weekly challenges;
- meaningful unlocks;
- visible mastery;
- stories/mysteries;
- creation challenges.

Rules:
- no infinite scroll;
- no endless autoplay;
- no manipulative streak pressure;
- no meaningless points;
- no dark patterns;
- clear completion/stopping moments.

A meaningful action earns reward because learning occurred.

Streak design should be forgiving rather than anxiety-producing.

---

## 20. Persistent Tutor Profile

Store only educationally useful information:
- mastered concepts;
- concepts in progress;
- concepts needing review;
- mistake patterns;
- English skill profile;
- AI skill profile;
- future skill profiles;
- typical scaffolding required;
- recent learning;
- review schedule;
- mission history needed for adaptation.

Do not create unsupported personality, intelligence, mental-health, or psychological profiles.

---

## 21. Parent Dashboard

Separate from Nour's main experience.

Weekly/period views can show:
- curriculum progress;
- mastery changes;
- weak concepts;
- recurring mistakes;
- reviews due;
- English progress by skill;
- AI skill progress;
- future-skill progress;
- completed meaningful missions;
- recommended next focus.

It is a learning dashboard, not intrusive surveillance.

---

## 22. Quick Access tools to preserve

Current useful tools should survive refactoring:
- PDF/file study companion;
- AI Buddy;
- problem-image helper;
- English helper;
- Escape Room;
- Python learning;
- goals/planner;
- motivational AI behavior.

Quick Access = tools.  
Subject/Skill Worlds = structured learning journeys.

---

## 23. Python and making

Python is enrichment/creative computational literacy, separate from school ICT when the school source uses another language.

Near term:
- explain short code;
- predict output;
- modify one element;
- tiny useful/fun programs.

Later:
- safe execution sandbox;
- small projects;
- AI + Python.

Do not prioritize a heavy sandbox before the learning core.

---

## 24. Platform architecture

The implementation should progressively move away from a monolithic `app.py`.

Target conceptual layers:

### Presentation layer
Pages, navigation, components, theme, RTL/LTR, accessibility.

### Module registry
Subjects and future skills register themselves through a common contract.

### Learning engine
Tutor flow, attempts, hints, mastery evidence, mistakes, reviews, missions.

### Content/knowledge layer
Source ingestion, metadata, page/image/text extraction, retrieval, provenance.

### AI service layer
Provider/model calls, prompt policies, grounding, retries/failures, cost controls.

### Persistence layer
Learner state, progress, mastery, mistakes, missions, source metadata.

### Analytics/parent layer
Aggregated learning evidence and recommendations.

The UI must not directly own business logic that future modules need to reuse.

---

## 25. Extensible data model principles

Use stable IDs and relationships instead of encoding today's subject names into database columns.

Prefer structures equivalent to:
- learners;
- modules;
- module_units/stages;
- concepts/competencies;
- sources;
- source_segments/pages;
- activities/missions;
- attempts;
- mastery_evidence/state;
- mistakes;
- reviews;
- achievements;
- goals/plans;
- learner_skill_profiles.

Exact tables/vendor are not frozen by this Master.

New modules should reuse these generic structures and add module-specific metadata only where necessary.

Schema migrations must preserve existing learning history.

---

## 26. AI service rules

Gemini is currently the intended in-app AI engine.

Requirements:
- API secrets never committed;
- centralize model access instead of scattered calls;
- curriculum grounding for curriculum tasks;
- structured outputs where reliability benefits;
- graceful missing-key/network/model-error behavior;
- cost/token awareness;
- avoid resending whole books when retrieval can supply relevant evidence;
- log only safe/necessary operational information.

Provider architecture should avoid making every feature impossible to change if the model/provider changes later.

---

## 27. Persistence

Session state is prototype-only.

Production progress must survive refresh/restart.

Persist at minimum:
- learner settings;
- module registrations/config needed at runtime;
- XP/level/badge evidence;
- streak evidence;
- mastery;
- mistakes;
- reviews;
- English profile;
- AI profile;
- future skill profiles;
- meaningful learning history;
- goals/plans;
- source metadata.

Backend selection criteria:
- reliability;
- maintainability;
- low/free cost where practical;
- secure secret handling;
- migration capability;
- fit with Streamlit deployment.

Neon PostgreSQL is the selected durable persistence backend for LUMINA NOUR. The persistence contract remains provider-independent so this decision does not couple the learning core to Neon.

---

## 28. Privacy, access, and safety

- Never expose API keys.
- Protect private learning progress and paid API usage with appropriate lightweight access control.
- Separate parent functions from Nour's normal UI.
- Do not send Nour's profile image to an AI service simply to display it.
- Minimize unnecessary personal data.
- Store educational signals, not invasive profiling.
- Treat uploaded files safely.
- Future features that materially change privacy behavior require explicit design review.

---

## 29. Accessibility and resilience

The app should:
- work well on phone widths;
- have touch-friendly controls;
- preserve readable contrast;
- handle Arabic RTL and English LTR correctly;
- avoid critical hover-only interactions;
- give clear loading/error/retry states;
- avoid losing Nour's completed work because of a transient model error where feasible;
- degrade gracefully if AI is temporarily unavailable.

---

## 30. Current implementation state

Current stack:
- Python;
- Streamlit;
- `google-genai`;
- Gemini 2.5 Flash;
- Pillow;
- psycopg / Neon PostgreSQL;
- boto3 / Neon Object Storage;
- Streamlit Community Cloud;
- GitHub.

Development branch:
`feature/nour-mobile-ui`

Current branch now includes:
- modular home/router/world structure;
- a gentle adaptive-scaffolding engine with three evidence-driven difficulty levels;
- one-question-at-a-time cognitive-load control and progressive hints;
- creative mission framing across subject worlds;
- live supplementary-source learning support that can use saved Main Books for simpler/creative explanations and revision books for source-grounded extra practice;
- learner-facing Answer Guides kept hidden and reserved as correction references;
- seven enabled school-subject worlds;
- mapped curriculum registry across supplied subjects;
- separate School English and Real English tracks;
- AI Lab foundation;
- source-grounded lesson checks;
- Daily Mission;
- adaptive Weekly Plan;
- Curriculum Search;
- evidence-based XP/streak/profile persistence;
- Mistake Notebook and review queue;
- source-grounded Exam Mode;
- Parent Dashboard;
- Quick Access tools;
- persistent Neon learning storage with verified live production connectivity;
- permanent trusted-source metadata catalog;
- selected Neon Object Storage backend and private `lumina-trusted-sources` bucket;
- permanent-source upload/archive UI in Parent Dashboard with live Neon Object Storage verified by six real El-Moasser uploads;
- learner-facing language cleanup and stronger mobile/photo presentation;
- CI/AppTest coverage for navigation, school worlds, learning flows, persistence contracts, source contracts, secret scanning and learner-facing UI guards.

No merge to production/main is authorized merely by this Master.

---

## 31. Known gaps

Still required before V1 production merge:
- final live verification that Streamlit Community Cloud is serving the exact latest feature-branch commit;
- one live interaction proving a saved supplementary PDF can be read by the deployed app for explanation/practice;
- final phone/browser visual smoke on the deployed app;
- final access-control/PIN verification only if those optional controls are enabled;
- explicit Mohamed approval before merging PR #1 to `main`.

Completed release evidence:
- six real El-Moasser PDFs are registered in Neon and present in private Object Storage;
- automated full learning transaction passes: wrong answer → mistake/review → correct retry → XP;
- AI Literacy hands-on activity transaction and durable skill profile pass;
- Real English baseline/adaptive profile transaction passes;
- mobile-first CSS/release guards and all current CI contracts pass on the development branch.

Post-V1 depth improvements remain planned rather than release blockers:
- richer subject-specific adventures and activity formats beyond the current mission/puzzle foundation;
- broader lesson-by-lesson Level 2/3 curated question coverage beyond the initial Science/Math prototypes;
- deeper adaptive Tutor Profile/scaffolding;
- broader Real English listening/speaking/pronunciation;
- deeper AI Lab progression and evidence-based badges;
- richer parent analytics;
- more sophisticated spaced review and exam configuration.

---

## 32. Final audit reconciliation

The Master has been cross-checked against the pre-master audit, curriculum inventory, implementation plan, and current feature-branch app.

Reconciliation decisions:
- All seven subject worlds are retained.
- School English and Real English are explicitly separate tracks sharing one learner profile.
- AI literacy remains a core learning pillar, not only an AI backend feature.
- Future Skills Framework is a mandatory architectural requirement.
- Permanent upload supports both temporary material and intentionally trusted/indexed sources.
- Image/page-aware curriculum handling is mandatory because the supplied corpus is mixed.
- Existing Quick Access capabilities are protected from silent regression.
- Prototype XP/streak/daily mission must not be mistaken for final evidence-based gamification.
- ICT's supplied VB.NET material remains separate from Python enrichment.
- Current app is still monolithic and must be modularized before large feature expansion.
- The earlier implementation plan's wording about waiting for curriculum uploads is superseded: the initial seven-subject source inventory is now available and inventoried.
- No production/main merge is implied by Master approval; implementation remains on the development branch until the quality gate and explicit production approval.

No unresolved requirement discovered in the final audit blocks Phase 1 implementation. Technical choices intentionally left configurable in Section 37 remain decisions to be made at the appropriate phase.

---

## 32. Development constraints and roles

For the Nour/LUMINA project:
- Codex is excluded so its quota can remain available for Mohamed's accounting project.
- ChatGPT acts as project manager/architect/implementation and review lead using available project tools.
- Gemini is the intended AI engine inside the application.
- Gemini as an additional **development assistant** is opt-in: explain why it is useful and obtain Mohamed's approval before using it for development.

Do not add technology merely because it is fashionable or available.

---

## 33. Implementation sequence

### Phase 1 — Freeze and modular foundation
- approve this Master;
- keep audit/inventory as evidence;
- refactor monolith safely;
- create module registry/common contracts;
- preserve feature parity;
- stabilize mobile navigation;
- integrate Nour photo safely;
- static/syntax/browser checks.

### Phase 2 — Curriculum engine
- page-by-page/source metadata indexing;
- support text + image-heavy sources;
- build subject/unit/lesson/concept map;
- implement targeted retrieval;
- show provenance;
- test grounding against real books.

### Phase 3 — Persistent learning brain
- choose persistence backend;
- implement learner/module/source/progress data model;
- attempts;
- mastery;
- mistakes;
- spaced reviews;
- Tutor Profile;
- persistent gamification.

### Phase 4 — Core learning modes
- Teach Me;
- Homework Coach;
- Exam Mode;
- adaptive missions;
- weekly plan.

### Phase 5 — English Adventure
- baseline assessment;
- School English integration;
- Real English skill journey;
- adaptive scaffolding;
- writing/reading/vocabulary/grammar;
- then listening/speaking/pronunciation.

### Phase 6 — AI Lab
- progressive AI literacy;
- AI Detective;
- Prompt Challenge;
- Fact Checker;
- Creative Builder;
- evidence-based badges.

### Phase 7 — Engagement worlds
- richer subject adventures;
- mysteries;
- stories;
- creation challenges;
- meaningful unlocks.

### Phase 8 — Parent Dashboard
- weekly snapshot;
- mastery/weakness/review;
- English/AI/future-skill progress;
- recommendations.

### Phase 9 — Hardening
- mobile/browser regression;
- failure/retry testing;
- privacy/security;
- cost/performance;
- migration/backup behavior;
- final feature-parity review.

---

## 34. Definition of Done for a feature

A feature is not “done” because code exists.

Where applicable it must:
1. work on mobile;
2. preserve RTL/LTR correctly;
3. use the correct source/track;
4. handle empty/error/model-failure states;
5. persist required progress;
6. produce evidence for mastery/reward where appropriate;
7. not leak secrets;
8. not break existing capabilities;
9. be testable;
10. be understandable to Nour without technical explanation;
11. expose useful parent analytics only where appropriate;
12. remain compatible with future module extension.

---

## 35. Pre-merge quality gate

Before merging a significant release to `main`:
- syntax/static checks pass;
- key flows tested;
- mobile visual verification;
- no secret leakage;
- missing/failed Gemini behavior tested;
- curriculum grounding sampled against source pages;
- progress persistence tested;
- feature parity reviewed;
- new module architecture not bypassed with unnecessary hard-coded exceptions;
- known limitations documented;
- explicit Mohamed approval for production merge.

---

## 36. Change control

New ideas are expected.

For each meaningful new feature/skill ask:
1. Does it improve curriculum mastery, English, AI literacy, another approved skill, reasoning, creativity, or healthy engagement?
2. Is it appropriate for Nour?
3. Is there a simpler implementation with the same benefit?
4. What evidence will show learning?
5. Does it introduce cost/privacy/maintenance risk?
6. Can it be implemented as a module/configuration rather than changing the core?
7. Does it require a Master update?

Important approved decisions update this Master or a versioned successor.

---

## 37. Decisions intentionally left configurable

The Master deliberately does **not** freeze:
- database vendor;
- vector/retrieval vendor;
- exact CEFR starting level;
- exact mastery thresholds;
- exact XP economy;
- exact voice/STT/TTS provider;
- exact authentication flow;
- exact model/provider forever;
- exact exam templates before verified assessment mapping;
- every future skill.

These are implementation/configuration decisions and should not force a rewrite of the product architecture.

---

## 38. Master acceptance criteria

This Master is successfully implemented only when LUMINA can demonstrate the following end-to-end:

1. Nour opens a personal mobile-first world.
2. She enters a real subject lesson backed by her source material.
3. The tutor teaches rather than dumps an answer.
4. Her attempt creates meaningful learning evidence.
5. A mistake can enter the Mistake Notebook.
6. Mastery can change based on evidence.
7. A later review can be scheduled and completed.
8. English has a school path and a separate beyond-school language path.
9. AI literacy has a real progressive learning path.
10. Progress survives restart.
11. Mohamed can see useful parent-level progress.
12. Future trusted files can be added safely.
13. A new future skill can be registered without rebuilding the core platform.
14. Existing useful Quick Access capabilities remain available.
15. Production changes are tested before merge.

---

## 39. Governing product statement

**LUMINA should grow with Nour.**

The curriculum changes, her English level rises, AI evolves, and Mohamed may add new skills that are not known today. The architecture must therefore preserve a stable learning core while allowing content, modules, skills, activities, assessments, models, and experiences to evolve.

The product is successful when Nour increasingly needs fewer hints, understands more deeply, communicates better in English, uses AI more critically and creatively, and can keep learning new skills through the same expandable platform.


---

## 40. Master v1.1 change note

This revision does not change the product mission. It records verified implementation/source discoveries made after v1.0:

- The supplied Math PDF contains explicit Term 1 and Term 2 sections.
- The supplied Science PDF contains explicit Term 1 and Term 2 sections.
- Term scope is therefore modeled independently from physical file identity.
- All seven school subject worlds now have functional routing foundations.
- The reusable learning brain now includes learning evidence, Mistake Notebook, Review Queue, conservative Mastery state derivation, a persistence contract, and a Parent Dashboard foundation.
- English Term 1, Science Term 1, and Math Term 1 have progressed from inventory-only status to structured verified lesson mappings in the development branch.

All architectural principles and acceptance criteria from v1.0 remain in force.


---

## 41. Master v1.2 change note

This revision records implementation progress without changing the governing product mission or acceptance criteria.

Verified development-branch state:
- A cross-subject mapped curriculum registry now contains 144 structured learning blocks across all seven supplied subject areas, including two structured English review blocks.
- English Term 1 is mapped across six units; Science and Math are mapped across both verified terms contained in their supplied PDFs; Arabic, Social Studies, and Religion are mapped for the supplied Term 1; ICT is mapped for the supplied Second Semester.
- Missing terms are not invented. A subject/term becomes curriculum-authoritative only when a trusted source supports it.
- A reusable all-subject Exam Mode now creates learning evidence and routes mistakes into review.
- Daily Mission selection now prioritizes due review and otherwise chooses from not-started mapped learning content.
- XP, streak, and badges are tied to new demonstrated learning evidence rather than simple button clicks.
- Parent Dashboard now aggregates all mapped subjects and includes a seven-day evidence snapshot.
- Learning attempts, mistakes, and review records now carry timestamps in the current persistence adapter.
- The persistence contract remains backend-independent; current session storage/manual backup is a temporary adapter, not the final durable database.

Outstanding high-priority work remains durable persistence, fine-grained source retrieval for arbitrary curriculum questions, live/mobile regression testing, real-photo asset integration, deeper adaptive mastery, and source-backed coverage for any school terms not yet supplied.


---

## 42. Master v1.3 change note

This revision records additional verified implementation progress:

- Nour's real photo is now integrated as a repository asset and shown in the home hero.
- An optional whole-app PIN gate is implemented in addition to the separate Parent Dashboard protection.
- A durable persistence schema and backend adapter were initially prepared around Supabase during exploration; this historical step was superseded by the later Neon decision. Existing accounting Supabase projects remained untouched.
- The persistence contract now covers attempts, mistakes, reviews, and learner profile state (XP, streak, badges, English profile, rewarded evidence).
- Learner profile state can hydrate automatically when a durable backend is configured.
- A cross-subject Curriculum Search now searches the 144 structured learning blocks and can ask the AI to explain only from the verified mapped evidence, explicitly refusing to invent unsupported details.
- Durable persistence activation still requires a dedicated LUMINA backend/project and server-side secrets before production release.


---

## 43. Master v1.4 change note

Persistence provider decision:
- LUMINA NOUR will use a dedicated Neon PostgreSQL database as the preferred durable persistence backend.
- Existing PROJECT LEDGER and PROJECT LEDGER UAT Supabase projects remain untouched.
- The application uses a backend-independent LearningStore contract; Neon is selected by `NEON_DATABASE_URL`.
- Obsolete Supabase persistence code has been removed from the LUMINA runtime path; Neon is now the single configured durable backend while the generic LearningStore contract preserves future portability.
- The Neon schema covers learning attempts, mistakes, reviews, and learner profile state.
- Portable backup/restore now reads from and writes to the active persistence store, allowing migration between temporary session storage and Neon without losing learning evidence.
- Production should use Neon's pooled PostgreSQL connection string with SSL enabled.


---

## 44. Master v1.5 change note

Persistence implementation consolidation:
- Neon PostgreSQL is now the single selected production persistence backend for LUMINA NOUR.
- The canonical runtime adapter is `NeonLearningStore` and the canonical schema is `neon/lumina_schema.sql`.
- Duplicate/legacy Supabase persistence runtime files and duplicate PostgreSQL adapter/schema paths were removed to avoid configuration ambiguity.
- Runtime selection uses `NEON_DATABASE_URL` + `NOUR_LEARNER_KEY`; when they are absent, the app safely falls back to session-only prototype storage.
- The Neon connection must remain server-side and use SSL; hosted production should prefer the Neon pooled connection string.
- Activation still requires a dedicated Neon account/project connection and applying the prepared schema before the production merge.


---

## 42. Master v1.6 change note

This revision records Mohamed's approved direction that LUMINA must make learning attractive and indirect rather than behave like a PDF library or hard question bank.

Approved implementation rules:
- learning should feel like missions, puzzles, stories, short challenges and discovery where appropriate;
- understanding comes before memorization;
- difficulty rises only from demonstrated evidence;
- one small task is preferred over a large intimidating question block;
- wrong answers trigger support, not punishment;
- supplementary books must actively support explanation, examples, practice, revision and correction according to their role;
- official Ministry sources remain authoritative for curriculum scope;
- Main Books may enrich teaching, assessment/revision books may generate practice, and Answer Guides remain hidden correction references;
- generated supplementary practice is not automatically treated as official mastery evidence;
- Science and Maths contain the first curated Level 1 → Level 2 → Level 3 prototype flows, to be generalized after learner validation.

This change strengthens Sections 2, 6, 11, 16 and 19 without changing the product mission.


---

## 43. Master v1.6 release-audit note — 2026-09-30

The pre-release audit now distinguishes **automated evidence** from **live visual evidence**.

Automated evidence completed on the development branch includes:
- permanent-source classification and priority rules;
- six real supplementary PDFs stored in Neon Object Storage with matching database metadata;
- source-role routing that keeps Answer Guides learner-hidden;
- gentle adaptive question difficulty and one-question-at-a-time scaffolding;
- wrong-answer → review → correct-retry → XP end-to-end AppTest;
- AI Literacy evidence tracking;
- Real English adaptive baseline/profile tracking;
- mobile CSS guards and secret scanning.

The remaining checks intentionally require the deployed Streamlit UI:
1. confirm the exact latest candidate commit is live;
2. trigger one saved-PDF explanation/practice action against the deployed storage credentials;
3. visually inspect the final experience at phone width;
4. obtain Mohamed's explicit production-merge approval.

No merge is authorized by this note.
