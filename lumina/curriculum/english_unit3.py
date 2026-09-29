from lumina.learning.lesson_models import LessonCheck, LessonData


ENGLISH_U3_L1 = LessonData(
    id="english_u3_l1",
    source_id="english_prep3_t1",
    unit_id="u3",
    title="Artificial Intelligence",
    source_pages="Book pages 42–43",
    objectives=(
        "Understand the difference between robots and Artificial Intelligence.",
        "Identify examples of AI use and its limits.",
        "Discuss whether robots can replace humans in different roles.",
    ),
    key_terms=("robot", "Artificial Intelligence", "behavior", "advanced", "limits", "tasks"),
    evidence_summary=(
        "The reading explains that robots and AI are not the same thing.",
        "AI is described as the 'brain' that can allow a robot to learn from actions and change its behavior.",
        "Robots with AI can be used in hospitals, schools, and other settings.",
        "The lesson also states limits: AI/robots do not truly understand emotions and still need human help or programming.",
    ),
    checks=(
        LessonCheck(
            id="robot_vs_ai",
            prompt="Which statement best matches the reading?",
            expected_points=("a robot is a machine while ai is the intelligence that can help it learn and change behavior",),
            hint="The text says a robot is a machine, while AI acts more like the 'brain'.",
            options=(
                "Robot and AI always mean exactly the same thing.",
                "A robot is a machine, while AI can act like the intelligence that helps it learn and change behavior.",
                "AI can only be used in factories.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U3_L2 = LessonData(
    id="english_u3_l2",
    source_id="english_prep3_t1",
    unit_id="u3",
    title="AI Technology",
    source_pages="Book pages 44–45",
    objectives=(
        "Listen for ideas about AI technology and innovation.",
        "Discuss useful and risky applications of AI.",
        "Use the Future Simple Passive to describe future actions.",
    ),
    key_terms=("innovation", "compose", "creative", "Future Simple Passive", "will be", "technology"),
    evidence_summary=(
        "The lesson explores AI technology, innovation, creativity, and possible future uses.",
        "Speaking tasks ask learners to discuss fields where AI can be used and whether it will become smarter than humans.",
        "The language focus is Future Simple Passive, formed with will be plus the past participle.",
    ),
    checks=(
        LessonCheck(
            id="future_passive",
            prompt="Which sentence correctly uses the Future Simple Passive?",
            expected_points=("will be plus past participle",),
            hint="The form in the lesson is will be + past participle.",
            options=(
                "The homework will check tomorrow.",
                "The homework will be checked tomorrow.",
                "The homework checked tomorrow.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U3_L3 = LessonData(
    id="english_u3_l3",
    source_id="english_prep3_t1",
    unit_id="u3",
    title="A Robot Teacher",
    source_pages="Book pages 46–47",
    objectives=(
        "Read a story about an AI robot teacher and identify benefits and limits.",
        "Compare technology with human teachers.",
        "Discuss whether AI may change jobs in the future.",
    ),
    key_terms=("customize", "connection", "instantly", "confused", "notice"),
    evidence_summary=(
        "The robot teacher adapts practice for different students and gives fast feedback.",
        "Students improve, but they miss the care and human connection of their real teacher.",
        "The story suggests AI can support learning but may not fully replace a real teacher.",
    ),
    checks=(
        LessonCheck(
            id="teacher_limit",
            prompt="What does the story suggest the robot teacher cannot fully replace?",
            expected_points=("human care and connection",),
            hint="Think about what the students missed even though the robot helped them improve.",
            options=(
                "Homework practice.",
                "Human care and connection.",
                "Fast feedback.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U3_L4 = LessonData(
    id="english_u3_l4",
    source_id="english_prep3_t1",
    unit_id="u3",
    title="Story Time — Facing Problems with Determination",
    source_pages="Book pages 48–49",
    objectives=(
        "Read the third chapter of The School Garden Project.",
        "Understand how initiative and determination help solve problems.",
        "Identify how a team responds to setbacks.",
    ),
    key_terms=("initiative", "donations", "quit", "climate", "disappointed", "determination"),
    evidence_summary=(
        "The garden team faces problems including money, heavy rain, and damaged plants.",
        "Zeina asks the local community for donations and encourages the team not to give up.",
        "The group works together, researches suitable plants, rebuilds, and learns from the setbacks.",
    ),
    checks=(
        LessonCheck(
            id="determination",
            prompt="Which action best shows Zeina's determination?",
            expected_points=("she keeps working on the project and looks for solutions instead of quitting",),
            hint="Look at what she does after the team faces money and weather problems.",
            options=(
                "She quits after the first problem.",
                "She looks for solutions and encourages the team to keep going.",
                "She leaves the project for another group.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U3_L5 = LessonData(
    id="english_u3_l5",
    source_id="english_prep3_t1",
    unit_id="u3",
    title="Let's Talk — Talking About AI",
    source_pages="Book pages 50–51",
    objectives=(
        "Discuss future uses and limits of AI.",
        "Ask open-ended questions to keep a conversation going.",
        "Practice Future Simple forms while talking about AI and technology.",
    ),
    key_terms=("future", "limits", "controlled", "open-ended questions", "will", "will be"),
    evidence_summary=(
        "The dialogue discusses AI becoming more advanced, future uses, limits, and the importance of human control.",
        "The conversation tip recommends open-ended questions such as how, why, and what to encourage deeper discussion.",
        "Role-play practice uses future language while discussing AI's effect on homes, schools, and daily life.",
    ),
    checks=(
        LessonCheck(
            id="open_question",
            prompt="Which question best follows the lesson's open-ended conversation tip?",
            expected_points=("open ended question invites explanation",),
            hint="Choose the question that cannot be answered with only yes or no.",
            options=(
                "Do you like AI?",
                "How do you think AI will help us in the future?",
                "Is AI useful?",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U3_L6 = LessonData(
    id="english_u3_l6",
    source_id="english_prep3_t1",
    unit_id="u3",
    title="Smart Robots — Email About AI",
    source_pages="Book pages 52–54",
    objectives=(
        "Write an email about the future benefits of AI.",
        "Use future language and AI vocabulary in meaningful writing.",
        "Review vocabulary, future forms, and unit learning outcomes.",
    ),
    key_terms=("Artificial Intelligence", "robots", "care", "check", "programs", "instant", "surgeries", "assist", "creativity", "humans", "technology"),
    evidence_summary=(
        "The writing model is an email about possible future uses and benefits of AI.",
        "The task asks learners to write about the benefits of AI in the future.",
        "The model also notes that AI should be controlled by humans and used creatively and safely.",
        "The assessment and self-reflection review vocabulary, future language, reading, listening, speaking, writing, and life skills.",
    ),
    checks=(
        LessonCheck(
            id="balanced_ai",
            prompt="Which idea best matches the unit's balanced view of AI?",
            expected_points=("ai can be useful but should remain under human control and has limits",),
            hint="The unit talks about benefits and limits together.",
            options=(
                "AI has no limits and should replace humans everywhere.",
                "AI can be useful, but it has limits and should remain under human control.",
                "AI has no useful role in daily life.",
            ),
            correct_index=1,
        ),
    ),
)


UNIT3_LESSONS = (
    ENGLISH_U3_L1,
    ENGLISH_U3_L2,
    ENGLISH_U3_L3,
    ENGLISH_U3_L4,
    ENGLISH_U3_L5,
    ENGLISH_U3_L6,
)
