from lumina.learning.lesson_models import LessonCheck, LessonData


ENGLISH_U1_L1 = LessonData(
    id="english_u1_l1",
    source_id="english_prep3_t1",
    unit_id="u1",
    title="Beyond My Looks",
    source_pages="Book pages 14–15",
    objectives=(
        "Understand personal identity as more than appearance.",
        "Identify details and values in a short reading text.",
        "Use key personal-identity vocabulary in context.",
        "Talk about what makes a person different and unique.",
    ),
    key_terms=(
        "background",
        "identity",
        "self-discovery",
        "value",
        "confidence",
        "strength",
        "stressed",
    ),
    evidence_summary=(
        "The reading presents Ahmed, who explains that identity is about who a person really is inside, not only how they look or how others see them.",
        "Ahmed links his background with values such as hard work and kindness.",
        "The text describes pressure from social media and the idea that being real matters more than being popular.",
        "Self-discovery helps Ahmed become more confident, accept what makes him unique, and rely on inner strength and self-respect.",
        "The lesson asks learners to connect identity with opinions, values, confidence, and what makes people different.",
    ),
    checks=(
        LessonCheck(
            id="identity_core",
            prompt="According to the lesson, is personal identity mainly about appearance? Explain in one or two sentences.",
            expected_points=("not mainly appearance", "who you are inside", "values or personal qualities"),
            hint="Think about what Ahmed says matters more than how other people see him.",
        ),
        LessonCheck(
            id="social_media",
            prompt="What pressure does Ahmed feel from social media, and what idea helps him deal with it?",
            expected_points=("pressure to change how he looks or dresses", "being real matters more than being popular"),
            hint="Look for the contrast between changing yourself and being real.",
        ),
    ),
)
