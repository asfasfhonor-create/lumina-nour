from lumina.learning.lesson_models import LessonCheck, LessonData


ICT_C3_L1 = LessonData(
    id="ict_c3_l1",
    source_id="ict_prep3_t2",
    unit_id="c3",
    title="For Next",
    source_pages="PDF pages 33–39",
    objectives=(
        "Understand iterative loops.",
        "Use For...Next when the number of repetitions is known.",
        "Trace counter start, end, and Step values.",
    ),
    key_terms=("loop", "For...Next", "counter", "start value", "end value", "Step"),
    evidence_summary=(
        "For...Next repeats code for a controlled number of times.",
        "The counter has a start value, end value, and optional Step increment.",
        "A negative Step is used when counting down, and decimal counters require an appropriate numeric type.",
    ),
    checks=(
        LessonCheck(
            id="for_next_use",
            prompt="When is For...Next most suitable?",
            expected_points=("when the number or range of repetitions is known",),
            hint="The chapter calls it a limited loop.",
            options=(
                "When the repetition range is known.",
                "Only when no repetition is needed.",
                "Only for text constants.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C3_L2 = LessonData(
    id="ict_c3_l2",
    source_id="ict_prep3_t2",
    unit_id="c3",
    title="Do While",
    source_pages="PDF pages 39–42",
    objectives=(
        "Understand indefinite repetition with Do While...Loop.",
        "Repeat code while a condition remains True.",
        "Compare condition-controlled loops with fixed-count loops.",
    ),
    key_terms=("Do While", "Loop", "condition", "indefinite loop"),
    evidence_summary=(
        "Do While...Loop repeats code as long as a condition is True.",
        "It is useful when the number of repetitions is not known in advance.",
        "The loop condition controls when repetition stops.",
    ),
    checks=(
        LessonCheck(
            id="do_while",
            prompt="What controls a Do While...Loop?",
            expected_points=("a condition that remains True",),
            hint="The loop continues while something is true.",
            options=(
                "A condition that is tested for True/False.",
                "Only the variable declaration.",
                "A fixed number that can never change.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C3_L3 = LessonData(
    id="ict_c3_l3",
    source_id="ict_prep3_t2",
    unit_id="c3",
    title="Procedure",
    source_pages="PDF pages 42–45",
    objectives=(
        "Declare and call a Sub procedure.",
        "Use procedures to avoid duplicated code.",
        "Understand Parameters and Arguments.",
    ),
    key_terms=("Sub procedure", "call", "Parameter", "Argument", "code reuse"),
    evidence_summary=(
        "A Sub procedure groups commands under a name and runs them when that name is called.",
        "Procedures help avoid duplicating the same code in multiple places.",
        "Parameters receive values when a procedure is declared, while Arguments are the values supplied when it is called.",
    ),
    checks=(
        LessonCheck(
            id="parameter_argument",
            prompt="What is an Argument in the chapter's terminology?",
            expected_points=("the value passed when calling a procedure",),
            hint="Compare declaration time with call time.",
            options=(
                "A value passed when the procedure is called.",
                "The procedure name only.",
                "A comment line.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C3_L4 = LessonData(
    id="ict_c3_l4",
    source_id="ict_prep3_t2",
    unit_id="c3",
    title="Function",
    source_pages="PDF pages 46–47",
    objectives=(
        "Declare and call a Function.",
        "Understand parameters, return type, and Return value.",
        "Distinguish a Function from a Sub procedure.",
    ),
    key_terms=("Function", "Parameters", "Return", "DataType", "returned value"),
    evidence_summary=(
        "A Function is a named set of commands that can receive parameters and returns a value.",
        "Its declaration specifies a name, parameters, return data type, code, and a Return value.",
        "The chapter contrasts Functions with Sub procedures by emphasizing that a Function returns a value.",
    ),
    checks=(
        LessonCheck(
            id="function_feature",
            prompt="What is the key feature of a Function highlighted in the chapter?",
            expected_points=("it returns a value",),
            hint="Look at the Return statement.",
            options=(
                "It returns a value.",
                "It cannot receive parameters.",
                "It is only a comment.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_CHAPTER3_LESSONS = (
    ICT_C3_L1,
    ICT_C3_L2,
    ICT_C3_L3,
    ICT_C3_L4,
)
