from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_U1_L1 = LessonData(
    id="math_u1_l1",
    source_id="math_prep3_t1",
    unit_id="u1",
    title="Cartesian Product",
    source_pages="PDF pages 8–13",
    objectives=(
        "Understand ordered pairs and projections.",
        "Form the Cartesian product of two non-empty sets.",
        "Represent ordered pairs using Cartesian and arrow diagrams.",
    ),
    key_terms=("ordered pair", "Cartesian product", "first projection", "second projection", "Cartesian diagram", "arrow diagram"),
    evidence_summary=(
        "An ordered pair (a, b) has a first projection a and a second projection b.",
        "In general, (a, b) is not equal to (b, a) unless the two components are equal.",
        "The Cartesian product combines elements of two sets as ordered pairs and can be represented in diagrams.",
    ),
    checks=(
        LessonCheck(
            id="ordered_pair_order",
            prompt="Which statement is correct about ordered pairs?",
            expected_points=("order matters",),
            hint="Compare (a, b) with (b, a).",
            options=(
                "(a, b) is always equal to (b, a).",
                "The order of the two components matters in an ordered pair.",
                "An ordered pair has only one component.",
            ),
            correct_index=1,
        ),
    ),
)

MATH_U1_L2 = LessonData(
    id="math_u1_l2",
    source_id="math_prep3_t1",
    unit_id="u1",
    title="Relations",
    source_pages="PDF pages 14–16",
    objectives=(
        "Understand a relation from one set to another.",
        "Represent a relation by ordered pairs, arrow diagrams, and Cartesian diagrams.",
        "Connect relation notation with subsets of a Cartesian product.",
    ),
    key_terms=("relation", "ordered pairs", "arrow diagram", "Cartesian diagram", "subset"),
    evidence_summary=(
        "A relation connects selected elements of one set with selected elements of another.",
        "A relation can be written as a set of ordered pairs and represented with arrow or Cartesian diagrams.",
        "A relation from X to Y is treated as a subset of the Cartesian product X × Y.",
    ),
    checks=(
        LessonCheck(
            id="relation_subset",
            prompt="A relation from X to Y is best described as what?",
            expected_points=("subset of the Cartesian product",),
            hint="Think about which ordered pairs are selected from all possible pairs.",
            options=(
                "A subset of X × Y.",
                "Every element of X only.",
                "Every element of Y only.",
            ),
            correct_index=0,
        ),
    ),
)

MATH_U1_L3 = LessonData(
    id="math_u1_l3",
    source_id="math_prep3_t1",
    unit_id="u1",
    title="Functions (Mapping)",
    source_pages="PDF pages 17–19",
    objectives=(
        "Understand the concept of a function.",
        "Recognize domain, codomain, and range.",
        "Use symbolic function notation.",
    ),
    key_terms=("function", "domain", "codomain", "range", "mapping", "image"),
    evidence_summary=(
        "A relation from X to Y is a function when each element of X appears only once as a first projection in the relation.",
        "The lesson introduces domain, codomain, range, and symbolic function notation.",
        "Function diagrams help distinguish mappings that satisfy the function condition from those that do not.",
    ),
    checks=(
        LessonCheck(
            id="function_condition",
            prompt="Which condition is required for a relation from X to Y to be a function?",
            expected_points=("each element of X maps to only one element of Y",),
            hint="Look at the definition on the Functions (Mapping) page.",
            options=(
                "Each element of X is connected to only one element of Y.",
                "Every element of Y must connect to every element of X.",
                "One element of X must connect to several elements of Y.",
            ),
            correct_index=0,
        ),
    ),
)

MATH_U1_L4 = LessonData(
    id="math_u1_l4",
    source_id="math_prep3_t1",
    unit_id="u1",
    title="Polynomial Functions",
    source_pages="PDF pages 20–24",
    objectives=(
        "Recognize polynomial functions.",
        "Determine the degree of a polynomial from the highest power.",
        "Connect linear and quadratic functions with graphical representation.",
    ),
    key_terms=("polynomial function", "degree", "linear function", "quadratic function", "graphical representation"),
    evidence_summary=(
        "A polynomial function is expressed as a finite sum of powers of x with real coefficients.",
        "The degree of the polynomial is the highest power of the variable with a non-zero coefficient.",
        "The lesson develops linear and quadratic polynomial functions and their graphical representations.",
    ),
    checks=(
        LessonCheck(
            id="degree",
            prompt="How is the degree of a polynomial determined?",
            expected_points=("highest power of the variable with non-zero coefficient",),
            hint="Look at the definition under Polynomial functions.",
            options=(
                "By the number of terms only.",
                "By the highest power of the variable with a non-zero coefficient.",
                "By the value of x.",
            ),
            correct_index=1,
        ),
    ),
)

MATH_UNIT1_LESSONS = (
    MATH_U1_L1,
    MATH_U1_L2,
    MATH_U1_L3,
    MATH_U1_L4,
)
