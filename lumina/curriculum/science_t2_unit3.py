from lumina.learning.lesson_models import LessonCheck, LessonData


SCIENCE_T2_U3_L1 = LessonData(
    id="science_t2_u3_l1",
    source_id="science_prep3_t2",
    unit_id="t2_u3",
    title="The Main Principles of Heredity",
    source_pages="Second Term book pages 120–132",
    objectives=(
        "Understand heredity through Mendel's pea-plant experiments.",
        "Distinguish dominant and recessive traits.",
        "Interpret simple genetic crosses using symbols.",
        "Understand Mendel's laws presented in the book.",
    ),
    key_terms=("heredity", "Mendel", "dominant trait", "recessive trait", "gene", "gamete", "segregation", "independent assortment"),
    evidence_summary=(
        "The lesson introduces heredity through Mendel's experiments on contrasting pea-plant traits.",
        "First-generation hybrids express the dominant trait while the recessive trait can reappear in the second generation.",
        "The law of segregation states that hereditary factors separate during gamete formation and reunite at fertilization.",
        "The lesson also presents independent assortment for different hereditary factors when applicable.",
    ),
    checks=(
        LessonCheck(
            id="dominant_recessive",
            prompt="What happens to the recessive trait in Mendel's first-generation hybrids?",
            expected_points=("it can be hidden in the first generation and reappear later",),
            hint="Compare F1 with F2 in the pea-plant examples.",
            options=(
                "It may be hidden in F1 and reappear in a later generation.",
                "It is permanently destroyed.",
                "It always appears more strongly than the dominant trait in F1.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="segregation",
            prompt="What does Mendel's law of segregation describe?",
            expected_points=("hereditary factors separate during gamete formation",),
            hint="Think about how paired factors enter different gametes.",
            options=(
                "Hereditary factors separate during gamete formation.",
                "All hereditary factors remain permanently joined.",
                "Traits are determined only by environment.",
            ),
            correct_index=0,
        ),
    ),
)


SCIENCE_T2_UNIT3_LESSONS = (SCIENCE_T2_U3_L1,)
