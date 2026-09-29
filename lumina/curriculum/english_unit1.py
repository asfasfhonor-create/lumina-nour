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
    key_terms=("background", "identity", "self-discovery", "value", "confidence", "strength", "stressed"),
    evidence_summary=(
        "Ahmed explains that identity is about who a person really is inside, not only how they look or how others see them.",
        "Ahmed links his background with values such as hard work and kindness.",
        "The reading contrasts social-media pressure with the idea that being real matters more than being popular.",
        "Self-discovery helps Ahmed become more confident, accept what makes him unique, and rely on inner strength and self-respect.",
    ),
    checks=(
        LessonCheck(
            id="identity_core",
            prompt="Which idea best matches Ahmed's message in the lesson?",
            expected_points=("identity includes inner qualities and values, not only appearance or popularity",),
            hint="Think about what Ahmed says matters more than how other people see him.",
            options=(
                "Your appearance is the most important part of your identity.",
                "Who you are includes your values and inner qualities, not just looks or popularity.",
                "Being popular on social media is the best way to build confidence.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U1_L2 = LessonData(
    id="english_u1_l2",
    source_id="english_prep3_t1",
    unit_id="u1",
    title="Self-Discovery",
    source_pages="Book pages 16–17",
    objectives=(
        "Listen for main ideas and details about identity and personal growth.",
        "Talk about qualities and values that make a good person.",
        "Use the present perfect in active and passive forms.",
    ),
    key_terms=("support", "growth", "individuality", "confidence", "present perfect", "active", "passive"),
    evidence_summary=(
        "The lesson connects personal experiences and support from others with self-discovery and confidence.",
        "Speaking tasks ask students to identify qualities and values that make a good person.",
        "The language focus is the present perfect tense in active and passive forms, including unfinished/recent actions and life experiences.",
    ),
    checks=(
        LessonCheck(
            id="present_perfect_meaning",
            prompt="Which sentence best fits the lesson's present perfect focus?",
            expected_points=("present perfect can describe a life experience or an action connected to the present",),
            hint="Think about experiences and actions that matter now.",
            options=(
                "I visited Alexandria yesterday at 5 p.m.",
                "I have never been to Aswan.",
                "I will visit Aswan next year.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U1_L3 = LessonData(
    id="english_u1_l3",
    source_id="english_prep3_t1",
    unit_id="u1",
    title="The Mirror Moment",
    source_pages="Book pages 18–19",
    objectives=(
        "Read a narrative about identity and self-expression.",
        "Infer feelings and motives from events in the text.",
        "Use vocabulary related to identity, values, and change.",
    ),
    key_terms=("curious", "values", "adjusting", "confident", "identity map", "self-respect"),
    evidence_summary=(
        "Nour initially tries to fit in and worries about how others see her.",
        "A class identity-map project helps her express who she is through dreams, values, and challenges.",
        "The story shows a shift from hiding differences to becoming more confident and authentic.",
    ),
    checks=(
        LessonCheck(
            id="nour_change",
            prompt="What is the most important change Nour makes in the story?",
            expected_points=("she becomes more confident about her real identity",),
            hint="Compare how she behaves at the beginning with how she presents herself later.",
            options=(
                "She decides to copy other students more closely.",
                "She becomes more confident about showing who she really is.",
                "She stops caring about her school work.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U1_L4 = LessonData(
    id="english_u1_l4",
    source_id="english_prep3_t1",
    unit_id="u1",
    title="Story Time — The School Garden Project",
    source_pages="Book pages 20–21",
    objectives=(
        "Read a story chapter and identify main ideas and details.",
        "Understand how initiative, honesty, and small actions can influence a community.",
        "Use story vocabulary in context and answer critical-thinking questions.",
    ),
    key_terms=("worth", "proud", "depressing", "honest", "challenge", "initiative"),
    evidence_summary=(
        "Zeina is new at school and notices a dull, empty playground.",
        "She suggests planting a garden even though others doubt the idea.",
        "Her idea becomes an example of how a small action can help improve a school community.",
        "The follow-up tasks focus on honesty, persistence, community change, and critical thinking.",
    ),
    checks=(
        LessonCheck(
            id="garden_message",
            prompt="What is the strongest message of this chapter?",
            expected_points=("small honest actions and initiative can create positive community change",),
            hint="Think about why Zeina keeps the garden idea even when it seems difficult.",
            options=(
                "Only adults can improve a school community.",
                "Small honest actions and initiative can lead to positive change.",
                "It is better to avoid difficult ideas.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U1_L5 = LessonData(
    id="english_u1_l5",
    source_id="english_prep3_t1",
    unit_id="u1",
    title="Let's Talk — Respecting Personal Identity",
    source_pages="Book pages 22–23",
    objectives=(
        "Discuss personal identity respectfully in conversation.",
        "Use supportive and positive conversational language.",
        "Role-play conversations about challenges, self-respect, confidence, and honesty.",
    ),
    key_terms=("self-respect", "confidence", "support", "honesty", "respect", "supportive language"),
    evidence_summary=(
        "The dialogue links self-discovery with confidence and self-respect.",
        "Students discuss how respect, support, and honesty help people feel accepted.",
        "The role-play section practices positive language that shows interest and support.",
    ),
    checks=(
        LessonCheck(
            id="supportive_language",
            prompt="Which response best shows the supportive conversation style taught in the lesson?",
            expected_points=("positive supportive language",),
            hint="Choose the reply that helps the other person feel heard and encouraged.",
            options=(
                "That's not important. Forget it.",
                "That's great. You've shown a lot of strength.",
                "You should just copy what everyone else does.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U1_L6 = LessonData(
    id="english_u1_l6",
    source_id="english_prep3_t1",
    unit_id="u1",
    title="This Is Me — Descriptive Paragraph",
    source_pages="Book pages 24–26",
    objectives=(
        "Plan and write a descriptive paragraph about values and identity.",
        "Use present perfect active/passive and target vocabulary where appropriate.",
        "Organize writing with a topic sentence, explanation, evidence/example, and ending sentence.",
        "Reflect on listening, speaking, reading, writing, vocabulary, language, life skills, and values.",
    ),
    key_terms=("background", "popular", "self-discovery", "unique", "value", "confident", "strong", "honesty", "honest"),
    evidence_summary=(
        "The writing model explains that a descriptive paragraph should include a clear topic sentence, explanation, evidence/example, and ending sentence.",
        "The task asks students to write about values they stand for and explain how those values appear in their actions.",
        "The unit assessment reviews vocabulary, present perfect language, and descriptive writing.",
        "The self-reflection checklist asks students to review progress across listening, speaking, reading, writing, vocabulary, language, and life skills/values.",
    ),
    checks=(
        LessonCheck(
            id="paragraph_structure",
            prompt="Which order best matches the paragraph structure shown in the lesson?",
            expected_points=("topic sentence, explanation, evidence/example, ending sentence",),
            hint="Look for the four-part structure in the model paragraph.",
            options=(
                "Evidence → Ending → Topic sentence → Explanation",
                "Topic sentence → Explanation → Evidence/Example → Ending sentence",
                "Title → Question → Dialogue → Ending sentence",
            ),
            correct_index=1,
        ),
    ),
)


UNIT1_LESSONS = (
    ENGLISH_U1_L1,
    ENGLISH_U1_L2,
    ENGLISH_U1_L3,
    ENGLISH_U1_L4,
    ENGLISH_U1_L5,
    ENGLISH_U1_L6,
)


def get_unit1_lesson(lesson_id: str) -> LessonData | None:
    return next((lesson for lesson in UNIT1_LESSONS if lesson.id == lesson_id), None)
