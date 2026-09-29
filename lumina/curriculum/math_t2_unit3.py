from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_T2_U3_L1 = LessonData(
    id="math_t2_u3_l1",
    source_id="math_prep3_t2",
    unit_id="t2_u3",
    title="Operations on Events",
    source_pages="Second Term book pages 30–34",
    objectives=(
        "Understand sample space and events.",
        "Use union and intersection of events.",
        "Interpret probability of combined events using set diagrams.",
    ),
    key_terms=("sample space", "event", "union", "intersection", "probability", "Venn diagram"),
    evidence_summary=(
        "An event is a subset of the sample space.",
        "The union A∪B contains outcomes belonging to A or B, while the intersection A∩B contains outcomes common to both.",
        "The lesson uses Venn diagrams and counting to calculate probabilities of combined events.",
    ),
    checks=(
        LessonCheck(
            id="intersection",
            prompt="What does A ∩ B represent?",
            expected_points=("outcomes common to A and B",),
            hint="Intersection means overlap.",
            options=(
                "Outcomes common to both A and B.",
                "All outcomes outside both events.",
                "Only outcomes in A but never B.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U3_L2 = LessonData(
    id="math_t2_u3_l2",
    source_id="math_prep3_t2",
    unit_id="t2_u3",
    title="Complementary Event and the Difference Between Two Events",
    source_pages="Second Term book pages 35–37",
    objectives=(
        "Understand the complement of an event.",
        "Use P(A') = 1 − P(A).",
        "Understand the difference between two events.",
    ),
    key_terms=("complementary event", "complement", "difference of events", "A'", "A-B"),
    evidence_summary=(
        "The complement A' contains outcomes in the sample space that are not in A.",
        "The probabilities of an event and its complement add to 1.",
        "The difference A−B contains outcomes belonging to A but not to B.",
    ),
    checks=(
        LessonCheck(
            id="complement_probability",
            prompt="If P(A)=0.3, what is P(A')?",
            expected_points=("0.7",),
            hint="An event and its complement add to 1.",
            options=("0.7", "0.3", "1.3"),
            correct_index=0,
        ),
    ),
)


MATH_T2_UNIT3_LESSONS = (
    MATH_T2_U3_L1,
    MATH_T2_U3_L2,
)
