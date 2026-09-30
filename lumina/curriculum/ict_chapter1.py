from lumina.learning.lesson_models import LessonCheck, LessonData


ICT_C1_L1 = LessonData(
    id="ict_c1_l1",
    source_id="ict_prep3_t2",
    unit_id="c1",
    title="Data Types",
    source_pages="PDF pages 6–7",
    objectives=(
        "Understand why programs need different data types.",
        "Recognize common data-type categories used in the supplied Visual Basic .NET curriculum.",
        "Connect a value with an appropriate type.",
    ),
    key_terms=("data", "data type", "Integer", "String", "Boolean", "Visual Basic .NET"),
    evidence_summary=(
        "The chapter begins by introducing data and the idea that programming values have types.",
        "Different data types are used for different kinds of values, such as numbers, text, and logical values.",
        "The supplied school material teaches these ideas using Visual Basic .NET terminology.",
    ),
    checks=(
        LessonCheck(
            id="type_purpose",
            prompt="Why do programs use different data types?",
            expected_points=("different kinds of values need suitable representations",),
            hint="Think about numbers, text, and True/False values.",
            options=(
                "Because every value must be stored in exactly the same way.",
                "Because different kinds of values need suitable representations and operations.",
                "Only to change the color of the program.",
            ),
            correct_index=1,
        ),
    ),
)

ICT_C1_L2 = LessonData(
    id="ict_c1_l2",
    source_id="ict_prep3_t2",
    unit_id="c1",
    title="Constants and Variables",
    source_pages="PDF pages 7–12",
    objectives=(
        "Distinguish constants from variables.",
        "Understand declaration and naming ideas in the supplied curriculum.",
        "Recognize that variable values can change while constants remain fixed.",
    ),
    key_terms=("constant", "variable", "declaration", "identifier", "value"),
    evidence_summary=(
        "The chapter distinguishes fixed values from values that may change while a program runs.",
        "Variables are associated with names and data types so that programs can store and manipulate values.",
        "Constants are used for values that should remain unchanged.",
    ),
    checks=(
        LessonCheck(
            id="constant_variable",
            prompt="Which statement correctly distinguishes a variable from a constant?",
            expected_points=("variable can change while constant remains fixed",),
            hint="Focus on whether the stored value is allowed to change.",
            options=(
                "A variable can change value, while a constant is intended to stay fixed.",
                "A constant always changes and a variable never changes.",
                "They have no difference.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C1_L3 = LessonData(
    id="ict_c1_l3",
    source_id="ict_prep3_t2",
    unit_id="c1",
    title="Assignment Statement",
    source_pages="PDF pages 12–13",
    objectives=(
        "Understand the role of an assignment statement.",
        "Trace how a value is placed into a variable.",
        "Distinguish assignment from a comparison in programming context.",
    ),
    key_terms=("assignment", "variable", "expression", "value"),
    evidence_summary=(
        "The chapter introduces assignment as the operation that gives a variable a value.",
        "The value assigned may come directly from a literal value or from an expression.",
        "Following assignments step by step is important for understanding program state.",
    ),
    checks=(
        LessonCheck(
            id="assignment_meaning",
            prompt="What does an assignment statement do?",
            expected_points=("stores or places a value in a variable",),
            hint="Think about changing the current value held by a variable.",
            options=(
                "It stores or places a value in a variable.",
                "It always ends the program.",
                "It changes a variable into a constant automatically.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C1_L4 = LessonData(
    id="ict_c1_l4",
    source_id="ict_prep3_t2",
    unit_id="c1",
    title="Operator Precedence",
    source_pages="PDF pages 13–15",
    objectives=(
        "Understand that arithmetic operators are evaluated in a defined order.",
        "Trace expressions using operator precedence.",
        "Use parentheses when a different order is required.",
    ),
    key_terms=("operator", "precedence", "expression", "parentheses"),
    evidence_summary=(
        "Arithmetic expressions are not evaluated only from left to right; operators have an order of precedence.",
        "Parentheses can be used to make the intended order explicit.",
        "Tracing expressions carefully helps avoid programming mistakes.",
    ),
    checks=(
        LessonCheck(
            id="precedence",
            prompt="Why are parentheses useful in an arithmetic expression?",
            expected_points=("they control or clarify evaluation order",),
            hint="Think about which operation should happen first.",
            options=(
                "They can control or clarify the order in which operations are evaluated.",
                "They turn every number into text.",
                "They remove all operators.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C1_L5 = LessonData(
    id="ict_c1_l5",
    source_id="ict_prep3_t2",
    unit_id="c1",
    title="Errors",
    source_pages="PDF pages 15–16",
    objectives=(
        "Recognize that programs can contain different kinds of errors.",
        "Use error messages and careful tracing to locate mistakes.",
        "Develop a debugging mindset instead of guessing.",
    ),
    key_terms=("error", "syntax", "runtime", "logic", "debugging"),
    evidence_summary=(
        "The chapter closes by discussing errors that can occur while writing or running programs.",
        "Finding an error requires examining the code, the program behavior, and any available error message.",
        "Debugging is a process of identifying and correcting the cause rather than randomly changing code.",
    ),
    checks=(
        LessonCheck(
            id="debugging",
            prompt="What is the best first attitude when a program has an error?",
            expected_points=("inspect the code and evidence systematically",),
            hint="Debugging is investigation, not random guessing.",
            options=(
                "Change many lines randomly until something happens.",
                "Inspect the code and available evidence systematically to locate the cause.",
                "Delete the whole program immediately.",
            ),
            correct_index=1,
        ),
    ),
)

ICT_CHAPTER1_LESSONS = (
    ICT_C1_L1,
    ICT_C1_L2,
    ICT_C1_L3,
    ICT_C1_L4,
    ICT_C1_L5,
)
