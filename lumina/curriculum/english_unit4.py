from lumina.learning.lesson_models import LessonCheck, LessonData


ENGLISH_U4_L1 = LessonData(
    id="english_u4_l1",
    source_id="english_prep3_t1",
    unit_id="u4",
    title="Screen Time",
    source_pages="Book pages 60–61",
    objectives=(
        "Understand useful and harmful forms of screen time.",
        "Explain why balance and breaks matter.",
        "Discuss healthy alternatives to excessive screen use.",
    ),
    key_terms=("screen time", "entertainment", "balance", "physical", "mentally", "side effects"),
    evidence_summary=(
        "The reading distinguishes useful screen time from unhelpful entertainment screen time.",
        "It warns that too much screen use can affect sleep, eyes, headaches, focus, stress, and physical activity.",
        "The lesson encourages balancing screen use with other healthy activities and regular breaks.",
    ),
    checks=(
        LessonCheck(
            id="screen_balance",
            prompt="Which habit best matches the lesson's advice about screen time?",
            expected_points=("balance screen use with breaks and other healthy activities",),
            hint="The reading does not say all screen time is bad; it focuses on balance.",
            options=(
                "Avoid every screen completely.",
                "Balance useful screen time with breaks and other healthy activities.",
                "Use screens for entertainment as long as possible.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U4_L2 = LessonData(
    id="english_u4_l2",
    source_id="english_prep3_t1",
    unit_id="u4",
    title="Egypt's Smart Future",
    source_pages="Book pages 62–63",
    objectives=(
        "Listen for main ideas about smart habits and Egypt's future.",
        "Discuss modern technology and responsible technology use.",
        "Use modal verbs and connectors accurately.",
    ),
    key_terms=("smart", "focused", "modern", "distraction", "must", "can", "should", "while", "although", "even though"),
    evidence_summary=(
        "The listening/speaking tasks connect smart habits, technology, and Egypt's future.",
        "The language section practices modal verbs for obligation, ability, advice, permission, and prohibition.",
        "The lesson also practices connectors such as while, although, and even though for contrast.",
    ),
    checks=(
        LessonCheck(
            id="modal_advice",
            prompt="Which sentence gives advice using the modal pattern from the lesson?",
            expected_points=("should for advice",),
            hint="The tip box uses should / shouldn't for advice.",
            options=(
                "You should limit your screen time.",
                "You mustn't can use your phone.",
                "You will should rest.",
            ),
            correct_index=0,
        ),
    ),
)

ENGLISH_U4_L3 = LessonData(
    id="english_u4_l3",
    source_id="english_prep3_t1",
    unit_id="u4",
    title="Balancing Screen Time",
    source_pages="Book page 64",
    objectives=(
        "Read about changing screen habits and setting a realistic plan.",
        "Identify a problem, goal, and practical steps in a personal plan.",
        "Reflect on how screen habits affect sleep, stress, study, and free time.",
    ),
    key_terms=("screen time report", "notification", "stressed", "control", "habit"),
    evidence_summary=(
        "The writer notices almost six hours of daily phone use and decides to change.",
        "The plan includes limiting phone use, turning off social-media notifications, keeping the phone away while studying, reading before bed, and spending more time outside and with friends.",
        "The intended outcome is better sleep, less stress, and greater control of time.",
    ),
    checks=(
        LessonCheck(
            id="practical_plan",
            prompt="Which action is part of the writer's plan to balance screen time?",
            expected_points=("turn off notifications or keep phone away while studying or limit use",),
            hint="Look for a concrete change the writer plans to make.",
            options=(
                "Keep every notification on while studying.",
                "Turn off social-media notifications and keep the phone away while studying.",
                "Use the phone more before bed.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U4_L4 = LessonData(
    id="english_u4_l4",
    source_id="english_prep3_t1",
    unit_id="u4",
    title="Story Time — Growing Success",
    source_pages="Book pages 65–66",
    objectives=(
        "Read the fourth chapter of The School Garden Project.",
        "Understand leadership as responsibility for both success and mistakes.",
        "Recognize global responsibility and eco-friendly choices.",
    ),
    key_terms=("leader", "eco-friendly", "global responsibility", "blame", "natural fertilizers"),
    evidence_summary=(
        "The garden succeeds after months of work and begins benefiting the school community.",
        "Zeina learns that leadership means responsibility for both successes and mistakes instead of blaming others.",
        "The students use eco-friendly methods such as natural fertilizers and connect the project with wider environmental responsibility.",
    ),
    checks=(
        LessonCheck(
            id="leadership",
            prompt="What does leadership mean in this chapter?",
            expected_points=("being responsible for success and mistakes",),
            hint="Zeina learns not to blame others when something goes wrong.",
            options=(
                "Taking credit only when things go well.",
                "Being responsible for both successes and mistakes.",
                "Avoiding difficult decisions.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U4_L5 = LessonData(
    id="english_u4_l5",
    source_id="english_prep3_t1",
    unit_id="u4",
    title="Let's Talk — Balancing Screen Time",
    source_pages="Book pages 67–68",
    objectives=(
        "Discuss practical ways to balance screen time and other activities.",
        "Use modal verbs to make advice friendly and clear.",
        "Use connectors to make spoken ideas smoother.",
    ),
    key_terms=("balance", "notifications", "distraction", "should", "could", "must", "but", "so", "also"),
    evidence_summary=(
        "The dialogue focuses on balancing screens used for study and entertainment with outdoor activities, reading, and sleep.",
        "Practical suggestions include setting times, avoiding screens during meals or before bedtime, and turning off notifications.",
        "The lesson encourages polite modal verbs and connectors in conversation.",
    ),
    checks=(
        LessonCheck(
            id="friendly_advice",
            prompt="Which sentence gives friendly advice in the style of the lesson?",
            expected_points=("modal verb used politely for advice",),
            hint="The Real-Talk Tip recommends modal verbs such as should and could.",
            options=(
                "You should take breaks from the screen.",
                "You screen now!",
                "You are must take breaks.",
            ),
            correct_index=0,
        ),
    ),
)

ENGLISH_U4_L6 = LessonData(
    id="english_u4_l6",
    source_id="english_prep3_t1",
    unit_id="u4",
    title="Small Change — Blog Post",
    source_pages="Book pages 69–71",
    objectives=(
        "Write a blog post about improving screen-time habits.",
        "Use modal verbs and target vocabulary in meaningful writing.",
        "Review the unit's reading, listening, speaking, writing, vocabulary, and language outcomes.",
    ),
    key_terms=("screen time", "develop", "smart", "waste", "scrolling", "reduce", "plan", "change", "control", "useful"),
    evidence_summary=(
        "The writing task asks learners to write a blog post about how to improve screen-time habits.",
        "The model connects personal reflection, goals, Egyptian history/culture content, and a plan to reduce online time.",
        "The unit assessment reviews vocabulary, modal verbs, and writing about screen-time habits.",
        "Self-reflection covers reading, listening, speaking, writing, vocabulary, and language goals.",
    ),
    checks=(
        LessonCheck(
            id="blog_goal",
            prompt="What should a useful screen-time blog post include according to the lesson?",
            expected_points=("a clear personal goal and practical changes",),
            hint="Look at the model's plan and the Your task prompt.",
            options=(
                "Only a list of apps.",
                "A clear goal and practical changes to improve screen-time habits.",
                "Only a definition of technology.",
            ),
            correct_index=1,
        ),
    ),
)

UNIT4_LESSONS = (
    ENGLISH_U4_L1,
    ENGLISH_U4_L2,
    ENGLISH_U4_L3,
    ENGLISH_U4_L4,
    ENGLISH_U4_L5,
    ENGLISH_U4_L6,
)
