from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_T2_U2_L1 = LessonData(
    id="math_t2_u2_l1",
    source_id="math_prep3_t2",
    unit_id="t2_u2",
    title="Set of Zeroes of a Polynomial Function",
    source_pages="Second Term book pages 15–16",
    objectives=(
        "Understand the set of zeroes of a polynomial function.",
        "Find values of x for which f(x)=0.",
        "Connect zeroes with factorized polynomial forms.",
    ),
    key_terms=("polynomial function", "zero", "set of zeroes", "factor"),
    evidence_summary=(
        "A zero of a polynomial function is a value of x for which the function value equals zero.",
        "The lesson finds zeroes by solving f(x)=0 and uses factorized forms in worked examples.",
        "The set of all such values is the set of zeroes of the function.",
    ),
    checks=(
        LessonCheck(
            id="zero_definition",
            prompt="What does it mean for a number a to be a zero of f?",
            expected_points=("f(a)=0",),
            hint="Substitute a into the function.",
            options=("f(a)=0", "f(a)=a always", "f(a)=1 always"),
            correct_index=0,
        ),
    ),
)


MATH_T2_U2_L2 = LessonData(
    id="math_t2_u2_l2",
    source_id="math_prep3_t2",
    unit_id="t2_u2",
    title="Algebraic Rational Function",
    source_pages="Second Term book pages 17–19",
    objectives=(
        "Recognize algebraic rational functions.",
        "Determine the domain by excluding values that make denominators zero.",
        "Simplify rational expressions while respecting domain restrictions.",
    ),
    key_terms=("algebraic rational function", "domain", "denominator", "common factor", "simplest form"),
    evidence_summary=(
        "An algebraic rational function contains a polynomial numerator and denominator.",
        "Values that make the denominator zero are excluded from the domain.",
        "Common factors may be cancelled in simplification, but the original excluded values remain outside the domain.",
    ),
    checks=(
        LessonCheck(
            id="rational_domain",
            prompt="Which values must be excluded from the domain of an algebraic rational function?",
            expected_points=("values that make the denominator zero",),
            hint="Division by zero is not allowed.",
            options=(
                "Values that make the denominator zero.",
                "All positive values.",
                "All values that make the numerator zero.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U2_L3 = LessonData(
    id="math_t2_u2_l3",
    source_id="math_prep3_t2",
    unit_id="t2_u2",
    title="Equality of Two Algebraic Fractions",
    source_pages="Second Term book pages 20–23",
    objectives=(
        "Reduce algebraic fractions to simplest form.",
        "Determine when two algebraic fractions are equal.",
        "Preserve domain restrictions while transforming fractions.",
    ),
    key_terms=("algebraic fraction", "equivalent fractions", "simplest form", "domain"),
    evidence_summary=(
        "The lesson reduces algebraic fractions by factoring and cancelling common factors where allowed.",
        "Two algebraic fractions can represent the same function on their common valid domain after simplification.",
        "Domain restrictions must still be respected after cancellation.",
    ),
    checks=(
        LessonCheck(
            id="cancel_condition",
            prompt="When cancelling a common algebraic factor from numerator and denominator, what must still be remembered?",
            expected_points=("values excluded from the original denominator remain excluded",),
            hint="Simplifying the expression does not erase the original domain restriction.",
            options=(
                "Original denominator restrictions must still be respected.",
                "Every excluded value becomes allowed.",
                "The numerator can never be factored.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U2_L4 = LessonData(
    id="math_t2_u2_l4",
    source_id="math_prep3_t2",
    unit_id="t2_u2",
    title="Operations on Algebraic Fractions",
    source_pages="Second Term book pages 24–28",
    objectives=(
        "Add and subtract algebraic fractions using a common denominator.",
        "Multiply and divide algebraic fractions.",
        "Simplify results and identify domain restrictions.",
    ),
    key_terms=("common denominator", "addition", "subtraction", "multiplication", "division", "reciprocal"),
    evidence_summary=(
        "Addition and subtraction require a common denominator before numerators are combined.",
        "Multiplication multiplies numerators and denominators and simplifies common factors where valid.",
        "Division is performed by multiplying by the reciprocal of the second fraction, with relevant domain restrictions preserved.",
    ),
    checks=(
        LessonCheck(
            id="division_fraction",
            prompt="How is division by an algebraic fraction performed?",
            expected_points=("multiply by the reciprocal",),
            hint="Use the same idea as dividing ordinary fractions.",
            options=(
                "Multiply by the reciprocal of the divisor.",
                "Add the denominators.",
                "Multiply only the numerators and ignore denominators.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_UNIT2_LESSONS = (
    MATH_T2_U2_L1,
    MATH_T2_U2_L2,
    MATH_T2_U2_L3,
    MATH_T2_U2_L4,
)
