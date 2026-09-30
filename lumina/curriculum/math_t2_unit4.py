from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_T2_U4_L1 = LessonData(
    id="math_t2_u4_l1",
    source_id="math_prep3_t2",
    unit_id="t2_u4",
    title="Basic Definitions and Concepts",
    source_pages="Second Term book pages 39–45",
    objectives=(
        "Identify basic circle parts and terms.",
        "Understand radius, chord, diameter, arc, sector, and symmetry.",
        "Use fundamental circle relationships in simple problems.",
    ),
    key_terms=("circle", "centre", "radius", "chord", "diameter", "arc", "sector", "symmetry"),
    evidence_summary=(
        "A circle is determined by a centre and a fixed radius.",
        "A chord joins two points on the circle, while a diameter is a chord passing through the centre.",
        "The lesson introduces arcs, sectors, and symmetry properties of the circle.",
    ),
    checks=(
        LessonCheck(
            id="diameter",
            prompt="What distinguishes a diameter from any other chord?",
            expected_points=("it passes through the centre",),
            hint="Every diameter is a chord, but with one extra condition.",
            options=(
                "It passes through the centre of the circle.",
                "It never touches the circle.",
                "It is always shorter than the radius.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U4_L2 = LessonData(
    id="math_t2_u4_l2",
    source_id="math_prep3_t2",
    unit_id="t2_u4",
    title="Positions of a Point, a Straight Line and a Circle with Respect to a Circle",
    source_pages="Second Term book pages 46–53",
    objectives=(
        "Classify the position of a point relative to a circle.",
        "Classify a straight line as secant, tangent, or external.",
        "Classify the relative positions of two circles using radii and centre distance.",
    ),
    key_terms=("inside", "on the circle", "outside", "secant", "tangent", "external line", "intersecting circles", "tangent circles"),
    evidence_summary=(
        "A point is inside, on, or outside a circle according to how its distance from the centre compares with the radius.",
        "A line may intersect a circle at two points (secant), one point (tangent), or no points.",
        "The relative position of two circles depends on the distance between their centres compared with the sum and difference of their radii.",
    ),
    checks=(
        LessonCheck(
            id="tangent_line",
            prompt="How many common points does a tangent line have with a circle?",
            expected_points=("one",),
            hint="A secant has two; a tangent just touches.",
            options=("One", "Two", "None"),
            correct_index=0,
        ),
    ),
)


MATH_T2_U4_L3 = LessonData(
    id="math_t2_u4_l3",
    source_id="math_prep3_t2",
    unit_id="t2_u4",
    title="Identifying the Circle",
    source_pages="Second Term book pages 54–57",
    objectives=(
        "Construct/identify a circle through three non-collinear points.",
        "Use perpendicular bisectors to locate the centre.",
        "Connect triangle constructions with circumcircles.",
    ),
    key_terms=("circumcircle", "circumcenter", "perpendicular bisector", "three non-collinear points"),
    evidence_summary=(
        "Three non-collinear points determine one circle.",
        "The centre is found at the intersection of perpendicular bisectors of suitable chords/triangle sides.",
        "The lesson applies this idea to the circumcircle of a triangle.",
    ),
    checks=(
        LessonCheck(
            id="three_points",
            prompt="How many circles pass through three non-collinear points?",
            expected_points=("one",),
            hint="The perpendicular bisectors meet at one centre.",
            options=("Exactly one", "Infinitely many", "None"),
            correct_index=0,
        ),
    ),
)


MATH_T2_U4_L4 = LessonData(
    id="math_t2_u4_l4",
    source_id="math_prep3_t2",
    unit_id="t2_u4",
    title="The Relation Between the Chords of a Circle and Its Center",
    source_pages="Second Term book pages 58–62",
    objectives=(
        "Relate equal chords to their distances from the centre.",
        "Use perpendicular lines from the centre to chords.",
        "Apply chord-centre relationships in geometric proofs.",
    ),
    key_terms=("chord", "centre", "equal chords", "distance from centre", "perpendicular"),
    evidence_summary=(
        "Equal chords in the same circle are at equal distances from the centre, and conversely.",
        "A perpendicular from the centre to a chord bisects that chord.",
        "The lesson uses these relationships to solve and prove circle problems.",
    ),
    checks=(
        LessonCheck(
            id="perpendicular_chord",
            prompt="What happens when a perpendicular is drawn from the centre of a circle to a chord?",
            expected_points=("it bisects the chord",),
            hint="The centre-to-chord perpendicular creates two equal chord parts.",
            options=(
                "It bisects the chord.",
                "It doubles the chord.",
                "It makes the radius zero.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_UNIT4_LESSONS = (
    MATH_T2_U4_L1,
    MATH_T2_U4_L2,
    MATH_T2_U4_L3,
    MATH_T2_U4_L4,
)
