from lumina.learning.lesson_models import LessonCheck, LessonData


ENGLISH_U5_L1 = LessonData(
    id="english_u5_l1",
    source_id="english_prep3_t1",
    unit_id="u5",
    title="Think Like a Designer",
    source_pages="Book pages 73–74",
    objectives=(
        "Understand design thinking as practical problem solving.",
        "Identify designer skills such as creativity, listening, curiosity, and empathy.",
        "Recognize prototypes and the need to explore different points of view.",
    ),
    key_terms=("designer", "prototype", "creativity", "curiosity", "empathy", "point of view", "problem"),
    evidence_summary=(
        "The reading presents designers as everyday problem-solvers who ask what people need and how things can be made better.",
        "Designers explore ideas from different points of view and test simple models called prototypes.",
        "Creativity, listening, curiosity, and empathy are presented as important design skills.",
    ),
    checks=(
        LessonCheck(
            id="designer_mindset",
            prompt="Which action best matches the designer mindset in the lesson?",
            expected_points=("understand people explore ideas and test prototypes",),
            hint="Think about people, needs, ideas, and testing.",
            options=(
                "Choose the first idea and never test it.",
                "Understand people's needs, explore ideas, and test a prototype.",
                "Focus only on making something look stylish.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U5_L2 = LessonData(
    id="english_u5_l2",
    source_id="english_prep3_t1",
    unit_id="u5",
    title="Dream It, Build It",
    source_pages="Book pages 75–76",
    objectives=(
        "Understand the main ideas of a design sprint and problem-solving steps.",
        "Use sequence adverbs to organize a process.",
        "Use imperatives accurately to give instructions.",
    ),
    key_terms=("practical", "sprint", "crazy", "ideation", "first", "next", "then", "finally", "imperative"),
    evidence_summary=(
        "The lesson presents a design sprint as a structured problem-solving process.",
        "Sequence adverbs organize steps such as defining the problem, brainstorming, building a prototype, and testing it.",
        "Imperatives are used to give positive or negative instructions.",
    ),
    checks=(
        LessonCheck(
            id="design_sequence",
            prompt="Which sequence best follows the design-sprint process shown in the lesson?",
            expected_points=("define brainstorm prototype test",),
            hint="Use the sequence words from first to finally.",
            options=(
                "Test → Brainstorm → Define → Prototype",
                "Define the problem → Brainstorm → Build a prototype → Test it",
                "Prototype → Finish → Ignore feedback",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U5_L3 = LessonData(
    id="english_u5_l3",
    source_id="english_prep3_t1",
    unit_id="u5",
    title="See through Their Eyes",
    source_pages="Book page 77",
    objectives=(
        "Read about empathy in design thinking.",
        "Understand how observing real users can reveal needs.",
        "Connect good design with real people and real feelings.",
    ),
    key_terms=("empathy", "observe", "welcome", "buddy plan", "users", "needs"),
    evidence_summary=(
        "Omar and his group try to help a new student feel welcome during break time.",
        "Instead of guessing, Omar observes a real new student and notices confusion about where to sit and what to do.",
        "The group creates a Welcome Buddy plan, and Omar learns that good design starts with real people and real feelings.",
    ),
    checks=(
        LessonCheck(
            id="empathy_design",
            prompt="Why does Omar observe a real new student before designing the solution?",
            expected_points=("to understand the student's real needs and feelings",),
            hint="The lesson title is 'See through Their Eyes'.",
            options=(
                "To copy another school's idea.",
                "To understand the student's real needs and feelings.",
                "To avoid talking to any students.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U5_L4 = LessonData(
    id="english_u5_l4",
    source_id="english_prep3_t1",
    unit_id="u5",
    title="Story Time — The Impact of Growth",
    source_pages="Book pages 78–79",
    objectives=(
        "Read the fifth chapter of The School Garden Project.",
        "Identify personal growth, honesty, leadership, and wider impact.",
        "Reflect on self-awareness and learning from strengths and weaknesses.",
    ),
    key_terms=("growth", "dedicated", "leadership", "honesty", "self-awareness", "personal growth"),
    evidence_summary=(
        "The garden becomes successful, but the chapter emphasizes changes in the students as much as changes in the garden.",
        "Students become more responsible and interested in the environment, while some discover new talents and future interests.",
        "Zeina learns that honest self-awareness about strengths and weaknesses helps build trust and leadership.",
    ),
    checks=(
        LessonCheck(
            id="growth_meaning",
            prompt="Why is the chapter called 'The Impact of Growth'?",
            expected_points=("growth happens in both the garden and the students",),
            hint="The text says the biggest change was not only in the garden.",
            options=(
                "Only the plants grew.",
                "Both the garden and the students changed and developed.",
                "The project stopped changing after it succeeded.",
            ),
            correct_index=1,
        ),
    ),
)

ENGLISH_U5_L5 = LessonData(
    id="english_u5_l5",
    source_id="english_prep3_t1",
    unit_id="u5",
    title="Let's Talk — Learning About Design Thinking",
    source_pages="Book pages 80–81",
    objectives=(
        "Explain design-thinking steps in conversation.",
        "Use questions and repeated key words to keep a conversation clear.",
        "Use design-thinking vocabulary naturally in discussion.",
    ),
    key_terms=("understand", "brainstorm", "prototype", "test", "improve", "process", "come up with", "make sense"),
    evidence_summary=(
        "The dialogue summarizes design thinking as understanding people, brainstorming ideas, making a prototype, testing it, and improving it.",
        "The conversation tips encourage asking questions to keep a conversation active and repeating important words to show listening and learning.",
        "Vocabulary practice reinforces the idea of a process and practical problem solving.",
    ),
    checks=(
        LessonCheck(
            id="process_summary",
            prompt="Which summary best matches the design-thinking process in the conversation?",
            expected_points=("understand brainstorm prototype test improve",),
            hint="Follow the steps Amir and Magdy discuss.",
            options=(
                "Understand → Brainstorm → Prototype → Test → Improve",
                "Prototype → Stop → Ignore users",
                "Brainstorm → Finish immediately",
            ),
            correct_index=0,
        ),
    ),
)

ENGLISH_U5_L6 = LessonData(
    id="english_u5_l6",
    source_id="english_prep3_t1",
    unit_id="u5",
    title="Try, Learn, and Improve",
    source_pages="Book pages 82–84",
    objectives=(
        "Write a review describing a group's design project.",
        "Use sequence adverbs to explain a problem-solving process.",
        "Review design-thinking vocabulary, language, and life-skills outcomes.",
    ),
    key_terms=("challenges", "define", "prototype", "solution", "brainstorm", "practical", "buddy", "sprint", "closely", "crazy", "confused"),
    evidence_summary=(
        "The writing model describes a project by moving from the problem to the proposed idea, testing, feedback, and improvement.",
        "The lesson asks learners to write a review of a group's design project using sequence adverbs.",
        "Assessment reviews vocabulary, imperatives, and writing about design thinking.",
        "Self-reflection includes reading, listening, speaking, writing, creativity, teamwork, and initiative.",
    ),
    checks=(
        LessonCheck(
            id="iteration",
            prompt="What should happen if a prototype does not work well?",
            expected_points=("use feedback and improve or change the design",),
            hint="The lesson title includes Try, Learn, and Improve.",
            options=(
                "Hide the result and stop.",
                "Use feedback to improve or change the design.",
                "Never test the prototype again.",
            ),
            correct_index=1,
        ),
    ),
)

UNIT5_LESSONS = (
    ENGLISH_U5_L1,
    ENGLISH_U5_L2,
    ENGLISH_U5_L3,
    ENGLISH_U5_L4,
    ENGLISH_U5_L5,
    ENGLISH_U5_L6,
)
