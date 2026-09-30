# LUMINA / NOUR'S WORLD — MASTER REQUIREMENTS

> Living product specification for Nour's personal learning app.
> Status: approved direction. This file is the reference for future design and implementation.
> Branch policy: develop and test on feature branches; do not merge to main before review.

## 1. Product mission

LUMINA is not a homework-answering chatbot. It is Nour's personal learning world for Egyptian Third Preparatory (3rd Prep) language-school study, English growth, AI literacy, curiosity, creativity, and healthy engagement.

The experience should make learning attractive enough that Nour voluntarily chooses useful challenges over passive time-wasting feeds. We do **not** copy harmful engagement patterns such as infinite scroll or empty reward loops. Every interaction should lead to a meaningful learning outcome, creation, reflection, or demonstrated skill.

Core outcomes:
1. Master the current Third Preparatory curriculum and its current assessment/learning style.
2. Improve practical English progressively.
3. Build strong, enjoyable, age-appropriate AI skills and digital judgment.
4. Build independent learning, reasoning, problem-solving, and confidence.

## 2. Learning philosophy

Default loop:
**Curiosity / Story / Mission → Discover → Understand → Example → Nour tries → Hint → Retry → Apply in a new context → Quick check → Record learning/mistake → Review later.**

Rules:
- Understanding before memorization whenever possible.
- Do not give the final answer immediately by default.
- Prefer questions, hints, scaffolding, and retrieval practice.
- When memorization is genuinely required by the curriculum, make it meaningful and use spaced review.
- Diagnose why an answer was wrong: concept understanding, application, question reading, inference, linking ideas, calculation, English/language comprehension, or careless error.
- Adapt explanation style when Nour does not understand: simpler wording, analogy, story, visual idea, worked example, or smaller steps.
- Encourage Nour without exaggerated praise or childish language.
- Teach at her age and school level, while allowing enrichment when clearly marked.

## 3. Current curriculum is the source of truth

The uploaded current-year curriculum files are the primary source for curriculum-bound teaching.

Required curriculum library structure:
**Subject → Term → Unit → Lesson → Concept → Source / Page**

The system should eventually retrieve only the relevant curriculum passages instead of repeatedly sending whole PDFs to the model.

For curriculum questions:
- Prefer the uploaded curriculum over model memory.
- Preserve official terminology, especially English terminology used by the language-school curriculum.
- Distinguish curriculum content from optional enrichment/general knowledge.
- Cite/display source location when feasible (subject, unit, lesson, page/source).
- Never silently invent missing curriculum content.

Curriculum ingestion, mapping, and RAG design must be finalized only after the uploaded source set has been inspected.

## 4. Subjects / Subject Hubs

Seven core hubs:
1. English
2. Science
3. Math
4. Arabic
5. Social Studies
6. Religion
7. ICT

Each subject should have its own learning personality rather than seven copies of the same chatbot.

Examples:
- Science Lab: experiments, why/how reasoning, analogies, prediction, interpretation.
- Math Quest: problem-solving, hints, patterns, reasoning, multiple approaches where appropriate.
- Social Studies: stories, investigations, timelines, maps, evidence and comparison.
- English Adventure: practical language journey.
- Arabic, Religion, ICT: experiences designed around the actual current curriculum after source review.

Until a hub is truly implemented, the UI may show it as coming soon rather than pretending it is complete.

## 5. Current Egyptian 3rd Prep learning and assessment style

LUMINA must follow the current curriculum's actual organization and assessment approach found in the uploaded materials and verified official guidance when needed.

Learning activities should go beyond recall and include, where supported by the curriculum:
- understanding and interpretation;
- application;
- problem solving;
- comparison and classification;
- inference and reasoning;
- linking concepts;
- explaining why/how;
- transfer to a new situation;
- reading and interpreting question wording.

Exam generation must reflect actual curriculum/evaluation patterns rather than defaulting to generic memorization questions.

## 6. English Adventure

English is a strategic priority.

Skill map:
**Vocabulary → Grammar → Reading → Writing → Listening → Speaking → Pronunciation**

Requirements:
- Gradual assistance levels.
- Gentle correction with concise Arabic explanation when useful.
- Practical conversations and missions, not only grammar drills.
- Vocabulary in meaningful contexts.
- Reading comprehension and writing.
- Later: speech-to-text, text-to-speech, listening practice and pronunciation coaching.
- Track strengths/weaknesses by skill, not just one global English score.
- Reduce scaffolding as Nour improves.
- Use curriculum English where relevant, while also building practical English.

## 7. AI Lab / AI Explorer

AI literacy is a core product pillar, not a side tab.

