from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_U3_L1 = LessonData(
    id="math_u3_l1",
    source_id="math_prep3_t1",
    unit_id="u3",
    title="Collecting Data",
    source_pages="Book pages 38–40",
    objectives=(
        "Distinguish primary and secondary data sources.",
        "Choose between population and sample methods.",
        "Recognize biased and random selection and common random-sample types.",
    ),
    key_terms=("primary resources", "secondary resources", "population", "sample", "biased choice", "random choice", "simple random sample", "layer sample"),
    evidence_summary=(
        "Primary data are collected directly for the research, while secondary data come from previously existing sources.",
        "A population study includes all members, while a sample studies a selected subset and generalizes carefully.",
        "The lesson distinguishes biased selection from random selection and presents simple random and layered sampling.",
    ),
    checks=(
        LessonCheck(
            id="primary_secondary",
            prompt="Which example is a primary data source for a school survey?",
            expected_points=("data collected directly through interview or questionnaire",),
            hint="Primary data are collected directly for the current research.",
            options=(
                "A questionnaire answered by the students for this study.",
                "An old published table from another study.",
                "A historical statistics website only.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="random_sample",
            prompt="Why is random selection important?",
            expected_points=("every member has a fair or equal chance and bias is reduced",),
            hint="Compare random selection with a researcher choosing preferred people.",
            options=(
                "It helps reduce selection bias by giving members a fair chance of being selected.",
                "It guarantees every answer will be identical.",
                "It means choosing only the easiest people to reach.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_U3_L2 = LessonData(
    id="math_u3_l2",
    source_id="math_prep3_t1",
    unit_id="u3",
    title="Dispersion",
    source_pages="Book pages 41–47",
    objectives=(
        "Understand dispersion as the spread of values.",
        "Calculate and interpret range.",
        "Understand standard deviation as a measure of dispersion.",
        "Compare data sets using central tendency together with dispersion.",
    ),
    key_terms=("dispersion", "range", "mean", "standard deviation", "frequency distribution", "homogeneous"),
    evidence_summary=(
        "Two data sets can have the same mean or median while differing greatly in how spread out their values are.",
        "Range is the difference between the greatest and smallest value and is a simple measure of dispersion.",
        "Standard deviation uses deviations from the mean and is more informative because it reflects all values in the set.",
        "Smaller dispersion indicates more homogeneous data; larger standard deviation indicates greater spread.",
    ),
    checks=(
        LessonCheck(
            id="range",
            prompt="How is the range of a data set calculated?",
            expected_points=("greatest value minus smallest value",),
            hint="The range uses only the two extreme values.",
            options=(
                "Greatest value − smallest value",
                "Mean × number of values",
                "Smallest value − greatest value",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="dispersion_compare",
            prompt="If two sets have the same mean, which set is more homogeneous?",
            expected_points=("the one with smaller standard deviation",),
            hint="More homogeneous means values are less spread out.",
            options=(
                "The set with the larger standard deviation.",
                "The set with the smaller standard deviation.",
                "They must always have the same dispersion.",
            ),
            correct_index=1,
        ),
    ),
)


MATH_UNIT3_LESSONS = (
    MATH_U3_L1,
    MATH_U3_L2,
)
