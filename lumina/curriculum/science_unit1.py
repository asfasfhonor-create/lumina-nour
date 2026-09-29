from lumina.learning.lesson_models import LessonCheck, LessonData


SCIENCE_U1_L1 = LessonData(
    id="science_u1_l1",
    source_id="science_prep3_t1",
    unit_id="u1",
    title="Motion in One Direction",
    source_pages="PDF pages 8–13",
    objectives=(
        "Describe motion in one direction using distance and time.",
        "Understand speed and distinguish uniform from non-uniform motion.",
        "Calculate average speed from total distance and total time.",
    ),
    key_terms=("motion", "distance", "time", "speed", "uniform speed", "average speed", "relative speed"),
    evidence_summary=(
        "The lesson introduces motion in one direction and relates motion description to distance and time.",
        "Speed expresses the distance travelled per unit time.",
        "Uniform speed describes motion at a constant speed, while average speed is used when speed changes during a journey.",
        "The lesson includes examples and applications involving moving vehicles and relative motion.",
    ),
    checks=(
        LessonCheck(
            id="average_speed",
            prompt="Which rule best matches average speed in the lesson?",
            expected_points=("total distance divided by total time",),
            hint="Think about the whole journey rather than one instant.",
            options=(
                "Average speed = total distance ÷ total time",
                "Average speed = total time ÷ total distance",
                "Average speed = distance × time",
            ),
            correct_index=0,
            difficulty=1,
            activity_kind="concept",
        ),
        LessonCheck(
            id="average_speed_practice",
            prompt="Practice mission: a toy car travels 120 m in 20 s. What is its average speed?",
            expected_points=("6 m/s",),
            hint="Use total distance ÷ total time.",
            options=(
                "6 m/s",
                "100 m/s",
                "2400 m/s",
            ),
            correct_index=0,
            difficulty=2,
            activity_kind="practice",
        ),
        LessonCheck(
            id="average_speed_challenge",
            prompt="Mini challenge: which trip has the greater average speed?",
            expected_points=("trip b",),
            hint="Calculate distance ÷ time for each trip.",
            options=(
                "Trip A: 90 m in 30 s",
                "Trip B: 120 m in 20 s",
                "They have the same average speed",
            ),
            correct_index=1,
            difficulty=3,
            activity_kind="challenge",
        ),
    ),
)

SCIENCE_U1_L2 = LessonData(
    id="science_u1_l2",
    source_id="science_prep3_t1",
    unit_id="u1",
    title="Graphic Representation of Motion in a Straight Line",
    source_pages="PDF pages 14–19",
    objectives=(
        "Represent motion using graphs.",
        "Relate the slope or change shown in a motion graph to the motion being described.",
        "Understand acceleration as change in velocity with time.",
    ),
    key_terms=("graph", "distance-time graph", "velocity", "acceleration", "uniform acceleration"),
    evidence_summary=(
        "The lesson uses graphs to represent motion in a straight line.",
        "Distance-time information can be plotted and interpreted to describe how an object moves.",
        "The lesson introduces acceleration through change in velocity over time and includes examples of uniform acceleration.",
    ),
    checks=(
        LessonCheck(
            id="acceleration_meaning",
            prompt="Which statement best describes acceleration in this lesson?",
            expected_points=("change in velocity per unit time",),
            hint="The lesson links acceleration to how velocity changes with time.",
            options=(
                "Acceleration is the total distance only.",
                "Acceleration describes the change in velocity with time.",
                "Acceleration is always equal to time.",
            ),
            correct_index=1,
        ),
    ),
)

SCIENCE_U1_L3 = LessonData(
    id="science_u1_l3",
    source_id="science_prep3_t1",
    unit_id="u1",
    title="Physical Quantities: Scalars and Vectors",
    source_pages="PDF pages 20–25",
    objectives=(
        "Distinguish scalar and vector physical quantities.",
        "Understand distance and displacement.",
        "Relate speed and velocity while recognizing the role of direction.",
    ),
    key_terms=("physical quantity", "scalar", "vector", "distance", "displacement", "speed", "velocity", "direction"),
    evidence_summary=(
        "The lesson classifies physical quantities into scalar and vector quantities.",
        "Scalar quantities are described by magnitude, while vector quantities require magnitude and direction.",
        "Distance and displacement are compared, and speed and velocity are distinguished using direction.",
    ),
    checks=(
        LessonCheck(
            id="vector_definition",
            prompt="Which statement correctly describes a vector quantity?",
            expected_points=("magnitude and direction",),
            hint="The key difference from a scalar is direction.",
            options=(
                "It has magnitude only.",
                "It has magnitude and direction.",
                "It has direction only and no magnitude.",
            ),
            correct_index=1,
        ),
    ),
)

SCIENCE_UNIT1_LESSONS = (
    SCIENCE_U1_L1,
    SCIENCE_U1_L2,
    SCIENCE_U1_L3,
)