Nour should learn to:
- understand what AI can and cannot do at an age-appropriate level;
- ask clear questions;
- write and improve prompts;
- request hints rather than answers;
- compare outputs;
- verify claims against reliable/source material;
- recognize hallucinations and uncertainty;
- use AI for study, explanation, brainstorming and creation;
- work with text, images and files;
- think critically about privacy, safety and responsible use;
- eventually combine AI with simple Python/projects.

Teaching style: **Create → Experiment → Discover → Reflect.**

Examples:
- AI Detective: find the incorrect AI claim using curriculum sources.
- Prompt Challenge: improve a prompt until it produces a useful quiz.
- Creative Builder: use AI to create a story, study aid, visual concept or small project.
- Compare two AI explanations and decide which is better and why.

Possible badges include Prompt Explorer, AI Detective, Fact Checker and Creative Builder. Badges must represent real achievements.

Key principle:
**Nour learns how to think with AI, direct it, verify it, and create with it — not merely obtain answers from it.**

## 8. Engagement without addiction

The product should compete for attention through curiosity, agency, story, creation, mastery and meaningful achievement.

Do:
- short missions;
- mysteries and quests;
- escape-room style learning;
- progress visibility;
- meaningful unlocks;
- creation challenges;
- variety and surprise;
- clear stopping points and completion moments.

Do not:
- infinite scroll;
- manipulative streak pressure;
- meaningless points;
- endless autoplay;
- dark patterns designed only to maximize screen time.

Success is learning and voluntary return, not minutes spent in the app.

## 9. Gamification

Replace the prototype with persistent, learning-linked systems:
- XP for meaningful learning actions;
- Levels derived from actual XP/progress;
- Streak with forgiving design;
- Badges tied to demonstrated skills;
- Daily Mission selected from real learning needs;
- Weekly challenges;
- meaningful unlocks where useful.

A user must not earn important XP simply by pressing "done" without completing the learning action.

## 10. Adaptive Personal Tutor

Create a persistent Tutor Profile that learns educationally relevant patterns over time:
- concepts mastered;
- concepts being learned;
- concepts needing review;
- recurring mistakes;
- English skill profile;
- hint/support level required;
- recent learning;
- review schedule.

The tutor should use this profile to select explanations, difficulty, review questions and Daily Missions.

Avoid unsupported psychological profiling. Store only what is useful for learning.

## 11. Mastery Map

Track:
**Subject → Unit → Lesson → Concept**

Suggested states:
- Not started
- Learning
- Needs review
- Mastered

Mastery should be based on evidence from attempts/reviews, not a single button press.

## 12. Mistake Notebook + spaced repetition

Automatically record useful learning mistakes, including:
- question/concept;
- Nour's answer;
- correct reasoning/answer;
- diagnosed mistake type;
- hints needed;
- date;
- review status.

Revisit weak concepts later using different questions and spaced repetition.

## 13. Exam Mode

Allow selection of subject/unit/scope and, where appropriate, time/difficulty.

Generate assessments grounded in the current curriculum and its assessment style.

After completion provide:
- score/result;
- question-by-question feedback;
- concepts needing review;
- mistake categories;
- recommended next activity;
- Mastery Map updates where evidence is sufficient.

Do not expose the answer key before completion.

## 14. Teach Me Mode

For "I don't understand":
1. identify the exact concept;
2. explain simply;
3. ask a tiny comprehension question;
4. if needed, change the explanation method;
5. let Nour try;
6. confirm understanding with a new example;
7. schedule review if still weak.

Avoid dumping long summaries by default.

## 15. Homework Coach

Image/file homework support should default to coaching, not answer dumping.

Flow:
**What do you think? → Hint 1 → Hint 2 → worked reasoning → final answer when needed → one quick check.**

For curriculum-bound work, use the curriculum knowledge base where available.

## 16. Daily Mission + Weekly Smart Plan

Daily Missions should eventually be selected from:
- curriculum progress;
- weak concepts;
- spaced reviews;
- English skill needs;
- AI skill challenges;
- upcoming assessment needs.

Weekly Smart Plan should balance curriculum, English, AI and review without overwhelming Nour.

## 17. Parent Dashboard

A separate parent-oriented view for Mohamed should summarize useful progress without turning into intrusive surveillance:
- curriculum/mastery progress;
- concepts needing help;
- recurring mistakes;
- English skill progress;
- AI skill progress;
- completed learning missions;
- weekly learning pattern;
- upcoming recommended focus.

Keep Nour's main interface simple and motivating; detailed analytics belong in the parent view.

## 18. UI / UX

Mobile-first is mandatory.

