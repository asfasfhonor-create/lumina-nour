from lumina.learning.lesson_models import LessonCheck, LessonData


ENGLISH_U6_L1 = LessonData(
    id="english_u6_l1",
    source_id="english_prep3_t1",
    unit_id="u6",
    title="The Power of Stories",
    source_pages="Book pages 86–87",
    objectives=(
        "Understand how stories can develop imagination, empathy, awareness, and critical thinking.",
        "Identify moral, social, and emotional lessons in stories.",
        "Discuss why reading stories can be useful beyond entertainment.",
    ),
    key_terms=("various", "moral", "empathy", "aware", "spark", "critically"),
    evidence_summary=(
        "The reading explains that stories help readers imagine different situations and points of view.",
        "Stories can help people understand emotions, social problems, and moral choices without living through every experience themselves.",
        "Reading stories can build empathy, awareness, imagination, and critical thinking.",
    ),
    checks=(
        LessonCheck(
            id="story_power",
            prompt="Which benefit best matches the lesson's message about stories?",
            expected_points=("stories help build empathy imagination awareness and critical thinking",),
            hint="The passage says stories are more than entertainment.",
            options=(
                "Stories are useful only because they are fun.",
                "Stories can build empathy, imagination, awareness, and critical thinking.",
                "Stories should avoid difficult problems.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U6_L2 = LessonData(
    id="english_u6_l2",
    source_id="english_prep3_t1",
    unit_id="u6",
    title="The Story That Helped Me",
    source_pages="Book pages 88–89",
    objectives=(
        "Listen to a conversation about learning from a story.",
        "Understand how stories can influence real-life behavior.",
        "Use reported statements accurately.",
    ),
    key_terms=("honestly", "unfair", "stuck", "debate", "recommendations", "reported statements"),
    evidence_summary=(
        "The listening text describes how a story helps a student stay calmer and more respectful during a debate.",
        "The lesson connects story lessons with real-life choices and behavior.",
        "The language focus is reported statements, including changes in pronouns, time expressions, and verb forms.",
    ),
    checks=(
        LessonCheck(
            id="reported_statement",
            prompt="Which sentence correctly reports: Sara said, 'I love reading stories.'?",
            expected_points=("Sara said that she loved reading stories",),
            hint="The lesson shows pronoun and tense changes in reported statements.",
            options=(
                "Sara said that she loved reading stories.",
                "Sara said that I love reading stories.",
                "Sara said she will loved reading stories.",
            ),
            correct_index=0,
        ),
    ),
)

ENGLISH_U6_L3 = LessonData(
    id="english_u6_l3",
    source_id="english_prep3_t1",
    unit_id="u6",
    title="Elements of a Story",
    source_pages="Book pages 90–91",
    objectives=(
        "Identify setting, characters, conflict, and solution in a story.",
        "Recognize different story types.",
        "Retell and plan stories using sequence words.",
    ),
    key_terms=("setting", "characters", "conflict", "solution", "fiction", "non-fiction", "folk tales", "adventure", "comic", "historical"),
    evidence_summary=(
        "The lesson explains four core story elements: setting, characters, conflict, and solution.",
        "It presents examples of story types such as fiction, non-fiction, folk tales, adventure, comic, and historical stories.",
        "Learners practice retelling and planning stories with a beginning, middle, and end.",
    ),
    checks=(
        LessonCheck(
            id="story_elements",
            prompt="Which set contains the four story elements highlighted in the lesson?",
            expected_points=("setting characters conflict solution",),
            hint="Look at the Story Elements tip box.",
            options=(
                "Setting, Characters, Conflict, Solution",
                "Title, Page, Picture, Author",
                "Beginning, Grammar, Vocabulary, Ending",
            ),
            correct_index=0,
        ),
    ),
)

ENGLISH_U6_L4 = LessonData(
    id="english_u6_l4",
    source_id="english_prep3_t1",
    unit_id="u6",
    title="Story Time — Looking Forward",
    source_pages="Book pages 92–93",
    objectives=(
        "Read the final chapter of The School Garden Project.",
        "Understand leadership, ambition, courage, and growth.",
        "Reflect on how small ideas can lead to larger changes.",
    ),
    key_terms=("ambition", "special", "symbol", "courage", "leadership", "growth"),
    evidence_summary=(
        "Zeina becomes student-council president and wants to help other students believe they can change their school and world.",
        "The chapter defines real leadership through listening, respect, determination, and helping others feel valued.",
        "The garden becomes a symbol of how small ideas can lead to larger changes.",
    ),
    checks=(
        LessonCheck(
            id="small_ideas",
            prompt="What does the garden symbolize in the final chapter?",
            expected_points=("small ideas can lead to big changes",),
            hint="The chapter title is Looking Forward and the ending reflects on the garden's wider meaning.",
            options=(
                "Only a place to grow vegetables.",
                "How small ideas can lead to bigger positive changes.",
                "A project that should never change.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U6_L5 = LessonData(
    id="english_u6_l5",
    source_id="english_prep3_t1",
    unit_id="u6",
    title="Let's Talk — The Power of Stories",
    source_pages="Book pages 94–95",
    objectives=(
        "Discuss why stories are powerful and memorable.",
        "Share personal examples and opinions clearly.",
        "Listen carefully and connect another person's story to your own ideas.",
    ),
    key_terms=("point of view", "conflict", "solution", "moral", "personal experience", "connection"),
    evidence_summary=(
        "The conversation explains that stories help people see different points of view and think about choices and actions.",
        "Stories can contain conflicts and solutions, teach lessons, and stay in memory because they carry deep messages.",
        "Conversation tips encourage sharing personal experiences and listening for connections to make discussion more meaningful.",
    ),
    checks=(
        LessonCheck(
            id="conversation_connection",
            prompt="What makes a story discussion more meaningful according to the conversation tips?",
            expected_points=("share personal experiences and listen for connections",),
            hint="The lesson encourages both sharing and careful listening.",
            options=(
                "Only repeat the plot.",
                "Share personal experiences and listen for connections to what others say.",
                "Avoid giving opinions.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U6_L6 = LessonData(
    id="english_u6_l6",
    source_id="english_prep3_t1",
    unit_id="u6",
    title="My Own Story",
    source_pages="Book pages 96–99",
    objectives=(
        "Plan and write a short story with a clear beginning, middle, and end.",
        "Use setting, characters, conflict, and solution.",
        "Use sequence words and accurate past forms in narrative writing.",
        "Review the unit's language, speaking, writing, and life-skills outcomes.",
    ),
    key_terms=("point of view", "conflict", "critically", "aware", "various", "respond", "calm", "beginning", "middle", "end"),
    evidence_summary=(
        "The writing section asks learners to choose an interesting title, plan the story, establish a setting and characters, introduce a conflict, and solve it with a clear ending.",
        "Sequence words help organize events, and past forms are used for storytelling.",
        "The assessment reviews vocabulary, past forms, speaking about reading benefits, and story understanding.",
        "Self-reflection includes reading, listening, speaking, writing, empathy, respect, teamwork, and problem solving.",
    ),
    checks=(
        LessonCheck(
            id="story_plan",
            prompt="Which plan best follows the story-writing guidance in the lesson?",
            expected_points=("setting and characters then conflict then solution and ending",),
            hint="Use the Writing a Story tip box.",
            options=(
                "Start with the solution, then add random events.",
                "Introduce setting and characters, create a conflict, then solve it with a clear ending.",
                "Write only dialogue with no problem or ending.",
            ),
            correct_index=1,
        ),
    ),
)

UNIT6_LESSONS = (
    ENGLISH_U6_L1,
    ENGLISH_U6_L2,
    ENGLISH_U6_L3,
    ENGLISH_U6_L4,
    ENGLISH_U6_L5,
    ENGLISH_U6_L6,
)
