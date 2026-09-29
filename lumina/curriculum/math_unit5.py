from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_U5_L1 = LessonData(
    id="math_u5_l1",
    source_id="math_prep3_t1",
    unit_id="u5",
    title="Distance Between Two Points",
    source_pages="Book pages 58–61",
    objectives=(
        "Find the distance between two points on the coordinate plane.",
        "Use the Pythagorean theorem to derive the distance rule.",
        "Apply distance to geometric classification and proofs.",
    ),
    key_terms=("coordinate plane", "ordered pair", "distance", "Pythagorean theorem"),
    evidence_summary=(
        "The distance formula comes from horizontal and vertical differences between two coordinate points and the Pythagorean theorem.",
        "For points (x1,y1) and (x2,y2), distance is the square root of the sum of squared coordinate differences.",
        "The lesson uses distances to analyze shapes, right triangles, and collinearity.",
    ),
    checks=(
        LessonCheck(
            id="distance_formula",
            prompt="Which expression gives the distance between (x1,y1) and (x2,y2)?",
            expected_points=("square root of squared x difference plus squared y difference",),
            hint="Use the Pythagorean theorem on horizontal and vertical differences.",
            options=(
                "√[(x2−x1)² + (y2−y1)²]",
                "(x2−x1) + (y2−y1)",
                "x1x2 + y1y2",
            ),
            correct_index=0,
        ),
    ),
)


MATH_U5_L2 = LessonData(
    id="math_u5_l2",
    source_id="math_prep3_t1",
    unit_id="u5",
    title="The Two Coordinates of the Midpoint Segment",
    source_pages="Book pages 62–64",
    objectives=(
        "Find the midpoint of a line segment from endpoint coordinates.",
        "Use midpoint relationships to find an unknown endpoint.",
        "Apply midpoint properties in coordinate geometry.",
    ),
    key_terms=("midpoint", "segment", "endpoint", "coordinates"),
    evidence_summary=(
        "The midpoint coordinate is found by averaging the x-coordinates and averaging the y-coordinates of the endpoints.",
        "The midpoint formula can also be rearranged to find an unknown endpoint.",
        "The lesson applies midpoint ideas to geometric figures such as parallelograms.",
    ),
    checks=(
        LessonCheck(
            id="midpoint_formula",
            prompt="How do you find the x-coordinate of the midpoint of two points?",
            expected_points=("average the two x coordinates",),
            hint="The midpoint is halfway between the endpoint coordinates.",
            options=(
                "(x1 + x2) ÷ 2",
                "x1 − x2",
                "x1 × x2",
            ),
            correct_index=0,
        ),
    ),
)


MATH_U5_L3 = LessonData(
    id="math_u5_l3",
    source_id="math_prep3_t1",
    unit_id="u5",
    title="The Slope of the Straight Line",
    source_pages="Book pages 65–69",
    objectives=(
        "Calculate slope from two points.",
        "Relate slope to the positive angle a line makes with the x-axis.",
        "Use slopes to identify parallel and perpendicular straight lines.",
    ),
    key_terms=("slope", "positive angle", "parallel lines", "perpendicular lines", "undefined slope"),
    evidence_summary=(
        "Slope between two points is the change in y divided by the change in x.",
        "Slope equals the tangent of the positive angle made with the positive x-axis.",
        "Parallel non-vertical lines have equal slopes, while perpendicular lines with defined slopes satisfy m1 × m2 = −1.",
    ),
    checks=(
        LessonCheck(
            id="parallel_slopes",
            prompt="What is true about the slopes of two parallel non-vertical straight lines?",
            expected_points=("their slopes are equal",),
            hint="The lesson states the parallel-line slope relation directly.",
            options=(
                "Their slopes are equal.",
                "Their slopes always multiply to −1.",
                "Both slopes must be zero.",
            ),
            correct_index=0,
        ),
        LessonCheck(
            id="perpendicular_slopes",
            prompt="For two perpendicular lines with defined slopes m1 and m2, what relation holds?",
            expected_points=("m1 times m2 equals minus one",),
            hint="This is the perpendicular-line slope rule.",
            options=(
                "m1 + m2 = 0",
                "m1 × m2 = −1",
                "m1 = m2",
            ),
            correct_index=1,
        ),
    ),
)


MATH_U5_L4 = LessonData(
    id="math_u5_l4",
    source_id="math_prep3_t1",
    unit_id="u5",
    title="The Equation of the Straight Line Given Its Slope and Its y-Intercept",
    source_pages="Book pages 70–72",
    objectives=(
        "Recognize slope-intercept form of a straight-line equation.",
        "Find a line equation from its slope and y-intercept.",
        "Connect standard and slope-intercept forms.",
    ),
    key_terms=("equation of straight line", "slope", "y-intercept", "y = mx + c", "ax + by + c = 0"),
    evidence_summary=(
        "The slope-intercept form is y = mx + c, where m is the slope and c is the y-intercept.",
        "The lesson connects this form to the general linear relation ax + by + c = 0.",
        "Examples determine equations using known slopes, intercepts, points, and perpendicular-line conditions.",
    ),
    checks=(
        LessonCheck(
            id="slope_intercept",
            prompt="In y = mx + c, what do m and c represent?",
            expected_points=("m slope, c y-intercept",),
            hint="The lesson names this the slope and y-intercept form.",
            options=(
                "m is slope and c is the y-intercept.",
                "m is the x-coordinate and c is the angle.",
                "m is the y-intercept and c is always zero.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_UNIT5_LESSONS = (
    MATH_U5_L1,
    MATH_U5_L2,
    MATH_U5_L3,
    MATH_U5_L4,
)
