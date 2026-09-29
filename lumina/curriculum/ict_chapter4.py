from lumina.learning.lesson_models import LessonCheck, LessonData


ICT_C4_L1 = LessonData(
    id="ict_c4_l1",
    source_id="ict_prep3_t2",
    unit_id="c4",
    title="Cyber Bullying",
    source_pages="PDF pages 60–64",
    objectives=(
        "Define cyber bullying and recognize common forms.",
        "Identify electronic media through which cyber bullying can occur.",
        "Follow safe-response rules when exposed to cyber bullying.",
        "Know when to seek help from trusted adults or responsible organizations.",
    ),
    key_terms=("cyber bullying", "harassment", "cyber stalking", "flaming", "outing", "exclusion", "cyber threats", "privacy"),
    evidence_summary=(
        "The chapter defines cyber bullying as deliberate aggressive behaviour through electronic communication.",
        "Forms include harassment, cyber stalking, flaming, outing, exclusion, threats, intimidation, and blackmailing.",
        "Safety guidance includes not sharing passwords, choosing strong passwords, protecting private data, preserving abusive messages as evidence, avoiding meetings with online strangers, and seeking help from trusted adults.",
        "The chapter also advises not sending messages while angry and not downloading unknown software without guidance.",
    ),
    checks=(
        LessonCheck(
            id="preserve_evidence",
            prompt="If someone sends a threatening cyber-bullying message, what does the chapter advise?",
            expected_points=("do not delete it; preserve it as evidence and seek help",),
            hint="The chapter gives an example of a student who deleted an abusive message.",
            options=(
                "Delete it immediately so nobody can see it.",
                "Keep it as evidence and tell a trusted adult or teacher.",
                "Reply angrily with another threat.",
            ),
            correct_index=1,
        ),
        LessonCheck(
            id="password_safety",
            prompt="Which password habit matches the chapter's safe-use rules?",
            expected_points=("use a difficult password and do not share it",),
            hint="Think about the examples involving Amr and Yasmeen.",
            options=(
                "Share your password with friends when they need your account.",
                "Use a strong password and keep it private.",
                "Use your name and birth year because they are easy to remember.",
            ),
            correct_index=1,
        ),
    ),
)

ICT_CHAPTER4_LESSONS = (ICT_C4_L1,)
