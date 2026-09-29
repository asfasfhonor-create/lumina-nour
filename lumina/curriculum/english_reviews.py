from lumina.learning.lesson_models import LessonCheck, LessonData


REVIEW1 = LessonData(
    id="english_review1",
    source_id="english_prep3_t1",
    unit_id="review1",
    title="Review 1",
    source_pages="Book pages 55–58",
    objectives=(
        "Review vocabulary and language from Units 1–3.",
        "Practice reading/listening ideas connected to personal development, technology, and AI.",
        "Review the school-garden story themes from the first three chapters.",
    ),
    key_terms=("determination", "misunderstood", "customized", "Third Conditional", "Future Passive", "AI"),
    evidence_summary=(
        "Review 1 revisits vocabulary, grammar, reading/listening, and story understanding from Units 1–3.",
        "It includes Third Conditional and future/passive language alongside vocabulary about confidence, determination, technology, and AI.",
        "The story review returns to teamwork, respect, and Zeina's project challenges.",
    ),
    checks=(
        LessonCheck(
            id="review1_third_conditional",
            prompt="Which sentence correctly completes an unreal past idea?",
            expected_points=("third conditional",),
            hint="Use had + past participle, then would have + past participle.",
            options=(
                "If she had studied harder, she would have passed.",
                "If she studies harder, she passes.",
                "If she will study harder, she would pass.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="review1_future_passive",
            prompt="Which sentence uses the future passive correctly?",
            expected_points=("future passive",),
            hint="Use will be + past participle.",
            options=(
                "The message will send tomorrow.",
                "The message will be sent tomorrow.",
                "The message will sent tomorrow.",
            ),
            correct_index=1,
        ),
        LessonCheck(
            id="review1_story",
            prompt="Which value best supports teamwork in the School Garden Project?",
            expected_points=("respect and determination",),
            hint="The review asks about respecting opinions and continuing through problems.",
            options=(
                "Ignoring other people's ideas.",
                "Respecting opinions and showing determination.",
                "Quitting when the first problem appears.",
            ),
            correct_index=1,
        ),
    ),
)


REVIEW2 = LessonData(
    id="english_review2",
    source_id="english_prep3_t1",
    unit_id="review2",
    title="Review 2",
    source_pages="Book pages 100–102",
    objectives=(
        "Review screen-time, technology, design-thinking, and story skills from Units 4–6.",
        "Practice reading, listening, vocabulary, modal verbs, and writing.",
        "Connect leadership and balance with the final School Garden Project themes.",
    ),
    key_terms=("balance", "determination", "helpful", "experts", "must", "mustn't", "technology", "leadership"),
    evidence_summary=(
        "Review 2 revisits healthy screen habits, digital technology, design thinking, leadership, and storytelling.",
        "It includes modal verbs, vocabulary, reading/listening comprehension, and a short-story writing task.",
        "The review emphasizes balanced technology use and leadership that helps people feel confident and important.",
    ),
    checks=(
        LessonCheck(
            id="review2_screen_balance",
            prompt="Which habit best matches the review's healthy technology message?",
            expected_points=("balanced screen use",),
            hint="The review passage warns about excessive use but also describes benefits.",
            options=(
                "Use technology without limits.",
                "Control technology use and keep a healthy balance.",
                "Avoid all digital tools.",
            ),
            correct_index=1,
        ),
        LessonCheck(
            id="review2_modal",
            prompt="Which modal best completes: You ___ turn off your phone during exams.",
            expected_points=("must",),
            hint="The sentence expresses a rule/obligation.",
            options=("must", "can", "shouldn't"),
            correct_index=0,
        ),
        LessonCheck(
            id="review2_leadership",
            prompt="What kind of leader does the review connect with positive growth?",
            expected_points=("honest supportive leader",),
            hint="Think about Zeina's growth as a leader.",
            options=(
                "A leader who makes people feel confident and important.",
                "A leader who never listens.",
                "A leader who avoids responsibility.",
            ),
            correct_index=0,
        ),
    ),
)


REVIEWS = {
    "Review 1": REVIEW1,
    "Review 2": REVIEW2,
}


def get_review(title: str) -> LessonData | None:
    return REVIEWS.get(title)
