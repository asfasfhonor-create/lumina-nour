from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_U4_L1 = LessonData(
    id="math_u4_l1",
    source_id="math_prep3_t1",
    unit_id="u4",
    title="The Main Trigonometrical Ratios of the Acute Angle",
    source_pages="Book pages 49–51",
    objectives=(
        "Understand sine, cosine, and tangent in a right-angled triangle.",
        "Identify opposite, adjacent, and hypotenuse relative to an acute angle.",
        "Use basic trigonometric identities in right triangles.",
    ),
    key_terms=("sine", "cosine", "tangent", "opposite", "adjacent", "hypotenuse", "acute angle"),
    evidence_summary=(
        "For an acute angle in a right triangle, sine is opposite over hypotenuse, cosine is adjacent over hypotenuse, and tangent is opposite over adjacent.",
        "The side descriptions depend on the chosen acute angle.",
        "The lesson connects these ratios with identities such as sin²A + cos²A = 1.",
    ),
    checks=(
        LessonCheck(
            id="sin_ratio",
            prompt="For an acute angle A in a right triangle, what is sin A?",
            expected_points=("opposite divided by hypotenuse",),
            hint="Sine uses the side opposite the angle and the longest side.",
            options=(
                "Opposite ÷ Hypotenuse",
                "Adjacent ÷ Hypotenuse",
                "Opposite ÷ Adjacent",
            ),
            correct_index=0,
        ),
    ),
)


MATH_U4_L2 = LessonData(
    id="math_u4_l2",
    source_id="math_prep3_t1",
    unit_id="u4",
    title="The Main Trigonometrical Ratios of Some Angles",
    source_pages="Book pages 52–56",
    objectives=(
        "Know the main trigonometric ratios for 30°, 45°, and 60°.",
        "Use a calculator to find trigonometric ratios and angles.",
        "Apply trigonometry in geometry problems.",
    ),
    key_terms=("30°", "45°", "60°", "special angles", "inverse trigonometric function"),
    evidence_summary=(
        "The lesson derives exact sine, cosine, and tangent values for 30°, 45°, and 60° from special triangles.",
        "It also uses calculator functions to find ratios of other angles and to recover an angle from a given ratio.",
        "Trigonometric ratios are applied to solve geometric lengths and areas.",
    ),
    checks=(
        LessonCheck(
            id="special_angle",
            prompt="Which statement is correct for the special angles in the lesson?",
            expected_points=("sin 30 equals one half",),
            hint="Use the 30°–60° triangle table.",
            options=(
                "sin 30° = 1/2",
                "sin 30° = 1",
                "tan 45° = 0",
            ),
            correct_index=0,
        ),
    ),
)


MATH_UNIT4_LESSONS = (
    MATH_U4_L1,
    MATH_U4_L2,
)
