from lumina.learning.lesson_models import LessonCheck, LessonData


MATH_T2_U1_L1 = LessonData(
    id="math_t2_u1_l1",
    source_id="math_prep3_t2",
    unit_id="t2_u1",
    title="Solving Two Equations of First Degrees in Two Variables Graphically and Algebraically",
    source_pages="Second Term book pages 5–9",
    objectives=(
        "Solve a system of two linear equations in two variables graphically.",
        "Interpret intersection of two straight lines as the common solution.",
        "Solve the same type of system algebraically.",
    ),
    key_terms=("linear equation", "system of equations", "graphical solution", "algebraic solution", "intersection"),
    evidence_summary=(
        "The lesson represents each first-degree equation as a straight line.",
        "The common solution of the two equations is the point of intersection of their graphs when such a point exists.",
        "It also solves systems algebraically using substitution/elimination-style transformations shown in the worked examples.",
    ),
    checks=(
        LessonCheck(
            id="graph_solution",
            prompt="Graphically, what represents the common solution of two linear equations in two variables?",
            expected_points=("the intersection point of the two lines",),
            hint="Each equation is drawn as a straight line.",
            options=(
                "The point where the two lines intersect.",
                "Any point on the x-axis.",
                "The midpoint of one line segment.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U1_L2 = LessonData(
    id="math_t2_u1_l2",
    source_id="math_prep3_t2",
    unit_id="t2_u1",
    title="Solving an Equation of Second Degree in One Unknown Graphically and Algebraically",
    source_pages="Second Term book pages 10–12",
    objectives=(
        "Solve a quadratic equation graphically.",
        "Interpret roots as x-coordinates where the graph meets the x-axis.",
        "Solve quadratic equations algebraically using the methods presented in the book.",
    ),
    key_terms=("quadratic equation", "root", "graphical solution", "algebraic solution", "parabola"),
    evidence_summary=(
        "A second-degree equation can be linked to the graph of a quadratic function.",
        "Graphical roots are read from the x-values where the graph intersects the x-axis.",
        "The worked examples also show algebraic solution methods and checking of roots.",
    ),
    checks=(
        LessonCheck(
            id="quadratic_root_graph",
            prompt="On the graph of y = f(x), where do the roots of f(x)=0 appear?",
            expected_points=("where the graph meets the x-axis",),
            hint="At a root, y equals zero.",
            options=(
                "Where the graph meets the x-axis.",
                "Where the graph meets the y-axis only.",
                "At every point on the graph.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_U1_L3 = LessonData(
    id="math_t2_u1_l3",
    source_id="math_prep3_t2",
    unit_id="t2_u1",
    title="Solving Two Equations in Two Variables, One First Degree and One Second Degree",
    source_pages="Second Term book pages 13–14",
    objectives=(
        "Solve a system containing one linear and one quadratic equation.",
        "Use substitution to reduce the system to one equation in one unknown.",
        "Interpret possible multiple solutions.",
    ),
    key_terms=("linear equation", "quadratic equation", "substitution", "system", "solution pair"),
    evidence_summary=(
        "The lesson combines a first-degree equation and a second-degree equation in two variables.",
        "One variable is expressed using the linear equation and substituted into the quadratic equation.",
        "The resulting roots produce one or more ordered-pair solutions depending on the system.",
    ),
    checks=(
        LessonCheck(
            id="mixed_system",
            prompt="What is a useful first step when solving a linear-quadratic system algebraically?",
            expected_points=("express one variable from the linear equation and substitute",),
            hint="Use the simpler first-degree equation to reduce the number of variables.",
            options=(
                "Express one variable from the linear equation and substitute it into the quadratic equation.",
                "Ignore the linear equation.",
                "Multiply every term by zero.",
            ),
            correct_index=0,
        ),
    ),
)


MATH_T2_UNIT1_LESSONS = (
    MATH_T2_U1_L1,
    MATH_T2_U1_L2,
    MATH_T2_U1_L3,
)