Direction:
- "Nour's World" dreamy dark visual identity;
- warm purple/pink/blue accents;
- real Nour photo as an app asset/avatar when available;
- preserve image aspect ratio;
- do not send the profile photo to an AI service merely to display it;
- subject cards instead of a crowded tab wall;
- Quick Access for tools;
- clear persistent route back to Nour's World;
- Arabic-friendly UI with correct handling of English/LTR content;
- age-appropriate, polished, not childish.

## 19. Existing tools to preserve/improve

Current capabilities must not be accidentally lost during redesign:
- PDF curriculum/file companion;
- AI Buddy;
- problem-image helper;
- English helper;
- Escape Room;
- Python learning;
- goals/planner, including the useful motivational AI behavior from the original version.

Quick Access should expose tools; subject hubs should represent learning worlds.

## 20. Python / making things

Python is for creative computational literacy, not a heavy programming course.

Near term:
- explain small code;
- predict output;
- modify one thing;
- create tiny useful/fun programs.

Later:
- safe executable sandbox;
- small AI + Python projects.

Do not prioritize executable sandbox ahead of curriculum, English, AI literacy and persistence.

## 21. Persistence / database

Session state is prototype-only. Production learning progress must survive refreshes/restarts.

Persist at minimum:
- student profile/settings;
- XP/levels/badges/streak evidence;
- tasks;
- mastery;
- mistakes/reviews;
- English skill progress;
- AI skill progress;
- learning history needed for adaptation.

Use a simple, maintainable and low-cost architecture. Supabase is a candidate, not an automatic requirement; choose after architecture review.

## 22. Privacy, access and cost control

- Never commit API keys/secrets.
- Keep Gemini/API credentials in protected secrets/environment configuration.
- Add lightweight access protection (PIN/password or appropriate auth) to protect private progress and API usage.
- Minimize unnecessary model calls and large-file resends.
- Nour's profile image should not be sent to external AI services unless a future feature explicitly requires it and that use is approved.
- Prefer free/low-cost solutions where they meet quality and reliability needs.

## 23. Knowledge architecture

Target direction:
1. ingest approved curriculum files;
2. extract and organize metadata/content;
3. map subject/term/unit/lesson/concept;
4. index for targeted retrieval;
5. retrieve the smallest useful curriculum evidence;
6. ask the AI to teach using that evidence;
7. record learning evidence separately from source documents.

Do not build a vector database merely because it is fashionable. Validate the corpus and retrieval needs first.

## 24. Quality / testing

Before main-branch merge:
- syntax/static checks;
- feature-parity review;
- mobile visual test;
- key user-flow test;
- Gemini failure/missing-key behavior;
- no secret leakage;
- no accidental loss of existing features;
- curriculum-grounding checks once sources are integrated.

Prefer a real browser verification when available rather than claiming a UI works from syntax alone.

## 25. Current implementation gaps

The current feature-branch foundation is intentionally incomplete:
- only four subject cards are shown;
- subject cards are placeholders;
- XP, streak and level are session/demo values;
- Daily Mission is self-reported;
- no database/persistence;
- no Mastery Map;
- no Mistake Notebook;
- no adaptive Tutor Profile;
- no Parent Dashboard;
- no AI Lab;
- no real curriculum knowledge base;
- no Nour photo asset yet;
- no speech/listening/pronunciation system;
- no real subject navigation;
- the original planner's motivational AI behavior must be restored before claiming strict feature parity.

## 26. Implementation priority

### Foundation
- lock this requirements document;
- inspect current curriculum sources when upload completes;
- audit existing feature branch against this document;
- restore feature parity;
- complete mobile navigation and seven subject presentation cards.

### Learning core
- curriculum map and retrieval architecture;
- persistent database;
- Mastery Map;
- Mistake Notebook + spaced repetition;
- Tutor Profile;
- Teach Me / Homework Coach / Exam Mode.

### Strategic experiences
- English Adventure;
- AI Lab / AI Explorer;
- meaningful Daily Mission and Weekly Smart Plan;
- real gamification;
- Parent Dashboard.

### Expansion
- listening/speaking/pronunciation;
- richer adventures;
- safe executable Python;
- AI + Python projects.

## 27. Change-control rule

New ideas are welcome, but they should be evaluated against:
1. Does it improve Nour's learning, English, AI literacy or healthy engagement?
2. Is it appropriate for her age/current curriculum?
3. Does it add unnecessary cost/complexity?
4. Can its learning benefit be measured?
5. Does it preserve privacy and safety?

This document should be updated when an important product decision is approved, so future chats and implementation work do not lose the project's intent.
