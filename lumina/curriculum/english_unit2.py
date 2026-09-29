from lumina.learning.lesson_models import LessonCheck, LessonData


ENGLISH_U2_L1 = LessonData(
    id="english_u2_l1",
    source_id="english_prep3_t1",
    unit_id="u2",
    title="Stay Connected",
    source_pages="Book pages 28–29",
    objectives=(
        "Understand the main idea and details in a reading about strong communication.",
        "Recognize communication vocabulary from context.",
        "Discuss how listening, honesty, and respectful conversation strengthen relationships.",
    ),
    key_terms=("communicate", "misunderstanding", "bond", "supportive", "resolve", "siblings", "respectful"),
    evidence_summary=(
        "The reading explains that communication includes tone of voice, facial expressions, body language, and words.",
        "Messages can be misunderstood, while open and respectful conversation can solve problems and build trust.",
        "Honesty, listening, and understanding another person's point of view help strengthen relationships.",
    ),
    checks=(
        LessonCheck(
            id="strong_communication",
            prompt="Which action best matches the lesson's idea of strong communication?",
            expected_points=("honest respectful listening and talking",),
            hint="Think about what helps people solve problems and build trust.",
            options=(
                "Avoid the other person whenever there is a problem.",
                "Listen respectfully, speak honestly, and try to understand the other person's point of view.",
                "Send more messages without checking whether they were understood.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U2_L2 = LessonData(
    id="english_u2_l2",
    source_id="english_prep3_t1",
    unit_id="u2",
    title="Communication, Challenges and Solutions",
    source_pages="Book pages 30–31",
    objectives=(
        "Listen for key ideas about misunderstandings and problem solving.",
        "Discuss communication problems and possible solutions.",
        "Use the Third Conditional to talk about unreal past situations and their imagined results.",
    ),
    key_terms=("misunderstanding", "face-to-face", "calm", "Third Conditional", "regret", "past perfect"),
    evidence_summary=(
        "The listening/speaking tasks focus on misunderstandings and solving problems through communication.",
        "The lesson emphasizes listening, honesty, and staying calm.",
        "The Third Conditional is used for an imaginary past condition and result that did not actually happen, and can express regret or imagined alternatives.",
    ),
    checks=(
        LessonCheck(
            id="third_conditional",
            prompt="Which sentence correctly uses the Third Conditional idea from the lesson?",
            expected_points=("if plus past perfect and would have plus past participle",),
            hint="The lesson talks about an unreal past situation and an imagined past result.",
            options=(
                "If I study hard, I will pass the exam.",
                "If I had studied harder, I would have passed the exam.",
                "If I studied hard, I would pass the exam.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U2_L3 = LessonData(
    id="english_u2_l3",
    source_id="english_prep3_t1",
    unit_id="u2",
    title="The Silent Dinner",
    source_pages="Book pages 32–33",
    objectives=(
        "Read a family story and identify the problem, turning point, and lesson.",
        "Understand how a small act of communication can reconnect people.",
        "Use communication vocabulary in context.",
    ),
    key_terms=("distraction", "frustrated", "gesture", "meaningful", "reconnect", "silence"),
    evidence_summary=(
        "Omar notices that his family has become quiet and distant during dinner.",
        "He honestly says that he misses how they used to talk, which becomes a small but meaningful act of communication.",
        "The family begins reconnecting by talking, listening, sharing jokes, and reducing distractions.",
    ),
    checks=(
        LessonCheck(
            id="turning_point",
            prompt="What starts the positive change in Omar's family?",
            expected_points=("Omar honestly says he misses how they used to talk",),
            hint="Look for the small action that breaks the silence.",
            options=(
                "They buy new phones.",
                "Omar honestly says he misses how they used to talk together.",
                "They stop eating dinner together.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U2_L4 = LessonData(
    id="english_u2_l4",
    source_id="english_prep3_t1",
    unit_id="u2",
    title="Story Time — Taking Initiative and Building a Team",
    source_pages="Book pages 34–35",
    objectives=(
        "Read the second chapter of The School Garden Project.",
        "Understand initiative, courage, determination, and teamwork.",
        "Identify how different people's talents can contribute to a shared project.",
    ),
    key_terms=("research", "courage", "talent", "proposal", "determination", "shared", "deserves"),
    evidence_summary=(
        "Zeina researches her garden idea and writes a simple proposal before speaking at the student council.",
        "She continues despite classmates laughing at her idea.",
        "A teacher supports her, and different students contribute different talents, turning the garden into a shared project.",
    ),
    checks=(
        LessonCheck(
            id="teamwork_message",
            prompt="Why does the garden become a shared project?",
            expected_points=("different students contribute their talents and help",),
            hint="Think about what Nancy, Noha, Amal, and Sara each bring to the idea.",
            options=(
                "Zeina refuses to let anyone else help.",
                "Different students contribute their talents and work together.",
                "The project succeeds without planning or support.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U2_L5 = LessonData(
    id="english_u2_l5",
    source_id="english_prep3_t1",
    unit_id="u2",
    title="Let's Talk — Proper Communication Skills",
    source_pages="Book pages 36–37",
    objectives=(
        "Practice conversations about misunderstandings and repairing relationships.",
        "Use friendly conversational phrases to show agreement, understanding, and support.",
        "Apply listening-before-speaking as a communication strategy.",
    ),
    key_terms=("That's cool", "I totally get that", "For sure", "Honestly", "Right?", "Absolutely"),
    evidence_summary=(
        "The model conversation shows two people discussing a misunderstanding honestly and calmly.",
        "The lesson recommends listening carefully before answering so people feel heard and valued.",
        "Role-play practice uses conversational phrases to keep communication natural and supportive.",
    ),
    checks=(
        LessonCheck(
            id="listen_first",
            prompt="Which habit best matches the lesson's communication tip?",
            expected_points=("listen carefully before answering",),
            hint="The tip says good conversation is not only about speaking.",
            options=(
                "Prepare your reply while the other person is still talking.",
                "Listen carefully before answering so the other person feels heard.",
                "Avoid discussing misunderstandings.",
            ),
            correct_index=1,
        ),
    ),
)


ENGLISH_U2_L6 = LessonData(
    id="english_u2_l6",
    source_id="english_prep3_t1",
    unit_id="u2",
    title="Staying Close — Opinion Paragraph",
    source_pages="Book pages 38–40",
    objectives=(
        "Write an opinion paragraph about the importance of communication.",
        "Organize writing with an introduction/opinion, explanation, personal feelings/thoughts, lesson learned, and closing sentence.",
        "Use target communication vocabulary and Third Conditional language where appropriate.",
        "Reflect on reading, listening, speaking, writing, and life-skills progress.",
    ),
    key_terms=("communication", "connection", "face-to-face", "calm", "misunderstand", "honest", "listen", "supportive", "resolve", "courage", "meaningful", "determination"),
    evidence_summary=(
        "The writing task asks for an opinion paragraph about the importance of communication.",
        "The model structure includes an introduction/opinion, explanation of what happened, personal feelings/thoughts, a lesson learned, and a closing sentence.",
        "The assessment reviews communication vocabulary, the Third Conditional, and paragraph writing.",
        "The self-reflection section asks learners to evaluate reading, listening, speaking, writing, and life-skills outcomes.",
    ),
    checks=(
        LessonCheck(
            id="opinion_structure",
            prompt="Which sequence best matches the opinion-paragraph structure shown in the lesson?",
            expected_points=("opinion then explanation then feelings then lesson learned then closing",),
            hint="Follow the Helpful Hints box from the beginning of the paragraph to the end.",
            options=(
                "Closing → Opinion → Example → Title",
                "Opinion/Introduction → Explanation → Feelings/Thoughts → Lesson Learned → Closing",
                "Question → Dialogue → Vocabulary List → Closing",
            ),
            correct_index=1,
        ),
    ),
)


UNIT2_LESSONS = (
    ENGLISH_U2_L1,
    ENGLISH_U2_L2,
    ENGLISH_U2_L3,
    ENGLISH_U2_L4,
    ENGLISH_U2_L5,
    ENGLISH_U2_L6,
)
