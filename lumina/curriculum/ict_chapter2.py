from lumina.learning.lesson_models import LessonCheck, LessonData


ICT_C2_L1 = LessonData(
    id="ict_c2_l1",
    source_id="ict_prep3_t2",
    unit_id="c2",
    title="If Then",
    source_pages="PDF pages 22–24",
    objectives=(
        "Understand conditional expressions and True/False results.",
        "Use If...Then for one-way branching.",
        "Connect branching code with flowchart logic.",
    ),
    key_terms=("If...Then", "conditional expression", "True", "False", "branching", "logical operator"),
    evidence_summary=(
        "A conditional expression compares values or expressions and evaluates to True or False.",
        "If...Then executes a block of code when the condition is True.",
        "The chapter explicitly connects branching code to equivalent flowchart decisions.",
    ),
    checks=(
        LessonCheck(
            id="if_then_behavior",
            prompt="What happens in an If...Then statement when the condition is True?",
            expected_points=("the code inside the branch executes",),
            hint="Think about the True path in the flowchart.",
            options=(
                "The code inside the If block executes.",
                "The program must always stop.",
                "The condition is ignored.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C2_L2 = LessonData(
    id="ict_c2_l2",
    source_id="ict_prep3_t2",
    unit_id="c2",
    title="If Then Else",
    source_pages="PDF pages 24–25",
    objectives=(
        "Use If...Then...Else for two-way branching.",
        "Distinguish the code executed for True and False conditions.",
        "Apply branching to examples such as even/odd decisions.",
    ),
    key_terms=("If...Then...Else", "Else", "True branch", "False branch", "Mod"),
    evidence_summary=(
        "If...Then...Else chooses between one code block when the condition is True and another when it is False.",
        "The chapter uses the Mod operator to test whether a number is even or odd.",
        "Branching can be represented in code and flowcharts.",
    ),
    checks=(
        LessonCheck(
            id="else_branch",
            prompt="When does the Else block run?",
            expected_points=("when the If condition is False",),
            hint="Else is the alternative branch.",
            options=(
                "When the If condition is False.",
                "Only when the condition is True.",
                "Before the condition is tested.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_C2_L3 = LessonData(
    id="ict_c2_l3",
    source_id="ict_prep3_t2",
    unit_id="c2",
    title="Select Case",
    source_pages="PDF pages 26–28",
    objectives=(
        "Understand when Select...Case is useful.",
        "Use Select...Case for multiple branches based on one variable.",
        "Recognize Case Else as a fallback branch.",
    ),
    key_terms=("Select Case", "Case", "Case Else", "multiple branching", "variable"),
    evidence_summary=(
        "Select...Case is used when branching depends on the value of one variable and there are many possible conditions.",
        "It can make multi-branch code shorter and clearer.",
        "Case Else provides a fallback when no listed case matches.",
    ),
    checks=(
        LessonCheck(
            id="select_case_use",
            prompt="When is Select...Case especially useful?",
            expected_points=("many branches based on one variable",),
            hint="Compare it with many repeated If conditions.",
            options=(
                "When there are many branches based on one variable.",
                "Only when there is no condition at all.",
                "Only for declaring variables.",
            ),
            correct_index=0,
        ),
    ),
)

ICT_CHAPTER2_LESSONS = (
    ICT_C2_L1,
    ICT_C2_L2,
    ICT_C2_L3,
)
