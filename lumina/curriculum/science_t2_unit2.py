from lumina.learning.lesson_models import LessonCheck, LessonData


SCIENCE_T2_U2_L1 = LessonData(
    id="science_t2_u2_l1",
    source_id="science_prep3_t2",
    unit_id="t2_u2",
    title="Physical Properties of the Electric Current",
    source_pages="Second Term book pages 98–105",
    objectives=(
        "Understand electric current intensity and its unit.",
        "Understand potential difference and its unit.",
        "Recognize electric resistance and factors affecting it.",
        "Apply Ohm's law.",
    ),
    key_terms=("electric current intensity", "ampere", "potential difference", "volt", "resistance", "ohm", "Ohm's law"),
    evidence_summary=(
        "Current intensity is the quantity of electric charge passing a cross-section per unit time and is measured in amperes.",
        "Potential difference represents the work needed to transfer electric charge between two points and is measured in volts.",
        "Resistance opposes electric current and depends on factors such as conductor material, length, cross-sectional area, and temperature.",
        "Ohm's law relates potential difference, current intensity, and resistance as V = I × R under the stated conditions.",
    ),
    checks=(
        LessonCheck(
            id="ohm_law",
            prompt="Which equation represents Ohm's law in the lesson?",
            expected_points=("V equals I times R",),
            hint="Potential difference equals current multiplied by resistance.",
            options=("V = I × R", "I = V × R", "R = V × I only"),
            correct_index=0,
        ),
        LessonCheck(
            id="current_unit",
            prompt="What is the unit of electric current intensity?",
            expected_points=("ampere",),
            hint="It is measured using an ammeter.",
            options=("Volt", "Ampere", "Ohm"),
            correct_index=1,
        ),
    ),
)


SCIENCE_T2_U2_L2 = LessonData(
    id="science_t2_u2_l2",
    source_id="science_prep3_t2",
    unit_id="t2_u2",
    title="The Electric Current and Cells",
    source_pages="Second Term book pages 106–110",
    objectives=(
        "Distinguish direct and alternating electric current.",
        "Understand common electric-cell connections.",
        "Relate series and parallel cell connections to electromotive force.",
    ),
    key_terms=("direct current", "alternating current", "electric cell", "electromotive force", "series connection", "parallel connection"),
    evidence_summary=(
        "Direct current flows in one direction, while alternating current changes direction periodically.",
        "Electric cells can be connected in series or in parallel.",
        "In series, electromotive forces add; in parallel identical cells maintain the same electromotive force while increasing the available current capacity.",
    ),
    checks=(
        LessonCheck(
            id="dc_ac",
            prompt="What is the main difference between direct current and alternating current?",
            expected_points=("direct current has one direction; alternating current changes direction",),
            hint="Think about the direction of charge flow over time.",
            options=(
                "Direct current flows in one direction; alternating current changes direction.",
                "Both always change direction in exactly the same way.",
                "Direct current has no charge movement.",
            ),
            correct_index=0,
        ),
    ),
)


SCIENCE_T2_U2_L3 = LessonData(
    id="science_t2_u2_l3",
    source_id="science_prep3_t2",
    unit_id="t2_u2",
    title="Radioactivity and Nuclear Energy",
    source_pages="Second Term book pages 111–117",
    objectives=(
        "Understand radioactive decay at the curriculum level.",
        "Distinguish natural from artificial radioactivity.",
        "Identify peaceful applications of nuclear energy.",
        "Recognize health and environmental risks and radiation-protection principles.",
    ),
    key_terms=("radioactivity", "radioactive decay", "natural radioactivity", "artificial radioactivity", "nuclear energy", "radiation protection"),
    evidence_summary=(
        "Radioactivity is presented as spontaneous change in unstable nuclei accompanied by radiation.",
        "The lesson distinguishes natural and artificial radioactivity.",
        "Peaceful applications include medicine, agriculture, industry, power generation, space uses, and other technological applications.",
        "The lesson also emphasizes harmful biological/environmental effects and protection principles such as reducing exposure time, increasing distance, and using suitable shielding.",
    ),
    checks=(
        LessonCheck(
            id="radiation_protection",
            prompt="Which action is consistent with radiation-protection principles in the lesson?",
            expected_points=("reduce time, increase distance, use shielding",),
            hint="Think about exposure time, distance, and barriers.",
            options=(
                "Increase exposure time whenever possible.",
                "Reduce exposure time, increase distance, and use suitable shielding.",
                "Remove all shielding.",
            ),
            correct_index=1,
        ),
    ),
)


SCIENCE_T2_UNIT2_LESSONS = (
    SCIENCE_T2_U2_L1,
    SCIENCE_T2_U2_L2,
    SCIENCE_T2_U2_L3,
)
