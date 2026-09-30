from lumina.learning.lesson_models import LessonCheck, LessonData


SCIENCE_U4_L1 = LessonData(
    id="science_u4_l1",
    source_id="science_prep3_t1",
    unit_id="u4",
    title="Cell Division",
    source_pages="Book pages 56–62",
    objectives=(
        "Explain the role of chromosomes in cell division.",
        "Distinguish mitosis from meiosis and connect each to its biological role.",
        "Understand that meiosis reduces chromosome number and contributes to genetic variation.",
    ),
    key_terms=("chromosome", "DNA", "mitosis", "meiosis", "somatic cells", "reproductive cells", "crossing over"),
    evidence_summary=(
        "The lesson links chromosomes and DNA with the genetic information needed during cell division.",
        "Mitosis produces cells used for growth and replacing damaged cells, while meiosis produces reproductive cells with half the chromosome number.",
        "Meiosis occurs in two successive divisions and restores the species chromosome number after fertilization.",
        "Crossing over during meiosis exchanges genetic material between homologous chromosomes and contributes to variation.",
    ),
    checks=(
        LessonCheck(
            id="mitosis_meiosis",
            prompt="Which statement correctly compares mitosis and meiosis?",
            expected_points=("mitosis growth repair, meiosis gametes half chromosomes",),
            hint="Think about body cells versus reproductive cells.",
            options=(
                "Mitosis forms gametes with half the chromosome number.",
                "Mitosis supports growth/repair, while meiosis forms gametes with half the chromosome number.",
                "Mitosis and meiosis always produce exactly the same cells.",
            ),
            correct_index=1,
        ),
        LessonCheck(
            id="crossing_over",
            prompt="Why is crossing over important according to the lesson?",
            expected_points=("it contributes to genetic variation",),
            hint="It exchanges parts between homologous chromosomes.",
            options=(
                "It makes every offspring genetically identical.",
                "It contributes to genetic variation by exchanging genetic material.",
                "It prevents chromosomes from carrying genes.",
            ),
            correct_index=1,
        ),
    ),
)


SCIENCE_U4_L2 = LessonData(
    id="science_u4_l2",
    source_id="science_prep3_t1",
    unit_id="u4",
    title="Sexual and Asexual Reproduction",
    source_pages="Book pages 63–68",
    objectives=(
        "Distinguish sexual from asexual reproduction.",
        "Identify examples of asexual reproduction such as binary fission, budding, regeneration, spore formation, and vegetative reproduction.",
        "Understand gamete formation and fertilization in sexual reproduction.",
        "Explain why sexual reproduction is a source of genetic variation.",
    ),
    key_terms=(
        "asexual reproduction",
        "sexual reproduction",
        "binary fission",
        "budding",
        "regeneration",
        "spore formation",
        "vegetative reproduction",
        "gametes",
        "fertilization",
        "genetic variation",
    ),
    evidence_summary=(
        "Asexual reproduction involves one parent and can produce offspring genetically similar to the parent through processes such as binary fission, budding, regeneration, spore formation, and vegetative reproduction.",
        "Sexual reproduction generally involves male and female gametes formed by meiosis.",
        "Fertilization combines male and female gametes to form a zygote and restores the species chromosome number.",
        "Because genetic traits come from two parents and meiosis introduces variation, sexual reproduction is a source of genetic variation.",
    ),
    checks=(
        LessonCheck(
            id="asexual_feature",
            prompt="Which feature best describes asexual reproduction in this lesson?",
            expected_points=("one parent, genetically similar offspring",),
            hint="Compare the number of parents and the source of genetic material.",
            options=(
                "It always requires two parents.",
                "It can involve one parent and usually produces genetically similar offspring.",
                "It always depends on fertilization.",
            ),
            correct_index=1,
        ),
        LessonCheck(
            id="sexual_variation",
            prompt="Why can sexual reproduction create more genetic variation?",
            expected_points=("genetic material comes from two parents and meiosis creates variation",),
            hint="Think about gametes and the combination of genetic material.",
            options=(
                "Because it combines genetic material from two parents and meiosis contributes variation.",
                "Because offspring receive no genetic material.",
                "Because it always creates identical copies.",
            ),
            correct_index=0,
        ),
    ),
)


SCIENCE_UNIT4_LESSONS = (
    SCIENCE_U4_L1,
    SCIENCE_U4_L2,
)
