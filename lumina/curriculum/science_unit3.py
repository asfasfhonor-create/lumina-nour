from lumina.learning.lesson_models import LessonCheck, LessonData


SCIENCE_U3_L1 = LessonData(
    id="science_u3_l1",
    source_id="science_prep3_t1",
    unit_id="u3",
    title="The Universe and the Solar System",
    source_pages="Book pages 44–53",
    objectives=(
        "Describe the relationship between the universe, galaxies, the Milky Way, the solar system, and Earth.",
        "Understand the Big Bang explanation presented in the book for the origin and expansion of the universe.",
        "Recognize major historical theories about the evolution of the solar system.",
        "Connect astronomical observations with tools such as telescopes.",
    ),
    key_terms=(
        "universe",
        "galaxy",
        "Milky Way",
        "solar system",
        "Big Bang",
        "expansion",
        "nebular assumption",
        "crossing star theory",
        "modern theory",
        "telescope",
    ),
    evidence_summary=(
        "The book presents the universe as a vast space containing galaxies; the Milky Way contains the Sun and solar system, and Earth is one planet within it.",
        "The Big Bang section describes the universe as beginning from a very small, hot state and expanding, with galaxies moving apart.",
        "The solar-system evolution section presents multiple historical theories, including Laplace's nebular assumption, the crossing-star theory, and Fred Hoyle's modern theory.",
        "The unit links astronomy to technological tools such as solar and Hubble telescopes.",
    ),
    checks=(
        LessonCheck(
            id="hierarchy",
            prompt="Which sequence goes from larger structure to smaller structure according to the lesson?",
            expected_points=("universe galaxy milky way solar system earth",),
            hint="Start with the largest space containing everything else.",
            options=(
                "Earth → Solar System → Milky Way → Universe",
                "Universe → Milky Way galaxy → Solar System → Earth",
                "Solar System → Universe → Earth → Milky Way",
            ),
            correct_index=1,
        ),
        LessonCheck(
            id="expansion",
            prompt="What evidence idea does the lesson connect with an expanding universe?",
            expected_points=("galaxies move apart",),
            hint="Think about the bread-and-raisins activity.",
            options=(
                "Galaxies move farther apart as the universe expands.",
                "All galaxies remain fixed at exactly the same distance.",
                "Only Earth changes its size.",
            ),
            correct_index=0,
        ),
    ),
)


SCIENCE_UNIT3_LESSONS = (SCIENCE_U3_L1,)
