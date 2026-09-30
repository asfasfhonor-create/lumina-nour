from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_U2_L1 = LessonData(
    id="math_u2_l1",
    source_id="math_prep3_t1",
    unit_id="u2",
    title="Ratio",
    source_pages="Book pages 25–26",
    objectives=(
        "Understand a ratio as a comparison between two quantities.",
        "Identify antecedent and consequent.",
        "Apply basic ratio properties and solve simple ratio problems.",
    ),
    key_terms=("ratio", "antecedent", "consequent", "terms of the ratio"),
    evidence_summary=(
        "A ratio compares two quantities and may be written in forms such as a:b or a/b.",
        "The first term is the antecedent and the second term is the consequent.",
        "The lesson explores how a ratio changes or remains unchanged when its terms are transformed in the same or different ways.",
    ),
    checks=(
        LessonCheck(
            id="ratio_terms",
            prompt="In the ratio a:b, which term is the antecedent?",
            expected_points=("a is antecedent",),
            hint="The antecedent is the first term.",
            options=("a", "b", "a+b"),
            correct_index=0,
        ),
    ),
)


MATH_U2_L2 = LessonData(
    id="math_u2_l2",
    source_id="math_prep3_t1",
    unit_id="u2",
    title="Proportion",
    source_pages="Book pages 27–31",
    objectives=(
        "Understand a proportion as equality of two ratios.",
        "Use the product of extremes equals product of means property.",
        "Work with first, second, third, and fourth proportionals and continued proportion.",
    ),
    key_terms=("proportion", "extremes", "means", "fourth proportional", "continued proportional", "middle proportional"),
    evidence_summary=(
        "A proportion is the equality of two ratios.",
        "If a/b = c/d, then the product of the extremes equals the product of the means.",
        "The lesson develops proportional terms, fourth proportional, and continued proportion, including middle proportional.",
    ),
    checks=(
        LessonCheck(
            id="proportion_property",
            prompt="If a/b = c/d, which relation follows from the basic property of proportion?",
            expected_points=("a times d equals b times c",),
            hint="Multiply the extremes and compare them with the means.",
            options=(
                "a × d = b × c",
                "a + d = b + c",
                "a × b = c × d",
            ),
            correct_index=0,
        ),
    ),
)


MATH_U2_L3 = LessonData(
    id="math_u2_l3",
    source_id="math_prep3_t1",
    unit_id="u2",
    title="Direct Variation and Inverse Variation",
    source_pages="Book pages 32–33",
    objectives=(
        "Distinguish direct variation from inverse variation.",
        "Recognize the constant of variation.",
        "Connect direct variation with a straight-line relation through the origin.",
        "Solve simple direct and inverse variation problems.",
    ),
    key_terms=("variation", "direct variation", "inverse variation", "constant of variation", "linear relation"),
    evidence_summary=(
        "In direct variation, y changes in constant proportion with x and can be written y = mx, where m is a non-zero constant.",
        "A direct variation graph is a straight line passing through the origin.",
        "In inverse variation, the product xy remains constant, so y can be written as a constant divided by x.",
    ),
    checks=(
        LessonCheck(
            id="direct_variation",
            prompt="Which equation represents direct variation between y and x?",
            expected_points=("y equals constant times x",),
            hint="The lesson writes direct variation in the form y = mx.",
            options=("y = mx", "y = m/x", "y = x + m only"),
            correct_index=0,
        ),
        LessonCheck(
            id="inverse_variation",
            prompt="What stays constant in an inverse variation between x and y?",
            expected_points=("product xy",),
            hint="Think about the rectangle-area example.",
            options=("x + y", "xy", "x - y"),
            correct_index=1,
        ),
    ),
)


MATH_UNIT2_LESSONS = (
    MATH_U2_L1,
    MATH_U2_L2,
    MATH_U2_L3,
)
