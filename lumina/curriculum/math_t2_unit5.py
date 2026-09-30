from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_T2_U5_L1 = LessonData(
    id="math_t2_u5_l1",
    source_id="math_prep3_t2",
    unit_id="t2_u5",
    title="Central Angle and Measuring Arcs",
    source_pages="Second Term book pages 64–70",
    objectives=(
        "Understand a central angle and its intercepted arc.",
        "Relate the measure of a central angle to the measure of its intercepted arc.",
        "Use arc measures and full-circle relationships in problems.",
    ),
    key_terms=("central angle", "arc", "measure of arc", "minor arc", "major arc", "semicircle"),
    evidence_summary=(
        "A central angle has its vertex at the centre of the circle.",
        "The measure of a central angle equals the measure of its intercepted arc.",
        "The full circle has 360°, and arc measures are combined or subtracted to solve problems.",
    ),
    checks=(
        LessonCheck(
            id="central_arc",
            prompt="What is the relation between a central angle and its intercepted arc?",
            expected_points=("their measures are equal",),
            hint="The vertex of the angle is at the centre.",
            options=(
                "Their measures are equal.",
                "The arc is always half the angle.",
                "The angle is always twice the arc.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U5_L2 = LessonData(
    id="math_t2_u5_l2",
    source_id="math_prep3_t2",
    unit_id="t2_u5",
    title="The Relation Between the Inscribed and Central Angles Subtended by the Same Arc",
    source_pages="Second Term book pages 71–78",
    objectives=(
        "Understand an inscribed angle.",
        "Relate inscribed and central angles subtending the same arc.",
        "Use semicircle and arc relationships to calculate unknown angles.",
    ),
    key_terms=("inscribed angle", "central angle", "subtended arc", "semicircle"),
    evidence_summary=(
        "An inscribed angle has its vertex on the circle.",
        "For the same arc, the central angle is twice the inscribed angle, or the inscribed angle is half the central angle.",
        "An angle subtended by a diameter at the circumference is a right angle.",
    ),
    checks=(
        LessonCheck(
            id="inscribed_central",
            prompt="For the same arc, how does an inscribed angle compare with the central angle?",
            expected_points=("inscribed angle equals half central angle",),
            hint="The central angle is the larger of the two.",
            options=(
                "The inscribed angle is half the central angle.",
                "They are always equal.",
                "The inscribed angle is double the central angle.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U5_L3 = LessonData(
    id="math_t2_u5_l3",
    source_id="math_prep3_t2",
    unit_id="t2_u5",
    title="Inscribed Angles Subtended by the Same Arc",
    source_pages="Second Term book pages 79–84",
    objectives=(
        "Recognize inscribed angles standing on the same arc.",
        "Use equality of inscribed angles subtended by the same arc.",
        "Apply the converse relation in cyclic reasoning.",
    ),
    key_terms=("inscribed angles", "same arc", "equal angles", "cyclic points"),
    evidence_summary=(
        "Inscribed angles subtended by the same arc are equal.",
        "The lesson also uses the converse idea: equal angles standing on the same chord/segment can establish concyclicity in the shown problems.",
        "These relationships support geometric proofs involving chords and intersecting segments.",
    ),
    checks=(
        LessonCheck(
            id="same_arc",
            prompt="Two inscribed angles subtend the same arc. What can you conclude?",
            expected_points=("the angles are equal",),
            hint="They stand on the same arc.",
            options=(
                "The angles are equal.",
                "One must be twice the other.",
                "Both must be 90°.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U5_L4 = LessonData(
    id="math_t2_u5_l4",
    source_id="math_prep3_t2",
    unit_id="t2_u5",
    title="Cyclic Quadrilaterals",
    source_pages="Second Term book pages 85–87",
    objectives=(
        "Understand what makes a quadrilateral cyclic.",
        "Recognize a quadrilateral whose four vertices lie on one circle.",
        "Use angle relationships to prove a quadrilateral is cyclic.",
    ),
    key_terms=("cyclic quadrilateral", "concyclic", "opposite angles", "circle"),
    evidence_summary=(
        "A cyclic quadrilateral has all four vertices on the same circle.",
        "The lesson uses angle relationships and circle theorems to identify and prove cyclic quadrilaterals.",
        "Worked examples connect cyclicity with equal angles subtended by the same arc.",
    ),
    checks=(
        LessonCheck(
            id="cyclic_definition",
            prompt="What makes a quadrilateral cyclic?",
            expected_points=("all four vertices lie on one circle",),
            hint="Think about where the four vertices are located.",
            options=(
                "All four vertices lie on the same circle.",
                "All four sides must be equal.",
                "It must have four right angles.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U5_L5 = LessonData(
    id="math_t2_u5_l5",
    source_id="math_prep3_t2",
    unit_id="t2_u5",
    title="Properties of Cyclic Quadrilaterals",
    source_pages="Second Term book pages 88–92",
    objectives=(
        "Use properties of opposite angles in a cyclic quadrilateral.",
        "Apply exterior-angle relationships.",
        "Use cyclic-quadrilateral properties in geometric proofs.",
    ),
    key_terms=("opposite angles", "supplementary", "exterior angle", "cyclic quadrilateral"),
    evidence_summary=(
        "Opposite angles of a cyclic quadrilateral are supplementary.",
        "An exterior angle of a cyclic quadrilateral equals the interior opposite angle in the relationships presented.",
        "The lesson uses these properties to prove angle and shape relations.",
    ),
    checks=(
        LessonCheck(
            id="opposite_angles",
            prompt="What is the sum of a pair of opposite angles in a cyclic quadrilateral?",
            expected_points=("180 degrees",),
            hint="They are supplementary.",
            options=("180°", "90°", "360°"),
            correct_index=0,
        ),
    ),
)


MATH_T2_U5_L6 = LessonData(
    id="math_t2_u5_l6",
    source_id="math_prep3_t2",
    unit_id="t2_u5",
    title="The Relation Between the Tangents of a Circle",
    source_pages="Second Term book pages 93–99",
    objectives=(
        "Understand tangent segments drawn from an external point.",
        "Use equality of tangent lengths from the same external point.",
        "Apply radius-tangent perpendicularity and tangent geometry.",
    ),
    key_terms=("tangent", "point of tangency", "external point", "tangent segment", "radius"),
    evidence_summary=(
        "A radius drawn to a point of tangency is perpendicular to the tangent.",
        "Tangent segments drawn from the same external point to a circle are equal in length.",
        "The lesson applies these properties to geometric calculations and proofs involving triangles and quadrilaterals.",
    ),
    checks=(
        LessonCheck(
            id="equal_tangents",
            prompt="Two tangents are drawn from the same external point to a circle. How do their lengths compare?",
            expected_points=("they are equal",),
            hint="This is the main tangent-segment theorem in the lesson.",
            options=(
                "They are equal.",
                "One is always twice the other.",
                "Their lengths cannot be compared.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U5_L7 = LessonData(
    id="math_t2_u5_l7",
    source_id="math_prep3_t2",
    unit_id="t2_u5",
    title="Angle of Tangency",
    source_pages="Second Term book pages 100–103",
    objectives=(
        "Understand the angle formed by a tangent and a chord.",
        "Relate an angle of tangency to the inscribed angle standing on the same arc/chord.",
        "Use tangent-angle relationships in circle problems.",
    ),
    key_terms=("angle of tangency", "tangent", "chord", "inscribed angle", "alternate segment"),
    evidence_summary=(
        "The lesson studies the angle between a tangent and a chord through the point of tangency.",
        "That angle is related to the inscribed angle standing on the corresponding arc/chord in the circle.",
        "The relationship is used to calculate unknown angles and prove geometric results.",
    ),
    checks=(
        LessonCheck(
            id="tangent_chord",
            prompt="Which angle is related to the angle between a tangent and a chord in this lesson?",
            expected_points=("the inscribed angle subtended by the same chord or arc",),
            hint="Look for the matching angle inside the circle.",
            options=(
                "The inscribed angle subtended by the same chord/arc.",
                "Only the central angle of an unrelated arc.",
                "No angle in the circle is related to it.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_UNIT5_LESSONS = (
    MATH_T2_U5_L1,
    MATH_T2_U5_L2,
    MATH_T2_U5_L3,
    MATH_T2_U5_L4,
    MATH_T2_U5_L5,
    MATH_T2_U5_L6,
    MATH_T2_U5_L7,
)
